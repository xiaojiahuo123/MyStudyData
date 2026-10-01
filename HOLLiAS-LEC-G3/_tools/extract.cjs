const { readFileSync, writeFileSync } = require('node:fs');
const { PDFParse } = require('pdf-parse');

const buf = readFileSync(process.argv[2]);
async function main() {
  const parser = new PDFParse({ data: buf });
  const result = await parser.getText();
  const pages = Array.isArray(result) ? result : [result];
  let full = '';
  for (let i = 0; i < pages.length; i++) {
    full += '===== PAGE ' + (i + 1) + ' =====\n' + (pages[i].text || '') + '\n';
  }
  console.log('pages:', pages.length);
  console.log('chars:', full.length);
  writeFileSync(process.argv[3], full, 'utf8');
  console.log(full.slice(0, 1500));
}
main().catch((e) => console.log('ERR:', e && e.message));