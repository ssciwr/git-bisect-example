import time
import subprocess
import sys


start = time.time()
subprocess.call([sys.executable, "app.py"])
end = time.time()

if end - start > 0.1:
    raise SystemExit(1)
