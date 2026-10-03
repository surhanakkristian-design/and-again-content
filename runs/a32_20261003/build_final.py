# A32: final lists = live snapshot  - body-part words (task 2)  + rebuilt Body Parts lists (task 3)
#      + fallback for thin videos (task 4). Writes out/distractors.json, out/fallback.json,
#      out/changes.json, out/stats.json, backup/changed_rows_before.json, out/a32_data.sql,
#      out/a32_dryrun.sql, out/a32_rollback.sql.
from load import *
from bodyparts import BODY,HUMAN,ANIMAL
from classify import classify, NONE
import bp_first, os, statistics
C=classify()
def strip(m,ids):
    if C[m]["cls"]=="none": return list(ids)
    rm=set(HUMAN)|(ANIMAL if C[m]["animal"] else set())
    return [x for x in ids if x not in rm]
# task 3: first look, minus everything the independent second look called doubt / fit
first=bp_first.build(verbose=False)
aud=json.load(open("packets/bp_audit_out.json"))["verdicts"]
# words added after the second look, by the written rules (out/BODY_PARTS_RULES.md), first look only
TOPUP=json.load(open("out/bp_topup.json")) if os.path.exists("out/bp_topup.json") else {}
bp={}; audit=collections.Counter()
for m,v in first.items():
    keep=[]
    for c in v:
        verdict=aud[str(m)][str(c)]; audit[verdict]+=1
        if verdict=="ok": keep.append(c)
    for c in TOPUP.get(str(m),[]):
        if c not in keep: keep.append(c)
    pos=concepts[twd[m]["concept"]]["part_of_speech"]
    # target 15-25: cap at 25; same part of speech first, the rest picked evenly (fixed order by a hash of video and word)
    import hashlib
    h=lambda c:hashlib.md5(f"{m}:{c}".encode()).hexdigest()
    keep.sort(key=lambda c:(concepts[c]["part_of_speech"]!=pos,h(c)))
    keep=keep[:25]
    keep.sort(key=lambda c:(concepts[c]["part_of_speech"]!=pos,c))
    bp[m]=keep
# task 4: fallback (other level of the same group) for thin videos that had none; my first look
NEW_FB={7302:[3619,5020,5323]}   # underground, chains, jimmy; 196 / 6828 / 8048: no word of level A survives the look
D={}; F={}; pairs=0; touched=set(); removed_by_word=collections.Counter()
for m,r in twd.items():
    d=strip(m,r["dist"]); f=strip(m,r["fb"])
    gone=(len(r["dist"])-len(d))+(len(r["fb"])-len(f))
    if gone: pairs+=gone; touched.add(m)
    for x in r["dist"]+r["fb"]:
        if x not in d and x not in f: removed_by_word[x]+=1
    if r["group"]==BP: d=bp[m]
    if m in NEW_FB: f=NEW_FB[m]
    if len(d)>=5: f=f  # fallback stays as stored; the app reads it only below 5
    D[m]=d; F[m]=f
# checks (the same as the SQL assertions)
keyset_bp={r["concept"] for r in twd.values() if r["group"]==BP}
for m in twd:
    allc=D[m]+F[m]
    assert len(set(D[m]))==len(D[m]) and len(set(F[m]))==len(F[m]),m
    assert not set(allc)&links[m],m
    assert all(c in concepts for c in allc),m
    assert twd[m]["concept"] not in allc,m
    if C[m]["cls"]!="none": assert not set(allc)&HUMAN,m
    if C[m]["animal"]: assert not set(allc)&ANIMAL,m
    if twd[m]["group"]==BP: assert len(D[m])>=10 and not set(D[m])&keyset_bp and not set(D[m])&set(BODY),(m,len(D[m]))
changed=sorted(m for m in twd if D[m]!=twd[m]["dist"] or F[m]!=twd[m]["fb"])
json.dump({str(m):D[m] for m in sorted(D)},open("out/distractors.json","w"))
json.dump({str(m):F[m] for m in sorted(F) if F[m]},open("out/fallback.json","w"))
json.dump([dict(media_id=m,concept_id=twd[m]["concept"],group_id=twd[m]["group"],level=twd[m]["level"],distractor_concept_ids=twd[m]["dist"],fallback_concept_ids=twd[m]["fb"]) for m in changed],open("backup/changed_rows_before.json","w"))
json.dump({str(m):dict(before_d=twd[m]["dist"],before_f=twd[m]["fb"],after_d=D[m],after_f=F[m]) for m in changed},open("out/changes.json","w"))
nb=[len(D[m]) for m in bp]
thin_list=sorted(m for m in twd if len(D[m])<5)
thin_both=sorted(m for m in twd if len(D[m])<5 and len(D[m])+len(F[m])<5)
none_all=sorted(m for m in thin_list if len(D[m])+len(F[m])==0)
alln=[len(v) for v in D.values()]
st=dict(rows=len(twd),body_part_concepts=len(BODY),pairs_removed=pairs,videos_touched=len(touched),
  pairs_removed_outside_body_parts_group=sum((len(twd[m]["dist"])-len(strip(m,twd[m]["dist"])))+(len(twd[m]["fb"])-len(strip(m,twd[m]["fb"]))) for m in twd if twd[m]["group"]!=BP),
  videos_touched_outside_body_parts_group=len([m for m in touched if twd[m]["group"]!=BP]),
  classes=dict(collections.Counter(v["cls"] for v in C.values())),person_with_animal=sum(v["cls"]=="person" and v["animal"] for v in C.values()),
  bp_videos=len(bp),bp_min=min(nb),bp_avg=round(statistics.mean(nb),1),bp_max=max(nb),audit=dict(audit),
  rows_changed=len(changed),thin_list_alone=thin_list,thin_list_plus_fallback=thin_both,no_option_at_all=none_all,
  avg_options_all=round(statistics.mean(alln),1),avg_before=round(statistics.mean(len(r["dist"]) for r in twd.values()),1),
  removed_by_word={concepts[c]["word"]+f" ({c})":n for c,n in removed_by_word.most_common()})
json.dump(st,open("out/stats.json","w"),indent=1)
print({k:v for k,v in st.items() if k!="removed_by_word"})
# ---------- SQL
arr=lambda xs:"'{"+",".join(map(str,xs))+"}'::bigint[]"
vals=",\n".join(f"({m},{arr(twd[m]['dist'])},{arr(twd[m]['fb'])},{arr(D[m])},{arr(F[m])})" for m in changed)
non_none="'{"+",".join(str(m) for m in sorted(NONE))+"}'::bigint[]"
animal_ids="'{"+",".join(str(m) for m in sorted(m for m in C if C[m]["animal"]))+"}'::bigint[]"
head=f"""-- A32 data write (guarded): body-part words out of the wrong-word lists, Body Parts lists rebuilt
-- from other groups, fallback for one thin video. {len(changed)} of 3,034 rows change. ONE transaction.
begin;
create temp table a32_change (media_id bigint primary key, old_d bigint[] not null, old_f bigint[] not null, new_d bigint[] not null, new_f bigint[] not null) on commit drop;
insert into a32_change (media_id, old_d, old_f, new_d, new_f) values
{vals};
do $$ begin
  if (select count(*) from a32_change) <> {len(changed)} then raise exception 'a32: change set is not complete'; end if;
  if (select count(*) from public.tinder_word_distractors) <> 3034 then raise exception 'a32: tinder_word_distractors does not have 3034 rows'; end if;
  if (select count(*) from public.tinder_word_distractors d join a32_change c on c.media_id = d.media_id
      where d.distractor_concept_ids = c.old_d and d.fallback_concept_ids = c.old_f) <> {len(changed)}
    then raise exception 'a32: a row to be changed no longer has the values of the snapshot; nothing was changed'; end if;
end $$;
update public.tinder_word_distractors d set distractor_concept_ids = c.new_d, fallback_concept_ids = c.new_f
  from a32_change c where c.media_id = d.media_id;
do $$
declare human bigint[] := {arr(sorted(HUMAN))};
        animal bigint[] := {arr(sorted(ANIMAL))};
        no_being bigint[] := {non_none};
        with_animal bigint[] := {animal_ids};
begin
  if (select count(*) from public.tinder_word_distractors) <> 3034 then raise exception 'a32: rows <> 3034'; end if;
  if exists (select 1 from public.tinder_word_distractors d where not (d.media_id = any(no_being)) and (d.distractor_concept_ids || d.fallback_concept_ids) && human)
    then raise exception 'a32: a body-part word is left on a video with a person or an animal'; end if;
  if exists (select 1 from public.tinder_word_distractors d where d.media_id = any(with_animal) and (d.distractor_concept_ids || d.fallback_concept_ids) && animal)
    then raise exception 'a32: an animal-part word is left on a video with an animal'; end if;
  if exists (select 1 from public.tinder_word_distractors d where d.group_id = {BP} and cardinality(d.distractor_concept_ids) < 10)
    then raise exception 'a32: a Body Parts video has fewer than 10 options'; end if;
  if exists (select 1 from public.tinder_word_distractors d join public.tinder_word_distractors o on o.group_id = {BP} and o.concept_id = any(d.distractor_concept_ids) where d.group_id = {BP})
    then raise exception 'a32: a Body Parts video has a word of its own group'; end if;
  if exists (select 1 from public.tinder_word_distractors d join public.concept_media cm on cm.media_id = d.media_id where cm.concept_id = any(d.distractor_concept_ids || d.fallback_concept_ids))
    then raise exception 'a32: a list holds a word linked to the same media'; end if;
  if exists (select 1 from public.tinder_word_distractors d, unnest(d.distractor_concept_ids || d.fallback_concept_ids) c where not exists (select 1 from public.word_concepts w where w.id = c))
    then raise exception 'a32: unknown concept in a list'; end if;
  if exists (select 1 from public.tinder_word_distractors d where d.concept_id = any(d.distractor_concept_ids || d.fallback_concept_ids))
    then raise exception 'a32: a list holds the key word itself'; end if;
end $$;
"""
open("out/a32_data.sql","w").write(head+"commit;\n")
open("out/a32_dryrun.sql","w").write(head+"""do $$ begin raise exception 'DRY RUN OK: rows %, changed rows now equal to the new values %, sum of options %, sum of fallback %',
  (select count(*) from public.tinder_word_distractors),
  (select count(*) from public.tinder_word_distractors d join a32_change c on c.media_id = d.media_id where d.distractor_concept_ids = c.new_d and d.fallback_concept_ids = c.new_f),
  (select sum(cardinality(distractor_concept_ids)) from public.tinder_word_distractors),
  (select sum(cardinality(fallback_concept_ids)) from public.tinder_word_distractors); end $$;
commit;
""")
rb=",\n".join(f"({m},{arr(D[m])},{arr(F[m])},{arr(twd[m]['dist'])},{arr(twd[m]['fb'])})" for m in changed)
open("out/a32_rollback.sql","w").write(f"""-- A32 rollback (NOT run). Puts the {len(changed)} changed rows back to their values before A32.
-- Guarded: it stops and changes nothing if a row no longer has the A32 values.
begin;
create temp table a32_back (media_id bigint primary key, cur_d bigint[] not null, cur_f bigint[] not null, old_d bigint[] not null, old_f bigint[] not null) on commit drop;
insert into a32_back (media_id, cur_d, cur_f, old_d, old_f) values
{rb};
do $$ begin
  if (select count(*) from public.tinder_word_distractors d join a32_back c on c.media_id = d.media_id
      where d.distractor_concept_ids = c.cur_d and d.fallback_concept_ids = c.cur_f) <> {len(changed)}
    then raise exception 'a32 rollback: a row no longer has the A32 values; nothing was changed'; end if;
end $$;
update public.tinder_word_distractors d set distractor_concept_ids = c.old_d, fallback_concept_ids = c.old_f
  from a32_back c where c.media_id = d.media_id;
commit;
""")
print("sum options",sum(len(v) for v in D.values()),"sum fallback",sum(len(v) for v in F.values()),"changed",len(changed))
