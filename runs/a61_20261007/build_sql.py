# A61: the data write from final.json ({media id: [verified cut times in s]}).
#   python3 build_sql.py -> out/a61_has_cut.sql (guarded: ends in an exception when the count differs) + out/a61_has_cut_rollback.sql
import json, os
os.makedirs('out', exist_ok=True)
final = {int(k): v for k, v in json.load(open('final.json')).items() if v}
ids = sorted(final)
vals = ',\n'.join(f"({i}, '{{{','.join(f'{t:.2f}' for t in sorted(final[i]))}}}'::real[])" for i in ids)
sql = f"""-- A61: mark the {len(ids)} videos with a verified cut (media.has_cut, media.cut_times). Guarded.
begin;
do $$ begin
  if (select count(*) from public.media where has_cut) <> 0 then raise exception 'has_cut already set on some rows'; end if;
end $$;
with v(id, times) as (values
{vals})
update public.media m set has_cut = true, cut_times = v.times from v where m.id = v.id;
do $$ declare n int; begin
  select count(*) into n from public.media where has_cut;
  if n <> {len(ids)} then raise exception 'expected {len(ids)} rows with has_cut, got %', n; end if;
end $$;
commit;
"""
open('out/a61_has_cut.sql', 'w').write(sql)
open('out/a61_has_cut_rollback.sql', 'w').write(f"""-- A61 rollback of the data write: no video counts as cut (the columns stay; to drop them see the migration's header).
begin;
update public.media set has_cut = false, cut_times = null where has_cut;
commit;
""")
print(len(ids), 'rows')
