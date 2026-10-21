/**
 * Web Audio API Synthesized Sound System for Arcana
 * 100% local, zero copyrighted audio files, lightweight and reliable.
 * Starts strictly muted by default.
 */

class SoundManager {
  private ctx: AudioContext | null = null;
  private ambientGain: GainNode | null = null;
  private ambientOscs: OscillatorNode[] = [];
  private isMuted: boolean = true;
  private isInitialized: boolean = false;

  public getInitialized(): boolean {
    return this.isInitialized;
  }

  private initContext() {
    if (this.ctx) return;
    try {
      const AudioCtx = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
        this.isInitialized = true;
      }
    } catch {
      // Audio not supported or blocked
    }
  }

  public getMuted(): boolean {
    return this.isMuted;
  }

  public setMuted(muted: boolean) {
    this.isMuted = muted;
    if (!muted) {
      this.initContext();
      if (this.ctx && this.ctx.state === 'suspended') {
        this.ctx.resume();
      }
      this.startAmbient();
    } else {
      this.stopAmbient();
    }
  }

  public toggleMute(): boolean {
    this.setMuted(!this.isMuted);
    return this.isMuted;
  }

  private startAmbient() {
    if (this.isMuted || !this.ctx || this.ambientGain) return;

    try {
      const now = this.ctx.currentTime;
      this.ambientGain = this.ctx.createGain();
      this.ambientGain.gain.setValueAtTime(0.001, now);
      // Gentle fade in
      this.ambientGain.gain.exponentialRampToValueAtTime(0.04, now + 3);
      this.ambientGain.connect(this.ctx.destination);

      // Mystical chord: D2 (73.4Hz), A2 (110Hz), D3 (146.8Hz), F#3 (185Hz)
      const freqs = [73.4, 110.0, 146.8, 185.0];
      this.ambientOscs = freqs.map((f, i) => {
        const osc = this.ctx!.createOscillator();
        osc.type = i % 2 === 0 ? 'sine' : 'triangle';
        osc.frequency.setValueAtTime(f, now);

        // Gentle tremolo
        const lfo = this.ctx!.createOscillator();
        const lfoGain = this.ctx!.createGain();
        lfo.frequency.setValueAtTime(0.2 + i * 0.05, now);
        lfoGain.gain.setValueAtTime(1.5, now);
        lfo.connect(osc.frequency);
        lfo.start();

        osc.connect(this.ambientGain!);
        osc.start();
        return osc;
      });
    } catch {
      // Silently fall back
    }
  }

  private stopAmbient() {
    if (!this.ctx || !this.ambientGain) return;
    try {
      const now = this.ctx.currentTime;
      this.ambientGain.gain.setValueAtTime(this.ambientGain.gain.value, now);
      this.ambientGain.gain.exponentialRampToValueAtTime(0.0001, now + 1);
      setTimeout(() => {
        this.ambientOscs.forEach((osc) => {
          try {
            osc.stop();
            osc.disconnect();
          } catch {
            // Ignore
          }
        });
        this.ambientOscs = [];
        this.ambientGain?.disconnect();
        this.ambientGain = null;
      }, 1000);
    } catch {
      this.ambientGain = null;
      this.ambientOscs = [];
    }
  }

  /**
   * Sound effect: Card Shuffle (Riffling rustle)
   */
  public playShuffle() {
    if (this.isMuted || !this.ctx) return;
    try {
      const now = this.ctx.currentTime;
      // Synthesize noise burst sequence
      const bufferSize = this.ctx.sampleRate * 0.12;
      const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.4));
      }

      // Play 5 quick overlapping card clicks
      for (let j = 0; j < 6; j++) {
        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;

        const filter = this.ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1200 + Math.random() * 800, now + j * 0.12);
        filter.Q.setValueAtTime(3, now + j * 0.12);

        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.08, now + j * 0.12);
        gain.gain.exponentialRampToValueAtTime(0.001, now + j * 0.12 + 0.1);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);

        noise.start(now + j * 0.12);
      }
    } catch {
      // Ignore
    }
  }

  /**
   * Sound effect: Flying Card (Soft airy whoosh)
   */
  public playFly() {
    if (this.isMuted || !this.ctx) return;
    try {
      const now = this.ctx.currentTime;
      const bufferSize = this.ctx.sampleRate * 0.6;
      const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
      }

      const noise = this.ctx.createBufferSource();
      noise.buffer = buffer;

      const filter = this.ctx.createBiquadFilter();
      filter.type = 'bandpass';
      filter.frequency.setValueAtTime(300, now);
      filter.frequency.exponentialRampToValueAtTime(1500, now + 0.3);
      filter.frequency.exponentialRampToValueAtTime(400, now + 0.6);
      filter.Q.setValueAtTime(2.5, now);

      const gain = this.ctx.createGain();
      gain.gain.setValueAtTime(0.001, now);
      gain.gain.linearRampToValueAtTime(0.06, now + 0.25);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.6);

      noise.connect(filter);
      filter.connect(gain);
      gain.connect(this.ctx.destination);

      noise.start(now);
    } catch {
      // Ignore
    }
  }

  /**
   * Sound effect: Card Flip / Reveal (Celestial chime & shimmer)
   */
  public playReveal() {
    if (this.isMuted || !this.ctx) return;
    try {
      const now = this.ctx.currentTime;
      // Celestial bell chord: A4 (440), C#5 (554), E5 (659), G#5 (830)
      const notes = [440, 554.37, 659.25, 830.61];
      notes.forEach((freq, idx) => {
        const osc = this.ctx!.createOscillator();
        const gain = this.ctx!.createGain();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + idx * 0.06);

        gain.gain.setValueAtTime(0.05, now + idx * 0.06);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.06 + 1.8);

        osc.connect(gain);
        gain.connect(this.ctx!.destination);

        osc.start(now + idx * 0.06);
        osc.stop(now + idx * 0.06 + 2);
      });
    } catch {
      // Ignore
    }
  }
}

export const soundManager = new SoundManager();
export const soundSystem = soundManager;
