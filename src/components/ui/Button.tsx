import React from 'react';

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  icon?: React.ReactNode;
  iconPosition?: 'left' | 'right';
  isLoading?: boolean;
  glowEffect?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  icon,
  iconPosition = 'left',
  isLoading = false,
  glowEffect = false,
  className = '',
  disabled,
  ...props
}) => {
  const getVariantStyles = () => {
    switch (variant) {
      case 'primary':
        return `
          background: linear-gradient(135deg, #D9B56D 0%, #A57D32 100%);
          color: #080711;
          font-weight: 600;
          box-shadow: 0 4px 20px rgba(217, 181, 109, 0.35);
          border: 1px solid rgba(240, 217, 160, 0.6);
        `;
      case 'secondary':
        return `
          background: linear-gradient(135deg, #2A2147 0%, #171327 100%);
          color: var(--color-primary-soft);
          border: 1px solid rgba(155, 123, 255, 0.3);
          box-shadow: 0 4px 16px rgba(155, 123, 255, 0.15);
        `;
      case 'outline':
        return `
          background: transparent;
          color: var(--color-gold);
          border: 1px solid rgba(217, 181, 109, 0.4);
        `;
      case 'ghost':
        return `
          background: transparent;
          color: var(--color-text-secondary);
          border: 1px solid transparent;
        `;
    }
  };

  const getSizeStyles = () => {
    switch (size) {
      case 'sm':
        return 'padding: 0.45rem 0.9rem; font-size: 0.85rem; border-radius: var(--radius-sm);';
      case 'md':
        return 'padding: 0.65rem 1.4rem; font-size: 0.95rem; border-radius: var(--radius-md);';
      case 'lg':
        return 'padding: 0.85rem 2rem; font-size: 1.05rem; border-radius: var(--radius-md);';
    }
  };

  return (
    <button
      disabled={disabled || isLoading}
      className={`arcana-btn ${className} ${glowEffect ? 'btn-glow' : ''}`}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '0.5rem',
        cursor: disabled || isLoading ? 'not-allowed' : 'pointer',
        opacity: disabled || isLoading ? 0.6 : 1,
        transition: 'all 200ms cubic-bezier(0.16, 1, 0.3, 1)',
        fontFamily: 'var(--font-sans)',
        textDecoration: 'none',
        lineHeight: 1,
        position: 'relative',
        userSelect: 'none',
      }}
      {...props}
    >
      <style>{`
        .arcana-btn {
          ${getVariantStyles()}
          ${getSizeStyles()}
        }
        .btn-glow {
          animation: celestialPulse 2.5s infinite ease-in-out;
        }
        }
        .arcana-btn:not(:disabled):hover {
          transform: translateY(-2px);
          filter: brightness(1.1);
        }
        .arcana-btn:not(:disabled):active {
          transform: translateY(0px);
          filter: brightness(0.95);
        }
      `}</style>

      {isLoading ? (
        <span
          style={{
            width: '1em',
            height: '1em',
            border: '2px solid currentColor',
            borderRightColor: 'transparent',
            borderRadius: '50%',
            display: 'inline-block',
            animation: 'spin 0.75s linear infinite',
          }}
        />
      ) : (
        <>
          {icon && iconPosition === 'left' && <span style={{ display: 'inline-flex' }}>{icon}</span>}
          <span>{children}</span>
          {icon && iconPosition === 'right' && <span style={{ display: 'inline-flex' }}>{icon}</span>}
        </>
      )}
    </button>
  );
};
