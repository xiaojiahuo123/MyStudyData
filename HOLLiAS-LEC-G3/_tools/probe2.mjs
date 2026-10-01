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
const { data } = await get(u);
const p = data.indexOf('HollyView');
console.log('HollyView at', p);
if (p >= 0) console.log(data.slice(p - 3500, p + 2500));
