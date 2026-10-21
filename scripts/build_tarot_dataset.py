#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tarot Dataset Builder for Arcana
Generates comprehensive TypeScript data for all 78 Tarot Cards and
their 7-category Indonesian readings based on traditional RWS symbolism.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")
READINGS_DIR = os.path.join(SRC_DATA_DIR, "readings")

os.makedirs(READINGS_DIR, exist_ok=True)
print("Building Arcana Tarot Dataset...")
