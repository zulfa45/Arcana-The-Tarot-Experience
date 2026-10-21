import {
  TarotCardReading,
  TarotInterpretation,
  ReadingCategory,
  CardOrientation,
} from '../types/tarot';
import { MAJOR_ARCANA_READINGS } from './readings/majorArcana';
import { WANDS_READINGS } from './readings/wands';
import { CUPS_READINGS } from './readings/cups';
import { SWORDS_READINGS } from './readings/swords';
import { PENTACLES_READINGS } from './readings/pentacles';

/**
 * Consolidated Master Tarot Readings (78 Cards × 7 Categories = 546 bespoke Indonesian interpretations)
 */
export const TAROT_READINGS: Record<string, TarotCardReading> = {
  ...MAJOR_ARCANA_READINGS,
  ...WANDS_READINGS,
  ...CUPS_READINGS,
  ...SWORDS_READINGS,
  ...PENTACLES_READINGS,
};

export function getCardReading(cardId: string): TarotCardReading | undefined {
  return TAROT_READINGS[cardId];
}

export function getCardInterpretation(
  cardId: string,
  category: ReadingCategory,
  orientation: CardOrientation = 'upright'
): TarotInterpretation | undefined {
  const reading = TAROT_READINGS[cardId];
  if (!reading) return undefined;

  const interpretation = reading.interpretations[category];
  if (!interpretation) return undefined;

  // If reversed orientation is selected, add nuance to title and meaning if needed
  if (orientation === 'reversed') {
    return {
      ...interpretation,
      title: `${interpretation.title} (Terbalik)`,
      summary: `[Aspek Terbalik] ${interpretation.summary} Perhatikan potensi hambatan atau perlunya refleksi batin lebih mendalam.`,
      meaning: `Dalam posisi terbalik, energi kartu ini mengajakmu meninjau kembali bagian batin yang terhambat atau tertunda: ${interpretation.meaning}`,
    };
  }

  return interpretation;
}
