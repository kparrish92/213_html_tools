"""Rebuild the standalone irregular present-subjunctive trainer after editing JSON.

From this directory: python build_irregular_subjunctive.py
"""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
source=root/'source'/'irregular_subjunctive_lesson.json'
template=root/'source'/'irregular_subjunctive_template.html'
data=json.loads(source.read_text(encoding='utf-8'))
ids={i['item_id'] for i in data['items']}
assert len(ids)==len(data['items']), 'Duplicate item_id values'
assert all(x['target_span'].casefold() in x['spanish'].casefold() for x in data['items']), 'Incorrect target span in Spanish'
assert all(i in ids for stage in data['stages'] for i in stage['main_ids']+stage['review_ids']), 'Stage references missing item'
embedded=json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</','<' + chr(92) + '/')
html=template.read_text(encoding='utf-8').replace('__IRREGULAR_SUBJUNCTIVE_DATA__',embedded)
assert '__IRREGULAR_SUBJUNCTIVE_DATA__' not in html
output=root/'irregular_subjunctive_practice.html'
output.write_text(html,encoding='utf-8')
print(f'Wrote {output}; {sum(i["kind"]=="main" for i in data["items"])} practice + {sum(i["kind"]=="review" for i in data["items"])} review trials')
