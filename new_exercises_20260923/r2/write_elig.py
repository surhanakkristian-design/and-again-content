"""Guarded writer: listening_eligible/speaking_eligible false -> true for the videos added by rule v2.
One transaction; only rows whose id AND title match, media_type='video', both flags still false, and a non-empty
speech_sentences are updated; raises (rollback) if the count differs."""
import json,subprocess,sys,os,tempfile
SB=os.path.expanduser("~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase")
rows=json.load(open("elig_added.json")); js=json.dumps(rows,ensure_ascii=False); assert "$J$" not in js
sql=f"""begin;
do $w$ declare n int; begin
  update public.media m set listening_eligible=true, speaking_eligible=true
  from jsonb_to_recordset($J${js}$J$::jsonb) as x(id bigint, title text)
  where m.id=x.id and m.title=x.title and m.media_type='video'
    and m.listening_eligible = false and m.speaking_eligible = false
    and jsonb_array_length(m.speech_sentences) > 0;
  get diagnostics n = row_count;
  if n <> {len(rows)} then raise exception 'GUARD elig: updated % of {len(rows)}', n; end if;
end $w$;
commit;
"""
f=tempfile.NamedTemporaryFile("w",suffix=".sql",delete=False); f.write(sql); f.close()
r=subprocess.run([SB,"db","query","--linked","--file",f.name],capture_output=True,text=True,cwd=os.path.expanduser("~/Projects/and-again"))
open("write_logs/elig_batch_1.log","w").write(r.stdout+r.stderr)
ok=r.returncode==0 and "GUARD" not in r.stdout+r.stderr
print(len(rows),"OK" if ok else "FAIL"); 
if not ok: print((r.stdout+r.stderr)[-800:]); sys.exit(1)
