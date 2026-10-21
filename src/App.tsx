import React, { useState, useEffect } from 'react';
import { Navbar } from './components/layout/Navbar';
import { HeroSection } from './components/hero/HeroSection';
import { TarotGachaSection } from './components/tarot/TarotGachaSection';
import { ReadingResult } from './components/reading/ReadingResult';
import { CardLibrary } from './components/library/CardLibrary';
import { ReadingHistory } from './components/history/ReadingHistory';
import { Footer } from './components/layout/Footer';
import { StarField } from './components/ui/StarField';

import { useTarotGacha } from './hooks/useTarotGacha';
import { useReadingHistory } from './hooks/useReadingHistory';
import { useReducedMotion } from './hooks/useReducedMotion';
import { soundManager } from './utils/sound';
import {
  getStoredMutePreference,
  setStoredMutePreference,
  getStoredReversedPreference,
  setStoredReversedPreference,
} from './utils/storage';
import { ReadingCategory, SavedReading } from './types/tarot';
import { getCardInterpretation } from './data/tarotReadings';
import { TAROT_CATEGORIES } from './data/tarotCategories';

export const App: React.FC = () => {
  // Modal states
  const [isLibraryOpen, setIsLibraryOpen] = useState(false);
  const [isHistoryOpen, setIsHistoryOpen] = useState(false);

  // Settings
  const [isMuted, setIsMuted] = useState<boolean>(() => getStoredMutePreference());
  const [allowReversed, setAllowReversed] = useState<boolean>(() => getStoredReversedPreference());

  // Reading Category Focus
  const [selectedCategory, setSelectedCategory] = useState<ReadingCategory>('love');

  // Accessibility
  const reducedMotion = useReducedMotion();

  // Custom Hooks
  const { history, addReading, deleteReading, clearHistory } = useReadingHistory();
  const {
    phase,
    card: currentCard,
    fannedCards,
    orientation,
    startGacha,
    pickCardFromFan,
    revealCard,
    resetSession,
  } = useTarotGacha({ allowReversed });

  const isReversed = orientation === 'reversed';

  // Sync initial sound state
  useEffect(() => {
    soundManager.setMuted(isMuted);
  }, []);

  const handleToggleMute = () => {
    const nextState = !isMuted;
    setIsMuted(nextState);
    setStoredMutePreference(nextState);
    soundManager.setMuted(nextState);
  };

  const handleToggleReversed = () => {
    const nextState = !allowReversed;
    setAllowReversed(nextState);
    setStoredReversedPreference(nextState);
  };

  const handleStartReading = () => {
    const gachaEl = document.getElementById('gacha-section');
    if (gachaEl) {
      gachaEl.scrollIntoView({ behavior: 'smooth' });
    }
    if (phase === 'idle') {
      setTimeout(() => {
        startGacha();
      }, 400);
    }
  };

  const handleSaveCurrentReading = (category: ReadingCategory) => {
    if (!currentCard) return;
    const interp = getCardInterpretation(currentCard.id, category, orientation);
    const catInfo = TAROT_CATEGORIES.find((c) => c.id === category);

    const newSaved: SavedReading = {
      id: `${Date.now()}-${currentCard.id}-${category}`,
      timestamp: Date.now(),
      cardId: currentCard.id,
      cardName: currentCard.name,
      cardImage: currentCard.image,
      arcana: currentCard.arcana,
      orientation: orientation,
      category: category,
      categoryName: catInfo?.name || category,
      title: interp?.title || currentCard.name,
      summary: interp?.summary || currentCard.description,
      meaning: interp?.meaning || currentCard.description,
      advice: interp?.advice || 'Dengarkan intuisi terdalammu.',
      reflectionQuestion: interp?.reflectionQuestion || 'Apa yang dapat kupelajari dari situasi ini?',
      keywords: isReversed ? currentCard.reversedKeywords : currentCard.uprightKeywords,
    };

    addReading(newSaved);
  };

  const isCurrentCardSaved = currentCard
    ? history.some(
        (h) =>
          h.cardId === currentCard.id &&
          h.orientation === orientation &&
          h.category === selectedCategory
      )
    : false;

  return (
    <div className="arcana-app">
      {/* Background Starlight & Ambient Nebulas */}
      <StarField />

      {/* Top Fixed Header */}
      <Navbar
        isMuted={isMuted}
        onToggleMute={handleToggleMute}
        onOpenLibrary={() => setIsLibraryOpen(true)}
        onOpenHistory={() => setIsHistoryOpen(true)}
        historyCount={history.length}
        allowReversed={allowReversed}
        onToggleReversed={handleToggleReversed}
      />

      <main>
        {/* Hero Section */}
        <HeroSection
          onStartReading={handleStartReading}
          onExploreCards={() => setIsLibraryOpen(true)}
        />

        {/* Interactive Gacha Altar with Jembereng Kartu (Fan Spread) */}
        <TarotGachaSection
          phase={phase}
          currentCard={currentCard}
          fannedCards={fannedCards}
          isReversed={isReversed}
          onShuffle={startGacha}
          onPickCardFromFan={pickCardFromFan}
          onReveal={revealCard}
          onReset={resetSession}
          reducedMotion={reducedMotion}
        />

        {/* Revealed Card Interpretation Panel */}
        {phase === 'revealed' && currentCard && (
          <ReadingResult
            card={currentCard}
            isReversed={isReversed}
            selectedCategory={selectedCategory}
            onSelectCategory={setSelectedCategory}
            onSaveReading={handleSaveCurrentReading}
            isSaved={isCurrentCardSaved}
          />
        )}
      </main>

      {/* Modals */}
      <CardLibrary
        isOpen={isLibraryOpen}
        onClose={() => setIsLibraryOpen(false)}
      />

      <ReadingHistory
        isOpen={isHistoryOpen}
        onClose={() => setIsHistoryOpen(false)}
        history={history}
        onDeleteReading={deleteReading}
        onClearHistory={clearHistory}
      />

      {/* Global Footer */}
      <Footer />
    </div>
  );
};

export default App;
