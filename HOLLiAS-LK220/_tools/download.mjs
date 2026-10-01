// Batch download files to ../downloads (run: node download.mjs <manifest.json>)
import http from 'node:http';
import https from 'node:https';
import { createWriteStream, existsSync, mkdirSync, readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const base = join(dirname(fileURLToPath(import.meta.url)), '..', 'downloads');
mkdirSync(base, { recursive: true });

const manifest = JSON.parse(readFileSync(process.argv[2], 'utf8'));

function download(item, redirects = 0) {
  return new Promise((res, rej) => {
    if (redirects > 6) return rej(new Error('too many redirects'));
    const lib = item.url.startsWith('https') ? https : http;
    // only encode once: raw manifest URLs may contain Chinese chars/spaces; redirect targets are pre-encoded
    const safe = /[^\x00-\x7F]/.test(item.url) ? encodeURI(item.url) : item.url;
    const u = new URL(safe);
    const req = lib.get(u, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://www.hollyfa.com/download/1871828135507615744-800-10.html', 'Accept': '*/*' } }, (x) => {
      if ([301, 302, 303, 307, 308].includes(x.statusCode) && x.headers.location) {
        x.resume();
        return res(download(Object.assign({}, item, { url: new URL(x.headers.location, u).href }), redirects + 1));
      }
      if (x.statusCode !== 200) {
        x.resume();
        return rej(new Error('HTTP ' + x.statusCode));
      }
      const file = join(base, item.file);
      mkdirSync(dirname(file), { recursive: true });
      const ws = createWriteStream(file);
      let n = 0;
      x.on('data', (c) => (n += c.length));
      x.pipe(ws);
      ws.on('finish', () => res({ ...item, bytes: n }));
      ws.on('error', rej);
    });
    req.setTimeout(120000, () => { req.destroy(new Error('timeout')); });
    req.on('error', rej);
  });
}

const results = [];
for (const item of manifest) {
  if (existsSync(join(base, item.file))) { console.log('SKIP(exists) ' + item.file); continue; }
  try {
    const r = await download(item);
    console.log('OK   ' + item.file + '  ' + (r.bytes / 1048576).toFixed(2) + ' MB');
    results.push(r);
  } catch (e) {
    console.log('FAIL ' + item.file + '  ' + e.message);
  }
}
console.log('done');