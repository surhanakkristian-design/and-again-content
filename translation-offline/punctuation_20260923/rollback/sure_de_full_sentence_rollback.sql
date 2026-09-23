-- rollback for punctuation_20260923/sure_de_full_sentence; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set full_sentence = v.n_full_sentence
from (values
(25446,2828,'de','Beide Arme gaben in derselben Sekunde auf, weil sie so lange gegeneinander gedrückt hatten'::text,'Beide Arme gaben in derselben Sekunde auf, weil sie so lange gegeneinander gedrückt hatten.'::text),
(32466,3608,'de','Der Motor war schon warm, weil das Team ihn seit Sonnenaufgang hatte laufen lassen'::text,'Der Motor war schon warm, weil das Team ihn seit Sonnenaufgang hatte laufen lassen.'::text),
(36759,4085,'de','Bevor er ein Wort sagen konnte, hatte er ein Gänseblümchen hinters Ohr gesteckt'::text,'Bevor er ein Wort sagen konnte, hatte er ein Gänseblümchen hinters Ohr gesteckt.'::text),
(127659,14185,'de','Das Loch ist offen. Die Katze hat vor, hineinzuklettern'::text,'Das Loch ist offen. Die Katze hat vor, hineinzuklettern.'::text)
) v(id, eid, lang, n_full_sentence, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
