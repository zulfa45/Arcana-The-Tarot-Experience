import React from 'react';
import styles from './Footer.module.css';

export const Footer: React.FC = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.divider} />

        <div className={styles.content}>
          <div className={styles.brandGroup}>
            <div className={styles.brandRow}>
              <img src="/assets/tarot/symbol.svg" alt="Arcana" className={styles.footerLogo} />
              <span className={styles.brandTitle}>ARCANA</span>
            </div>
            <p className={styles.tagline}>"Discover the story written in your cards."</p>
          </div>

          <div className={styles.infoGroup}>
            <p className={styles.disclaimer}>
              Kartu tarot menyajikan simbol arketipe untuk refleksi diri, kesadaran intuitif, dan
              perspektif hidup baru. Keputusan hidup Anda selalu berada di tangan Anda sepenuhnya.
            </p>
            <p className={styles.copyright}>
              © {new Date().getFullYear()} Arcana — The Tarot Experience. Crafted with precision &
              spiritual reverence.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};
