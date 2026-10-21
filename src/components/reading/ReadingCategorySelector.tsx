import React from 'react';
import { ReadingCategory } from '../../types/tarot';
import { TAROT_CATEGORIES } from '../../data/tarotCategories';
import { Heart, Briefcase, Compass, Coins, Sparkles, Users, Moon } from 'lucide-react';
import styles from './ReadingCategorySelector.module.css';

interface ReadingCategorySelectorProps {
  selectedCategory: ReadingCategory;
  onSelectCategory: (category: ReadingCategory) => void;
}

const iconMap = {
  Heart,
  Briefcase,
  Compass,
  Coins,
  Sparkles,
  Users,
  Moon,
};

export const ReadingCategorySelector: React.FC<ReadingCategorySelectorProps> = ({
  selectedCategory,
  onSelectCategory,
}) => {
  return (
    <div className={styles.selectorContainer}>
      <div className={styles.header}>
        <span className={styles.eyebrow}>PILIH FOKUS PEMBACAAN</span>
        <h3 className={styles.title}>Kategori Kehidupan</h3>
        <p className={styles.description}>
          Pilih salah satu dimensi untuk membaca panduan spiritual yang spesifik dari kartu ini.
        </p>
      </div>

      <div className={styles.categoriesGrid} role="tablist" aria-label="Kategori Pembacaan Tarot">
        {TAROT_CATEGORIES.map((cat) => {
          const isSelected = selectedCategory === cat.id;
          const IconComponent = iconMap[cat.iconName] || Sparkles;

          return (
            <button
              key={cat.id}
              role="tab"
              aria-selected={isSelected}
              onClick={() => onSelectCategory(cat.id)}
              className={`${styles.categoryCard} ${isSelected ? styles.isActive : ''}`}
            >
              <div className={styles.iconCircle}>
                <IconComponent size={20} className={styles.icon} />
              </div>
              <div className={styles.textGroup}>
                <span className={styles.categoryLabel}>{cat.name}</span>
                <span className={styles.categoryDesc}>{cat.description}</span>
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
};
