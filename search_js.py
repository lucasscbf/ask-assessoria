import re
import json
import base64
import gzip

with open('modelo03_comFotos.html', 'r', encoding='utf-8') as f:
    content = f.read()

m_mani = re.search(r'<script type="__bundler/manifest">(.*?)</script>', content, re.DOTALL)
if m_mani:
    m = json.loads(m_mani.group(1).strip())
    
    for uuid, info in m.items():
        if info.get('mime') in ['application/javascript', 'text/jsx']:
            data = base64.b64decode(info['data'])
            if info.get('compressed'):
                data = gzip.decompress(data)
            text = data.decode('utf-8', errors='replace')
            
            if 'athlete' in text or 'carousel' in text or 'slider' in text or 'stack' in text:
                print(f"\n--- JS Asset {uuid} ---")
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if 'athlete' in line or 'carousel' in line or 'slider' in line or 'stack' in line:
                        print(f"Line {i}: {line.strip()[:150]}")
