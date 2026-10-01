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
// all anchors with product-ish text
const anchors = [...data.matchAll(/<a[^>]+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi)];
for (const m of anchors) {
  const t = m[2].replace(/<[^>]+>/g, '').trim();
  if (t && /LE系列|LK系列|LX系列|工业软件|AutoThink|SCADA|编程|PLC|软件/.test(t) && t.length < 40) {
    console.log(t + '  =>  ' + m[1]);
  }
}
