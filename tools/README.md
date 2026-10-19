# Ferramentas dos cards

- `gen_2010.py`: carrosséis da rotina de 20/10/2026 (6h live que vende sem janelinha, 18h música de streaming na live).
- `gen_1510.py`: carrosséis da rotina de 15/10/2026 (persona de IA sem rótulo, postado às 13h; 3 formatos que vendem, 18h).
- `gen_trail_parte2.py`: trail parte 2 de 14/10/2026 13h (a semana de subida, dia a dia); fotos recortadas dos cards aprovados de 13/10.
- `gen_1410.py`: carrosséis da rotina de 14/10/2026 (6h Informações de Pesquisas, 18h roteiro de 1 minuto).
- `gen_1310_rotina.py`: carrosséis da rotina de 13/10/2026 (6h perfil, 18h marca d’água).
- `gen_1210.py`: gera os artboards `.dc.html` dos carrosséis de 12/10/2026 (modelo para os próximos).
- `render.js`: renderiza artboards `.dc.html` em JPG 1080×1440 e acusa texto fora da área segura
  (150 px no topo, 170 px à direita).

Uso:

```
npm install            # dentro de tools/, baixa as fontes Fredoka e Nunito
python3 gen_1210.py <saida>/project
node render.js <saida>/project <pasta-jpg> <prefixo> Arquivo_1.dc.html Arquivo_2.dc.html ...
```

`render.js` precisa do pacote `playwright` com Chromium disponível.
