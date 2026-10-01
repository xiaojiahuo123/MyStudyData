# -*- coding: utf-8 -*-
"""
把 AI 生成 PPT 里的占位装饰图，替换为赫斯曼 / 东土 / 和利时的真实界面截图。
策略：保留原有形状的位置、大小、层级，只替换图片内容（按目标框比例做 cover 裁剪）。
"""
import os
import io
from collections import defaultdict

from PIL import Image
from pptx import Presentation
from pptx.oxml.ns import qn
from pptx.util import Emu

SRC_DIR = r"E:\Code\MyStudyData\3、网络安全\赫斯曼\images"
PPTX_IN = r"E:\Code\MyStudyData\hs_training.pptx"
PPTX_OUT = r"E:\Code\MyStudyData\hs_training_with_images.pptx"

EMU_INCH = 914400
MIN_PX, MAX_PX, DPI = 900, 2600, 200
JPEG_Q = 84

# (slide_index, 该页第几个大图位) -> [截图文件名...]
# 宽幅位会横向拼接，竖幅位会纵向拼接，方形位单张 cover 裁剪
MAPPING = {
    (0, 0): ["Snipaste_2026-09-06_15-44-47.png", "Snipaste_2026-09-06_19-01-27.png"],
    (3, 0): ["Snipaste_2026-09-06_19-01-05.png"],
    (3, 1): ["Snipaste_2026-09-06_19-01-27.png"],
    (3, 2): ["Snipaste_2026-09-06_19-02-13.png"],
    (4, 0): ["Snipaste_2026-09-06_19-01-34.png", "Snipaste_2026-09-06_19-01-44.png"],
    (5, 0): ["Snipaste_2026-09-06_15-44-47.png"],
    (5, 1): ["Snipaste_2026-09-06_19-01-27.png"],
    (5, 2): ["Snipaste_2026-09-06_19-02-28.png"],
    (5, 3): ["Snipaste_2026-09-07_10-21-43.png"],
    (7, 0): ["Snipaste_2026-09-06_15-44-47.png", "Snipaste_2026-09-06_15-47-03.png"],
    (8, 0): ["Snipaste_2026-09-06_15-44-47.png"],
    (8, 1): ["Snipaste_2026-09-06_15-47-03.png"],
    (10, 0): ["Snipaste_2026-09-06_15-47-03.png", "Snipaste_2026-09-06_19-03-42.png"],
    (10, 1): ["Snipaste_2026-09-06_19-04-02.png", "Snipaste_2026-09-06_19-03-53.png"],
    (12, 0): ["Snipaste_2026-09-06_19-01-27.png", "Snipaste_2026-09-06_19-02-13.png"],
    (13, 0): ["Snipaste_2026-09-06_19-01-05.png"],
    (13, 1): ["Snipaste_2026-09-06_19-02-02.png"],
    (13, 2): ["Snipaste_2026-09-06_19-01-27.png"],
    (14, 0): ["Snipaste_2026-09-06_19-02-13.png", "Snipaste_2026-09-06_19-01-05.png"],
    (15, 0): ["Snipaste_2026-09-06_19-02-13.png"],
    (15, 1): ["Snipaste_2026-09-06_19-02-49.png"],
    (17, 0): ["Snipaste_2026-09-06_19-01-44.png"],
    (17, 1): ["Snipaste_2026-09-06_19-01-53.png"],
    (17, 2): ["Snipaste_2026-09-06_19-01-34.png"],
    (18, 0): ["Snipaste_2026-09-06_19-02-28.png", "Snipaste_2026-09-06_19-01-34.png"],
    (19, 0): ["Snipaste_2026-09-06_19-02-36.png"],
    (19, 1): ["Snipaste_2026-09-06_19-02-54.png"],
    (19, 2): ["Snipaste_2026-09-06_19-03-02.png"],
    (20, 0): ["Snipaste_2026-09-06_19-03-27.png", "Snipaste_2026-09-06_19-03-42.png",
              "Snipaste_2026-09-06_19-04-02.png"],
    (21, 0): ["Snipaste_2026-09-06_19-04-13.png"],
    (21, 1): ["Snipaste_2026-09-06_19-04-29.png"],
    (21, 2): ["Snipaste_2026-09-06_19-04-41.png"],
    (21, 3): ["Snipaste_2026-09-06_19-06-11.png"],
    (23, 0): ["Snipaste_2026-09-06_19-06-25.png"],
    (23, 1): ["Snipaste_2026-09-06_19-06-40.png"],
    (23, 2): ["Snipaste_2026-09-06_19-06-53.png"],
    (25, 0): ["Snipaste_2026-09-07_10-21-43.png", "Snipaste_2026-09-07_11-14-14.png"],
    (26, 0): ["Snipaste_2026-09-07_11-14-14.png"],
    (26, 1): ["Snipaste_2026-09-07_10-21-43.png"],
    (26, 2): ["Snipaste_2026-09-06_19-03-53.png"],
    (28, 0): ["Snipaste_2026-09-06_15-44-47.png", "Snipaste_2026-09-06_15-47-03.png"],
    (29, 0): ["Snipaste_2026-09-06_19-04-53.png"],
    (29, 1): ["Snipaste_2026-09-06_19-05-09.png"],
    (30, 0): ["Snipaste_2026-09-06_19-01-34.png", "Snipaste_2026-09-06_19-01-44.png"],
}

LANCZOS = Image.Resampling.LANCZOS


def cover_crop(img, tw, th):
    """按目标比例居中裁剪后缩放到目标像素"""
    tr, ir = tw / th, img.width / img.height
    if ir > tr:                      # 图偏宽 -> 裁左右
        nw = int(round(img.height * tr))
        left = (img.width - nw) // 2
        img = img.crop((left, 0, left + nw, img.height))
    else:                            # 图偏高 -> 裁上下（偏上对齐，界面信息多在上部）
        nh = int(round(img.width / tr))
        top = int((img.height - nh) * 0.35)
        img = img.crop((0, top, img.width, top + nh))
    return img.resize((tw, th), LANCZOS)


def build_canvas(paths, tw, th):
    """按目标框比例拼接若干截图，再做 cover 裁剪"""
    imgs = [Image.open(os.path.join(SRC_DIR, p)).convert("RGB") for p in paths]
    if len(imgs) == 1:
        return cover_crop(imgs[0], tw, th)

    tr = tw / th
    gap = max(4, tw // 300)
    if tr > 2.2:                     # 宽幅 -> 横向拼接（等高）
        h = int(sum(i.height for i in imgs) / len(imgs))
        imgs = [i.resize((max(1, int(i.width * h / i.height)), h), LANCZOS) for i in imgs]
        cw = sum(i.width for i in imgs) + gap * (len(imgs) - 1)
        canvas = Image.new("RGB", (cw, h), "white")
        x = 0
        for i in imgs:
            canvas.paste(i, (x, 0))
            x += i.width + gap
    else:                            # 竖幅/方幅 -> 纵向拼接（等宽）
        w = int(sum(i.width for i in imgs) / len(imgs))
        imgs = [i.resize((w, max(1, int(i.height * w / i.width))), LANCZOS) for i in imgs]
        ch = sum(i.height for i in imgs) + gap * (len(imgs) - 1)
        canvas = Image.new("RGB", (w, ch), "white")
        y = 0
        for i in imgs:
            canvas.paste(i, (0, y))
            y += i.height + gap
    return cover_crop(canvas, tw, th)


def target_px(w_emu, h_emu):
    """由形状实际英寸大小推导输出像素，兼顾清晰度与文件体积"""
    tw = min(MAX_PX, max(MIN_PX, int(w_emu / EMU_INCH * DPI)))
    th = min(MAX_PX, max(MIN_PX, int(h_emu / EMU_INCH * DPI)))
    return tw, th


def encode(img, fmt):
    buf = io.BytesIO()
    if fmt == "png":
        img.save(buf, "PNG", optimize=True)
    else:
        img.save(buf, "JPEG", quality=JPEG_Q, optimize=True, progressive=True)
    return buf.getvalue()


def main():
    prs = Presentation(PPTX_IN)
    # 统计每个媒体 part 被多少形状引用，避免替换时误伤共享图
    usage = defaultdict(int)
    pic_shapes = {}                       # (slide_idx, pos) -> shape
    for si, slide in enumerate(prs.slides):
        pos = 0
        for sh in slide.shapes:
            if sh.shape_type != 13:
                continue
            if sh.width < 800000 or sh.height < 800000:   # 跳过小图标
                continue
            blip = sh._element.find(".//" + qn("a:blip"))
            rid = blip.get(qn("r:embed"))
            usage[rid] += 1
            pic_shapes[(si, pos)] = sh
            pos += 1

    print(f"可替换大图位: {len(pic_shapes)}  共享引用: "
          f"{[r for r, c in usage.items() if c > 1]}")

    replaced = skipped = 0
    for key, names in MAPPING.items():
        sh = pic_shapes.get(key)
        if sh is None:
            print(f"  ! 未找到图位 {key}")
            skipped += 1
            continue
        for n in names:
            if not os.path.exists(os.path.join(SRC_DIR, n)):
                raise FileNotFoundError(n)

        tw, th = target_px(sh.width, sh.height)
        fmt = "png" if "png" in sh.image.content_type else "jpeg"
        blob = encode(build_canvas(names, tw, th), fmt)

        blip = sh._element.find(".//" + qn("a:blip"))
        rid = blip.get(qn("r:embed"))
        if usage[rid] > 1:
            # 该图被多处引用：新建独立 part，再改指向，避免牵连其它页
            tmp = prs.slides[key[0]].shapes.add_picture(
                io.BytesIO(blob), sh.left, sh.top, sh.width, sh.height)
            new_rid = tmp._element.find(".//" + qn("a:blip")).get(qn("r:embed"))
            blip.set(qn("r:embed"), new_rid)
            tmp._element.getparent().remove(tmp._element)
        else:
            sh.part.related_part(rid)._blob = blob

        # 清掉原图自带的裁剪，避免与新图叠加
        src_rect = sh._element.find(".//" + qn("a:srcRect"))
        if src_rect is not None:
            for a in ("l", "t", "r", "b"):
                if src_rect.get(a):
                    src_rect.set(a, "0")
        replaced += 1
        print(f"  S{key[0]:>2} #{key[1]}  <- {len(names)}张  {names[0][11:19]}")

    prs.save(PPTX_OUT)
    print(f"\n完成: 替换 {replaced} 处, 跳过 {skipped} 处")
    print("输出:", PPTX_OUT, f"{os.path.getsize(PPTX_OUT)/1048576:.1f} MB")


if __name__ == "__main__":
    main()
