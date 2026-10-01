// Scrape download pages for direct file links (run: node scrape.mjs)
import http from 'node:http';
import https from 'node:https';

const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';

function get(u, redirects = 0) {
  return new Promise((res, rej) => {
    if (redirects > 5) return rej(new Error('too many redirects'));
    const lib = u.startsWith('https') ? https : http;
    const req = lib.get(u, { headers: { 'User-Agent': UA } }, (x) => {
      if ([301, 302, 303, 307, 308].includes(x.statusCode) && x.headers.location) {
        const next = new URL(x.headers.location, u).href;
        x.resume();
        return res(get(next, redirects + 1));
      }
      let d = '';
      x.on('data', (c) => (d += c));
      x.on('end', () => res({ status: x.statusCode, data: d, finalUrl: u }));
    });
    req.setTimeout(25000, () => { req.destroy(); rej(new Error('timeout')); });
    req.on('error', rej);
  });
}

const pages = process.argv.slice(2);
for (const u of pages) {
  try {
    const { status, data, finalUrl } = await get(u);
    console.log(`== ${u} -> status ${status} len ${data.length}`);
    const files = [...data.matchAll(/href=["']([^"']+\.(?:pdf|rar|zip|7z)[^"']*)["']/gi)]
      .map((m) => new URL(m[1], finalUrl).href);
    console.log([...new Set(files)].slice(0, 20).join('\n') || '(no file links)');
  } catch (e) {
    console.log(`== ${u} ERR ${e.message}`);
  }
}
