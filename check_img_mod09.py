import re

with open('modelo09.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all base64 images and print 100 characters before and after to see context
for m in re.finditer(r'<img[^>]+src="data:image/[^;]+;base64,([^"]+)"[^>]*>', content):
    start = max(0, m.start() - 150)
    end = min(len(content), m.end() + 150)
    print("CONTEXT:")
    print(content[start:m.start()])
    print("<img src='base64...'>")
    print(content[m.end():end])
    print("-" * 50)
