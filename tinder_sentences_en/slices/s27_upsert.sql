begin;
insert into public.tinder_sentences (media_id, language_code, true_sentence, false_sentence, true_phrase, false_phrase, tone, device) values
(277,'en','Exercise makes her happy.','Exercise makes her angry.','daily exercise in a garden','daily exercise in a gym','chill','none')
on conflict (media_id, language_code) do update set true_sentence=excluded.true_sentence, false_sentence=excluded.false_sentence, true_phrase=excluded.true_phrase, false_phrase=excluded.false_phrase, tone=excluded.tone, device=excluded.device, created_at=now();
commit;
