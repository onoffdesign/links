"""Download the cover image of every post in posts.json that is not saved yet.

Instagram image links expire after a few weeks, so each cover is copied into
assets/posts/ the first time it appears in posts.json. Runs in GitHub Actions.
"""
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "posts.json").read_text(encoding="utf-8"))

missing = 0
for post in data.get("posts", []):
    target = ROOT / post["image"]
    if target.exists() and target.stat().st_size > 0:
        continue
    src = post.get("source_image")
    if not src:
        print(f"skip {post['id']}: no source_image")
        missing += 1
        continue
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
        if len(body) < 1000:
            raise ValueError(f"response too small ({len(body)} bytes)")
        target.write_bytes(body)
        print(f"saved {target.relative_to(ROOT)} ({len(body)} bytes)")
    except Exception as e:  # keep going, the page falls back to source_image
        print(f"failed {post['id']}: {e}")
        missing += 1

print(f"done, {missing} missing")
sys.exit(0)
