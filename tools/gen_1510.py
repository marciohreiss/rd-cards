"""Gera os artboards .dc.html dos dois carrosséis da R&D de 15/10/2026 (6h persona de IA sem rótulo, 18h 3 formatos que vendem)
(padrão neon quente 3:4, área segura: 150 px no topo, 170 px à direita).
Uso: python3 gen_1510.py <pasta project/ de saída>"""
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


# ---------------------------------------------------------------- 6h: persona de IA sem rótulo
T6 = "Persona de IA sem rótulo"
P_CARDS = [
    card(T6, 1, 6, 0, [
        pill_solid("Isso derruba sua conta?"),
        h1(f'Persona de IA {coral("sem rótulo")}'),
        lead("Avatar realista, voz feita por IA, cena que parece de verdade. O que o TikTok exige antes de você postar?"),
        trio([("user", "Avatar"), ("mic", "Voz"), ("video", "Cena")]).replace("margin-top: 80px", "margin-top: 110px"),
        GROW,
        cta("Arrasta que eu te mostro"),
        foot(f'Checado na <strong style="color: {AMBER}">Academia de Criadores do TikTok</strong> e no TikTok Newsroom em {HOJE}.', 22),
    ]),
    card(T6, 2, 6, 1, [
        stamp("É regra", 44),
        h(f'Parece real e foi feito por IA? {amber("Leva rótulo.")}', 70, 40, 1.02),
        box_glow(f'Pessoa ou cena {amber("realista")}, gerada ou {amber("muito editada")} por IA, precisa do rótulo de conteúdo gerado por IA.', 50, 36),
        box_dashed(f'{b("Vale pra persona:")} se o seu “criador” na tela é um avatar realista feito por IA, o rótulo vai em todo vídeo com ele.', 30, 34),
        box_dashed(f'{b("Imagem, áudio ou vídeo:")} a regra do TikTok cobre os três quando são realistas.', 22, 34),
        GROW,
        foot(src(f"{ACADEMIA} · {NEWS_IA}.")),
    ]),
    card(T6, 3, 6, 2, [
        pill_line("Precisa ou não precisa?"),
        h(f'O rótulo é pro que {coral("parece real")}', 70, 28, 1.02),
        group_label("Precisa", AMBER, 60),
        '    <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 16px">',
        mark_row(True, "Pessoa <strong>realista</strong> gerada por IA", 38),
        mark_row(True, "Cena <strong>realista</strong> gerada por IA", 38),
        mark_row(True, "Vídeo <strong>muito editado</strong> por IA", 38),
        '    </div>',
        group_label("Não precisa", A, 60),
        '    <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 16px">',
        mark_row(False, "Narração <strong>TTS genérica</strong>", 38),
        mark_row(False, "Estilo <strong>anime</strong>", 38),
        '    </div>',
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T6, 4, 6, 3, [
        pill_line("O TikTok também confere"),
        h(f'Tem rótulo {amber("automático")}', 76, 28, 1),
        '    <div style="margin-top: 80px; display: flex; flex-direction: column; gap: 64px">',
        irow("layers", "Credenciais de Conteúdo", "Metadado C2PA que vem gravado no arquivo e ajuda o TikTok a identificar IA.", True, -6, "l"),
        irow("tag", "1,3 bilhão", "de vídeos já rotulados assim, segundo o TikTok em nov/2025.", False, 5, "r"),
        '    </div>',
        box_dashed(f'{b("Não conte só com isso:")} o TikTok avisa que o rótulo pode se perder quando o vídeo é editado ou reenviado de outro lugar. Marque você.', 80, 34),
        GROW,
        foot(src("TikTok Newsroom (19/11/2025).")),
    ]),
    card(T6, 5, 6, 4, [
        pill_line("O que pouca gente sabe"),
        h(f'O rótulo {coral("não te pune")}', 76, 28, 1),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 18px">',
        mark_row(True, "Rótulo de IA <strong>não reduz o alcance</strong>", 34),
        mark_row(False, "Pôr ou tirar o rótulo <strong>depois de publicar</strong>: não dá", 34),
        mark_row(False, "Vídeo com IA em <strong>concurso de publicação</strong>: não entra", 34),
        '    </div>',
        box_glow(f'Decida {amber("antes")} de apertar Publicar.', 50, 36),
        box_dashed(f'{b("Vídeo sem views?")} Não quer dizer bloqueado. Se ele for inelegível, aparece um aviso em Análises → Desempenho.', 30, 33),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T6, 6, 6, 5, [
        stamp("Resumo"),
        h(f'Então, {amber("derruba?")}', 70, 30, 1.02),
        box_glow(f'Na prática: postar IA realista sem rótulo é {amber("descumprir a regra")}, e cada violação gera um aviso.', 34, 33),
        '    <div style="margin-top: 30px; display: flex; flex-direction: column; gap: 16px">',
        pstep(1, f'Avatar ou cena realista? {b("Ligue o rótulo")}'),
        pstep(2, f'O rótulo {b("não reduz")} alcance'),
        pstep(3, f'Avisos {b("expiram em 90 dias")}', True),
        '    </div>',
        GROW,
        '    <div style="height: 20px"></div>',
        ask("Você já usa avatar de IA?", "Comenta: sim, não ou pensando nisso."),
        foot(src(f"Academia de Criadores do TikTok (jun a set/2026) e {NEWS_IA} · checado em {HOJE}."), 22),
    ]),
]

# ---------------------------------------------------------------- 18h: 3 formatos que vendem
T18 = "3 formatos de vídeo que vendem"


def fmt_pill(n, top=44):
    return step_badge(n, top).replace(f"Passo {n} de 4", f"Formato {n} de 3")


F_CARDS = [
    card(T18, 1, 6, 2, [
        pill_solid("TikTok Shop do zero"),
        h1(f'3 formatos de vídeo {coral("que vendem")}'),
        lead("Os formatos de conteúdo de marca que a Academia de Criadores do TikTok aponta como os que performam."),
        trio([("mic", "Sensorial"), ("refresh", "Reviravolta"), ("eye", "POV")]).replace("margin-top: 80px", "margin-top: 110px").replace("font-size: 48px", "font-size: 44px"),
        GROW,
        cta("Arrasta e escolhe o seu"),
        foot(f'Checado na <strong style="color: {AMBER}">Academia de Criadores do TikTok</strong> em {HOJE}.', 22),
    ]),
    card(T18, 2, 6, 0, [
        pill_line("Vale pros três"),
        h(f'Produto na tela {amber("logo de cara")}', 70, 28, 1.02),
        '    <div style="margin-top: 50px; display: flex; gap: 20px">',
        big_num("3s", "primeiros", "é onde o produto já precisa aparecer", 190),
        big_num("0:02", "termômetro", "retenção caindo aqui = gancho fraco", 150),
        '    </div>',
        box_glow(f'{amber("Tempo assistido")} é o sinal mais forte da recomendação.', 44, 34),
        box_dashed(f'{b("Nos três formatos:")} uma mensagem por vídeo, e algo muda na tela a cada poucos segundos.', 26, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 3, 6, 1, [
        fmt_pill(1),
        h(f'{coral("Sensorial")}', 96, 30, 1),
        lead("O som e a textura do produto em uso seguram o olho.", 16, 35),
        '    <div style="margin-top: 80px; display: flex; flex-direction: column; gap: 64px">',
        irow("mic", "Som de perto", "Abrir, apertar, aplicar: o barulho do produto.", True, -6, "l"),
        irow("eye", "Close na textura", "Espuma, brilho, tecido: mostre de pertinho.", False, 5, "r"),
        '    </div>',
        box_dashed(f'{b("Exemplos da Academia:")} ASMR e limpeza.', 80, 36),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 4, 6, 3, [
        fmt_pill(2),
        h(f'{amber("Reviravolta")}', 96, 30, 1),
        lead("Antes e depois: a transformação segura até o fim.", 16, 35),
        '    <div style="margin-top: 46px; display: flex; gap: 22px">',
        gap_side("clock", "Antes", "o problema, sem o produto", False),
        gap_side("check", "Depois", "o resultado, com o produto", True),
        '    </div>',
        box_dashed(f'{b("Gancho pronto:")} mostrar o resultado antes é um dos ganchos que a Academia recomenda.', 40, 33),
        box_glow(f'Mostre só o resultado que o {amber("anúncio e a embalagem")} sustentam.', 22, 33),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 5, 6, 4, [
        fmt_pill(3),
        h(f'{coral("Ponto de vista")}', 92, 30, 1),
        lead("POV: quem assiste se vê usando o produto.", 16, 35),
        '    <div style="margin-top: 80px; display: flex; flex-direction: column; gap: 64px">',
        irow("user", "Você na cena", "A câmera mostra o que a pessoa veria.", True, -6, "l"),
        irow("book", "Mini-história", "Motivação → obstáculo → desfecho.", False, 5, "r"),
        '    </div>',
        box_dashed(f'{b("Também na lista da Academia:")} entrevista ou podcast e narrativa.', 80, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 6, 6, 5, [
        stamp("Resumo"),
        h(f'Escolha 1 e {amber("teste por semanas")}', 66, 30, 1.04),
        '    <div style="margin-top: 36px; display: flex; flex-direction: column; gap: 16px">',
        pstep(1, f'Produto {b("nos 3 primeiros segundos")}'),
        pstep(2, f'{b("Um formato")} por vídeo'),
        pstep(3, f'Vídeo com link: {b("Divulgar conteúdo comercial")}', True),
        '    </div>',
        box_dashed(f'{b("Regra da Academia:")} não tire conclusão de um vídeo só. Compare com as suas últimas publicações.', 30, 31),
        GROW,
        '    <div style="height: 20px"></div>',
        ask("Qual você testa primeiro?", "Comenta: sensorial, reviravolta ou POV."),
        foot(src(f"Academia de Criadores do TikTok (jun a set/2026) · checado em {HOJE}."), 22),
    ]),
]

for i, html in enumerate(P_CARDS, 1):
    (OUT / f"PersonaIA_{i}.dc.html").write_text(html, encoding="utf-8")
for i, html in enumerate(F_CARDS, 1):
    (OUT / f"Formatos_{i}.dc.html").write_text(html, encoding="utf-8")
print(len(P_CARDS), "cards PersonaIA;", len(F_CARDS), "cards Formatos")
