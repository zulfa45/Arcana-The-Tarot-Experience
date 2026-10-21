import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { TarotCard as TarotCardType } from '../../types/tarot';
import { Eye, Sparkles } from 'lucide-react';
import styles from './TarotCard.module.css';

interface TarotCardProps {
  card?: TarotCardType | null;
  isRevealed?: boolean;
  isReversed?: boolean;
  onClick?: () => void;
  size?: 'sm' | 'md' | 'lg';
  interactive?: boolean;
  showKeywords?: boolean;
  className?: string;
  glow?: boolean;
}

export const TarotCard: React.FC<TarotCardProps> = ({
  card,
  isRevealed = false,
  isReversed = false,
  onClick,
  size = 'md',
  interactive = false,
  showKeywords = false,
  className = '',
  glow = false,
}) => {
  const [imageError, setImageError] = useState(false);

  const backCardPath = '/assets/tarot/back-card.jpg';

  const sizeClasses = {
    sm: styles.sizeSm,
    md: styles.sizeMd,
    lg: styles.sizeLg,
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (interactive && (e.key === 'Enter' || e.key === ' ')) {
      e.preventDefault();
      onClick?.();
    }
  };

  return (
    <div
      className={`${styles.cardWrapper} ${sizeClasses[size]} ${className}`}
      onClick={interactive ? onClick : undefined}
      onKeyDown={handleKeyDown}
      role={interactive ? 'button' : 'figure'}
      tabIndex={interactive ? 0 : -1}
      aria-label={
        isRevealed && card
          ? `${card.name} (${card.arcana} arcana)${isReversed ? ' - Terbalik (Reversed)' : ' - Tegak (Upright)'}`
          : 'Kartu Tarot Tertutup'
      }
    >
      <div
        className={`${styles.card3d} ${isRevealed ? styles.isFlipped : ''} ${
          glow ? styles.cardGlow : ''
        } ${interactive ? styles.isInteractive : ''}`}
      >
        {/* SISI BELAKANG (Back of the Card - Shown when face-down) */}
        <div className={`${styles.cardFace} ${styles.cardBack}`}>
          <div className={styles.cardFrame}>
            <img
              src={backCardPath}
              alt="Punggung Kartu Tarot Arcana"
              className={styles.cardImage}
              loading="eager"
              onError={(e) => {
                // Fallback to png if jpg fails
                const target = e.currentTarget;
                if (!target.src.endsWith('.png')) {
                  target.src = '/assets/tarot/back-card.png';
                }
              }}
            />
            {interactive && !isRevealed && (
              <div className={styles.revealHint}>
                <Eye className={styles.revealIcon} size={22} />
                <span>Ketuk untuk Membuka</span>
              </div>
            )}
          </div>
        </div>

        {/* SISI DEPAN (Front of the Card - Shown when revealed) */}
        <div
          className={`${styles.cardFace} ${styles.cardFront} ${
            isReversed ? styles.isReversedCard : ''
          }`}
        >
          <div className={styles.cardFrame}>
            {card ? (
              imageError ? (
                <div className={styles.imageFallback}>
                  <Sparkles size={36} className={styles.fallbackIcon} />
                  <span className={styles.fallbackTitle}>{card.name}</span>
                  <span className={styles.fallbackSub}>{card.arcana.toUpperCase()} ARCANA</span>
                </div>
              ) : (
                <img
                  src={card.image}
                  alt={`${card.name} Tarot Card`}
                  className={styles.cardImage}
                  onError={() => {
                    console.warn(`[Arcana] Failed to load card image: ${card.image}`);
                    setImageError(true);
                  }}
                  loading="eager"
                />
              )
            ) : (
              <div className={styles.imageFallback}>
                <Sparkles size={36} className={styles.fallbackIcon} />
                <span>Kartu Misterius</span>
              </div>
            )}

            {/* Subtle ornate overlay corner highlights */}
            <div className={`${styles.cornerOrnament} ${styles.cornerTL}`} />
            <div className={`${styles.cornerOrnament} ${styles.cornerTR}`} />
            <div className={`${styles.cornerOrnament} ${styles.cornerBL}`} />
            <div className={`${styles.cornerOrnament} ${styles.cornerBR}`} />
          </div>

          {/* Optional bottom card label */}
          {card && (
            <div className={styles.cardFooter}>
              <span className={styles.cardName}>{card.name}</span>
              {isReversed && <span className={styles.reversedBadge}>Terbalik</span>}
            </div>
          )}
        </div>
      </div>

      {/* Keywords underneath card if enabled */}
      {showKeywords && isRevealed && card && (
        <motion.div
          className={styles.keywordsContainer}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          {(isReversed ? card.reversedKeywords : card.uprightKeywords)
            .slice(0, 3)
            .map((kw, i) => (
              <span key={i} className={styles.keywordTag}>
                {kw}
              </span>
            ))}
        </motion.div>
      )}
    </div>
  );
};
