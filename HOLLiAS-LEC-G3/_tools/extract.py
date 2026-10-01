# -*- coding: utf-8 -*-
import sys, io
from PyPDF2 import PdfReader

src = sys.argv[1]
out = sys.argv[2]
reader = PdfReader(src)
parts = []
for i, page in enumerate(reader.pages):
    try:
        t = page.extract_text() or ""
    except Exception as e:
        t = "[extract error: %s]" % e
    parts.append("===== PAGE %d =====\n%s" % (i + 1, t))
full = "\n".join(parts)
with io.open(out, "w", encoding="utf-8") as f:
    f.write(full)
print("pages:", len(reader.pages))
print("chars:", len(full))
print(full[:1500])
