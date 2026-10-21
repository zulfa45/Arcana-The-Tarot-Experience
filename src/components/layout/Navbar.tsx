import React, { useState, useEffect } from 'react';
import { Volume2, VolumeX, Sparkles, BookOpen, History, RotateCcw, Menu, X } from 'lucide-react';
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
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Prevent background scroll when mobile menu is open
  useEffect(() => {
    if (mobileMenuOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [mobileMenuOpen]);

  const scrollToSection = (id: string) => {
    setMobileMenuOpen(false);
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleOpenLibrary = () => {
    setMobileMenuOpen(false);
    onOpenLibrary();
  };

  const handleOpenHistory = () => {
    setMobileMenuOpen(false);
    onOpenHistory();
  };

  return (
    <header className={`${styles.navbar} ${scrolled ? styles.isScrolled : ''}`}>
      <div className={styles.navContainer}>
        {/* Brand Logo & Title */}
        <div
          className={styles.brand}
          onClick={() => {
            setMobileMenuOpen(false);
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }}
        >
          <img src="/assets/tarot/symbol.svg" alt="Arcana Mystical Seal" className={styles.brandLogo} />
          <div className={styles.brandText}>
            <span className={styles.brandName}>ARCANA</span>
            <span className={styles.brandTagline}>TAROT EXPERIENCE</span>
          </div>
        </div>

        {/* Desktop Navigation Menus */}
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

        {/* Action Controls: Audio & Reversed Card Toggle & History Quick-Button on Mobile */}
        <div className={styles.navActions}>
          {/* Mobile Quick History Button so user can directly tap history in mobile header */}
          <button
            className={`${styles.iconButton} ${styles.mobileHistoryBtn}`}
            onClick={onOpenHistory}
            title="Riwayat Pembacaan Tarot"
            aria-label="Buka Riwayat Pembacaan"
          >
            <History size={18} />
            {historyCount > 0 && <span className={styles.mobileBadge}>{historyCount}</span>}
          </button>

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

          {/* Mobile Hamburger Menu Toggle */}
          <button
            className={`${styles.iconButton} ${styles.mobileMenuToggle}`}
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label={mobileMenuOpen ? 'Tutup Menu' : 'Buka Menu'}
            aria-expanded={mobileMenuOpen}
          >
            {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer Overlay */}
      {mobileMenuOpen && (
        <div className={styles.mobileDrawer} role="dialog" aria-modal="true">
          <div className={styles.drawerBackdrop} onClick={() => setMobileMenuOpen(false)} />
          <div className={styles.drawerContent}>
            <div className={styles.drawerHeader}>
              <div className={styles.drawerBrand}>
                <img src="/assets/tarot/symbol.svg" alt="Arcana" className={styles.drawerLogo} />
                <span className={styles.drawerBrandTitle}>ARCANA MENU</span>
              </div>
              <button
                className={styles.drawerCloseBtn}
                onClick={() => setMobileMenuOpen(false)}
                aria-label="Tutup Menu"
              >
                <X size={20} />
              </button>
            </div>

            <nav className={styles.drawerLinks}>
              <button
                className={styles.drawerItem}
                onClick={() => scrollToSection('gacha-section')}
              >
                <div className={styles.drawerIconBox}>
                  <Sparkles size={18} />
                </div>
                <div className={styles.drawerTextGroup}>
                  <span className={styles.drawerItemTitle}>Tarot Reading</span>
                  <span className={styles.drawerItemDesc}>Kocok dan ungkap kartu nasibmu</span>
                </div>
              </button>

              <button className={styles.drawerItem} onClick={handleOpenLibrary}>
                <div className={styles.drawerIconBox}>
                  <BookOpen size={18} />
                </div>
                <div className={styles.drawerTextGroup}>
                  <span className={styles.drawerItemTitle}>Card Library</span>
                  <span className={styles.drawerItemDesc}>Eksplorasi 78 kartu tarot & simbolisme</span>
                </div>
              </button>

              <button className={`${styles.drawerItem} ${styles.drawerHistoryHighlight}`} onClick={handleOpenHistory}>
                <div className={styles.drawerIconBox}>
                  <History size={18} />
                </div>
                <div className={styles.drawerTextGroup}>
                  <div className={styles.drawerTitleRow}>
                    <span className={styles.drawerItemTitle}>Reading History</span>
                    {historyCount > 0 && <span className={styles.badge}>{historyCount} tersimpan</span>}
                  </div>
                  <span className={styles.drawerItemDesc}>Baca kembali hasil pembacaan yang kamu simpan</span>
                </div>
              </button>
            </nav>

            <div className={styles.drawerFooter}>
              <div className={styles.drawerSettingRow}>
                <span>Kartu Terbalik (Reversed):</span>
                <button
                  className={`${styles.drawerPillBtn} ${allowReversed ? styles.drawerPillActive : ''}`}
                  onClick={onToggleReversed}
                >
                  {allowReversed ? 'Aktif' : 'Nonaktif'}
                </button>
              </div>
              <div className={styles.drawerSettingRow}>
                <span>Efek Suara:</span>
                <button
                  className={`${styles.drawerPillBtn} ${!isMuted ? styles.drawerPillActive : ''}`}
                  onClick={onToggleMute}
                >
                  {!isMuted ? 'Menyala' : 'Bisu'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </header>
  );
};
