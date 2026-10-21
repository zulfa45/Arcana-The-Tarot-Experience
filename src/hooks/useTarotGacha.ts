import { useState, useCallback, useRef, useEffect } from 'react';
import confetti from 'canvas-confetti';
import {
  GachaPhase,
  TarotCard,
  ReadingCategory,
  CardOrientation,
} from '../types/tarot';
import { drawRandomCard, determineCardOrientation } from '../utils/randomCard';
import { soundManager } from '../utils/sound';

export interface UseTarotGachaOptions {
  allowReversed?: boolean;
}

export function useTarotGacha(options: UseTarotGachaOptions = {}) {
  const [phase, setPhase] = useState<GachaPhase>('idle');
  const [card, setCard] = useState<TarotCard | null>(null);
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
   * Start shuffling and drawing sequence
   */
  const startGacha = useCallback(() => {
    if (phase !== 'idle' && phase !== 'revealed') return;

    clearTimers();
    setPhase('shuffling');
    soundManager.playShuffle();

    // 1. Shuffling duration: 1350ms
    const shuffleTimer = setTimeout(() => {
      // Pick random card & orientation
      const pickedCard = drawRandomCard();
      const pickedOrientation = determineCardOrientation(options.allowReversed ?? false);

      setCard(pickedCard);
      setOrientation(pickedOrientation);
      setPhase('flying');
      soundManager.playFly();

      // 2. Flying card trajectory & landing: 850ms
      const flyingTimer = setTimeout(() => {
        setPhase('waiting-to-reveal');
      }, 850);

      timerRefs.current.push(flyingTimer);
    }, 1350);

    timerRefs.current.push(shuffleTimer);
  }, [phase, options.allowReversed, clearTimers]);

  /**
   * Reveal the waiting face-down card with 3D flip animation
   */
  const revealCard = useCallback(() => {
    if (phase !== 'waiting-to-reveal' || !card) return;

    setPhase('revealing');
    soundManager.playReveal();

    // Trigger celestial particle shower
    try {
      confetti({
        particleCount: 40,
        spread: 60,
        origin: { y: 0.65 },
        colors: ['#D9B56D', '#F0D9A0', '#9B7BFF', '#C5B5FF', '#FFFFFF'],
        disableForReducedMotion: true,
      });
    } catch {
      // Ignore if confetti not supported
    }

    // 3. 3D Flip animation duration: 800ms
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
   * Reset session and draw another card
   */
  const drawAnotherCard = useCallback(() => {
    clearTimers();
    setPhase('idle');
    setCard(null);
    setOrientation('upright');
    // Start immediately
    setTimeout(() => {
      startGacha();
    }, 100);
  }, [clearTimers, startGacha]);

  /**
   * Reset to initial idle state
   */
  const resetSession = useCallback(() => {
    clearTimers();
    setPhase('idle');
    setCard(null);
    setOrientation('upright');
    setSelectedCategory('love');
  }, [clearTimers]);

  return {
    phase,
    card,
    orientation,
    selectedCategory,
    startGacha,
    revealCard,
    selectCategory,
    drawAnotherCard,
    resetSession,
  };
}
