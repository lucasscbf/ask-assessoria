import re

with open('modelo10.html', 'r', encoding='utf-8') as f:
    content = f.read()

galeria = re.search(r'<section id="galeria".*?</section>', content, re.DOTALL)
if galeria:
    print(galeria.group(0))
else:
    print("Not found")
