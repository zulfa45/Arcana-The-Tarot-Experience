import React, { useState, useEffect } from 'react';
import { Volume2, VolumeX, Sparkles, BookOpen, History, RotateCcw } from 'lucide-react';
import styles from './Navbar.module.css';

interface NavbarProps {
  isMuted: boolean;
  onToggleMute: () => void;
  onOpenLibrary: () => void;
  onOpenHistory: () => void;
  historyCount: number;
  allowReversed: boolean;
  onToggleReversed: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  isMuted,
  onToggleMute,
  onOpenLibrary,
  onOpenHistory,
  historyCount,
  allowReversed,
  onToggleReversed,
}) => {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className={`${styles.navbar} ${scrolled ? styles.isScrolled : ''}`}>
      <div className={styles.navContainer}>
        {/* Brand Logo & Title */}
        <div className={styles.brand} onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>
          <img src="/assets/tarot/symbol.svg" alt="Arcana Mystical Seal" className={styles.brandLogo} />
          <div className={styles.brandText}>
            <span className={styles.brandName}>ARCANA</span>
            <span className={styles.brandTagline}>TAROT EXPERIENCE</span>
          </div>
        </div>

        {/* Navigation Menus */}
        <nav className={styles.navLinks} aria-label="Main Navigation">
          <button
            className={styles.navItem}
            onClick={() => scrollToSection('gacha-section')}
          >
            <Sparkles size={16} />
            <span>Tarot Reading</span>
          </button>

          <button className={styles.navItem} onClick={onOpenLibrary}>
            <BookOpen size={16} />
            <span>Card Library</span>
          </button>

          <button className={styles.navItem} onClick={onOpenHistory}>
            <History size={16} />
            <span>History</span>
            {historyCount > 0 && <span className={styles.badge}>{historyCount}</span>}
          </button>
        </nav>

        {/* Action Controls: Audio & Reversed Card Toggle */}
        <div className={styles.navActions}>
          {/* Reversed Card Switch */}
          <button
            className={`${styles.iconButton} ${allowReversed ? styles.activeSetting : ''}`}
            onClick={onToggleReversed}
            title={allowReversed ? 'Posisi Terbalik Aktif' : 'Hanya Posisi Tegak'}
            aria-label="Toggle Reversed Cards"
          >
            <RotateCcw size={18} />
          </button>

          {/* Audio Mute/Unmute */}
          <button
            className={`${styles.iconButton} ${!isMuted ? styles.activeSetting : ''}`}
            onClick={onToggleMute}
            title={isMuted ? 'Nyalakan Suara Spiritual' : 'Matikan Suara'}
            aria-label={isMuted ? 'Nyalakan Suara' : 'Matikan Suara'}
          >
            {isMuted ? <VolumeX size={18} /> : <Volume2 size={18} />}
          </button>
        </div>
      </div>
    </header>
  );
};
