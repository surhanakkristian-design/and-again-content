-- A45 rollback of the picture-shape columns (NOT run).
begin;
alter table public.media_exercise_sets drop column if exists width, drop column if exists height;
commit;
