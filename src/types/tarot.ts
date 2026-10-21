export type ArcanaType = 'major' | 'minor';
export type TarotSuit = 'wands' | 'cups' | 'swords' | 'pentacles';
export type CardOrientation = 'upright' | 'reversed';

export type ReadingCategory =
  | 'love'
  | 'work'
  | 'career'
  | 'finance'
  | 'selfGrowth'
  | 'relationships'
  | 'spirituality';

export interface TarotCard {
  id: string;
  number?: number;
  name: string;
  slug: string;
  image: string;
  arcana: ArcanaType;
  suit?: TarotSuit;
  rank?: string;
  uprightKeywords: string[];
  reversedKeywords: string[];
  description: string;
}

export interface TarotInterpretation {
  title: string;
  summary: string;
  meaning: string;
  advice: string;
  reflectionQuestion: string;
  keywords: string[];
}

export interface TarotCardReading {
  cardId: string;
  orientation: CardOrientation;
  interpretations: Record<ReadingCategory, TarotInterpretation>;
}

export interface SavedReading {
  id: string;
  timestamp: number;
  cardId: string;
  cardName: string;
  cardImage: string;
  arcana: ArcanaType;
  orientation: CardOrientation;
  category: ReadingCategory;
  categoryName: string;
  title: string;
  summary: string;
  meaning: string;
  advice: string;
  reflectionQuestion: string;
  keywords: string[];
}

export interface CategoryInfo {
  id: ReadingCategory;
  name: string;
  englishName: string;
  description: string;
  iconName: 'Heart' | 'Briefcase' | 'Compass' | 'Coins' | 'Sparkles' | 'Users' | 'Moon';
}

export type GachaPhase =
  | 'idle'
  | 'shuffling'
  | 'flying'
  | 'waiting-to-reveal'
  | 'revealing'
  | 'revealed';
