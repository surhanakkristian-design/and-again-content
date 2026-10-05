-- A45 rollback of batch lab10 (NOT run). The rows did not exist before; the audio objects stay in storage.
begin;
delete from public.media_exercise_sets where media_id in (8055,236,624,7071,8056,4265,461,62,8039,432);
commit;
