"""Carrossel da R&D de 13/10/2026 13h: caso real de 'Promoção de produto inconsistente'.
Reaproveita os componentes do padrão neon quente de gen_1210.py.
Uso: python3 gen_1310.py <pasta project/ de saída>"""
import pathlib
import sys

_src = (pathlib.Path(__file__).parent / "gen_1210.py").read_text(encoding="utf-8")
exec(_src.split("# ---------------------------------------------------------------- Carrossel A")[0])

T = "Produto inconsistente"
N = 7
AVISO = "aviso de violação do TikTok Shop no app, recebido em 12/10/2026."

CARDS = [
    card(T, 1, N, 0, [
        pill_solid("Caso real da R&amp;D"),
        f'    <h1 style="margin: 30px 0 0; {FRED}; font-size: 84px; font-weight: 700; line-height: 1; text-shadow: 0 0 36px rgba(255,107,74,0.4)">Mostrei o produto real. {coral("E tomei violação.")}</h1>',
        f'    <div style="margin-top: 26px; font-size: 33px; line-height: 1.34; color: {SOFT}">Motivo: <strong style="color: #FFF3EC">Promoção de produto inconsistente.</strong> Fui frase por frase descobrir onde errei.</div>',
        stamp("Violação", 54),
        GROW,
        cta("Arrasta e não repete o erro"),
        foot(f'Base: <strong style="color: {AMBER}">{AVISO}</strong>', 22),
    ]),
    card(T, 2, N, 1, [
        pill_line("O que o TikTok confere"),
        h(f'Seu vídeo é comparado com o {amber("produto do link")}', 64, 28, 1.04),
        '    <div style="margin-top: 34px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(True, "<strong>Tipo, tamanho e peso</strong>"),
        mark_row(True, "<strong>Imagens e logotipos</strong>"),
        mark_row(True, "<strong>Ofertas promocionais</strong> (ex.: \"compre 1, ganhe 1\")"),
        '    </div>',
        box_dashed(f'{b("Leitura nossa:")} conta tudo o que está no conteúdo. O que aparece, o que é falado, a legenda e a capa.', 32),
        GROW,
        foot(src(AVISO)),
    ]),
    card(T, 3, N, 2, [
        pill_line("Erro 1: a origem"),
        h(f'A fala disse uma coisa. {coral("A caixa, outra.")}', 64, 28, 1.04),
        '    <div style="margin-top: 34px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(False, "Na fala: <strong>\"veio do Japão para o Brasil\"</strong>"),
        mark_row(True, "Na caixa: <strong>\"Formulado no Japão\"</strong>"),
        mark_row(False, "Também na caixa: <strong>\"País de origem: R.P.C\"</strong> (China)"),
        '    </div>',
        box_glow(f'Formulado em ≠ fabricado em ≠ {amber("veio de.")}', 34, 34),
        GROW,
        foot(src("embalagem do produto (frente, verso e laterais), conferida em 12/10/2026.")),
    ]),
    card(T, 4, N, 3, [
        pill_line("Erro 2: quantidade"),
        h(f'"Olha quantas {coral("eu comprei!")}"', 70, 28, 1.02),
        '    <div style="margin-top: 34px; display: flex; flex-direction: column; gap: 14px">',
        mark_row(False, "No vídeo: <strong>uma pilha de caixas</strong> atrás da bisnaga"),
        mark_row(False, "No link: <strong>1 unidade</strong>"),
        mark_row(False, "E a fala era em 1ª pessoa num vídeo <strong>marcado como IA</strong>"),
        '    </div>',
        box_dashed(f'{b("Regra:")} mostre a mesma quantidade do link. E persona de IA não diz "comprei", "usei" ou "gostei".', 32),
        GROW,
        foot(src(AVISO)),
    ]),
    card(T, 5, N, 4, [
        pill_line("Erro 3: a capa"),
        h(f'A capa {coral("não era foto")} do produto', 70, 28, 1.02),
        f'    <div style="margin-top: 26px; font-size: 32px; line-height: 1.34; color: {SOFT}">Era uma imagem feita por IA, com a bisnaga num pódio e respingos. Bonita, mas não é o produto do anúncio.</div>',
        box_glow(f'A capa é a primeira {amber("imagem do produto")} que o revisor vê.', 36, 32),
        box_dashed(f'{b("Regra:")} capa = um quadro real do próprio vídeo.', 26),
        GROW,
        foot(src(AVISO)),
    ]),
    card(T, 6, N, 1, [
        pill_line("O que estava certo"),
        h(f'O resto estava {amber("escrito na embalagem")}', 64, 28, 1.04),
        '    <div style="margin-top: 32px; display: flex; flex-direction: column; gap: 12px">',
        mark_row(True, "<strong>\"Clareador\"</strong>: na frente e explicado no verso", 28),
        mark_row(True, "<strong>Roxo neutraliza o amarelado</strong>: na lateral", 28),
        mark_row(True, "<strong>Nano-hidroxiapatita e flúor</strong>: na frente", 28),
        mark_row(True, "<strong>Sabor refrescante</strong>: no verso", 28),
        '    </div>',
        box_dashed(f'{b("E virou prova:")} as fotos da caixa foram junto no recurso.', 28),
        GROW,
        foot(src("embalagem do produto, conferida em 12/10/2026.")),
    ]),
    card(T, 7, N, 5, [
        stamp("Regra de ouro"),
        h(f'Se não está na embalagem ou no anúncio, {coral("não sai da sua boca.")}', 62, 36, 1.06),
        f'    <div style="margin-top: 24px; font-size: 27px; line-height: 1.35; color: {SOFT}">Sem a caixa em mãos? Use o título, a descrição e as fotos do anúncio. Se nada confirma, a frase fica de fora.</div>',
        GROW,
        ask("Já tomou essa violação?", "Comenta o que o aviso dizia."),
        foot(src("aviso de violação no app e embalagem do produto · checado em 12/10/2026."), 22),
    ]),
]

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
for i, html in enumerate(CARDS, 1):
    (OUT / f"Inconsistente_{i}.dc.html").write_text(html, encoding="utf-8")
print(len(CARDS), "cards")
