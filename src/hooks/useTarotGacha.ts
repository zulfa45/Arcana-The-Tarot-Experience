import { useState, useCallback, useRef, useEffect } from 'react';
import confetti from 'canvas-confetti';
import {
  GachaPhase,
  TarotCard,
  ReadingCategory,
  CardOrientation,
} from '../types/tarot';
import { drawMultipleRandomCards, determineCardOrientation } from '../utils/randomCard';
import { soundManager } from '../utils/sound';

export interface UseTarotGachaOptions {
  allowReversed?: boolean;
}

export function useTarotGacha(options: UseTarotGachaOptions = {}) {
  const [phase, setPhase] = useState<GachaPhase>('idle');
  const [card, setCard] = useState<TarotCard | null>(null);
  const [fannedCards, setFannedCards] = useState<TarotCard[]>([]);
  const [orientation, setOrientation] = useState<CardOrientation>('upright');
  const [selectedCategory, setSelectedCategory] = useState<ReadingCategory>('love');

  // Timers ref for clean unmount
  const timerRefs = useRef<NodeJS.Timeout[]>([]);

  const clearTimers = useCallback(() => {
    timerRefs.current.forEach(clearTimeout);
    timerRefs.current = [];
  }, []);

  useEffect(() => {
    return () => {
      clearTimers();
    };
  }, [clearTimers]);

  /**
   * Start shuffling and expand deck into a fan spread (jembereng kartu)
   */
  const startGacha = useCallback(() => {
    if (phase !== 'idle' && phase !== 'revealed') return;

    clearTimers();
    setPhase('shuffling');
    setCard(null);
    soundManager.playShuffle();

    // 1. Shuffling duration: 1200ms
    const shuffleTimer = setTimeout(() => {
      // Pick 9 random unique cards for the visual fan spread (clean & balanced)
      const spread = drawMultipleRandomCards(9);
      setFannedCards(spread);
      setPhase('fanned');
      soundManager.playFly();
    }, 1200);

    timerRefs.current.push(shuffleTimer);
  }, [phase, clearTimers]);

  /**
   * User picks one card directly from the fan spread
   */
  const pickCardFromFan = useCallback((pickedCard: TarotCard) => {
    if (phase !== 'fanned') return;

    clearTimers();
    const pickedOrientation = determineCardOrientation(options.allowReversed ?? false);
    setCard(pickedCard);
    setOrientation(pickedOrientation);
    setPhase('waiting-to-reveal');
    soundManager.playFly();

    // Auto trigger reveal flip right after picking from fan spread
    const autoRevealTimer = setTimeout(() => {
      setPhase('revealing');
      soundManager.playReveal();

      // Trigger celestial particle shower
      try {
        confetti({
          particleCount: 45,
          spread: 60,
          origin: { y: 0.65 },
          colors: ['#D9B56D', '#F0D9A0', '#9B7BFF', '#C5B5FF', '#FFFFFF'],
          disableForReducedMotion: true,
        });
      } catch {
        // Ignore if confetti not supported
      }

      // Complete 3D Flip animation duration: 800ms
      const flipTimer = setTimeout(() => {
        setPhase('revealed');
      }, 800);

      timerRefs.current.push(flipTimer);
    }, 450);

    timerRefs.current.push(autoRevealTimer);
  }, [phase, options.allowReversed, clearTimers]);

  /**
   * Manual reveal (if in waiting-to-reveal state)
   */
  const revealCard = useCallback(() => {
    if (phase !== 'waiting-to-reveal' || !card) return;

    setPhase('revealing');
    soundManager.playReveal();

    try {
      confetti({
        particleCount: 45,
        spread: 60,
        origin: { y: 0.65 },
        colors: ['#D9B56D', '#F0D9A0', '#9B7BFF', '#C5B5FF', '#FFFFFF'],
        disableForReducedMotion: true,
      });
    } catch {
      // Ignore if confetti not supported
    }

    const flipTimer = setTimeout(() => {
      setPhase('revealed');
    }, 800);

    timerRefs.current.push(flipTimer);
  }, [phase, card]);

  /**
   * Select life reading category
   */
  const selectCategory = useCallback((category: ReadingCategory) => {
    setSelectedCategory(category);
  }, []);

  /**
   * Reset session and draw another card immediately
   */
  const drawAnotherCard = useCallback(() => {
    clearTimers();
    setPhase('idle');
    setCard(null);
    setFannedCards([]);
    setOrientation('upright');
    setTimeout(() => {
      startGacha();
    }, 100);
  }, [clearTimers, startGacha]);

  /**
   * Reset to initial idle state (Kocok Ulang)
   */
  const resetSession = useCallback(() => {
    clearTimers();
    setPhase('idle');
    setCard(null);
    setFannedCards([]);
    setOrientation('upright');
    setSelectedCategory('love');
  }, [clearTimers]);

  return {
    phase,
    card,
    fannedCards,
    orientation,
    selectedCategory,
    startGacha,
    pickCardFromFan,
    revealCard,
    selectCategory,
    drawAnotherCard,
    resetSession,
  };
}
