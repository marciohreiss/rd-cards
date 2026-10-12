"""Gera os artboards .dc.html dos dois carrosséis da R&D de 13/10/2026 (6h e 18h)
(padrão neon quente 3:4, área segura: 150 px no topo, 170 px à direita).
Uso: python3 gen_1310_rotina.py <pasta project/ de saída>"""
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
HOJE = "12/10/2026"


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


# ---------------------------------------------------------------- 6h: perfil que vende
T6 = "Perfil que vende"
P_CARDS = [
    card(T6, 1, 6, 0, [
        pill_solid("TikTok Shop do zero"),
        f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: 100px; font-weight: 700; line-height: 1; text-shadow: 0 0 36px rgba(255,107,74,0.4)">Seu perfil {coral("vende ou espanta?")}</h1>',
        f'    <div style="margin-top: 24px; font-size: 33px; line-height: 1.34; color: {SOFT}">Nome, bio e link: o que a Academia de Criadores manda arrumar antes do primeiro achado.</div>',
        trio([("at", "Nome"), ("edit", "Bio"), ("link", "Link")]),
        GROW,
        cta("Arrasta e arruma o seu"),
        foot(f'Checado na <strong style="color: {AMBER}">Academia de Criadores do TikTok</strong> em {HOJE}.', 22),
    ]),
    card(T6, 2, 6, 1, [
        pill_line("1 · Nome"),
        h(f'Coloque o {amber("nicho")} no seu @', 70, 28, 1),
        f'    <div style="margin-top: 18px; font-size: 35px; line-height: 1.32; color: {SOFT}">Nome de usuário com palavra-chave do nicho ajuda a ser achado na busca.</div>',
        '    <div style="margin-top: 50px; display: flex; gap: 20px">',
        big_num("7", "dias", "pra trocar de novo o nome de exibição"),
        big_num("30", "dias", "pra trocar de novo o @"),
        '    </div>',
        box_glow(f'Escolha com calma: {amber("errou o @, só muda de novo em 30 dias.")}', 44, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T6, 3, 6, 2, [
        pill_line("2 · Bio"),
        '    <div style="margin-top: 26px; display: flex; align-items: flex-end; gap: 22px">',
        f'      <div style="flex: none; {FRED}; font-size: 230px; font-weight: 700; line-height: 0.86; color: {AMBER}; text-shadow: 0 0 50px rgba(255,107,74,0.75), 0 0 120px rgba(255,107,74,0.4)">160</div>',
        f'      <div style="padding-bottom: 10px; {FRED}; font-size: 46px; font-weight: 700; line-height: 1.06">caracteres pra dizer o quê e pra quem</div>',
        '    </div>',
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 20px">',
        mark_row(False, "“Posto coisas legais”", 34),
        mark_row(True, "“Ensino a vender como afiliado no TikTok Shop, do zero”", 34),
        '    </div>',
        box_dashed(f'{b("Cuidado:")} contato comercial na bio pode deixar a conta inelegível ao Programa de Recompensas.', 46, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T6, 4, 6, 3, [
        pill_line("3 · Link"),
        h(f'O link de site {coral("não libera pra todo mundo")}', 66, 28, 1.02),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 44px">',
        irow("user", "Conta pessoal", "Libera a partir de 1 mil seguidores.", False, -6, "l"),
        irow("store", "Conta comercial", "Libera sem esperar os 1 mil.", True, 5, "r"),
        irow("link", "Sem link ainda?", "Capriche no nome e na bio enquanto cresce.", False, -4, "l"),
        '    </div>',
        box_dashed(f'{b("Antes de trocar pra comercial:")} só a conta pessoal entra no Programa de Recompensas.', 54, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T6, 5, 6, 4, [
        pill_line("4 · Topo do perfil"),
        h(f'Quem chega precisa {amber("entender em 3 segundos")}', 64, 28, 1.04),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 44px">',
        irow("pin", "Fixe os melhores", "Os vídeos que mostram quem você é.", True, -6, "l"),
        irow("layers", "Capas no mesmo modelo", "O perfil vira uma vitrine organizada.", False, 5, "r"),
        irow("list", "Série com nome fixo", "Mesma abertura e mesma pergunta final.", True, -4, "l"),
        '    </div>',
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T6, 6, 6, 5, [
        stamp("Resumo"),
        h(f'Perfil que vende em {amber("4 ajustes")}', 66, 36, 1.04),
        '    <div style="margin-top: 46px; display: flex; flex-direction: column; gap: 18px">',
        pstep(1, f'{b("@")} com a palavra do nicho'),
        pstep(2, f'{b("Bio:")} o quê e pra quem, sem contato'),
        pstep(3, f'{b("Link:")} 1 mil seguidores ou conta comercial'),
        pstep(4, f'{b("Topo:")} fixados e capas no mesmo modelo', True),
        '    </div>',
        GROW,
        ask("O que falta no seu perfil?", "Comenta: nome, bio ou link."),
        foot(src(f"Academia de Criadores do TikTok (jun a set/2026) · checado em {HOJE}."), 22),
    ]),
]

# ---------------------------------------------------------------- 18h: marca d'água de outro app
T18 = "Marca d'água de outro app"


def phone():
    return (f'    <div style="margin-top: 60px; display: flex; align-items: center; gap: 40px">\n'
            f'      <div style="position: relative; flex: none; width: 300px; height: 540px; border-radius: 40px; border: 5px solid {AMBER}; '
            f'background: linear-gradient(160deg, rgba(255,181,71,0.25), rgba(255,107,74,0.25) 50%, rgba(23,8,13,0.9)); box-shadow: 0 0 40px rgba(255,181,71,0.4)">\n'
            f'        <div style="position: absolute; left: 22px; bottom: 30px; border: 3px dashed {A}; border-radius: 12px; padding: 6px 12px; '
            f'{FRED}; font-size: 24px; font-weight: 700; color: {A}">LOGO</div>\n'
            f'        <div style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%) rotate(-12deg)">{svg("x", 220, "#FF6B4A", 2.6)}</div>\n'
            f'      </div>\n'
            f'      <div style="{FRED}; font-size: 50px; font-weight: 700; line-height: 1.12">Baixou de outra rede, {coral("com a logo dela,")} e postou aqui?</div>\n'
            f'    </div>')


W_CARDS = [
    card(T18, 1, 6, 1, [
        pill_solid("Isso derruba sua conta?"),
        f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: 84px; font-weight: 700; line-height: 1; text-shadow: 0 0 36px rgba(255,107,74,0.4)">Corte com {coral("marca d’água de outro app")}</h1>',
        phone(),
        GROW,
        cta("Arrasta pro veredito"),
        foot(f'Checado na <strong style="color: {AMBER}">Academia de Criadores do TikTok</strong> em {HOJE}.', 22),
    ]),
    card(T18, 2, 6, 0, [
        stamp("Veredito"),
        h(f'O vídeo {coral("sai do Para Você")}', 74, 36, 1),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 44px">',
        irow("eyeoff", "Fora do Para Você", "Conteúdo não original não é recomendado no feed.", True, -6, "l"),
        irow("coin", "Não monetiza", "Fica de fora dos programas que pagam.", False, 5, "r"),
        '    </div>',
        box_glow(f'A Academia põe isso na lista de {amber("regras que derrubam conta.")}', 50, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 3, 6, 2, [
        pill_line("O que conta como cópia"),
        h(f'O TikTok chama de {amber("não original")}', 68, 28, 1),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 20px">',
        mark_row(False, "<strong>Cópia</strong> do vídeo de outra pessoa", 34),
        mark_row(False, "Vídeo de outra fonte <strong>sem edição criativa</strong>", 34),
        mark_row(False, "<strong>Colagem</strong> sem valor novo", 34),
        mark_row(False, "<strong>Marca d’água ou logo</strong> de outro app", 34),
        '    </div>',
        box_glow(f'Qualquer um dos quatro: {amber("fora do Para Você e sem monetizar.")}', 50, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 4, 6, 3, [
        pill_line("E editar fora do TikTok?"),
        h(f'Editar em outro app {amber("pode")}', 72, 28, 1),
        f'    <div style="margin-top: 18px; font-size: 35px; line-height: 1.32; color: {SOFT}">Pela Academia, editar fora do TikTok não prejudica a busca. O problema é o que fica gravado no vídeo.</div>',
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 20px">',
        mark_row(True, "Editar no app que você preferir", 34),
        mark_row(False, "Exportar com a <strong>marca d’água</strong> do editor", 34),
        mark_row(False, "Repostar com a <strong>logo</strong> de outra rede", 34),
        '    </div>',
        box_dashed(f'{b("Antes de postar:")} assista o vídeo exportado até o fim e confira os cantos da tela.', 50, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 5, 6, 4, [
        pill_line("Jeito certo"),
        h(f'Reaproveitar {coral("sem copiar")}', 72, 28, 1),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 18px">',
        pstep(1, f'{b("Selecione")} um momento do vídeo'),
        pstep(2, f'{b("Atraia")} com um gancho novo'),
        pstep(3, f'{b("Torne nativo:")} 9:16 e legenda'),
        pstep(4, f'{b("Sem")} marca d’água nem logo de outro app', True),
        '    </div>',
        box_dashed(f'{b("Na prática:")} corte de live de outra plataforma também sai sem a logo dela.', 46, 34),
        GROW,
        foot(src(ACADEMIA)),
    ]),
    card(T18, 6, 6, 5, [
        stamp("Confere aí"),
        h(f'Onde ver se o vídeo {amber("ficou de fora")}', 64, 36, 1.04),
        '    <div style="margin-top: 50px; display: flex; flex-direction: column; gap: 44px">',
        irow("chart", "Análises → Desempenho", "Vídeo inelegível mostra um aviso ali.", True, -6, "l"),
        irow("shield", "Verificação de conta", "TikTok Studio → Mais ferramentas: olha as últimas 30 publicações.", False, 5, "r"),
        '    </div>',
        GROW,
        ask("Já postou vídeo com logo de outro app?", "Comenta: sim ou não."),
        foot(src(f"Academia de Criadores do TikTok (jun a set/2026) · checado em {HOJE}."), 22),
    ]),
]

for i, html in enumerate(P_CARDS, 1):
    (OUT / f"Perfil_{i}.dc.html").write_text(html, encoding="utf-8")
for i, html in enumerate(W_CARDS, 1):
    (OUT / f"MarcaDagua_{i}.dc.html").write_text(html, encoding="utf-8")
print(len(P_CARDS), "cards Perfil;", len(W_CARDS), "cards MarcaDagua")
