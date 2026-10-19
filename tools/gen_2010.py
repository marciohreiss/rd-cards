"""Gera os artboards .dc.html dos dois carrosséis da R&D de 20/10/2026 (6h live que vende sem janelinha, 18h música de streaming na live)
(padrão neon quente 3:4, área segura: 150 px no topo, 170 px à direita).
Uso: python3 gen_2010.py <pasta project/ de saída>"""
import pathlib
import sys

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

A = "@A@"            # coral (tweak 'accent')
AMBER = "#FFB547"
INK = "#17080D"
MUTED = "#D9B9AC"
SOFT = "#E6CFC6"
FRED = "font-family: 'Fredoka', sans-serif"

DOTS = "radial-gradient(rgba(255,181,71,0.1) 1.5px, transparent 2px) 0 0 / 34px 34px"
LINES = "repeating-linear-gradient(135deg, rgba(255,181,71,0.05) 0 2px, transparent 2px 28px)"
BGS = [
    f"radial-gradient(820px 640px at 86% 18%, rgba(255,107,74,0.34), transparent 70%), radial-gradient(760px 600px at 6% 92%, rgba(255,181,71,0.22), transparent 70%), {DOTS}, {INK}",
    f"radial-gradient(760px 620px at 24% 34%, rgba(255,107,74,0.34), transparent 70%), radial-gradient(700px 560px at 100% 100%, rgba(255,181,71,0.2), transparent 70%), {LINES}, {INK}",
    f"radial-gradient(620px 900px at 4% 55%, rgba(255,181,71,0.22), transparent 70%), radial-gradient(700px 560px at 100% 6%, rgba(255,107,74,0.3), transparent 70%), {DOTS}, {INK}",
    f"radial-gradient(640px 600px at 24% 44%, rgba(255,181,71,0.26), transparent 70%), radial-gradient(700px 560px at 100% 100%, rgba(255,107,74,0.28), transparent 70%), {LINES}, {INK}",
    f"radial-gradient(760px 520px at 70% 30%, rgba(255,181,71,0.28), transparent 70%), radial-gradient(760px 600px at 10% 96%, rgba(255,107,74,0.3), transparent 70%), {DOTS}, {INK}",
    f"radial-gradient(800px 620px at 30% 100%, rgba(255,107,74,0.36), transparent 70%), radial-gradient(700px 560px at 96% 10%, rgba(255,181,71,0.22), transparent 70%), {LINES}, {INK}",
]

ICONS = {
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>',
    "store": '<path d="M3 9l1.5-5h15L21 9"></path><path d="M4 9v11h16V9"></path><path d="M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"></path><path d="M10 20v-6h4v6"></path>',
    "coin": '<circle cx="12" cy="12" r="9"></circle><path d="M15 9.5a3 3 0 0 0-3-1.5c-1.7 0-3 .9-3 2s1.3 2 3 2 3 .9 3 2-1.3 2-3 2a3 3 0 0 1-3-1.5"></path><line x1="12" y1="6" x2="12" y2="18"></line>',
    "music": '<path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle>',
    "trophy": '<path d="M8 21h8"></path><path d="M12 17v4"></path><path d="M7 4h10v5a5 5 0 0 1-10 0V4z"></path><path d="M17 5h3v2a3 3 0 0 1-3 3"></path><path d="M7 5H4v2a3 3 0 0 0 3 3"></path>',
    "pulse": '<path d="M3 12h4l3-8 4 16 3-8h4"></path>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path>',
    "toggle": '<rect x="1" y="6" width="22" height="12" rx="6"></rect><circle cx="16" cy="12" r="3"></circle>',
    "check": '<polyline points="20 6 9 17 4 12"></polyline>',
    "x": '<line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line>',
}


def svg(name, size, stroke, width=1.9, extra=""):
    return (f'<svg {extra}width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def brand(n, total):
    bars = ""
    for i in range(1, total + 1):
        if i == n:
            bars += f'\n      <div style="width: 72px; height: 10px; border-radius: 999px; background: {AMBER}; box-shadow: 0 0 16px rgba(255,181,71,0.7)"></div>'
        else:
            bars += '\n      <div style="width: 28px; height: 10px; border-radius: 999px; background: rgba(255,181,71,0.24)"></div>'
    return f'''  <div style="position: relative; padding: 150px 170px 0 68px">
    <div style="display: flex; align-items: baseline; gap: 14px">
      <span style="{FRED}; font-size: 50px; font-weight: 700; color: {A}; text-shadow: 0 0 24px rgba(255,107,74,0.6)">R&amp;D</span>
      <span style="font-size: 24px; font-weight: 700; color: {MUTED}">Rico e Débora</span>
      <span style="{FRED}; font-size: 24px; font-weight: 600; color: {AMBER}; margin-left: 12px">{n:02d}/{total:02d}</span>
    </div>
    <div style="display: flex; gap: 10px; margin-top: 14px">{bars}
    </div>
  </div>'''


def foot(html, top=0):
    mt = f"margin-top: {top}px; " if top else ""
    return (f'    <div style="{mt}border-top: 2px solid rgba(255,181,71,0.35); padding-top: 16px; font-size: 21px; '
            f'line-height: 1.4; color: {MUTED}">{html}</div>')


def src(text):
    return f'<strong style="color: {AMBER}">Fonte:</strong> {text}'


GROW = '    <div style="flex-grow: 1"></div>'


def pill_solid(text, top=40):
    return (f'    <div style="margin-top: {top}px; align-self: flex-start; {FRED}; font-size: 28px; font-weight: 600; '
            f'letter-spacing: 0.05em; text-transform: uppercase; color: {INK}; background: {AMBER}; border-radius: 999px; '
            f'padding: 10px 26px; box-shadow: 0 0 28px rgba(255,181,71,0.55)">{text}</div>')


def pill_line(text, top=44):
    return (f'    <div style="margin-top: {top}px; align-self: flex-start; {FRED}; font-size: 28px; font-weight: 600; '
            f'letter-spacing: 0.05em; text-transform: uppercase; color: {AMBER}; border: 3px solid {AMBER}; border-radius: 999px; '
            f'padding: 8px 26px; background: rgba(23,8,13,0.6); box-shadow: 0 0 24px rgba(255,181,71,0.4)">{text}</div>')


def stamp(text, top=56):
    return (f'    <div style="margin: {top}px 0 0 10px; align-self: flex-start; transform: rotate(-5deg); border: 5px solid {A}; '
            f'border-radius: 20px; padding: 5px; box-shadow: 0 0 40px rgba(255,107,74,0.5)">\n'
            f'      <div style="border: 3px dashed {A}; border-radius: 13px; padding: 8px 24px; {FRED}; font-size: 40px; '
            f'font-weight: 700; line-height: 1; letter-spacing: 0.04em; text-transform: uppercase; color: {A}">{text}</div>\n'
            f'    </div>')


def h(text, size=64, top=44, lh=1.02):
    return (f'    <h2 style="margin: {top}px 0 0; {FRED}; font-size: {size}px; font-weight: 700; line-height: {lh}; '
            f'text-shadow: 0 0 36px rgba(255,107,74,0.4)">{text}</h2>')


def cta(text, top=0):
    mt = f"margin-top: {top}px; " if top else ""
    return (f'    <div style="{mt}display: flex; align-items: center; justify-content: space-between; border-radius: 24px; '
            f'padding: 22px 30px; background: {A}; color: {INK}; box-shadow: 0 0 40px rgba(255,107,74,0.55)">\n'
            f'      <span style="{FRED}; font-size: 32px; font-weight: 700">{text}</span>\n'
            f'      <span style="{FRED}; font-size: 40px; font-weight: 700">»</span>\n'
            f'    </div>')


def tile(icon, color, glow, rot, size=124, isize=62):
    rad = round(size * 0.31)
    return (f'<div style="flex: none; width: {size}px; height: {size}px; border-radius: {rad}px; display: flex; align-items: center; '
            f'justify-content: center; transform: rotate({rot}deg); background: linear-gradient(150deg, rgba(255,255,255,0.3), '
            f'rgba({glow},0.35) 45%, rgba(23,8,13,0.7)); border: 3px solid {color}; box-shadow: 0 0 44px rgba({glow},0.55), '
            f'inset 0 0 26px rgba(255,181,71,0.3)">{svg(icon, isize, "#FFF1E6")}</div>')


def icon_row(icon, title, text, coral, rot, indent):
    color = A if coral else AMBER
    glow = "255,107,74" if coral else "255,181,71"
    side = "margin-right: 70px" if indent == "l" else "margin-left: 70px"
    return (f'      <div style="display: flex; align-items: center; gap: 26px; {side}">\n'
            f'        {tile(icon, color, glow, rot)}\n'
            f'        <div>\n'
            f'          <div style="{FRED}; font-size: 40px; font-weight: 700; line-height: 1.1; color: {color}">{title}</div>\n'
            f'          <div style="margin-top: 4px; font-size: 28px; line-height: 1.3">{text}</div>\n'
            f'        </div>\n'
            f'      </div>')


def mark_row(ok, html, size=30):
    if ok:
        style = f"border: 3px solid {AMBER}; box-shadow: 0 0 24px rgba(255,181,71,0.3)"
        icon = svg("check", 40, AMBER, 3, 'style="flex: none" ')
    else:
        style = f"border: 3px dashed {A}"
        icon = svg("x", 40, "#FF6B4A", 3, 'style="flex: none" ')
    return (f'      <div style="display: flex; align-items: center; gap: 18px; {style}; border-radius: 26px; padding: 16px 22px; '
            f'background: rgba(23,8,13,0.62)">\n        {icon}\n'
            f'        <div style="font-size: {size}px; line-height: 1.3">{html}</div>\n      </div>')


def box_dashed(html, top=30, size=30):
    return (f'    <div style="margin-top: {top}px; border: 3px dashed rgba(255,181,71,0.8); border-radius: 30px; padding: 20px 28px; '
            f'background: rgba(23,8,13,0.6)">\n      <div style="font-size: {size}px; line-height: 1.32">{html}</div>\n    </div>')


def box_glow(html, top=26, size=30):
    return (f'    <div style="margin-top: {top}px; border: 3px solid {A}; border-radius: 30px; padding: 20px 28px; '
            f'background: rgba(23,8,13,0.62); box-shadow: 0 0 34px rgba(255,107,74,0.4), inset 0 0 22px rgba(255,107,74,0.14)">\n'
            f'      <div style="font-size: {size}px; font-weight: 800; line-height: 1.3">{html}</div>\n    </div>')


def ask(question, action):
    return (f'    <div style="border: 3px solid {A}; border-radius: 30px; padding: 22px 30px; background: rgba(23,8,13,0.66); '
            f'box-shadow: 0 0 40px rgba(255,107,74,0.45), inset 0 0 24px rgba(255,107,74,0.15)">\n'
            f'      <div style="{FRED}; font-size: 40px; font-weight: 700; line-height: 1.1">{question}</div>\n'
            f'      <div style="margin-top: 8px; font-size: 26px; font-weight: 800; color: {AMBER}">{action}</div>\n'
            f'    </div>')


def amber(t):
    return f'<span style="color: {AMBER}">{t}</span>'


def coral(t):
    return f'<span style="color: {A}">{t}</span>'


def b(t):
    return f'<strong style="{FRED}; font-weight: 700; color: {AMBER}">{t}</strong>'


def card(title, n, total, bg, body):
    inner = "\n".join(body)
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title} — {n}/{total}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&amp;family=Nunito:wght@400;700;800&amp;display=swap">
<style>
body {{ margin: 0; font-family: "Nunito", "Helvetica Neue", sans-serif; }}
</style>
</helmet>
<div style="position: relative; overflow: hidden; width: 1080px; height: 1440px; box-sizing: border-box; color: #FFF3EC; display: flex; flex-direction: column; background: {BGS[bg]}">

{brand(n, total)}

  <div style="position: relative; padding: 0 170px 56px 68px; display: flex; flex-direction: column; flex-grow: 1">
{inner}
  </div>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"accent":{{"editor":"color","default":"#FF6B4A","options":["#FF6B4A","#FFB547","#FF4F7B","#FFF3EC"]}},"$preview":{{"width":1080,"height":1440}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{ accent: this.props.accent ?? '#FF6B4A' }};
  }}
}}
</script>
</body>
</html>
'''
    return html.replace(A, "{{accent}}")


def step_badge(n, top=44):
    return (f'    <div style="margin-top: {top}px; align-self: flex-start; display: flex; align-items: center; gap: 14px; {FRED}; '
            f'font-size: 28px; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; color: {AMBER}; '
            f'border: 3px solid {AMBER}; border-radius: 999px; padding: 6px 26px 6px 8px; background: rgba(23,8,13,0.6); '
            f'box-shadow: 0 0 24px rgba(255,181,71,0.4)">'
            f'<span style="display: flex; align-items: center; justify-content: center; width: 46px; height: 46px; border-radius: 50%; '
            f'background: {AMBER}; color: {INK}; font-size: 30px; font-weight: 700">{n}</span>Passo {n} de 4</div>')


def dot(n, label, on):
    if on:
        circle = (f'background: {A}; border: 3px solid {A}; color: {INK}; box-shadow: 0 0 30px rgba(255,107,74,0.6)')
    else:
        circle = f'border: 3px solid {AMBER}; color: {AMBER}; background: rgba(23,8,13,0.7)'
    return (f'        <div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 14px">\n'
            f'          <div style="width: 104px; height: 104px; border-radius: 50%; display: flex; align-items: center; justify-content: center; '
            f'{FRED}; font-size: 56px; font-weight: 700; {circle}">{n}</div>\n'
            f'          <div style="{FRED}; font-size: 30px; font-weight: 600; line-height: 1.1; text-align: center">{label}</div>\n'
            f'        </div>')


def path_step(n, label, last=False):
    fill = (f'background: {A}; border: 3px solid {A}; color: {INK}; box-shadow: 0 0 24px rgba(255,107,74,0.6)' if last
            else f'border: 3px solid {A}; color: {A}')
    border = f'border: 3px solid {AMBER}; box-shadow: 0 0 24px rgba(255,181,71,0.35)' if last else 'border: 3px solid rgba(255,243,236,0.28)'
    return (f'      <div style="display: flex; align-items: center; gap: 20px; {border}; border-radius: 24px; padding: 14px 22px; background: rgba(23,8,13,0.62)">\n'
            f'        <div style="flex: none; width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; '
            f'{FRED}; font-size: 30px; font-weight: 700; {fill}">{n}</div>\n'
            f'        <div style="font-size: 31px; line-height: 1.25">{label}</div>\n'
            f'      </div>')


def doc(label, sub):
    return (f'      <div style="box-sizing: border-box; width: calc(50% - 9px); border: 3px solid rgba(255,181,71,0.75); border-radius: 26px; '
            f'padding: 18px 22px; background: rgba(23,8,13,0.62)">\n'
            f'        <div style="{FRED}; font-size: 36px; font-weight: 700; line-height: 1.1; color: {AMBER}">{label}</div>\n'
            f'        <div style="margin-top: 4px; font-size: 24px; line-height: 1.3; color: {SOFT}">{sub}</div>\n'
            f'      </div>')



ICONS.update({
    "at": '<circle cx="12" cy="12" r="4"></circle><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-3.92 7.94"></path>',
    "edit": '<path d="M12 20h9"></path><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4z"></path>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>',
    "pin": '<line x1="12" y1="17" x2="12" y2="22"></line><path d="M5 17h14v-1.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a2 2 0 0 0 0-4H8a2 2 0 0 0 0 4h1v4.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24z"></path>',
    "layers": '<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>',
    "list": '<line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><circle cx="4" cy="6" r="1"></circle><circle cx="4" cy="12" r="1"></circle><circle cx="4" cy="18" r="1"></circle>',
    "eyeoff": '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94"></path><path d="M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19"></path><line x1="1" y1="1" x2="23" y2="23"></line>',
    "chart": '<line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><polyline points="9 12 11 14 15 10"></polyline>',
})

ACADEMIA = "Academia de Criadores do TikTok (artigos de jun a set/2026)."
HOJE = "13/10/2026"


def irow(icon, title, text, coral, rot, indent):
    color = A if coral else AMBER
    glow = "255,107,74" if coral else "255,181,71"
    side = "margin-right: 40px" if indent == "l" else "margin-left: 70px"
    return (f'      <div style="display: flex; align-items: center; gap: 30px; {side}">\n'
            f'        {tile(icon, color, glow, rot, 150, 76)}\n'
            f'        <div>\n'
            f'          <div style="{FRED}; font-size: 46px; font-weight: 700; line-height: 1.1; color: {color}">{title}</div>\n'
            f'          <div style="margin-top: 6px; font-size: 32px; line-height: 1.3">{text}</div>\n'
            f'        </div>\n'
            f'      </div>')


def pstep(n, label, last=False):
    return path_step(n, label, last).replace('font-size: 31px', 'font-size: 36px').replace('padding: 14px 22px', 'padding: 22px 26px')


def big_num(num, label, sub, size=200):
    return (f'      <div style="flex: 1 1 0; border: 3px solid rgba(255,181,71,0.75); border-radius: 32px; padding: 24px 26px; background: rgba(23,8,13,0.62)">\n'
            f'        <div style="{FRED}; font-size: {size}px; font-weight: 700; line-height: 0.9; color: {AMBER}; text-shadow: 0 0 50px rgba(255,107,74,0.75), 0 0 120px rgba(255,107,74,0.4)">{num}</div>\n'
            f'        <div style="margin-top: 12px; {FRED}; font-size: 44px; font-weight: 700; line-height: 1.08">{label}</div>\n'
            f'        <div style="margin-top: 6px; font-size: 30px; line-height: 1.3; color: {SOFT}">{sub}</div>\n'
            f'      </div>')


def trio(items):
    out = '    <div style="margin-top: 80px; display: flex; gap: 22px">\n'
    for i, (icon, label) in enumerate(items):
        coral_side = i % 2 == 1
        color = A if coral_side else AMBER
        glow = "255,107,74" if coral_side else "255,181,71"
        out += (f'      <div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 16px">\n'
                f'        {tile(icon, color, glow, (-5, 4, -3)[i], 180, 90)}\n'
                f'        <div style="{FRED}; font-size: 48px; font-weight: 700; color: {color}">{label}</div>\n'
                f'      </div>\n')
    return out + '    </div>'


ICONS.update({
    "search": '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>',
    "video": '<polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>',
    "mic": '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line>',
    "type": '<polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line>',
    "hash": '<line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line>',
    "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>',
    "refresh": '<polyline points="23 4 23 10 17 10"></polyline><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>',
    "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>',
    "target": '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
    "cc": '<rect x="2" y="5" width="20" height="14" rx="3"></rect><path d="M10 10.5a2 2 0 1 0 0 3"></path><path d="M17 10.5a2 2 0 1 0 0 3"></path>',
})

NEWS = "TikTok Newsroom, “Creator Search Insights” (13/03/2024)."
ACAD_SET = "Academia de Criadores do TikTok (jun a set/2026)"


def searchbar(text, top=60):
    return (f'    <div style="margin-top: {top}px; display: flex; align-items: center; gap: 22px; border: 4px solid {AMBER}; border-radius: 999px; '
            f'padding: 22px 34px; background: rgba(23,8,13,0.72); box-shadow: 0 0 40px rgba(255,181,71,0.45)">\n'
            f'      {svg("search", 56, AMBER, 2.6, "style=\"flex: none\" ")}\n'
            f'      <div style="{FRED}; font-size: 38px; font-weight: 600; line-height: 1.12">{text}<span style="color: {A}">|</span></div>\n'
            f'    </div>')


def gap_side(icon, big, label, coral_side):
    color = A if coral_side else AMBER
    glow = "255,107,74" if coral_side else "255,181,71"
    return (f'      <div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 18px; border: 3px solid {color}; '
            f'border-radius: 32px; padding: 30px 20px; background: rgba(23,8,13,0.62); box-shadow: 0 0 30px rgba({glow},0.3)">\n'
            f'        {tile(icon, color, glow, -4 if coral_side else 5, 140, 70)}\n'
            f'        <div style="{FRED}; font-size: 64px; font-weight: 700; line-height: 1; color: {color}">{big}</div>\n'
            f'        <div style="font-size: 30px; line-height: 1.25; text-align: center">{label}</div>\n'
            f'      </div>')


ICONS.update({
    "eye": '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>',
    "tag": '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line>',
    "clock": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
})

HOJE = "14/10/2026"
ACADEMIA = "Academia de Criadores do TikTok (artigos de jun a set/2026)."
NEWS_IA = "TikTok Newsroom (19/09/2023 e 19/11/2025)"


def lead(text, top=24, size=33):
    return f'    <div style="margin-top: {top}px; font-size: {size}px; line-height: 1.34; color: {SOFT}">{text}</div>'


def h1(html, size=96):
    return (f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: {size}px; font-weight: 700; line-height: 1; '
            f'text-shadow: 0 0 36px rgba(255,107,74,0.4)">{html}</h1>')


def small_trio(items, top=50):
    return (trio(items).replace("margin-top: 80px", f"margin-top: {top}px").replace("font-size: 48px", "font-size: 38px")
            .replace("width: 180px; height: 180px", "width: 132px; height: 132px").replace('width="90" height="90"', 'width="66" height="66"'))


def group_label(text, color, top=34):
    return (f'    <div style="margin-top: {top}px; {FRED}; font-size: 34px; font-weight: 700; letter-spacing: 0.04em; '
            f'text-transform: uppercase; color: {color}">{text}</div>')



ICONS.update({
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line>',
    "radio": '<circle cx="12" cy="12" r="2"></circle><path d="M16.24 7.76a6 6 0 0 1 0 8.49"></path><path d="M7.76 16.24a6 6 0 0 1 0-8.49"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path><path d="M4.93 19.07a10 10 0 0 1 0-14.14"></path>',
})

HOJE = "19/10/2026"
CRIADORES = "Academia de Criadores do TikTok (jun a set/2026)"
SHOP = "Academia do TikTok Shop"


def dots3(items, top=60):
    out = f'    <div style="margin-top: {top}px; display: flex; gap: 14px">\n'
    for i, label in enumerate(items, 1):
        out += dot(i, label, i == len(items)) + "\n"
    return out + '    </div>'


# ---------------------------------------------------------------- 6h: live que vende sem janelinha
T6 = "Live que vende sem janelinha"
L_CARDS = [
    card(T6, 1, 6, 0, [
        pill_solid("TikTok Shop do zero"),
        h1(f'Live que vende {coral("sem janelinha")}'),
        lead("Dá pra crescer e vender na live sem “sigo de volta”? Dá. A Academia do TikTok mostra o caminho."),
        trio([("calendar", "Antes"), ("mic", "Durante"), ("clock", "Duração")]).replace("margin-top: 80px", "margin-top: 110px"),
        GROW,
        cta("Arrasta que eu te mostro"),
        foot(f'Checado na <strong style="color: {AMBER}">Academia de Criadores</strong> e na <strong style="color: {AMBER}">Academia do TikTok Shop</strong> em {HOJE}.', 22),
    ]),
    card(T6, 2, 6, 1, [
        stamp("Isso não", 44),
        h(f'O que {coral("derruba")} a live de venda', 70, 40, 1.02),
        '    <div style="margin-top: 44px; display: flex; flex-direction: column; gap: 16px">',
        mark_row(False, "Troca de follow e curtida, o <strong>“sigo de volta”</strong>", 33),
        mark_row(False, "Sorteio fora da ferramenta oficial <strong>Live Giveaway</strong>", 33),
        mark_row(False, "<strong>“Link na bio”</strong>, WhatsApp ou outra rede", 33),
        mark_row(False, "<strong>Voz de IA</strong> ou áudio gravado", 33),
        '    </div>',
        box_glow(f'Pedir pra seguir {amber("pode")}: com um motivo claro, sem troca.', 36, 34),
        GROW,
        foot(src(f"{CRIADORES} (engajamento falso) · {SHOP}: Fraude (18/06/2026), Jogos de azar (28/07/2026), Redirecionamento e Alta qualidade (13/03/2026).")),
    ]),
    card(T6, 3, 6, 2, [
        pill_line("Antes de entrar ao vivo"),
        h(f'Chegue com {amber("plateia marcada")}', 72, 28, 1.02),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 18px">',
        pstep(1, f'Publique {b("um vídeo")} antes da live'),
        pstep(2, f'Crie um {b("Evento de LIVE")}'),
        pstep(3, f'{b("Programação fixa")} na bio'),
        pstep(4, f'Adesivo de {b("contagem regressiva")}', True),
        '    </div>',
        box_dashed(f'{b("Por que o Evento:")} quem cria tem mais espectadores, em média, segundo a Academia.', 40, 33),
        GROW,
        foot(src(CRIADORES + ".")),
    ]),
    card(T6, 4, 6, 3, [
        pill_line("Durante a live"),
        h(f'Segure quem {coral("acabou de chegar")}', 70, 28, 1.02),
        '    <div style="margin-top: 60px; display: flex; flex-direction: column; gap: 48px">',
        irow("clock", "5 segundos", "pra dizer o tema da live a quem entrou agora.", True, -6, "l"),
        irow("users", "Pelo nome", "Cumprimente quem entra e lance a pergunta do dia.", False, 5, "r"),
        irow("bag", "Produto na mão", "O produto fixado aparece e é usado na câmera.", True, -4, "l"),
        '    </div>',
        GROW,
        foot(src(f"{CRIADORES} · {SHOP}: Produto inconsistente (28/09/2026) e Erros comuns em LIVEs (12/11/2025).")),
    ]),
    card(T6, 5, 6, 4, [
        pill_line("Quanto tempo ficar"),
        h(f'Live curta {amber("rende menos")}', 74, 28, 1.02),
        '    <div style="margin-top: 50px; display: flex; gap: 20px">',
        big_num("60+", "minutos", "lives de 60 a 80 min tendem a ter mais views que as de 10 a 20", 170),
        big_num("25", "minutos", "ou mais fazem um dia de LIVE valer nas missões", 170),
        '    </div>',
        box_dashed(f'{b("Em campanha:")} a Academia do TikTok Shop recomenda live de pelo menos 2 horas.', 36, 33),
        box_glow(f'Métrica de base: {amber("média de espectadores simultâneos")}.', 22, 33),
        GROW,
        foot(src(f"{CRIADORES} · {SHOP}: Campanhas (16/01/2026).")),
    ]),
    card(T6, 6, 6, 5, [
        stamp("Resumo"),
        h(f'Live que vende {amber("sem atalho")}', 70, 30, 1.02),
        '    <div style="margin-top: 40px; display: flex; flex-direction: column; gap: 16px">',
        pstep(1, f'Sem troca: {b("motivo real")} pra seguir'),
        pstep(2, f'{b("Evento de LIVE")} + vídeo antes'),
        pstep(3, f'Produto fixado {b("na câmera")}'),
        pstep(4, f'{b("60 minutos")} ou mais', True),
        '    </div>',
        GROW,
        '    <div style="height: 20px"></div>',
        ask("Você já fez live de venda?", "Comenta: já fiz, quero fazer ou tenho medo."),
        foot(src(f"{CRIADORES} e {SHOP} · checado em {HOJE}."), 22),
    ]),
]

# ---------------------------------------------------------------- 18h: música de streaming na live
T18 = "Música de streaming na live"
M_CARDS = [
    card(T18, 1, 6, 2, [
        pill_solid("Isso derruba sua conta?"),
        h1(f'Música de streaming {coral("na live")}'),
        lead("Aquela playlist tocando no fundo enquanto você vende. Pode? Derruba?"),
        trio([("music", "Playlist"), ("radio", "Live"), ("bag", "Venda")]).replace("margin-top: 80px", "margin-top: 110px"),
        GROW,
        cta("Arrasta que eu te mostro"),
        foot(f'Checado nos <strong style="color: {AMBER}">Termos de Música do TikTok</strong> e na <strong style="color: {AMBER}">Academia do TikTok Shop</strong> em {HOJE}.', 22),
    ]),
    card(T18, 2, 6, 0, [
        stamp("Meia-verdade", 44),
        h(f'Os sons do app {amber("não valem")} pra live', 70, 40, 1.02),
        box_glow(f'A biblioteca de sons do app, inclusive a comercial, não cobre transmissão ao vivo. Música gravada na live só {amber("com os direitos dela")}.', 50, 34),
        box_dashed(f'{b("Não é regra nova:")} está nos Termos de Música do TikTok desde 2023.', 30, 34),
        box_dashed(f'{b("Na prática:")} se você não tem os direitos da música, ela não deveria tocar na sua live.', 22, 34),
        GROW,
        foot(src("Termos de Música do TikTok, transmissões ao vivo (tiktok.com/legal), conferidos em 26/09/2026.")),
    ]),
    card(T18, 3, 6, 1, [
        pill_line("Live de venda é mais rígida"),
        h(f'No TikTok Shop, {coral("áudio gravado")} não entra', 66, 28, 1.04),
        '    <div style="margin-top: 44px; display: flex; flex-direction: column; gap: 16px">',
        mark_row(False, "<strong>Áudio gravado</strong> na live", 34),
        mark_row(False, "<strong>Voz de IA</strong>", 34),
        mark_row(False, "Imagem parada cobrindo <strong>mais da metade</strong> da tela", 34),
        mark_row(False, "<strong>Print</strong> da página do produto", 34),
        '    </div>',
        box_glow(f'{amber("Na prática:")} playlist tocando é áudio gravado. Quem fala é você.', 36, 34),
        GROW,
        foot(src(f"{SHOP}: Imagens estáticas (30/09/2026) e Alta qualidade (13/03/2026).")),
    ]),
    card(T18, 4, 6, 3, [
        pill_line("Se a regra for quebrada"),
        h(f'A live tem {coral("escada de avisos")}', 70, 28, 1.02),
        dots3(["Lembrete", "Aviso", "Live encerrada"], 120),
        box_glow(f'No {amber("nível 2")}, o TikTok pode tirar o produto da live e dar ponto de violação.', 120, 37),
        box_dashed(f'{b("Nível 3:")} a live é encerrada. Produto proibido encerra direto, sem escada.', 34, 36),
        GROW,
        foot(src(f"{SHOP}: Avisos em LIVE (11/03/2026).")),
    ]),
    card(T18, 5, 6, 4, [
        pill_line("E os pontos somam"),
        h(f'Ponto vira {amber("conta em risco")}', 72, 28, 1.02),
        '    <div style="margin-top: 80px; display: flex; gap: 20px">',
        big_num("24", "pontos", "de violação = perda garantida do TikTok Shop", 190),
        big_num("90", "dias", "pra cada ponto zerar depois de emitido", 190),
        '    </div>',
        box_glow(f'O ponto do aviso de {amber("nível 2")} entra nessa conta.', 70, 36),
        box_dashed(f'{b("Repetir a mesma regra")} pode tirar o e-commerce mesmo com a nota de integridade em dia.', 34, 36),
        GROW,
        foot(src(f"{SHOP}: Avaliação de desempenho (15/06/2026).")),
    ]),
    card(T18, 6, 6, 5, [
        stamp("Resumo"),
        h(f'Então, {amber("derruba?")}', 70, 30, 1.02),
        box_glow(f'Uma música não apaga a conta, mas pode {amber("encerrar a live")} e somar pontos.', 34, 33),
        '    <div style="margin-top: 30px; display: flex; flex-direction: column; gap: 16px">',
        pstep(1, f'Tire a {b("playlist")} do fundo'),
        pstep(2, f'Só música que você {b("tem direito")} de usar'),
        pstep(3, f'Na venda, {b("sua voz")} é o áudio', True),
        '    </div>',
        GROW,
        '    <div style="height: 20px"></div>',
        ask("Você deixa música de fundo na live?", "Comenta: sempre, às vezes ou nunca."),
        foot(src(f"Termos de Música do TikTok e {SHOP} · checado em {HOJE}."), 22),
    ]),
]

for i, html in enumerate(L_CARDS, 1):
    (OUT / f"LiveSemJanelinha_{i}.dc.html").write_text(html, encoding="utf-8")
for i, html in enumerate(M_CARDS, 1):
    (OUT / f"MusicaNaLive_{i}.dc.html").write_text(html, encoding="utf-8")
print(len(L_CARDS), "cards LiveSemJanelinha;", len(M_CARDS), "cards MusicaNaLive")
