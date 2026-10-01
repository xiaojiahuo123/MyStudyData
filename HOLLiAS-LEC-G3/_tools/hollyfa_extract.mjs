// Extract all file entries (name|size|fileUrl) from hollyfa download pages
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
    out.push('== ' + u + ' status ' + status);
    const re = /value="([{&][^"]*fileUrl[^"]*)"/g;
    let m;
    while ((m = re.exec(data))) {
      let v = m[1].replace(/&quot;/g, '"').replace(/&amp;/g, '&');
      if (v.startsWith('[')) v = v.slice(1, -1);
      try {
        const j = JSON.parse(v);
        out.push(j.name + ' | ' + j.size + ' | ' + j.fileUrl);
      } catch (e) {
        out.push('PARSE_FAIL ' + v.slice(0, 120));
      }
    }
    if (!re.lastIndex || out.length === 0) out.push('(no entries)');
  } catch (e) {
    out.push('== ' + u + ' ERR ' + e.message);
  }
}
const text = out.join('\n');
console.log(text.slice(0, 12000));
writeFileSync(new URL('./hollyfa_files.txt', import.meta.url), text, 'utf8');
