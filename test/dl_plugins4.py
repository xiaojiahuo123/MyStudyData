# -*- coding: utf-8 -*-
"""验证并补全 Obsidian 插件文件：剔除假文件，用可靠镜像重新下载"""
import os, json, urllib.request, time

PLUGINS = [
    ("attachment-management", "trganda/obsidian-attachment-management"),
    ("obsidian-image-toolkit", "sissilab/obsidian-image-toolkit"),
    ("dataview", "blacksmithgu/obsidian-dataview"),
    ("obsidian-editing-toolbar", "cumany/obsidian-editing-toolbar"),
]

# 只保留这两个镜像（ghps.cc 会返回跳转假页）
MIRRORS = ["https://gh-proxy.com/", "https://ghfast.top/", "https://gh.llkk.cc/"]

plugins_dir = r"E:\Code\MyStudyData\9、笔记\.obsidian\plugins"
log = []

def looks_fake(data, fname):
    if fname == "main.js":
        if len(data) < 1000:
            return True
        if b"targetUrl" in data or b"jsjumptopage" in data:
            return True
    if fname == "manifest.json":
        try:
            json.loads(data.decode("utf-8"))
        except Exception:
            return True
    if fname == "styles.css":
        if len(data) < 50 or b"targetUrl" in data:
            return True
    return False

def download(url, dst, fname):
    for m in MIRRORS:
        full = m + url
        try:
            req = urllib.request.Request(full, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if looks_fake(data, fname):
                log.append(f"  fake from {m} size={len(data)}")
                continue
            with open(dst, "wb") as f:
                f.write(data)
            return True, m
        except Exception as e:
            log.append(f"  {m} err {type(e).__name__}")
            time.sleep(1)
    return False, None

for pid, repo in PLUGINS:
    pdir = os.path.join(plugins_dir, pid)
    os.makedirs(pdir, exist_ok=True)
    log.append(f"== {pid}")
    for fname in ("manifest.json", "main.js", "styles.css"):
        dst = os.path.join(pdir, fname)
        need = True
        if os.path.exists(dst):
            with open(dst, "rb") as f:
                cur = f.read()
            if not looks_fake(cur, fname):
                log.append(f"  {fname} exists ok {len(cur)}B")
                need = False
            else:
                log.append(f"  {fname} fake/exists-bad {len(cur)}B, redownload")
        if need:
            url = f"https://github.com/{repo}/releases/latest/download/{fname}"
            for attempt in range(3):
                ok, m = download(url, dst, fname)
                if ok:
                    sz = os.path.getsize(dst)
                    log.append(f"  {fname} OK via {m} {sz}B")
                    break
                time.sleep(2)
            else:
                log.append(f"  {fname} FAILED")

with open(r"E:\Code\MyStudyData\test\plugin_dl_log4.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(log))
print("done")
