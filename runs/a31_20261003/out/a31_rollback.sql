-- A31 rollback (NOT run). Removes everything A31 added; nothing else was changed.
begin;
drop table if exists public.tinder_word_distractors;
drop index if exists public.media_group_id_idx;
alter table public.media drop column if exists group_id;
drop table if exists public.media_groups;
commit;
-- then: supabase migration repair --linked --status reverted 20261003210000
