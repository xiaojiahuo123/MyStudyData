// Crawl hollyfa download center paginated lists and extract all file entries
import https from 'node:https';
import { writeFileSync } from 'node:fs';

const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';

function get(u, redirects = 0) {
  return new Promise((res, rej) => {
    if (redirects > 5) return rej(new Error('too many redirects'));
    const req = https.get(u, { headers: { 'User-Agent': UA } }, (x) => {
      if ([301, 302, 303, 307, 308].includes(x.statusCode) && x.headers.location) {
        x.resume();
        return res(get(new URL(x.headers.location, u).href, redirects + 1));
      }
      let d = '';
      x.on('data', (c) => (d += c));
      x.on('end', () => res({ status: x.statusCode, data: d }));
    });
    req.setTimeout(30000, () => { req.destroy(); rej(new Error('timeout')); });
    req.on('error', rej);
  });
}

function extract(data) {
  const out = [];
  const re = /value="([^"]*fileUrl[^"]*)"/g;
  let m;
  while ((m = re.exec(data))) {
    let v = m[1].replace(/&quot;/g, '"').replace(/&amp;/g, '&');
    if (v.startsWith('[')) v = v.slice(1, -1);
    try {
      const j = JSON.parse(v);
      if (j.fileUrl && j.name) out.push({ name: j.name, size: j.size, url: j.fileUrl });
    } catch (e) { /* skip */ }
  }
  const seen = new Set();
  return out.filter((o) => (seen.has(o.url) ? false : (seen.add(o.url), true)));
}

const listId = process.argv[2];
const pageCount = Number(process.argv[3] || 95);
const all = [];
const queue = [];
for (let p = 1; p <= pageCount; p++) queue.push(p);

let done = 0;
async function worker() {
  while (queue.length) {
    const p = queue.shift();
    const u = 'https://www.hollyfa.com/download/' + listId + '-' + (p * 10) + '-10.html';
    try {
      const { status, data } = await get(u);
      const items = extract(data);
      if (items.length) console.log('page ' + p + ': ' + items.length + ' entries: ' + items.map((i) => i.name.slice(0, 28)).join(' | '));
      else console.log('page ' + p + ': 0 entries status ' + status);
      for (const it of items) all.push(Object.assign({ page: p }, it));
    } catch (e) {
      console.log('page ' + p + ': ERR ' + e.message);
    }
    done++;
    if (done % 20 === 0) console.log('progress ' + done + '/' + pageCount);
  }
}

await Promise.all([worker(), worker(), worker(), worker()]);

const text = all.map((o) => [o.page, o.name, o.size, o.url].join('\t')).join('\n');
writeFileSync(new URL('./hollyfa_all.txt', import.meta.url), text, 'utf8');
console.log('');
console.log('TOTAL entries:', all.length, '-> saved hollyfa_all.txt');
const kw = /LM|LE|G3|PowerPro|AutoThink|PLC|可编程|指令|选型|硬件|手册|培训|教程|HMI|编程|软件/;
const hits = all.filter((o) => kw.test(o.name));
console.log('=== keyword hits (' + hits.length + ') ===');
for (const h of hits) console.log('page ' + h.page + ' | ' + h.name + ' | ' + h.size + ' | ' + h.url);