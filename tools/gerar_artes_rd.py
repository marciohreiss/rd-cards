"""Gerador de artes R&D Garimpo (Plano B, sem ChatGPT).

Uso: python artes.py <pasta_saida>
Gera 1080x1350 PNG: D1111-01..09 (Instagram) e B1111-05..13 (TikTok bot).
Sem logos/marcas de terceiros. Fonte Liberation Sans (compativel com Arial).
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
VERDE = (49, 71, 57)
GRAFITE = (32, 42, 48)
CLARO = (236, 242, 237)
DESTAQUE = (150, 214, 160)
ALERTA = (226, 90, 80)
BRANCO = (255, 255, 255)
CINZA = (160, 175, 168)
_FONTES = Path(__file__).parent / "fonts"
FB = str(_FONTES / "Poppins-Bold.ttf")
FR = str(_FONTES / "Poppins-Medium.ttf")
FSEMI = str(_FONTES / "Poppins-SemiBold.ttf")
FANTON = str(_FONTES / "Anton-Regular.ttf")
FSERIF = str(_FONTES / "DMSerifDisplay-Regular.ttf")
OURO = (227, 167, 47)
PAPEL = (243, 238, 227)


def f(size, bold=True):
    return ImageFont.truetype(FB if bold else FR, size)


def anton(size):
    return ImageFont.truetype(FANTON, size)


def semi(size):
    return ImageFont.truetype(FSEMI, size)


def serif(size):
    return ImageFont.truetype(FSERIF, size)


def fundo():
    img = Image.new("RGB", (W, H), VERDE)
    px = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(VERDE[i] * (1 - t) + GRAFITE[i] * t) for i in range(3))
        px.line([(0, y), (W, y)], fill=c)
    return img


def quebra(d, texto, fonte, largura):
    linhas, atual = [], ""
    for p in texto.split():
        t = (atual + " " + p).strip()
        if d.textlength(t, font=fonte) <= largura:
            atual = t
        else:
            linhas.append(atual)
            atual = p
    linhas.append(atual)
    return linhas


def titulo(d, texto, y=170, largura=900):
    texto = texto.upper()
    for tam in (112, 100, 90, 80, 70, 62):
        fonte = anton(tam)
        ls = quebra(d, texto, fonte, largura)
        if len(ls) <= 3:
            break
    passo = int(tam * 1.26)
    for i, ln in enumerate(ls):
        d.text((W // 2, y + i * passo), ln, font=fonte, fill=BRANCO, anchor="mt")
    return y + len(ls) * passo


def chip(d, texto):
    fonte = semi(28)
    texto = "  ".join(texto.upper())  # espacejamento de letras
    w = d.textlength(texto, font=fonte) + 64
    x0 = (W - w) / 2
    d.rounded_rectangle([x0, 66, x0 + w, 122], 28, fill=OURO)
    d.text((W / 2, 94), texto, font=fonte, fill=GRAFITE, anchor="mm")


def rodape(d, texto):
    d.rounded_rectangle([60, 1196, W - 60, 1290], 47, fill=PAPEL)
    d.ellipse([92, 1232, 118, 1258], fill=OURO)
    d.text((W / 2 + 14, 1243), texto, font=semi(34), fill=GRAFITE, anchor="mm")


def estrela(d, cx, cy, r, cor):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=cor)


def check(d, cx, cy, s, cor=DESTAQUE, w=12):
    d.line([(cx - s, cy), (cx - s / 3, cy + s * 0.7), (cx + s, cy - s * 0.7)], fill=cor, width=w, joint="curve")


def xis(d, cx, cy, s, cor=ALERTA, w=12):
    d.line([(cx - s, cy - s), (cx + s, cy + s)], fill=cor, width=w)
    d.line([(cx - s, cy + s), (cx + s, cy - s)], fill=cor, width=w)


def celular(d, cx, y0, w=330, h=440, linhas=3, tela=CLARO):
    x0 = cx - w // 2
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 48, fill=GRAFITE, outline=CLARO, width=8)
    d.rounded_rectangle([x0 + 18, y0 + 18, x0 + w - 18, y0 + h - 18], 34, fill=tela)
    d.rounded_rectangle([cx - 40, y0 + 28, cx + 40, y0 + 40], 6, fill=GRAFITE)
    for i in range(linhas):
        yy = y0 + 76 + i * 100
        d.rounded_rectangle([x0 + 40, yy, x0 + w - 40, yy + 84], 20, fill=(214, 232, 218))
        d.ellipse([x0 + 56, yy + 17, x0 + 106, yy + 67], fill=VERDE)
        d.rounded_rectangle([x0 + 124, yy + 18, x0 + w - 70, yy + 38], 8, fill=GRAFITE)
        d.rounded_rectangle([x0 + 124, yy + 50, x0 + w - 130, yy + 66], 8, fill=CINZA)


def selo_hora(d, cx, cy, hora, r=78):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CLARO, outline=DESTAQUE, width=8)
    d.text((cx, cy), hora, font=f(46), fill=GRAFITE, anchor="mm")


def ilus_celular_horas(d):
    celular(d, W // 2, 700)
    selo_hora(d, 190, 760, "11h")
    selo_hora(d, 890, 760, "18h")
    selo_hora(d, 190, 1000, "21h")


def ilus_lupa(d):
    for i in range(3):
        d.rounded_rectangle([130 + i * 40, 760 + i * 20, 470 + i * 40, 940 + i * 20], 24, fill=(70, 92, 78))
        xis(d, 300 + i * 40, 850 + i * 20, 30)
    d.rounded_rectangle([560, 700, 960, 1000], 30, fill=CLARO)
    for i in range(5):
        estrela(d, 625 + i * 68, 790, 30, OURO)
    d.text((760, 880), "4,7+", font=f(96), fill=GRAFITE, anchor="mm")
    d.ellipse([850, 930, 940, 1020], fill=DESTAQUE)
    check(d, 895, 975, 24, GRAFITE, 10)


def ilus_relogios(d):
    for i, h in enumerate(("11h", "18h", "21h")):
        cx = 220 + i * 320
        d.ellipse([cx - 120, 700, cx + 120, 940], fill=CLARO, outline=DESTAQUE, width=10)
        ang = {"11h": -60, "18h": 90, "21h": 180}[h]
        d.line([(cx, 820), (cx + 70 * math.cos(math.radians(ang)), 820 + 70 * math.sin(math.radians(ang)))], fill=GRAFITE, width=10)
        d.line([(cx, 820), (cx, 750)], fill=GRAFITE, width=8)
        d.text((cx, 990), h, font=f(60), fill=BRANCO, anchor="mm")
    d.text((W // 2, 1100), "10 achados em cada horário", font=f(44, False), fill=CLARO, anchor="mm")


def ilus_sofa(d):
    celular(d, W // 2, 690, linhas=3)
    d.text((W // 2, 1160), "os achados chegam prontos", font=f(38, False), fill=CLARO, anchor="mm")


def ilus_cronometro(d):
    celular(d, 400, 700, w=320, h=440, linhas=2)
    d.ellipse([700, 760, 940, 1000], fill=CLARO, outline=ALERTA, width=12)
    d.line([(820, 880), (820, 810)], fill=GRAFITE, width=10)
    d.line([(820, 880), (870, 900)], fill=GRAFITE, width=10)
    d.rounded_rectangle([790, 730, 850, 755], 8, fill=ALERTA)


def ilus_noite(d):
    celular(d, W // 2, 690, linhas=3)
    d.ellipse([820, 700, 960, 840], fill=(250, 226, 150))
    d.ellipse([850, 690, 990, 830], fill=GRAFITE)
    d.text((W // 2, 1160), "21h · o garimpo da noite", font=f(40, False), fill=CLARO, anchor="mm")


def ilus_checklist(d):
    d.rounded_rectangle([220, 690, 860, 1120], 36, fill=CLARO)
    for i, t in enumerate(("Nota", "Vendas", "Loja")):
        yy = 770 + i * 120
        d.rounded_rectangle([270, yy - 36, 340, yy + 34], 14, fill=DESTAQUE)
        check(d, 305, yy, 20, GRAFITE, 9)
        d.text((380, yy), t, font=f(58), fill=GRAFITE, anchor="lm")


def ilus_equacao(d):
    d.ellipse([90, 760, 330, 1000], fill=CLARO)
    d.text((210, 860), "+ mil", font=f(66), fill=GRAFITE, anchor="mm")
    d.text((210, 935), "vendas", font=f(36, False), fill=GRAFITE, anchor="mm")
    d.text((385, 880), "+", font=f(90), fill=BRANCO, anchor="mm")
    d.ellipse([450, 760, 690, 1000], fill=CLARO)
    estrela(d, 570, 825, 40, OURO)
    d.text((570, 920), "4,7+", font=f(70), fill=GRAFITE, anchor="mm")
    d.text((735, 880), "=", font=f(90), fill=BRANCO, anchor="mm")
    cx, cy = 900, 880
    for r in (110, 75, 40):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=DESTAQUE, width=8)
    d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=DESTAQUE)
    d.text((cx, 1030), "radar", font=f(40), fill=DESTAQUE, anchor="mm")


def ilus_sem_corrente(d):
    celular(d, 330, 700, w=320, h=440, linhas=3)
    d.rounded_rectangle([600, 760, 960, 960], 40, fill=(190, 200, 195))
    d.text((780, 860), "corrente?", font=f(46), fill=GRAFITE, anchor="mm")
    xis(d, 780, 860, 150, ALERTA, 16)
    d.text((780, 1040), "só oferta conferida", font=f(36, False), fill=CLARO, anchor="mm")


def ilus_cansaco(d):
    for i, t in enumerate(("legenda", "hashtags", "aviso de afiliado")):
        yy = 720 + i * 120
        d.rounded_rectangle([200, yy, 880, yy + 92], 24, fill=CLARO)
        d.text((240, yy + 46), t, font=f(44), fill=GRAFITE, anchor="lm")
        d.line([(230, yy + 46), (850, yy + 46)], fill=ALERTA, width=6)
    d.text((W // 2, 1110), "para cada rede, todo dia", font=f(40, False), fill=CLARO, anchor="mm")


def ilus_leque(d):
    cx = W // 2
    d.rounded_rectangle([cx - 150, 700, cx + 150, 800], 40, fill=CLARO)
    d.text((cx, 750), "link", font=f(56), fill=GRAFITE, anchor="mm")
    for i in range(11):
        ang = math.radians(25 + i * (130 / 10))
        x = cx + 380 * math.cos(ang) * 1.05
        y = 800 + 330 * math.sin(ang)
        d.line([(cx, 800), (x, y)], fill=(90, 115, 100), width=3)
        d.rounded_rectangle([x - 42, y - 42, x + 42, y + 42], 16, fill=DESTAQUE)
        d.text((x, y), str(i + 1), font=f(34), fill=GRAFITE, anchor="mm")


def ilus_relogio_celular(d):
    d.ellipse([110, 760, 370, 1020], fill=CLARO, outline=DESTAQUE, width=10)
    d.line([(240, 890), (240, 810)], fill=GRAFITE, width=10)
    d.line([(240, 890), (300, 920)], fill=GRAFITE, width=10)
    celular(d, 700, 700, w=330, h=440, linhas=2)


def ilus_antes_depois(d, esq="link solto", dir_="post pronto"):
    d.rounded_rectangle([70, 720, 470, 1100], 30, fill=(70, 92, 78))
    d.text((270, 780), "ANTES", font=f(40), fill=CINZA, anchor="mm")
    d.rounded_rectangle([110, 880, 430, 940], 20, fill=CLARO)
    d.text((270, 910), esq, font=f(34, False), fill=GRAFITE, anchor="mm")
    d.polygon([(500, 880), (560, 910), (500, 940)], fill=DESTAQUE)
    d.rounded_rectangle([590, 720, 1010, 1100], 30, fill=CLARO)
    d.text((800, 780), "DEPOIS", font=f(40), fill=VERDE, anchor="mm")
    for i, t in enumerate(("título", "legenda", "hashtags", "aviso")):
        d.rounded_rectangle([620, 830 + i * 64, 980, 880 + i * 64], 14, fill=(214, 232, 218))
        d.text((800, 855 + i * 64), t, font=f(32), fill=GRAFITE, anchor="mm")


def ilus_copiar(d):
    ilus_antes_depois(d, "copiar+colar", "só o link")


def ilus_painel(d):
    for i, h in enumerate(("11h", "18h", "21h")):
        x0 = 80 + i * 320
        d.rounded_rectangle([x0, 720, x0 + 280, 1050], 30, fill=CLARO)
        d.text((x0 + 140, 790), h, font=f(50), fill=VERDE, anchor="mm")
        d.text((x0 + 140, 920), "10", font=f(150), fill=GRAFITE, anchor="mm")
        d.text((x0 + 140, 1005), "ofertas", font=f(34, False), fill=GRAFITE, anchor="mm")
    d.text((W // 2, 1120), "tudo automático", font=f(40, False), fill=CLARO, anchor="mm")


def ilus_planos(d):
    for i, (n, p) in enumerate((("semanal", "9,90"), ("mensal", "24,90"), ("trimestral", "59,90"))):
        x0 = 70 + i * 322
        d.rounded_rectangle([x0, 730, x0 + 296, 1060], 30, fill=CLARO)
        d.text((x0 + 148, 800), n, font=f(40), fill=VERDE, anchor="mm")
        d.text((x0 + 148, 900), "R$", font=f(40, False), fill=GRAFITE, anchor="mm")
        d.text((x0 + 148, 980), p, font=f(70), fill=GRAFITE, anchor="mm")
    d.text((W // 2, 1120), "via Pix · 3 conversões grátis para testar", font=f(36, False), fill=CLARO, anchor="mm")


INSTA = "Canal R&D Radar · link na bio"
BOT = "Teste grátis no Telegram · link na bio"

ARTES = [
    ("D1111-01", "04_instagram", "insta", "3 achados por dia", "3 garimpos por dia. Você vê primeiro.", ilus_celular_horas, INSTA),
    ("D1111-02", "04_instagram", "insta", "meu filtro", "Só entra produto com nota 4,7+", ilus_lupa, INSTA),
    ("D1111-03", "04_instagram", "insta", "horários", "11h · 18h · 21h: hora do garimpo", ilus_relogios, INSTA),
    ("D1111-04", "04_instagram", "insta", "POV", "POV: você parou de procurar promoção sozinho", ilus_sofa, INSTA),
    ("D1111-05", "04_instagram", "insta", "POV", "POV: o achado chega antes de esgotar", ilus_cronometro, INSTA),
    ("D1111-06", "04_instagram", "insta", "POV", "POV: seu celular avisa quando tem garimpo", ilus_noite, INSTA),
    ("D1111-07", "04_instagram", "insta", "conferido", "Antes de postar, eu confiro: nota, vendas, loja", ilus_checklist, INSTA),
    ("D1111-08", "04_instagram", "insta", "a conta", "Milhares de vendas + nota alta = entra no radar", ilus_equacao, INSTA),
    ("D1111-09", "04_instagram", "insta", "sem corrente", "Sem corrente, sem conversa: só oferta conferida", ilus_sem_corrente, INSTA),
    ("B1111-05", "05_bot_conversor", "bot", "para afiliados", "Você ainda escreve legenda pra cada rede?", ilus_cansaco, BOT),
    ("B1111-06", "05_bot_conversor", "bot", "1 link", "1 link. 11 posts prontos.", ilus_leque, BOT),
    ("B1111-07", "05_bot_conversor", "bot", "sem tempo?", "Afiliado sem tempo? Cola o link e pronto.", ilus_relogio_celular, BOT),
    ("B1111-08", "05_bot_conversor", "bot", "antes e depois", "Link cru → post pronto pro WhatsApp", ilus_antes_depois, BOT),
    ("B1111-09", "05_bot_conversor", "bot", "antes e depois", "Do link solto ao post completo", ilus_antes_depois, BOT),
    ("B1111-10", "05_bot_conversor", "bot", "antes e depois", "Antes: copiar e colar. Depois: só colar o link.", ilus_copiar, BOT),
    ("B1111-11", "05_bot_conversor", "bot", "na prática", "Quer ver automação de afiliado na prática?", ilus_celular_horas, "Canal t.me/rd_radarofertas · link na bio"),
    ("B1111-12", "05_bot_conversor", "bot", "bastidor", "30 ofertas por dia sem eu digitar nada", ilus_painel, BOT),
    ("B1111-13", "05_bot_conversor", "bot", "teste grátis", "Teste grátis: 3 conversões no Telegram", ilus_planos, BOT),
]


def gerar(saida: Path):
    saida.mkdir(parents=True, exist_ok=True)
    for id_, _pasta, tipo, tag, texto, ilus, rod in ARTES:
        img = fundo()
        d = ImageDraw.Draw(img)
        chip(d, tag.upper())
        titulo(d, texto)
        ilus(d)
        rodape(d, rod)
        img.save(saida / f"{id_}_{tipo}.png", optimize=True)
    return len(ARTES)


if __name__ == "__main__":
    print(gerar(Path(sys.argv[1] if len(sys.argv) > 1 else "artes_saida")), "artes")
