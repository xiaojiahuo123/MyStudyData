// Extract download entries from hollyfa download center pages
import https from 'node:https';
import { writeFileSync } from 'node:fs';

function get(u, redirects = 0) {
  return new Promise((res, rej) => {
    if (redirects > 5) return rej(new Error('too many redirects'));
    const req = https.get(u, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' } }, (x) => {
      if ([301, 302, 303, 307, 308].includes(x.statusCode) && x.headers.location) {
        x.resume();
        return res(get(new URL(x.headers.location, u).href, redirects + 1));
      }
      let d = '';
      x.on('data', (c) => (d += c));
      x.on('end', () => res({ status: x.statusCode, data: d, finalUrl: u }));
    });
    req.setTimeout(30000, () => { req.destroy(); rej(new Error('timeout')); });
    req.on('error', rej);
  });
}

const pages = process.argv.slice(2);
const out = [];
for (const u of pages) {
  try {
    const { status, data } = await get(u);
    out.push('== ' + u + ' status ' + status + ' len ' + data.length);
    // find anchors that contain 下载 or 预览 text
    const anchors = [...data.matchAll(/<a\b[^>]*>([\s\S]*?)<\/a>/gi)];
    for (const a of anchors) {
      const text = a[1].replace(/<[^>]+>/g, '').trim();
      if (/下载|预览/.test(text)) {
        const href = (a[0].match(/href=["']([^"']*)["']/i) || [])[1] || '';
        out.push('  [' + text + '] ' + href);
      }
    }
    // also dump nearby title-like spans for context: lines with size info
    const titles = [...data.matchAll(/<a\b([^>]*)>[\s\S]{0,200}?(?:MB|KB)[\s\S]{0,200}?<\/a>/gi)];
    for (const t of titles.slice(0, 40)) {
      out.push('  T: ' + t[0].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 160));
    }
  } catch (e) {
    out.push('== ' + u + ' ERR ' + e.message);
  }
}
const text = out.join('\n');
console.log(text.slice(0, 9000));
writeFileSync(new URL('./hollyfa_out.txt', import.meta.url), text, 'utf8');
