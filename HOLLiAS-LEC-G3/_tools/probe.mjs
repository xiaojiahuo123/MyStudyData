import https from 'node:https';

function get(u) {
  return new Promise((res, rej) => {
    const req = https.get(u, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' } }, (x) => {
      let d = '';
      x.on('data', (c) => (d += c));
      x.on('end', () => res({ status: x.statusCode, data: d }));
    });
    req.setTimeout(30000, () => { req.destroy(); rej(new Error('timeout')); });
    req.on('error', rej);
  });
}

const u = process.argv[2];
const { status, data } = await get(u);
console.log('status', status, 'len', data.length);
const p = data.indexOf('javascript:;');
console.log('first js button at', p);
if (p >= 0) console.log(data.slice(p - 2500, p + 900));
// list entry titles with sizes
const entries = [];
const re = /<h\d[^>]*>([\s\S]*?)<\/h\d>/gi;
let m;
while ((m = re.exec(data))) {
  const t = m[1].replace(/<[^>]+>/g, '').trim();
  if (t && t.length < 120) entries.push(t);
}
console.log('HEADINGS:');
console.log(entries.slice(0, 60).join('\n'));
