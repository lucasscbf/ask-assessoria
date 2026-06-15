import re

with open('modelo09.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The script replaces the base64 images in order of their appearance
replacements = [
    'images/equipe_professores.png',  # 1. hero-card
    'images/logos (1).png',           # 2. floating-logo
    'images/alunos.png',              # 3. panel-image
    'images/logos (1).png'            # 4. mini-logo
]

def replace_base64(match):
    if not hasattr(replace_base64, "counter"):
        replace_base64.counter = 0
    
    if replace_base64.counter < len(replacements):
        replacement_src = replacements[replace_base64.counter]
        replace_base64.counter += 1
        # The match group 0 is the entire src attribute: src="data:..."
        # Let's preserve the img tag and only replace the src content
        return f'src="{replacement_src}"'
    return match.group(0)

# Match src="data:image...base64,..."
new_content = re.sub(r'src="data:image/[^;]+;base64,[^"]+"', replace_base64, content)

with open('modelo09.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Replaced {getattr(replace_base64, 'counter', 0)} base64 images.")
