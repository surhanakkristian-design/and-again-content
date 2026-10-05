# A45: the picture shape (pixel width / height) of a video, and the guarded shape update of a batch already built.
#   python3 shape.py <batch> [...]  -> out/<batch>_shape.sql (one transaction: width/height of every row of the batch that has
#   none yet; checks afterwards that every row of the batch has its shape), and adds "shape" to batches/<batch>.json.
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
_lab = None
def shape(i):
    p = f'{HERE}/frames/{i}/info.json'
    if os.path.exists(p):
        d = json.load(open(p)); return int(d['width']), int(d['height'])
    global _lab
    if _lab is None: _lab = json.load(open(f'{HERE}/data/lab10_shape.json'))
    d = _lab[str(i)]; return int(d['width']), int(d['height'])
def build(batch):
    bp = f'{HERE}/batches/{batch}.json'; b = json.load(open(bp)); ids = b['ids']
    vals = ',\n'.join(f'({i}, {w}, {h})' for i in ids for w, h in [shape(i)])
    allid = ','.join(str(i) for i in ids); f = f'out/{batch}_shape.sql'
    open(f'{HERE}/{f}', 'w').write(f"""begin;
-- A45 batch {batch}: picture shape (pixel width / height) of its {len(ids)} videos; only rows without a shape are touched.
update public.media_exercise_sets s set width = v.w, height = v.h, updated_at = now()
  from (values
{vals}
  ) as v(id, w, h)
 where s.media_id = v.id and s.width is null;
do $g$ begin
  if (select count(*) from public.media_exercise_sets where media_id in ({allid}) and width > 0 and height > 0) <> (select count(*) from public.media_exercise_sets where media_id in ({allid})) then raise exception 'A45 {batch} shape: a row has no shape after the update, rolled back'; end if;
end $g$;
commit;
""")
    b['shape'] = f; json.dump(b, open(bp, 'w'), indent=1)
    return f
if __name__ == '__main__':
    for batch in sys.argv[1:]: print(batch, build(batch))
