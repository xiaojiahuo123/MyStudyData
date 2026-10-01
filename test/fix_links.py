# -*- coding: utf-8 -*-
"""更新言语.md 中图片引用路径：统一指向 言语笔记/images/"""
import re, io

path = r'E:\Code\MyStudyData\9、笔记\言语.md'
with io.open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1) ![](.\言语_xxx) -> ![](言语笔记/images/言语_xxx)
text = text.replace(r'![](.\言语_', '![](言语笔记/images/言语_')
# 2) ![](言语_xxx) -> ![](言语笔记/images/言语_xxx)（注意别重复加前缀）
text = re.sub(r'!\[(.*?)\]\((?!言语笔记/|https?:)(言语_[^)]*)\)', r'![\1](言语笔记/images/\2)', text)
# 3) .\言语笔记\images\ 反斜杠统一为正斜杠、去 ./
text = text.replace('.\\言语笔记\\images\\', '言语笔记/images/')

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(text)

print('done')
