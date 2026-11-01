"""Gera o link de importação do Motor Stories a partir de um JSON {"sequencias":[...]}.
Uso: python3 gerar_link.py arquivo.json  -> imprime o link (cole no Motor vermelho com "Colar do Motor azul")."""
import json, sys, zlib, base64
dados = json.load(open(sys.argv[1], encoding='utf-8'))
if 'sequencias' not in dados: dados = {'sequencias': dados if isinstance(dados, list) else [dados]}
dados.setdefault('v', 1)
txt = json.dumps(dados, ensure_ascii=False)
c = zlib.compressobj(9, zlib.DEFLATED, -15)
raw = c.compress(txt.encode('utf-8')) + c.flush()
print('https://danielsoaresbarboza-debug.github.io/motor-storiesV2/postar/?c=' + base64.urlsafe_b64encode(raw).decode().rstrip('='))
