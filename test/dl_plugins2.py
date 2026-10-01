# -*- coding: utf-8 -*-
"""通过国内 GitHub 镜像下载 Obsidian 插件"""
import os, urllib.request

PLUGINS = [
    ("attachment-management", "trganda/obsidian-attachment-management"),
    ("obsidian-image-toolkit", "sissilab/obsidian-image-toolkit"),
    ("dataview", "blacksmithgu/obsidian-dataview"),
    ("obsidian-editing-toolbar", "cumany/obsidian-editing-toolbar"),
]

MIRRORS = [
    "https://ghfast.top/",
    "https://gh.llkk.cc/",
    "https://ghps.cc/",
    "https://gh-proxy.com/",
    "https://github.moeyy.xyz/",
    "https://mirror.ghproxy.com/",
]

plugins_dir = r"E:\Code\MyStudyData\9、笔记\.obsidian\plugins"
log = []

def try_download(url, dst):
    for m in MIRRORS:
        full = m + url
        try:
            req = urllib.request.Request(full, headers={"User-Agent": "workbuddy"})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read()
            if len(data) < 500 and b"not found" in data.lower():
                continue
            with open(dst, "wb") as f:
                f.write(data)
            return True, full
        except Exception as e:
            last = str(e)
    return False, last

for pid, repo in PLUGINS:
    pdir = os.path.join(plugins_dir, pid)
    os.makedirs(pdir, exist_ok=True)
    for fname in ("manifest.json", "main.js", "styles.css"):
        dst = os.path.join(pdir, fname)
        if os.path.exists(dst) and os.path.getsize(dst) > 0:
            continue
        url = f"https://github.com/{repo}/releases/latest/download/{fname}"
        ok, info = try_download(url, dst)
        log.append(f"{'OK' if ok else 'FAIL'} {pid}/{fname} via {info if ok else ''} {'' if ok else info}")

with open(r"E:\Code\MyStudyData\test\plugin_dl_log2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log))
print("done")
