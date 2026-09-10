-- ============================================================================
-- 5b pass N/cz: append the final mark where the intro ended on the blank and the live
-- full_sentence has none (population: cz rows with full_sentence not null, intro_text
-- ending on '...', exercise_type <> 69, full_sentence not ending in . ? !, hold-out ids
-- excluded). Expected about 2237 rows. Mark = '.' where the English sibling ends in
-- '.', otherwise the per-row mark from no_stop_wrong_mark_119.csv.
-- ============================================================================

-- ---- 1. BEFORE ---------------------------------------------------------------
select count(*) rows_before, count(*) filter (where el.chunks is not null) chunked_before
from exercise_localizations el join exercises e on e.id = el.exercise_id
where el.language_code = 'cz' and el.full_sentence is not null and e.exercise_type_id <> 69
  and rtrim(el.intro_text) like '%...' and el.full_sentence !~ '[.?!]$' ;

-- ---- 2. UPDATE -----------------------------------------------------------------
with tgt as (
  select el.id, (el.chunks is not null) was_chunked, el.full_sentence f,
         case el.id
      when 103918 then '!'
      when 152536 then '.'
      when 153814 then '.'
         else '.' end mark,
         right(en.full_sentence, 1) en_last
  from exercise_localizations el
  join exercises e on e.id = el.exercise_id
  join exercise_localizations en on en.exercise_id = el.exercise_id and en.language_code = 'en'
  where el.language_code = 'cz' and el.full_sentence is not null and e.exercise_type_id <> 69
    and rtrim(el.intro_text) like '%...' and el.full_sentence !~ '[.?!]$' 
),
ok as (select * from tgt where mark <> '.' or en_last = '.')   -- guard: '.' only where English ends in '.'
update exercise_localizations el
set full_sentence = ok.f || ok.mark,
    chunks = case when ok.was_chunked then null else el.chunks end,
    correct_alternative = case when ok.was_chunked then null else el.correct_alternative end
from ok
where el.id = ok.id and el.language_code = 'cz'
returning el.id, ok.was_chunked, ok.mark;

-- ---- 3. AFTER ----------------------------------------------------------------
select count(*) rows_after_expected_0
from exercise_localizations el join exercises e on e.id = el.exercise_id
where el.language_code = 'cz' and el.full_sentence is not null and e.exercise_type_id <> 69
  and rtrim(el.intro_text) like '%...' and el.full_sentence !~ '[.?!]$' ;
