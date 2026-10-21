import { SavedReading } from '../types/tarot';

const HISTORY_KEY = 'arcana_tarot_reading_history';
const AUDIO_KEY = 'arcana_audio_muted';
const REVERSED_KEY = 'arcana_allow_reversed';

export function getSavedReadings(): SavedReading[] {
  try {
    const raw = localStorage.getItem(HISTORY_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    if (Array.isArray(parsed)) {
      return parsed;
    }
    return [];
  } catch (err) {
    console.warn('[Arcana Storage] Could not read reading history from localStorage:', err);
    return [];
  }
}

export function saveReading(reading: SavedReading): boolean {
  try {
    const current = getSavedReadings();
    // Prepend new reading to front of list
    const updated = [reading, ...current];
    // Keep max 50 items to avoid localStorage overflow
    const trimmed = updated.slice(0, 50);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(trimmed));
    return true;
  } catch (err) {
    console.warn('[Arcana Storage] Could not save reading to localStorage:', err);
    return false;
  }
}

export function deleteSavedReading(id: string): SavedReading[] {
  try {
    const current = getSavedReadings();
    const updated = current.filter((item) => item.id !== id);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(updated));
    return updated;
  } catch (err) {
    console.warn('[Arcana Storage] Could not delete reading from localStorage:', err);
    return getSavedReadings();
  }
}

export function clearAllSavedReadings(): boolean {
  try {
    localStorage.removeItem(HISTORY_KEY);
    return true;
  } catch (err) {
    console.warn('[Arcana Storage] Could not clear readings from localStorage:', err);
    return false;
  }
}

export function getStoredAudioMuted(): boolean {
  try {
    const raw = localStorage.getItem(AUDIO_KEY);
    if (raw === null) return true; // Default muted
    return raw === 'true';
  } catch {
    return true;
  }
}

export function setStoredAudioMuted(muted: boolean): void {
  try {
    localStorage.setItem(AUDIO_KEY, String(muted));
  } catch {
    // Ignore
  }
}

export function getStoredAllowReversed(): boolean {
  try {
    const raw = localStorage.getItem(REVERSED_KEY);
    if (raw === null) return false; // Default upright only for clean initial experience
    return raw === 'true';
  } catch {
    return false;
  }
}

export function setStoredAllowReversed(allow: boolean): void {
  try {
    localStorage.setItem(REVERSED_KEY, String(allow));
  } catch {
    // Ignore
  }
}

export const getStoredMutePreference = getStoredAudioMuted;
export const setStoredMutePreference = setStoredAudioMuted;
export const getStoredReversedPreference = getStoredAllowReversed;
export const setStoredReversedPreference = setStoredAllowReversed;
