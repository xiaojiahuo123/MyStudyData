import https from 'node:https';

function get(u) {
  return new Promise((res, rej) => {
    const req = https.get(u, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (x) => {
      let d = '';
      x.on('data', (c) => (d += c));
      x.on('end', () => res(d));
    });
    req.setTimeout(30000, () => { req.destroy(); rej(new Error('timeout')); });
    req.on('error', rej);
  });
}

const u = process.argv[2];
const data = await get(u);
// category links
const cats = [...data.matchAll(/<a[^>]+href="([^"]*video[^"]*)"[^>]*>([\s\S]*?)<\/a>/gi)];
for (const m of cats) {
  const t = m[2].replace(/<[^>]+>/g, '').trim();
  if (t) console.log('CAT ' + t + ' => ' + m[1]);
}
// detail links
const dets = [...data.matchAll(/<a[^>]+href="([^"]*(?:video_detail|video|detail)[^"]*)"[^>]*>([\s\S]*?)<\/a>/gi)];
console.log('--- detail-ish links ---');
for (const m of dets) {
  const t = m[2].replace(/<[^>]+>/g, '').trim();
  if (t && t.length < 60) console.log(t + ' => ' + m[1]);
}