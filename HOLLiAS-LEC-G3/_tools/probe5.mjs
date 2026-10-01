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
console.log('len', data.length);
const anchors = [...data.matchAll(/<a[^>]+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi)];
for (const m of anchors) {
  const t = m[2].replace(/<[^>]+>/g, '').trim();
  if (t && /下载|资料|手册|软件|文档/.test(t) && t.length < 50) console.log(t + '  =>  ' + m[1]);
}
console.log('--- all download-ish hrefs ---');
for (const m of anchors) {
  if (/download|file|ziliao/.test(m[1]) && m[1] !== 'javascript:;') console.log(m[1]);
}
