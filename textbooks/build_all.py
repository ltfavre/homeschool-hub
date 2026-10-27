"""Build every book (full year so far) into downloads/textbooks/ with page-index sidecars, in parallel.

python3 textbooks/build_all.py [key ...]"""
import os, sys, subprocess
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "downloads", "textbooks")
KEYS = sys.argv[1:] or ["math4", "math7", "ela4", "ela7", "sci4", "sci7", "ss4", "ss7", "art4", "art7", "span4", "span7", "data"]


def run(k):
    r = subprocess.run([sys.executable, os.path.join(HERE, "build.py"), k, "--all", "--out", OUT], capture_output=True, text=True)
    return k, r.returncode, (r.stderr or "")[-400:]


with ThreadPoolExecutor(max_workers=6) as ex:
    for k, code, err in ex.map(run, KEYS):
        print(k, "ok" if code == 0 else "FAILED\n" + err, flush=True)
