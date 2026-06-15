import re

with open('modelo09.html', 'r', encoding='utf-8') as f:
    content = f.read()

hero_section = re.search(r'<section[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</section>', content, re.DOTALL)
if hero_section:
    print("Hero section HTML:")
    print(hero_section.group(0))
else:
    print("Hero section not found using regex")

# Also let's print all <img> src paths in the file to see what images are currently used
imgs = re.findall(r'<img[^>]+src="([^"]+)"', content)
print("\nImages in file:")
print(imgs)
