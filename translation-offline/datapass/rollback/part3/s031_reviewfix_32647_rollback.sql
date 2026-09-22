-- rollback for part3/s031_reviewfix_32647; NOT run. Restores the backed-up values where the row
-- still holds exactly what the data pass wrote.
begin;
update exercise_localizations l set intro_text = v.n_intro_text, correct_answer = v.n_correct_answer, distractor_1 = v.n_distractor_1, distractor_2 = v.n_distractor_2, full_sentence = v.n_full_sentence
from (values
(293822,32647,'tr','O bisiklette çok hızlı ... İkonik.'::text,''::text,NULL::text,NULL::text,'O bisiklette çok hızlı İkonik.'::text,'İkonik. O bisiklette çok hızlı ...'::text,''::text,NULL::text,NULL::text,'İkonik. O bisiklette çok hızlı.'::text)
) v(id, eid, lang, n_intro_text, n_correct_answer, n_distractor_1, n_distractor_2, n_full_sentence, o_intro_text, o_correct_answer, o_distractor_1, o_distractor_2, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.intro_text is not distinct from v.o_intro_text and l.correct_answer is not distinct from v.o_correct_answer and l.distractor_1 is not distinct from v.o_distractor_1 and l.distractor_2 is not distinct from v.o_distractor_2 and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
