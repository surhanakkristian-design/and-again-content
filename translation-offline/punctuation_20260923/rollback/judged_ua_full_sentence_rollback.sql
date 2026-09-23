-- rollback for punctuation_20260923/judged_ua_full_sentence; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set full_sentence = v.n_full_sentence
from (values
(43657,4851,'ua','Він запитав офіціантку, чи розетка за рослиною взагалі працює'::text,'Він запитав офіціантку, чи розетка за рослиною взагалі працює.'::text),
(77038,8560,'ua','Він запитав, чи начальниця знову на них кричала'::text,'Він запитав, чи начальниця знову на них кричала.'::text),
(103921,11547,'ua','Не відкривай піч, бо хліб не підійде'::text,'Не відкривай піч, бо хліб не підійде!'::text),
(152539,16949,'ua','Скільки ящиків підніме цей вертоліт? Він підніме їх багато'::text,'Скільки ящиків підніме цей вертоліт? Він підніме їх багато.'::text),
(153817,17091,'ua','Скільки моделей на полиці? Їх там багато'::text,'Скільки моделей на полиці? Їх там багато.'::text)
) v(id, eid, lang, n_full_sentence, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
