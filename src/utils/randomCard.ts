import { TarotCard, CardOrientation } from '../types/tarot';
import { TAROT_CARDS } from '../data/tarotCards';

let lastDrawnCardId: string | null = null;

/**
 * Draws a random tarot card using uniform random distribution.
 * Prevents consecutive duplicates in back-to-back draws if more than 1 card is available.
 */
export function drawRandomCard(allowSameAsLast = false): TarotCard {
  if (TAROT_CARDS.length === 0) {
    throw new Error('Tarot card deck is empty.');
  }

  if (TAROT_CARDS.length === 1) {
    return TAROT_CARDS[0];
  }

  let candidates = TAROT_CARDS;
  if (!allowSameAsLast && lastDrawnCardId) {
    const filtered = TAROT_CARDS.filter((c) => c.id !== lastDrawnCardId);
    if (filtered.length > 0) {
      candidates = filtered;
    }
  }

  // Uniform random selection
  const randomIndex = Math.floor(Math.random() * candidates.length);
  const pickedCard = candidates[randomIndex];
  lastDrawnCardId = pickedCard.id;

  return pickedCard;
}

/**
 * Draws N unique random cards for the fan spread.
 */
export function drawMultipleRandomCards(count: number): TarotCard[] {
  if (TAROT_CARDS.length === 0) return [];
  const safeCount = Math.min(count, TAROT_CARDS.length);
  
  // Clone and shuffle using Fisher-Yates
  const shuffled = [...TAROT_CARDS];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }

  return shuffled.slice(0, safeCount);
}

/**
 * Determines card orientation based on configuration.
 * If allowReversed is true, ~25% chance of being reversed (standard traditional probability).
 */
export function determineCardOrientation(allowReversed = false): CardOrientation {
  if (!allowReversed) return 'upright';
  return Math.random() < 0.25 ? 'reversed' : 'upright';
}
