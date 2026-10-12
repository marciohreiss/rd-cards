"""Carrosséis de teste de formato da R&D (13 e 14/10/2026): Trail Run (pessoal) e usos do DJI Neo 2 (produto).
Reaproveita os componentes do padrão neon quente de gen_1210.py.
Uso: python3 gen_testes_1013.py <pasta project/ de saída>"""
import pathlib
import sys

_src = (pathlib.Path(__file__).parent / "gen_1210.py").read_text(encoding="utf-8")
exec(_src.split("# ---------------------------------------------------------------- Carrossel A")[0])


def big(num, label, sub, top=34):
    return (f'    <div style="margin-top: {top}px; display: flex; align-items: center; gap: 26px">\n'
            f'      <div style="flex: none; {FRED}; font-size: 140px; font-weight: 700; line-height: 0.9; color: {AMBER}; '
            f'text-shadow: 0 0 50px rgba(255,107,74,0.75), 0 0 120px rgba(255,107,74,0.4)">{num}</div>\n'
            f'      <div>\n        <div style="{FRED}; font-size: 40px; font-weight: 700; line-height: 1.06">{label}</div>\n'
            f'        <div style="margin-top: 8px; font-size: 27px; line-height: 1.3; color: {SOFT}">{sub}</div>\n      </div>\n    </div>')


def p(text, top=22, size=31):
    return f'    <div style="margin-top: {top}px; font-size: {size}px; line-height: 1.34; color: {SOFT}">{text}</div>'


# ---------------------------------------------------------------- Trail Run (pessoal)
TT = "Montanha em cidade plana"
NT = 7
STRAVA = "meus treinos e provas registrados no Strava (2026)."
TRAIL = [
    card(TT, 1, NT, 0, [
        pill_solid("Trail run de verdade"),
        f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: 82px; font-weight: 700; line-height: 1; text-shadow: 0 0 36px rgba(255,107,74,0.4)">Treinar montanha morando numa {coral("cidade plana")}</h1>',
        p("Moro em Uberlândia. Quase não tem subida. Mesmo assim terminei La Misión, KTR e Paraty by UTMB em 2026. Te conto como.", 26, 33),
        GROW,
        cta("Arrasta: é o que eu faço"),
        foot(f'Relato pessoal · base: <strong style="color: {AMBER}">{STRAVA}</strong>', 22),
    ]),
    card(TT, 2, NT, 1, [
        pill_line("O tamanho do problema"),
        h(f'Uma prova de montanha {amber("não perdoa")}', 66, 28, 1.02),
        big("2.675", "metros de subida", "na La Misión Serra Fina, em 36,87 km."),
        box_dashed(f'{b("E aqui?")} O relevo da cidade não ajuda. Subida tem que ser caçada.', 36),
        GROW,
        foot(src(STRAVA)),
    ]),
    card(TT, 3, NT, 2, [
        pill_line("A semana que funciona pra mim"),
        h(f'Cada dia {amber("um tipo de subida")}', 66, 28, 1.02),
        '    <div style="margin-top: 32px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "<strong>Terça:</strong> tiros (velocidade)", 29),
        mark_row(True, "<strong>Quinta:</strong> rampa de 7% (força na subida)", 29),
        mark_row(True, "<strong>Sexta:</strong> escada (perna e cardio)", 29),
        mark_row(True, "<strong>Domingo:</strong> longão em trilha", 29),
        '    </div>',
        box_dashed(f'{b("Mais o treino de força")} durante a semana.', 26),
        GROW,
        foot("Rotina pessoal, não é prescrição. Procure um profissional para montar a sua."),
    ]),
    card(TT, 4, NT, 3, [
        pill_line("Onde acumular D+"),
        h(f'Ache o seu {coral("morro de treino")}', 70, 28, 1.02),
        p("Aqui, é a Serrinha: o lugar que mais soma altimetria e fica perto de casa. Logística boa vale mais que o morro perfeito longe.", 26),
        box_glow(f'Treino que você consegue repetir {amber("toda semana")} ganha do treino épico uma vez por mês.', 34, 31),
        GROW,
        foot(src(STRAVA)),
    ]),
    card(TT, 5, NT, 4, [
        pill_line("O que mudou"),
        h(f'Parei de {coral("recomeçar")} a cada prova', 66, 28, 1.02),
        p("Antes, cada prova era um ciclo novo. Agora o plano mira um objetivo só, e cada prova é um degrau dele.", 26),
        '    <div style="margin-top: 32px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "La Misión Serra Fina · 36,87 km", 29),
        mark_row(True, "KTR Campos do Jordão · 30 km", 29),
        mark_row(True, "Paraty Brazil by UTMB · 2026", 29),
        '    </div>',
        GROW,
        foot(src(STRAVA)),
    ]),
    card(TT, 6, NT, 5, [
        pill_line("Próximo degrau"),
        big("50K+", "a meta", "uma ultra até agosto de 2027. A prova-alvo é a La Misión 55K.", 40),
        box_dashed(f'{b("E não vou sozinho:")} a Débora vai nos 18 km. Objetivo e família na mesma prova.', 40),
        GROW,
        foot("Planejamento pessoal 2027."),
    ]),
    card(TT, 7, NT, 0, [
        stamp("Bora junto?"),
        h(f'Você corre em cidade plana {coral("também?")}', 64, 36, 1.04),
        p("Salva esse post pro próximo treino e me conta onde você caça subida aí.", 24),
        GROW,
        ask("Onde você treina subida?", "Comenta o nome do lugar."),
        foot("Relato pessoal · Rico e Débora", 22),
    ]),
]

# ---------------------------------------------------------------- DJI Neo 2 (produto, sem link)
TD = "Usos do DJI Neo 2"
ND = 8
FONTE = "DJI (lançamento, nov/2025) e ficha técnica do varejo, checadas em 12/10/2026."
DJI = [
    card(TD, 1, ND, 4, [
        pill_solid("Publi · drone compacto"),
        f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: 82px; font-weight: 700; line-height: 1; text-shadow: 0 0 36px rgba(255,107,74,0.4)">6 usos do DJI Neo 2 pra quem {coral("nunca pilotou")}</h1>',
        p("Decola da mão, segue você sozinho e grava em vertical. Veja onde ele faz sentido.", 26, 33),
        GROW,
        cta("Arrasta e escolhe o seu"),
        foot(src(FONTE), 22),
    ]),
    card(TD, 2, ND, 1, [
        pill_line("Uso 1: corrida, trilha e pedal"),
        h(f'Ele te {amber("segue")} sozinho', 70, 28, 1.02),
        big("12 m/s", "de acompanhamento", "em áreas abertas, com o ActiveTrack, em 8 direções."),
        box_dashed(f'{b("Sem controle na mão:")} você corre, ele filma.', 36),
        GROW,
        foot(src(FONTE)),
    ]),
    card(TD, 3, ND, 2, [
        pill_line("Uso 2: viagem"),
        h(f'Decola e pousa {coral("na palma da mão")}', 66, 28, 1.02),
        p("Sem procurar chão plano pra decolar. E o \"Retorno para a palma\" faz ele achar sua mão e pousar de volta.", 26),
        box_glow(f'Ideal pra mirante, praia e topo de trilha.', 34, 31),
        GROW,
        foot(src(FONTE)),
    ]),
    card(TD, 4, ND, 3, [
        pill_line("Uso 3: foto de grupo"),
        h(f'Selfie {amber("sem pau de selfie")}', 70, 28, 1.02),
        '    <div style="margin-top: 32px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "<strong>SelfieShot:</strong> foto e vídeo sem usar as mãos"),
        mark_row(True, "<strong>Gestos:</strong> a palma guia o drone pra cima, pra baixo e pros lados"),
        mark_row(True, "<strong>Voz e app</strong> também controlam"),
        '    </div>',
        GROW,
        foot(src(FONTE)),
    ]),
    card(TD, 5, ND, 0, [
        pill_line("Uso 4: conteúdo pro TikTok"),
        h(f'Grava {coral("em pé")}, já no formato', 68, 28, 1.02),
        big("2,7K", "vertical", "direto do drone, sem cortar o vídeo depois."),
        box_dashed(f'{b("E na horizontal:")} 4K a 60 fps, com gimbal de 2 eixos.', 36),
        GROW,
        foot(src(FONTE)),
    ]),
    card(TD, 6, ND, 5, [
        pill_line("Uso 5: câmera lenta"),
        h(f'Salto, chegada, {amber("respingo")}', 68, 28, 1.02),
        big("4K/100", "fps", "pra câmera lenta com resolução alta."),
        GROW,
        foot(src(FONTE)),
    ]),
    card(TD, 7, ND, 1, [
        pill_line("Uso 6: primeiro drone"),
        h(f'Feito pra {coral("errar menos")}', 70, 28, 1.02),
        '    <div style="margin-top: 32px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "<strong>Detecção de obstáculos</strong> em todas as direções, com LiDAR na frente"),
        mark_row(True, "<strong>19 minutos</strong> de voo por bateria"),
        mark_row(True, "<strong>49 GB</strong> de armazenamento interno"),
        '    </div>',
        box_dashed(f'{b("Antes de voar:")} confira as regras de voo da ANAC e do DECEA.', 30),
        GROW,
        foot(src(FONTE)),
    ]),
    card(TD, 8, ND, 2, [
        stamp("Sua vez"),
        h(f'Qual desses usos {amber("é a sua cara?")}', 66, 36, 1.04),
        p("Salva pra lembrar na próxima viagem. Os modelos e combos mudam de loja pra loja: confira o que vem no kit antes de comprar.", 24),
        GROW,
        ask("Corrida, viagem ou selfie?", "Comenta o número do uso."),
        foot(src(FONTE), 22),
    ]),
]

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
for i, html in enumerate(TRAIL, 1):
    (OUT / f"Trail_{i}.dc.html").write_text(html, encoding="utf-8")
for i, html in enumerate(DJI, 1):
    (OUT / f"DJI_{i}.dc.html").write_text(html, encoding="utf-8")
print(len(TRAIL), "Trail;", len(DJI), "DJI")
