import React from 'react';

function Skel({ className = '' }) {
  return (
    <div
      className={`rounded animate-pulse ${className}`}
      style={{ background: 'var(--surface-2)' }}
    />
  );
}

export default function WeatherCardSkeleton() {
  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 pb-16">

      {/* Hero */}
      <div
        className="rounded-t-lg p-8 sm:p-10 min-h-[220px] flex items-end justify-between mb-1"
        style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
      >
        <div className="flex flex-col gap-3">
          <Skel className="h-3 w-20" />
          <Skel className="h-10 w-56" />
          <Skel className="h-3 w-40" />
        </div>
        <div className="flex flex-col items-end gap-3">
          <Skel className="w-14 h-14 rounded-full" />
          <Skel className="h-14 w-28" />
        </div>
      </div>

      {/* Stats strip */}
      <div
        className="flex divide-x mb-6 rounded-b-lg px-6"
        style={{ background: 'var(--surface-2)', border: '1px solid var(--border)', borderTop: 'none' }}
      >
        {[...Array(6)].map((_, i) => (
          <div key={i} className="flex flex-col gap-2 py-4 flex-1">
            <Skel className="h-2.5 w-12" />
            <Skel className="h-5 w-16" />
          </div>
        ))}
      </div>

      {/* Body */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <div className="lg:col-span-2 flex flex-col gap-4">
          <Skel className="h-3 w-28" />
          <div
            className="rounded-lg p-4 grid grid-cols-7 gap-1"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            {[...Array(7)].map((_, i) => (
              <div key={i} className="flex flex-col items-center gap-2 py-3">
                <Skel className="h-2.5 w-10" />
                <Skel className="w-9 h-9 rounded-full" />
                <Skel className="h-3 w-6" />
              </div>
            ))}
          </div>
          <div
            className="rounded-lg px-5 py-4 flex items-center justify-between"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            <div className="flex flex-col gap-2">
              <Skel className="h-2.5 w-24" />
              <Skel className="h-3 w-36" />
            </div>
            <div className="flex items-center gap-6">
              {[...Array(3)].map((_, i) => (
                <div key={i} className="flex flex-col items-end gap-2">
                  <Skel className="h-2 w-8" />
                  <Skel className="h-6 w-12" />
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="flex flex-col gap-4">
          <Skel className="h-3 w-16" />
          <div
            className="rounded-lg overflow-hidden"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            {[...Array(8)].map((_, i) => (
              <div
                key={i}
                className="flex items-center justify-between px-3 py-2.5"
                style={{ borderBottom: '1px solid var(--border)' }}
              >
                <div className="flex items-center gap-3">
                  <Skel className="h-3 w-14" />
                  <Skel className="w-5 h-5 rounded-full" />
                  <Skel className="h-3 w-20" />
                </div>
                <Skel className="h-4 w-8" />
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
