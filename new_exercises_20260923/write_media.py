"""Guarded writer for Part 1: media.transcript / asset_description / speech_sentences / *_eligible.
Batches of <=500, one transaction each; only rows whose id AND title match and whose five new
columns are still all NULL are updated. The batch aborts (raise) if the updated count differs."""
import json,subprocess,sys,os,tempfile
SB=os.path.expanduser("~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase")
rows=json.load(open("payload.json")); B=500
def lit(s): return "$J$"+s+"$J$"
os.makedirs("write_logs",exist_ok=True)
for i in range(0,len(rows),B):
    chunk=rows[i:i+B]; js=json.dumps(chunk,ensure_ascii=False)
    assert "$J$" not in js
    sql=f"""begin;
do $w$ declare n int; begin
  with x as (select * from jsonb_to_recordset({lit(js)}::jsonb) as x(id bigint, title text, transcript text, asset_description text, speech_sentences jsonb, listening_eligible boolean, speaking_eligible boolean))
  update public.media m set transcript=x.transcript, asset_description=x.asset_description, speech_sentences=x.speech_sentences,
         listening_eligible=x.listening_eligible, speaking_eligible=x.speaking_eligible
  from x where m.id=x.id and m.title=x.title
    and m.transcript is null and m.asset_description is null and m.speech_sentences is null
    and m.listening_eligible is null and m.speaking_eligible is null;
  get diagnostics n = row_count;
  if n <> {len(chunk)} then raise exception 'GUARD batch {i//B+1}: updated % of {len(chunk)}', n; end if;
end $w$;
commit;
"""
    f=tempfile.NamedTemporaryFile("w",suffix=".sql",delete=False); f.write(sql); f.close()
    r=subprocess.run([SB,"db","query","--linked","--file",f.name],capture_output=True,text=True,cwd=os.path.expanduser("~/Projects/and-again"))
    open(f"write_logs/batch_{i//B+1}.log","w").write(r.stdout+r.stderr)
    ok=r.returncode==0 and "GUARD" not in r.stdout+r.stderr
    print("batch",i//B+1,len(chunk),"OK" if ok else "FAIL"); 
    if not ok: print((r.stdout+r.stderr)[-800:]); sys.exit(1)
