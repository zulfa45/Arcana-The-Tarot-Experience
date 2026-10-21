import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { TarotCard as TarotCardType, ReadingCategory } from '../../types/tarot';
import { TarotCard } from '../tarot/TarotCard';
import { getCardReading } from '../../data/tarotReadings';
import { TAROT_CATEGORIES } from '../../data/tarotCategories';
import { Modal } from '../ui/Modal';
import { Sparkles, Compass, Lightbulb, HelpCircle } from 'lucide-react';
import styles from './CardDetailModal.module.css';

interface CardDetailModalProps {
  card: TarotCardType | null;
  isOpen: boolean;
  onClose: () => void;
}

export const CardDetailModal: React.FC<CardDetailModalProps> = ({
  card,
  isOpen,
  onClose,
}) => {
  const [activeCategory, setActiveCategory] = useState<ReadingCategory>('love');

  if (!card) return null;

  const reading = getCardReading(card.id);
  const currentCategoryData = TAROT_CATEGORIES.find((c) => c.id === activeCategory);
  const currentInterp = reading?.interpretations[activeCategory];

  return (
    <Modal isOpen={isOpen} onClose={onClose} title={card.name} size="lg">
      <div className={styles.modalContent}>
        {/* Left Side: Card Visual & Badges */}
        <div className={styles.visualCol}>
          <div className={styles.cardFrameWrapper}>
            <TarotCard card={card} isRevealed={true} size="md" />
          </div>

          <div className={styles.metaBadgeBox}>
            <div className={styles.metaRow}>
              <span className={styles.metaLabel}>Arcana</span>
              <span className={styles.metaValue}>{card.arcana.toUpperCase()}</span>
            </div>
            {card.suit && (
              <div className={styles.metaRow}>
                <span className={styles.metaLabel}>Suit</span>
                <span className={styles.metaValue}>{card.suit.toUpperCase()}</span>
              </div>
            )}
            {card.rank && (
              <div className={styles.metaRow}>
                <span className={styles.metaLabel}>Rank</span>
                <span className={styles.metaValue}>{card.rank.toUpperCase()}</span>
              </div>
            )}
          </div>

          <div className={styles.keywordsBlock}>
            <span className={styles.keywordsTitle}>Kata Kunci Tegak:</span>
            <div className={styles.tagWrap}>
              {card.uprightKeywords.map((kw, i) => (
                <span key={i} className={styles.uprightBadge}>
                  {kw}
                </span>
              ))}
            </div>

            <span className={styles.keywordsTitle} style={{ marginTop: '10px' }}>
              Kata Kunci Terbalik:
            </span>
            <div className={styles.tagWrap}>
              {card.reversedKeywords.map((kw, i) => (
                <span key={i} className={styles.reversedBadge}>
                  {kw}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Right Side: Meanings & Category Exploration */}
        <div className={styles.detailsCol}>
          {/* General Overview */}
          <div className={styles.overviewBox}>
            <div className={styles.overviewTitle}>
              <Sparkles size={18} className={styles.sparkleIcon} />
              <h4>Makna Spiritual Utama</h4>
            </div>
            <p className={styles.generalText}>
              {card.description ||
                'Kartu ini sarat dengan simbol arketipe spiritual yang membimbing kesadaran hidup.'}
            </p>
          </div>

          {/* Category Tabs */}
          <div className={styles.categoryNav}>
            <span className={styles.categoryNavTitle}>Eksplorasi Dimensi Kehidupan:</span>
            <div className={styles.tabButtons}>
              {TAROT_CATEGORIES.map((cat) => (
                <button
                  key={cat.id}
                  onClick={() => setActiveCategory(cat.id)}
                  className={`${styles.tabBtn} ${
                    activeCategory === cat.id ? styles.tabBtnActive : ''
                  }`}
                >
                  {cat.name}
                </button>
              ))}
            </div>
          </div>

          {/* Tab Content Panel */}
          <AnimatePresence mode="wait">
            <motion.div
              key={activeCategory}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.2 }}
              className={styles.tabBody}
            >
              <div className={styles.infoGroup}>
                <div className={styles.infoTitle}>
                  <Compass size={16} className={styles.accentIcon} />
                  <h5>Interpretasi ({currentCategoryData?.name})</h5>
                </div>
                <p>{currentInterp?.meaning}</p>
              </div>

              <div className={styles.infoGroup}>
                <div className={styles.infoTitle}>
                  <Lightbulb size={16} className={styles.accentIcon} />
                  <h5>Saran Praktis</h5>
                </div>
                <p>{currentInterp?.advice}</p>
              </div>

              {currentInterp?.reflectionQuestion && (
                <div className={styles.questionsBox}>
                  <div className={styles.infoTitle}>
                    <HelpCircle size={16} className={styles.accentIcon} />
                    <h5>Refleksi Diri</h5>
                  </div>
                  <ul>
                    <li>✧ {currentInterp.reflectionQuestion}</li>
                  </ul>
                </div>
              )}
            </motion.div>
          </AnimatePresence>
        </div>
      </div>
    </Modal>
  );
};
