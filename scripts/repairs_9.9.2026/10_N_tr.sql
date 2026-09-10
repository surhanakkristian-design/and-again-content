-- ============================================================================
-- 5b pass N/tr: append the final mark where the intro ended on the blank and the live
-- full_sentence has none (population: tr rows with full_sentence not null, intro_text
-- ending on '...', exercise_type <> 69, full_sentence not ending in . ? !, hold-out ids
-- excluded: all seven Turkish ids in holdout_glued_blanks.md, not only the five whose
-- sentence differs. 208259 and 208790 already end in a stop, but that is a guard, not an
-- assumption). Expected about 11709 rows. Mark = '.' where the English sibling ends in
-- '.', otherwise the per-row mark from no_stop_wrong_mark_119.csv.
-- ============================================================================

-- ---- 1. BEFORE ---------------------------------------------------------------
select count(*) rows_before, count(*) filter (where el.chunks is not null) chunked_before
from exercise_localizations el join exercises e on e.id = el.exercise_id
where el.language_code = 'tr' and el.full_sentence is not null and e.exercise_type_id <> 69
  and rtrim(el.intro_text) like '%...' and el.full_sentence !~ '[.?!]$' and el.id not in (207053, 208610, 210563, 210806, 211049, 208259, 208790);

-- ---- 2. UPDATE -----------------------------------------------------------------
with tgt as (
  select el.id, (el.chunks is not null) was_chunked, el.full_sentence f,
         case el.id
      when 29798 then '!'
      when 30500 then '!'
      when 31553 then '!'
      when 103427 then '!'
      when 103922 then '!'
      when 104462 then '!'
      when 107504 then '!'
      when 107522 then '!'
      when 107837 then '!'
      when 108089 then '!'
      when 108341 then '!'
      when 108584 then '!'
      when 108845 then '!'
      when 109070 then '!'
      when 109088 then '!'
      when 109313 then '!'
      when 109331 then '!'
      when 109583 then '!'
      when 122633 then '!'
      when 128708 then '!'
      when 129077 then '!'
      when 137879 then '!'
      when 138392 then '!'
      when 138662 then '!'
      when 139184 then '!'
      when 139697 then '!'
      when 140192 then '!'
      when 140444 then '!'
      when 140696 then '!'
      when 140939 then '!'
      when 141209 then '!'
      when 141452 then '!'
      when 141695 then '!'
      when 141938 then '!'
      when 142190 then '!'
      when 142433 then '!'
      when 142676 then '!'
      when 142919 then '!'
      when 143162 then '!'
      when 143423 then '!'
      when 143666 then '!'
      when 143909 then '!'
      when 144152 then '!'
      when 144404 then '!'
      when 144674 then '!'
      when 144917 then '!'
      when 145169 then '!'
      when 145421 then '!'
      when 145664 then '!'
      when 145907 then '!'
      when 146150 then '!'
      when 146402 then '!'
      when 146681 then '!'
      when 155636 then '!'
      when 155879 then '!'
      when 156140 then '!'
      when 156383 then '!'
      when 156626 then '!'
      when 156869 then '!'
      when 157139 then '!'
      when 157400 then '!'
      when 157652 then '!'
      when 157895 then '!'
      when 158147 then '!'
      when 158426 then '!'
      when 158669 then '!'
      when 158921 then '!'
      when 159164 then '!'
      when 159425 then '!'
      when 159668 then '!'
      when 159911 then '!'
      when 160172 then '!'
      when 160424 then '!'
      when 160676 then '!'
      when 160928 then '!'
      when 161171 then '!'
      when 161432 then '!'
      when 161675 then '!'
      when 161945 then '!'
      when 162188 then '!'
      when 162440 then '!'
      when 162683 then '!'
      when 162926 then '!'
      when 163169 then '!'
      when 163412 then '!'
      when 163664 then '!'
      when 163916 then '!'
      when 164159 then '!'
      when 164411 then '!'
      when 164654 then '!'
      when 164897 then '!'
      when 165140 then '!'
      when 165410 then '!'
      when 165662 then '!'
      when 175733 then '!'
      when 176309 then '!'
      when 101546 then '?'
      when 131399 then '?'
      when 132137 then '?'
      when 137708 then '?'
      when 231794 then '?'
      when 119708 then '.'
      when 23525 then '.'
      when 29492 then '.'
         else '.' end mark,
         right(en.full_sentence, 1) en_last
  from exercise_localizations el
  join exercises e on e.id = el.exercise_id
  join exercise_localizations en on en.exercise_id = el.exercise_id and en.language_code = 'en'
  where el.language_code = 'tr' and el.full_sentence is not null and e.exercise_type_id <> 69
    and rtrim(el.intro_text) like '%...' and el.full_sentence !~ '[.?!]$' and el.id not in (207053, 208610, 210563, 210806, 211049, 208259, 208790)
),
ok as (select * from tgt where mark <> '.' or en_last = '.')   -- guard: '.' only where English ends in '.'
update exercise_localizations el
set full_sentence = ok.f || ok.mark,
    chunks = case when ok.was_chunked then null else el.chunks end,
    correct_alternative = case when ok.was_chunked then null else el.correct_alternative end
from ok
where el.id = ok.id and el.language_code = 'tr'
returning el.id, ok.was_chunked, ok.mark;

-- ---- 3. AFTER ----------------------------------------------------------------
select count(*) rows_after_expected_0
from exercise_localizations el join exercises e on e.id = el.exercise_id
where el.language_code = 'tr' and el.full_sentence is not null and e.exercise_type_id <> 69
  and rtrim(el.intro_text) like '%...' and el.full_sentence !~ '[.?!]$' and el.id not in (207053, 208610, 210563, 210806, 211049, 208259, 208790);
