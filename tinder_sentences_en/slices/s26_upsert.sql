begin;
insert into public.tinder_sentences (media_id, language_code, true_sentence, false_sentence, true_phrase, false_phrase, tone, device) values
(302,'en','He is covered in flour!','He is covered in mud!','flour like snow','flour on a cake','dramatic','exaggeration'),
(2500,'en','He is typing on a laptop.','He is typing on a phone.','typing on a laptop','carrying a laptop','chill','none'),
(4909,'en','People are filming her like she is famous.','People are painting her like she is famous.','famous for a minute','famous for her songs','chill','exaggeration'),
(5119,'en','The entrance has wooden gates.','The entrance has glass gates.','the park entrance','the museum entrance','chill','none'),
(1424,'en','The standing colleague wears blue.','The standing colleague wears red.','colleague in a blue shirt','colleague in a red shirt','chill','none')
on conflict (media_id, language_code) do update set true_sentence=excluded.true_sentence, false_sentence=excluded.false_sentence, true_phrase=excluded.true_phrase, false_phrase=excluded.false_phrase, tone=excluded.tone, device=excluded.device, created_at=now();
commit;
