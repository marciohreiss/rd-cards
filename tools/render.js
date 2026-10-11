// Renderiza artboards .dc.html do canvas em JPG 1080x1440.
// Uso: node render.js <pasta-dos-dc-html> <pasta-de-saida> <prefixo> <arquivo1> [arquivo2 ...]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [srcDir, outDir, prefix, ...names] = process.argv.slice(2);
const fontsRoot = path.join(__dirname, 'node_modules', '@fontsource');

function face(family, pkg, weight) {
  const file = path.join(fontsRoot, pkg, 'files', `${pkg}-latin-${weight}-normal.woff2`);
  const b64 = fs.readFileSync(file).toString('base64');
  return `@font-face{font-family:"${family}";font-weight:${weight};font-style:normal;src:url(data:font/woff2;base64,${b64}) format("woff2");}`;
}
const fontCss = [
  face('Fredoka', 'fredoka', 500), face('Fredoka', 'fredoka', 600), face('Fredoka', 'fredoka', 700),
  face('Nunito', 'nunito', 400), face('Nunito', 'nunito', 700), face('Nunito', 'nunito', 800),
].join('\n');

function toHtml(source) {
  const m = source.match(/<x-dc>([\s\S]*?)<\/x-dc>/);
  if (!m) throw new Error('sem <x-dc>');
  let body = m[1].replace(/<helmet>[\s\S]*?<\/helmet>/, '');
  const props = source.match(/data-props='([^']*)'/);
  const accent = props ? (JSON.parse(props[1]).accent || {}).default : null;
  if (body.includes('{{accent}}') && !accent) throw new Error('accent sem valor padrão');
  body = body.split('{{accent}}').join(accent);
  if (/\{\{[^}]+\}\}/.test(body)) throw new Error('sobrou {{hole}} sem valor');
  return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${fontCss}
body{margin:0;font-family:"Nunito","Helvetica Neue",sans-serif}</style></head><body>${body}</body></html>`;
}

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1080, height: 1440 }, deviceScaleFactor: 1 });
  await ctx.route('**/*', (route) => route.abort()); // nada de rede: tudo embutido
  for (let i = 0; i < names.length; i++) {
    const page = await ctx.newPage();
    await page.setContent(toHtml(fs.readFileSync(path.join(srcDir, names[i]), 'utf8')), { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const info = await page.evaluate(() => {
      const root = document.body.firstElementChild;
      const r = root.getBoundingClientRect();
      const used = new Set();
      document.fonts.forEach((f) => { if (f.status === 'loaded') used.add(`${f.family} ${f.weight}`); });
      // texto que invade as áreas sem texto (150 px do topo, 170 px da direita) ou estoura o card
      const bad = [];
      const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
      while (walker.nextNode()) {
        const t = walker.currentNode;
        if (!t.textContent.trim()) continue;
        const range = document.createRange();
        range.selectNodeContents(t);
        for (const b of range.getClientRects()) {
          if (b.top < 150 || b.right > 1080 - 170 || b.bottom > 1440) {
            bad.push(`${t.textContent.trim().slice(0, 40)} [top ${Math.round(b.top)}, right ${Math.round(b.right)}, bottom ${Math.round(b.bottom)}]`);
            break;
          }
        }
      }
      return { w: r.width, h: r.height, scrollH: document.documentElement.scrollHeight, fonts: [...used].sort(), bad };
    });
    const out = path.join(outDir, `${prefix}_${String(i + 1).padStart(2, '0')}.jpg`);
    await page.screenshot({ path: out, type: 'jpeg', quality: 92, clip: { x: 0, y: 0, width: 1080, height: 1440 } });
    console.log(names[i], '->', path.basename(out), JSON.stringify(info));
    await page.close();
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
