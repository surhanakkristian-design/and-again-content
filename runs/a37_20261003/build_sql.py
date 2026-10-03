# A37: the guarded data SQL, its rollback and the tables of the report.
import json,os,hashlib,collections,re
from load import twd,concepts,media
from build_lists import build,A36_4754
APP=os.path.expanduser("~/Projects/and-again-a37")
G=json.load(open("out/groups_final.json")); N=json.load(open("out/names_final.json")); REPS=json.load(open("out/reps_final.json"))
old={int(g["id"]):g for g in json.load(open("data/groups.json"))}
rows=build(G)
t0={m:dict(v) for m,v in twd.items()}; t0[4754]=dict(A36_4754)      # the state after A36's 4754 write
arr=lambda xs:"'{"+",".join(map(str,xs))+"}'::bigint[]"
q=lambda s:"'"+s.replace("'","''")+"'"
# guards: the tables as in the snapshot (4754 as A36 leaves it)
h_twd=hashlib.md5(";".join(f'{m}:{v["concept"]}:{v["group"]}:{",".join(map(str,v["dist"]))}:{",".join(map(str,v["fb"]))}' for m,v in sorted(t0.items())).encode()).hexdigest()
mg={int(i):(int(m["group_id"]) if m["group_id"] is not None else None) for i,m in media.items()}; mg[4754]=20
assert all(v is not None for v in mg.values())
h_media=hashlib.md5(";".join(f"{i}:{g}" for i,g in sorted(mg.items())).encode()).hexdigest()
LANGS=["en","de","sk","cz","es","fr","hu","tr","ua"]
out=["-- A37 (3 Oct 2026): 112 smaller groups of videos made from the 35 groups of A31 (decisions 1-2).",
"-- Runs inside the caller's transaction, after the migration 20261003230000 and A36's two files.",
"-- Guarded: media.group_id and tinder_word_distractors must be exactly as in the snapshot; raises otherwise.",
"do $$","declare n int; h text;","begin",
" if (select count(*) from media_groups) <> 35 or exists (select 1 from media_groups where id >= 100 or parent_id is not null) then raise exception 'A37: media_groups is not the 35 groups of A31'; end if;",
f" select md5(string_agg(id || ':' || group_id, ';' order by id)) into h from media; if h is distinct from '{h_media}' then raise exception 'A37: media.group_id differs from the snapshot'; end if;",
f" select md5(string_agg(media_id || ':' || concept_id || ':' || group_id || ':' || array_to_string(distractor_concept_ids, ',') || ':' || array_to_string(fallback_concept_ids, ','), ';' order by media_id)) into h from tinder_word_distractors; if h is distinct from '{h_twd}' then raise exception 'A37: tinder_word_distractors differs from the snapshot'; end if;",
"","insert into media_groups (id, name, source_category_ids, rep_media_a, rep_media_b, rep_media_all, parent_id) values"]
vals=[]
for g in G:
    name={l:N[str(g["id"])][l] for l in LANGS}
    r=REPS[str(g["id"])]
    vals.append(f' ({g["id"]}, {q(json.dumps(name,ensure_ascii=False))}::jsonb, {arr(old[g["parent"]]["source_category_ids"])}, {r["A"]}, {r["B"]}, {r["all"]}, {g["parent"]})')
out.append(",\n".join(vals)+";")
out.append(" with v(id, was, new) as (values\n"+",\n".join(f'  ({m}, {rows[m]["group"]//100}, {rows[m]["group"]})' for m in sorted(rows))+"),\n u as (update media m set group_id = v.new from v where m.id = v.id and m.group_id = v.was and m.media_type = 'video' returning 1) select count(*) into n from u;")
out.append(f" if n <> {len(rows)} then raise exception 'A37 media: % rows, expected {len(rows)}', n; end if;")
out.append(" with v(media_id, grp, dist, fb) as (values\n"+",\n".join(f'  ({m}, {r["group"]}, {arr(r["own"])}, {arr(r["fb"])})' for m,r in sorted(rows.items()))+"),\n u as (update tinder_word_distractors t set group_id = v.grp, distractor_concept_ids = v.dist, fallback_concept_ids = v.fb from v where t.media_id = v.media_id returning 1) select count(*) into n from u;")
out.append(f" if n <> {len(rows)} then raise exception 'A37 lists: % rows, expected {len(rows)}', n; end if;")
out+=["",
 " -- after the write",
 " if (select count(*) from media_groups where parent_id is not null) <> 112 then raise exception 'A37: not 112 new groups'; end if;",
 " if (select count(*) from media_groups g, jsonb_each_text(g.name) e where g.parent_id is not null and e.value !~ '[[:space:]&/-]' and e.key in ('en','de','sk','cz','es','fr','hu','tr','ua')) <> 112 * 9 then raise exception 'A37: a name is missing or not one word'; end if;",
 " if exists (select 1 from media_groups g join media_groups o on o.parent_id is not null and g.parent_id is not null and o.id < g.id, jsonb_each_text(g.name) e where o.name ->> e.key = e.value) then raise exception 'A37: a name is used twice in a language'; end if;",
 " if exists (select 1 from media m left join media_groups g on g.id = m.group_id where m.media_type = 'video' and g.parent_id is null) then raise exception 'A37: a video without a new group'; end if;",
 " if exists (select 1 from media_groups g where g.parent_id is not null and ((select count(*) from media m join exercises e on e.media_id = m.id and e.exercise_type_id = 74 where m.group_id = g.id and m.media_type = 'video') < 6 or (select count(*) from media m join exercises e on e.media_id = m.id and e.exercise_type_id = 75 where m.group_id = g.id and m.media_type = 'video') < 6)) then raise exception 'A37: a group with fewer than 6 videos at a level'; end if;",
 " if exists (select 1 from media_groups g where g.parent_id is not null and (not exists (select 1 from media m join exercises e on e.media_id = m.id and e.exercise_type_id = 74 where m.id = g.rep_media_a and m.group_id = g.id and m.media_type = 'video') or not exists (select 1 from media m join exercises e on e.media_id = m.id and e.exercise_type_id = 75 where m.id = g.rep_media_b and m.group_id = g.id and m.media_type = 'video') or not exists (select 1 from media m where m.id = g.rep_media_all and m.group_id = g.id and m.media_type = 'video'))) then raise exception 'A37: a representative is not a video of its group and level'; end if;",
 " if not exists (select 1 from media_groups g join media m on m.id = 209 and m.group_id = g.id where g.rep_media_a = 209 and g.rep_media_all = 209) then raise exception 'A37: media 209 does not represent its group'; end if;",
 " if exists (select 1 from tinder_word_distractors t join media m on m.id = t.media_id where t.group_id <> m.group_id) then raise exception 'A37: a list names another group than its video'; end if;",
 " if exists (select 1 from tinder_word_distractors t where t.concept_id = any(t.distractor_concept_ids) or t.concept_id = any(t.fallback_concept_ids)) then raise exception 'A37: a list holds its own key word'; end if;",
 " if exists (select 1 from tinder_word_distractors t join concept_media c on c.media_id = t.media_id where c.concept_id = any(t.distractor_concept_ids) or c.concept_id = any(t.fallback_concept_ids)) then raise exception 'A37: a list holds a word linked to its video'; end if;",
 "end $$;"]
open("out/a37_data.sql","w").write("\n".join(out)+"\n")
# rollback (not run): the state before A37 (after A36's files)
rb=["-- A37 ROLLBACK (not run): back to the 35 groups; the lists as before A37 (after A36's 4754 write).","begin;",
 "update media m set group_id = g.parent_id from media_groups g where g.id = m.group_id and g.parent_id is not null;",
 "update tinder_word_distractors t set group_id = v.grp, distractor_concept_ids = v.dist, fallback_concept_ids = v.fb from (values\n"+",\n".join(f'  ({m}, {v["group"]}, {arr(v["dist"])}, {arr(v["fb"])})' for m,v in sorted(t0.items()))+") as v(media_id, grp, dist, fb) where t.media_id = v.media_id;",
 "delete from media_groups where parent_id is not null;","commit;","-- the column media_groups.parent_id may stay (additive); to drop it: alter table media_groups drop column parent_id;"]
open("out/a37_rollback.sql","w").write("\n".join(rb)+"\n")
# tables
lev={m:r["level"] for m,r in rows.items()}
cnt=lambda g,L:sum(lev[m]==L for m in g["media"])
eff=lambda x: len(x["own"]) if len(x["own"])>=5 else x["n_all"]
md=["# A37 groups (112)","","| id | group | from | videos A | videos B | rep A | rep B | rep all | wrong words from the group, avg A / B |","|---|---|---|---|---|---|---|---|---|"]
for g in G:
    r=REPS[str(g["id"])]; av=lambda L:(lambda xs: f"{sum(xs)/len(xs):.1f}")([len(rows[m]["own"]) for m in g["media"] if lev[m]==L])
    md.append(f'| {g["id"]} | {g["en"]} | {g["parent_en"]} | {cnt(g,"A")} | {cnt(g,"B")} | {r["A"]} | {r["B"]} | {r["all"]} | {av("A")} / {av("B")} |')
open("out/group_list.md","w").write("\n".join(md)+"\n")
nm=["# A37 group names","","| id | "+" | ".join(LANGS)+" |","|"+"---|"*10]+[f'| {g["id"]} | '+" | ".join(N[str(g["id"])][l] for l in LANGS)+" |" for g in G]
open("out/group_names.md","w").write("\n".join(nm)+"\n")
thin=[x for x in rows.values() if eff(x)<5]
stats=dict(groups=len(G),min_a=min(cnt(g,"A") for g in G),min_b=min(cnt(g,"B") for g in G),videos=len(rows),own_below5=sum(len(x["own"])<5 for x in rows.values()),own_none=sum(len(x["own"])==0 for x in rows.values()),after_parent_below5=sum(len(x["own"])<5 and x["n_parent"]<5 for x in rows.values()),final_below5=len(thin),final_none=sum(eff(x)==0 for x in thin),avg_own=round(sum(len(x["own"]) for x in rows.values())/len(rows),1),avg_shown=round(sum(eff(x) for x in rows.values())/len(rows),1),thin=[dict(media=x["media"],word=concepts[x["concept"]]["word"],group=x["group"],options=eff(x)) for x in thin],sha_data=hashlib.sha256(open("out/a37_data.sql","rb").read()).hexdigest())
json.dump(stats,open("out/stats.json","w"),indent=1); print({k:v for k,v in stats.items() if k!="thin"}); print(stats["thin"])
print(os.path.getsize("out/a37_data.sql"),os.path.getsize("out/a37_rollback.sql"))
