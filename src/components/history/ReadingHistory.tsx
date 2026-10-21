import React, { useState } from 'react';
import { SavedReading, TarotCard as TarotCardType } from '../../types/tarot';
import { TAROT_CARDS } from '../../data/tarotCards';
import { TAROT_CATEGORIES } from '../../data/tarotCategories';
import { Modal } from '../ui/Modal';
import { Button } from '../ui/Button';
import { CardDetailModal } from '../library/CardDetailModal';
import { History, Trash2, Calendar, Compass } from 'lucide-react';
import styles from './ReadingHistory.module.css';

interface ReadingHistoryProps {
  isOpen: boolean;
  onClose: () => void;
  history: SavedReading[];
  onDeleteReading: (id: string) => void;
  onClearHistory: () => void;
}

export const ReadingHistory: React.FC<ReadingHistoryProps> = ({
  isOpen,
  onClose,
  history,
  onDeleteReading,
  onClearHistory,
}) => {
  const [selectedCardForDetail, setSelectedCardForDetail] = useState<TarotCardType | null>(null);

  const formatDate = (timestamp: number) => {
    try {
      const d = new Date(timestamp);
      return new Intl.DateTimeFormat('id-ID', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      }).format(d);
    } catch {
      return '';
    }
  };

  const handleCardClick = (cardId: string) => {
    const found = TAROT_CARDS.find((c) => c.id === cardId);
    if (found) {
      setSelectedCardForDetail(found);
    }
  };

  return (
    <>
      <Modal isOpen={isOpen} onClose={onClose} title="Riwayat Pembacaan Tarot" size="lg">
        <div className={styles.historyContainer}>
          {/* Header Action Bar */}
          {history.length > 0 && (
            <div className={styles.actionBar}>
              <span className={styles.countText}>
                Total <strong>{history.length}</strong> pembacaan tersimpan
              </span>
              <Button
                variant="ghost"
                size="sm"
                icon={<Trash2 size={15} />}
                onClick={() => {
                  if (window.confirm('Hapus seluruh riwayat pembacaan tarot?')) {
                    onClearHistory();
                  }
                }}
              >
                Hapus Semua
              </Button>
            </div>
          )}

          {/* History Item List */}
          {history.length > 0 ? (
            <div className={styles.historyList}>
              {history.map((item) => {
                const categoryObj = TAROT_CATEGORIES.find((c) => c.id === item.category);
                const isItemReversed = item.orientation === 'reversed';

                return (
                  <div key={item.id} className={styles.historyCard}>
                    {/* Thumbnail */}
                    <div
                      className={styles.thumbnailBox}
                      onClick={() => handleCardClick(item.cardId)}
                      role="button"
                      tabIndex={0}
                      title="Klik untuk melihat detail kartu"
                    >
                      <img
                        src={item.cardImage}
                        alt={item.cardName}
                        className={styles.thumbImage}
                        style={{
                          transform: isItemReversed ? 'rotate(180deg)' : 'none',
                        }}
                      />
                    </div>

                    {/* Content */}
                    <div className={styles.itemContent}>
                      <div className={styles.titleRow}>
                        <h4
                          className={styles.cardNameLink}
                          onClick={() => handleCardClick(item.cardId)}
                        >
                          {item.cardName}
                        </h4>
                        <span
                          className={isItemReversed ? styles.badgeReversed : styles.badgeUpright}
                        >
                          {isItemReversed ? 'Terbalik' : 'Tegak'}
                        </span>
                      </div>

                      <div className={styles.categoryInfo}>
                        <Compass size={14} className={styles.iconGold} />
                        <span>Fokus: {categoryObj?.name || item.categoryName || item.category}</span>
                      </div>

                      <p className={styles.meaningSnippet}>"{item.meaning}"</p>

                      <div className={styles.footerRow}>
                        <div className={styles.dateMeta}>
                          <Calendar size={13} />
                          <span>{formatDate(item.timestamp)}</span>
                        </div>

                        <button
                          className={styles.deleteBtn}
                          onClick={() => onDeleteReading(item.id)}
                          aria-label={`Hapus pembacaan ${item.cardName}`}
                          title="Hapus pembacaan ini"
                        >
                          <Trash2 size={15} />
                        </button>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          ) : (
            <div className={styles.emptyState}>
              <History size={48} className={styles.emptyIcon} />
              <h4>Belum Ada Riwayat Pembacaan</h4>
              <p>
                Lakukan pengocokan kartu tarot pertama Anda dan simpan hasil pembacaannya untuk
                dilihat kembali di sini.
              </p>
            </div>
          )}
        </div>
      </Modal>

      {/* Card Detail Modal when clicked from history */}
      <CardDetailModal
        card={selectedCardForDetail}
        isOpen={!!selectedCardForDetail}
        onClose={() => setSelectedCardForDetail(null)}
      />
    </>
  );
};
