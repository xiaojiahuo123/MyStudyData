# -*- coding: utf-8 -*-
"""从 GitHub 下载 Obsidian 社区插件 release 文件并安装到 .obsidian/plugins"""
import os, sys, urllib.request, json

PLUGINS = [
    ("attachment-management", "trganda/obsidian-attachment-management"),
    ("obsidian-image-toolkit", "sissilab/obsidian-image-toolkit"),
    ("dataview", "blacksmithgu/obsidian-dataview"),
    ("obsidian-editing-toolbar", "cumany/obsidian-editing-toolbar"),
]

VAULT = r"E:\Code\MyStudyData\9、笔记"
plugins_dir = os.path.join(VAULT, ".obsidian", "plugins")
os.makedirs(plugins_dir, exist_ok=True)

log = []
for pid, repo in PLUGINS:
    pdir = os.path.join(plugins_dir, pid)
    os.makedirs(pdir, exist_ok=True)
    for fname in ("manifest.json", "main.js", "styles.css"):
        url = f"https://github.com/{repo}/releases/latest/download/{fname}"
        dst = os.path.join(pdir, fname)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "workbuddy"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(dst, "wb") as f:
                f.write(data)
            log.append(f"OK {pid}/{fname} {len(data)}B")
        except Exception as e:
            log.append(f"FAIL {pid}/{fname} {e}")

out = os.path.join(r"E:\Code\MyStudyData\test", "plugin_dl_log.txt")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(log))
print("done")
