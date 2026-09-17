import json, subprocess, os
SB=os.path.expanduser('~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase')
out=[]
for lo,hi in [(1,6),(7,11),(12,19),(20,26),(31,40),(41,49),(50,58),(59,67)]:
    sql=f"""select e.id, e.exercise_type_id as type_id, e.media_id, e.concept_id, en.full_sentence en, en.correct_answer en_answer, en.intro_text en_intro, sk.full_sentence sk, cz.full_sentence cz from exercises e join exercise_localizations en on en.exercise_id=e.id and en.language_code='en' join exercise_localizations sk on sk.exercise_id=e.id and sk.language_code='sk' join exercise_localizations cz on cz.exercise_id=e.id and cz.language_code='cz' where e.exercise_type_id between {lo} and {hi} order by e.id"""
    r=subprocess.run([SB,'db','query',sql,'--linked','-o','json'],cwd=os.path.expanduser('~/Projects/and-again'),capture_output=True,text=True)
    s=r.stdout; s=s[s.index('{'):]
    rows=json.loads(s)['rows']; print(lo,hi,len(rows)); out+=rows
json.dump(out,open('grammar_rows.json','w'),ensure_ascii=False)
print(len(out))
