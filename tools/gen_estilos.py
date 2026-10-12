"""Dois padrões de arte novos da R&D (além do neon quente):
- DRONE: painel de voo (HUD) azul-noite, linhas ciano, telemetria em fonte mono.
- TRAIL: mapa topográfico em papel creme, verde-mata e laranja, títulos condensados e placas de trilha.
Gera páginas HTML 1080x1440 para render_html.js.
Uso: python3 gen_estilos.py <pasta de saída>"""
import math
import pathlib
import random
import sys

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)


def page(title, css, body):
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{title}</title>
<style>/*FONTS*/
*{{box-sizing:border-box}} body{{margin:0}}
{css}
</style></head><body>{body}</body></html>'''


# =============================================================== DRONE (HUD)
NAVY, NAVY2, CYAN, ICE, DIM = "#06101C", "#0B1B2E", "#3EC6FF", "#EAF6FF", "#7FA3BF"
DCSS = f'''
.c{{position:relative;width:1080px;height:1440px;overflow:hidden;color:{ICE};font-family:"Space Grotesk",sans-serif;
  background:radial-gradient(900px 700px at 80% 12%,rgba(62,198,255,.20),transparent 70%),
  radial-gradient(800px 700px at 0% 100%,rgba(62,198,255,.12),transparent 70%),
  linear-gradient(rgba(62,198,255,.07) 1px,transparent 1px) 0 0/60px 60px,
  linear-gradient(90deg,rgba(62,198,255,.07) 1px,transparent 1px) 0 0/60px 60px,{NAVY}}}
.br{{position:absolute;width:64px;height:64px;border:3px solid {CYAN};opacity:.7}}
.in{{position:absolute;inset:0;padding:150px 170px 56px 72px;display:flex;flex-direction:column}}
.mono{{font-family:"JetBrains Mono",monospace}}
.top{{display:flex;justify-content:space-between;align-items:center;font-family:"JetBrains Mono",monospace;font-size:22px;letter-spacing:.08em;color:{DIM}}}
.top b{{color:{CYAN}}}
.seg{{display:flex;gap:6px;margin-top:14px}} .seg i{{height:6px;flex:1;background:rgba(62,198,255,.18)}} .seg i.on{{background:{CYAN};box-shadow:0 0 14px {CYAN}}}
.tag{{align-self:flex-start;margin-top:38px;font-family:"JetBrains Mono",monospace;font-size:24px;letter-spacing:.1em;text-transform:uppercase;color:{NAVY};background:{CYAN};padding:8px 18px}}
.tagl{{align-self:flex-start;margin-top:38px;font-family:"JetBrains Mono",monospace;font-size:24px;letter-spacing:.1em;text-transform:uppercase;color:{CYAN};border:2px solid {CYAN};padding:6px 16px}}
h1,h2{{margin:22px 0 0;font-weight:700;letter-spacing:-.02em;line-height:1.02}} h1{{font-size:84px}} h2{{font-size:70px}}
h1 em,h2 em{{font-style:normal;color:{CYAN};text-shadow:0 0 30px rgba(62,198,255,.5)}}
.p{{margin-top:22px;font-size:31px;line-height:1.36;color:#C9DCEB}}
.panel{{margin-top:34px;border:2px solid rgba(62,198,255,.45);background:rgba(11,27,46,.75);position:relative}}
.panel .lbl{{position:absolute;top:-16px;left:22px;background:{NAVY};padding:0 10px;font-family:"JetBrains Mono",monospace;font-size:20px;color:{CYAN};letter-spacing:.1em}}
.read{{display:flex;gap:14px;flex-wrap:wrap;margin-top:22px}}
.read div{{font-family:"JetBrains Mono",monospace;font-size:24px;border:1px solid rgba(62,198,255,.5);padding:10px 16px;background:rgba(6,16,28,.7)}}
.read div b{{color:{CYAN}}}
.row{{display:flex;align-items:center;gap:18px;border-left:4px solid {CYAN};background:rgba(11,27,46,.8);padding:16px 20px;font-size:28px;line-height:1.3}}
.row b{{color:#fff}}
.note{{margin-top:26px;font-size:27px;line-height:1.35;color:#C9DCEB;border:1px dashed rgba(62,198,255,.6);padding:16px 20px}}
.note b{{color:{CYAN};font-family:"JetBrains Mono",monospace;font-weight:700}}
.cta{{display:flex;justify-content:space-between;align-items:center;background:{CYAN};color:{NAVY};padding:22px 28px;font-size:32px;font-weight:700}}
.cta span:last-child{{font-family:"JetBrains Mono",monospace}}
.ask{{border:2px solid {CYAN};padding:22px 28px;background:rgba(11,27,46,.85);box-shadow:0 0 40px rgba(62,198,255,.25)}}
.ask div:first-child{{font-size:40px;font-weight:700}} .ask div:last-child{{margin-top:8px;font-family:"JetBrains Mono",monospace;font-size:24px;color:{CYAN}}}
.ft{{margin-top:22px;border-top:1px solid rgba(62,198,255,.35);padding-top:14px;font-family:"JetBrains Mono",monospace;font-size:18px;line-height:1.45;color:{DIM}}}
.grow{{flex-grow:1}}
'''


def drone(x, y, s=1.0, glow=True):
    a = 34 * s
    r = 17 * s
    g = f' filter="url(#gl)"' if glow else ""
    rotors = "".join(f'<circle cx="{x+dx*a}" cy="{y+dy*a}" r="{r}" fill="none" stroke="{CYAN}" stroke-width="{2.5*s}"/>'
                     for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)))
    arms = (f'<line x1="{x-a}" y1="{y-a}" x2="{x+a}" y2="{y+a}" stroke="{ICE}" stroke-width="{4*s}"/>'
            f'<line x1="{x+a}" y1="{y-a}" x2="{x-a}" y2="{y+a}" stroke="{ICE}" stroke-width="{4*s}"/>')
    body = f'<rect x="{x-14*s}" y="{y-10*s}" width="{28*s}" height="{20*s}" rx="{6*s}" fill="{ICE}"/>'
    return f'<g{g}>{arms}{rotors}{body}</g>'


DEFS = (f'<defs><filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        f'<marker id="ar" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0 0L10 5L0 10z" fill="{CYAN}"/></marker></defs>')


def svg(w, h, inner):
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block">{DEFS}{inner}</svg>'


def path(d, dash=True, w=4):
    da = ' stroke-dasharray="14 12"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{CYAN}" stroke-width="{w}"{da} marker-end="url(#ar)" filter="url(#gl)"/>'


def dot(x, y, r=12, label=""):
    t = (f'<text x="{x}" y="{y+r+30}" text-anchor="middle" font-family="JetBrains Mono" font-size="20" fill="{DIM}">{label}</text>'
         if label else "")
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFB547"/><circle cx="{x}" cy="{y}" r="{r+10}" fill="none" stroke="#FFB547" stroke-opacity=".4" stroke-width="2"/>{t}'


def dcard(n, total, body, uso=""):
    segs = "".join(f'<i class="{"on" if i <= n else ""}"></i>' for i in range(1, total + 1))
    corners = (f'<div class="br" style="top:40px;left:40px;border-right:0;border-bottom:0"></div>'
               f'<div class="br" style="top:40px;right:40px;border-left:0;border-bottom:0"></div>'
               f'<div class="br" style="bottom:40px;left:40px;border-right:0;border-top:0"></div>'
               f'<div class="br" style="bottom:40px;right:40px;border-left:0;border-top:0"></div>')
    head = (f'<div class="top"><span><b>R&amp;D</b> // LAB DE DRONE</span><span>{uso or "REC ●"} · {n:02d}/{total:02d}</span></div>'
            f'<div class="seg">{segs}</div>')
    return page("DJI Neo 2", DCSS, f'<div class="c">{corners}<div class="in" data-safe>{head}{body}</div></div>')


FD = "DJI (lançamento, nov/2025) e ficha técnica do varejo · checado em 12/10/2026"
ND = 8
DJI = [
    dcard(1, ND, f'''
<div class="tag">Publi · drone compacto</div>
<h1>6 usos do DJI Neo 2 pra quem <em>nunca pilotou</em></h1>
<div class="p">Decola da mão, segue você sozinho e grava em vertical.</div>
<div class="panel" style="height:470px"><span class="lbl">MODO DE VOO</span>{svg(834, 466,
    f'<ellipse cx="417" cy="250" rx="300" ry="120" fill="none" stroke="{CYAN}" stroke-opacity=".5" stroke-width="2" stroke-dasharray="10 10"/>'
    f'<ellipse cx="417" cy="250" rx="190" ry="72" fill="none" stroke="{CYAN}" stroke-opacity=".3" stroke-width="2"/>'
    + drone(417, 210, 2.1) + dot(150, 300, 10) + dot(690, 320, 10) +
    f'<text x="40" y="440" font-family="JetBrains Mono" font-size="20" fill="{DIM}">4K/60 · 2,7K VERT · 19 MIN</text>')}</div>
<div class="grow"></div>
<div class="cta"><span>Arrasta e escolhe o seu</span><span>&gt;&gt;</span></div>
<div class="ft">FONTE: {FD}</div>''', "CAPA"),
    dcard(2, ND, f'''
<div class="tagl">Uso 1 · corrida, trilha, pedal</div>
<h2>Ele te <em>segue</em> sozinho</h2>
<div class="panel" style="height:430px"><span class="lbl">ACTIVETRACK</span>{svg(834, 426,
    path("M120 330 C 260 180, 420 380, 560 230 S 760 140, 790 120") + dot(560, 230, 12, "VOCÊ") + drone(380, 120, 1.3) +
    path("M380 160 C 450 200, 500 210, 535 220", True, 3))}</div>
<div class="read"><div>VEL <b>até 12 m/s</b></div><div>DIR <b>8 direções</b></div><div>ÁREA <b>aberta</b></div></div>
<div class="note"><b>SEM CONTROLE NA MÃO:</b> você corre, ele filma.</div>
<div class="grow"></div><div class="ft">FONTE: {FD}</div>''', "USO 1"),
    dcard(3, ND, f'''
<div class="tagl">Uso 2 · viagem</div>
<h2>Decola e pousa <em>na palma da mão</em></h2>
<div class="panel" style="height:430px"><span class="lbl">RETORNO PARA A PALMA</span>{svg(834, 426,
    f'<ellipse cx="417" cy="360" rx="150" ry="34" fill="none" stroke="#FFB547" stroke-width="3"/>'
    f'<ellipse cx="417" cy="360" rx="90" ry="20" fill="none" stroke="#FFB547" stroke-opacity=".5" stroke-width="2"/>'
    f'<text x="417" y="414" text-anchor="middle" font-family="JetBrains Mono" font-size="20" fill="{DIM}">PALMA</text>'
    + drone(417, 120, 1.5) + path("M330 300 L 330 170", False, 3) + path("M504 170 L 504 300", False, 3) +
    f'<text x="300" y="240" text-anchor="end" font-family="JetBrains Mono" font-size="20" fill="{CYAN}">DECOLA</text>'
    f'<text x="534" y="240" font-family="JetBrains Mono" font-size="20" fill="{CYAN}">POUSA</text>')}</div>
<div class="p">Sem procurar chão plano. O "Retorno para a palma" faz ele achar sua mão e pousar de volta.</div>
<div class="grow"></div><div class="ft">FONTE: {FD}</div>''', "USO 2"),
    dcard(4, ND, f'''
<div class="tagl">Uso 3 · foto de grupo</div>
<h2>Selfie <em>sem pau de selfie</em></h2>
<div class="panel" style="height:360px"><span class="lbl">ENQUADRAMENTO</span>{svg(834, 356,
    drone(150, 170, 1.4) + path("M230 170 L 420 170", True, 3) +
    f'<path d="M460 110 V70 H500 M720 70 H760 V110 M760 240 V280 H720 M500 280 H460 V240" fill="none" stroke="{ICE}" stroke-width="4"/>' +
    dot(545, 190, 14) + dot(610, 175, 14) + dot(675, 190, 14))}</div>
<div style="display:flex;flex-direction:column;gap:12px;margin-top:26px">
<div class="row"><b>SelfieShot:</b>&nbsp;foto e vídeo sem usar as mãos</div>
<div class="row"><b>Gestos:</b>&nbsp;a palma guia pra cima, baixo e lados</div>
<div class="row"><b>Voz e app</b>&nbsp;também controlam</div></div>
<div class="grow"></div><div class="ft">FONTE: {FD}</div>''', "USO 3"),
    dcard(5, ND, f'''
<div class="tagl">Uso 4 · conteúdo pro TikTok</div>
<h2>Grava <em>em pé</em>, já no formato</h2>
<div class="panel" style="height:470px"><span class="lbl">FORMATOS</span>{svg(834, 466,
    f'<rect x="90" y="50" width="210" height="373" rx="18" fill="rgba(62,198,255,.08)" stroke="{CYAN}" stroke-width="4" filter="url(#gl)"/>'
    f'<text x="195" y="250" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="64" fill="{ICE}">2,7K</text>'
    f'<text x="195" y="295" text-anchor="middle" font-family="JetBrains Mono" font-size="22" fill="{CYAN}">VERTICAL</text>'
    f'<rect x="380" y="140" width="380" height="214" rx="14" fill="none" stroke="{DIM}" stroke-width="3"/>'
    f'<text x="570" y="255" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="56" fill="{ICE}">4K/60</text>'
    f'<text x="570" y="298" text-anchor="middle" font-family="JetBrains Mono" font-size="22" fill="{DIM}">HORIZONTAL</text>')}</div>
<div class="read"><div>GIMBAL <b>2 eixos</b></div><div>SEM CORTE <b>depois</b></div></div>
<div class="grow"></div><div class="ft">FONTE: {FD}</div>''', "USO 4"),
    dcard(6, ND, f'''
<div class="tagl">Uso 5 · câmera lenta</div>
<h2>Salto, chegada, <em>respingo</em></h2>
<div class="panel" style="height:440px"><span class="lbl">FPS</span>{svg(834, 436,
    f'<path d="M187 360 A 230 230 0 0 1 647 360" fill="none" stroke="rgba(62,198,255,.25)" stroke-width="26"/>'
    f'<path d="M187 360 A 230 230 0 0 1 600 220" fill="none" stroke="{CYAN}" stroke-width="26" filter="url(#gl)"/>'
    f'<text x="417" y="320" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="110" fill="{ICE}">100</text>'
    f'<text x="417" y="370" text-anchor="middle" font-family="JetBrains Mono" font-size="26" fill="{CYAN}">FPS EM 4K</text>')}</div>
<div class="p">Câmera lenta com resolução alta, pra deixar o momento durar.</div>
<div class="grow"></div><div class="ft">FONTE: {FD}</div>''', "USO 5"),
    dcard(7, ND, f'''
<div class="tagl">Uso 6 · primeiro drone</div>
<h2>Feito pra <em>errar menos</em></h2>
<div class="panel" style="height:330px"><span class="lbl">SENSORES</span>{svg(834, 326,
    "".join(f'<circle cx="417" cy="163" r="{r}" fill="none" stroke="{CYAN}" stroke-opacity="{o}" stroke-width="2"/>' for r, o in ((60, .6), (110, .4), (150, .25)))
    + f'<path d="M417 163 L 560 110 A 150 150 0 0 1 567 163 Z" fill="rgba(62,198,255,.25)"/>' + drone(417, 163, 1.0)
    + dot(520, 70, 8) + dot(300, 240, 8) +
    f'<text x="600" y="60" font-family="JetBrains Mono" font-size="20" fill="{CYAN}">LiDAR FRONTAL</text>')}</div>
<div style="display:flex;flex-direction:column;gap:12px;margin-top:24px">
<div class="row"><b>Obstáculos:</b>&nbsp;detecção em todas as direções</div>
<div class="row"><b>19 min</b>&nbsp;de voo por bateria</div>
<div class="row"><b>49 GB</b>&nbsp;de armazenamento interno</div></div>
<div class="note"><b>ANTES DE VOAR:</b> confira as regras da ANAC e do DECEA.</div>
<div class="grow"></div><div class="ft">FONTE: {FD}</div>''', "USO 6"),
    dcard(8, ND, f'''
<div class="tag">Sua vez</div>
<h2>Qual desses usos <em>é a sua cara?</em></h2>
<div class="p">Salva pra lembrar na próxima viagem. Os combos mudam de loja pra loja: confira o que vem no kit antes de comprar.</div>
<div class="read" style="margin-top:34px"><div><b>1</b> corrida</div><div><b>2</b> viagem</div><div><b>3</b> selfie</div><div><b>4</b> vertical</div><div><b>5</b> câmera lenta</div><div><b>6</b> 1º drone</div></div>
<div class="grow"></div>
<div class="ask"><div>Corrida, viagem ou selfie?</div><div>&gt; comenta o número do uso</div></div>
<div class="ft">FONTE: {FD}</div>''', "FIM"),
]

# =============================================================== TRAIL (topográfico)
CREAM, SAND, GREEN, ORANGE, INK = "#EFE6D2", "#D9CBAA", "#1E3A2B", "#D9541E", "#2B2A26"


def contours(seed, cx, cy, n=14):
    rnd = random.Random(seed)
    ph = [rnd.random() * 6.28 for _ in range(4)]
    out = []
    for k in range(1, n + 1):
        base = 40 + k * 48
        pts = []
        for i in range(0, 73):
            t = i / 72 * 2 * math.pi
            r = base * (1 + .12 * math.sin(3 * t + ph[0]) + .07 * math.sin(5 * t + ph[1] + k * .2) + .05 * math.sin(2 * t + ph[2]))
            pts.append(f"{cx + r * math.cos(t) * 1.25:.1f},{cy + r * math.sin(t):.1f}")
        w = 2.2 if k % 5 == 0 else 1.2
        out.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="#B9A57F" stroke-opacity=".55" stroke-width="{w}"/>')
    return "".join(out)


TCSS = f'''
.c{{position:relative;width:1080px;height:1440px;overflow:hidden;color:{INK};font-family:"Barlow",sans-serif;background:{CREAM}}}
.topo{{position:absolute;inset:0}}
.in{{position:absolute;inset:0;padding:150px 170px 56px 72px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:28px;letter-spacing:.12em;text-transform:uppercase;color:{GREEN}}}
.km{{background:{ORANGE};color:{CREAM};padding:4px 14px 4px 14px;clip-path:polygon(0 0,88% 0,100% 50%,88% 100%,0 100%);padding-right:30px}}
.trail{{margin-top:14px;height:6px;background:repeating-linear-gradient(90deg,{GREEN} 0 18px,transparent 18px 30px);opacity:.35;position:relative}}
.trail i{{position:absolute;top:-7px;width:20px;height:20px;border-radius:50%;background:{ORANGE};border:4px solid {CREAM}}}
.kick{{align-self:flex-start;margin-top:38px;font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:28px;letter-spacing:.12em;text-transform:uppercase;color:{CREAM};background:{GREEN};padding:6px 18px}}
h1,h2{{margin:20px 0 0;font-family:"Barlow Condensed",sans-serif;font-weight:800;text-transform:uppercase;line-height:.92;color:{GREEN};letter-spacing:-.005em}}
h1{{font-size:118px}} h2{{font-size:92px}} h1 em,h2 em{{font-style:normal;color:{ORANGE}}}
.p{{margin-top:22px;font-size:32px;line-height:1.38;color:#3E3B33}}
.p b{{color:{GREEN}}}
.sign{{display:flex;align-items:center;gap:18px;background:{GREEN};color:{CREAM};padding:14px 60px 14px 22px;font-size:30px;clip-path:polygon(0 0,93% 0,100% 50%,93% 100%,0 100%)}}
.sign b{{font-family:"Barlow Condensed",sans-serif;font-weight:800;font-size:34px;letter-spacing:.06em;text-transform:uppercase;color:#F2B48F;min-width:150px}}
.box{{margin-top:28px;border-left:8px solid {ORANGE};background:rgba(255,250,238,.85);padding:18px 24px;font-size:29px;line-height:1.36}}
.box b{{color:{ORANGE}}}
.bib{{background:#FFFDF6;border:2px solid #CDBF9E;box-shadow:0 10px 0 rgba(30,58,43,.12);position:relative;padding:58px 26px 22px}}
.bib:before{{content:"";position:absolute;left:0;right:0;top:0;height:36px;background:{ORANGE}}}
.bib .h{{position:absolute;top:4px;left:22px;font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:22px;letter-spacing:.12em;color:{CREAM};text-transform:uppercase}}
.bib .pin{{position:absolute;top:50px;width:14px;height:14px;border-radius:50%;border:3px solid #CDBF9E}}
.bib .n{{font-family:"Barlow Condensed",sans-serif;font-weight:800;font-size:64px;line-height:1;color:{GREEN}}}
.bib .s{{margin-top:4px;font-size:24px;color:#5A5547}}
.cta{{display:flex;justify-content:space-between;align-items:center;background:{ORANGE};color:{CREAM};padding:22px 28px;font-family:"Barlow Condensed",sans-serif;font-weight:800;font-size:40px;letter-spacing:.04em;text-transform:uppercase}}
.ask{{background:{GREEN};color:{CREAM};padding:22px 28px}}
.ask div:first-child{{font-family:"Barlow Condensed",sans-serif;font-weight:800;font-size:50px;text-transform:uppercase;line-height:1}}
.ask div:last-child{{margin-top:8px;font-size:26px;color:#F2B48F;font-weight:600}}
.ft{{margin-top:22px;border-top:2px solid rgba(30,58,43,.25);padding-top:14px;font-size:20px;line-height:1.4;color:#6A6453}}
.grow{{flex-grow:1}}
'''


def tcard(n, total, body, seed):
    topo = f'<svg class="topo" width="1080" height="1440">{contours(seed, 760 if seed % 2 else 300, 1080 if seed % 3 else 420)}</svg>'
    pos = (n - 1) / (total - 1) * 96
    head = (f'<div class="top"><span>R&amp;D · Diário de trilha</span><span class="km">KM {n:02d}/{total:02d}</span></div>'
            f'<div class="trail"><i style="left:{pos:.1f}%"></i></div>')
    return page("Trail", TCSS, f'<div class="c">{topo}<div class="in" data-safe>{head}{body}</div></div>')


def profile():
    pts = [0, 6, 14, 30, 44, 40, 52, 70, 88, 76, 60, 72, 95, 100, 82, 64, 50, 58, 40, 26, 18, 8]
    w, h = 836, 330
    step = w / (len(pts) - 1)
    line = " ".join(f"{i*step:.1f},{h-30-(v/100)*(h-80):.1f}" for i, v in enumerate(pts))
    area = f"0,{h} {line} {w},{h}"
    return (f'<svg width="{w}" height="{h}" style="display:block;margin-top:30px">'
            f'<polygon points="{area}" fill="{GREEN}" fill-opacity=".9"/>'
            f'<polyline points="{line}" fill="none" stroke="{ORANGE}" stroke-width="6" stroke-linejoin="round"/>'
            f'<text x="12" y="{h-12}" font-family="Barlow Condensed" font-weight="700" font-size="24" fill="{CREAM}">LARGADA</text>'
            f'<text x="{w-12}" y="{h-12}" text-anchor="end" font-family="Barlow Condensed" font-weight="700" font-size="24" fill="{CREAM}">36,87 KM</text>'
            f'<text x="{w-12}" y="28" text-anchor="end" font-family="Barlow" font-size="18" fill="#6A6453">perfil ilustrativo</text>'
            f'</svg>')


ST = "meus treinos e provas registrados no Strava (2026)"
NT = 7
TRAIL = [
    tcard(1, NT, f'''
<div class="kick">Trail run de verdade</div>
<h1>Treinar montanha numa <em>cidade plana</em></h1>
<div class="p">Moro em Uberlândia. Quase não tem subida. Mesmo assim terminei <b>La Misión, KTR e Paraty by UTMB</b> em 2026. Te conto como.</div>
<div class="grow"></div>
<div class="cta"><span>Arrasta: é o que eu faço</span><span>→</span></div>
<div class="ft">Relato pessoal · base: {ST}</div>''', 3),
    tcard(2, NT, f'''
<div class="kick">O tamanho do problema</div>
<h2>Montanha <em>não perdoa</em></h2>
{profile()}
<div style="display:flex;align-items:baseline;gap:18px;margin-top:22px"><span style="font-family:'Barlow Condensed';font-weight:800;font-size:120px;line-height:.9;color:{ORANGE}">2.675 m</span><span style="font-family:'Barlow Condensed';font-weight:700;font-size:34px;text-transform:uppercase;color:{GREEN}">de subida</span></div>
<div class="p" style="margin-top:8px">na La Misión Serra Fina. E aqui, o relevo não ajuda: subida tem que ser caçada.</div>
<div class="grow"></div><div class="ft">Fonte: {ST}</div>''', 4),
    tcard(3, NT, f'''
<div class="kick">A semana que funciona pra mim</div>
<h2>Cada dia, <em>uma subida</em></h2>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:32px">
<div class="sign"><b>Terça</b>tiros (velocidade)</div>
<div class="sign"><b>Quinta</b>rampa de 7% (força na subida)</div>
<div class="sign"><b>Sexta</b>escada (perna e cardio)</div>
<div class="sign"><b>Domingo</b>longão em trilha</div></div>
<div class="box"><b>+ treino de força</b> durante a semana.</div>
<div class="grow"></div><div class="ft">Rotina pessoal, não é prescrição. Procure um profissional para montar a sua.</div>''', 5),
    tcard(4, NT, f'''
<div class="kick">Onde acumular D+</div>
<h2>Ache o seu <em>morro de treino</em></h2>
<div class="p">Aqui, é a <b>Serrinha</b>: o lugar que mais soma altimetria e fica perto de casa. Logística boa vale mais que o morro perfeito longe.</div>
<div class="box">Treino que você repete <b>toda semana</b> ganha do treino épico uma vez por mês.</div>
<div class="grow"></div><div class="ft">Fonte: {ST}</div>''', 7),
    tcard(5, NT, f'''
<div class="kick">O que mudou</div>
<h2>Parei de <em>recomeçar</em> a cada prova</h2>
<div class="p">Agora o plano mira um objetivo só, e cada prova é um degrau dele.</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:30px">
<div class="bib"><span class="h">2026</span><span class="pin" style="left:14px"></span><span class="pin" style="right:14px"></span><div class="n">36,87 KM</div><div class="s">La Misión Serra Fina</div></div>
<div class="bib"><span class="h">2026</span><span class="pin" style="left:14px"></span><span class="pin" style="right:14px"></span><div class="n">30 KM</div><div class="s">KTR Campos do Jordão</div></div>
<div class="bib" style="grid-column:1/3"><span class="h">2026</span><span class="pin" style="left:14px"></span><span class="pin" style="right:14px"></span><div class="n">PARATY BY UTMB</div><div class="s">Paraty Brazil by UTMB</div></div>
</div>
<div class="grow"></div><div class="ft">Fonte: {ST}</div>''', 8),
    tcard(6, NT, f'''
<div class="kick">Próximo degrau</div>
<div class="bib" style="margin-top:34px;padding:80px 34px 34px"><span class="h">Meta · agosto de 2027</span><span class="pin" style="left:16px;top:66px"></span><span class="pin" style="right:16px;top:66px"></span>
<div class="n" style="font-size:210px;color:{ORANGE}">50K+</div><div class="s" style="font-size:30px">uma ultra · prova-alvo: La Misión 55K</div></div>
<div class="box">E não vou sozinho: <b>a Débora vai nos 18 km.</b> Objetivo e família na mesma prova.</div>
<div class="grow"></div><div class="ft">Planejamento pessoal 2027.</div>''', 10),
    tcard(7, NT, f'''
<div class="kick">Bora junto?</div>
<h2>Corre em cidade plana <em>também?</em></h2>
<div class="p">Salva esse post pro próximo treino e me conta onde você caça subida aí.</div>
<div class="grow"></div>
<div class="ask"><div>Onde você treina subida?</div><div>Comenta o nome do lugar.</div></div>
<div class="ft">Relato pessoal · Rico e Débora</div>''', 11),
]

for i, h in enumerate(DJI, 1):
    (OUT / f"DJI2_{i}.html").write_text(h, encoding="utf-8")
for i, h in enumerate(TRAIL, 1):
    (OUT / f"Trail2_{i}.html").write_text(h, encoding="utf-8")
print(len(DJI), "DJI;", len(TRAIL), "Trail")
