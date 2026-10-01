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
// item titles: text after e_text-49 s_title
const titles = [...data.matchAll(/e_text-49 s_title">\s*([^<\n]+)/g)].map((m) => m[1].trim());
console.log('titles on page:');
titles.forEach((t) => console.log(' - ' + t));
// pagination links
const pages = [...data.matchAll(/<a[^>]+href="([^"]*download[^"]*)"[^>]*>([\s\S]*?)<\/a>/gi)];
console.log('download hrefs:');
for (const m of pages) console.log(m[2].replace(/<[^>]+>/g, '').trim() + ' => ' + m[1]);
// search for total pages info
const tot = data.match(/共[^<]{0,20}[頁页]/);
console.log('total:', tot && tot[0]);
// any api urls
const apis = [...data.matchAll(/["'](\/[^"']*(?:api|ajax|search|list)[^"']*)["']/gi)].map((m) => m[1]);
console.log('api-ish:', [...new Set(apis)].slice(0, 20));
