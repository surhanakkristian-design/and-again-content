begin;
update public.media_exercise_sets
   set tr = jsonb_set(tr, '{fr,answer}', to_jsonb('Il calme le perroquet en colère en le serrant dans ses bras.'::text)), content_version = 2, updated_at = now()
 where media_id = 4265 and content_version = 3 and tr->'fr'->>'answer' = 'Il calme le perroquet en colère en lui faisant un câlin.';
commit;
