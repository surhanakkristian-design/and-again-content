-- rollback for punctuation_20260923/judged_hu_full_sentence; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set full_sentence = v.n_full_sentence
from (values
(30501,3389,'hu','Nézd - a játékvezető épp a szabadrúgás helyére mutat'::text,'Nézd - a játékvezető épp a szabadrúgás helyére mutat!'::text),
(103923,11547,'hu','Ne nyisd ki a sütőt, mert a kenyér nem fog megkelni'::text,'Ne nyisd ki a sütőt, mert a kenyér nem fog megkelni!'::text),
(128709,14301,'hu','A repedő jégen áll. Mindjárt el fog esni'::text,'A repedő jégen áll. Mindjárt el fog esni!'::text),
(129078,14342,'hu','A kiszállítás végre itt van'::text,'A kiszállítás végre itt van!'::text),
(130257,14473,'hu','Előretör. Mindjárt megint ugrani fog'::text,'Előretör. Mindjárt megint ugrani fog!'::text),
(138501,15389,'hu','A kocsma tele van hangos foci szurkolókkal'::text,'A kocsma tele van hangos foci szurkolókkal.'::text),
(139878,15542,'hu','Általában megtartják a halat, de ma vissza engedik'::text,'Általában megtartják a halat, de ma vissza engedik.'::text),
(140400,15600,'hu','Nézd azt a madarat! Mindjárt megint rá fog szállni'::text,'Nézd azt a madarat! Mindjárt megint rá fog szállni.'::text),
(141381,15709,'hu','A gépen általában alszik, de most ki néz'::text,'A gépen általában alszik, de most ki néz.'::text),
(141408,15712,'hu','Nézd azokat a felhőket! Mindjárt bele repülünk majd'::text,'Nézd azokat a felhőket! Mindjárt bele repülünk majd.'::text),
(141615,15735,'hu','Nézd! Most éppen a ködből ki fut'::text,'Nézd! Most éppen a ködből ki fut.'::text),
(210249,23361,'hu','A tüsszentés elfújja az összes pitypang magot'::text,'A tüsszentés elfújja az összes pitypang magot.'::text)
) v(id, eid, lang, n_full_sentence, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
