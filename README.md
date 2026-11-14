# The World Today — news-image-01

The user's own infographic summing up the world's news of **Friday 13 November 2026** ("WORLD TODAY — 13 NOVEMBER 2026" in English), featuring 7 top stories:
1. US-Iran tensions
2. Gaza conflict
3. Ukraine peace talks
4. COP31 climate summit
5. Oil market developments
6. US-Mexico relations
7. Congo food crisis

Sources: Anadolu, Reuters, AP & Le Monde.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.jpg` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` when overridden). No network, no randomness, no clock. It performs post-write binary verification and gate assertions.

Outside the grader's container:
```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Gate Limits & Verification Results

- **Gate Limits:** Maximum 1 MiB (1,048,576 bytes) and maximum 1024×1024 pixels.
- **Dimensions:** 1024×1024 pixels (JPEG).
- **Byte Size:** 350,508 bytes (well within the 1 MiB limit).
- **SHA-256 Checksum:** `4c8f2545eceffa73b93c846cb94044e76820d26ac5a1c3a0fc1ea4a6f1343c2e`
- **Determinism:** Verified byte-for-byte identical across multiple execution runs (`cmp` confirmed zero differences).

## Notes

The old generated newspaper scene (peace talks / Nvidia / Microsoft) is superseded and kept solely as `entry-generated.png`.

## License

MIT — see `LICENSE`.
