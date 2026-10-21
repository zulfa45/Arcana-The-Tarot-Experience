#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Tarot Knowledge Generator for Arcana — The Tarot Experience
Produces type-safe TypeScript files for all 78 tarot cards and 546 bespoke Indonesian interpretations.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DATA_DIR = os.path.join(BASE_DIR, "src", "data")
READINGS_DIR = os.path.join(SRC_DATA_DIR, "readings")
os.makedirs(READINGS_DIR, exist_ok=True)

def ts_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)

def build_card_ts(cards):
    lines = [
        "import { TarotCard } from '../types/tarot';",
        "",
        "/**",
        " * Complete Tarot Cards Dataset for Arcana (78 Cards)",
        " * Mapped directly to public/assets/tarot/cards/",
        " */",
        "export const TAROT_CARDS: TarotCard[] = ["
    ]
    for c in cards:
        suit_field = f"    suit: {ts_str(c['suit'])}," if c.get('suit') else ""
        rank_field = f"    rank: {ts_str(c['rank'])}," if c.get('rank') else ""
        num_field = f"    number: {c['number']}," if 'number' in c and c['number'] is not None else ""
        
        lines.append(f"""  {{
    id: {ts_str(c['id'])},
{num_field}
    name: {ts_str(c['name'])},
    slug: {ts_str(c['slug'])},
    image: {ts_str(c['image'])},
    arcana: {ts_str(c['arcana'])},
{suit_field}
{rank_field}
    uprightKeywords: {json.dumps(c['uprightKeywords'], ensure_ascii=False)},
    reversedKeywords: {json.dumps(c['reversedKeywords'], ensure_ascii=False)},
    description: {ts_str(c['description'])},
  }},""")
    lines.append("];")
    lines.append("")
    lines.append("export const CARD_MAP = new Map<string, TarotCard>(")
    lines.append("  TAROT_CARDS.map((c) => [c.id, c])")
    lines.append(");")
    lines.append("")
    lines.append("export function getCardById(id: string): TarotCard | undefined {")
    lines.append("  return CARD_MAP.get(id);")
    lines.append("}")
    return "\n".join(lines)

def build_reading_file(module_name, readings_dict, comment):
    lines = [
        "import { TarotCardReading } from '../../types/tarot';",
        "",
        f"/**",
        f" * {comment}",
        f" */",
        f"export const {module_name}: Record<string, TarotCardReading> = {{"
    ]
    categories = ["love", "work", "career", "finance", "selfGrowth", "relationships", "spirituality"]
    for card_id, reading in readings_dict.items():
        lines.append(f"  {ts_str(card_id)}: {{")
        lines.append(f"    cardId: {ts_str(card_id)},")
        lines.append("    orientation: 'upright',")
        lines.append("    interpretations: {")
        for cat in categories:
            interp = reading[cat]
            lines.append(f"      {cat}: {{")
            lines.append(f"        title: {ts_str(interp['title'])},")
            lines.append(f"        summary: {ts_str(interp['summary'])},")
            lines.append(f"        meaning: {ts_str(interp['meaning'])},")
            lines.append(f"        advice: {ts_str(interp['advice'])},")
            lines.append(f"        reflectionQuestion: {ts_str(interp['reflectionQuestion'])},")
            lines.append(f"        keywords: {json.dumps(interp['keywords'], ensure_ascii=False)},")
            lines.append("      },")
        lines.append("    },")
        lines.append("  },")
    lines.append("};")
    return "\n".join(lines)

print("Template builder initialized.")
