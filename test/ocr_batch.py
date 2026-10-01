# -*- coding: utf-8 -*-
"""批量 OCR：参数为多个图片路径，每个图片的结果写入 <序号>.txt，汇总写 index.txt"""
import sys, os
from rapidocr_onnxruntime import RapidOCR

imgs = sys.argv[1:-1]
outdir = sys.argv[-1]

engine = RapidOCR()
for i, img in enumerate(imgs, 1):
    result, _ = engine(img)
    lines = [t for _, t, _ in result] if result else []
    p = os.path.join(outdir, 'batch_%d.txt' % i)
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(i, len(lines))
