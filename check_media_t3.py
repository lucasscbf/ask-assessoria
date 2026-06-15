import re
import json

t3 = None
with open('modelo03_comFotos.html', 'r', encoding='utf-8') as f:
    content = f.read()
    m_temp = re.search(r'<script type="__bundler/template">(.*?)</script>', content, re.DOTALL)
    if m_temp:
        t3 = json.loads(m_temp.group(1).strip())

if t3:
    matches = re.findall(r'[^}]*media-img[^}]*{[^}]+}', t3)
    print("media-img rules in modelo03:")
    for m in matches:
        print(m.strip())
