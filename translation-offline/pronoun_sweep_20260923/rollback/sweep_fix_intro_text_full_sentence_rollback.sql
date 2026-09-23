-- rollback for pronoun_sweep_20260923/sweep_fix_intro_text_full_sentence; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set intro_text = v.n_intro_text, full_sentence = v.n_full_sentence
from (values
(25818,2869,'es','La próxima primavera él ... dosis con ese mismo cuentagotas durante treinta años.'::text,'La próxima primavera él habrá estado midiendo dosis con ese mismo cuentagotas durante treinta años.'::text,'La próxima primavera ella ... dosis con ese mismo cuentagotas durante treinta años.'::text,'La próxima primavera ella habrá estado midiendo dosis con ese mismo cuentagotas durante treinta años.'::text)
) v(id, eid, lang, n_intro_text, n_full_sentence, o_intro_text, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.intro_text is not distinct from v.o_intro_text and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
