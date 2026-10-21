import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { TarotCard as TarotCardType, GachaPhase } from '../../types/tarot';
import { TarotDeck } from './TarotDeck';
import { TarotCard } from './TarotCard';
import { Button } from '../ui/Button';
import { Sparkles, Shuffle, Eye, RotateCcw } from 'lucide-react';
import styles from './TarotGachaSection.module.css';

interface TarotGachaSectionProps {
  phase: GachaPhase;
  currentCard: TarotCardType | null;
  isReversed: boolean;
  onShuffle: () => void;
  onReveal: () => void;
  onReset: () => void;
  reducedMotion?: boolean;
}

export const TarotGachaSection: React.FC<TarotGachaSectionProps> = ({
  phase,
  currentCard,
  isReversed,
  onShuffle,
  onReveal,
  onReset,
  reducedMotion = false,
}) => {
  // Phase description & instruction text
  const getInstruction = () => {
    switch (phase) {
      case 'idle':
        return 'Tarik napas perlahan, jernihkan pikiranmu, dan acak kartu tarot.';
      case 'shuffling':
        return 'Energi semesta sedang menyelaraskan takdir kartumu...';
      case 'flying':
        return 'Satu kartu telah terpilih dari kedalaman semesta!';
      case 'waiting-to-reveal':
        return 'Sentuh kartu atau tekan tombol untuk mengungkap misteri.';
      case 'revealing':
        return 'Membuka tabir nasib...';
      case 'revealed':
        return 'Kartumu telah terungkap. Temukan pesan di baliknya di bawah ini.';
      default:
        return '';
    }
  };

  const isDeckVisible = phase === 'idle' || phase === 'shuffling';
  const isFlying = phase === 'flying';
  const isCardVisible =
    phase === 'waiting-to-reveal' || phase === 'revealing' || phase === 'revealed';

  return (
    <section id="gacha-section" className={styles.gachaSection}>
      {/* Astrological circle decoration in background */}
      <div className={styles.celestialAura}>
        <div className={styles.astrologicalCircle} />
      </div>

      <div className={styles.contentContainer}>
        {/* Section Header */}
        <div className={styles.headerArea}>
          <div className={styles.eyebrow}>
            <Sparkles size={16} className={styles.sparkleIcon} />
            <span>PANGGILAN TAKDIR</span>
          </div>
          <h2 className={styles.sectionTitle}>Choose Your Destiny</h2>
          <p className={styles.instructionText} aria-live="polite">
            {getInstruction()}
          </p>
        </div>

        {/* Interactive Altar / Table Stage */}
        <div className={styles.altarStage}>
          {/* Ambient center spotlight */}
          <div className={styles.spotlightGlow} />

          {/* 1. Deck Area (Visible during idle / shuffling) */}
          <AnimatePresence mode="wait">
            {isDeckVisible && (
              <motion.div
                key="deck"
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.85, transition: { duration: 0.25 } }}
                className={styles.deckWrapper}
              >
                <TarotDeck
                  isShuffling={phase === 'shuffling'}
                  onClick={phase === 'idle' ? onShuffle : undefined}
                  disabled={phase === 'shuffling'}
                />
              </motion.div>
            )}
          </AnimatePresence>

          {/* 2. Flying Card Transition (Deck -> Center Altar) */}
          <AnimatePresence>
            {isFlying && (
              <motion.div
                key="flying-card"
                className={styles.flyingCardContainer}
                initial={
                  reducedMotion
                    ? { opacity: 0, scale: 0.5 }
                    : { y: -80, scale: 0.65, rotate: -25, opacity: 0 }
                }
                animate={
                  reducedMotion
                    ? { opacity: 1, scale: 1 }
                    : {
                        y: [ -80, -180, 0 ],
                        scale: [ 0.65, 1.15, 1 ],
                        rotate: [ -25, 15, 0 ],
                        opacity: [ 0, 1, 1 ],
                      }
                }
                transition={{
                  duration: 0.85,
                  ease: [0.22, 1, 0.36, 1],
                }}
              >
                <TarotCard card={null} isRevealed={false} size="lg" glow />
              </motion.div>
            )}
          </AnimatePresence>

          {/* 3. Revealed / Waiting to Reveal Card */}
          <AnimatePresence>
            {isCardVisible && (
              <motion.div
                key="revealed-card-slot"
                initial={{ opacity: 0, scale: 0.92 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.4 }}
                className={styles.revealedCardWrapper}
              >
                <TarotCard
                  card={currentCard}
                  isRevealed={phase === 'revealed'}
                  isReversed={isReversed}
                  onClick={phase === 'waiting-to-reveal' ? onReveal : undefined}
                  size="lg"
                  interactive={phase === 'waiting-to-reveal'}
                  glow={phase === 'waiting-to-reveal'}
                  showKeywords={phase === 'revealed'}
                />
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        {/* Action Controls */}
        <div className={styles.controlsArea}>
          {phase === 'idle' && (
            <Button
              variant="primary"
              size="lg"
              icon={<Shuffle size={18} />}
              onClick={onShuffle}
              glowEffect
            >
              Shuffle the Cards
            </Button>
          )}

          {phase === 'shuffling' && (
            <Button
              variant="primary"
              size="lg"
              isLoading
              disabled
            >
              Shuffling...
            </Button>
          )}

          {phase === 'waiting-to-reveal' && (
            <Button
              variant="primary"
              size="lg"
              icon={<Eye size={20} />}
              onClick={onReveal}
              glowEffect
              className={styles.revealPulseBtn}
            >
              Reveal Your Card
            </Button>
          )}

          {phase === 'revealing' && (
            <Button variant="secondary" size="lg" disabled isLoading>
              Opening Card...
            </Button>
          )}

          {phase === 'revealed' && (
            <div className={styles.revealedActions}>
              <Button
                variant="outline"
                size="md"
                icon={<RotateCcw size={16} />}
                onClick={onReset}
              >
                Tarik Kartu Lain
              </Button>
            </div>
          )}
        </div>
      </div>
    </section>
  );
};
