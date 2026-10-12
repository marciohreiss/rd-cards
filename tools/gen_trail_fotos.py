"""Carrossel Trail (padrão mapa topográfico) com fotos reais do Márcio e perfil real do GPX oficial.
Reaproveita CSS e componentes de gen_estilos.py.
Uso: python3 gen_trail_fotos.py <pasta de saída> <pasta com c_*.jpg e ptr25.json>"""
import base64
import json
import pathlib
import sys

_src = (pathlib.Path(__file__).parent / "gen_estilos.py").read_text(encoding="utf-8")
exec(_src.split("def profile():")[0].replace("OUT = pathlib.Path(sys.argv[1])\nOUT.mkdir(parents=True, exist_ok=True)", ""))

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
FOT = pathlib.Path(sys.argv[2])


def img(name):
    return "data:image/jpeg;base64," + base64.b64encode((FOT / name).read_bytes()).decode()


PTR = json.loads((FOT / "ptr25.json").read_text())

EXTRA = f'''
.photo{{position:absolute;inset:0;background-size:cover;background-position:center}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,38,28,.55) 0%,rgba(20,38,28,0) 28%,rgba(20,38,28,0) 42%,rgba(20,38,28,.88) 70%,rgba(20,38,28,.97) 100%)}}
.onphoto .top{{color:{CREAM}}} .onphoto h1{{color:{CREAM}}} .onphoto .p{{color:#EFE6D2}} .onphoto .p b{{color:#F2B48F}}
.onphoto .ft{{color:#D9CBAA;border-top-color:rgba(239,230,210,.35)}}
.polaroid{{background:#FFFDF6;padding:14px 14px 50px;box-shadow:0 14px 30px rgba(30,58,43,.25);position:relative}}
.polaroid img{{display:block;width:100%}}
.polaroid span{{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-family:"Barlow Condensed",sans-serif;font-weight:700;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:{GREEN}}}
'''
CSS = TCSS + EXTRA


def tpage(n, total, body, seed, photo=None):
    pos = (n - 1) / (total - 1) * 96
    head = (f'<div class="top"><span>R&amp;D · Diário de trilha</span><span class="km">KM {n:02d}/{total:02d}</span></div>'
            f'<div class="trail"><i style="left:{pos:.1f}%"></i></div>')
    if photo:
        bg = f'<div class="photo" style="background-image:url({img(photo)})"></div><div class="shade"></div>'
        return page("Trail", CSS, f'<div class="c onphoto">{bg}<div class="in" data-safe>{head}{body}</div></div>')
    topo = f'<svg class="topo" width="1080" height="1440">{contours(seed, 760 if seed % 2 else 300, 1080 if seed % 3 else 420)}</svg>'
    return page("Trail", CSS, f'<div class="c">{topo}<div class="in" data-safe>{head}{body}</div></div>')


def real_profile():
    pts = PTR["prof"]
    w, h = 836, 300
    top = max(pts)
    step = w / (len(pts) - 1)
    line = " ".join(f"{i*step:.1f},{h-26-(v/top)*(h-70):.1f}" for i, v in enumerate(pts))
    return (f'<svg width="{w}" height="{h}" style="display:block;margin-top:26px">'
            f'<polygon points="0,{h} {line} {w},{h}" fill="{GREEN}" fill-opacity=".92"/>'
            f'<polyline points="{line}" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-linejoin="round"/>'
            f'<text x="12" y="{h-8}" font-family="Barlow Condensed" font-weight="700" font-size="24" fill="{CREAM}">LARGADA</text>'
            f'<text x="{w-12}" y="{h-8}" text-anchor="end" font-family="Barlow Condensed" font-weight="700" font-size="24" fill="{CREAM}">CHEGADA</text>'
            f'<text x="{w-12}" y="22" text-anchor="end" font-family="Barlow" font-size="18" fill="#6A6453">percurso oficial (GPX) · ponto mais alto {top} m</text>'
            f'</svg>')


KM = f'{PTR["km"]:.0f}'.replace(".", ",")
GAIN = f'{round(PTR["gain"], -1):,.0f}'.replace(",", ".")
ST = "meus treinos e provas registrados no Strava (2026)"
NT = 7
TRAIL = [
    tpage(1, NT, f'''
<div class="grow"></div>
<div class="kick" style="background:{ORANGE}">Trail run de verdade</div>
<h1 style="font-size:112px">Treinar montanha numa <em>cidade plana</em></h1>
<div class="p">Moro em Uberlândia, quase não tem subida. Mesmo assim terminei <b>La Misión, KTR e Paraty by UTMB</b> em 2026. Te conto como.</div>
<div class="cta" style="margin-top:28px"><span>Arrasta: é o que eu faço</span><span>→</span></div>
<div class="ft">Foto: chegada do Paraty Brazil by UTMB 2026 · relato pessoal</div>''', 3, "c_cover.jpg"),
    tpage(2, NT, f'''
<div class="kick">O tamanho do problema</div>
<h2>Montanha <em>não perdoa</em></h2>
{real_profile()}
<div style="display:flex;align-items:baseline;gap:18px;margin-top:20px"><span style="font-family:'Barlow Condensed';font-weight:800;font-size:110px;line-height:.9;color:{ORANGE}">~{GAIN} m</span><span style="font-family:'Barlow Condensed';font-weight:700;font-size:32px;text-transform:uppercase;color:{GREEN}">de subida em {KM} km</span></div>
<div class="p" style="margin-top:8px">no PTR 25 de Paraty. Na La Misión Serra Fina foram <b>2.675 m em 36,87 km</b>. E aqui, subida tem que ser caçada.</div>
<div class="grow"></div><div class="ft">Fonte: GPX oficial do PTR 25 (Paraty Brazil by UTMB 2026), cálculo próprio · {ST}</div>''', 4),
    tpage(3, NT, f'''
<div class="kick">A semana que funciona pra mim</div>
<h2>Cada dia, <em>uma subida</em></h2>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:32px">
<div class="sign"><b>Terça</b>tiros (velocidade)</div>
<div class="sign"><b>Quinta</b>rampa de 7% (força na subida)</div>
<div class="sign"><b>Sexta</b>escada (perna e cardio)</div>
<div class="sign"><b>Domingo</b>longão em trilha</div></div>
<div class="box"><b>+ treino de força</b> durante a semana.</div>
<div class="grow"></div><div class="ft">Rotina pessoal, não é prescrição. Procure um profissional para montar a sua.</div>''', 5),
    tpage(4, NT, f'''
<div class="kick">Onde acumular D+</div>
<h2>Ache o seu <em>morro de treino</em></h2>
<div class="p">Aqui, é a <b>Serrinha</b>: o lugar que mais soma altimetria e fica perto de casa. Logística boa vale mais que o morro perfeito longe.</div>
<div class="box">Treino que você repete <b>toda semana</b> ganha do treino épico uma vez por mês.</div>
<div style="margin:30px 0 0 160px;width:430px;transform:rotate(-3deg)" class="polaroid"><img src="{img("c_rua.jpg")}"><span>Prova é consequência</span></div>
<div class="grow"></div><div class="ft">Fonte: {ST}</div>''', 7),
    tpage(5, NT, f'''
<div class="kick">O que mudou</div>
<h2>Parei de <em>recomeçar</em> a cada prova</h2>
<div class="p">Agora o plano mira um objetivo só, e cada prova é um degrau dele.</div>
<div style="display:flex;gap:22px;margin-top:28px;align-items:flex-start">
<div class="polaroid" style="width:380px;transform:rotate(-3deg);flex:none"><img src="{img("c_utmb.jpg")}"><span>Paraty · PTR 25</span></div>
<div style="display:flex;flex-direction:column;gap:16px;flex:1">
<div class="bib" style="padding:50px 18px 14px"><span class="h">2026</span><div class="n" style="font-size:46px">36,87 KM</div><div class="s">La Misión Serra Fina</div></div>
<div class="bib" style="padding:50px 18px 14px"><span class="h">2026</span><div class="n" style="font-size:46px">30 KM</div><div class="s">KTR Campos do Jordão</div></div>
<div class="bib" style="padding:50px 18px 14px"><span class="h">2026</span><div class="n" style="font-size:46px">{KM} KM</div><div class="s">Paraty by UTMB · PTR 25</div></div>
</div></div>
<div class="grow"></div><div class="ft">Fonte: {ST}</div>''', 8),
    tpage(6, NT, f'''
<div class="kick">Próximo degrau</div>
<div style="display:flex;align-items:center;gap:26px;margin-top:30px">
<div class="bib" style="flex:none;width:400px;padding:62px 24px 22px"><span class="h">Meta · ago/2027</span><div class="n" style="font-size:130px;color:{ORANGE}">50K+</div><div class="s">uma ultra · alvo: La Misión 55K</div></div>
<div class="polaroid" style="flex:1;transform:rotate(3deg)"><img src="{img("c_casal.jpg")}"><span>Rico e Débora</span></div>
</div>
<div class="box" style="margin-top:36px">E não vou sozinho: <b>a Débora vai nos 18 km.</b> Objetivo e família na mesma prova.</div>
<div class="grow"></div><div class="ft">Planejamento pessoal 2027 · foto em Paraty, set/2026</div>''', 10),
    tpage(7, NT, f'''
<div class="kick">Bora junto?</div>
<h2>Corre em cidade plana <em>também?</em></h2>
<div class="p">Salva esse post pro próximo treino e me conta onde você caça subida aí.</div>
<div style="margin:34px 0 0 140px;width:470px;transform:rotate(2deg)" class="polaroid"><img src="{img("c_welcome.jpg")}"><span>Bem-vindo à montanha</span></div>
<div class="grow"></div>
<div class="ask"><div>Onde você treina subida?</div><div>Comenta o nome do lugar.</div></div>
<div class="ft">Relato pessoal · Rico e Débora</div>''', 11),
]

for i, h in enumerate(TRAIL, 1):
    (OUT / f"TrailF_{i}.html").write_text(h, encoding="utf-8")
print(len(TRAIL), "Trail com fotos;", KM, "km;", GAIN, "m D+")
