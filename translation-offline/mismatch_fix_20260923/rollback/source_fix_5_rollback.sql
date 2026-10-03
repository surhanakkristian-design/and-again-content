-- rollback for mismatch_fix/source_fix_5; NOT run. Restores the backed-up values where the row still holds
-- exactly what this pass wrote.
begin;
update exercise_localizations l set intro_text = v.n_intro_text, correct_answer = v.n_correct_answer, distractor_1 = v.n_distractor_1, distractor_2 = v.n_distractor_2, full_sentence = v.n_full_sentence
from (values
(243539,27060,'tr','Macera gün batımı ... bitiyor.'::text,''::text,NULL::text,NULL::text,'Macera gün batımı bitiyor.'::text,'Macera ... bitiyor.'::text,'gün batımında'::text,'gün batımına'::text,'gün batımından'::text,'Macera gün batımında bitiyor.'::text),
(287936,31993,'tr','Kürek toprağı çeviriyor ve iki ... ortaya çıkıyor.'::text,'yapraklar'::text,'yapraklar'::text,'yaprak'::text,'Kürek toprağı çeviriyor ve iki yapraklar ortaya çıkıyor.'::text,'Kürek toprağı çeviriyor ve iki ... ortaya çıkıyor.'::text,'yaprak'::text,'yapraklar'::text,'yaprağı'::text,'Kürek toprağı çeviriyor ve iki yaprak ortaya çıkıyor.'::text),
(119708,13301,'tr','Çikolata çok sert. Sen onu ...'::text,'kırabilirsin'::text,'kırabilir'::text,'kırabilmek'::text,'Çikolata çok sert. Sen onu kırabilirsin'::text,'Çikolata çok sert. Sen onu ...?'::text,'kırabilir misin'::text,'kırar mısın'::text,'kırabilir mi'::text,'Çikolata çok sert. Sen onu kırabilir misin?'::text),
(283338,31482,'hu','... kap oda a huskynak? Két játék dinoszaurusz.'::text,'Mi'::text,'Ki'::text,'Mikor'::text,'Mi kap oda a huskynak? Két játék dinoszaurusz.'::text,'... kap a husky után? Két játék dinoszaurusz.'::text,'Mi'::text,'Ki'::text,'Mikor'::text,'Mi kap a husky után? Két játék dinoszaurusz.'::text),
(332145,36905,'hu','Az üzlet arra számít, hogy ... 500 új ügyfelet, amint felszerelik a tévét.'::text,'bevonz'::text,'bevonzva'::text,'bevonzani'::text,'Az üzlet arra számít, hogy bevonz 500 új ügyfelet, amint felszerelik a tévét.'::text,'Az üzlet arra számít, hogy 500 új ügyfelet ..., amint felszerelik a tévét.'::text,'fog vonzani'::text,'fogsz vonzani'::text,'fogja vonzani'::text,'Az üzlet arra számít, hogy 500 új ügyfelet fog vonzani, amint felszerelik a tévét.'::text)
) v(id, eid, lang, n_intro_text, n_correct_answer, n_distractor_1, n_distractor_2, n_full_sentence, o_intro_text, o_correct_answer, o_distractor_1, o_distractor_2, o_full_sentence)
where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and l.intro_text is not distinct from v.o_intro_text and l.correct_answer is not distinct from v.o_correct_answer and l.distractor_1 is not distinct from v.o_distractor_1 and l.distractor_2 is not distinct from v.o_distractor_2 and l.full_sentence is not distinct from v.o_full_sentence
returning l.id;
commit;
