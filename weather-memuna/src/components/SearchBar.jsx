import React, { useState } from 'react';
import search from '../assets/images/icon-search.svg';

export default function SearchBar({ onSearch }) {
  const [inputText, setInputText] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    if (!inputText.trim()) return;
    onSearch(inputText.trim());
    setInputText('');
  };

  return (
    <div className="w-full max-w-xl mx-auto px-6 mt-8 mb-10">
      <form onSubmit={handleSearch} className="flex items-center gap-2">
        <div className="relative flex-1">
          <img
            src={search}
            alt=""
            className="absolute left-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5"
            style={{ opacity: 0.3 }}
          />
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Search city…"
            style={{
              background: 'var(--surface)',
              border: '1px solid var(--border-2)',
              color: 'var(--text)',
            }}
            className="w-full pl-9 pr-4 py-2.5 rounded-md text-sm font-medium placeholder:text-[var(--text-3)] transition-colors focus:border-[var(--accent)] focus:outline-none"
          />
        </div>
        <button
          type="submit"
          style={{
            background: 'var(--accent)',
            color: '#000',
          }}
          className="shrink-0 px-4 py-2.5 rounded-md text-xs font-bold tracking-wide transition-opacity hover:opacity-85 active:opacity-70"
        >
          Search
        </button>
      </form>
    </div>
  );
}
