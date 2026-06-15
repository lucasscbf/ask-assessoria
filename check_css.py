import re
import json

def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    m_temp = re.search(r'<script type="__bundler/template">(.*?)</script>', content, re.DOTALL)
    if m_temp:
        t = json.loads(m_temp.group(1).strip())
        return t
    return None

t2 = get_data('modelo02__foto_hero_comfotos.html')
t3 = get_data('modelo03_comFotos.html')

if t2 and t3:
    css2 = re.findall(r'#hero-foto[^{]*{[^}]+}', t2)
    css3 = re.findall(r'#hero-foto[^{]*{[^}]+}', t3)
    
    with open('hero_css_compare.txt', 'w', encoding='utf-8') as f:
        f.write("--- modelo02 CSS ---\n")
        f.write('\n'.join(css2) + '\n\n')
        f.write("--- modelo03 CSS ---\n")
        f.write('\n'.join(css3) + '\n')
    print("CSS comparison written to hero_css_compare.txt")
else:
    print("Files not found")
