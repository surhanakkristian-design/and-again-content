-- A57 rollback of batch b002_fr_r2 (not run)
begin;
delete from public.media_exercise_sets_l10n where learning_language = 'fr' and media_id in (68,5149,7870);
commit;
