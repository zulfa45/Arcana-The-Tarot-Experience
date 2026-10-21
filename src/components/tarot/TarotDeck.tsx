import React from 'react';
import { motion } from 'framer-motion';
import styles from './TarotDeck.module.css';

interface TarotDeckProps {
  isShuffling?: boolean;
  onClick?: () => void;
  disabled?: boolean;
}

export const TarotDeck: React.FC<TarotDeckProps> = ({
  isShuffling = false,
  onClick,
  disabled = false,
}) => {
  const backCardPath = '/assets/tarot/back-card.jpg';

  // 6 stacked visual cards
  const deckCards = [
    { id: 1, offset: 0, rotate: 0 },
    { id: 2, offset: 2, rotate: -1.2 },
    { id: 3, offset: 4, rotate: 1.5 },
    { id: 4, offset: 6, rotate: -2 },
    { id: 5, offset: 8, rotate: 0.8 },
    { id: 6, offset: 10, rotate: 0 },
  ];

  return (
    <div
      className={`${styles.deckContainer} ${isShuffling ? styles.isShuffling : ''} ${
        disabled ? styles.isDisabled : ''
      }`}
      onClick={!disabled ? onClick : undefined}
      role="button"
      tabIndex={disabled ? -1 : 0}
      onKeyDown={(e) => {
        if (!disabled && (e.key === 'Enter' || e.key === ' ')) {
          e.preventDefault();
          onClick?.();
        }
      }}
      aria-label="Tumpukan Kartu Tarot Arcana"
    >
      <div className={styles.deckGlowRing} />

      <div className={styles.deckStack}>
        {deckCards.map((c, index) => {
          const isTopCard = index === deckCards.length - 1;

          // Animation variant for shuffling cards
          const shuffleAnimation = isShuffling
            ? {
                x: [0, (index % 2 === 0 ? 1 : -1) * (20 + index * 6), 0],
                y: [0, (index % 3 === 0 ? -12 : 8), 0],
                rotate: [c.rotate, (index % 2 === 0 ? 8 : -8), c.rotate],
                transition: {
                  repeat: Infinity,
                  duration: 0.45 + index * 0.05,
                  ease: 'easeInOut' as const,
                },
              }
            : {
                x: 0,
                y: -c.offset,
                rotate: c.rotate,
                transition: { duration: 0.3 },
              };

          return (
            <motion.div
              key={c.id}
              className={`${styles.cardInStack} ${isTopCard ? styles.topCard : ''}`}
              animate={shuffleAnimation}
              style={{
                zIndex: index,
              }}
            >
              <img
                src={backCardPath}
                alt="Punggung Kartu Tarot"
                className={styles.cardImage}
                onError={(e) => {
                  const target = e.currentTarget;
                  if (!target.src.endsWith('.png')) {
                    target.src = '/assets/tarot/back-card.png';
                  }
                }}
              />
              <div className={styles.cardBorderOverlay} />
            </motion.div>
          );
        })}
      </div>

      <div className={styles.deckShadow} />
    </div>
  );
};
