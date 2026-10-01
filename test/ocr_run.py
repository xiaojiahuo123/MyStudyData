# -*- coding: utf-8 -*-
"""用 RapidOCR 识别截图，按行输出文本，写入结果文件"""
import sys
from rapidocr_onnxruntime import RapidOCR

img = sys.argv[1]
out = sys.argv[2]

engine = RapidOCR()
result, _ = engine(img)

lines = []
if result:
    for box, text, score in result:
        lines.append(text)

with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('OK lines:', len(lines))
