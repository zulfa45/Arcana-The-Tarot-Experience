import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { TarotCard as TarotCardType, GachaPhase } from '../../types/tarot';
import { TarotDeck } from './TarotDeck';
import { TarotCard } from './TarotCard';
import { TarotFanSpread } from './TarotFanSpread';
import { Button } from '../ui/Button';
import { Sparkles, Shuffle, RotateCcw } from 'lucide-react';
import styles from './TarotGachaSection.module.css';

interface TarotGachaSectionProps {
  phase: GachaPhase;
  currentCard: TarotCardType | null;
  fannedCards?: TarotCardType[];
  isReversed: boolean;
  onShuffle: () => void;
  onPickCardFromFan: (card: TarotCardType) => void;
  onReveal: () => void;
  onReset: () => void;
  reducedMotion?: boolean;
}

export const TarotGachaSection: React.FC<TarotGachaSectionProps> = ({
  phase,
  currentCard,
  fannedCards = [],
  isReversed,
  onShuffle,
  onPickCardFromFan,
  onReset,
  reducedMotion = false,
}) => {
  // Phase description & instruction text
  const getInstruction = () => {
    switch (phase) {
      case 'idle':
        return 'Tarik napas perlahan, jernihkan pikiranmu, dan kocok kartu tarot.';
      case 'shuffling':
        return 'Energi semesta sedang mengocok dan menyelaraskan kartumu...';
      case 'fanned':
        return 'Pilih 1 kartu yang memanggil intuisimu dari jemberengan di bawah.';
      case 'flying':
      case 'waiting-to-reveal':
        return 'Menarik kartu pilihanmu ke tengah altar...';
      case 'revealing':
        return 'Membuka tabir nasib...';
      case 'revealed':
        return 'Kartumu telah terungkap! Temukan pesan arketipenya di bawah ini.';
      default:
        return '';
    }
  };

  const isDeckVisible = phase === 'idle' || phase === 'shuffling';
  const isFannedVisible = phase === 'fanned';
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

          {/* 2. Jembereng Kartu (Fan Spread Area - User chooses 1 card) */}
          <AnimatePresence mode="wait">
            {isFannedVisible && (
              <motion.div
                key="fan-spread"
                initial={{ opacity: 0, scale: 0.85, y: 30 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                exit={{ opacity: 0, scale: 0.9, transition: { duration: 0.3 } }}
                className={styles.fanSpreadWrapper}
              >
                <TarotFanSpread
                  cards={fannedCards}
                  onSelectCard={(selected) => onPickCardFromFan(selected)}
                  disabled={phase !== 'fanned'}
                />
              </motion.div>
            )}
          </AnimatePresence>

          {/* 3. Revealed / Waiting to Reveal Card (After user picks from fan) */}
          <AnimatePresence>
            {isCardVisible && currentCard && (
              <motion.div
                key="revealed-card-slot"
                initial={
                  reducedMotion
                    ? { opacity: 0, scale: 0.9 }
                    : { opacity: 0, scale: 0.7, y: 40 }
                }
                animate={{ opacity: 1, scale: 1, y: 0 }}
                transition={{ duration: 0.5, type: 'spring', stiffness: 140, damping: 16 }}
                className={styles.revealedCardWrapper}
              >
                <TarotCard
                  card={currentCard}
                  isRevealed={phase === 'revealed'}
                  isReversed={isReversed}
                  size="lg"
                  interactive={false}
                  glow={phase === 'revealed'}
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
              Kocok Kartu
            </Button>
          )}

          {phase === 'shuffling' && (
            <Button
              variant="primary"
              size="lg"
              isLoading
              disabled
            >
              Mengocok Kartu...
            </Button>
          )}

          {phase === 'fanned' && (
            <div className={styles.fannedInstructionBox}>
              <span className={styles.fannedHint}>✦ Sentuh salah satu kartu untuk membukanya ✦</span>
              <Button
                variant="outline"
                size="sm"
                icon={<RotateCcw size={15} />}
                onClick={onReset}
              >
                Kocok Ulang
              </Button>
            </div>
          )}

          {(phase === 'waiting-to-reveal' || phase === 'revealing') && (
            <Button variant="secondary" size="lg" disabled isLoading>
              Membuka Kartu Pilihanmu...
            </Button>
          )}

          {phase === 'revealed' && (
            <div className={styles.revealedActions}>
              <Button
                variant="primary"
                size="lg"
                icon={<RotateCcw size={18} />}
                onClick={onReset}
                glowEffect
              >
                Kocok Ulang
              </Button>
            </div>
          )}
        </div>
      </div>
    </section>
  );
};
