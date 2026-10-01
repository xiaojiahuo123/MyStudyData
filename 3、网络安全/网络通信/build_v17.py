# -*- coding: utf-8 -*-
"""
工业网络与 PLC 通信技术培训 PPT —— 知识讲解版 v17
- 依据云端金山文档（file_id=hTLWujy1orM2r4mH6C62rxi3E4nh3BExC，version 17）重建
- 保留用户的全部文字（修正错别字：valn→VLAN、concole→Console）
- 占位页（Slide 4/7/17）保留为规范占位版式，等待用户后续填充
- Slide 5 按图选图注（图是 VLAN 划分截图，图注同步改为 VLAN 划分）
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls
from PIL import Image

IMG_DIR = r"E:\Code\MyStudyData\3、网络安全\网络通信\images"
OUT = r"E:\Code\MyStudyData\3、网络安全\网络通信\工业网络与PLC通信技术培训.pptx"

# 文件名按所在子目录分组
P = {
    # 赫斯曼子目录
    "sys": "赫斯曼/Snipaste_2026-09-06_15-44-47.png",
    "vlan_hs": "赫斯曼/Snipaste_2026-09-06_15-47-03.png",
    # 东土交换机子目录（与原 v4 映射一致）
    "ip1": "东土交换机/Snipaste_2026-09-06_19-01-05.png",
    "dev": "东土交换机/Snipaste_2026-09-06_19-01-27.png",
    "port_st": "东土交换机/Snipaste_2026-09-06_19-01-34.png",
    "port_fl": "东土交换机/Snipaste_2026-09-06_19-01-44.png",
    "sysrun": "东土交换机/Snipaste_2026-09-06_19-01-53.png",
    "ip2": "东土交换机/Snipaste_2026-09-06_19-02-02.png",
    "devset": "东土交换机/Snipaste_2026-09-06_19-02-13.png",
    "portcfg": "东土交换机/Snipaste_2026-09-06_19-02-28.png",
    "pwd": "东土交换机/Snipaste_2026-09-06_19-02-36.png",
    "ver": "东土交换机/Snipaste_2026-09-06_19-02-49.png",
    "upgrade": "东土交换机/Snipaste_2026-09-06_19-02-54.png",
    "cfgbak": "东土交换机/Snipaste_2026-09-06_19-03-02.png",
    "limit": "东土交换机/Snipaste_2026-09-06_19-03-27.png",
    "pvlan": "东土交换机/Snipaste_2026-09-06_19-03-42.png",
    "gvrp": "东土交换机/Snipaste_2026-09-06_19-03-53.png",
    "vlaninfo": "东土交换机/Snipaste_2026-09-06_19-04-02.png",
    "mirror": "东土交换机/Snipaste_2026-09-06_19-04-13.png",
    "mcast": "东土交换机/Snipaste_2026-09-06_19-04-29.png",
    "acl": "东土交换机/Snipaste_2026-09-06_19-04-41.png",
    "arp": "东土交换机/Snipaste_2026-09-06_19-04-53.png",
    "snmp": "东土交换机/Snipaste_2026-09-06_19-05-09.png",
    "portsec": "东土交换机/Snipaste_2026-09-06_19-06-11.png",
    "alarm_st": "东土交换机/Snipaste_2026-09-06_19-06-25.png",
    "alarm_set": "东土交换机/Snipaste_2026-09-06_19-06-40.png",
    "alarm_port": "东土交换机/Snipaste_2026-09-06_19-06-53.png",
    # 根目录 / 补回（autothink 在云端拉回）
    "modbus": "Snipaste_2026-09-07_11-14-14.png",
    "autothink": "holliAS_autothink.png",
    # 新增场景（来自云端新增页）
    "ring_topology": "东土交换机/Snipaste_2026-09-06_19-04-29.png",  # 临时复用 mcast
}

C_PRIMARY = RGBColor(0x1B, 0x4F, 0x72)
C_ACCENT = RGBColor(0x2E, 0x86, 0xC1)
C_WARN = RGBColor(0xB9, 0x4A, 0x14)
C_TEXT = RGBColor(0x2C, 0x3E, 0x50)
C_MUTED = RGBColor(0x70, 0x7B, 0x84)
C_CARD = RGBColor(0xF2, 0xF6, 0xF9)
FONT = "微软雅黑"
NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
SW, SH = 13.333, 7.5

CAPTION = {
    "sys": "图：赫斯曼 RSP 交换机系统总览 —— 设备状态、安全状态、信号触点与 LED 状态",
    "vlan_hs": "图：赫斯曼 VLAN 端口划分 —— 1/4、1/5 属 VLAN 300，1/6、1/7 属 VLAN 370",
    "ip1": "图：IP 地址配置 —— MAC 地址、IP、子网掩码与网关",
    "ip2": "图：配置菜单位置 —— 在管理界面中找到 IP 配置项的入口",
    "dev": "图：设备基本信息 —— 型号 SICOM2024M-2S24T-SC40-L3-L3 与序列号",
    "port_st": "图：端口状态信息 —— 管理状态、连接状态、速率与双工模式",
    "port_fl": "图：端口流量统计 —— 收发字节、包数、CRC 错误与超短帧",
    "sysrun": "图：系统运行信息 —— 运行时长、CPU、内存与系统时间",
    "devset": "图：设备信息设置 —— 项目名、位置、时区与联系方式",
    "portcfg": "图：端口配置 —— 别名、状态、协商、速率与双工",
    "pwd": "图：修改密码 —— admin 账号的口令变更界面",
    "ver": "图：软件版本查询 —— 双镜像结构：软件 1 启动、软件 2 备用",
    "upgrade": "图：软件升级 —— 通过 FTP 服务器上传固件",
    "cfgbak": "图：配置上传与下载 —— 备份与回滚通道",
    "limit": "图：端口流量限速 —— 按单播 / 多播 / 广播分类抑制",
    "pvlan": "图：PVLAN 配置 —— 同一 VLAN 内的端口之间再次隔离",
    "gvrp": "图：GVRP 配置 —— Disable / Normal / Fixed 三种状态",
    "vlaninfo": "图：VLAN 信息 —— 默认 VLAN 1，所有端口均为 Untag",
    "mirror": "图：端口镜像配置 —— FE24 作为镜像目的端口",
    "mcast": "图：静态组播地址表 —— 手工绑定组播 MAC 与转发端口",
    "acl": "图：ACL 配置 —— 端口访问控制模式（默认为不控制）",
    "arp": "图：ARP 地址配置 —— 老化时间与动态 / 静态条目",
    "snmp": "图：SNMP 配置 —— 团体名、Trap 端口与 Trap 服务器地址",
    "portsec": "图：端口安全配置 —— 限制单端口可学习的最大 MAC 数量",
    "alarm_st": "图：告警状态显示 —— 内存、CPU、电源、IP 与 MAC 冲突",
    "alarm_set": "图：告警设置 —— 各告警项的使能开关、阈值与浮动值",
    "alarm_port": "图：端口流量告警 —— 入出方向、CRC 错误与丢包率",
    "autothink": "图：和利时 HOLLiAS AutoThink 编程软件 V3.2.3",
    "modbus": "图：LK 系列 PLC 数据区与 Modbus 地址映射关系",
    "ring_topology": "图：环网形成过程示意 —— 设备重启/新设备接入时 Gratuitous ARP 触发组播泛洪",
}


# ------------------------------------------------------------ 基础工具

def set_font(run, size, bold=False, color=C_TEXT, font=FONT):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.name = font
    run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    for tag in ("latin", "ea", "cs"):
        el = rPr.find(NS + tag)
        if el is None:
            el = parse_xml('<a:%s %s typeface="%s"/>' % (tag, nsdecls("a"), font))
            rPr.append(el)
        else:
            el.set("typeface", font)


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    return tf


def add_para(tf, text, size, bold=False, color=C_TEXT, space_after=6,
             first=False, line=1.25, align=PP_ALIGN.LEFT):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    p.line_spacing = line
    r = p.add_run()
    r.text = text
    set_font(r, size, bold, color)
    return p


def rect(slide, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE, lw=1.0):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(lw)
    s.shadow.inherit = False
    return s


def est_lines(text, size_pt, width_in):
    """按字符宽度估算换行数：CJK 记 1.0 em，ASCII 记 0.53 em，空格 0.28 em"""
    avail = width_in * 72.0
    w = 0.0
    for ch in text:
        if ch == " ":
            w += 0.28 * size_pt
        elif ord(ch) < 0x2E80:
            w += 0.53 * size_pt
        else:
            w += 1.0 * size_pt
    return max(1, int(-(-w // avail)))


def place_image(slide, key, bx, by, bw, bh, border=True, cap_size=9.0):
    """等比缩放完整放入指定区域（contain，绝不裁剪），下方配讲解性图注"""
    path = os.path.join(IMG_DIR, P[key])
    with Image.open(path) as im:
        iw, ih = im.size
    cap_h = (cap_size / 72.0) * 1.9 if (cap_size and CAPTION.get(key)) else 0.0
    avail_h = bh - cap_h
    scale = min(bw / iw, avail_h / ih)
    w, h = iw * scale, ih * scale
    left = bx + (bw - w) / 2
    top = by + (avail_h - h) / 2
    if border:
        rect(slide, left - 0.05, top - 0.05, w + 0.10, h + 0.10,
             fill=RGBColor(0xFF, 0xFF, 0xFF), line=RGBColor(0xD3, 0xDC, 0xE3), lw=0.75)
    slide.shapes.add_picture(path, Inches(left), Inches(top), Inches(w), Inches(h))
    if cap_size and CAPTION.get(key):
        cy = by + avail_h + 0.06
        tf = textbox(slide, bx, cy, bw, cap_h)
        add_para(tf, CAPTION[key], cap_size, color=C_MUTED, first=True,
                 line=1.2, space_after=0, align=PP_ALIGN.CENTER)
    return h


def add_page_no(slide, n):
    tf = textbox(slide, SW - 1.05, SH - 0.55, 0.6, 0.3, MSO_ANCHOR.MIDDLE)
    add_para(tf, str(n), 9, color=C_MUTED, first=True, align=PP_ALIGN.RIGHT)


# ------------------------------------------------------------ 版式

def slide_cover(prs):
    """封面 —— 加署名"谭跃"在右下角"""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=C_PRIMARY)
    rect(s, 0, 0, 0.28, SH, fill=C_ACCENT)
    rect(s, 8.6, 0, 4.733, SH, fill=RGBColor(0x17, 0x3F, 0x5C))

    tf = textbox(s, 1.15, 2.15, 7.3, 1.6)
    add_para(tf, "工业网络与 PLC 通信", 40, bold=True,
             color=RGBColor(0xFF, 0xFF, 0xFF), first=True, space_after=12)
    add_para(tf, "技术培训", 40, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF), space_after=0)

    rect(s, 1.2, 4.15, 1.6, 0.045, fill=C_ACCENT)

    tf = textbox(s, 1.15, 4.5, 7.3, 1.2)
    add_para(tf, "从交换机原理到 Modbus 通信 · 现场真实界面图解", 15,
             color=RGBColor(0xBF, 0xD7, 0xE8), first=True, space_after=12)
    add_para(tf, "面向工业现场运维工程师 / 自动化工程师", 12,
             color=RGBColor(0x9C, 0xBC, 0xD4), space_after=0)

    place_image(s, "sys", 9.0, 1.75, 3.85, 3.7, border=False, cap_size=0)
    # 署名（用户新增）
    rect(s, 8.85, 5.7, 4.15, 0.95, fill=RGBColor(0x14, 0x38, 0x51))
    tf = textbox(s, 9.0, 5.9, 3.9, 0.55, MSO_ANCHOR.MIDDLE)
    add_para(tf, "Hirschmann  ·  KYLAND  ·  HOLLiAS", 10.5,
             color=RGBColor(0x8F, 0xB4, 0xCE), first=True, align=PP_ALIGN.CENTER)
    # 署名条
    tf = textbox(s, 9.0, 6.42, 3.9, 0.28, MSO_ANCHOR.MIDDLE)
    add_para(tf, "讲者：谭跃", 11.5, color=RGBColor(0xBF, 0xD7, 0xE8),
             first=True, align=PP_ALIGN.CENTER)
    return s


def slide_toc(prs):
    """目录 —— 用云端新版描述"""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=RGBColor(0xFF, 0xFF, 0xFF))
    rect(s, 0, 0, SW, 1.35, fill=C_CARD)
    rect(s, 0, 0, 0.16, 1.35, fill=C_PRIMARY)
    tf = textbox(s, 0.75, 0.34, 6, 0.7, MSO_ANCHOR.MIDDLE)
    add_para(tf, "课程目录", 26, bold=True, color=C_PRIMARY, first=True)
    tf = textbox(s, SW - 3.6, 0.45, 2.9, 0.5, MSO_ANCHOR.MIDDLE)
    add_para(tf, "CONTENTS", 11, color=C_MUTED, first=True, align=PP_ALIGN.RIGHT)

    items = [
        ("01", "工业网络与设备基础", "工业交换机的定位、路由器、IP 规划"),
        ("02", "端口、链路与数据转发", "MAC 学习、统计计数、端口命名规范"),
        ("03", "VLAN 与广播域隔离", "广播域、标签与端口类型、PVLAN、GVRP"),
        ("04", "安全加固与网络监控", "口令、备份升级、ACL、镜像、SNMP、ARP"),
        ("05", "告警体系与故障定位", "告警分级、健康度指标、排查路径"),
        ("06", "PLC 与 Modbus 通信", "协议模型、数据区、地址映射与 +1 陷阱"),
    ]
    x0, y0, cw, ch, gap = 0.75, 1.75, 5.9, 1.55, 0.28
    for i, (no, title, sub) in enumerate(items):
        col, row = i % 2, i // 2
        x = x0 + col * (cw + gap)
        y = y0 + row * (ch + gap)
        rect(s, x, y, cw, ch, fill=C_CARD)
        rect(s, x, y, 0.06, ch, fill=C_ACCENT)
        tf = textbox(s, x + 0.35, y + 0.24, 1.0, 0.6)
        add_para(tf, no, 24, bold=True, color=C_ACCENT, first=True)
        tf = textbox(s, x + 1.35, y + 0.30, 4.3, 0.5)
        add_para(tf, title, 15, bold=True, color=C_PRIMARY, first=True)
        tf = textbox(s, x + 1.35, y + 0.88, 4.3, 0.5)
        add_para(tf, sub, 10.5, color=C_MUTED, first=True)
    return s


def slide_section(prs, no, title, lead_lines):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=C_PRIMARY)
    rect(s, 0, 0, 6.2, SH, fill=RGBColor(0x17, 0x3F, 0x5C))
    tf = textbox(s, 1.1, 2.35, 2.4, 1.5)
    add_para(tf, no, 68, bold=True, color=C_ACCENT, first=True)
    rect(s, 1.15, 4.0, 1.4, 0.05, fill=C_ACCENT)
    tf = textbox(s, 1.1, 4.32, 4.7, 0.95)
    add_para(tf, title, 27, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF), first=True)
    tf = textbox(s, 1.1, 5.4, 4.7, 1.1)
    for i, ln in enumerate(lead_lines):
        add_para(tf, ln, 12, color=RGBColor(0x9C, 0xBC, 0xD4),
                 first=(i == 0), line=1.45, space_after=2)
    rect(s, 7.3, 2.1, 5.25, 3.3, fill=RGBColor(0x21, 0x56, 0x78))
    return s


def slide_section_minor(prs, title, lead):
    """小节封面页（用于 Slide 7 的"赫斯曼交换机 VLAN 划分教程"）"""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=RGBColor(0xFF, 0xFF, 0xFF))
    rect(s, 0, 0, SW, 1.18, fill=C_CARD)
    rect(s, 0, 0, 0.16, 1.18, fill=C_ACCENT)
    tf = textbox(s, 0.72, 0.19, 9.4, 0.56, MSO_ANCHOR.MIDDLE)
    add_para(tf, title, 22, bold=True, color=C_PRIMARY, first=True)
    tf = textbox(s, 0.75, 0.80, 10.2, 0.32)
    add_para(tf, lead, 11, color=C_MUTED, first=True)
    # 大块留白作为"小节封面"
    rect(s, 2.5, 2.6, 8.33, 3.6, fill=C_CARD, line=RGBColor(0xD8, 0xE3, 0xEA), lw=0.75)
    tf = textbox(s, 2.8, 3.4, 7.73, 2.0, MSO_ANCHOR.MIDDLE)
    add_para(tf, "▶  以下为实操讲解", 24, bold=True, color=C_ACCENT, first=True,
             align=PP_ALIGN.CENTER, space_after=12)
    add_para(tf, "请配合下一页的截图逐步操作", 13, color=C_MUTED,
             align=PP_ALIGN.CENTER, space_after=0)
    return s


def slide_placeholder(prs, no, chapter, hint_lines, title="（占位）", lead="内容待补充"):
    """占位页 —— 保留用户备注，等待后续填充"""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=RGBColor(0xFF, 0xFF, 0xFF))
    # 标题条
    rect(s, 0, 0, SW, 1.18, fill=C_CARD)
    rect(s, 0, 0, 0.16, 1.18, fill=C_WARN)  # 用 warn 色突出"待补充"
    tf = textbox(s, 0.72, 0.19, 9.4, 0.56, MSO_ANCHOR.MIDDLE)
    add_para(tf, title, 21, bold=True, color=C_PRIMARY, first=True)
    tf = textbox(s, 0.75, 0.80, 10.2, 0.32)
    add_para(tf, lead, 11, color=C_MUTED, first=True)
    tf = textbox(s, SW - 3.15, 0.24, 2.4, 0.4, MSO_ANCHOR.MIDDLE)
    add_para(tf, chapter, 10.5, color=C_WARN, first=True, align=PP_ALIGN.RIGHT)
    # 占位主区
    rect(s, 1.5, 2.0, 10.33, 4.0, fill=RGBColor(0xFD, 0xF3, 0xE7),
         line=RGBColor(0xEE, 0xC7, 0x92), lw=0.75)
    # 标识徽章
    rect(s, 1.5, 2.0, 2.0, 0.45, fill=C_WARN)
    tf = textbox(s, 1.5, 2.0, 2.0, 0.45, MSO_ANCHOR.MIDDLE)
    add_para(tf, "占位 · 待补充", 12, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
             first=True, align=PP_ALIGN.CENTER)
    tf = textbox(s, 1.8, 2.7, 9.73, 3.0, MSO_ANCHOR.MIDDLE)
    for i, ln in enumerate(hint_lines):
        add_para(tf, "• " + ln, 14, color=C_TEXT,
                 first=(i == 0), line=1.6, space_after=8, align=PP_ALIGN.LEFT)
    add_page_no(s, no)
    return s


def slide_text_only(prs, no, chapter, title, lead, points, note=None):
    """无图版式 —— 左侧文字大纲 + 右侧提示卡（用于内容太短但要保留的页）"""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=RGBColor(0xFF, 0xFF, 0xFF))
    rect(s, 0, 0, SW, 1.18, fill=C_CARD)
    rect(s, 0, 0, 0.16, 1.18, fill=C_PRIMARY)
    tf = textbox(s, 0.72, 0.19, 9.4, 0.56, MSO_ANCHOR.MIDDLE)
    add_para(tf, title, 21, bold=True, color=C_PRIMARY, first=True)
    tf = textbox(s, 0.75, 0.80, 10.2, 0.32)
    add_para(tf, lead, 11, color=C_MUTED, first=True)
    tf = textbox(s, SW - 3.15, 0.24, 2.4, 0.4, MSO_ANCHOR.MIDDLE)
    add_para(tf, chapter, 10.5, color=C_ACCENT, first=True, align=PP_ALIGN.RIGHT)

    # 左侧：要点列表（占左侧 7 英寸）
    x, y, wtxt = 0.62, 1.7, 7.0
    body_w = wtxt - 0.30
    for hd, tx in points:
        rect(s, x, y + 0.05, 0.055, 0.60, fill=C_ACCENT)
        tf = textbox(s, x + 0.24, y, wtxt - 0.24, 0.34)
        add_para(tf, hd, 13.5, bold=True, color=C_PRIMARY, first=True, space_after=0)
        lines = est_lines(tx, 11, body_w)
        body_h = lines * (11 * 1.34 / 72.0) + 0.06
        tf = textbox(s, x + 0.24, y + 0.35, body_w, body_h)
        add_para(tf, tx, 11, color=C_TEXT, first=True, line=1.34, space_after=0)
        y += 0.35 + body_h + 0.32

    # 右侧：场景速记卡（与左半要点行数相近时放这里，否则留白避免视觉失衡）
    rx, ry = 8.0, 1.7
    rw = 4.9
    # 这里不画卡，让左半主导；如要保留卡，把下面 rect 取消注释
    # rect(s, rx, ry, rw, 5.0, fill=C_CARD, line=RGBColor(0xD8, 0xE3, 0xEA), lw=0.75)
    add_page_no(s, no)
    return s


def slide_content(prs, no, chapter, title, lead, img_keys, points, note=None):
    """左侧完整截图 + 右侧知识讲解"""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=RGBColor(0xFF, 0xFF, 0xFF))

    rect(s, 0, 0, SW, 1.18, fill=C_CARD)
    rect(s, 0, 0, 0.16, 1.18, fill=C_PRIMARY)
    tf = textbox(s, 0.72, 0.19, 9.4, 0.56, MSO_ANCHOR.MIDDLE)
    add_para(tf, title, 21, bold=True, color=C_PRIMARY, first=True)
    tf = textbox(s, 0.75, 0.80, 10.2, 0.32)
    add_para(tf, lead, 11, color=C_MUTED, first=True)
    tf = textbox(s, SW - 3.15, 0.24, 2.4, 0.4, MSO_ANCHOR.MIDDLE)
    add_para(tf, chapter, 10.5, color=C_ACCENT, first=True, align=PP_ALIGN.RIGHT)

    bx, by, bw, bh = 0.62, 1.52, 7.35, 5.28
    rect(s, bx, by, bw, bh, fill=RGBColor(0xFA, 0xFC, 0xFD),
         line=RGBColor(0xE2, 0xE9, 0xEE), lw=0.75)
    n = len(img_keys)
    if n == 1:
        place_image(s, img_keys[0], bx + 0.18, by + 0.18, bw - 0.36, bh - 0.36)
    else:
        gap = 0.16
        sub_h = (bh - 0.36 - gap * (n - 1)) / n
        for i, k in enumerate(img_keys):
            sy = by + 0.18 + i * (sub_h + gap)
            place_image(s, k, bx + 0.18, sy, bw - 0.36, sub_h, cap_size=8.0)

    x, wtxt, y = 8.28, 4.42, 1.60
    body_w = wtxt - 0.30
    for hd, tx in points:
        rect(s, x, y + 0.05, 0.055, 0.60, fill=C_ACCENT)
        tf = textbox(s, x + 0.24, y, wtxt - 0.24, 0.34)
        add_para(tf, hd, 12.5, bold=True, color=C_PRIMARY, first=True, space_after=0)
        lines = est_lines(tx, 10.5, body_w)
        body_h = lines * (10.5 * 1.34 / 72.0) + 0.06
        tf = textbox(s, x + 0.24, y + 0.35, body_w, body_h)
        add_para(tf, tx, 10.5, color=C_TEXT, first=True, line=1.34, space_after=0)
        y += 0.35 + body_h + 0.30

    if note:
        ny = min(6.32, max(6.02, y + 0.08))
        rect(s, x, ny, wtxt, 0.66, fill=RGBColor(0xFD, 0xF3, 0xE7),
             line=RGBColor(0xEE, 0xC7, 0x92), lw=0.75)
        tf = textbox(s, x + 0.18, ny + 0.09, wtxt - 0.36, 0.5, MSO_ANCHOR.MIDDLE)
        add_para(tf, note, 9.8, color=C_WARN, first=True, line=1.22, space_after=0)
        nlines = est_lines(note, 9.8, wtxt - 0.36)
        print("   [check] S%-3d 文字结束 y=%.2f  提示框 %s  提示 %d 行"
              % (no, y, "%.2f~%.2f" % (ny, ny + 0.66), nlines))
        if y > ny + 0.02:
            print("   [WARN] S%d 文字与提示框重叠 (%.2f > %.2f)" % (no, y, ny))
    else:
        print("   [check] S%-3d 文字结束 y=%.2f" % (no, y))
        if y > 6.95:
            print("   [WARN] S%d 文字溢出页面底部 (%.2f)" % (no, y))

    add_page_no(s, no)
    return s


def slide_summary(prs, no, img_key):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=RGBColor(0xFF, 0xFF, 0xFF))
    rect(s, 0, 0, SW, 1.18, fill=C_CARD)
    rect(s, 0, 0, 0.16, 1.18, fill=C_PRIMARY)
    tf = textbox(s, 0.72, 0.19, 9, 0.56, MSO_ANCHOR.MIDDLE)
    add_para(tf, "知识地图与课后练习", 21, bold=True, color=C_PRIMARY, first=True)
    tf = textbox(s, 0.75, 0.80, 10.2, 0.32)
    add_para(tf, "把六章内容串成一条排查主线", 11, color=C_MUTED, first=True)

    place_image(s, img_key, 0.62, 1.52, 6.45, 5.28)

    x, y, w = 7.42, 1.58, 5.31
    blocks = [
        ("一条主线",
         "物理链路 → 二层转发（MAC / VLAN）→ 三层地址（IP / ARP）→ 应用协议（Modbus）。"
         "故障排查按这个顺序自下而上排除。"),
        ("两个习惯",
         "① 变更前先备份配置；② 配置即文档 —— 端口描述、设备位置与联系人写清楚，"
         "比事后补画拓扑图可靠得多。"),
        ("三个必查",
         "端口统计计数（CRC / 丢包）、告警状态、系统时间。这三项能覆盖大部分现场问题。"),
    ]
    for hd, tx in blocks:
        rect(s, x, y + 0.05, 0.055, 0.60, fill=C_ACCENT)
        tf = textbox(s, x + 0.24, y, w, 0.34)
        add_para(tf, hd, 13, bold=True, color=C_PRIMARY, first=True, space_after=0)
        tf = textbox(s, x + 0.24, y + 0.36, w - 0.24, 1.05)
        add_para(tf, tx, 10.5, color=C_TEXT, first=True, line=1.34, space_after=0)
        y += 1.40

    rect(s, x, 5.78, w, 1.02, fill=C_CARD, line=RGBColor(0xD8, 0xE3, 0xEA), lw=0.75)
    tf = textbox(s, x + 0.2, 5.88, w - 0.4, 0.85)
    add_para(tf, "练习", 11.5, bold=True, color=C_PRIMARY, first=True, space_after=4)
    add_para(tf, "① 新增端口划入 VLAN 370 并验证互通  ② 计算 IW 区第 10 个字的 Modbus TCP 地址",
             9.6, color=C_TEXT, line=1.28, space_after=3)
    add_para(tf, "③ 从 CRC 错误计数出发，判断故障属于哪一层", 9.6, color=C_TEXT, line=1.28, space_after=0)
    add_page_no(s, no)
    return s


def slide_end(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, SW, SH, fill=C_PRIMARY)
    rect(s, 0, 0, 0.28, SH, fill=C_ACCENT)
    tf = textbox(s, 1.1, 2.8, 8, 1.35)
    add_para(tf, "谢谢", 46, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
             first=True, space_after=14)
    add_para(tf, "Questions & Discussion", 15, color=RGBColor(0x9C, 0xBC, 0xD4), space_after=0)
    rect(s, 1.15, 4.35, 1.5, 0.045, fill=C_ACCENT)
    return s


# ------------------------------------------------------------ 内容（v17，39 页）

def build():
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)

    CH1 = "01 工业网络与设备基础"
    CH2 = "02 端口、链路与数据转发"
    CH3 = "03 VLAN 与广播域隔离"
    CH4 = "04 安全加固与网络监控"
    CH5 = "05 告警体系与故障定位"
    CH6 = "06 PLC 与 Modbus 通信"

    # ==== Slide 1 — 封面
    slide_cover(prs)
    # ==== Slide 2 — 目录
    slide_toc(prs)
    # ==== Slide 3 — 章节 01
    slide_section(prs, "01", "工业网络与设备基础",
                  ["什么是网络通信中的设备？",
                   "它们有什么作用？"])

    # ==== Slide 4 — 什么是 VLAN（用户要求代写内容）
    slide_content(prs, 4, CH1, "什么是 VLAN？",
                  "Virtual LAN —— 把一台物理交换机切成多台逻辑交换机",
                  ["vlaninfo"],
                  [("没有 VLAN 会怎样",
                    "所有端口默认同属一个广播域，广播帧会转发到每一个端口。"
                    "终端越多广播越频繁，一个故障网卡就可能拖垮整个网段。"),
                   ("VLAN 是什么",
                    "VLAN（Virtual LAN，虚拟局域网）把一台物理交换机划分成多个"
                    "相互隔离的逻辑交换机，每个 VLAN 都是一个独立的广播域。"),
                   ("有什么作用",
                    "① 缩小广播域与故障范围；② 安全分区，控制网、监控网、办公网互不可见；"
                    "③ 组网灵活，跨机柜的同业务设备也能归到同一组。"),
                   ("如何起作用",
                    "依靠 802.1Q 标签：Access 口接终端收发不带标签的帧，"
                    "Trunk 口承载多个 VLAN 做互联，PVID 决定未打标帧归到哪个 VLAN。")],
                  note="不同 VLAN 之间通信必须走三层（路由），二层上它们互相隔离")

    # ==== Slide 5 — 工业交换机（按图选图注：VLAN 划分）
    slide_content(prs, 5, CH1, "工业交换机",
                  "VLAN 划分，网段隔离，ACL 访问控制",
                  ["vlan_hs"],
                  [("VLAN 划分能力",
                    "以赫斯曼交换机为例，图中将对应的端口划分到需要的 vlan，也就实现了"
                    "不同的端口对应不同网段。"),
                   ("可靠性与冗余",
                    "支持环网冗余协议，链路中断时倒换时间通常在几十毫秒级，"
                    "保证控制业务不中断。"),
                   ("状态可视化",
                    "图中这类设备会持续上报温度、电源、信号触点与告警计数，"
                    "商用交换机一般不具备这些工业运维关心的状态量。")],
                  note="选型先看环境等级与冗余能力，端口数量反而是次要因素")

    # ==== Slide 6 — AdmitAll 与 Ingress filtering（新增）
    slide_content(prs, 6, CH3, "实例解读：AdmitAll 与 Ingress filtering",
                  "两个开关，决定了端口对 VLAN 帧的宽容程度",
                  ["vlan_hs"],
                  [("划分方案",
                    "图中 1/4、1/5 划入 VLAN 300，1/6、1/7 划入 VLAN 370，其余端口保留在"
                    "默认 VLAN 1，不同业务各归其位。"),
                   ("AdmitAll（允许所有）",
                    "端口接收所有 VLAN 标签的帧，不做筛选。调试阶段用它快速打通，"
                    "但生产环境应当收敛。"),
                   ("Ingress filtering（入向过滤）",
                    "丢弃不属于本端口允许 VLAN 的帧。这是防止私接设备、"
                    "阻止误配置扩散的有效开关。"),
                   ("配置顺序",
                    "先规划好 VLAN 与端口归属，再逐个端口收紧策略，"
                    "避免一次性全改导致管理通道中断。")],
                  note="远程改 VLAN 有掉线风险，条件允许时现场操作")

    # ==== Slide 7 — 小节封面（赫斯曼交换机 VLAN 划分教程）
    slide_section_minor(prs, "赫斯曼交换机 VLAN 划分教程",
                        "以下为赫斯曼交换机的 VLAN 划分现场操作步骤")

    # ==== Slide 8 — 东土交换机简介（无图，纯文字）
    slide_text_only(prs, 8, CH1, "东土交换机简介",
                    "场站内部数据汇聚与交换的主力机型",
                    [("跨场站用赫斯曼",
                      "赫斯曼交换机主要使用于场站到阀室以及阀室之间，"
                      "负责长距离、光纤环网与冗余切换。"),
                     ("场站内用东土",
                      "场站内的网络转发、数据通信使用东土交换机，"
                      "覆盖机柜内接入与短距汇聚。"),
                     ("选型原则",
                      "按『使用边界 + 距离 + 业务等级』组合选型，"
                      "不要在所有位置都用同一型号。")],
                    note="赫斯曼偏骨干 / 关键链路，东土偏接入 / 汇聚")

    # ==== Slide 9 — 设备铭牌
    slide_content(prs, 9, CH1, "读懂设备铭牌：型号里藏着配置清单",
                  "验收第一步不是通电，而是核对型号、序列号与版本",
                  ["dev"],
                  [("型号拆解",
                    "以 SICOM2024M-2S24T-SC40-L3-L3 为例：24 个百兆电口加 2 个光口槽位，"
                    "SC40 表示光模块传输距离约 40km，L3 表示支持三层路由功能。"),
                   ("序列号与 MAC",
                    "是设备的身份证。资产台账、质保报修、授权许可、网管平台纳管都依赖它们，"
                    "验收时必须记录归档。"),
                   ("BootRom 与软件版本",
                    "BootRom 类似 PC 的 BIOS，负责引导，一般不轻易升级；"
                    "软件版本决定功能集与已知漏洞，是升级的主要对象。")],
                  note="BootRom 升级失败会导致设备变砖，非必要不动")

    # ==== Slide 10 — 端口状态监测（新增）
    slide_content(prs, 10, CH2, "端口状态监测",
                  "数据看不到了？先看端口状态与流量",
                  ["port_st", "port_fl"],
                  [("场景",
                    "场站中有时出现设备的数据无法监测，或者调控中心监测不到，"
                    "肉眼无法直接判断连接状态。"),
                   ("看哪两项",
                    "登录东土交换机管理页面，查看端口连接状态（管理 / 链路 up/down）"
                    "与端口流量统计。"),
                   ("成环特征",
                    "东土交换机用于数据汇聚与交换，属于二层。如果出现接错网线或"
                    "其他原因导致成环，会导致泛洪、广播风暴，表现为设备正常但没数据。"
                    "此时可通过 Console 口连接交换机，查看端口流量是否异常，"
                    "判断是否存在成环情况。"),
                   ("判断要点",
                    "多个口的包速率同时飙高且数值接近 → 泛洪特征（都在转发同一批帧）；"
                    "CRC 错误和小于 64Bytes 两列同步增长 → 强烈提示环路或物理层问题。")])

    # ==== Slide 11 — 统计计数判断链路
    slide_content(prs, 11, CH2, "从统计计数判断链路是否健康",
                  "不要只看通不通，要看计数是怎么涨的",
                  ["port_fl"],
                  [("收发字节与包数",
                    "判断链路上是否真有业务流量。若只有广播包持续增长而没有有效单播，"
                    "往往是环路或配置问题。"),
                   ("CRC 错误帧",
                    "帧校验失败，指向物理层：线缆受损、光模块老化、接头污染、"
                    "超距、强电干扰。这是最有诊断价值的指标。"),
                   ("超短帧（小于 64 字节）",
                    "正常以太网帧最小 64 字节，小于它的多为冲突碎片，"
                    "常见于双工不匹配或物理层异常。"),
                   ("看增量，不看绝对值",
                    "计数通常只增不清零。正确做法是记录基线，隔一段时间再对比增量，"
                    "判断是否在持续劣化。")],
                  note="重启会清空计数，排查前先截图留证")

    # ==== Slide 12 — 为什么成环（新增）
    slide_content(prs, 12, CH2, "为什么成环会导致数据出不去",
                  "环路本身不致命，组播/广播泛洪才是元凶",
                  ["portcfg"],
                  [("简单解释",
                    "回路成环时并不会立即出现广播风暴：通信中的设备是存在于 MAC 表的。"
                    "一旦 MAC 表老化或 ARP 缓存到期重新广播，"
                    "就会在环路中不断循环导致广播风暴、MAC 表失效，"
                    "无法正常通信，数据也就无法交互。")],
                  note="环路上线缆错接是工地最常见的诱因之一")

    # ==== Slide 13 — 端口配置（新增）
    slide_content(prs, 13, CH2, "端口配置",
                  "管理好每个端口，是网络可维护的前提",
                  ["portcfg"],
                  [("基本属性",
                    "别名、管理状态、协商模式、速率、双工、流控。"
                    "修改前先记录当前值，错了能立刻回滚。"),
                   ("命名建议",
                    "采用『对端设备 - 用途 - 冗余侧』格式，"
                    "例如 PLC-NOC-A2 / PLC-NOC-B2，便于一眼看清链路归属。"),
                   ("修改窗口",
                    "避开业务高峰期，先改一台观察，再批量推广。")],
                  note="端口别名写明白，比事后补画拓扑图可靠得多")

    # ==== Slide 14 — IP 地址
    slide_content(prs, 14, CH1, "IP 地址：为什么工控现场必须静态",
                  "动态分配带来便利，也带来不确定性",
                  ["ip1", "ip2"],
                  [("DHCP 的问题",
                    "依赖服务器在线、依赖广播报文。服务器故障时新设备无法入网，"
                    "租期到期还可能换地址，导致上位机组态失联。"),
                   ("静态配置三要素",
                    "IP 地址、子网掩码、默认网关。掩码决定同网段范围，"
                    "网关是跨网段通信的唯一出口，填错就会出现能通同网段却出不去的怪象。"),
                   ("入口与复核",
                    "上图为参数填写区，下图展示了菜单路径。改完逐项复核，"
                    "并确认新地址不与已有设备冲突、已在监控平台登记。")],
                  note="改管理 IP 前，先确认维护通道不会因此中断")

    # ==== Slide 15 — SNMP 配置（新增）
    slide_content(prs, 15, CH4, "SNMP 配置：调控中心智能感知",
                  "让设备主动把状态报上来，而不是等人去巡检",
                  ["snmp"],
                  [("团体名就是口令",
                    "只读与读写团体名用于鉴权。public 与 private 是出厂默认值，"
                    "必须修改，否则等于把配置权限公开。"),
                   ("Trap 与查询端口",
                    "查询用 161，Trap（设备主动上报）用 162。"
                    "Trap 服务器地址必须指向真实在运行的网管主机。"),
                   ("版本选择",
                    "v1/v2c 的团体名在报文中明文传输，"
                    "建议升级到 SNMPv3，支持加密与真正的用户认证。")],
                  note="团体名不改，等同于给全网发了一把钥匙")

    # ==== Slide 16 — 东土 ACL（新增）
    slide_content(prs, 16, CH4, "东土 ACL 现状",
                  "有 ACL 但目前未启用 —— 物理分段已满足当前需求",
                  ["acl"],
                  [("当前状态",
                    "东土交换机自带 ACL 访问控制，但我们目前没有使用。"
                    "主要原因是当前使用场景中已通过物理方式做了网段划分，"
                    "且该交换机仅用于场站内部数据通信，设备都可信。"),
                   ("为什么不立刻启用",
                    "现场设备多、变更频繁；启用 ACL 一旦写错规则，"
                    "可能直接阻断正常通信，且目前没有回滚预案。"),
                   ("什么时候要补上",
                    "当出现私接设备、违规接入或安全事件需要阻断时，"
                    "应优先在核心与汇聚口开启 ACL 并先观察一段时间。")],
                  note="默认不控制 = 任何设备插上就能通信")

    # ==== Slide 17 — 占位（整网通信链路）
    slide_placeholder(prs, 17, CH2,
                      ["这页先空着，我要写从阀室赫斯曼到场站赫斯曼、"
                       "到场站交换机、到路由器、到其他场站路由器、"
                       "以及调控中心路由器是如何实现通信的"],
                      title="整网通信链路",
                      lead="从阀室到场站，再到调控中心")

    # ==== Slide 18 — MAC 转发
    slide_content(prs, 18, CH2, "交换机怎么知道该往哪转发",
                  "二层转发的全部秘密：学习、查表、泛洪",
                  ["port_st"],
                  [("学习（Learning）",
                    "收到帧后把「源 MAC + 入端口」记进 MAC 地址表（FDB）。"
                    "图中每个端口的状态，是这张表发挥作用的基础。"),
                   ("查表转发",
                    "用目的 MAC 查表，命中就只往对应端口发。"
                    "这正是交换机区别于集线器的核心能力，也是带宽利用率的来源。"),
                   ("查不到就泛洪",
                    "目的 MAC 不在表里时，会向同 VLAN 的所有端口泛洪。"
                    "广播风暴与 MAC 表被刷爆都源于这个机制。"),
                   ("表项会老化",
                    "MAC 表项有老化时间。设备换口后需等待老化或手工清空，"
                    "否则会出现按老表转发的诡异丢包。")])

    # ==== Slide 19 — 端口命名
    slide_content(prs, 19, CH2, "端口命名：把物理接线变成可维护资产",
                  "一份端口描述，就是一张最小可用的拓扑图",
                  ["portcfg"],
                  [("命名规范",
                    "采用「对端设备-用途-冗余侧」格式，例如 PLC-NOC-A2 与 PLC-NOC-B2 "
                    "分别表示双网冗余的 A 网与 B 网。"),
                   ("从端口表读出结构",
                    "图中可见 PLC、SIS 安全仪表系统、站控机、路由器、"
                    "运营商专线、工控安全监测设备，业务边界一目了然。"),
                   ("先命名，后接线",
                    "接入前先把描述写好再插线，"
                    "避免先接上以后再补 —— 现实情况是这个以后永远不会到来。"),
                   ("交接与抢修价值",
                    "人员变动时，完整的端口描述能让接手的人在几分钟内摸清现场，"
                    "而不是逐根拔线确认。")])

    # ==== Slide 20 — 章节 03
    slide_section(prs, "03", "VLAN 与广播域隔离",
                  ["VLAN 不只是分组，",
                   "它是把一台交换机切成多台逻辑交换机的手段"])

    # ==== Slide 21 — 广播域
    slide_content(prs, 21, CH3, "广播域：为什么必须隔离",
                  "不隔离的代价，是整个网段一起瘫痪",
                  ["vlaninfo"],
                  [("广播会传遍全网",
                    "二层广播帧会被转发到同一广播域的所有端口。"
                    "终端越多、广播越频繁，带宽与终端 CPU 被消耗得越厉害。"),
                   ("广播风暴的成因",
                    "网络环路、故障网卡、病毒或误配置都可能引发风暴，"
                    "表现为全网卡顿甚至完全不可用。"),
                   ("VLAN 的本质",
                    "把一个物理交换机划分成多个相互隔离的逻辑交换机，"
                    "每个 VLAN 都是一个独立的广播域。"),
                   ("隔离也是安全手段",
                    "控制网、监控网、办公网划分到不同 VLAN 后互不可见，"
                    "这是从网络层面落实分区分域的基础。")])

    # ==== Slide 22 — VLAN 标签
    slide_content(prs, 22, CH3, "VLAN 标签与端口类型",
                  "Access 口与 Trunk 口的区别，一张图讲清楚",
                  ["vlaninfo"],
                  [("默认 VLAN 1 的隐患",
                    "出厂状态是所有端口都在 VLAN 1（图中 default，全部 Untag）。"
                    "这意味着所有终端同处一个广播域，应尽早整改。"),
                   ("Untag（Access 口）",
                    "端口只属于一个 VLAN，收发的帧不带标签。"
                    "PLC、站控机、仪表等终端都接在这类端口上。"),
                   ("Tag（Trunk 口）",
                    "端口承载多个 VLAN，帧带 802.1Q 标签，"
                    "用于交换机之间或交换机与上联设备的互联。"),
                   ("PVID",
                    "端口收到不带标签的帧时，给它打上哪个 VLAN 的标签。"
                    "PVID 与允许 VLAN 列表不一致是常见的配置错误来源。")])

    # ==== Slide 23 — PVLAN
    slide_content(prs, 23, CH3, "PVLAN：同一个 VLAN 内还要再隔离",
                  "当同网段也不代表可以互访时",
                  ["pvlan"],
                  [("要解决什么问题",
                    "同一 VLAN 内的端口默认可以互访。"
                    "但多套装置、多个承包商的设备常需要在二层就先隔离开。"),
                   ("靠端口角色实现",
                    "PVLAN 把端口分为隔离口与上联（混杂）口："
                    "隔离口之间不能互访，只能与上联口通信。"),
                   ("典型场景",
                    "同网段内多台 PLC 只需与上位机通信，彼此不需要也不应该互通；"
                    "或视频、办公终端共享上联但互不干扰。"),
                   ("代价",
                    "排障路径变长。部署时要把端口角色画进拓扑图，"
                    "否则后期很难解释为什么两台设备 ping 不通。")])

    # ==== Slide 24 — GVRP
    slide_content(prs, 24, CH3, "GVRP：VLAN 自动同步的利与弊",
                  "自动化程度越高，出问题时往往越难定位",
                  ["gvrp"],
                  [("它做什么",
                    "GVRP 让交换机之间自动通告与学习 VLAN 信息，"
                    "减少在多台设备上重复手工创建 VLAN 的工作量。"),
                   ("三种状态",
                    "Disable 关闭；Normal 动态学习并向外通告；"
                    "Fixed 只通告本地 VLAN、不从邻居学习。"),
                   ("工控网常关闭的原因",
                    "自动扩散意味着 VLAN 范围不可预期："
                    "一台设备的误配置可能顺着 GVRP 扩散到全网。"),
                   ("取舍原则",
                    "关键控制网络优先选择手动加可预期的方案，"
                    "用配置工作量换取故障时的可解释性。")])

    # ==== Slide 25 — 章节 04
    slide_section(prs, "04", "安全加固与网络监控",
                  ["默认配置是为了开箱即用，",
                   "不是为了让设备安全"])

    # ==== Slide 26 — ACL
    slide_content(prs, 26, CH4, "ACL：把不该进网的挡在端口之外",
                  "默认不控制，意味着任何设备插上就能通信",
                  ["acl"],
                  [("ACL 做什么",
                    "在端口上按 MAC 地址、IP 地址等条件过滤报文，"
                    "决定哪些流量允许通过、哪些直接丢弃。"),
                   ("默认状态的风险",
                    "图中所有端口都是不控制模式。"
                    "机柜若管理不严，私接一台笔记本就能直接进入控制网。"),
                   ("部署节奏",
                    "先在核心与汇聚口开启并观察一段时间，"
                    "确认没有误伤业务，再逐步推广到接入层端口。"),
                   ("文档化",
                    "每条 ACL 规则都要写清楚为什么加、目标是谁，"
                    "否则半年后没人敢删也没人敢改。")])

    # ==== Slide 27 — 端口安全
    slide_content(prs, 27, CH4, "端口安全：限制一个口能挂多少设备",
                  "防止私接交换机把网络越接越大",
                  ["portsec"],
                  [("机制",
                    "限制单个端口允许学习的 MAC 地址数量（图中最大 32 个），"
                    "超出后按策略告警、丢弃或关闭端口。"),
                   ("防的是什么",
                    "私接小型交换机或随身 WiFi，"
                    "会在一个端口后面挂上多台未知设备，从而绕过所有基于端口的管控措施。"),
                   ("默认不启用的原因",
                    "工业现场存在冗余切换与主备切换，MAC 会有规律地变化。"
                    "启用前需先摸清正常 MAC 数量基线。"),
                   ("配置建议",
                    "终端端口设为 1 到 2 个 MAC，上联口适当放宽。"
                    "先设告警模式观察，再改为保护动作。")])

    # ==== Slide 28 — SNMP
    slide_content(prs, 28, CH4, "SNMP：让设备主动上报状态",
                  "从人去巡检，到设备主动喊人",
                  ["snmp"],
                  [("三个角色",
                    "管理站（网管平台）、Agent（交换机上的代理进程）、"
                    "MIB（可被查询的对象字典，定义了能读到哪些指标）。"),
                   ("团体名就是口令",
                    "只读与读写团体名用于鉴权。public 与 private 是出厂默认值，"
                    "必须修改，否则等于把配置权限公开。"),
                   ("Trap 与查询端口",
                    "查询用 161，Trap（设备主动上报）用 162。"
                    "Trap 服务器地址必须指向真实在运行的网管主机。"),
                   ("版本选择",
                    "v1/v2c 的团体名在报文中明文传输，"
                    "建议升级到 SNMPv3，它支持加密与真正的用户认证。")],
                  note="团体名不改，等同于给全网发了一把钥匙")

    # ==== Slide 29 — ARP
    slide_content(prs, 29, CH4, "ARP：地址解析与它的先天风险",
                  "三层通信的最后一跳，也是最容易被利用的一环",
                  ["arp"],
                  [("它解决什么",
                    "IP 包要封装成帧才能发出去，ARP 负责把 IP 解析成 MAC 地址，"
                    "结果缓存在 ARP 表中并按老化时间失效（图中 20 分钟）。"),
                   ("动态与静态",
                    "动态条目通过学习获得，会被刷新；"
                    "静态条目手工绑定，不会被伪造应答覆盖。"),
                   ("ARP 欺骗",
                    "ARP 协议没有任何认证机制，"
                    "同网段主机可以伪造应答，把自己伪装成网关实施中间人攻击。"),
                   ("加固做法",
                    "对网关与关键服务器配置静态 ARP 条目；"
                    "在支持的交换机上启用 ARP 防护或动态 ARP 检测。")])

    # ==== Slide 30 — 章节 05
    slide_section(prs, "05", "告警体系与故障定位",
                  ["告警的价值不在多，",
                   "而在该响的时候响"])

    # ==== Slide 31 — 告警分级
    slide_content(prs, 31, CH5, "告警分级与阈值：别让告警变成噪音",
                  "被忽略的告警，等于没有告警",
                  ["alarm_set"],
                  [("先分级",
                    "紧急（电源丢失、端口 down）需要立即处置；"
                    "重要（温度、CPU 越限）当班处理；一般（阈值告警）纳入观察。"),
                   ("阈值与浮动值",
                    "浮动值即回差，用于避免指标在临界点抖动时反复触发。"
                    "没有回差，一条抖动的曲线能刷出上百条告警。"),
                   ("按重要性逐个使能",
                    "图中包含内存、CPU、电源、IP 冲突、MAC 冲突等项目。"
                    "全部打开不等于更安全，只等于更吵。"),
                   ("定期复盘",
                    "统计一段时间内从未触发或频繁误报的项，"
                    "持续调整阈值，让告警保持可信。")])

    # ==== Slide 32 — 设备健康度
    slide_content(prs, 32, CH5, "设备健康度：该看哪几个指标",
                  "CPU、内存、运行时长、系统时间，四个就够了",
                  ["sysrun"],
                  [("CPU 与内存",
                    "短时峰值属正常，持续高位才需警惕。"
                    "常见原因是广播风暴、环路、扫描攻击或网管轮询过密。"),
                   ("运行时长",
                    "意外归零说明设备重启过。"
                    "重启原因比重启本身更重要，要回溯当时的告警与日志。"),
                   ("系统时间",
                    "图中时间停留在 1970.01.01，说明时钟从未初始化。"
                    "日志、告警排序、证书校验全部会失真，必须配置 NTP。"),
                   ("建立基线",
                    "记录正常运行时的 CPU、内存与流量水平。"
                    "没有基线，就无法判断当前值是否异常。")],
                  note="系统时间错误会让所有日志失去时间线，务必优先修复")

    # ==== Slide 33 — 从告警到定位
    slide_content(prs, 33, CH5, "从告警到定位：一条可复用的排查路径",
                  "按层级自下而上，比凭经验乱试可靠得多",
                  ["alarm_port", "alarm_st"],
                  [("端口级告警（上图）",
                    "入出方向流量、CRC 错误、丢包率与丢包数，"
                    "能直接把问题锁定到具体端口，是最有用的一类告警。"),
                   ("第一层：物理层",
                    "看端口是否 down、CRC 是否增长。"
                    "指向线缆、模块、接口、距离与干扰。"),
                   ("第二层：数据链路层",
                    "查 MAC 表、VLAN 归属、是否存在环路、双工与速率是否匹配。"),
                   ("第三层及以上",
                    "查 IP 与掩码、网关、ARP 表项，最后才怀疑应用协议本身。")],
                  note="每次排查先记录计数基线，重启会清空证据")

    # ==== Slide 34 — 章节 06
    slide_section(prs, "06", "PLC 与 Modbus 通信",
                  ["网络最终是为业务服务的：",
                   "让上位机读懂 PLC 的数据"])

    # ==== Slide 35 — PLC 位置
    slide_content(prs, 35, CH6, "PLC 在工业网络中的位置",
                  "它是控制层的执行者，也是网络里的一台终端",
                  ["autothink"],
                  [("角色定位",
                    "PLC 负责执行控制逻辑并采集现场数据，"
                    "上位机（SCADA 或站控机）通过网络读取与下发数据。"),
                   ("编程软件的作用",
                    "和利时 AutoThink 这类软件承担逻辑开发、工程下载、在线监视与调试，"
                    "是工程师与 PLC 之间的桥梁。"),
                   ("版本匹配",
                    "软件版本、PLC 固件版本、工程文件版本三者需要对应。"
                    "版本不匹配是最常见的连不上原因之一。"),
                   ("网络视角",
                    "PLC 对交换机而言就是一台终端主机。"
                    "前面讲的端口、VLAN、告警，直接决定它的通信质量。")])

    # ==== Slide 36 — Modbus 数据区
    slide_content(prs, 36, CH6, "Modbus 协议与四种数据区",
                  "把 PLC 内部数据映射到统一地址，上位机才读得到",
                  ["modbus"],
                  [("协议定位",
                    "Modbus 是应用层协议，Modbus TCP 基于以太网、默认端口 502，"
                    "报文结构简单，是工控领域最通用的协议之一。"),
                   ("四种数据区",
                    "线圈（可读写位）、离散输入（只读位）、"
                    "输入寄存器（只读字）、保持寄存器（可读写字）。"),
                   ("为什么要映射",
                    "PLC 内部用 I（输入）、Q（输出）、M（中间）等数据区，"
                    "上位机只认 Modbus 地址，因此需要一张映射表把两者对应起来。"),
                   ("常用功能码",
                    "01 读线圈、03 读保持寄存器、05 写单个线圈、06 写单个寄存器。"
                    "排查时先用工具读一个已知地址验证连通性。")])

    # ==== Slide 37 — 地址映射 +1 陷阱
    slide_content(prs, 37, CH6, "地址映射计算与 +1 陷阱",
                  "差一个编号，读到的就是另一个变量",
                  ["modbus"],
                  [("映射公式",
                    "图中给出 LK 系列 PLC 数据区到 Modbus 地址的换算关系："
                    "IX 区按 m*8+n 计算位地址，IW 区按 m/2 计算字地址，"
                    "MX 与 MW 区带有固定偏移。"),
                   ("陷阱从哪来",
                    "协议报文中的地址从 0 开始编号，而很多组态软件与文档从 1 开始显示，"
                    "两者相差 1。"),
                   ("Modbus TCP 的做法",
                    "实际使用中，需要在公式计算结果的基础上加 1，"
                    "才能与软件侧显示的地址对应上。"),
                   ("验证方法",
                    "先在 PLC 中给一个变量赋已知值，"
                    "再用调试工具按计算出的地址读取，对得上之后再批量配置点位表。")],
                  note="点位表批量配置前，务必先用单个地址验证编号基准")

    # ==== Slide 38 — 知识地图
    slide_summary(prs, 38, "sys")

    # ==== Slide 39 — 谢谢
    slide_end(prs)

    prs.save(OUT)
    print("=== saved:", OUT)
    print("=== total slides:", len(prs.slides.__iter__.__self__._sldIdLst))


if __name__ == "__main__":
    build()