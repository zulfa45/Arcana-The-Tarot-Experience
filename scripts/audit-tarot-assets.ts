import fs from 'fs';
import path from 'path';
import { TAROT_CARDS } from '../src/data/tarotCards';
import { TAROT_READINGS } from '../src/data/tarotReadings';
import { TAROT_CATEGORIES } from '../src/data/tarotCategories';

interface AuditResult {
  totalImageFilesFound: number;
  totalCardsRegistered: number;
  totalInterpretationsAvailable: number;
  backCardFound: boolean;
  missingImages: string[];
  unregisteredImages: string[];
  incompleteInterpretations: string[];
  allValid: boolean;
}

export function runTarotAssetAudit(): AuditResult {
  console.log('\n========================================================');
  console.log('       ARCANA — TAROT ASSET & DATA AUDIT SUITE          ');
  console.log('========================================================\n');

  const cardsDir = path.resolve(process.cwd(), 'public/assets/tarot/cards');
  const backCardJpg = path.resolve(process.cwd(), 'public/assets/tarot/back-card.jpg');
  const backCardPng = path.resolve(process.cwd(), 'public/assets/tarot/back-card.png');

  if (!fs.existsSync(cardsDir)) {
    console.error(`[ERROR] Directory not found: ${cardsDir}`);
    return {
      totalImageFilesFound: 0,
      totalCardsRegistered: TAROT_CARDS.length,
      totalInterpretationsAvailable: 0,
      backCardFound: false,
      missingImages: TAROT_CARDS.map((c) => c.image),
      unregisteredImages: [],
      incompleteInterpretations: [],
      allValid: false,
    };
  }

  const diskFiles = fs.readdirSync(cardsDir).filter((f) => {
    const ext = path.extname(f).toLowerCase();
    return ['.jpg', '.jpeg', '.png', '.webp'].includes(ext);
  });

  const backCardFound = fs.existsSync(backCardJpg) || fs.existsSync(backCardPng);

  console.log(`[ASSET DISK SCAN]`);
  console.log(`- Folder: ${cardsDir}`);
  console.log(`- Total Card Image Files on Disk: ${diskFiles.length}`);
  console.log(`- Back Card Image Present: ${backCardFound ? 'YES' : 'NO'}`);

  const registeredImages = new Set(
    TAROT_CARDS.map((c) => path.basename(c.image).toLowerCase())
  );
  const diskFilesLower = new Set(diskFiles.map((f) => f.toLowerCase()));

  const missingImages: string[] = [];
  for (const card of TAROT_CARDS) {
    const filename = path.basename(card.image).toLowerCase();
    if (!diskFilesLower.has(filename)) {
      missingImages.push(card.name + ` (${card.image})`);
    }
  }

  const unregisteredImages: string[] = [];
  for (const file of diskFiles) {
    if (!registeredImages.has(file.toLowerCase())) {
      unregisteredImages.push(file);
    }
  }

  console.log(`\n[CODE DATASET CHECK]`);
  console.log(`- Total Cards in TAROT_CARDS: ${TAROT_CARDS.length}`);
  console.log(`- Total Cards in TAROT_READINGS: ${Object.keys(TAROT_READINGS).length}`);
  console.log(`- Required Categories per Card: ${TAROT_CATEGORIES.length}`);

  const requiredCategories = TAROT_CATEGORIES.map((c) => c.id);
  const incompleteInterpretations: string[] = [];

  for (const card of TAROT_CARDS) {
    const reading = TAROT_READINGS[card.id];
    if (!reading) {
      incompleteInterpretations.push(`${card.name} (${card.id}) [NO READING OBJECT]`);
      continue;
    }

    const missingCats: string[] = [];
    for (const cat of requiredCategories) {
      const interp = reading.interpretations[cat];
      if (
        !interp ||
        !interp.title ||
        !interp.summary ||
        !interp.meaning ||
        !interp.advice ||
        !interp.reflectionQuestion ||
        !interp.keywords ||
        interp.keywords.length === 0
      ) {
        missingCats.push(cat);
      }
    }

    if (missingCats.length > 0) {
      incompleteInterpretations.push(
        `${card.name} (${card.id}) [Missing/Incomplete: ${missingCats.join(', ')}]`
      );
    }
  }

  const allValid =
    backCardFound &&
    missingImages.length === 0 &&
    unregisteredImages.length === 0 &&
    incompleteInterpretations.length === 0 &&
    TAROT_CARDS.length === 78;

  console.log(`\n[AUDIT RESULTS SUMMARY]`);
  console.log(`✓ Back Card: ${backCardFound ? 'OK' : 'MISSING'}`);
  console.log(
    `✓ Missing Card Images: ${missingImages.length === 0 ? '0 (None)' : missingImages.join(', ')}`
  );
  console.log(
    `✓ Unregistered Images on Disk: ${unregisteredImages.length === 0 ? '0 (None)' : unregisteredImages.join(', ')}`
  );
  console.log(
    `✓ Incomplete 7-Category Interpretations: ${incompleteInterpretations.length === 0 ? '0 (All 78 cards fully populated)' : incompleteInterpretations.join(', ')}`
  );
  console.log(`\nOverall Status: ${allValid ? 'PASS (100% COMPLETE & VERIFIED)' : 'FAIL'}`);
  console.log('========================================================\n');

  return {
    totalImageFilesFound: diskFiles.length,
    totalCardsRegistered: TAROT_CARDS.length,
    totalInterpretationsAvailable: Object.keys(TAROT_READINGS).length,
    backCardFound,
    missingImages,
    unregisteredImages,
    incompleteInterpretations,
    allValid,
  };
}

// Run immediately if executed via CLI
runTarotAssetAudit();
