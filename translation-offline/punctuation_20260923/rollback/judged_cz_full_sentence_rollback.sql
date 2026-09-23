-- rollback for punctuation_20260923/judged_cz_full_sentence; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set full_sentence = v.n_full_sentence
from (values
(30487,3388,'cz','Jak padala na zem, už věděla, že rozhodčí zapíská'::text,'Jak padala na zem, už věděla, že rozhodčí zapíská.'::text),
(39928,4437,'cz','Jak tleská se všemi ostatními, přeje si, aby byl o dvě minuty dřív mlčel'::text,'Jak tleská se všemi ostatními, přeje si, aby byl o dvě minuty dřív mlčel.'::text),
(103918,11547,'cz','Neotvírej troubu, jinak chleba nevykyne'::text,'Neotvírej troubu, jinak chleba nevykyne!'::text),
(152536,16949,'cz','Kolik beden unese tenhle vrtulník? Unese jich hodně'::text,'Kolik beden unese tenhle vrtulník? Unese jich hodně.'::text),
(153814,17091,'cz','Kolik modelů je na polici? Je jich tam hodně'::text,'Kolik modelů je na polici? Je jich tam hodně.'::text)
) v(id, eid, lang, n_full_sentence, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
