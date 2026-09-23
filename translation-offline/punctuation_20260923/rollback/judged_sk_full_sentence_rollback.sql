-- rollback for punctuation_20260923/judged_sk_full_sentence; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set full_sentence = v.n_full_sentence
from (values
(21547,2395,'sk','Ako študentka prechádzala cez túto hranicu každý mesiac a ten istý colník ju vždy pustil'::text,'Ako študentka prechádzala cez túto hranicu každý mesiac a ten istý colník ju vždy pustil.'::text),
(30484,3388,'sk','Ako padala na zem, už vedela, že rozhodkyňa zapíska'::text,'Ako padala na zem, už vedela, že rozhodkyňa zapíska.'::text),
(39925,4437,'sk','Ako tlieska so všetkými ostatnými, želá si, aby bol o dve minúty skôr mlčal'::text,'Ako tlieska so všetkými ostatnými, želá si, aby bol o dve minúty skôr mlčal.'::text),
(103915,11547,'sk','Neotváraj rúru, inak chlieb nevykysne'::text,'Neotváraj rúru, inak chlieb nevykysne!'::text),
(152533,16949,'sk','Koľko debien unesie tento vrtuľník? Unesie ich veľa'::text,'Koľko debien unesie tento vrtuľník? Unesie ich veľa.'::text),
(153811,17091,'sk','Koľko modelov je na polici? Je ich tam veľa'::text,'Koľko modelov je na polici? Je ich tam veľa.'::text)
) v(id, eid, lang, n_full_sentence, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
