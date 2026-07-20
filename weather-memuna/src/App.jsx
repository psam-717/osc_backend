import { useState } from 'react';
import useWeather from './hooks/useWeather';
import SearchBar from './components/SearchBar';
import WeatherCardSkeleton from './components/WeatherCardSkeleton';
import Header from './components/Header';
import WeatherCard from './components/WeatherCard';

function App() {
  const [city, setCity] = useState('Kumasi');
  const [unit, setUnit] = useState('metric');
  const [selectedDayIndex, setSelectedDayIndex] = useState(0);

  function targetLocation(newCity) {
    setCity(newCity);
    setSelectedDayIndex(0);
  }

  const { data: weather, loading, error } = useWeather({ location: city });

  return (
    <div className="min-h-screen" style={{ color: 'var(--text)' }}>

      {/* Header */}
      <Header unit={unit} onUnitChange={setUnit} />

      {/* Page title */}
      <div className="max-w-6xl mx-auto px-4 sm:px-6 pt-10 pb-2">
        <h1 className="text-2xl font-semibold tracking-tight" style={{ color: 'var(--text)' }}>
          Weather
        </h1>
        <p className="text-sm mt-1" style={{ color: 'var(--text-3)' }}>
          Real-time forecasts for anywhere on Earth.
        </p>
      </div>

      {/* Search */}
      <SearchBar onSearch={targetLocation} />

      {/* Loading */}
      {loading && <WeatherCardSkeleton />}

      {/* Error */}
      {error && !loading && (
        <div
          className="max-w-xl mx-auto mx-6 mt-2 px-5 py-3.5 rounded-md flex items-center gap-3 text-sm"
          style={{
            background: 'rgba(239,68,68,0.08)',
            border: '1px solid rgba(239,68,68,0.25)',
            color: '#fca5a5',
          }}
        >
          <span>⚠</span>
          <span>{error} — please check the spelling and try again.</span>
        </div>
      )}

      {/* Weather card */}
      {!loading && weather && !error && (
        <WeatherCard
          weather={weather}
          unit={unit}
          selectedDayIndex={selectedDayIndex}
          setSelectedDayIndex={setSelectedDayIndex}
        />
      )}
    </div>
  );
}

export default App;
