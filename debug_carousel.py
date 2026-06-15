import re
import json

filename = 'modelo03_comFotos.html'

with open(filename, 'r', encoding='utf-8') as f:
    html_content = f.read()

m_temp = re.search(r'<script type="__bundler/template">(.*?)</script>', html_content, re.DOTALL)
if m_temp:
    t = json.loads(m_temp.group(1).strip())
    
    start = t.find('<!-- ===================== ATLETAS CONFIRMADOS ===================== -->')
    end = t.find('<!-- ===================== RESULTADOS ===================== -->')
    if start != -1 and end != -1:
        print("--- HTML ---")
        print(t[start:start+1000])
        
    css = re.findall(r'[^}]*athletes-carousel[^}]*{[^}]+}', t)
    print("\n--- CSS ---")
    for c in css:
        print(c.strip())
