# Implementation Plan - weather-memuna

We will improve the weather app by implementing secure credential management, full functionality matching the Frontend Mentor challenge, and a premium, modern design system.

---

## 🛠️ Tasks

### 1. Environment Variable Setup (`.env`)
- **Action**: Create a `.env` file at the root of `weather-memuna` to securely store the WeatherAPI key.
- **Action**: Add `.env` to `.gitignore` to prevent it from being committed to GitHub.
- **Action**: Update `useWeather.js` hook to read the key dynamically using Vite's `import.meta.env.VITE_WEATHER_API_KEY`.

### 2. Unit Toggling (Metric vs. Imperial)
- **Action**: Create a state in `App.jsx` for tracking the user's unit system preference (`'metric'` or `'imperial'`).
- **Action**: Add unit options in the [Header.jsx](file:///D:/Projects/osc_backend/weather-memuna/src/components/Header.jsx) component to allow toggle switching.
- **Action**: Update [WeatherCard.jsx](file:///D:/Projects/osc_backend/weather-memuna/src/components/WeatherCard.jsx) to render metrics appropriately:
  - **Temperature**: Celsius (°C) vs. Fahrenheit (°F)
  - **Wind Speed**: km/h vs. mph
  - **Precipitation**: Millimeters (mm) vs. Inches (in)
  - **Feels Like**: `feelslike_c` vs. `feelslike_f`

### 3. Interactive Day & Hourly Selector
- **Action**: Create a `selectedDayIndex` state in `App.jsx` to track which day's hourly forecast to display.
- **Action**: Connect the day dropdown/selector in [WeatherCard.jsx](file:///D:/Projects/osc_backend/weather-memuna/src/components/WeatherCard.jsx) to list the available forecast days.
- **Action**: Update the hourly forecast rendering to map the hours of the selected day (`weather.forecast.forecastday[selectedDayIndex].hour`).

### 4. Premium UI Redesign
- **Aesthetic**: Deep futuristic dark mode utilizing vibrant blue, purple, and glassmorphic layers (`backdrop-blur`).
- **Typography**: Integrate premium sans-serif fonts (e.g., `Outfit` or `Plus Jakarta Sans` via Google Fonts) and clean weight hierarchy.
- **Metrics**: Update the Daily forecast cards to display both High (`maxtemp`) and Low (`mintemp`) temperatures.
- **Transitions**: Add subtle hover and click micro-animations for all buttons, inputs, and selectors.
