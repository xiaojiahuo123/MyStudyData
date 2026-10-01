# -*- coding: utf-8 -*-
import io, sys

src = sys.argv[1]
out = sys.argv[2]

raw = io.open(src, "r", encoding="utf-8", errors="replace").read()

cands = ["latin-1", "cp1252", "gbk", "gb18030"]
# 1) try re-encoding as latin-1 then decoding gbk/gb18030
for enc in cands:
    try:
        b = raw.encode("latin-1", errors="strict")
        for dec in ["gbk", "gb18030", "big5"]:
            try:
                t = b.decode(dec, errors="strict")
                # heuristic: count CJK chars
                cjk = sum(1 for ch in t if "一" <= ch <= "鿿")
                print("latin1->%s: cjk=%d sample=%s" % (dec, cjk, t[200:300].replace("\n", " ")))
            except Exception as e:
                print("latin1->%s FAIL %s" % (dec, e))
        break
    except Exception as e:
        print("encode as %s FAIL: %s" % (enc, e))

print("---raw sample repr---")
print(repr(raw[100:160]))
