"""Carrossel Trail parte 2 (14/10/2026 13h): a semana de treino de subida, dia a dia.
Padrão mapa topográfico (gen_estilos.py). Fotos recortadas dos cards aprovados do trail de 13/10.
Uso: python3 gen_trail_parte2.py <pasta de saída> <pasta com p_*.jpg>"""
import base64
import pathlib
import sys

_src = (pathlib.Path(__file__).parent / "gen_estilos.py").read_text(encoding="utf-8")
exec(_src.split("def profile():")[0].replace("OUT = pathlib.Path(sys.argv[1])\nOUT.mkdir(parents=True, exist_ok=True)", ""))

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
FOT = pathlib.Path(sys.argv[2])


def img(name):
    return "data:image/jpeg;base64," + base64.b64encode((FOT / name).read_bytes()).decode()


EXTRA = f'''
.polaroid{{background:#FFFDF6;padding:14px 14px 50px;box-shadow:0 14px 30px rgba(30,58,43,.25);position:relative}}
.polaroid img{{display:block;width:100%}}
.polaroid span{{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:{GREEN}}}
.week{{display:flex;flex-direction:column;gap:20px;margin-top:34px}}
.week .sign{{font-size:36px;padding:24px 70px 24px 26px}} .week .sign b{{font-size:44px;min-width:190px}}
.week .sign{{opacity:.38}}
.week .sign.on{{opacity:1;background:{ORANGE}}}
.week .sign.on b{{color:{CREAM}}}
.big{{font-family:"Barlow Condensed",sans-serif;font-weight:800;line-height:.85;color:{ORANGE}}}
.coverphoto{{position:absolute;left:0;top:0;width:1080px;height:760px;background-size:cover;background-position:top}}
.covershade{{position:absolute;left:0;right:0;top:430px;bottom:0;background:linear-gradient(180deg,rgba(30,58,43,0) 0%,{GREEN} 30%,{GREEN} 100%)}}
.cv h1,.cv .p,.cv .ft{{color:{CREAM}}} .cv .p b{{color:#F2B48F}} .cv .ft{{border-top-color:rgba(239,230,210,.35);color:#D9CBAA}}
'''
CSS = TCSS + EXTRA
NT = 7
ST = "meus treinos e provas registrados no Strava (2026)"
PESSOAL = "Rotina pessoal, não é prescrição. Procure um profissional para montar a sua."
DAYS = [("Terça", "tiros (velocidade)"), ("Quinta", "rampa de 7% (força na subida)"),
        ("Sexta", "escada (perna e cardio)"), ("Domingo", "longão em trilha")]


def tpage(n, body, seed):
    pos = (n - 1) / (NT - 1) * 96
    head = (f'<div class="top"><span>R&amp;D · Diário de trilha</span><span class="km">KM {n:02d}/{NT:02d}</span></div>'
            f'<div class="trail"><i style="left:{pos:.1f}%"></i></div>')
    topo = f'<svg class="topo" width="1080" height="1440">{contours(seed, 760 if seed % 2 else 300, 1080 if seed % 3 else 420)}</svg>'
    return page("Trail parte 2", CSS, f'<div class="c">{topo}<div class="in" data-safe>{head}{body}</div></div>')


def week(on):
    rows = "".join(f'<div class="sign{" on" if d == on else ""}"><b>{d}</b>{t}</div>' for d, t in DAYS)
    return f'<div class="week">{rows}</div>'


STAIRS = (f'<svg width="760" height="543" viewBox="0 0 420 300" style="display:block">'
          f'<polyline points="10,290 10,240 80,240 80,190 150,190 150,140 220,140 220,90 290,90 290,40 360,40 360,10 410,10" '
          f'fill="none" stroke="{GREEN}" stroke-width="10" stroke-linejoin="round"/>'
          f'<polyline points="40,220 380,0" fill="none" stroke="{ORANGE}" stroke-width="6" stroke-dasharray="18 12"/></svg>')

COVER = page("Trail parte 2", CSS, f'''<div class="c">
<div class="coverphoto" style="background-image:url({img("p_cover_top.jpg")})"></div><div class="covershade"></div>
<div class="in cv" data-safe style="padding-top:0">
<div class="grow"></div>
<div class="kick" style="background:{ORANGE}">Parte 2 · a semana</div>
<h1 style="font-size:104px">Subida numa <em>cidade plana</em>, dia a dia</h1>
<div class="p">Ontem contei que terminei <b>La Misión, KTR e Paraty by UTMB</b> em 2026 morando em Uberlândia. Hoje, a semana que me levou lá.</div>
<div class="cta" style="margin-top:28px"><span>Arrasta: terça a domingo</span><span>→</span></div>
<div class="ft">Foto: chegada do Paraty Brazil by UTMB 2026 · relato pessoal</div>
</div></div>''')

CARDS = [
    COVER,
    tpage(2, f'''
<div class="kick">Terça</div>
<h2>Dia de <em>tiros</em></h2>
<div class="p">O treino de <b>velocidade</b> da semana.</div>
<div class="grow"></div>{week("Terça")}
<div class="box" style="margin-top:44px"><b>4 treinos-chave</b> por semana, um com cada objetivo. A terça abre a semana.</div><div class="grow"></div><div class="ft">{PESSOAL}</div>''', 4),
    tpage(3, f'''
<div class="kick">Quinta</div>
<div class="grow"></div><div style="display:flex;align-items:flex-end;gap:24px;margin-top:26px">
<div class="big" style="font-size:380px">7%</div>
<div style="padding-bottom:26px;font-family:'Barlow Condensed';font-weight:800;font-size:62px;line-height:1;text-transform:uppercase;color:{GREEN}">de rampa:<br>força na<br>subida</div></div>
<div class="p" style="font-size:38px;margin-top:30px">Sem morro perto de casa, <b>a subida vem da rampa.</b></div>
<div class="box">Na La Misión Serra Fina foram <b>2.675 m de subida em 36,87 km</b>. É pra isso que a quinta existe.</div>
<div class="grow"></div><div class="grow"></div><div class="ft">Fonte: {ST} · {PESSOAL}</div>''', 5),
    tpage(4, f'''
<div class="kick">Sexta</div>
<h2>Escada: <em>perna e cardio</em></h2>
<div class="p">Mais um jeito de <b>subir sem sair da cidade.</b></div>
<div class="grow"></div><div style="margin-left:40px">{STAIRS}</div><div class="grow"></div><div class="ft">{PESSOAL}</div>''', 7),
    tpage(5, f'''
<div class="kick">Domingo</div>
<h2>Longão <em>em trilha</em></h2>
<div class="p">O treino mais longo da semana. Aqui, a <b>Serrinha</b> é o lugar que mais soma altimetria perto de casa.</div>
<div class="box">Logística boa vale mais que o <b>morro perfeito longe.</b></div>
<div class="grow"></div><div class="polaroid" style="width:520px;margin-left:120px;transform:rotate(-3deg)"><img src="{img("p_rua.jpg")}"><span>Paraty · PTR 25</span></div><div class="grow"></div><div class="ft">Fonte: {ST} · {PESSOAL}</div>''', 8),
    tpage(6, f'''
<div class="kick">O que segura tudo</div>
<h2>Força e <em>repetição</em></h2>
<div class="p">Por baixo dos quatro dias, <b>treino de força durante a semana.</b></div>
<div class="grow"></div>{week("")}
<div class="box">Treino que você repete <b>toda semana</b> ganha do treino épico uma vez por mês.</div>
<div class="grow"></div><div class="ft">{PESSOAL}</div>''', 10),
    tpage(7, f'''
<div class="kick">Pra onde isso vai</div>
<div style="display:flex;align-items:center;gap:26px;margin-top:30px">
<div class="bib" style="flex:none;width:380px;padding:62px 24px 22px"><span class="h">Meta · ago/2027</span><div class="n" style="font-size:124px;color:{ORANGE}">50K+</div><div class="s">uma ultra · alvo: La Misión 55K</div></div>
<div class="polaroid" style="flex:1;transform:rotate(3deg)"><img src="{img("p_casal.jpg")}"><span>Rico e Débora</span></div></div>
<div class="box" style="margin-top:34px">E a <b>Débora vai nos 18 km.</b></div>
<div class="grow"></div>
<div class="ask"><div>Qual desses dias é o seu?</div><div>Comenta: terça, quinta, sexta ou domingo.</div></div>
<div class="ft">Relato pessoal · Rico e Débora</div>''', 11),
]

for i, h in enumerate(CARDS, 1):
    (OUT / f"TrailP2_{i}.html").write_text(h, encoding="utf-8")
print(len(CARDS), "cards Trail parte 2")
