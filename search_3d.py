import re

with open('modelo03_comFotos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find arrows
matches = re.findall(r'<.*?>.*?<.*?>', content)
# actually let's just search for CSS that has 3D transform or 'translateZ'
transforms = re.findall(r'[^}]*transform[^}]*{[^}]+}', content)
with open('transforms.txt', 'w', encoding='utf-8') as f:
    for t in transforms:
        f.write(t.strip() + '\n')
