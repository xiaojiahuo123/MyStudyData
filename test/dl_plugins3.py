# -*- coding: utf-8 -*-
"""绕过系统代理直连 GitHub 下载 Obsidian 插件"""
import os, urllib.request

PLUGINS = [
    ("attachment-management", "trganda/obsidian-attachment-management"),
    ("obsidian-image-toolkit", "sissilab/obsidian-image-toolkit"),
    ("dataview", "blacksmithgu/obsidian-dataview"),
    ("obsidian-editing-toolbar", "cumany/obsidian-editing-toolbar"),
]

plugins_dir = r"E:\Code\MyStudyData\9、笔记\.obsidian\plugins"
log = []

# 完全绕过系统代理
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

for pid, repo in PLUGINS:
    pdir = os.path.join(plugins_dir, pid)
    os.makedirs(pdir, exist_ok=True)
    for fname in ("manifest.json", "main.js", "styles.css"):
        url = f"https://github.com/{repo}/releases/latest/download/{fname}"
        dst = os.path.join(pdir, fname)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with opener.open(req, timeout=90) as r:
                data = r.read()
            if len(data) < 300:
                log.append(f"FAIL {pid}/{fname} too small {len(data)}B")
                continue
            with open(dst, "wb") as f:
                f.write(data)
            log.append(f"OK {pid}/{fname} {len(data)}B")
        except Exception as e:
            log.append(f"FAIL {pid}/{fname} {type(e).__name__}: {e}")

with open(r"E:\Code\MyStudyData\test\plugin_dl_log3.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log))
print("done")
