-- ============================================================================
-- 5b pass P/hu: French spacing in hu full_sentence (population: hu rows with
-- full_sentence not null, intro_text carrying a blank, exercise_type <> 69, and a space
-- before , . ; : ! ? in full_sentence). Expected 14 rows, 0 of them chunked.
-- Run the three blocks one after another in the Supabase SQL editor.
-- ============================================================================

-- ---- 1. BEFORE ---------------------------------------------------------------
-- Same population as the update below (blank in intro_text, type 69 excluded).
select count(*) rows_before, count(*) filter (where el.chunks is not null) chunked_before
from exercise_localizations el join exercises e on e.id = el.exercise_id
where el.full_sentence is not null and el.intro_text like '%...%' and e.exercise_type_id <> 69
  and el.language_code = 'hu' and el.full_sentence ~ ' [,.;:!?]';

-- ---- 2. UPDATE (four-step derivation; guard: the only change is the stray space) --
with base as (
  select el.id, el.language_code lang, el.intro_text i, el.correct_answer a, el.full_sentence f,
         (el.chunks is not null) was_chunked,
         (length(el.intro_text) - length(replace(el.intro_text,'...','')))/3 nb,
         (length(el.correct_answer) - length(replace(el.correct_answer,'...','')))/3 na
  from exercise_localizations el join exercises e on e.id = el.exercise_id
  where el.full_sentence is not null and el.intro_text like '%...%' and e.exercise_type_id <> 69
    and el.language_code = 'hu' and el.full_sentence ~ ' [,.;:!?]'
),
sub as (select *, case
    when nb = 1 and na = 0 then split_part(i,'...',1)||a||split_part(i,'...',2)
    when nb = 2 and na = 1 then split_part(i,'...',1)||split_part(a,'...',1)||split_part(i,'...',2)||split_part(a,'...',2)||split_part(i,'...',3)
    end s1 from base),
col as (select *, btrim(regexp_replace(s1, '\s+', ' ', 'g')) s2 from sub),                  -- step 2
pun as (select *, regexp_replace(s2, ' +([,.;:!?])', '\1', 'g') s3 from col),               -- step 3 (non-French)
fin as (select *, case when rtrim(i) like '%...' and s3 !~ '[.?!]$' then s3||'.' else s3 end d4 from pun),  -- step 4
ok  as (select * from fin where d4 = regexp_replace(f, ' +([,.;:!?])', '\1', 'g') and d4 <> f)  -- guard: only stray spaces removed
update exercise_localizations el
set full_sentence = ok.d4,
    chunks = null,                  -- chunked rows re-enter `remaining`
    correct_alternative = null
from ok
where el.id = ok.id and el.language_code = 'hu'
returning el.id, ok.was_chunked, ok.f old_sentence, el.full_sentence new_sentence;

-- ---- 3. AFTER ----------------------------------------------------------------
-- Same population as block 1. Expected 0.
-- A NON-ZERO count here is NOT a failed update: it is the rows the guard in block 2
-- refused, because their derivation differs from the live sentence by more than the
-- stray space. They were left untouched on purpose. Block 4 lists them; report them,
-- do not re-run with a weaker guard.
select count(*) rows_after_expected_0
from exercise_localizations el join exercises e on e.id = el.exercise_id
where el.full_sentence is not null and el.intro_text like '%...%' and e.exercise_type_id <> 69
  and el.language_code = 'hu' and el.full_sentence ~ ' [,.;:!?]';

-- ---- 4. REFUSED ROWS (only needed when block 3 is non-zero) -------------------
select el.id, (el.chunks is not null) chunked, el.intro_text, el.correct_answer, el.full_sentence
from exercise_localizations el join exercises e on e.id = el.exercise_id
where el.full_sentence is not null and el.intro_text like '%...%' and e.exercise_type_id <> 69
  and el.language_code = 'hu' and el.full_sentence ~ ' [,.;:!?]'
order by el.id;
