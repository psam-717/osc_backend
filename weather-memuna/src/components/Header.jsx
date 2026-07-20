import React, { useState, useRef, useEffect } from 'react';
import logo from '../assets/images/logo.svg';

export default function Header({ unit, onUnitChange }) {
  const [isOpen, setIsOpen] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const handler = (e) => { if (ref.current && !ref.current.contains(e.target)) setIsOpen(false); };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  return (
    <header style={{ borderBottom: '1px solid var(--border)' }}>
      <div className="max-w-6xl mx-auto px-6 h-14 flex items-center justify-between">

        {/* Logo */}
        <img src={logo} alt="logo" className="h-6 opacity-90" />

        {/* Unit Toggle */}
        <div className="relative" ref={ref}>
          <button
            onClick={() => setIsOpen(!isOpen)}
            style={{
              background: 'var(--surface)',
              border: '1px solid var(--border-2)',
              color: 'var(--text-2)',
            }}
            className="flex items-center gap-2 px-3 py-1.5 rounded-md text-xs font-medium tracking-wide transition-colors hover:border-[var(--accent)] hover:text-[var(--text)]"
          >
            <span style={{ color: 'var(--accent)' }}>⊙</span>
            {unit === 'metric' ? '°C / km/h' : '°F / mph'}
            <span style={{ opacity: 0.4 }}>{isOpen ? '▲' : '▼'}</span>
          </button>

          {isOpen && (
            <div
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--border-2)',
              }}
              className="absolute right-0 mt-1 w-40 rounded-md shadow-2xl z-50 overflow-hidden"
            >
              {[
                { label: 'Metric  (°C, km/h)', value: 'metric' },
                { label: 'Imperial (°F, mph)', value: 'imperial' },
              ].map(({ label, value }) => (
                <button
                  key={value}
                  onClick={() => { onUnitChange(value); setIsOpen(false); }}
                  className="w-full text-left px-4 py-2.5 text-xs font-medium transition-colors"
                  style={{
                    background: unit === value ? 'var(--accent-dim)' : 'transparent',
                    color: unit === value ? 'var(--accent)' : 'var(--text-2)',
                    borderLeft: unit === value ? '2px solid var(--accent)' : '2px solid transparent',
                  }}
                >
                  {label}
                </button>
              ))}
            </div>
          )}
        </div>
      </div>
    </header>
  );
}
