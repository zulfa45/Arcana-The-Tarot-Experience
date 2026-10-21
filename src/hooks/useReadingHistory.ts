import { useState, useCallback, useEffect } from 'react';
import { SavedReading } from '../types/tarot';
import {
  getSavedReadings,
  saveReading as persistSaveReading,
  deleteSavedReading as persistDeleteReading,
  clearAllSavedReadings as persistClearAll,
} from '../utils/storage';

export function useReadingHistory() {
  const [history, setHistory] = useState<SavedReading[]>([]);
  const [isLoaded, setIsLoaded] = useState<boolean>(false);

  useEffect(() => {
    setHistory(getSavedReadings());
    setIsLoaded(true);
  }, []);

  const addReading = useCallback((reading: SavedReading): boolean => {
    const success = persistSaveReading(reading);
    if (success) {
      setHistory(getSavedReadings());
    }
    return success;
  }, []);

  const deleteReading = useCallback((id: string) => {
    const updated = persistDeleteReading(id);
    setHistory(updated);
  }, []);

  const clearHistory = useCallback(() => {
    const success = persistClearAll();
    if (success) {
      setHistory([]);
    }
  }, []);

  return {
    history,
    isLoaded,
    addReading,
    deleteReading,
    clearHistory,
    totalCount: history.length,
  };
}
