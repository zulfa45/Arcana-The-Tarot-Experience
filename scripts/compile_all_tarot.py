#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Tarot Compiler for Arcana
Compiles:
- deck_major.py
- deck_wands.py
- deck_cups.py
- deck_swords.py
- deck_pentacles.py
Into production TypeScript data files in src/data/ and src/data/readings/
"""

import os
import sys
import json

# Ensure scripts dir is on python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

from compiler_helpers import ts_str, format_card_entry, format_reading_entry, SRC_DATA_DIR, READINGS_DIR
from deck_major import MAJOR_ARCANA
from deck_wands import WANDS_CARDS
from deck_cups import CUPS_CARDS
from deck_swords import SWORDS_CARDS
from deck_pentacles import PENTACLES_CARDS

ALL_CARDS = MAJOR_ARCANA + WANDS_CARDS + CUPS_CARDS + SWORDS_CARDS + PENTACLES_CARDS
print(f"Total cards loaded for compilation: {len(ALL_CARDS)}")

# 1. Generate src/data/tarotCards.ts
card_lines = [
    "import { TarotCard } from '../types/tarot';",
    "",
    "/**",
    " * Complete Tarot Cards Dataset for Arcana (78 Cards)",
    " * Directly referencing assets in /assets/tarot/cards/",
    " */",
    "export const TAROT_CARDS: TarotCard[] = ["
]

for c in ALL_CARDS:
    card_lines.append(format_card_entry(c))

card_lines.append("];")
card_lines.append("")
card_lines.append("export const CARD_MAP = new Map<string, TarotCard>(")
card_lines.append("  TAROT_CARDS.map((c) => [c.id, c])")
card_lines.append(");")
card_lines.append("")
card_lines.append("export function getCardById(id: string): TarotCard | undefined {")
card_lines.append("  return CARD_MAP.get(id);")
card_lines.append("}")
card_lines.append("")
card_lines.append("export function getAllCards(): TarotCard[] {")
card_lines.append("  return TAROT_CARDS;")
card_lines.append("}")

tarot_cards_ts = "\n".join(card_lines)
with open(os.path.join(SRC_DATA_DIR, "tarotCards.ts"), "w", encoding="utf-8") as f:
    f.write(tarot_cards_ts)
print("Generated src/data/tarotCards.ts")

# Helper to write individual reading modules
def write_reading_module(filename, var_name, cards_subset, desc):
    lines = [
        "import { TarotCardReading } from '../../types/tarot';",
        "",
        f"/**",
        f" * {desc}",
        f" */",
        f"export const {var_name}: Record<string, TarotCardReading> = {{"
    ]
    for c in cards_subset:
        lines.append(format_reading_entry(c["id"], c["readings"]))
    lines.append("};")
    
    file_path = os.path.join(READINGS_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated src/data/readings/{filename}")

# 2. Write modules
write_reading_module("majorArcana.ts", "MAJOR_ARCANA_READINGS", MAJOR_ARCANA, "Major Arcana Readings (22 Cards, 7 Categories)")
write_reading_module("wands.ts", "WANDS_READINGS", WANDS_CARDS, "Suit of Wands Readings (14 Cards, 7 Categories)")
write_reading_module("cups.ts", "CUPS_READINGS", CUPS_CARDS, "Suit of Cups Readings (14 Cards, 7 Categories)")
write_reading_module("swords.ts", "SWORDS_READINGS", SWORDS_CARDS, "Suit of Swords Readings (14 Cards, 7 Categories)")
write_reading_module("pentacles.ts", "PENTACLES_READINGS", PENTACLES_CARDS, "Suit of Pentacles Readings (14 Cards, 7 Categories)")

# 3. Generate src/data/tarotReadings.ts (Combined map and lookup functions)
combined_lines = [
    "import {",
    "  TarotCardReading,",
    "  TarotInterpretation,",
    "  ReadingCategory,",
    "  CardOrientation,",
    "} from '../types/tarot';",
    "import { MAJOR_ARCANA_READINGS } from './readings/majorArcana';",
    "import { WANDS_READINGS } from './readings/wands';",
    "import { CUPS_READINGS } from './readings/cups';",
    "import { SWORDS_READINGS } from './readings/swords';",
    "import { PENTACLES_READINGS } from './readings/pentacles';",
    "",
    "/**",
    " * Consolidated Master Tarot Readings (78 Cards × 7 Categories = 546 bespoke Indonesian interpretations)",
    " */",
    "export const TAROT_READINGS: Record<string, TarotCardReading> = {",
    "  ...MAJOR_ARCANA_READINGS,",
    "  ...WANDS_READINGS,",
    "  ...CUPS_READINGS,",
    "  ...SWORDS_READINGS,",
    "  ...PENTACLES_READINGS,",
    "};",
    "",
    "export function getCardReading(cardId: string): TarotCardReading | undefined {",
    "  return TAROT_READINGS[cardId];",
    "}",
    "",
    "export function getCardInterpretation(",
    "  cardId: string,",
    "  category: ReadingCategory,",
    "  orientation: CardOrientation = 'upright'",
    "): TarotInterpretation | undefined {",
    "  const reading = TAROT_READINGS[cardId];",
    "  if (!reading) return undefined;",
    "",
    "  const interpretation = reading.interpretations[category];",
    "  if (!interpretation) return undefined;",
    "",
    "  // If reversed orientation is selected, add nuance to title and meaning if needed",
    "  if (orientation === 'reversed') {",
    "    return {",
    "      ...interpretation,",
    "      title: `${interpretation.title} (Terbalik)`,",
    "      summary: `[Aspek Terbalik] ${interpretation.summary} Perhatikan potensi hambatan atau perlunya refleksi batin lebih mendalam.`,",
    "      meaning: `Dalam posisi terbalik, energi kartu ini mengajakmu meninjau kembali bagian batin yang terhambat atau tertunda: ${interpretation.meaning}`,",
    "    };",
    "  }",
    "",
    "  return interpretation;",
    "}",
    ""
]

with open(os.path.join(SRC_DATA_DIR, "tarotReadings.ts"), "w", encoding="utf-8") as f:
    f.write("\n".join(combined_lines))
print("Generated src/data/tarotReadings.ts")

print("Master Compilation Finished Successfully!")
