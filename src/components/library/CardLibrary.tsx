import React, { useState, useMemo } from 'react';
import { TarotCard as TarotCardType } from '../../types/tarot';
import { TAROT_CARDS } from '../../data/tarotCards';
import { TarotCard } from '../tarot/TarotCard';
import { CardDetailModal } from './CardDetailModal';
import { Modal } from '../ui/Modal';
import { Search, Filter, BookOpen } from 'lucide-react';
import styles from './CardLibrary.module.css';

interface CardLibraryProps {
  isOpen: boolean;
  onClose: () => void;
}

type ArcanaFilter = 'all' | 'major' | 'minor' | 'wands' | 'cups' | 'swords' | 'pentacles';

export const CardLibrary: React.FC<CardLibraryProps> = ({ isOpen, onClose }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [activeFilter, setActiveFilter] = useState<ArcanaFilter>('all');
  const [selectedCard, setSelectedCard] = useState<TarotCardType | null>(null);

  const filteredCards = useMemo(() => {
    return TAROT_CARDS.filter((c) => {
      // Filter criteria
      let matchesFilter = true;
      if (activeFilter === 'major') matchesFilter = c.arcana === 'major';
      else if (activeFilter === 'minor') matchesFilter = c.arcana === 'minor';
      else if (['wands', 'cups', 'swords', 'pentacles'].includes(activeFilter)) {
        matchesFilter = c.suit === activeFilter;
      }

      if (!matchesFilter) return false;

      // Search criteria
      if (!searchTerm.trim()) return true;
      const term = searchTerm.toLowerCase();
      const inName = c.name.toLowerCase().includes(term);
      const inUpright = c.uprightKeywords.some((k) => k.toLowerCase().includes(term));
      const inReversed = c.reversedKeywords.some((k) => k.toLowerCase().includes(term));

      return inName || inUpright || inReversed;
    });
  }, [searchTerm, activeFilter]);

  const filterButtons: { id: ArcanaFilter; label: string }[] = [
    { id: 'all', label: 'Semua (78)' },
    { id: 'major', label: 'Major Arcana (22)' },
    { id: 'wands', label: 'Wands (14)' },
    { id: 'cups', label: 'Cups (14)' },
    { id: 'swords', label: 'Swords (14)' },
    { id: 'pentacles', label: 'Pentacles (14)' },
  ];

  return (
    <>
      <Modal isOpen={isOpen} onClose={onClose} title="Koleksi Kartu Tarot" size="xl">
        <div className={styles.libraryContainer}>
          {/* Controls Bar: Search & Filter */}
          <div className={styles.controlsBar}>
            {/* Search Input */}
            <div className={styles.searchBox}>
              <Search size={18} className={styles.searchIcon} />
              <input
                type="text"
                placeholder="Cari kartu berdasarkan nama atau kata kunci..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className={styles.searchInput}
              />
            </div>

            {/* Filter Pills */}
            <div className={styles.filterPills}>
              <Filter size={16} className={styles.filterIcon} />
              {filterButtons.map((btn) => (
                <button
                  key={btn.id}
                  onClick={() => setActiveFilter(btn.id)}
                  className={`${styles.filterPill} ${
                    activeFilter === btn.id ? styles.activeFilter : ''
                  }`}
                >
                  {btn.label}
                </button>
              ))}
            </div>
          </div>

          {/* Result Count Banner */}
          <div className={styles.resultBanner}>
            <span>
              Menampilkan <strong>{filteredCards.length}</strong> dari 78 kartu tarot
            </span>
          </div>

          {/* Cards Grid */}
          <div className={styles.cardsGrid}>
            {filteredCards.map((card) => (
              <div
                key={card.id}
                className={styles.cardItem}
                onClick={() => setSelectedCard(card)}
              >
                <div className={styles.miniCardWrapper}>
                  <TarotCard card={card} isRevealed={true} size="sm" interactive />
                </div>
                <div className={styles.cardItemInfo}>
                  <span className={styles.itemTitle}>{card.name}</span>
                  <span className={styles.itemArcana}>
                    {card.arcana === 'major' ? 'Major Arcana' : card.suit}
                  </span>
                </div>
              </div>
            ))}
          </div>

          {filteredCards.length === 0 && (
            <div className={styles.emptyState}>
              <BookOpen size={48} className={styles.emptyIcon} />
              <h4>Tidak ada kartu yang cocok</h4>
              <p>Coba gunakan kata kunci pencarian yang lain.</p>
            </div>
          )}
        </div>
      </Modal>

      {/* Detail Modal when a card in library is clicked */}
      <CardDetailModal
        card={selectedCard}
        isOpen={!!selectedCard}
        onClose={() => setSelectedCard(null)}
      />
    </>
  );
};
