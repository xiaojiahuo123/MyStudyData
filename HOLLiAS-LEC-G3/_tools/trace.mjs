import https from 'node:https';

const start = 'https://omo-oss-file110.thefastfile.com/portal-saas/pg2024102318492727606/cms/file/le%E7%B3%BB%E5%88%97%E5%8F%AF%E7%BC%96%E7%A8%8B%E6%8E%A7%E5%88%B6%E5%99%A8%E7%A1%AC%E4%BB%B6%E6%89%8B%E5%86%8C.pdf';
const ref = 'https://www.hollyfa.com/download/1871828135507615744-800-10.html';

function step(u, n) {
  return new Promise((res) => {
    if (n > 8) return res('too many');
    const req = https.get(u, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': ref, 'Accept': '*/*' } }, (x) => {
      console.log(n, x.statusCode, 'loc:', (x.headers.location || '').slice(0, 150));
      if ([301, 302, 303, 307, 308].includes(x.statusCode) && x.headers.location) {
        x.resume();
        return res(step(new URL(x.headers.location, u).href, n + 1));
      }
      let d = '';
      x.on('data', (c) => (d += c));
      x.on('end', () => res('final ' + x.statusCode + ' ' + x.headers['content-type'] + ' len ' + d.length));
    });
    req.setTimeout(25000, () => { req.destroy(); res('timeout'); });
    req.on('error', (e) => res('ERR ' + e.message));
  });
}

console.log('result:', await step(start, 0));