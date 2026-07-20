/**
 * Production server: static `dist/` + /api/weather proxy (API key stays on server).
 * Dev: use `npm run dev` (Vite middleware). Prod: `npm run build && npm start`.
 */
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createWeatherApiMiddleware } from './server/weatherApi.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = __dirname;
const DIST = path.join(ROOT, 'dist');
const PORT = Number(process.env.PORT) || 3000;

function loadEnvFile() {
  const envPath = path.join(ROOT, '.env');
  if (!fs.existsSync(envPath)) return;
  for (const line of fs.readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const eq = trimmed.indexOf('=');
    if (eq === -1) continue;
    const key = trimmed.slice(0, eq).trim();
    let value = trimmed.slice(eq + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    if (key && process.env[key] === undefined) {
      process.env[key] = value;
    }
  }
}

loadEnvFile();

const weatherMiddleware = createWeatherApiMiddleware(
  () => process.env.WEATHER_API_KEY || '',
);

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.map': 'application/json',
};

function sendFile(res, filePath) {
  const ext = path.extname(filePath).toLowerCase();
  res.statusCode = 200;
  res.setHeader('Content-Type', MIME[ext] || 'application/octet-stream');
  fs.createReadStream(filePath).pipe(res);
}

function safeJoin(base, requestPath) {
  const decoded = decodeURIComponent(requestPath.split('?')[0]);
  const normalized = path.normalize(decoded).replace(/^(\.\.[/\\])+/, '');
  const full = path.join(base, normalized);
  if (!full.startsWith(base)) return null;
  return full;
}

const server = http.createServer(async (req, res) => {
  const url = req.url || '/';

  if (url.startsWith('/api/weather')) {
    await weatherMiddleware(req, res, () => {
      res.statusCode = 404;
      res.end('Not found');
    });
    return;
  }

  if (!fs.existsSync(DIST)) {
    res.statusCode = 503;
    res.setHeader('Content-Type', 'text/plain; charset=utf-8');
    res.end('Build missing. Run npm run build first.');
    return;
  }

  let filePath = safeJoin(DIST, url === '/' ? '/index.html' : url);
  if (filePath && fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    sendFile(res, filePath);
    return;
  }

  // SPA fallback
  const indexHtml = path.join(DIST, 'index.html');
  if (fs.existsSync(indexHtml)) {
    sendFile(res, indexHtml);
    return;
  }

  res.statusCode = 404;
  res.end('Not found');
});

server.listen(PORT, () => {
  console.log(`Weather app listening on http://localhost:${PORT}`);
  if (!process.env.WEATHER_API_KEY) {
    console.warn('Warning: WEATHER_API_KEY is not set. /api/weather will fail until it is configured.');
  }
});
