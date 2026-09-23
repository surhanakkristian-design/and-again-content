"""Guarded insert of AGREED listening questions. <=500 per transaction; each row must point at a
listening_eligible video; conflicts are not overwritten; the batch aborts if the count differs."""
import json,subprocess,sys,os,tempfile
SB=os.path.expanduser("~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase")
rows=json.load(open("lq/final_rows.json")); B=500
for i in range(0,len(rows),B):
    chunk=rows[i:i+B]; js=json.dumps(chunk,ensure_ascii=False); assert "$J$" not in js
    sql=f"""begin;
do $w$ declare n int; begin
  insert into public.listening_questions (media_id, question, correct_answer, accepted_answers)
  select x.media_id, x.question, x.correct_answer, x.accepted_answers
  from jsonb_to_recordset($J${js}$J$::jsonb) as x(media_id bigint, question text, correct_answer text, accepted_answers jsonb)
  join public.media m on m.id = x.media_id and m.listening_eligible and m.media_type = 'video'
  on conflict (media_id) do nothing;
  get diagnostics n = row_count;
  if n <> {len(chunk)} then raise exception 'GUARD batch {i//B+1}: inserted % of {len(chunk)}', n; end if;
end $w$;
commit;
"""
    f=tempfile.NamedTemporaryFile("w",suffix=".sql",delete=False); f.write(sql); f.close()
    r=subprocess.run([SB,"db","query","--linked","--file",f.name],capture_output=True,text=True,cwd=os.path.expanduser("~/Projects/and-again"))
    open(f"write_logs/lq_batch_{i//B+1}.log","w").write(r.stdout+r.stderr)
    ok=r.returncode==0 and "GUARD" not in r.stdout+r.stderr
    print("batch",i//B+1,len(chunk),"OK" if ok else "FAIL")
    if not ok: print((r.stdout+r.stderr)[-800:]); sys.exit(1)
