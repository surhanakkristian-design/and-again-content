-- A55 rollback of batch lab10_de (not run)
begin;
delete from public.media_exercise_sets_l10n where learning_language = 'de' and media_id in (8055,236,624,7071,4265,461,62,8039,432,8056);
commit;
