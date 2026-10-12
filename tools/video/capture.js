// Captura quadros do index.html (animações CSS posicionadas por window.seek).
// Quadros: node capture.js frames <index.html> <pasta> <fps> <parte> <partes>
// Conferência: node capture.js check <index.html> <pasta> <t1,t2,...>
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [mode, htmlPath, outDir, ...rest] = process.argv.slice(2);

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await ctx.route('**/*', (r) => (r.request().url().startsWith('file:') ? r.continue() : r.abort()));
  const page = await ctx.newPage();
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const total = await page.evaluate(() => window.TOTAL);

  if (mode === 'check') {
    for (const t of rest[0].split(',').map(Number)) {
      await page.evaluate((x) => window.seek(x), t);
      const info = await page.evaluate(() => {
        const bad = [];
        let maxBottom = 0;
        for (const sc of document.querySelectorAll('.scene')) {
          if (parseFloat(getComputedStyle(sc).opacity) < 0.5) continue;
          const c = sc.querySelector('.content').getBoundingClientRect();
          maxBottom = Math.round(c.bottom);
          const w = document.createTreeWalker(sc, NodeFilter.SHOW_TEXT);
          while (w.nextNode()) {
            const n = w.currentNode;
            if (!n.textContent.trim()) continue;
            const r = document.createRange();
            r.selectNodeContents(n);
            for (const b of r.getClientRects()) {
              if (b.top < 150 || b.right > 912 || b.left < 60 || b.bottom > 1310) {
                bad.push(`${n.textContent.trim().slice(0, 36)} [l ${Math.round(b.left)} t ${Math.round(b.top)} r ${Math.round(b.right)} b ${Math.round(b.bottom)}]`);
                break;
              }
            }
          }
        }
        const caps = [...document.querySelectorAll('.cap')].filter((c) => parseFloat(getComputedStyle(c).opacity) > 0.5)
          .map((c) => { const r = c.querySelector('span').getBoundingClientRect(); return `${c.textContent} [${Math.round(r.left)}-${Math.round(r.right)} x ${Math.round(r.top)}-${Math.round(r.bottom)}]`; });
        return { contentBottom: maxBottom, bad, caps };
      }, null);
      await page.screenshot({ path: path.join(outDir, `check_${t.toFixed(2)}.jpg`), type: 'jpeg', quality: 80 });
      console.log(t.toFixed(2), JSON.stringify(info));
    }
  } else {
    const fps = Number(rest[0]);
    const part = Number(rest[1]);
    const parts = Number(rest[2]);
    const n = Math.ceil(total * fps);
    for (let i = part; i < n; i += parts) {
      await page.evaluate((x) => window.seek(x), i / fps);
      await page.screenshot({ path: path.join(outDir, `f_${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 93 });
    }
    console.log(`parte ${part}/${parts} pronta (${n} quadros no total)`);
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
