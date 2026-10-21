import React from 'react';
import { motion } from 'framer-motion';
import { TarotCard as TarotCardType } from '../../types/tarot';
import styles from './TarotFanSpread.module.css';

interface TarotFanSpreadProps {
  cards: TarotCardType[];
  onSelectCard: (card: TarotCardType, index: number) => void;
  disabled?: boolean;
  selectedCardId?: string | null;
}

export const TarotFanSpread: React.FC<TarotFanSpreadProps> = ({
  cards,
  onSelectCard,
  disabled = false,
  selectedCardId = null,
}) => {
  const backCardPath = '/assets/tarot/back-card.jpg';
  const total = cards.length;

  return (
    <div className={styles.fanContainer} role="region" aria-label="Jemberengan Kartu Tarot">
      <div className={styles.fanArc}>
        {cards.map((card, index) => {
          // Calculate angle spread across a gentle arc, centered around 0
          // e.g. for 9 cards, angles range from -36deg to +36deg in steps of 9deg
          const centerIndex = (total - 1) / 2;
          const offsetFromCenter = index - centerIndex;
          const rotateDeg = offsetFromCenter * 8.5; // angle per card
          const translateY = Math.abs(offsetFromCenter) * 10; // arc curvature
          const translateX = offsetFromCenter * 34; // horizontal spacing overlap

          const isSelected = selectedCardId === card.id;

          return (
            <motion.div
              key={card.id || index}
              className={`${styles.fanCardWrapper} ${isSelected ? styles.isSelected : ''} ${
                disabled && !isSelected ? styles.isDisabled : ''
              }`}
              style={{
                zIndex: index + 1,
              }}
              initial={{
                opacity: 0,
                scale: 0.6,
                x: 0,
                y: 60,
                rotate: 0,
              }}
              animate={
                isSelected
                  ? {
                      opacity: 0,
                      scale: 1.1,
                      y: -100,
                      rotate: 0,
                      transition: { duration: 0.4 },
                    }
                  : {
                      opacity: 1,
                      scale: 1,
                      x: translateX,
                      y: translateY,
                      rotate: rotateDeg,
                      transition: {
                        type: 'spring',
                        stiffness: 120,
                        damping: 14,
                        delay: index * 0.04,
                      },
                    }
              }
              whileHover={
                !disabled
                  ? {
                      y: translateY - 28,
                      scale: 1.08,
                      zIndex: 50,
                      transition: { duration: 0.2 },
                    }
                  : {}
              }
              whileTap={!disabled ? { scale: 0.98 } : {}}
              onClick={() => {
                if (!disabled) {
                  onSelectCard(card, index);
                }
              }}
              role="button"
              tabIndex={disabled ? -1 : 0}
              onKeyDown={(e) => {
                if (!disabled && (e.key === 'Enter' || e.key === ' ')) {
                  e.preventDefault();
                  onSelectCard(card, index);
                }
              }}
              aria-label={`Pilih Kartu Tarot ke-${index + 1}`}
            >
              <div className={styles.cardInner}>
                <img
                  src={backCardPath}
                  alt="Punggung Kartu Tarot"
                  className={styles.cardBackImage}
                  onError={(e) => {
                    const target = e.currentTarget;
                    if (!target.src.endsWith('.png')) {
                      target.src = '/assets/tarot/back-card.png';
                    }
                  }}
                />
                <div className={styles.cardSheen} />
                <div className={styles.cardBorder} />
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
};
