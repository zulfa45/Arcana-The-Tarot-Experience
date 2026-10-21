import React, { useMemo } from 'react';
import { useReducedMotion } from '../../hooks/useReducedMotion';

interface Star {
  id: number;
  x: number;
  y: number;
  size: number;
  opacity: number;
  duration: number;
  delay: number;
}

export const StarField: React.FC = () => {
  const prefersReduced = useReducedMotion();

  // Generate 75 fixed stars based on random seeds
  const stars: Star[] = useMemo(() => {
    const list: Star[] = [];
    for (let i = 0; i < 75; i++) {
      list.push({
        id: i,
        x: Math.random() * 100,
        y: Math.random() * 100,
        size: Math.random() * 2 + 1,
        opacity: Math.random() * 0.7 + 0.2,
        duration: Math.random() * 4 + 3,
        delay: Math.random() * 5,
      });
    }
    return list;
  }, []);

  return (
    <div
      aria-hidden="true"
      style={{
        position: 'fixed',
        inset: 0,
        pointerEvents: 'none',
        overflow: 'hidden',
        zIndex: -1,
      }}
    >
      {/* Astrological Celestial Circles */}
      <div
        className={prefersReduced ? '' : 'anim-celestial-rotate'}
        style={{
          position: 'absolute',
          top: '20%',
          left: '50%',
          width: '750px',
          height: '750px',
          marginLeft: '-375px',
          marginTop: '-375px',
          borderRadius: '50%',
          border: '1px dashed rgba(217, 181, 109, 0.08)',
          boxShadow: '0 0 100px rgba(155, 123, 255, 0.04)',
          pointerEvents: 'none',
        }}
      >
        <div
          style={{
            position: 'absolute',
            inset: '50px',
            borderRadius: '50%',
            border: '1px solid rgba(155, 123, 255, 0.06)',
          }}
        />
        <div
          style={{
            position: 'absolute',
            inset: '120px',
            borderRadius: '50%',
            border: '1px dotted rgba(217, 181, 109, 0.06)',
          }}
        />
      </div>

      {/* Twinkling Stars */}
      {stars.map((s) => (
        <div
          key={s.id}
          style={{
            position: 'absolute',
            left: `${s.x}%`,
            top: `${s.y}%`,
            width: `${s.size}px`,
            height: `${s.size}px`,
            backgroundColor: s.id % 4 === 0 ? 'var(--color-gold-light)' : '#FFFFFF',
            borderRadius: '50%',
            opacity: s.opacity,
            boxShadow: `0 0 ${s.size * 2}px ${s.id % 4 === 0 ? 'rgba(217,181,109,0.8)' : 'rgba(255,255,255,0.6)'}`,
            animation: prefersReduced
              ? 'none'
              : `starTwinkle ${s.duration}s ease-in-out ${s.delay}s infinite alternate`,
          }}
        />
      ))}
    </div>
  );
};
