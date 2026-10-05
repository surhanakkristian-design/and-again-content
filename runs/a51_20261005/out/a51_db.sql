begin;
-- A51 part 3: 4265's French model answer (a parrot hugs with wings, not arms). Native verifiers: verify/out_<lang>.json (only fr had the problem).
do $g$ begin
  if (select tr->'fr'->>'answer' from public.media_exercise_sets where media_id = 4265 and content_version = 2) is distinct from 'Il calme le perroquet en colère en le serrant dans ses bras.'
  then raise exception 'A51: 4265 changed since the backup, nothing written'; end if;
end $g$;
update public.media_exercise_sets
   set tr = jsonb_set(tr, '{fr,answer}', to_jsonb('Il calme le perroquet en colère en lui faisant un câlin.'::text)),
       content_version = 3, updated_at = now()
 where media_id = 4265 and content_version = 2;
do $g$ begin
  if (select count(*) from public.media_exercise_sets where media_id = 4265 and content_version = 3 and tr->'fr'->>'answer' = 'Il calme le perroquet en colère en lui faisant un câlin.') <> 1
  then raise exception 'A51: 4265 not written, rolled back'; end if;
end $g$;
commit;
