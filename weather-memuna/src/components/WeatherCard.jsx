import React, { useState, useRef, useEffect } from 'react';
import back from '../assets/images/bg-today-large.svg';
import dropdown from '../assets/images/icon-dropdown.svg';

// ─── Helpers ────────────────────────────────────────────────────────────────

function fixIcon(url) {
  if (!url) return '';
  return url.startsWith('//') ? `https:${url}` : url;
}

function fmtDate(str) {
  if (!str) return '';
  return new Date(str).toLocaleDateString('en-US', {
    weekday: 'long', month: 'long', day: 'numeric', timeZone: 'UTC',
  });
}

function fmtHour(timeStr) {
  if (!timeStr) return '';
  const t = timeStr.split(' ')[1];
  if (!t) return '';
  const h = parseInt(t.split(':')[0], 10);
  return `${h % 12 === 0 ? 12 : h % 12}:00 ${h >= 12 ? 'PM' : 'AM'}`;
}

function dayLabel(dateStr, i) {
  if (i === 0) return 'Today';
  if (i === 1) return 'Tomorrow';
  return new Date(dateStr).toLocaleDateString('en-US', { weekday: 'short', timeZone: 'UTC' });
}

// ─── Stat Row ───────────────────────────────────────────────────────────────

function StatItem({ label, value }) {
  return (
    <div className="flex flex-col gap-1 py-4 flex-1 min-w-0">
      <span className="text-[11px] font-semibold uppercase tracking-widest"
        style={{ color: 'var(--text-3)' }}>
        {label}
      </span>
      <span className="text-xl font-semibold tabular-nums"
        style={{ color: 'var(--text)' }}>
        {value}
      </span>
    </div>
  );
}

// ─── Day Pill ────────────────────────────────────────────────────────────────

function DayPill({ day, index, isActive, unit, onClick }) {
  const max = unit === 'metric' ? Math.round(day.day?.maxtemp_c) : Math.round(day.day?.maxtemp_f);
  const min = unit === 'metric' ? Math.round(day.day?.mintemp_c) : Math.round(day.day?.mintemp_f);

  return (
    <button
      onClick={onClick}
      className="flex flex-col items-center gap-2 py-3 px-2 rounded-md transition-all duration-150 text-center"
      style={{
        background: isActive ? 'var(--accent-dim)' : 'transparent',
        border: `1px solid ${isActive ? 'var(--accent)' : 'transparent'}`,
        color: isActive ? 'var(--accent)' : 'var(--text-2)',
      }}
    >
      <span className="text-[11px] font-semibold uppercase tracking-wider">
        {dayLabel(day.date, index)}
      </span>
      <img src={fixIcon(day.day?.condition?.icon)} alt="" className="w-9 h-9" />
      <div className="flex flex-col items-center">
        <span className="text-sm font-semibold" style={{ color: isActive ? 'var(--accent)' : 'var(--text)' }}>
          {max}°
        </span>
        <span className="text-xs" style={{ color: 'var(--text-3)' }}>{min}°</span>
      </div>
    </button>
  );
}

// ─── Hourly Row ──────────────────────────────────────────────────────────────

function HourRow({ item, unit }) {
  const temp = unit === 'metric' ? `${Math.round(item.temp_c)}°` : `${Math.round(item.temp_f)}°`;
  return (
    <div
      className="flex items-center justify-between px-3 py-2.5 rounded-md transition-colors"
      style={{ borderBottom: '1px solid var(--border)' }}
    >
      <div className="flex items-center gap-3 min-w-0">
        <span className="text-xs font-mono w-16 shrink-0" style={{ color: 'var(--text-2)' }}>
          {fmtHour(item.time)}
        </span>
        <img src={fixIcon(item.condition?.icon)} alt="" className="w-5 h-5 shrink-0" />
        <span className="text-xs truncate" style={{ color: 'var(--text-3)' }}>
          {item.condition?.text}
        </span>
      </div>
      <span className="text-sm font-semibold tabular-nums ml-3 shrink-0" style={{ color: 'var(--text)' }}>
        {temp}
      </span>
    </div>
  );
}

// ─── Main Component ──────────────────────────────────────────────────────────

export default function WeatherCard({ weather, unit, selectedDayIndex, setSelectedDayIndex }) {
  const [dayDropOpen, setDayDropOpen] = useState(false);
  const dayDropRef = useRef(null);

  useEffect(() => {
    const h = (e) => { if (dayDropRef.current && !dayDropRef.current.contains(e.target)) setDayDropOpen(false); };
    document.addEventListener('mousedown', h);
    return () => document.removeEventListener('mousedown', h);
  }, []);

  if (!weather) return null;

  const cur = weather.current;
  const loc = weather.location;
  const days = weather.forecast?.forecastday || [];
  const selDay = days[selectedDayIndex] || days[0];
  const hours = selDay?.hour || [];

  const temp      = unit === 'metric' ? `${Math.round(cur?.temp_c)}°C`      : `${Math.round(cur?.temp_f)}°F`;
  const feelsLike = unit === 'metric' ? `${Math.round(cur?.feelslike_c)}°C` : `${Math.round(cur?.feelslike_f)}°F`;
  const wind      = unit === 'metric' ? `${cur?.wind_kph} km/h`             : `${cur?.wind_mph} mph`;
  const precip    = unit === 'metric' ? `${cur?.precip_mm} mm`              : `${cur?.precip_in} in`;

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 pb-16">

      {/* ══════════════════ HERO SECTION ══════════════════ */}
      <div
        className="relative rounded-lg overflow-hidden mb-1"
        style={{
          background: 'var(--surface)',
          border: '1px solid var(--border)',
          backgroundImage: `url(${back})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
        }}
      >
        {/* Dark scrim */}
        <div
          className="absolute inset-0"
          style={{ background: 'linear-gradient(135deg, rgba(9,13,18,0.88) 0%, rgba(9,13,18,0.60) 100%)' }}
        />

        <div className="relative z-10 flex items-end justify-between p-8 sm:p-10 min-h-[220px]">
          {/* Left: Location + Meta */}
          <div>
            <p className="text-xs font-semibold uppercase tracking-widest mb-3" style={{ color: 'var(--accent)' }}>
              {cur?.condition?.text}
            </p>
            <h2 className="text-4xl sm:text-5xl font-bold tracking-tight mb-1" style={{ color: 'var(--text)' }}>
              {loc?.name}
            </h2>
            <p className="text-sm" style={{ color: 'var(--text-2)' }}>
              {loc?.country} — {fmtDate(loc?.localtime)}
            </p>
          </div>

          {/* Right: Temp + Icon */}
          <div className="flex flex-col items-end gap-2">
            <img src={fixIcon(cur?.condition?.icon)} alt={cur?.condition?.text} className="w-16 h-16" />
            <span className="text-6xl font-bold tabular-nums leading-none" style={{ color: 'var(--text)' }}>
              {temp}
            </span>
            <span className="text-xs font-mono" style={{ color: 'var(--text-3)' }}>
              updated {cur?.last_updated?.split(' ')[1]}
            </span>
          </div>
        </div>
      </div>

      {/* ══════════════════ STATS STRIP ══════════════════ */}
      <div
        className="flex divide-x mb-6 rounded-b-lg px-6"
        style={{
          background: 'var(--surface-2)',
          border: '1px solid var(--border)',
          borderTop: 'none',
          divideColor: 'var(--border)',
        }}
      >
        <StatItem label="Feels Like"   value={feelsLike} />
        <div style={{ width: '1px', background: 'var(--border)', margin: '0 1px' }} />
        <StatItem label="Humidity"     value={`${cur?.humidity}%`} />
        <div style={{ width: '1px', background: 'var(--border)', margin: '0 1px' }} />
        <StatItem label="Wind"         value={wind} />
        <div style={{ width: '1px', background: 'var(--border)', margin: '0 1px' }} />
        <StatItem label="Precip."      value={precip} />
        <div style={{ width: '1px', background: 'var(--border)', margin: '0 1px' }} />
        <StatItem label="UV Index"     value={cur?.uv ?? '—'} />
        <div style={{ width: '1px', background: 'var(--border)', margin: '0 1px' }} />
        <StatItem label="Visibility"   value={unit === 'metric' ? `${cur?.vis_km} km` : `${cur?.vis_miles} mi`} />
      </div>

      {/* ══════════════════ BODY: 2-col layout ══════════════════ */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">

        {/* ── LEFT: Daily Forecast ── */}
        <div className="lg:col-span-2 flex flex-col gap-4">

          {/* Section label */}
          <div className="flex items-center gap-3">
            <span className="text-xs font-semibold uppercase tracking-widest" style={{ color: 'var(--text-3)' }}>
              7-Day Forecast
            </span>
            <div className="flex-1 h-px" style={{ background: 'var(--border)' }} />
          </div>

          {/* Day grid */}
          <div
            className="rounded-lg p-4 grid grid-cols-7 gap-1"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            {days.map((day, i) => (
              <DayPill
                key={day.date}
                day={day}
                index={i}
                isActive={i === selectedDayIndex}
                unit={unit}
                onClick={() => setSelectedDayIndex(i)}
              />
            ))}
          </div>

          {/* Selected day detail strip */}
          <div
            className="rounded-lg px-5 py-4 flex items-center justify-between"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest mb-1" style={{ color: 'var(--text-3)' }}>
                Selected — {dayLabel(selDay?.date, selectedDayIndex)}
              </p>
              <p className="text-sm" style={{ color: 'var(--text-2)' }}>
                {selDay?.day?.condition?.text}
              </p>
            </div>
            <div className="flex items-center gap-6 text-right">
              <div>
                <p className="text-[10px] uppercase tracking-widest mb-0.5" style={{ color: 'var(--text-3)' }}>High</p>
                <p className="text-lg font-semibold tabular-nums" style={{ color: 'var(--accent)' }}>
                  {unit === 'metric' ? `${Math.round(selDay?.day?.maxtemp_c)}°C` : `${Math.round(selDay?.day?.maxtemp_f)}°F`}
                </p>
              </div>
              <div>
                <p className="text-[10px] uppercase tracking-widest mb-0.5" style={{ color: 'var(--text-3)' }}>Low</p>
                <p className="text-lg font-semibold tabular-nums" style={{ color: 'var(--text-2)' }}>
                  {unit === 'metric' ? `${Math.round(selDay?.day?.mintemp_c)}°C` : `${Math.round(selDay?.day?.mintemp_f)}°F`}
                </p>
              </div>
              <div>
                <p className="text-[10px] uppercase tracking-widest mb-0.5" style={{ color: 'var(--text-3)' }}>Rain %</p>
                <p className="text-lg font-semibold tabular-nums" style={{ color: 'var(--text-2)' }}>
                  {selDay?.day?.daily_chance_of_rain}%
                </p>
              </div>
            </div>
          </div>

        </div>

        {/* ── RIGHT: Hourly Panel ── */}
        <div className="flex flex-col gap-4">

          {/* Section label + day dropdown */}
          <div className="flex items-center justify-between gap-3">
            <div className="flex items-center gap-3">
              <span className="text-xs font-semibold uppercase tracking-widest" style={{ color: 'var(--text-3)' }}>
                Hourly
              </span>
              <div className="h-px w-8" style={{ background: 'var(--border)' }} />
            </div>

            {/* Day Dropdown */}
            <div className="relative" ref={dayDropRef}>
              <button
                onClick={() => setDayDropOpen(!dayDropOpen)}
                className="flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-medium transition-colors"
                style={{
                  background: 'var(--surface)',
                  border: '1px solid var(--border-2)',
                  color: 'var(--text-2)',
                }}
              >
                {dayLabel(selDay?.date, selectedDayIndex)}
                <img src={dropdown} alt="" className="w-2.5 opacity-40" style={{ transform: dayDropOpen ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }} />
              </button>
              {dayDropOpen && (
                <div
                  className="absolute right-0 mt-1 w-36 rounded-md shadow-xl z-50 overflow-hidden"
                  style={{ background: 'var(--surface)', border: '1px solid var(--border-2)' }}
                >
                  {days.map((day, idx) => (
                    <button
                      key={day.date}
                      onClick={() => { setSelectedDayIndex(idx); setDayDropOpen(false); }}
                      className="w-full text-left px-3 py-2 text-xs font-medium transition-colors"
                      style={{
                        color: idx === selectedDayIndex ? 'var(--accent)' : 'var(--text-2)',
                        background: idx === selectedDayIndex ? 'var(--accent-dim)' : 'transparent',
                      }}
                    >
                      {dayLabel(day.date, idx)}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Hourly list */}
          <div
            className="rounded-lg overflow-hidden flex flex-col"
            style={{ background: 'var(--surface)', border: '1px solid var(--border)' }}
          >
            <div className="overflow-y-auto" style={{ maxHeight: '420px' }}>
              {hours.map((hr) => (
                <HourRow key={hr.time} item={hr} unit={unit} />
              ))}
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}