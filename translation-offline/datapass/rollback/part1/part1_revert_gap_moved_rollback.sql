-- rollback for part1/part1_revert_gap_moved; NOT run. Restores the backed-up values where the row
-- still holds exactly what the data pass wrote.
begin;
update exercise_localizations l set intro_text = v.n_intro_text, correct_answer = v.n_correct_answer, full_sentence = v.n_full_sentence
from (values
(350398,38934,'sk','Nikde na grafike ... duny nekončia.'::text,'nekonečné'::text,'Nikde na grafike nekonečné duny nekončia.'::text,'Nikde na grafike ... nekonečné duny nekončia.'::text,''::text,'Nikde na grafike nekonečné duny nekončia.'::text),
(350401,38934,'cz','Nikde na grafice ... duny nekončí.'::text,'nekonečné'::text,'Nikde na grafice nekonečné duny nekončí.'::text,'Nikde na grafice ... nekonečné duny nekončí.'::text,''::text,'Nikde na grafice nekonečné duny nekončí.'::text),
(357409,39713,'sk','Úprimne, pretlačil si sa tou medzerou ako ...'::text,'expert'::text,'Úprimne, pretlačil si sa tou medzerou ako expert.'::text,'Úprimne, pretlačil si sa tou medzerou ako ... expert.'::text,''::text,'Úprimne, pretlačil si sa tou medzerou ako expert.'::text),
(357412,39713,'cz','Upřímně, protáhl ses tou mezerou jako ...'::text,'expert'::text,'Upřímně, protáhl ses tou mezerou jako expert.'::text,'Upřímně, protáhl ses tou mezerou jako ... expert.'::text,''::text,'Upřímně, protáhl ses tou mezerou jako expert.'::text),
(358039,39783,'sk','Zriedka právnik ... na súde také veľké gesto.'::text,'urobí'::text,'Zriedka právnik urobí na súde také veľké gesto.'::text,'Zriedka ... právnik urobí na súde také veľké gesto.'::text,''::text,'Zriedka právnik urobí na súde také veľké gesto.'::text),
(358042,39783,'cz','Zřídka právník ... u soudu tak velké gesto.'::text,'udělá'::text,'Zřídka právník udělá u soudu tak velké gesto.'::text,'Zřídka ... právník udělá u soudu tak velké gesto.'::text,''::text,'Zřídka právník udělá u soudu tak velké gesto.'::text),
(370738,41194,'sk','Zriedka pes po ostrihaní ... takto úhľadne. Mierne pôsobivé.'::text,'vyzerá'::text,'Zriedka pes po ostrihaní vyzerá takto úhľadne. Mierne pôsobivé.'::text,'Zriedka ... pes po ostrihaní vyzerá takto úhľadne. Mierne pôsobivé.'::text,''::text,'Zriedka pes po ostrihaní vyzerá takto úhľadne. Mierne pôsobivé.'::text),
(370741,41194,'cz','Málokdy pes po ostříhání ... takhle úhledně. Mírně působivé.'::text,'vypadá'::text,'Málokdy pes po ostříhání vypadá takhle úhledně. Mírně působivé.'::text,'Málokdy ... pes po ostříhání vypadá takhle úhledně. Mírně působivé.'::text,''::text,'Málokdy pes po ostříhání vypadá takhle úhledně. Mírně působivé.'::text)
) v(id, eid, lang, n_intro_text, n_correct_answer, n_full_sentence, o_intro_text, o_correct_answer, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.intro_text is not distinct from v.o_intro_text and l.correct_answer is not distinct from v.o_correct_answer and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
