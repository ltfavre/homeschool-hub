"""Read and write the packed curriculum assets (gzip+base64 parts, see curriculum-assets.js).

    from curriculum_pack import load, save
    data = load("daily-packets.json"); ...; save("daily-packets.json", data)

save() writes deterministic gzip (mtime 0), splits into <=60000-character parts named
curriculum-data/packed-<name>-NNN.json, and updates the manifest's source_sha256."""
import base64, glob, gzip, hashlib, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PART = 60000


def _p(rel):
    return os.path.join(ROOT, rel.lstrip("/"))


def load(name):
    m = json.load(open(_p(name)))
    if "_gzip_parts" not in m:
        raise SystemExit(f"{name} is not a packed asset")
    s = "".join(json.load(open(_p(p)))["data"] for p in m["_gzip_parts"])
    raw = gzip.decompress(base64.b64decode(s))
    assert hashlib.sha256(raw).hexdigest() == m["source_sha256"], f"{name}: checksum mismatch"
    return json.loads(raw)


def save(name, data):
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode()
    b64 = base64.b64encode(gzip.compress(raw, compresslevel=9, mtime=0)).decode()
    chunks = [b64[i:i + PART] for i in range(0, len(b64), PART)]
    if len(chunks) > 8:
        raise SystemExit(f"{name}: too large for 8 parts")
    stem = os.path.splitext(os.path.basename(name))[0]
    for old in glob.glob(_p(f"curriculum-data/packed-{stem}-*.json")):
        os.remove(old)
    parts = []
    for i, c in enumerate(chunks, 1):
        rel = f"/curriculum-data/packed-{stem}-{i:03d}.json"
        json.dump({"data": c}, open(_p(rel), "w"))
        parts.append(rel)
    m = json.load(open(_p(name)))
    m.update({"_gzip_parts": parts, "encoding": "gzip+base64", "source_sha256": hashlib.sha256(raw).hexdigest()})
    json.dump(m, open(_p(name), "w"))
