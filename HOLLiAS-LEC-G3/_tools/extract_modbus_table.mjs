import { PDFParse } from 'pdf-parse';
import { readFileSync } from 'node:fs';
const buf = readFileSync('E:/Code/MyStudyData/HOLLiAS-LK220/downloads/01_系统手册/LK220系列可编程控制器系统手册201512.pdf');
const parser = new PDFParse({ data: new Uint8Array(buf) });
const result = await parser.getText();
await parser.destroy();
const text = result.text || '';
for (const needle of ['3801', '加 1', '加1', '+1', '基础上加']) {
  let i = text.indexOf(needle);
  let count = 0;
  let start = 0; let found = [];
  while ((i = text.indexOf(needle, start)) >= 0 && found.length < 12) {
    found.push(i); start = i + 1; count++;
  }
  console.log('NEEDLE[' + needle + '] count>=' + count);
  for (const idx of found.slice(0,6)) {
    console.log('  @' + idx + ': ' + text.slice(Math.max(0,idx-120), idx+160).replaceAll('\n','|'));
  }
}