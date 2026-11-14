#!/usr/bin/env python3
"""news-image-01 entry (Python 3.13, standard library only).

Copies entry.jpg to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
SRC = os.path.join(HERE, "entry.jpg")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)

with open(SRC, "rb") as f:
    src_bytes = f.read()

with open(OUT, "rb") as f:
    out_bytes = f.read()

if len(out_bytes) > 1048576:
    print(f"Error: output size {len(out_bytes)} bytes exceeds 1 MiB gate (1048576 bytes)", file=sys.stderr)
    sys.exit(1)

if out_bytes != src_bytes:
    print("Error: output file does not match source entry.jpg byte-for-byte", file=sys.stderr)
    sys.exit(1)

sha256_sum = hashlib.sha256(out_bytes).hexdigest()
print(OUT)
print(f"sha256: {sha256_sum}")
