import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { TarotCard as TarotCardType, ReadingCategory } from '../../types/tarot';
import { getCardReading } from '../../data/tarotReadings';
import { TAROT_CATEGORIES } from '../../data/tarotCategories';
import { ReadingCategorySelector } from './ReadingCategorySelector';
import { Button } from '../ui/Button';
import { Bookmark, Check, Share2, Sparkles, HelpCircle, Compass, Lightbulb } from 'lucide-react';
import styles from './ReadingResult.module.css';

interface ReadingResultProps {
  card: TarotCardType;
  isReversed: boolean;
  selectedCategory: ReadingCategory;
  onSelectCategory: (cat: ReadingCategory) => void;
  onSaveReading?: (category: ReadingCategory, notes?: string) => void;
  isSaved?: boolean;
}

export const ReadingResult: React.FC<ReadingResultProps> = ({
  card,
  isReversed,
  selectedCategory,
  onSelectCategory,
  onSaveReading,
  isSaved = false,
}) => {
  const [copied, setCopied] = useState(false);
  const [justSaved, setJustSaved] = useState(false);

  const reading = getCardReading(card.id);
  const currentCategoryData = TAROT_CATEGORIES.find((c) => c.id === selectedCategory);
  const currentInterpretation = reading?.interpretations[selectedCategory];

  const handleSave = () => {
    if (onSaveReading && !isSaved && !justSaved) {
      onSaveReading(selectedCategory);
      setJustSaved(true);
      setTimeout(() => setJustSaved(false), 3000);
    }
  };

  const handleShare = async () => {
    const text = `Arcana Tarot Reading: Aku menarik kartu ${card.name} (${
      isReversed ? 'Terbalik' : 'Tegak'
    }) untuk fokus ${currentCategoryData?.name || 'Kehidupan'}. "${
      currentInterpretation?.meaning || card.description
    }"`;

    if (navigator.share) {
      try {
        await navigator.share({
          title: `Arcana Tarot — ${card.name}`,
          text: text,
          url: window.location.href,
        });
        return;
      } catch {
        // Fallback to clipboard
      }
    }

    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch {
      console.warn('Failed to copy text');
    }
  };

  return (
    <section className={styles.resultSection} id="reading-result" aria-label="Hasil Pembacaan Tarot">
      <div className={styles.container}>
        {/* Card Identity Header Banner */}
        <div className={styles.cardHeaderBanner}>
          <div className={styles.bannerInfo}>
            <span className={styles.arcanaBadge}>
              {card.arcana.toUpperCase()} ARCANA {card.suit ? `• ${card.suit.toUpperCase()}` : ''}
            </span>
            <h2 className={styles.cardTitle}>{card.name}</h2>
            <div className={styles.orientationStatus}>
              {isReversed ? (
                <span className={styles.reversedTag}>Posisi Terbalik (Reversed)</span>
              ) : (
                <span className={styles.uprightTag}>Posisi Tegak (Upright)</span>
              )}
            </div>
          </div>

          <div className={styles.bannerActions}>
            <Button
              variant="outline"
              size="sm"
              icon={isSaved || justSaved ? <Check size={16} /> : <Bookmark size={16} />}
              onClick={handleSave}
              disabled={isSaved || justSaved}
            >
              {isSaved || justSaved ? 'Tersimpan di Riwayat' : 'Simpan Pembacaan'}
            </Button>
            <Button
              variant="ghost"
              size="sm"
              icon={<Share2 size={16} />}
              onClick={handleShare}
            >
              {copied ? 'Tersalin!' : 'Bagikan'}
            </Button>
          </div>
        </div>

        {/* General Overview Card */}
        <div className={styles.overviewCard}>
          <div className={styles.overviewHeader}>
            <Sparkles size={20} className={styles.accentIcon} />
            <h3>Makna Utama</h3>
          </div>
          <p className={styles.generalMeaningText}>
            {card.description ||
              'Kartu ini melambangkan titik balik dalam perjalanan hidupmu.'}
          </p>

          <div className={styles.keywordsList}>
            <span className={styles.keywordsTitle}>Kata Kunci:</span>
            {(isReversed ? card.reversedKeywords : card.uprightKeywords).map((kw, i) => (
              <span key={i} className={styles.keywordBadge}>
                {kw}
              </span>
            ))}
          </div>
        </div>

        {/* Category Selector Chips */}
        <ReadingCategorySelector
          selectedCategory={selectedCategory}
          onSelectCategory={onSelectCategory}
        />

        {/* Dynamic Category Interpretation Panel */}
        <AnimatePresence mode="wait">
          <motion.div
            key={selectedCategory}
            initial={{ opacity: 0, y: 14 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -14 }}
            transition={{ duration: 0.3 }}
            className={styles.interpretationPanel}
          >
            <div className={styles.interpretationHeader}>
              <div className={styles.categoryTitleGroup}>
                <span className={styles.categoryTag}>{currentCategoryData?.name}</span>
                <h3 className={styles.interpretationHeading}>
                  {currentInterpretation?.title || `Panduan ${currentCategoryData?.name}`}
                </h3>
              </div>
            </div>

            {/* Meaning Section */}
            <div className={styles.sectionBlock}>
              <div className={styles.sectionTitleRow}>
                <Compass size={18} className={styles.blockIcon} />
                <h4>Interpretasi</h4>
              </div>
              <p className={styles.sectionBody}>
                {currentInterpretation?.meaning ||
                  'Renungkan pesan kartu ini dengan situasi hidupmu saat ini.'}
              </p>
            </div>

            {/* Advice Section */}
            <div className={styles.sectionBlock}>
              <div className={styles.sectionTitleRow}>
                <Lightbulb size={18} className={styles.blockIcon} />
                <h4>Saran & Arah Tindakan</h4>
              </div>
              <p className={styles.sectionBody}>
                {currentInterpretation?.advice ||
                  'Ambil langkah bijak dan dengarkan intuisi terdalammu.'}
              </p>
            </div>

            {/* Reflection Questions */}
            {currentInterpretation?.reflectionQuestion && (
              <div className={styles.reflectionBlock}>
                <div className={styles.sectionTitleRow}>
                  <HelpCircle size={18} className={styles.blockIcon} />
                  <h4>Pertanyaan untuk Refleksi</h4>
                </div>
                <ul className={styles.questionsList}>
                  <li className={styles.questionItem}>
                    <span className={styles.questionBullet}>✧</span>
                    <span>{currentInterpretation.reflectionQuestion}</span>
                  </li>
                </ul>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </div>
    </section>
  );
};
