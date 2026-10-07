# A61 part 3: A61_CUT_VIDEOS.csv from final.json + the live rows (word, level, part of speech, group, storage file, original).
import csv, json, os, subprocess, sys
final = {int(k): v for k, v in json.load(open('final.json')).items() if v}
ids = sorted(final)
sb = os.path.expanduser('~/Projects/and-again-a61/supabase/scripts/_sb.sh')
q = f"""select m.id, m.title, m.media_url, s.level, wc.word, wc.part_of_speech, g.name->>'en' grp, g.id gid
from media m join media_exercise_sets s on s.media_id = m.id
left join lateral (select concept_id from concept_media cm where cm.media_id = m.id order by cm.id limit 1) c on true
left join word_concepts wc on wc.id = c.concept_id left join media_groups g on g.id = m.group_id
where m.id in ({','.join(map(str, ids))}) order by m.id"""
rows = json.loads(subprocess.run(['bash', '-c', f'cd ~/Projects/and-again-a61 && source {sb} && sb_rows "$Q"'], env={**os.environ, 'Q': q}, capture_output=True, text=True, timeout=300).stdout)
orig = {}
for p in ['../a33_20261003/map.json', '../a34_20261003/map59.json']:
    for r in json.load(open(p)): orig[r['id']] = os.path.basename(r['src'])
json.dump(rows, open('cut_rows.json', 'w'))
with open('A61_CUT_VIDEOS.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['media_id', 'word', 'level', 'part_of_speech', 'group', 'storage_file', 'original_file', 'cut_times_s'])
    for r in rows:
        w.writerow([r['id'], r['word'], r['level'], r['part_of_speech'], f"{r['grp']} ({r['gid']})", 'Words/' + r['media_url'].split('/Words/')[-1] if '/Words/' in (r['media_url'] or '') else r['media_url'],
                    orig.get(r['id'], ''), ' '.join(f'{t:.2f}' for t in sorted(final[r['id']]))])
print(len(rows), 'rows of', len(ids))
