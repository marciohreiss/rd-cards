"""Monta um vídeo educativo 9:16 (1080x1920) da R&D a partir de um roteiro em cenas:
1) narra cada frase com o Kokoro (voz aberta, roda local), 2) calcula o tempo de cada trecho,
3) escreve o index.html com todas as animações amarradas a esses tempos.
Uso: python3 build_video.py <pasta-modelos> <pasta-fontes-@fontsource> <pasta-saida> [voz] [velocidade]
Saída: narracao.wav, tempos.json, index.html"""
import base64
import json
import pathlib
import sys

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

MODELS, FONTS, OUT = (pathlib.Path(p) for p in sys.argv[1:4])
VOICE = sys.argv[4] if len(sys.argv) > 4 else "pf_dora"
SPEED = float(sys.argv[5]) if len(sys.argv) > 5 else 1.06
OUT.mkdir(parents=True, exist_ok=True)
SR = 24000
LEAD, GAP_SENT, GAP_SCENE, TAIL = 0.30, 0.20, 0.50, 1.40

# ------------------------------------------------------------------ roteiro
# cena -> frases -> trechos (legenda, fala [None = igual à legenda], deixa visual)
# Texto tirado do carrossel "Antes do primeiro link" (checado em 11/10/2026).
SCENES = [
    ("s1", [
        [("Vai colocar seu primeiro link de afiliado", None, "h1"), ("no TikTok Shop?", None, None)],
        [("Então faz esses 4 passos", "Então faz esses quatro passos", "dots"), ("na ordem certa,", None, "sub"),
         ("pra não travar na análise", None, None), ("nem ficar sem sacar a comissão.", None, None)],
    ]),
    ("s2", [
        [("Passo 1:", "Passo um:", "b"), ("confere se você entra.", None, "h")],
        [("A conta precisa ter", None, None), ("no mínimo 1.000 seguidores,", "no mínimo mil seguidores,", "big"),
         ("você precisa ter 18 anos ou mais", "você precisa ter dezoito anos ou mais", "r1"),
         ("e não pode ter tido permissão", None, "r2"), ("de e-commerce revogada antes.", "de i-cômers revogada antes.", None)],
        [("Conta ligada a outra que perdeu a permissão", None, "note"), ("também fica de fora.", None, None)],
    ]),
    ("s3", [
        [("Passo 2:", "Passo dois:", "b"), ("faz a inscrição pelo aplicativo.", None, "h")],
        [("Abre o seu Perfil,", None, "p1"), ("toca nas três linhas do menu,", None, "p2"),
         ("entra em TikTok Studio", "entra em TikTok Estúdio", "p3"),
         ("e toca em TikTok Shop para criadores.", None, "p4")],
        [("Confere os requisitos", None, "p5"), ("e toca em Inscrever-se.", None, None)],
        [("Depois é aguardar:", None, "box"), ("a resposta da análise", None, None), ("chega por notificação.", None, None)],
    ]),
    ("s4", [
        [("Passo 3:", "Passo três:", "b"), ("verifica a identidade.", None, "h")],
        [("Depois da aprovação,", None, "sub"), ("a Central de criadores", None, None), ("mostra o botão Verificar.", None, None)],
        [("Separa o CPF,", "Separa o cê pê éfe,", "d1"),
         ("um documento válido: RG, CNH ou RNE,", "um documento válido: érre gê, cê êne agá ou érre êne é,", "d2"),
         ("seu nome e data de nascimento", None, "d3"), ("e as informações fiscais.", None, "d4")],
        [("Sem verificação,", None, "glow"), ("não dá pra ganhar", None, None), ("nem sacar comissão.", None, None)],
    ]),
    ("s5", [
        [("Passo 4:", "Passo quatro:", "b"), ("arruma a casa antes de postar.", None, "h")],
        [("Olha a Saúde da Conta", None, "i1"), ("pra ver se tem ponto de violação.", None, None)],
        [("Escolhe o produto na seção", None, "i2"), ("Encontre produtos para promover.", None, None)],
        [("E liga a chave", None, "i3"), ("Divulgar conteúdo comercial", None, None), ("em todo vídeo com link.", None, None)],
    ]),
    ("s6", [
        [("Cumpriu tudo", None, "h"), ("e não foi aprovado?", None, None)],
        [("A própria Academia do TikTok Shop orienta", None, "txt"), ("abrir um tíquete pra investigação.", None, "box")],
        [("Em qual passo você está?", None, "ask"), ("Comenta o número aqui embaixo.", None, "ask2")],
    ]),
]

# ------------------------------------------------------------------ narração
kokoro = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))


def weight(text):
    return max(1, len(kokoro.tokenizer.phonemize(text, "pt-br").replace(" ", "")))


def trim(x, thr=0.012, pad=0.03):
    idx = np.where(np.abs(x) > thr)[0]
    if not len(idx):
        return x
    a = max(0, idx[0] - int(pad * SR))
    b = min(len(x), idx[-1] + int(pad * SR))
    return x[a:b]


audio = [np.zeros(int(LEAD * SR), dtype=np.float32)]
t = LEAD
caps, cues, scene_in = [], {}, {}
for sid, sents in SCENES:
    scene_in[sid] = max(0.0, t - 0.28)
    for sent in sents:
        spoken = " ".join(b[1] or b[0] for b in sent)
        samples, sr = kokoro.create(spoken, voice=VOICE, speed=SPEED, lang="pt-br")
        assert sr == SR
        samples = trim(np.asarray(samples, dtype=np.float32))
        dur = len(samples) / SR
        ws = [weight(b[1] or b[0]) for b in sent]
        acc = 0.0
        for (cap, _, cue), w in zip(sent, ws):
            a = t + dur * acc / sum(ws)
            acc += w
            b_ = t + dur * acc / sum(ws)
            caps.append({"a": round(a, 3), "b": round(b_, 3), "text": cap, "scene": sid})
            if cue:
                cues[f"{sid}.{cue}"] = round(a, 3)
        audio.append(samples)
        audio.append(np.zeros(int(GAP_SENT * SR), dtype=np.float32))
        t += dur + GAP_SENT
    audio.append(np.zeros(int((GAP_SCENE - GAP_SENT) * SR), dtype=np.float32))
    t += GAP_SCENE - GAP_SENT
audio.append(np.zeros(int(TAIL * SR), dtype=np.float32))
TOTAL = t + TAIL
wav = np.concatenate(audio)
wav = wav / max(1e-6, float(np.abs(wav).max())) * 0.89
sf.write(OUT / "narracao.wav", wav, SR)
# legenda fica na tela até a próxima começar (dentro da cena)
for i, c in enumerate(caps[:-1]):
    nxt = caps[i + 1]
    c["b"] = nxt["a"] if nxt["scene"] == c["scene"] else round(c["b"] + 0.15, 3)
ids = [s for s, _ in SCENES]
scene_out = {s: (scene_in[ids[i + 1]] if i + 1 < len(ids) else TOTAL + 1) for i, s in enumerate(ids)}
json.dump({"total": round(TOTAL, 3), "scene_in": scene_in, "cues": cues, "caps": caps, "voice": VOICE, "speed": SPEED},
          open(OUT / "tempos.json", "w"), ensure_ascii=False, indent=1)
print(f"narração: {TOTAL:.1f}s · {len(caps)} legendas · voz {VOICE} · velocidade {SPEED}")

# ------------------------------------------------------------------ visual
A, AMBER, INK, MUTED, SOFT, TXT = "#FF6B4A", "#FFB547", "#17080D", "#D9B9AC", "#E6CFC6", "#FFF3EC"
FRED = "font-family:'Fredoka',sans-serif"
ICONS = {
    "pulse": '<path d="M3 12h4l3-8 4 16 3-8h4"></path>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path>',
    "toggle": '<rect x="1" y="6" width="22" height="12" rx="6"></rect><circle cx="16" cy="12" r="3"></circle>',
    "check": '<polyline points="20 6 9 17 4 12"></polyline>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>',
}


def svg(name, size, stroke, width=2.0):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def T(sid, cue, extra=0.0):
    return f"--t:{cues[f'{sid}.{cue}'] + extra:.3f}s"


def span_of(sid, cue):
    """duração em que a deixa fica 'ativa' (até a próxima deixa da cena ou 2,2 s)"""
    t0 = cues[f"{sid}.{cue}"]
    later = sorted(v for k, v in cues.items() if k.startswith(sid + ".") and v > t0)
    end = later[0] if later else min(t0 + 2.2, scene_out[sid])
    return max(0.6, end - t0)


def amber(x):
    return f'<span style="color:{AMBER}">{x}</span>'


def coral(x):
    return f'<span style="color:{A}">{x}</span>'


def badge(sid, n):
    return (f'<div class="pop badge" style="{T(sid, "b")}"><span class="num">{n}</span>Passo {n} de 4</div>')


def h(sid, html, size=88):
    return f'<h2 class="rise" style="{T(sid, "h")};font-size:{size}px">{html}</h2>'


def src(sid, text):
    return f'<div class="src fade" style="--t:{scene_in[sid] + 0.5:.3f}s"><strong>Fonte:</strong> {text}</div>'


def mark(sid, cue, html):
    return (f'<div class="pop mark" style="{T(sid, cue)}"><span class="ok">{svg("check", 30, INK, 3.4)}</span>'
            f'<div>{html}</div></div>')


def pstep(sid, n, html, last=False):
    cue = f"p{n}"
    return (f'<div class="pop" style="{T(sid, cue)}"><div class="pstep{" last" if last else ""} hl" '
            f'style="{T(sid, cue)};--d:{span_of(sid, cue):.3f}s"><span class="pn">{n}</span><div>{html}</div></div></div>')


def doc(sid, cue, label, sub):
    return (f'<div class="pop doc" style="{T(sid, cue)}"><div class="dl">{label}</div><div class="ds">{sub}</div></div>')


def irow(sid, cue, icon, title, text, coral_tile, rot):
    col = A if coral_tile else AMBER
    glow = "rgba(255,107,74,0.6)" if coral_tile else "rgba(255,181,71,0.55)"
    return (f'<div class="pop irow" style="{T(sid, cue)}"><div class="tile bob" style="background:{col};box-shadow:0 0 40px {glow};'
            f'--r:{rot}deg">{svg(icon, 64, INK, 2.1)}</div><div><div class="it">{title}</div><div class="ix">{text}</div></div></div>')


def scene(sid, body, source):
    return (f'<section class="scene" id="{sid}" style="--in:{scene_in[sid]:.3f}s;--out:{scene_out[sid] - 0.22:.3f}s">'
            f'<div class="content">{body}</div>{src(sid, source)}</section>')


SHOP_REG = "Academia do TikTok Shop, como se registrar como criador afiliado (15/07/2025)."
dots = "".join(
    f'<div class="pop dotc" style="{T("s1", "dots", i * 0.16)}"><div class="dn{" on" if i == 0 else ""}">{i + 1}</div>'
    f'<div class="dlb">{lab}</div></div>'
    for i, lab in enumerate(["Conferir", "Inscrever", "Verificar", "Preparar"]))

S = {}
S["s1"] = scene("s1", f'''
  <div class="pop pill" style="--t:0.15s">TikTok Shop do zero</div>
  <h1 class="rise" style="{T("s1", "h1")}">Antes do {coral("primeiro link de afiliado")}</h1>
  <div class="fade sub" style="{T("s1", "sub")}">4 passos na ordem certa, pra não travar na análise nem ficar sem sacar a comissão.</div>
  <div class="dots">{dots}</div>
''', "Academia do TikTok Shop · checado em 11/10/2026.")

S["s2"] = scene("s2", f'''
  {badge("s2", 1)}
  {h("s2", f"Confere se você {amber('entra')}", 96)}
  <div class="bigrow">
    <div class="zoom big" style="{T("s2", "big")}">1.000</div>
    <div class="fade" style="{T("s2", "big", 0.25)}"><div class="bl">seguidores</div><div class="bs">é o mínimo na conta</div></div>
  </div>
  <div class="marks">
    {mark("s2", "r1", "<strong>18 anos</strong> ou mais.")}
    {mark("s2", "r2", "Nenhuma permissão de e-commerce <strong>revogada antes.</strong>")}
  </div>
  <div class="fade note" style="{T("s2", "note")}">Conta ligada a outra que perdeu a permissão também fica de fora.</div>
''', "Política de Elegibilidade de Criadores do TikTok Shop, Brasil (01/07/2026).")

S["s3"] = scene("s3", f'''
  {badge("s3", 2)}
  {h("s3", f"Faz a {amber('inscrição')} pelo app", 74)}
  <div class="psteps">
    {pstep("s3", 1, "Abra o seu <b>Perfil</b>")}
    {pstep("s3", 2, "Toque nas <b>três linhas</b> do menu")}
    {pstep("s3", 3, "Entre em <b>TikTok Studio</b>")}
    {pstep("s3", 4, "Toque em <b>TikTok Shop para criadores</b>")}
    {pstep("s3", 5, "Confira os requisitos e toque em <b>Inscrever-se</b>", True)}
  </div>
  <div class="pop dashed" style="{T("s3", "box")}"><b>Depois é aguardar.</b> A resposta da análise chega por notificação.</div>
''', SHOP_REG)

S["s4"] = scene("s4", f'''
  {badge("s4", 3)}
  {h("s4", f"Verifica a {amber('identidade')}", 84)}
  <div class="fade sub2" style="{T("s4", "sub")}">Depois da aprovação, a Central de criadores mostra o botão <strong>Verificar</strong>. Separe:</div>
  <div class="docs">
    {doc("s4", "d1", "CPF", "informe o número")}
    {doc("s4", "d2", "Documento", "RG, CNH ou RNE válido")}
    {doc("s4", "d3", "Seus dados", "nome e data de nascimento")}
    {doc("s4", "d4", "Fiscal", "informações fiscais")}
  </div>
  <div class="pop glowbox" style="{T("s4", "glow")}">Sem verificação, {amber("não dá pra ganhar nem sacar comissão.")}</div>
''', "Academia do TikTok Shop: registro de criador (15/07/2025) e Política de Elegibilidade (01/07/2026).")

S["s5"] = scene("s5", f'''
  {badge("s5", 4)}
  {h("s5", f"Arruma a casa {amber('antes de postar')}", 88)}
  <div class="irows">
    {irow("s5", "i1", "pulse", "Saúde da Conta", "Veja na Central de criadores se há ponto de violação.", True, -6)}
    {irow("s5", "i2", "bag", "Produto pra promover", "A Central de criadores tem a seção Encontre produtos para promover.", False, 5)}
    {irow("s5", "i3", "toggle", "Divulgar conteúdo comercial", "Ligue a chavinha em todo vídeo com link.", True, -4)}
  </div>
''', "Academia do TikTok Shop, Central de criadores (14/04/2025), e Central de Ajuda para Negócios do TikTok (abr/2026).")

S["s6"] = scene("s6", f'''
  <div class="pop stamp" style="--t:{scene_in["s6"] + 0.1:.3f}s">E se travar?</div>
  {h("s6", f"Cumpriu tudo e {coral('não foi aprovado?')}", 92)}
  <div class="pop amberbox" style="{T("s6", "box")}">Dá pra abrir um tíquete pra investigação.</div>
  <div class="fade note" style="{T("s6", "txt")}">É o que a própria Academia do TikTok Shop orienta pra quem atende a todos os requisitos.</div>
  <div class="pop ask" style="{T("s6", "ask")}"><div class="bob askic">{svg("chat", 60, INK, 2.2)}</div>
    <div><div class="aq">Em qual passo você está?</div><div class="fade aa" style="{T("s6", "ask2")}">Comenta o número.</div></div></div>
''', "Academia do TikTok Shop (abr/2025, jul/2025 e jul/2026) · checado em 11/10/2026.")

bars = "".join(
    f'<div class="bar"><i style="--t:{scene_in[s]:.3f}s;--d:{scene_out[s] - scene_in[s] if s != ids[-1] else TOTAL - scene_in[s]:.3f}s"></i></div>'
    for s in ids)
captions = "".join(
    f'<div class="cap" style="--a:{c["a"]:.3f}s;--b:{c["b"]:.3f}s"><span>{c["text"]}</span></div>' for c in caps)


def face(family, pkg, w):
    data = (FONTS / pkg / "files" / f"{pkg}-latin-{w}-normal.woff2").read_bytes()
    return (f'@font-face{{font-family:"{family}";font-weight:{w};font-style:normal;'
            f'src:url(data:font/woff2;base64,{base64.b64encode(data).decode()}) format("woff2")}}')


fonts = "\n".join([face("Fredoka", "fredoka", w) for w in (500, 600, 700)] + [face("Nunito", "nunito", w) for w in (400, 700, 800)])

CSS = f'''
*{{box-sizing:border-box}} html,body{{margin:0}}
body{{width:1080px;height:1920px;overflow:hidden;background:{INK};color:{TXT};font-family:'Nunito',sans-serif;position:relative}}
.g{{position:absolute;border-radius:50%;filter:blur(10px)}}
.g1{{width:1300px;height:1100px;left:300px;top:-260px;background:radial-gradient(closest-side,rgba(255,107,74,.40),transparent);animation:d1 13s ease-in-out infinite alternate}}
.g2{{width:1250px;height:1150px;left:-520px;top:1050px;background:radial-gradient(closest-side,rgba(255,181,71,.26),transparent);animation:d2 17s ease-in-out infinite alternate}}
.g3{{width:900px;height:900px;left:-300px;top:260px;background:radial-gradient(closest-side,rgba(255,107,74,.16),transparent);animation:d2 11s ease-in-out infinite alternate-reverse}}
@keyframes d1{{from{{transform:translate(0,0) scale(1)}}to{{transform:translate(-190px,170px) scale(1.14)}}}}
@keyframes d2{{from{{transform:translate(0,0) scale(1)}}to{{transform:translate(210px,-150px) scale(1.1)}}}}
.dotsbg{{position:absolute;inset:-40px;background:radial-gradient(rgba(255,181,71,.11) 1.6px,transparent 2.2px) 0 0/36px 36px;animation:pan 30s linear infinite}}
@keyframes pan{{to{{transform:translate(36px,36px)}}}}
.brand{{position:absolute;left:68px;top:162px;display:flex;align-items:baseline;gap:16px}}
.brand b{{{FRED};font-size:58px;font-weight:700;color:{A};text-shadow:0 0 26px rgba(255,107,74,.6)}}
.brand span{{font-size:28px;font-weight:700;color:{MUTED}}}
.bars{{position:absolute;left:68px;top:248px;width:842px;display:flex;gap:10px}}
.bar{{flex:1;height:10px;border-radius:99px;background:rgba(255,181,71,.24);overflow:hidden}}
.bar i{{display:block;height:100%;width:100%;border-radius:99px;background:{AMBER};box-shadow:0 0 16px rgba(255,181,71,.7);transform-origin:left;transform:scaleX(0);animation:fill var(--d) linear both;animation-delay:var(--t)}}
@keyframes fill{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
.scene{{position:absolute;inset:0;opacity:0;animation:scin .32s ease both var(--in),scout .22s ease forwards var(--out)}}
@keyframes scin{{from{{opacity:0;transform:translateX(46px)}}to{{opacity:1;transform:none}}}}
@keyframes scout{{from{{opacity:1;transform:none}}to{{opacity:0;transform:translateX(-46px)}}}}
.content{{position:absolute;left:68px;top:312px;width:842px;display:flex;flex-direction:column;align-items:flex-start}}
.src{{position:absolute;left:68px;top:1246px;width:842px;border-top:2px solid rgba(255,181,71,.35);padding-top:12px;font-size:23px;line-height:1.3;color:{MUTED}}}
.src strong{{color:{AMBER}}}
.pop{{animation:pop .55s cubic-bezier(.2,1.5,.4,1) both;animation-delay:var(--t)}}
@keyframes pop{{from{{opacity:0;transform:translateY(46px) scale(.9)}}to{{opacity:1;transform:none}}}}
.rise{{animation:rise .6s cubic-bezier(.2,.9,.3,1) both;animation-delay:var(--t)}}
@keyframes rise{{from{{opacity:0;transform:translateY(60px)}}to{{opacity:1;transform:none}}}}
.fade{{animation:fade .5s ease both;animation-delay:var(--t)}}
@keyframes fade{{from{{opacity:0;transform:translateY(16px)}}to{{opacity:1;transform:none}}}}
.zoom{{animation:zoom .7s cubic-bezier(.2,1.6,.4,1) both;animation-delay:var(--t);transform-origin:left bottom}}
@keyframes zoom{{from{{opacity:0;transform:scale(.3)}}to{{opacity:1;transform:none}}}}
.bob{{animation:bob 3.2s ease-in-out infinite alternate}}
@keyframes bob{{from{{transform:rotate(var(--r,0deg)) translateY(-5px)}}to{{transform:rotate(calc(var(--r,0deg) * -0.6)) translateY(6px)}}}}
h1{{margin:34px 0 0;{FRED};font-size:122px;font-weight:700;line-height:.98;text-shadow:0 0 40px rgba(255,107,74,.4)}}
h2{{margin:24px 0 0;{FRED};font-weight:700;line-height:1;text-shadow:0 0 34px rgba(255,107,74,.3)}}
.pill{{{FRED};font-size:38px;font-weight:600;background:{A};color:{INK};border-radius:99px;padding:10px 32px;box-shadow:0 0 34px rgba(255,107,74,.55)}}
.sub{{margin-top:30px;font-size:44px;line-height:1.3;color:{SOFT}}}
.sub2{{margin-top:16px;font-size:36px;line-height:1.3;color:{SOFT}}} .sub2 strong{{color:{TXT}}}
.dots{{margin-top:54px;width:100%;display:grid;grid-template-columns:repeat(4,1fr);gap:8px}}
.dotc{{display:flex;flex-direction:column;align-items:center;gap:16px}}
.dn{{width:136px;height:136px;border-radius:50%;display:flex;align-items:center;justify-content:center;{FRED};font-size:72px;font-weight:700;border:4px solid {AMBER};color:{AMBER};background:rgba(23,8,13,.7)}}
.dn.on{{background:{A};border-color:{A};color:{INK};box-shadow:0 0 36px rgba(255,107,74,.65)}}
.dlb{{{FRED};font-size:36px;font-weight:600}}
.badge{{display:flex;align-items:center;gap:16px;{FRED};font-size:36px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:{AMBER};border:3px solid {AMBER};border-radius:99px;padding:8px 32px 8px 10px;background:rgba(23,8,13,.6);box-shadow:0 0 26px rgba(255,181,71,.4)}}
.badge .num{{display:flex;align-items:center;justify-content:center;width:58px;height:58px;border-radius:50%;background:{AMBER};color:{INK};font-size:38px;font-weight:700}}
.bigrow{{margin-top:36px;display:flex;align-items:flex-end;gap:26px}}
.big{{{FRED};font-size:236px;font-weight:700;line-height:.86;color:{AMBER};text-shadow:0 0 54px rgba(255,107,74,.75),0 0 130px rgba(255,107,74,.4)}}
.bl{{{FRED};font-size:52px;font-weight:700;line-height:1.05}} .bs{{margin-top:6px;font-size:34px;line-height:1.25;color:{SOFT}}}
.marks{{margin-top:44px;display:flex;flex-direction:column;gap:22px}}
.mark{{display:flex;align-items:center;gap:22px;font-size:42px;line-height:1.22}}
.ok{{flex:none;width:58px;height:58px;border-radius:50%;background:{AMBER};display:flex;align-items:center;justify-content:center;box-shadow:0 0 22px rgba(255,181,71,.6)}}
.note{{margin-top:28px;font-size:34px;line-height:1.32;color:{SOFT}}}
.psteps{{margin-top:30px;width:100%;display:flex;flex-direction:column;gap:12px}}
.pstep{{display:flex;align-items:center;gap:22px;border:3px solid rgba(255,243,236,.28);border-radius:26px;padding:12px 24px;background:rgba(23,8,13,.62);font-size:38px;line-height:1.2}}
.pstep b{{color:{TXT};font-weight:800}}
.pn{{flex:none;width:62px;height:62px;border-radius:50%;display:flex;align-items:center;justify-content:center;{FRED};font-size:34px;font-weight:700;border:3px solid {A};color:{A}}}
.pstep.last .pn{{background:{A};color:{INK};box-shadow:0 0 24px rgba(255,107,74,.6)}}
.hl{{animation:hl var(--d) ease both;animation-delay:var(--t)}}
@keyframes hl{{0%{{border-color:rgba(255,243,236,.28);box-shadow:none;background:rgba(23,8,13,.62)}}12%,86%{{border-color:{AMBER};box-shadow:0 0 34px rgba(255,181,71,.5);background:rgba(255,181,71,.16)}}100%{{border-color:rgba(255,243,236,.28);box-shadow:none;background:rgba(23,8,13,.62)}}}}
.dashed{{margin-top:18px;width:100%;border:3px dashed rgba(255,181,71,.7);border-radius:26px;padding:18px 26px;font-size:36px;line-height:1.28;color:{SOFT}}} .dashed b{{color:{TXT}}}
.docs{{margin-top:24px;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.doc{{border:3px solid rgba(255,181,71,.75);border-radius:28px;padding:17px 26px;background:rgba(23,8,13,.62)}}
.dl{{{FRED};font-size:48px;font-weight:700;line-height:1.08;color:{AMBER}}} .ds{{margin-top:6px;font-size:31px;line-height:1.25;color:{SOFT}}}
.glowbox{{margin-top:22px;width:100%;border:3px solid {A};border-radius:28px;padding:18px 28px;{FRED};font-size:42px;font-weight:600;line-height:1.16;background:rgba(255,107,74,.12);box-shadow:0 0 40px rgba(255,107,74,.4)}}
.irows{{margin-top:44px;display:flex;flex-direction:column;gap:40px}}
.irow{{display:flex;align-items:center;gap:30px}}
.tile{{flex:none;width:132px;height:132px;border-radius:34px;display:flex;align-items:center;justify-content:center}}
.it{{{FRED};font-size:48px;font-weight:700;line-height:1.08}} .ix{{margin-top:6px;font-size:34px;line-height:1.28;color:{SOFT}}}
.stamp{{{FRED};font-size:40px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:{A};border:4px solid {A};border-radius:18px;padding:8px 26px;transform:rotate(-4deg);box-shadow:0 0 30px rgba(255,107,74,.4)}}
.amberbox{{margin-top:34px;width:100%;border-radius:32px;padding:26px 32px;background:{AMBER};color:{INK};{FRED};font-size:54px;font-weight:700;line-height:1.1;box-shadow:0 0 44px rgba(255,181,71,.5)}}
.ask{{margin-top:44px;width:100%;display:flex;align-items:center;gap:28px;border:3px solid {A};border-radius:32px;padding:24px 28px;background:rgba(23,8,13,.66);box-shadow:0 0 36px rgba(255,107,74,.35)}}
.askic{{flex:none;width:112px;height:112px;border-radius:30px;background:{A};display:flex;align-items:center;justify-content:center}}
.aq{{{FRED};font-size:52px;font-weight:700;line-height:1.08}} .aa{{margin-top:6px;font-size:38px;color:{AMBER};font-weight:800}}
.caps{{position:absolute;left:68px;top:1332px;width:842px;height:170px}}
.cap{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;animation:capin .12s ease-out both var(--a),capout .08s linear forwards var(--b)}}
.cap span{{{FRED};font-size:50px;font-weight:600;line-height:1.14;text-align:center;color:#fff;text-wrap:balance;background:rgba(23,8,13,.86);border:2px solid rgba(255,181,71,.45);border-radius:28px;padding:14px 30px;box-shadow:0 10px 30px rgba(0,0,0,.45);max-width:842px}}
@keyframes capin{{from{{opacity:0;transform:translateY(12px) scale(.96)}}to{{opacity:1;transform:none}}}}
@keyframes capout{{to{{opacity:0}}}}
'''

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>R&D — Antes do primeiro link</title>
<style>{fonts}{CSS}</style></head><body>
<div class="g g1"></div><div class="g g2"></div><div class="g g3"></div><div class="dotsbg"></div>
<div class="brand"><b>R&amp;D</b><span>Rico e Débora</span></div>
<div class="bars">{bars}</div>
{"".join(S[s] for s in ids)}
<div class="caps">{captions}</div>
<script>
window.TOTAL = {TOTAL:.3f};
window.seek = (t) => {{ for (const a of document.getAnimations()) {{ a.pause(); a.currentTime = t * 1000; }} }};
</script></body></html>'''
(OUT / "index.html").write_text(html, encoding="utf-8")
print("index.html pronto;", "cenas:", {k: round(v, 2) for k, v in scene_in.items()})
