#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")
READINGS_DIR = os.path.join(SRC_DATA_DIR, "readings")
os.makedirs(READINGS_DIR, exist_ok=True)

# We will define the comprehensive dataset for Major Arcana, Wands, Cups, Swords, Pentacles
# Each item will have:
# id, number, name, slug, image, arcana, suit, rank, uprightKeywords, reversedKeywords, description, readings (7 categories)
