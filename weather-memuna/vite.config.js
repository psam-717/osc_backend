import { defineConfig, loadEnv } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import { createWeatherApiMiddleware } from './server/weatherApi.js'

function weatherApiPlugin(apiKey) {
  const middleware = createWeatherApiMiddleware(() => apiKey || process.env.WEATHER_API_KEY || '')
  return {
    name: 'weather-api-proxy',
    configureServer(server) {
      server.middlewares.use(middleware)
    },
    configurePreview(server) {
      server.middlewares.use(middleware)
    },
  }
}

export default defineConfig(({ mode }) => {
  // Load all env vars for the Node process (WEATHER_API_KEY is NOT VITE_-prefixed,
  // so it never appears in the client bundle).
  const env = loadEnv(mode, process.cwd(), '')
  if (env.WEATHER_API_KEY) {
    process.env.WEATHER_API_KEY = env.WEATHER_API_KEY
  }

  return {
    plugins: [
      tailwindcss(),
      weatherApiPlugin(env.WEATHER_API_KEY),
    ],
  }
})
