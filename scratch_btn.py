import re
import json

with open('modelo03_comFotos.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<script type="__bundler/template">(.*?)</script>', content, re.DOTALL)
template = json.loads(m.group(1).strip())

# Find ALL btn--wa occurrences with context
with open('btn_search.txt', 'w', encoding='utf-8') as out:
    for m2 in re.finditer(r'btn--wa', template):
        idx = m2.start()
        # Get surrounding context
        ctx = template[max(0,idx-150):idx+200]
        out.write(f"@{idx}:\n{ctx}\n{'='*80}\n\n")
    
    # Also search for .btn class (without --wa) to see how they look
    out.write("\n\n=== CSS definitions for .btn and .btn--wa ===\n")
    for m2 in re.finditer(r'\.btn[^{]*\{[^}]+\}', template):
        out.write(f"@{m2.start()}: {m2.group()}\n\n")

print("Saved to btn_search.txt")
