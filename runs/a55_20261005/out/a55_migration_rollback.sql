-- A55 rollback of the migration 20261006100000 (not run): drops the table of the German / Spanish / French sets.
begin;
drop table if exists public.media_exercise_sets_l10n;
commit;
