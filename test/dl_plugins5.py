# -*- coding: utf-8 -*-
"""下载 editing-toolbar（仓库迁移到 PKM-er，用明确 tag 4.1.4）"""
import os, json, urllib.request, time

REPO = "PKM-er/obsidian-editing-toolbar"
TAG = "4.1.4"
MIRRORS = ["https://gh-proxy.com/", "https://ghfast.top/", "https://gh.llkk.cc/"]
pdir = r"E:\Code\MyStudyData\9、笔记\.obsidian\plugins\obsidian-editing-toolbar"
os.makedirs(pdir, exist_ok=True)
log = []

for fname in ("manifest.json", "main.js", "styles.css"):
    url = f"https://github.com/{REPO}/releases/download/{TAG}/{fname}"
    ok = False
    for m in MIRRORS:
        try:
            req = urllib.request.Request(m + url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 200 or b"targetUrl" in data:
                log.append(f"  {fname} bad data {len(data)}B from {m}")
                continue
            if fname == "manifest.json":
                json.loads(data.decode("utf-8"))
            with open(os.path.join(pdir, fname), "wb") as f:
                f.write(data)
            log.append(f"  {fname} OK via {m} {len(data)}B")
            ok = True
            break
        except Exception as e:
            log.append(f"  {fname} {m} err {type(e).__name__}")
            time.sleep(1)
    if not ok:
        log.append(f"  {fname} FAILED all")

with open(r"E:\Code\MyStudyData\test\plugin_dl_log5.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log))
print("done")
