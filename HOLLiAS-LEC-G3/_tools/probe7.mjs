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

const data = await get(process.argv[2]);
const i = data.indexOf('...');
const seg = data.slice(i - 4000, i + 3000);
const anchors = [...seg.matchAll(/<a[^>]+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi)];
for (const m of anchors) {
  console.log((m[2].replace(/<[^>]+>/g, '').trim() || '(num)') + '  =>  ' + m[1]);
}
