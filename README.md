# ✦ ARCANA — The Tarot Experience ✦

> *"Discover the story written in your cards."*

[![React](https://img.shields.io/badge/React-18.3.1-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.6.2-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-6.0.0-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![License](https://img.shields.io/badge/License-MIT-D9B56D?style=for-the-badge)](LICENSE)

**Arcana** adalah aplikasi web gacha kartu tarot interaktif premium dengan estetika *dark mystical celestial*. Dirancang dengan animasi 3D halus, Web Audio API sound synthesis lokal, serta sistem pembacaan tarot mendalam dalam Bahasa Indonesia yang mencakup 7 dimensi kehidupan.

---

## ✨ Fitur Unggulan

- 🃏 **Koleksi Lengkap 78 Kartu Tarot (Rider-Waite-Smith)**
  - 22 Major Arcana + 56 Minor Arcana (Wands, Cups, Swords, Pentacles).
  - Tampilan visual presisi dengan aspek rasio kartu tarot asli tanpa distorsi.
- 🔮 **Altar Gacha Interaktif & Animasi 3D Realistis**
  - **Fase Shuffling**: Tumpukan kartu bergeser dinamis dengan efek gemerisik kartu.
  - **Fase Flying**: Kartu terpilih melesat dalam lintasan parabola menuju tengah altar.
  - **Fase Flip 3D**: Membuka kartu melalui rotasi 180° CSS 3D (`preserve-3d`) disertai dentang lonceng spiritual dan pancaran starlight.
- 📜 **546 Interpretasi Tarot Mendalam (Bahasa Indonesia)**
  - 78 kartu × 7 dimensi kehidupan:
    1. **Percintaan (Love)**
    2. **Pekerjaan (Work)**
    3. **Karier (Career)**
    4. **Keuangan (Finance)**
    5. **Pengembangan Diri (Self-Growth)**
    6. **Keluarga & Pertemanan (Relationships)**
    7. **Spiritual (Spirituality)**
  - Mengganti kategori tidak akan mengocok ulang kartu atau mengulang animasi.
  - Setiap interpretasi dilengkapi makna arketipe, arahan tindakan, dan pertanyaan refleksi batin.
- 📚 **Card Library (Koleksi Kartu)**
  - Jelajahi seluruh 78 kartu tarot kapan saja.
  - Pencarian instan berdasarkan nama kartu dan kata kunci.
  - Filter cepat per kategori (*Major Arcana, Wands, Cups, Swords, Pentacles*).
- 📜 **Reading History (Riwayat Pembacaan)**
  - Simpan hasil pembacaan favorit ke `localStorage`.
  - Akses kembali detail kartu, makna, dan waktu pembacaan kapan pun.
  - Pengelolaan riwayat: hapus satu per satu atau bersihkan semua.
- 🎵 **Sintesis Audio Spiritual Lokal (Web Audio API)**
  - Bebas ketergantungan berkas eksternal dan hak cipta.
  - Meliputi ambient drone mistis (432Hz/528Hz harmonics), efek suara shuffle, whoosh fly, dan chime reveal.
  - Default dalam kondisi *muted* untuk kenyamanan pengguna.
- 🔄 **Pengaturan Posisi Terbalik (Reversed Cards)**
  - Opsi toggle di navbar untuk menyertakan atau menonaktifkan kartu dalam orientasi terbalik.
- ♿ **Aksesibilitas & Responsivitas**
  - Navigasi keyboard penuh (`Enter`, `Space`, `Escape`).
  - Dukungan preferensi sistem `prefers-reduced-motion`.
  - Tata letak responsif untuk Smartphone, Tablet, Laptop, dan Desktop.

---

## 🛠️ Tech Stack

- **Framework:** React 18
- **Bahasa:** TypeScript (Strict Mode)
- **Build Tool:** Vite
- **Animasi:** CSS 3D Transforms, Framer Motion, Keyframes, Canvas Confetti
- **Ikon:** Lucide React
- **Audio:** Web Audio API (Osilator & Filter Sintesis Murni)
- **Styling:** CSS Modules, CSS Custom Properties (Design Tokens)
- **Tipografi:** Google Fonts (`Cinzel` untuk heading, `Plus Jakarta Sans` untuk body)

---

## 🚀 Panduan Memulai

### Prasyarat
- Node.js (versi 18.0.0 atau lebih baru)
- npm / yarn / pnpm

### Instalasi & Menjalankan

1. **Clone repositori:**
   ```bash
   git clone https://github.com/zulfa45/Arcana-The-Tarot-Experience.git
   cd "Arcana-The-Tarot-Experience"
   ```

2. **Pasang dependensi:**
   ```bash
   npm install
   ```

3. **Jalankan development server:**
   ```bash
   npm run dev
   ```
   Buka peramban di `http://localhost:5173`.

4. **Build untuk produksi:**
   ```bash
   npm run build
   ```

5. **Pratinjau hasil build:**
   ```bash
   npm run preview
   ```

---

## 📁 Struktur Proyek

```
Arcana — The Tarot Experience/
├── card/                         # Berkas master kartu asli
├── public/
│   └── assets/
│       └── tarot/
│           ├── back-card.jpg     # Tekstur belakang kartu
│           ├── symbol.svg        # Segel mistis Arcana
│           └── cards/            # 78 gambar kartu tarot Rider-Waite-Smith
├── scripts/
│   └── audit-tarot-assets.ts     # Skrip verifikasi kelengkapan aset & dataset
├── src/
│   ├── components/
│   │   ├── hero/                 # HeroSection (pembuka & CTA)
│   │   ├── history/              # ReadingHistory Modal & Item
│   │   ├── layout/               # Navbar & Footer
│   │   ├── library/              # CardLibrary & CardDetailModal
│   │   ├── reading/              # ReadingCategorySelector & ReadingResult
│   │   ├── tarot/                # TarotCard (3D), TarotDeck, TarotGachaSection
│   │   └── ui/                   # Button, Modal, StarField
│   ├── data/
│   │   ├── readings/             # Dataset interpretasi modular (major, wands, cups, swords, pentacles)
│   │   ├── tarotCards.ts         # Metadata 78 kartu tarot
│   │   ├── tarotCategories.ts    # 7 Kategori kehidupan
│   │   └── tarotReadings.ts      # Master registry bacaan tarot
│   ├── hooks/
│   │   ├── useReadingHistory.ts  # State riwayat + sinkronisasi localStorage
│   │   ├── useReducedMotion.ts   # Deteksi aksesibilitas gerak
│   │   └── useTarotGacha.ts      # State machine siklus penarikan kartu
│   ├── styles/
│   │   ├── animations.css        # Keyframes celestial, denyut aura, rotasi
│   │   ├── globals.css           # Global resets & typography
│   │   └── variables.css         # Token warna, spacing, radius, shadows
│   ├── types/
│   │   └── tarot.ts              # Definisi interface TypeScript
│   ├── utils/
│   │   ├── randomCard.ts         # Generator acak seragam & anti-duplikasi
│   │   ├── sound.ts              # Synthesizer audio Web Audio API
│   │   └── storage.ts            # LocalStorage helper
│   ├── App.tsx                   # Main container
│   └── main.tsx                  # Vite entrypoint
├── DESAIN.md                     # Dokumentasi arsitektur sistem komprehensif
├── index.html                    # Single Page App shell
└── package.json
```

---

## 🎨 Palet Warna Desain

| Token CSS | Kode Warna | Deskripsi |
| :--- | :--- | :--- |
| `--color-background` | `#080711` | Ruang celestial gelap tanpa batas |
| `--color-background-secondary` | `#100D1D` | Lapisan kontras sekunder |
| `--color-surface` | `#171327` | Permukaan kartu dan glassmorphic modal |
| `--color-gold` | `#D9B56D` | Aksen emas astrologi klasik |
| `--color-gold-light` | `#F0D9A0` | Kilau bintang dan teks judul |
| `--color-primary` | `#9B7BFF` | Ungu mistis untuk aura dan seleksi |
| `--color-text` | `#F5F0FF` | Teks utama putih mutiara |
| `--color-border` | `rgba(217, 181, 109, 0.25)` | Garis batas bertatahkan emas |

---

## 🔮 Cara Menambah / Mengubah Kartu

Untuk menambahkan kartu kustom atau mengganti aset:
1. Tempatkan gambar kartu baru di `public/assets/tarot/cards/<Nama Kartu>.jpg`.
2. Daftarkan metadata kartu di [`src/data/tarotCards.ts`](src/data/tarotCards.ts).
3. Tambahkan 7 interpretasi kategorinya di [`src/data/readings/`](src/data/readings/).
4. Jalankan audit otomatis:
   ```bash
   npx tsx scripts/audit-tarot-assets.ts
   ```

Dokumentasi rancangan dan arsitektur lebih lengkap dapat dibaca di **[`DESAIN.md`](DESAIN.md)**.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

*Dibuat dengan dedikasi untuk menyajikan pengalaman pembacaan tarot digital yang elegan, tenang, dan bermakna.*
