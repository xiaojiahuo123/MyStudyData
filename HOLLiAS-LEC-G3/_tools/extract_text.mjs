import { readFileSync, writeFileSync } from 'node:fs';
import pdfParse from 'pdf-parse';

const file = process.argv[2];
const out = process.argv[3];
const buf = readFileSync(file);
const res = await pdfParse(buf);
console.log('pages:', res.numpages);
writeFileSync(out, res.text, 'utf8');
console.log('text length:', res.text.length);
console.log('--- first 2000 chars ---');
console.log(res.text.slice(0, 2000));