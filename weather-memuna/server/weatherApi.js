/**
 * Server-only WeatherAPI helpers. Never import this from client/React code.
 */

const UPSTREAM = 'https://api.weatherapi.com/v1/forecast.json';
const MAX_Q_LENGTH = 100;

/**
 * @param {string | null | undefined} rawQ
 * @returns {{ ok: true, q: string } | { ok: false, status: number, error: string }}
 */
export function validateLocationQuery(rawQ) {
  if (rawQ == null || String(rawQ).trim() === '') {
    return { ok: false, status: 400, error: 'Missing required query parameter: q' };
  }
  const q = String(rawQ).trim();
  if (q.length > MAX_Q_LENGTH) {
    return { ok: false, status: 400, error: `Location query must be at most ${MAX_Q_LENGTH} characters` };
  }
  return { ok: true, q };
}

/**
 * Fetch forecast from WeatherAPI using a server-side key (never exposed to the browser).
 * @param {string} q
 * @param {string} apiKey
 */
export async function fetchWeatherForecast(q, apiKey) {
  if (!apiKey) {
    return {
      ok: false,
      status: 500,
      body: { error: 'Server is missing WEATHER_API_KEY configuration' },
    };
  }

  const url = new URL(UPSTREAM);
  url.searchParams.set('key', apiKey);
  url.searchParams.set('q', q);
  url.searchParams.set('days', '7');
  url.searchParams.set('aqi', 'no');

  let upstream;
  try {
    upstream = await fetch(url);
  } catch {
    return {
      ok: false,
      status: 502,
      body: { error: 'Unable to reach weather service' },
    };
  }

  const text = await upstream.text();
  let data;
  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    return {
      ok: false,
      status: 502,
      body: { error: 'Invalid response from weather service' },
    };
  }

  if (!upstream.ok) {
    const message =
      data?.error?.message ||
      (upstream.status === 400 ? 'City not found' : 'Weather service error');
    return {
      ok: false,
      status: upstream.status === 401 || upstream.status === 403 ? 502 : upstream.status,
      body: { error: message },
    };
  }

  return { ok: true, status: 200, body: data };
}

/**
 * Connect-style middleware: GET /api/weather?q=...
 * Compatible with Vite configureServer / configurePreview and Node http.
 */
export function createWeatherApiMiddleware(getApiKey) {
  return async function weatherApiMiddleware(req, res, next) {
    const method = req.method || 'GET';
    const url = new URL(req.url || '/', 'http://localhost');

    if (!url.pathname.startsWith('/api/weather')) {
      if (typeof next === 'function') return next();
      res.statusCode = 404;
      res.end('Not found');
      return;
    }

    if (method !== 'GET' && method !== 'HEAD') {
      res.statusCode = 405;
      res.setHeader('Allow', 'GET, HEAD');
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({ error: 'Method not allowed' }));
      return;
    }

    const validated = validateLocationQuery(url.searchParams.get('q'));
    if (!validated.ok) {
      res.statusCode = validated.status;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({ error: validated.error }));
      return;
    }

    const result = await fetchWeatherForecast(validated.q, getApiKey());
    res.statusCode = result.status;
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Cache-Control', 'no-store');
    if (method === 'HEAD') {
      res.end();
      return;
    }
    res.end(JSON.stringify(result.body));
  };
}
