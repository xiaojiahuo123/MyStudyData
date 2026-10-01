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
const anchors = [...data.matchAll(/<a[^>]+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi)];
const seen = new Set();
for (const m of anchors) {
  const t = m[2].replace(/<[^>]+>/g, '').trim();
  if (t && /培训|云课堂|课程|视频|教学/.test(t) && t.length < 60 && !seen.has(m[1])) {
    seen.add(m[1]);
    console.log(t + '  =>  ' + m[1]);
  }
}