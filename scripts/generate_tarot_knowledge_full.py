#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for complete 78 cards and all 7 categories
"""
import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")
READINGS_DIR = os.path.join(SRC_DATA_DIR, "readings")
os.makedirs(READINGS_DIR, exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

print("Generator script skeleton ready.")
