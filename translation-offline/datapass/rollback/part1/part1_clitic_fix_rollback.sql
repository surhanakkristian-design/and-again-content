-- rollback for part1/part1_clitic_fix; NOT run. Restores the backed-up values where the row
-- still holds exactly what the data pass wrote.
begin;
update exercise_localizations l set intro_text = v.n_intro_text, correct_answer = v.n_correct_answer, full_sentence = v.n_full_sentence
from (values
(63343,7039,'sk','Blato bolo hlboké; ... , držali sa stopy.'::text,'napriek tomu'::text,'Blato bolo hlboké; napriek tomu, držali sa stopy.'::text,'Blato bolo hlboké; ... sa držali stopy.'::text,'napriek tomu'::text,'Blato bolo hlboké; napriek tomu sa držali stopy.'::text),
(63346,7039,'cz','Bláto bylo hluboké; ... , drželi se stopy.'::text,'přesto'::text,'Bláto bylo hluboké; přesto, drželi se stopy.'::text,'Bláto bylo hluboké; ... se drželi stopy.'::text,'přesto'::text,'Bláto bylo hluboké; přesto se drželi stopy.'::text),
(64315,7147,'sk','Dres je o dve čísla väčší; ..., Nina ho odmieta vymeniť.'::text,'napriek tomu'::text,'Dres je o dve čísla väčší; napriek tomu, Nina ho odmieta vymeniť.'::text,'Dres je o dve čísla väčší; ... ho Nina odmieta vymeniť.'::text,'napriek tomu'::text,'Dres je o dve čísla väčší; napriek tomu ho Nina odmieta vymeniť.'::text),
(64318,7147,'cz','Dres je o dvě čísla větší; ..., Nina ho odmítá vyměnit.'::text,'přesto'::text,'Dres je o dvě čísla větší; přesto, Nina ho odmítá vyměnit.'::text,'Dres je o dvě čísla větší; ... ho Nina odmítá vyměnit.'::text,'přesto'::text,'Dres je o dvě čísla větší; přesto ho Nina odmítá vyměnit.'::text)
) v(id, eid, lang, n_intro_text, n_correct_answer, n_full_sentence, o_intro_text, o_correct_answer, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.intro_text is not distinct from v.o_intro_text and l.correct_answer is not distinct from v.o_correct_answer and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
