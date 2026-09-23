-- rollback for mismatch_fix/round2; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set intro_text = v.n_intro_text, correct_answer = v.n_correct_answer, distractor_1 = v.n_distractor_1, distractor_2 = v.n_distractor_2, full_sentence = v.n_full_sentence
from (values
(78523,8725,'ua','Кажуть, що ходу ... за два дні.'::text,'організували'::text,'організовують'::text,'організують'::text,'Кажуть, що ходу організували за два дні.'::text,'..., що ходу організували за два дні.'::text,'Кажуть'::text,'Казати'::text,'Кажучи'::text,'Кажуть, що ходу організували за два дні.'::text),
(80404,8934,'ua','Кажуть, що його зміна напрямку ... найшвидша в команді.'::text,'є'::text,'була'::text,'буде'::text,'Кажуть, що його зміна напрямку є найшвидша в команді.'::text,'..., що його зміна напрямку є найшвидша в команді.'::text,'Кажуть'::text,'Казати'::text,'Кажучи'::text,'Кажуть, що його зміна напрямку є найшвидша в команді.'::text),
(140631,15626,'es','Ella añade agua y la harina se ... masa.'::text,'hará'::text,'hace'::text,'hacer'::text,'Ella añade agua y la harina se hará masa.'::text,'Añade agua y la harina se ... masa.'::text,'hará'::text,'hizo'::text,'hacer'::text,'Añade agua y la harina se hará masa.'::text),
(161914,17991,'cz','Kolik ... je na gauči?'::text,'sáčků'::text,'sáčky'::text,'sáčcích'::text,'Kolik sáčků je na gauči?'::text,'... snacků je na gauči?'::text,'Kolik'::text,'Kolika'::text,'Kolikrát'::text,'Kolik snacků je na gauči?'::text),
(161919,17991,'hu','... zacskó van a kanapén?'::text,'Hány'::text,'Mennyi'::text,'Sok'::text,'Hány zacskó van a kanapén?'::text,'... rágcsálnivaló van a kanapén?'::text,'Hány'::text,'Hányan'::text,'Hányszor'::text,'Hány rágcsálnivaló van a kanapén?'::text),
(161911,17991,'sk','Koľko ... je na gauči?'::text,'vreciek'::text,'vrecká'::text,'vreckami'::text,'Koľko vreciek je na gauči?'::text,'... snackov je na gauči?'::text,'Koľko'::text,'Koľkých'::text,'Koľkokrát'::text,'Koľko snackov je na gauči?'::text),
(161917,17991,'ua','Скільки ... на дивані?'::text,'пакетів'::text,'пакети'::text,'пакетами'::text,'Скільки пакетів на дивані?'::text,'... снеків на дивані?'::text,'Скільки'::text,'Скількох'::text,'Скількома'::text,'Скільки снеків на дивані?'::text),
(270258,30029,'es','Tía, ella ha dicho que este palo es ... que el viejo.'::text,'mejor'::text,'mejor'::text,'el mejor'::text,'Tía, ella ha dicho que este palo es mejor que el viejo.'::text,'Tía, él ha dicho que este palo es ... que el viejo.'::text,'mejor'::text,'más mejor'::text,'el mejor'::text,'Tía, él ha dicho que este palo es mejor que el viejo.'::text),
(375236,41693,'tr','O direğin tepesinde yuva ...! Tam bir kâbus!'::text,'tam kaos'::text,'tam bir kaos'::text,'tam kaoslar'::text,'O direğin tepesinde yuva tam kaos! Tam bir kâbus!'::text,'O direğin tepesinde yuva ...! Tam bir kâbus!'::text,'tam kaostu'::text,'tam kaostum'::text,'tam kaoslardı'::text,'O direğin tepesinde yuva tam kaostu! Tam bir kâbus!'::text)
) v(id, eid, lang, n_intro_text, n_correct_answer, n_distractor_1, n_distractor_2, n_full_sentence, o_intro_text, o_correct_answer, o_distractor_1, o_distractor_2, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.intro_text is not distinct from v.o_intro_text and l.correct_answer is not distinct from v.o_correct_answer and l.distractor_1 is not distinct from v.o_distractor_1 and l.distractor_2 is not distinct from v.o_distractor_2 and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
