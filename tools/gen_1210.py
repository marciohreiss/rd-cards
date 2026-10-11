"""Gera os artboards .dc.html dos dois carrosséis da R&D de 12/10/2026
(padrão neon quente 3:4, área segura: 150 px no topo, 170 px à direita).
Uso: python3 gen_1210.py <pasta project/ de saída>"""
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


# ---------------------------------------------------------------- Carrossel A: conta pessoal ou comercial
def choice(icon, label, sub, coral_side):
    color = A if coral_side else AMBER
    glow = "255,107,74" if coral_side else "255,181,71"
    rot = -5 if coral_side else 5
    return (f'      <div style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 18px; border: 3px solid {color}; '
            f'border-radius: 38px; padding: 34px 20px 30px; background: rgba(23,8,13,0.62); box-shadow: 0 0 40px rgba({glow},0.4)">\n'
            f'        {tile(icon, color, glow, rot, 150, 78)}\n'
            f'        <div style="{FRED}; font-size: 46px; font-weight: 700; line-height: 1; color: {color}">{label}</div>\n'
            f'        <div style="font-size: 25px; line-height: 1.25; text-align: center; color: {SOFT}">{sub}</div>\n'
            f'      </div>')


TA = "Conta pessoal ou comercial"
A_CARDS = [
    card(TA, 1, 5, 0, [
        pill_solid("TikTok Shop do zero"),
        f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: 82px; font-weight: 700; line-height: 1; text-shadow: 0 0 36px rgba(255,107,74,0.4)">Conta pessoal ou {coral("comercial pra vender?")}</h1>',
        f'    <div style="margin-top: 24px; font-size: 33px; line-height: 1.34; color: {SOFT}">A regra de afiliado não escolhe por você. O resto do TikTok, sim.</div>',
        '    <div style="margin-top: 40px; display: flex; align-items: stretch; gap: 22px">',
        choice("user", "Pessoal", "de quem cria conteúdo", False),
        choice("store", "Comercial", "de marca ou loja", True),
        '    </div>',
        GROW,
        cta("Arrasta pra decidir"),
        foot(f'Checado na <strong style="color: {AMBER}">Academia de Criadores</strong> e na <strong style="color: {AMBER}">Academia do TikTok Shop</strong> em 11/10/2026.', 22),
    ]),
    card(TA, 2, 5, 1, [
        pill_line("O que o TikTok Shop pede"),
        h(f'Pra ser afiliado, a lista é {amber("esta")}', 66, 28),
        '    <div style="margin-top: 34px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "<strong>18 anos</strong> ou mais"),
        mark_row(True, "<strong>1.000 seguidores</strong> na conta"),
        mark_row(True, "<strong>Identidade verificada:</strong> CPF e RG, CNH ou RNE"),
        mark_row(True, "Nenhuma permissão de e-commerce <strong>revogada antes</strong>"),
        '    </div>',
        box_glow(f'Pessoal ou comercial? {amber("A política não exige nenhum dos dois.")}', 30, 32),
        f'    <div style="margin-top: 16px; font-size: 25px; line-height: 1.35; color: {SOFT}">Só não pode ser conta de governo, político ou partido.</div>',
        GROW,
        foot(src("Política de Elegibilidade de Criadores do TikTok Shop, Brasil (01/07/2026).")),
    ]),
    card(TA, 3, 5, 2, [
        h(f'Onde a conta {amber("pessoal")} ganha', 68, 44, 1),
        f'    <div style="margin-top: 14px; font-size: 32px; line-height: 1.3; color: {SOFT}">Só ela entra em:</div>',
        '    <div style="margin-top: 34px; display: flex; flex-direction: column; gap: 26px">',
        icon_row("coin", "Programa de Recompensas", "Paga por visualização qualificada em vídeo de 1 minuto ou mais.", False, -6, "l"),
        icon_row("music", "Biblioteca de Sons Ilimitados", "Mais de 80 mil sons liberados.", True, 5, "r"),
        icon_row("trophy", "Concursos de publicação", "Com prêmios em dinheiro.", False, -4, "l"),
        '    </div>',
        box_dashed(f'{b("Por isso")} a Academia resume assim: conta pessoal pra criador, comercial pra marca ou loja.', 36),
        GROW,
        foot(src("Academia de Criadores do TikTok (artigos de jun a set/2026).")),
    ]),
    card(TA, 4, 5, 3, [
        h(f'Onde a {coral("comercial")} faz sentido', 68, 44, 1),
        f'    <div style="margin-top: 14px; font-size: 32px; line-height: 1.3; color: {SOFT}">É a conta de marca ou loja.</div>',
        '    <div style="margin-top: 30px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "<strong>Link de site no perfil</strong> sem esperar os 1 mil seguidores.", 28),
        mark_row(False, "<strong>Música:</strong> só a Biblioteca de Música Comercial.", 28),
        mark_row(False, "<strong>Fica fora</strong> do Programa de Recompensas e dos concursos.", 28),
        '    </div>',
        '    <div style="margin-top: 34px; display: flex; align-items: center; gap: 26px">',
        f'      <div style="flex: none; {FRED}; font-size: 150px; font-weight: 700; line-height: 0.9; color: {AMBER}; text-shadow: 0 0 50px rgba(255,107,74,0.75), 0 0 120px rgba(255,107,74,0.4)">30</div>',
        '      <div>',
        f'        <div style="{FRED}; font-size: 40px; font-weight: 700; line-height: 1.06">dias de espera</div>',
        f'        <div style="margin-top: 8px; font-size: 27px; line-height: 1.3; color: {SOFT}">pra pedir o Programa de Recompensas depois de trocar de comercial pra pessoal.</div>',
        '      </div>',
        '    </div>',
        GROW,
        foot(src("Academia de Criadores do TikTok (artigos de jun a set/2026).")),
    ]),
    card(TA, 5, 5, 5, [
        stamp("Resumo"),
        h(f'Criador afiliado: {amber("pessoal.")}<span style="display: block">Marca ou loja: {coral("comercial.")}</span>', 66, 36, 1.06),
        box_dashed(f'{b("E as duas coisas?")} Dá pra ser criador e vendedor ao mesmo tempo, cumprindo os requisitos de cada função.', 36),
        f'    <div style="margin-top: 20px; font-size: 26px; line-height: 1.35; color: {SOFT}">Antes de trocar o tipo de conta, lembre dos 30 dias de espera do Programa de Recompensas.</div>',
        GROW,
        ask("Qual é a sua conta hoje?", "Comenta: pessoal ou comercial."),
        foot(src("Academia de Criadores do TikTok (set/2026) e Academia do TikTok Shop (jul/2025 e jul/2026) · checado em 11/10/2026."), 22),
    ]),
]

# ---------------------------------------------------------------- Carrossel B: antes do primeiro link de afiliado
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


TB = "Antes do primeiro link"
SHOP_REG = "Academia do TikTok Shop, como se registrar como criador afiliado (15/07/2025)."
B_CARDS = [
    card(TB, 1, 6, 4, [
        pill_solid("TikTok Shop do zero"),
        f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: 86px; font-weight: 700; line-height: 1; text-shadow: 0 0 36px rgba(255,107,74,0.4)">Antes do {coral("primeiro link de afiliado")}</h1>',
        f'    <div style="margin-top: 24px; font-size: 33px; line-height: 1.34; color: {SOFT}">4 passos na ordem certa, pra não travar na análise nem ficar sem sacar a comissão.</div>',
        '    <div style="margin-top: 50px; position: relative">',
        f'      <div style="position: absolute; left: 105px; right: 105px; top: 50px; height: 0; border-top: 4px dashed rgba(255,181,71,0.6)"></div>',
        '      <div style="position: relative; display: flex; align-items: flex-start">',
        dot(1, "Conferir", True), dot(2, "Inscrever", False), dot(3, "Verificar", False), dot(4, "Preparar", False),
        '      </div>',
        '    </div>',
        GROW,
        cta("Arrasta e segue a ordem"),
        foot(f'Checado na <strong style="color: {AMBER}">Academia do TikTok Shop</strong> em 11/10/2026.', 22),
    ]),
    card(TB, 2, 6, 1, [
        step_badge(1),
        h(f'Confere se você {amber("entra")}', 70, 26, 1),
        '    <div style="margin-top: 30px; display: flex; align-items: flex-end; gap: 22px">',
        f'      <div style="flex: none; {FRED}; font-size: 176px; font-weight: 700; line-height: 0.86; color: {AMBER}; text-shadow: 0 0 50px rgba(255,107,74,0.75), 0 0 120px rgba(255,107,74,0.4)">1.000</div>',
        '      <div style="padding-bottom: 12px">',
        f'        <div style="{FRED}; font-size: 40px; font-weight: 700; line-height: 1.06">seguidores</div>',
        f'        <div style="margin-top: 4px; font-size: 27px; line-height: 1.3; color: {SOFT}">é o mínimo na conta</div>',
        '      </div>',
        '    </div>',
        '    <div style="margin-top: 34px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "<strong>18 anos</strong> ou mais."),
        mark_row(True, "Nenhuma permissão de e-commerce <strong>revogada antes.</strong>"),
        '    </div>',
        f'    <div style="margin-top: 18px; font-size: 25px; line-height: 1.35; color: {SOFT}">Conta ligada a outra que perdeu a permissão também fica de fora.</div>',
        GROW,
        foot(src("Política de Elegibilidade de Criadores do TikTok Shop, Brasil (01/07/2026).")),
    ]),
    card(TB, 3, 6, 2, [
        step_badge(2),
        h(f'Faz a {amber("inscrição")} pelo app', 68, 26, 1),
        '    <div style="margin-top: 32px; display: flex; flex-direction: column; gap: 12px">',
        path_step(1, f'Abra o seu {b("Perfil")}'),
        path_step(2, f'Toque nas {b("três linhas")} do menu'),
        path_step(3, f'Entre em {b("TikTok Studio")}'),
        path_step(4, f'Toque em {b("TikTok Shop para criadores")}'),
        path_step(5, f'Confira os requisitos e toque em {b("Inscrever-se")}', True),
        '    </div>',
        box_dashed(f'{b("Depois é aguardar.")} A resposta da análise chega por notificação.', 30),
        GROW,
        foot(src(SHOP_REG)),
    ]),
    card(TB, 4, 6, 3, [
        step_badge(3),
        h(f'Verifica a {amber("identidade")}', 70, 26, 1),
        f'    <div style="margin-top: 14px; font-size: 30px; line-height: 1.32; color: {SOFT}">Depois da aprovação, a Central de criadores mostra o botão <strong style="color: #FFF3EC">Verificar</strong>. Separe:</div>',
        '    <div style="margin-top: 28px; display: flex; flex-wrap: wrap; gap: 18px">',
        doc("CPF", "informe o número"),
        doc("Documento", "RG, CNH ou RNE válido"),
        doc("Seus dados", "nome e data de nascimento"),
        doc("Fiscal", "informações fiscais"),
        '    </div>',
        box_glow(f'Sem verificação, {amber("não dá pra ganhar nem sacar comissão.")}', 32, 32),
        GROW,
        foot(src("Academia do TikTok Shop: registro de criador (15/07/2025) e Política de Elegibilidade (01/07/2026).")),
    ]),
    card(TB, 5, 6, 0, [
        step_badge(4),
        h(f'Arruma a casa {amber("antes de postar")}', 66, 26, 1),
        '    <div style="margin-top: 36px; display: flex; flex-direction: column; gap: 26px">',
        icon_row("pulse", "Saúde da Conta", "Veja na Central de criadores se há ponto de violação.", True, -6, "l"),
        icon_row("bag", "Produto pra promover", "A Central de criadores tem a seção Encontre produtos para promover.", False, 5, "r"),
        icon_row("toggle", "Divulgar conteúdo comercial", "Ligue a chavinha em todo vídeo com link.", True, -4, "l"),
        '    </div>',
        GROW,
        foot(src("Academia do TikTok Shop, Central de criadores (14/04/2025), e Central de Ajuda para Negócios do TikTok (abr/2026).")),
    ]),
    card(TB, 6, 6, 5, [
        stamp("E se travar?"),
        h(f'Cumpriu tudo e {coral("não foi aprovado?")}', 64, 36, 1.04),
        f'    <div style="margin-top: 30px; border-radius: 30px; padding: 20px 28px; background: {AMBER}; color: {INK}; box-shadow: 0 0 36px rgba(255,181,71,0.5)">',
        f'      <div style="{FRED}; font-size: 40px; font-weight: 700; line-height: 1.12">Dá pra abrir um tíquete pra investigação.</div>',
        '    </div>',
        f'    <div style="margin-top: 16px; font-size: 26px; line-height: 1.35; color: {SOFT}">É o que a própria Academia do TikTok Shop orienta pra quem atende a todos os requisitos.</div>',
        GROW,
        ask("Em qual passo você está?", "Comenta o número."),
        foot(src("Academia do TikTok Shop (abr/2025, jul/2025 e jul/2026) · checado em 11/10/2026."), 22),
    ]),
]

for i, html in enumerate(A_CARDS, 1):
    (OUT / f"Conta_{i}.dc.html").write_text(html, encoding="utf-8")
for i, html in enumerate(B_CARDS, 1):
    (OUT / f"PrimeiroLink_{i}.dc.html").write_text(html, encoding="utf-8")
print(len(A_CARDS), "cards Conta;", len(B_CARDS), "cards PrimeiroLink")
