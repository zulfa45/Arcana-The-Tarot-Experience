import React from 'react';
import { motion } from 'framer-motion';
import { Button } from '../ui/Button';
import { Sparkles, Compass, BookOpen } from 'lucide-react';
import styles from './HeroSection.module.css';

interface HeroSectionProps {
  onStartReading: () => void;
  onExploreCards: () => void;
}

export const HeroSection: React.FC<HeroSectionProps> = ({
  onStartReading,
  onExploreCards,
}) => {
  return (
    <section className={styles.heroSection}>
      {/* Background Celestial Glowing Orbs */}
      <div className={styles.ambientOrbLeft} />
      <div className={styles.ambientOrbRight} />

      <div className={styles.container}>
        {/* Text Content */}
        <motion.div
          className={styles.textContent}
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
        >
          <div className={styles.eyebrow}>
            <Sparkles size={16} className={styles.sparkle} />
            <span>YOUR PERSONAL TAROT EXPERIENCE</span>
          </div>

          <h1 className={styles.heading}>
            Let the Cards Reveal <br />
            <span className={styles.goldGradient}>Their Story</span>
          </h1>

          <p className={styles.description}>
            Take a moment, trust your intuition, and discover a new perspective through the
            ancient symbolism of tarot.
          </p>

          <div className={styles.ctaGroup}>
            <Button
              variant="primary"
              size="lg"
              icon={<Compass size={18} />}
              onClick={onStartReading}
              glowEffect
            >
              Begin Your Reading
            </Button>
            <Button
              variant="outline"
              size="lg"
              icon={<BookOpen size={18} />}
              onClick={onExploreCards}
            >
              Explore the Cards
            </Button>
          </div>
        </motion.div>

        {/* Visual Mystical Illustration / Hero Deck Showcase */}
        <motion.div
          className={styles.visualContent}
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
        >
          <div className={styles.celestialRings}>
            <div className={styles.outerRing} />
            <div className={styles.innerRing} />
          </div>

          <div className={styles.cardsShowcase}>
            {/* Left Fan Card */}
            <div className={`${styles.fanCard} ${styles.fanLeft}`}>
              <img
                src="/assets/tarot/back-card.jpg"
                alt="Tarot Back"
                className={styles.showcaseImg}
                onError={(e) => {
                  const target = e.currentTarget;
                  if (!target.src.endsWith('.png')) {
                    target.src = '/assets/tarot/back-card.png';
                  }
                }}
              />
            </div>

            {/* Center Glowing Card (The Star or The Magician as iconic tarot symbol) */}
            <div className={`${styles.fanCard} ${styles.fanCenter}`}>
              <img
                src="/assets/tarot/cards/The Star.jpg"
                alt="The Star Tarot Card"
                className={styles.showcaseImg}
              />
              <div className={styles.centerGlowRing} />
            </div>

            {/* Right Fan Card */}
            <div className={`${styles.fanCard} ${styles.fanRight}`}>
              <img
                src="/assets/tarot/back-card.jpg"
                alt="Tarot Back"
                className={styles.showcaseImg}
                onError={(e) => {
                  const target = e.currentTarget;
                  if (!target.src.endsWith('.png')) {
                    target.src = '/assets/tarot/back-card.png';
                  }
                }}
              />
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};
