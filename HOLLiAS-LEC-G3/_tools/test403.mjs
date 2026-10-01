import https from 'node:https';

const url = 'https://omo-oss-file110.thefastfile.com/portal-saas/pg2024102318492727606/cms/file/le%E7%B3%BB%E5%88%97%E5%8F%AF%E7%BC%96%E7%A8%8B%E6%8E%A7%E5%88%B6%E5%99%A8%E7%A1%AC%E4%BB%B6%E6%89%8B%E5%86%8C.pdf';
const variants = [
  { label: 'plain', headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' } },
  { label: 'referer', headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://www.hollyfa.com/download/1871828135507615744-800-10.html' } },
  { label: 'referer+origin', headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://www.hollyfa.com/', 'Origin': 'https://www.hollyfa.com' } },
  { label: 'sec-fetch', headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://www.hollyfa.com/download/1871828135507615744-800-10.html', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'cross-site', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'zh-CN,zh;q=0.9' } }
];

function tryGet(v) {
  return new Promise((res) => {
    const req = https.get(url, { headers: v.headers }, (x) => {
      let d = '';
      x.on('data', (c) => (d += c));
      x.on('end', () => res({ label: v.label, status: x.statusCode, headers: x.headers, body: d.slice(0, 300) }));
    });
    req.setTimeout(20000, () => { req.destroy(); res({ label: v.label, status: 'TIMEOUT' }); });
    req.on('error', (e) => res({ label: v.label, status: 'ERR ' + e.message }));
  });
}

for (const v of variants) {
  const r = await tryGet(v);
  console.log(r.label, '->', r.status);
  if (r.headers) console.log('  headers:', JSON.stringify({ 'content-type': r.headers['content-type'], 'server': r.headers.server, 'x-cache': r.headers['x-cache'], 'etag': r.headers.etag }));
  if (r.body) console.log('  body:', r.body.slice(0, 200));
}