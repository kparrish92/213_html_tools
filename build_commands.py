"""Rebuild the standalone commands trainer from its editable JSON source.

Run from the Lección 4 folder: python build_commands.py
"""
from pathlib import Path
import json
root = Path(__file__).resolve().parent
source = root / 'source' / 'commands_lesson.json'
template = root / 'source' / 'commands_template.html'
output = root / 'commands_practice.html'
data = json.loads(source.read_text(encoding='utf-8'))
embedded = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = template.read_text(encoding='utf-8').replace('__COMMANDS_DATA__', embedded)
output.write_text(html, encoding='utf-8')
print(f'Wrote {output} ({len([i for i in data["items"] if i["kind"]=="main"])} main trials)')
