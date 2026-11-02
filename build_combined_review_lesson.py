"""Rebuild combined_review.html after editing source/combined_review_lesson.json.
Run: python build_combined_review_lesson.py
"""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
source=root/'source'/'combined_review_lesson.json'
template=root/'source'/'combined_review_lesson_template.html'
output=root/'combined_review.html'
data=json.loads(source.read_text(encoding='utf8'))
items=data['items']
assert len(set(x['item_id'] for x in items))==len(items), 'Duplicate IDs'
assert all(x['target_span'].casefold() in x['spanish'].casefold() for x in items), 'Missing target span'
assert all(x['kind'] in ('main','review') for x in items)
assert all(sum(j['kind']=='review' and j['stage_id']==i['stage_id'] for j in items)>=2 for i in items if i['kind']=='main'), 'Missing extra review examples'
embedded=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
html=template.read_text(encoding='utf8').replace('__LESSON_DATA__',embedded)
assert '__LESSON_DATA__' not in html
output.write_text(html,encoding='utf8')
print('Updated',output)
