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

for (const u of process.argv.slice(2)) {
  const data = await get(u);
  console.log('== ' + u + ' len ' + data.length);
  const titles = [...data.matchAll(/e_text[^>]*>\s*([^<\n]{4,80})/g)].map((m) => m[1].trim());
  console.log([...new Set(titles)].slice(0, 40).join('\n'));
}