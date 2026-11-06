"""Restore the currently published 106-slide por/para lesson from the source HTML.
Run: python build_por_para_lesson.py
"""
from pathlib import Path
from shutil import copyfile
root = Path(__file__).resolve().parent
copyfile(root / 'source' / 'por_para_106_slides.html', root / 'por_para_practice.html')
print('Updated', root / 'por_para_practice.html')
