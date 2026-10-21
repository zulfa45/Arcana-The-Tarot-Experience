#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Tarot Knowledge Base Generator for Arcana — The Tarot Experience
Generates:
  - src/data/tarotCards.ts
  - src/data/readings/majorArcana.ts
  - src/data/readings/wands.ts
  - src/data/readings/cups.ts
  - src/data/readings/swords.ts
  - src/data/readings/pentacles.ts
  - src/data/tarotReadings.ts
"""

import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")
READINGS_DIR = os.path.join(SRC_DATA_DIR, "readings")
os.makedirs(READINGS_DIR, exist_ok=True)

def ts_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)

def write_ts_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {os.path.relpath(path, BASE_DIR)}")

print("Builder environment ready.")
