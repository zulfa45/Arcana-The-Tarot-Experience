#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")
READINGS_DIR = os.path.join(SRC_DATA_DIR, "readings")
os.makedirs(READINGS_DIR, exist_ok=True)

def ts_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)

def format_card_entry(c):
    suit_line = f"    suit: {ts_str(c['suit'])}," if c.get('suit') else ""
    rank_line = f"    rank: {ts_str(c['rank'])}," if c.get('rank') else ""
    num_line = f"    number: {c['number']}," if 'number' in c and c['number'] is not None else ""
    
    return f"""  {{
    id: {ts_str(c['id'])},
{num_line}
    name: {ts_str(c['name'])},
    slug: {ts_str(c['slug'])},
    image: {ts_str(c['image'])},
    arcana: {ts_str(c['arcana'])},
{suit_line}
{rank_line}
    uprightKeywords: {json.dumps(c['uprightKeywords'], ensure_ascii=False)},
    reversedKeywords: {json.dumps(c['reversedKeywords'], ensure_ascii=False)},
    description: {ts_str(c['description'])},
  }},"""

def format_reading_entry(card_id, r):
    cat_keys = ["love", "work", "career", "finance", "selfGrowth", "relationships", "spirituality"]
    cats_str = []
    for k in cat_keys:
        item = r[k]
        cats_str.append(f"""    {k}: {{
      title: {ts_str(item['title'])},
      summary: {ts_str(item['summary'])},
      meaning: {ts_str(item['meaning'])},
      advice: {ts_str(item['advice'])},
      reflectionQuestion: {ts_str(item['reflectionQuestion'])},
      keywords: {json.dumps(item['keywords'], ensure_ascii=False)},
    }},""")
    joined_cats = "\n".join(cats_str)
    return f"""  {ts_str(card_id)}: {{
    cardId: {ts_str(card_id)},
    orientation: 'upright',
    interpretations: {{
{joined_cats}
    }},
  }},"""

print("Base helper ready.")
