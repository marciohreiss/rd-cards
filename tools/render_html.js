// Renderiza páginas HTML completas (1080x1440) em JPG, embutindo as fontes do @fontsource.
// O HTML deve conter o marcador /*FONTS*/ dentro de um <style>.
// Uso: node render_html.js <pasta-html> <pasta-saida> <prefixo> <arquivo1> [arquivo2 ...]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [srcDir, outDir, prefix, ...names] = process.argv.slice(2);
const root = path.join(__dirname, 'node_modules', '@fontsource');

function face(family, pkg, weight) {
  const file = path.join(root, pkg, 'files', `${pkg}-latin-${weight}-normal.woff2`);
  const b64 = fs.readFileSync(file).toString('base64');
  return `@font-face{font-family:"${family}";font-weight:${weight};font-style:normal;src:url(data:font/woff2;base64,${b64}) format("woff2");}`;
}
const fontCss = [
  ['Space Grotesk', 'space-grotesk', [400, 500, 700]],
  ['JetBrains Mono', 'jetbrains-mono', [400, 700]],
  ['Barlow Condensed', 'barlow-condensed', [500, 700, 800]],
  ['Barlow', 'barlow', [400, 600, 700]],
].flatMap(([fam, pkg, ws]) => ws.map((w) => face(fam, pkg, w))).join('\n');

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1440 } });
  let i = 0;
  for (const name of names) {
    i += 1;
    const html = fs.readFileSync(path.join(srcDir, name), 'utf8').replace('/*FONTS*/', fontCss);
    await page.setContent(html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const info = await page.evaluate(() => {
      const bad = [];
      document.querySelectorAll('[data-safe] *').forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.width && (r.right > 1080 - 120 || r.bottom > 1440 - 40 || r.top < 0)) bad.push(el.textContent.trim().slice(0, 40));
      });
      return { scrollH: document.documentElement.scrollHeight, bad: [...new Set(bad)].slice(0, 5) };
    });
    const out = path.join(outDir, `${prefix}_${String(i).padStart(2, '0')}.jpg`);
    await page.screenshot({ path: out, type: 'jpeg', quality: 92, clip: { x: 0, y: 0, width: 1080, height: 1440 } });
    console.log(name, '->', path.basename(out), JSON.stringify(info));
  }
  await browser.close();
})();
