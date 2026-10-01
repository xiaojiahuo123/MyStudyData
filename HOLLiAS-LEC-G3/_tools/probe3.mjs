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
let idx = 0, n = 0;
while ((idx = data.indexOf('fileUrl', idx)) !== -1 && n < 5) {
  console.log('--- hit at', idx, '---');
  console.log(data.slice(idx - 300, idx + 400));
  idx += 7; n++;
}
console.log('total fileUrl hits:', (data.match(/fileUrl/g) || []).length);
