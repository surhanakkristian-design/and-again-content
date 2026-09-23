-- ROLLBACK for Part 1 (NOT RUN). The five columns were added empty on 23 Sept 2026, so the
-- data rollback is a reset to NULL; the schema rollback drops them (and migration record).
begin;
update public.media set transcript=null, asset_description=null, speech_sentences=null,
       listening_eligible=null, speaking_eligible=null
 where transcript is not null or asset_description is not null or speech_sentences is not null
    or listening_eligible is not null or speaking_eligible is not null;
-- schema (only if the whole feature is withdrawn; listening_questions must go first):
-- drop table if exists public.listening_questions;
-- alter table public.media drop constraint if exists media_speech_sentences_is_array,
--   drop column transcript, drop column asset_description, drop column speech_sentences,
--   drop column listening_eligible, drop column speaking_eligible;
-- delete from supabase_migrations.schema_migrations where version in ('20260923140000','20260923140100');
commit;
