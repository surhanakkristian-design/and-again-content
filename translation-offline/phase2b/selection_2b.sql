-- Phase 2B selection rule (read-only). Czech language_code in the live DB is 'cz'.
-- There is no sentence_translations table live: sentences live in exercise_localizations.
with vt as (
  select e.concept_id, t.level from exercises e join exercise_types t on t.id = e.exercise_type_id
  where t.focus_category->>'en' = 'Vocabulary'),
vl as (select concept_id,
         case when bool_or(level = 'A') and not bool_or(level = 'B') then 'A'
              when bool_or(level = 'B') and not bool_or(level = 'A') then 'B' end vlev
       from vt group by 1),
ge as (  -- grammar-topic exercises (focus Grammar, level A1..B2, not the 'Random' pseudo-topic) with an en full_sentence
  select e.id exercise_id, e.concept_id, t.level, e.exercise_type_id
  from exercises e join exercise_types t on t.id = e.exercise_type_id
  join exercise_localizations en on en.exercise_id = e.id and en.language_code = 'en'
  where t.focus_category->>'en' = 'Grammar' and t.level in ('A1','A2','B1','B2') and t.title->>'en' <> 'Random'
    and coalesce(en.full_sentence, '') <> ''),
gf as (select concept_id,
         case when bool_and(level like 'A%') then 'A' when bool_and(level like 'B%') then 'B' end glev
       from ge group by 1),
-- concept level: no column exists; = level of the concept's vocabulary exercises (types 27/74/76 = A, 68/69/75/77 = B);
-- if it has both, the family of its grammar exercises; if still ambiguous, A (lower level)
cl as (select w.id concept_id, coalesce(vl.vlev, gf.glev, 'A') clevel,
         case when vl.vlev is not null then 'vocab' when gf.glev is not null then 'grammar' else 'tie_A' end level_source
       from word_concepts w left join vl on vl.concept_id = w.id left join gf on gf.concept_id = w.id),
cc as (select cl.*, row_number() over (order by md5(concept_id::text || 'phase2b-concept'), concept_id) crk from cl),
rk as (select ge.*, cc.clevel, cc.level_source,
         row_number() over (partition by ge.concept_id, ge.level
                            order by md5(ge.concept_id::text || ge.exercise_id::text || 'phase2b'), ge.exercise_id) r
       from ge join cc on cc.concept_id = ge.concept_id and cc.crk <= 3600 and left(ge.level, 1) = cc.clevel)
select rk.concept_id, rk.clevel, rk.level_source, rk.exercise_id, rk.level, rk.exercise_type_id,
  t.title->>'en' type_title, t.level type_level, w.word headword,
  en.full_sentence en, en.correct_answer ca_en, sk.full_sentence sk, sk.correct_answer ca_sk,
  cz.full_sentence cz, cz.correct_answer ca_cz
from rk join exercise_types t on t.id = rk.exercise_type_id join word_concepts w on w.id = rk.concept_id
join exercise_localizations en on en.exercise_id = rk.exercise_id and en.language_code = 'en'
left join exercise_localizations sk on sk.exercise_id = rk.exercise_id and sk.language_code = 'sk'
left join exercise_localizations cz on cz.exercise_id = rk.exercise_id and cz.language_code = 'cz'
where rk.r = 1
order by rk.concept_id, rk.level;
