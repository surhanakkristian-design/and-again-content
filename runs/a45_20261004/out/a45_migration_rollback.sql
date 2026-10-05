-- A45 rollback of the migration (NOT run). Removes the table and its rows; the audio objects stay in storage.
begin;
drop table if exists public.media_exercise_sets;
update storage.buckets set allowed_mime_types = array['audio/mpeg'] where id = 'audio';
commit;
