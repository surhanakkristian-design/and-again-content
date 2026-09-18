import json, re, os, sys
os.chdir(os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1b'))
topics = json.load(open('selection/topics.json'))
W, T = 'wrong', 'correct_with_tip'
L = {}
def I(t, kind, v, pattern, sk, cz, en):
    L.setdefault(t, []).append((kind, W if v == 'w' else T, pattern, sk, cz, en))

# ---------------- 50 Past Perfect Continuous ----------------
t = 50
I(t,"Past Continuous instead","w","was/were + -ing instead of had been + -ing for duration up to a past point",
 "Dej trval až do iného minulého bodu, preto Past Perfect Continuous: „{right}“, nie „{wrong}“.",
 "Děj trval až do jiného minulého bodu, proto Past Perfect Continuous: „{right}“, ne „{wrong}“.",
 "It lasted up to a later past moment: Past Perfect Continuous “{right}”, not “{wrong}”.")
I(t,"Past Perfect Simple instead","t","had + past participle instead of had been + -ing (duration stressed)",
 "Dôraz je na trvaní, preto je lepší Past Perfect Continuous: „{right}“.",
 "Důraz je na trvání, proto je lepší Past Perfect Continuous: „{right}“.",
 "The duration is stressed, so Past Perfect Continuous fits better: “{right}”.")
I(t,"Past Simple instead","t","Past Simple instead of had been + -ing before another past event",
 "Na trvanie pred iným minulým dejom sa lepšie hodí Past Perfect Continuous: „{right}“.",
 "Pro trvání před jiným minulým dějem se lépe hodí Past Perfect Continuous: „{right}“.",
 "For duration before another past event, Past Perfect Continuous fits better: “{right}”.")
I(t,"Present Perfect Continuous instead","w","has/have been + -ing in a past story",
 "Všetko je v minulosti, preto „had been“, nie „has been“: „{right}“.",
 "Vše je v minulosti, proto „had been“, ne „has been“: „{right}“.",
 "It is all in the past, so “had been”, not “has been”: “{right}”.")
I(t,"Present Perfect Simple instead","w","has/have + past participle in a past story",
 "Dej je celý v minulosti, preto nie „{wrong}“, ale „{right}“.",
 "Děj je celý v minulosti, proto ne „{wrong}“, ale „{right}“.",
 "It is all in the past, so not “{wrong}”, but “{right}”.")
I(t,"Present Continuous instead","w","is/are + -ing in a past story",
 "Príbeh je v minulosti, preto Past Perfect Continuous: „{right}“.",
 "Příběh je v minulosti, proto Past Perfect Continuous: „{right}“.",
 "The story is in the past, so use Past Perfect Continuous: “{right}”.")
I(t,"missing -ing form","w","had been + base form",
 "Po „had been“ patrí tvar s -ing: „{right}“, nie „{wrong}“.",
 "Po „had been“ následuje tvar s -ing: „{right}“, ne „{wrong}“.",
 "After “had been” use the -ing form: “{right}”, not “{wrong}”.")
I(t,"missing been","w","had + -ing (been dropped)",
 "Chýba „been“: Past Perfect Continuous je „had been“ + -ing: „{right}“.",
 "Chybí „been“: Past Perfect Continuous je „had been“ + -ing: „{right}“.",
 "“been” is missing: Past Perfect Continuous is “had been” + -ing: “{right}”.")
I(t,"missing had","w","been + -ing without had",
 "Chýba pomocné sloveso „had“: „{right}“, nie „{wrong}“.",
 "Chybí pomocné sloveso „had“: „{right}“, ne „{wrong}“.",
 "The auxiliary “had” is missing: “{right}”, not “{wrong}”.")
I(t,"being instead of been","w","had being + -ing",
 "Po „had“ patrí „been“, nie „being“: „{right}“.",
 "Po „had“ následuje „been“, ne „being“: „{right}“.",
 "After “had” use “been”, not “being”: “{right}”.")
I(t,"be instead of been","w","had be + -ing",
 "Po „had“ patrí past participle „been“: „{right}“.",
 "Po „had“ následuje past participle „been“: „{right}“.",
 "After “had” use the past participle “been”: “{right}”.")
I(t,"was instead of had","w","was been + -ing",
 "Past Perfect Continuous sa tvorí s „had“, nie „was“: „{right}“.",
 "Past Perfect Continuous se tvoří s „had“, ne „was“: „{right}“.",
 "Past Perfect Continuous is formed with “had”, not “was”: “{right}”.")
I(t,"PPC for the later event","w","the later short event (before/when clause) also put into had been + -ing or had + participle",
 "Neskorší krátky dej je v Past Simple: „{right}“, nie „{wrong}“.",
 "Pozdější krátký děj je v Past Simple: „{right}“, ne „{wrong}“.",
 "The later, short event takes Past Simple: “{right}”, not “{wrong}”.")
I(t,"since instead of for","w","since + length of time",
 "Pri dĺžke trvania patrí „for“, nie „since“: „{right}“.",
 "U délky trvání patří „for“, ne „since“: „{right}“.",
 "For a length of time use “for”, not “since”: “{right}”.")
I(t,"missing for","w","for dropped before a length of time where it is required",
 "Pri dĺžke trvania chýba „for“: „{right}“.",
 "U délky trvání chybí „for“: „{right}“.",
 "“for” is missing before the length of time: “{right}”.")
I(t,"during instead of for","w","during + length of time",
 "S dĺžkou trvania patrí „for“, nie „during“: „{right}“.",
 "S délkou trvání patří „for“, ne „during“: „{right}“.",
 "With a length of time use “for”, not “during”: “{right}”.")
I(t,"ago with duration","w","'for months' replaced by 'months ago'",
 "„Ago“ sa s trvaním nespája; trvanie vyjadruje „for“: „{right}“.",
 "„Ago“ se s trváním nepojí; trvání vyjadřuje „for“: „{right}“.",
 "“ago” does not go with a duration; use “for”: “{right}”.")
I(t,"stative verb in continuous","w","state verb (know, own, believe) in had been + -ing",
 "Stavové sloveso nemá tvar s -ing, patrí Past Perfect: „{right}“.",
 "Stavové sloveso nemá tvar s -ing, patří Past Perfect: „{right}“.",
 "A state verb has no -ing form here; use Past Perfect: “{right}”.")
I(t,"regular form of irregular verb","w","irregular verb given a regular -ed form elsewhere in the sentence",
 "Nepravidelné sloveso: správny tvar je „{right}“, nie „{wrong}“.",
 "Nepravidelné sloveso: správný tvar je „{right}“, ne „{wrong}“.",
 "Irregular verb: the correct form is “{right}”, not “{wrong}”.")
I(t,"Past Simple in the before-clause wrong","w","the later event put into Present Simple/Perfect instead of Past Simple",
 "Aj neskorší dej je minulý, preto Past Simple: „{right}“, nie „{wrong}“.",
 "I pozdější děj je minulý, proto Past Simple: „{right}“, ne „{wrong}“.",
 "The later event is past too, so Past Simple: “{right}”, not “{wrong}”.")

# ---------------- 51 Future Perfect Simple ----------------
t = 51
I(t,"Future Simple instead","w","will + base form after a 'by …' deadline",
 "„By …“ znamená hotové do toho času, preto Future Perfect: „{right}“, nie „{wrong}“.",
 "„By …“ znamená hotové do té doby, proto Future Perfect: „{right}“, ne „{wrong}“.",
 "“By …” means finished by then, so Future Perfect: “{right}”, not “{wrong}”.")
I(t,"base form after will have","w","will have + base form",
 "Po „will have“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Po „will have“ následuje past participle: „{right}“, ne „{wrong}“.",
 "After “will have” use the past participle: “{right}”, not “{wrong}”.")
I(t,"Past Simple instead of participle","w","will have + Past Simple form (will have took)",
 "Po „will have“ patrí past participle, nie Past Simple: „{right}“.",
 "Po „will have“ následuje past participle, ne Past Simple: „{right}“.",
 "After “will have” use the past participle, not Past Simple: “{right}”.")
I(t,"regularised participle","w","irregular verb with a regular -ed participle (will have writed)",
 "Nepravidelné sloveso: past participle je „{right}“, nie „{wrong}“.",
 "Nepravidelné sloveso: past participle je „{right}“, ne „{wrong}“.",
 "Irregular verb: the past participle is “{right}”, not “{wrong}”.")
I(t,"until instead of by","w","until/till instead of by before the deadline",
 "„Do“ ako termín je „by“, nie „until“: „{right}“.",
 "„Do“ jako termín je „by“, ne „until“: „{right}“.",
 "A deadline takes “by”, not “until”: “{right}”.")
I(t,"to/in instead of by","w","to, in or on instead of by before the deadline",
 "Termín „do …“ sa vyjadruje cez „by“: „{right}“, nie „{wrong}“.",
 "Termín „do …“ se vyjadřuje pomocí „by“: „{right}“, ne „{wrong}“.",
 "A deadline is expressed with “by”: “{right}”, not “{wrong}”.")
I(t,"Future Continuous instead","w","will be + -ing instead of will have + participle",
 "Ide o dej hotový do termínu, nie prebiehajúci: Future Perfect „{right}“.",
 "Jde o děj hotový do termínu, ne probíhající: Future Perfect „{right}“.",
 "The action is finished by then, not in progress: Future Perfect “{right}”.")
I(t,"Present Simple instead","w","Present Simple instead of will have + participle",
 "Dej bude hotový do budúceho termínu, preto Future Perfect: „{right}“.",
 "Děj bude hotový do budoucího termínu, proto Future Perfect: „{right}“.",
 "It will be finished by a future time, so Future Perfect: “{right}”.")
I(t,"Present Perfect instead","w","has/have + participle for a future deadline",
 "Termín je v budúcnosti, preto „will have“, nie „has“: „{right}“.",
 "Termín je v budoucnosti, proto „will have“, ne „has“: „{right}“.",
 "The deadline is in the future, so “will have”, not “has”: “{right}”.")
I(t,"will has","w","will has + participle",
 "Po „will“ je vždy „have“, nie „has“: „{right}“.",
 "Po „will“ je vždy „have“, ne „has“: „{right}“.",
 "After “will” always use “have”, not “has”: “{right}”.")
I(t,"will had","w","will had + participle",
 "Po „will“ je vždy „have“, nie „had“: „{right}“.",
 "Po „will“ je vždy „have“, ne „had“: „{right}“.",
 "After “will” always use “have”, not “had”: “{right}”.")
I(t,"missing have","w","will + participle (have dropped)",
 "Chýba „have“: Future Perfect je „will have“ + past participle: „{right}“.",
 "Chybí „have“: Future Perfect je „will have“ + past participle: „{right}“.",
 "“have” is missing: Future Perfect is “will have” + past participle: “{right}”.")
I(t,"will be + participle","w","will be + participle followed by an object (she will be finished every exercise)",
 "„Will be“ + past participle je Passive; Future Perfect je „will have“: „{right}“.",
 "„Will be“ + past participle je Passive; Future Perfect je „will have“: „{right}“.",
 "“will be” + past participle is Passive; Future Perfect is “will have”: “{right}”.")
I(t,"will have to changes meaning","w","will have to + base form",
 "„Will have to“ znamená „bude musieť“. Hotový dej je „{right}“.",
 "„Will have to“ znamená „bude muset“. Hotový děj je „{right}“.",
 "“will have to” means “must”. The finished action is “{right}”.")
I(t,"going to instead","w","be going to + base after a 'by …' deadline",
 "„By …“ vyžaduje dej hotový do termínu: Future Perfect „{right}“.",
 "„By …“ vyžaduje děj hotový do termínu: Future Perfect „{right}“.",
 "“By …” needs an action finished by then: Future Perfect “{right}”.")
I(t,"Future Perfect Continuous for a result","w","will have been + -ing with a finished result or count",
 "Pri hotovom výsledku alebo počte patrí Future Perfect Simple: „{right}“.",
 "U hotového výsledku nebo počtu patří Future Perfect Simple: „{right}“.",
 "For a finished result or a count, use Future Perfect Simple: “{right}”.")
I(t,"avoids Future Perfect","t","'will be done/finished with' + noun instead of will have + participle",
 "Precvičuje sa Future Perfect: „{right}“.",
 "Procvičuje se Future Perfect: „{right}“.",
 "Practise the Future Perfect here: “{right}”.")
I(t,"article before day or time","w","the added before a day of the week or 'closing time'",
 "Tu sa člen „the“ nepíše: „{right}“.",
 "Zde se člen „the“ nepíše: „{right}“.",
 "No “the” here: “{right}”.")
I(t,"missing article","w","a/an or the dropped before a singular countable noun",
 "Pred počítateľným podstatným menom v jednotnom čísle chýba člen: „{right}“.",
 "Před počitatelným podstatným jménem v jednotném čísle chybí člen: „{right}“.",
 "A singular countable noun needs an article: “{right}”.")
I(t,"plural after every","w","every + plural noun",
 "Po „every“ patrí jednotné číslo: „{right}“.",
 "Po „every“ následuje jednotné číslo: „{right}“.",
 "“every” takes a singular noun: “{right}”.")

# ---------------- 52 Future Perfect Continuous ----------------
t = 52
I(t,"Future Continuous instead","w","will be + -ing instead of will have been + -ing",
 "Trvanie až do budúceho bodu vyjadruje Future Perfect Continuous: „{right}“.",
 "Trvání až do budoucího bodu vyjadřuje Future Perfect Continuous: „{right}“.",
 "Duration up to a future point: Future Perfect Continuous “{right}”.")
I(t,"Future Perfect Simple instead","t","will have + participle where the duration is stressed",
 "Dôraz je na trvaní, preto je lepší Future Perfect Continuous: „{right}“.",
 "Důraz je na trvání, proto je lepší Future Perfect Continuous: „{right}“.",
 "The duration is stressed, so Future Perfect Continuous fits better: “{right}”.")
I(t,"Future Simple instead","w","will + base form with 'by …' and a duration",
 "„By …“ s trvaním vyžaduje Future Perfect Continuous: „{right}“.",
 "„By …“ s trváním vyžaduje Future Perfect Continuous: „{right}“.",
 "“By …” with a duration needs Future Perfect Continuous: “{right}”.")
I(t,"Present Continuous instead","w","is/are + -ing instead of will have been + -ing",
 "Ide o trvanie do budúceho bodu: Future Perfect Continuous „{right}“.",
 "Jde o trvání do budoucího bodu: Future Perfect Continuous „{right}“.",
 "It is duration up to a future point: Future Perfect Continuous “{right}”.")
I(t,"Present Perfect Continuous instead","w","has/have been + -ing for a future point",
 "Bod je v budúcnosti, preto nie „has been“, ale „{right}“.",
 "Bod je v budoucnosti, proto ne „has been“, ale „{right}“.",
 "The point is in the future, so not “has been”, but “{right}”.")
I(t,"missing -ing form","w","will have been + base form",
 "Po „will have been“ patrí tvar s -ing: „{right}“.",
 "Po „will have been“ následuje tvar s -ing: „{right}“.",
 "After “will have been” use the -ing form: “{right}”.")
I(t,"missing been","w","will have + -ing",
 "Chýba „been“: „will have been“ + -ing: „{right}“.",
 "Chybí „been“: „will have been“ + -ing: „{right}“.",
 "“been” is missing: “will have been” + -ing: “{right}”.")
I(t,"missing have","w","will been + -ing",
 "Chýba „have“: „will have been“ + -ing: „{right}“.",
 "Chybí „have“: „will have been“ + -ing: „{right}“.",
 "“have” is missing: “will have been” + -ing: “{right}”.")
I(t,"will has been","w","will has been + -ing",
 "Po „will“ je vždy „have“, nie „has“: „{right}“.",
 "Po „will“ je vždy „have“, ne „has“: „{right}“.",
 "After “will” always use “have”, not “has”: “{right}”.")
I(t,"being instead of been","w","will have being + -ing",
 "Po „will have“ patrí „been“, nie „being“: „{right}“.",
 "Po „will have“ následuje „been“, ne „being“: „{right}“.",
 "After “will have” use “been”, not “being”: “{right}”.")
I(t,"will be been","w","will be been + -ing",
 "Future Perfect Continuous je „will have been“ + -ing: „{right}“, nie „{wrong}“.",
 "Future Perfect Continuous je „will have been“ + -ing: „{right}“, ne „{wrong}“.",
 "Future Perfect Continuous is “will have been” + -ing: “{right}”, not “{wrong}”.")
I(t,"going to instead","w","be going to + base with 'by …' and a duration",
 "„Going to“ nevyjadrí trvanie do bodu; treba „{right}“.",
 "„Going to“ nevyjádří trvání do bodu; je potřeba „{right}“.",
 "“going to” does not show duration up to a point; use “{right}”.")
I(t,"since instead of for","w","since + length of time",
 "Pri dĺžke trvania patrí „for“, nie „since“: „{right}“.",
 "U délky trvání patří „for“, ne „since“: „{right}“.",
 "For a length of time use “for”, not “since”: “{right}”.")
I(t,"missing for","w","for dropped before a length of time where it is required (not with 'straight')",
 "Pri dĺžke trvania chýba „for“: „{right}“.",
 "U délky trvání chybí „for“: „{right}“.",
 "“for” is missing before the length of time: “{right}”.")
I(t,"during instead of for","w","during + length of time",
 "S dĺžkou trvania patrí „for“, nie „during“: „{right}“.",
 "S délkou trvání patří „for“, ne „during“: „{right}“.",
 "With a length of time use “for”, not “during”: “{right}”.")
I(t,"until instead of by","w","until/till instead of by before the future point",
 "Časový bod „do …“ je „by“, nie „until“: „{right}“.",
 "Časový bod „do …“ je „by“, ne „until“: „{right}“.",
 "A point in time takes “by”, not “until”: “{right}”.")
I(t,"duration before the verb","w","'for + time' moved between will have been and the verb",
 "Údaj o trvaní patrí až za sloveso a predmet: „{right}“.",
 "Údaj o trvání patří až za sloveso a předmět: „{right}“.",
 "Put the duration after the verb and object: “{right}”.")
I(t,"stative verb in continuous","w","state verb (know, own, belong) in will have been + -ing",
 "Stavové sloveso nemá tvar s -ing; patrí Future Perfect: „{right}“.",
 "Stavové sloveso nemá tvar s -ing; patří Future Perfect: „{right}“.",
 "A state verb has no -ing form here; use Future Perfect: “{right}”.")
I(t,"avoids Future Perfect Continuous","t","rephrased as 'it will be X years since …' or similar",
 "Precvičuje sa Future Perfect Continuous: „{right}“.",
 "Procvičuje se Future Perfect Continuous: „{right}“.",
 "Practise Future Perfect Continuous here: “{right}”.")
I(t,"this instead of these","w","this/that with a plural noun",
 "Pri množnom čísle patrí „these“ alebo „those“: „{right}“.",
 "U množného čísla patří „these“ nebo „those“: „{right}“.",
 "A plural noun takes “these” or “those”: “{right}”.")

# ---------------- 53 Third Conditional ----------------
t = 53
I(t,"Second Conditional instead","w","Past Simple + would + base for an unreal past",
 "Ide o minulosť, ktorá sa nestala, preto Third Conditional: „{right}“.",
 "Jde o minulost, která se nestala, proto Third Conditional: „{right}“.",
 "An unreal past situation needs the Third Conditional: “{right}”.")
I(t,"would in if-clause","w","would (have) + verb after if",
 "Po „if“ nepatrí „would“; v Third Conditional je tam Past Perfect: „{right}“.",
 "Po „if“ nepatří „would“; ve Third Conditional je tam Past Perfect: „{right}“.",
 "No “would” after “if”; the Third Conditional uses Past Perfect: “{right}”.")
I(t,"Past Simple in if-clause","w","Past Simple instead of Past Perfect after if (result clause kept)",
 "Podmienka je v minulosti, preto po „if“ Past Perfect: „{right}“, nie „{wrong}“.",
 "Podmínka je v minulosti, proto po „if“ Past Perfect: „{right}“, ne „{wrong}“.",
 "The condition is past, so Past Perfect after “if”: “{right}”, not “{wrong}”.")
I(t,"Present Perfect in if-clause","w","has/have + participle after if",
 "Po „if“ v Third Conditional patrí Past Perfect: „{right}“, nie „{wrong}“.",
 "Po „if“ ve Third Conditional patří Past Perfect: „{right}“, ne „{wrong}“.",
 "After “if” the Third Conditional uses Past Perfect: “{right}”, not “{wrong}”.")
I(t,"present result for a past result","w","would + base where the result is clearly over (event finished)",
 "Následok je tiež v minulosti: „{right}“, nie „{wrong}“.",
 "Následek je také v minulosti: „{right}“, ne „{wrong}“.",
 "The result is in the past too: “{right}”, not “{wrong}”.")
I(t,"present result that could be mixed","t","would + base where a present result still makes sense",
 "Následok je v minulosti, preto v Third Conditional: „{right}“.",
 "Následek je v minulosti, proto ve Third Conditional: „{right}“.",
 "The result is in the past, so the Third Conditional: “{right}”.")
I(t,"past result instead of present","t","would have + participle where the result is true now (Mixed)",
 "Následok platí teraz, preto „{right}“, nie „{wrong}“.",
 "Následek platí teď, proto „{right}“, ne „{wrong}“.",
 "The result is true now, so “{right}”, not “{wrong}”.")
I(t,"would had","w","would had + participle",
 "Po „would“ patrí vždy „have“, nie „had“: „{right}“.",
 "Po „would“ je vždy „have“, ne „had“: „{right}“.",
 "After “would” always use “have”, not “had”: “{right}”.")
I(t,"would of","w","would of / could of instead of would have",
 "Píše sa „would have“ (skrátene „would've“), nie „would of“.",
 "Píše se „would have“ (zkráceně „would've“), ne „would of“.",
 "Write “would have” (or “would've”), not “would of”.")
I(t,"missing have","w","would + participle (have dropped)",
 "Chýba „have“: „would have“ + past participle: „{right}“.",
 "Chybí „have“: „would have“ + past participle: „{right}“.",
 "“have” is missing: “would have” + past participle: “{right}”.")
I(t,"base form after would have","w","would have + base form",
 "Po „would have“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Po „would have“ následuje past participle: „{right}“, ne „{wrong}“.",
 "After “would have” use the past participle: “{right}”, not “{wrong}”.")
I(t,"base form after had","w","if + had + base form",
 "Po „had“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Po „had“ následuje past participle: „{right}“, ne „{wrong}“.",
 "After “had” use the past participle: “{right}”, not “{wrong}”.")
I(t,"Past Simple form as participle","w","had/have + Past Simple form (would have went)",
 "Za „have/had“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Za „have/had“ patří past participle: „{right}“, ne „{wrong}“.",
 "After “have/had” use the past participle: “{right}”, not “{wrong}”.")
I(t,"will have in main clause","w","will have + participle in the result clause",
 "V Third Conditional patrí „would have“, nie „will have“: „{right}“.",
 "Ve Third Conditional patří „would have“, ne „will have“: „{right}“.",
 "The Third Conditional uses “would have”, not “will have”: “{right}”.")
I(t,"Past Perfect in main clause","w","had + participle in the result clause instead of would have",
 "V hlavnej vete patrí „would have“ + past participle: „{right}“.",
 "V hlavní větě patří „would have“ + past participle: „{right}“.",
 "The result clause needs “would have” + past participle: “{right}”.")
I(t,"when instead of if","w","when instead of if for an unreal condition",
 "„Keby“ je „if“; „when“ znamená „keď“ (naozaj sa stalo).",
 "„Kdyby“ je „if“; „when“ znamená „když“ (opravdu se stalo).",
 "An unreal condition takes “if”; “when” means it really happened.")
I(t,"unless misused","w","unless used for 'if … not' with an unreal past",
 "„Unless“ tu mení význam; patrí „if … not“: „{right}“.",
 "„Unless“ tu mění význam; patří „if … not“: „{right}“.",
 "“unless” changes the meaning here; use “if … not”: “{right}”.")
I(t,"double negation","w","two negatives in one clause (wouldn't … no)",
 "V angličtine je len jeden zápor: „{right}“.",
 "V angličtině je jen jeden zápor: „{right}“.",
 "English allows only one negative here: “{right}”.")
I(t,"still after be before adverb","w","still placed after be before an adverb/adjective (would be still here)",
 "„Still“ patrí hneď za „would“: „{right}“.",
 "„Still“ patří hned za „would“: „{right}“.",
 "“still” goes right after “would”: “{right}”.")
I(t,"still after be before -ing","t","still placed after be before an -ing form (would be still crying)",
 "Prirodzenejšie stojí „still“ hneď za „would“: „{right}“.",
 "Přirozeněji stojí „still“ hned za „would“: „{right}“.",
 "“still” sounds more natural right after “would”: “{right}”.")
I(t,"more with short word","w","more + short adjective/adverb (more early, more thick)",
 "Krátke slovo stupňujeme príponou: „{right}“, nie „{wrong}“.",
 "Krátké slovo stupňujeme příponou: „{right}“, ne „{wrong}“.",
 "A short word takes -er: “{right}”, not “{wrong}”.")

# ---------------- 54 Mixed Conditional ----------------
t = 54
I(t,"Third Conditional instead","t","if + had been for a condition that is still true (permanent trait)",
 "Podmienka platí stále, preto v Mixed Conditional: „{right}“.",
 "Podmínka platí stále, proto v Mixed Conditional: „{right}“.",
 "The condition is still true, so the Mixed Conditional: “{right}”.")
I(t,"present result instead of past","w","would + base where the result would already have happened",
 "Následok by sa už stal, preto „{right}“, nie „{wrong}“.",
 "Následek by už nastal, proto „{right}“, ne „{wrong}“.",
 "The result would already have happened: “{right}”, not “{wrong}”.")
I(t,"Third Conditional result with now","w","would have + participle for a result true now",
 "Následok platí teraz, preto „{right}“, nie „{wrong}“.",
 "Následek platí teď, proto „{right}“, ne „{wrong}“.",
 "The result is true now, so “{right}”, not “{wrong}”.")
I(t,"would in if-clause","w","would + verb after if",
 "Po „if“ nepatrí „would“: „{right}“, nie „{wrong}“.",
 "Po „if“ nepatří „would“: „{right}“, ne „{wrong}“.",
 "No “would” after “if”: “{right}”, not “{wrong}”.")
I(t,"Present Simple in if-clause","w","Present Simple after if for an unreal present condition",
 "Neskutočnú prítomnú podmienku vyjadruje Past Simple: „{right}“.",
 "Neskutečnou přítomnou podmínku vyjadřuje Past Simple: „{right}“.",
 "An unreal present condition takes Past Simple: “{right}”.")
I(t,"Past Simple in if-clause","w","Past Simple after if for a past cause",
 "Príčina je v minulosti, preto po „if“ Past Perfect: „{right}“.",
 "Příčina je v minulosti, proto po „if“ Past Perfect: „{right}“.",
 "The cause is in the past, so Past Perfect after “if”: “{right}”.")
I(t,"Present Perfect in if-clause","w","has/have + participle after if",
 "Po „if“ patrí Past Perfect, nie Present Perfect: „{right}“.",
 "Po „if“ patří Past Perfect, ne Present Perfect: „{right}“.",
 "After “if” use Past Perfect, not Present Perfect: “{right}”.")
I(t,"was instead of were","t","if + I/he/she/it was instead of were",
 "Po „if“ je štandardné „were“: „{right}“.",
 "Po „if“ je standardní „were“: „{right}“.",
 "After “if”, “were” is the standard form: “{right}”.")
I(t,"will in main clause","w","will instead of would in the result clause",
 "Neskutočný následok je s „would“, nie „will“: „{right}“.",
 "Neskutečný následek je s „would“, ne „will“: „{right}“.",
 "An unreal result takes “would”, not “will”: “{right}”.")
I(t,"First Conditional instead","w","real condition (is/will) instead of an unreal one",
 "Ide o neskutočnú situáciu: „{right}“, nie „{wrong}“.",
 "Jde o neskutečnou situaci: „{right}“, ne „{wrong}“.",
 "The situation is unreal: “{right}”, not “{wrong}”.")
I(t,"missing would in main clause","w","result clause in plain present/past without would",
 "V hlavnej vete chýba „would“: „{right}“.",
 "V hlavní větě chybí „would“: „{right}“.",
 "The result clause needs “would”: “{right}”.")
I(t,"would had","w","would had + participle",
 "Po „would“ patrí vždy „have“, nie „had“: „{right}“.",
 "Po „would“ je vždy „have“, ne „had“: „{right}“.",
 "After “would” always use “have”, not “had”: “{right}”.")
I(t,"base form after had","w","if + had + base form",
 "Po „had“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Po „had“ následuje past participle: „{right}“, ne „{wrong}“.",
 "After “had” use the past participle: “{right}”, not “{wrong}”.")
I(t,"unless misused","w","unless used for 'if … not' in an unreal condition",
 "„Unless“ tu mení význam; patrí „if … not“: „{right}“.",
 "„Unless“ tu mění význam; patří „if … not“: „{right}“.",
 "“unless” changes the meaning here; use “if … not”: “{right}”.")
I(t,"when instead of if","w","when instead of if for an unreal condition",
 "„Keby“ je „if“; „when“ znamená „keď“ (naozaj).",
 "„Kdyby“ je „if“; „when“ znamená „když“ (opravdu).",
 "An unreal condition takes “if”; “when” means it really happens.")
I(t,"yet instead of already","w","yet in a positive clause for 'already'",
 "„Už“ v kladnej vete je „already“; „yet“ patrí do záporu a otázok.",
 "„Už“ v kladné větě je „already“; „yet“ patří do záporu a otázek.",
 "Use “already” in a positive clause; “yet” is for negatives and questions.")
I(t,"such instead of so","w","such + adjective without a noun",
 "Pred samotným prídavným menom patrí „so“, nie „such“: „{right}“.",
 "Před samotným přídavným jménem patří „so“, ne „such“: „{right}“.",
 "Before an adjective alone use “so”, not “such”: “{right}”.")
I(t,"more with short adjective","w","more + short adjective (more thick)",
 "Krátke prídavné meno stupňujeme príponou: „{right}“, nie „{wrong}“.",
 "Krátké přídavné jméno stupňujeme příponou: „{right}“, ne „{wrong}“.",
 "A short adjective takes -er: “{right}”, not “{wrong}”.")
I(t,"article with uncountable noun","w","a/an before an uncountable noun (a paper, an advice)",
 "Nepočítateľné podstatné meno je bez „a“: „{right}“.",
 "Nepočitatelné podstatné jméno je bez „a“: „{right}“.",
 "An uncountable noun takes no “a”: “{right}”.")
I(t,"all them word order","w","'all them' instead of 'them all' / 'all of them'",
 "Správne je „them all“ alebo „all of them“, nie „all them“.",
 "Správně je „them all“ nebo „all of them“, ne „all them“.",
 "Say “them all” or “all of them”, not “all them”.")

# ---------------- 55 Advanced Passive Voice ----------------
t = 55
I(t,"simple instead of perfect Infinitive","w","is said to + base for an earlier action",
 "Dej bol skôr, preto perfect Infinitive: „{right}“, nie „{wrong}“.",
 "Děj byl dříve, proto perfect Infinitive: „{right}“, ne „{wrong}“.",
 "The action was earlier, so the perfect Infinitive: “{right}”, not “{wrong}”.")
I(t,"perfect instead of simple Infinitive","w","is said to have + participle for something true now",
 "Platí to teraz, preto jednoduchý Infinitive: „{right}“, nie „{wrong}“.",
 "Platí to teď, proto prostý Infinitive: „{right}“, ne „{wrong}“.",
 "It is true now, so the simple Infinitive: “{right}”, not “{wrong}”.")
I(t,"is said that it","w","subject + is said + that-clause (mixing personal and impersonal passive)",
 "Po podmete s „is said“ nasleduje Infinitive, nie „that“: „{right}“.",
 "Po podmětu s „is said“ následuje Infinitive, ne „that“: „{right}“.",
 "After a subject + “is said” use the Infinitive, not “that”: “{right}”.")
I(t,"active instead of Passive","t","People say / They say + clause instead of the passive",
 "Precvičuje sa Passive: „{right}“.",
 "Procvičuje se Passive: „{right}“.",
 "Practise the Passive here: “{right}”.")
I(t,"supposed to instead of said","t","is supposed to / is believed to instead of the practised is said to",
 "Precvičuje sa Passive so slovesom „say“: „{right}“.",
 "Procvičuje se Passive se slovesem „say“: „{right}“.",
 "Practise the Passive with “say”: “{right}”.")
I(t,"Past Simple instead of participle","w","to have + Past Simple form (to have took)",
 "Po „to have“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Po „to have“ následuje past participle: „{right}“, ne „{wrong}“.",
 "After “to have” use the past participle: “{right}”, not “{wrong}”.")
I(t,"base form after to have","w","to have + base form",
 "Po „to have“ patrí past participle: „{right}“.",
 "Po „to have“ následuje past participle: „{right}“.",
 "After “to have” use the past participle: “{right}”.")
I(t,"Gerund instead of Infinitive","w","is said + -ing",
 "Po „is said“ patrí Infinitive: „{right}“, nie „{wrong}“.",
 "Po „is said“ následuje Infinitive: „{right}“, ne „{wrong}“.",
 "After “is said” use the Infinitive: “{right}”, not “{wrong}”.")
I(t,"missing to","w","is said + base form without to",
 "Po „is said“ patrí „to“ + sloveso: „{right}“.",
 "Po „is said“ následuje „to“ + sloveso: „{right}“.",
 "After “is said” use “to” + verb: “{right}”.")
I(t,"calque It says","w","It says (that) … for 'hovorí sa'",
 "„It says“ znamená, že je to niekde napísané. Treba Passive: „{right}“.",
 "„It says“ znamená, že je to někde napsané. Je potřeba Passive: „{right}“.",
 "“It says” means it is written somewhere. Use the Passive: “{right}”.")
I(t,"calque About … is said","w","About X is said (that) … word-for-word from 'o … sa hovorí'",
 "Doslovné „About … is said“ nefunguje; treba „{right}“.",
 "Doslovné „About … is said“ nefunguje; je potřeba „{right}“.",
 "A word-for-word “About … is said” does not work; use “{right}”.")
I(t,"missing subject it","w","Is said that … without It",
 "Chýba podmet „It“: „It is said that…“.",
 "Chybí podmět „It“: „It is said that…“.",
 "The subject “It” is missing: “It is said that…”.")
I(t,"active form with thing as subject","w","thing + says/believes (This mascara says to …)",
 "Vec nič nehovorí; treba Passive: „{right}“.",
 "Věc nic neříká; je potřeba Passive: „{right}“.",
 "The thing says nothing itself; use the Passive: “{right}”.")
I(t,"missing be in Passive","w","passive without a form of be (The treaty said to …)",
 "Passive potrebuje tvar „be“: „{right}“, nie „{wrong}“.",
 "Passive potřebuje tvar „be“: „{right}“, ne „{wrong}“.",
 "The Passive needs a form of “be”: “{right}”, not “{wrong}”.")
I(t,"wrong tense of reporting verb","w","was said / has been said instead of present is said",
 "„Hovorí sa“ je v prítomnosti: „{right}“, nie „{wrong}“.",
 "„Říká se“ je v přítomnosti: „{right}“, ne „{wrong}“.",
 "The reporting verb is present here: “{right}”, not “{wrong}”.")
I(t,"unnecessary by people","t","passive + by people / by everyone",
 "„By people“ je zbytočné; stačí „{right}“.",
 "„By people“ je zbytečné; stačí „{right}“.",
 "“by people” is unnecessary; just “{right}”.")
I(t,"active Gerund instead of passive Gerund","w","verb + -ing where being + participle is needed (likes rushing)",
 "Podmet dej nerobí, ale znáša: passive Gerund „{right}“, nie „{wrong}“.",
 "Podmět děj nedělá, ale snáší: passive Gerund „{right}“, ne „{wrong}“.",
 "The subject receives the action: passive Gerund “{right}”, not “{wrong}”.")
I(t,"been instead of being","w","verb + been + participle instead of being + participle",
 "Passive Gerund je „being“ + past participle: „{right}“.",
 "Passive Gerund je „being“ + past participle: „{right}“.",
 "The passive Gerund is “being” + past participle: “{right}”.")
I(t,"Passive Continuous missing being","w","is + participle for an action in progress (is repaired now)",
 "Dej práve prebieha: Passive Continuous „{right}“, nie „{wrong}“.",
 "Děj právě probíhá: Passive Continuous „{right}“, ne „{wrong}“.",
 "It is happening now: Passive Continuous “{right}”, not “{wrong}”.")
I(t,"regularised participle","w","irregular verb with a regular -ed participle in the passive",
 "Nepravidelné sloveso: past participle je „{right}“, nie „{wrong}“.",
 "Nepravidelné sloveso: past participle je „{right}“, ne „{wrong}“.",
 "Irregular verb: the past participle is “{right}”, not “{wrong}”.")
I(t,"for + -ing after take + time","w","take + time + for + -ing instead of to + verb",
 "Po „take + čas“ patrí Infinitive: „{right}“.",
 "Po „take + čas“ následuje Infinitive: „{right}“.",
 "After “take + time” use the Infinitive: “{right}”.")

# ---------------- 56 Reported speech ----------------
t = 56
I(t,"Past Simple instead of Past Perfect","t","reported earlier action in Past Simple instead of had + participle",
 "Dej bol pred oznámením, preto je lepší Past Perfect: „{right}“.",
 "Děj byl před oznámením, proto je lepší Past Perfect: „{right}“.",
 "The action came before the reporting, so Past Perfect fits better: “{right}”.")
I(t,"question word order","w","auxiliary before the subject in a reported question",
 "V Reported speech nie je otázkový slovosled: „{right}“, nie „{wrong}“.",
 "V Reported speech není tázací slovosled: „{right}“, ne „{wrong}“.",
 "Reported questions use statement word order: “{right}”, not “{wrong}”.")
I(t,"direct question with did","w","did + base kept in a reported question",
 "Reported speech nepoužíva „did“: „{right}“.",
 "Reported speech nepoužívá „did“: „{right}“.",
 "Reported questions do not use “did”: “{right}”.")
I(t,"direct question kept","w","direct question form (is/are/do + subject) after asked",
 "Toto je priama otázka. V Reported speech: „{right}“.",
 "Toto je přímá otázka. V Reported speech: „{right}“.",
 "That is a direct question. In Reported speech: “{right}”.")
I(t,"no backshift, situation over","w","has/have + participle kept after a past reporting verb when the situation is clearly over",
 "Po minulom slovese sa čas posúva: „{right}“, nie „{wrong}“.",
 "Po minulém slovese se čas posouvá: „{right}“, ne „{wrong}“.",
 "After a past reporting verb the tense moves back: “{right}”, not “{wrong}”.")
I(t,"no backshift, may still be true","t","present tense kept after a past reporting verb when it may still be true",
 "Po minulom slovese sa čas zvyčajne posúva: „{right}“.",
 "Po minulém slovese se čas obvykle posouvá: „{right}“.",
 "After a past reporting verb the tense usually moves back: “{right}”.")
I(t,"Past Simple instead of Past Continuous","w","Past Simple for an action that was in progress (meaning: finished)",
 "Dej prebiehal, preto Past Continuous: „{right}“, nie „{wrong}“.",
 "Děj probíhal, proto Past Continuous: „{right}“, ne „{wrong}“.",
 "The action was in progress, so Past Continuous: “{right}”, not “{wrong}”.")
I(t,"Present Simple in reported speech","w","Present Simple for an action in progress after a past verb",
 "Ide o dej v priebehu po minulom slovese: „{right}“.",
 "Jde o děj v průběhu po minulém slovese: „{right}“.",
 "It is an action in progress after a past verb: “{right}”.")
I(t,"will instead of would","w","will kept after a past reporting verb",
 "Po minulom slovese sa „will“ mení na „would“: „{right}“.",
 "Po minulém slovese se „will“ mění na „would“: „{right}“.",
 "After a past reporting verb “will” becomes “would”: “{right}”.")
I(t,"can instead of could","w","can kept after a past reporting verb",
 "Po minulom slovese sa „can“ mení na „could“: „{right}“.",
 "Po minulém slovese se „can“ mění na „could“: „{right}“.",
 "After a past reporting verb “can” becomes “could”: “{right}”.")
I(t,"Past Simple with how long","w","how long + Past Simple instead of had been",
 "„How long“ až po moment otázky vyžaduje Past Perfect: „{right}“.",
 "„How long“ až do chvíle otázky vyžaduje Past Perfect: „{right}“.",
 "“how long” up to the moment of asking needs Past Perfect: “{right}”.")
I(t,"that instead of if/whether","w","asked (me) that … for a yes/no question",
 "Pri otázke áno/nie patrí „if“ alebo „whether“, nie „that“.",
 "U otázky ano/ne patří „if“ nebo „whether“, ne „that“.",
 "A yes/no question takes “if” or “whether”, not “that”.")
I(t,"missing if/whether","w","asked + clause without if/whether",
 "Pri otázke áno/nie chýba „if“ alebo „whether“.",
 "U otázky ano/ne chybí „if“ nebo „whether“.",
 "A yes/no question needs “if” or “whether”.")
I(t,"said + person","w","said me / said him (person directly after say)",
 "Po „say“ nenasleduje osoba priamo: „told me“ alebo „said to me“.",
 "Po „say“ nenásleduje osoba přímo: „told me“ nebo „said to me“.",
 "“say” takes no direct person: “told me” or “said to me”.")
I(t,"tell without person","w","told that … without a person",
 "Po „tell“ patrí osoba: „told me that…“; inak „said that…“.",
 "Po „tell“ následuje osoba: „told me that…“; jinak „said that…“.",
 "“tell” needs a person: “told me that…”; otherwise “said that…”.")
I(t,"pronoun not shifted","w","possessive/personal pronoun not adapted to the reporter's view",
 "Zámeno sa mení podľa osoby: „{right}“, nie „{wrong}“.",
 "Zájmeno se mění podle osoby: „{right}“, ne „{wrong}“.",
 "The pronoun changes to fit the speaker: “{right}”, not “{wrong}”.")
I(t,"time word not shifted","t","tomorrow/yesterday/now kept after a past reporting verb",
 "V Reported speech sa časový údaj zvyčajne mení: „{right}“.",
 "V Reported speech se časový údaj obvykle mění: „{right}“.",
 "In Reported speech the time word usually changes: “{right}”.")
I(t,"insist on changes meaning","w","insisted on + -ing instead of insisted that …",
 "„Insisted on“ + -ing znamená trvať na čine; „tvrdiť, že“ je „insisted that“.",
 "„Insisted on“ + -ing znamená trvat na činu; „tvrdit, že“ je „insisted that“.",
 "“insisted on” + -ing means demanding it; “claimed” is “insisted that”.")
I(t,"direct speech instead","t","quoted direct speech instead of reported speech",
 "Precvičuje sa Reported speech: „{right}“.",
 "Procvičuje se Reported speech: „{right}“.",
 "Practise Reported speech here: “{right}”.")
I(t,"asked about if","w","asked about whether/if",
 "Za „asked“ nepatrí „about“ pred „if/whether“.",
 "Za „asked“ nepatří „about“ před „if/whether“.",
 "No “about” between “asked” and “if/whether”.")

# ---------------- 57 Modals in past ----------------
t = 57
I(t,"modal + base for the past","w","could/should/might + base form instead of modal + have + participle",
 "O minulosti: modálne sloveso + „have“ + past participle: „{right}“.",
 "O minulosti: modální sloveso + „have“ + past participle: „{right}“.",
 "For the past use modal + “have” + past participle: “{right}”.")
I(t,"base form after modal have","w","should/could have + base form",
 "Po „have“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Po „have“ následuje past participle: „{right}“, ne „{wrong}“.",
 "After “have” use the past participle: “{right}”, not “{wrong}”.")
I(t,"Past Simple instead of participle","w","modal have + Past Simple form (should have drew)",
 "Po „have“ patrí past participle, nie Past Simple: „{right}“.",
 "Po „have“ následuje past participle, ne Past Simple: „{right}“.",
 "After “have” use the past participle, not Past Simple: “{right}”.")
I(t,"regularised participle","w","irregular verb with a regular -ed participle (drawed)",
 "Nepravidelné sloveso: past participle je „{right}“, nie „{wrong}“.",
 "Nepravidelné sloveso: past participle je „{right}“, ne „{wrong}“.",
 "Irregular verb: the past participle is “{right}”, not “{wrong}”.")
I(t,"had instead of have","w","modal + had + participle (should had)",
 "Po modálnom slovese je vždy „have“, nie „had“: „{right}“.",
 "Po modálním slovese je vždy „have“, ne „had“: „{right}“.",
 "After a modal always use “have”, not “had”: “{right}”.")
I(t,"modal of","w","should of / could of / would of",
 "Píše sa „{right}“, nie „… of“.",
 "Píše se „{right}“, ne „… of“.",
 "Write “{right}”, not “… of”.")
I(t,"missing have","w","modal + participle (have dropped)",
 "Chýba „have“: „{right}“, nie „{wrong}“.",
 "Chybí „have“: „{right}“, ne „{wrong}“.",
 "“have” is missing: “{right}”, not “{wrong}”.")
I(t,"was able to changes meaning","w","was able to + verb for an unused possibility",
 "„Was able to“ znamená, že sa to podarilo; nevyužitú možnosť vyjadrí „{right}“.",
 "„Was able to“ znamená, že se to podařilo; nevyužitou možnost vyjádří „{right}“.",
 "“was able to” means it happened; an unused chance is “{right}”.")
I(t,"had to changes meaning","w","had to + verb for a reproach about the past",
 "„Had to“ vyjadruje splnenú povinnosť; výčitku za minulosť vyjadrí „{right}“.",
 "„Had to“ vyjadřuje splněnou povinnost; výčitku za minulost vyjádří „{right}“.",
 "“had to” is an obligation that was met; a past reproach is “{right}”.")
I(t,"would instead of could","w","would have instead of could have for a possibility",
 "„Would have“ je podmienka, nie možnosť; tu patrí „{right}“.",
 "„Would have“ je podmínka, ne možnost; tady patří „{right}“.",
 "“would have” is a condition, not a possibility; use “{right}”.")
I(t,"must have for reproach","w","must have + participle (deduction) instead of should have",
 "„Must have“ znamená „určite“; výčitku vyjadrí „{right}“.",
 "„Must have“ znamená „určitě“; výčitku vyjádří „{right}“.",
 "“must have” means “surely”; a reproach is “{right}”.")
I(t,"must have instead of can't have","w","must have where the sense is 'surely not' (opposite meaning)",
 "Ide o istotu, že sa to nestalo: „{right}“, nie „{wrong}“.",
 "Jde o jistotu, že se to nestalo: „{right}“, ne „{wrong}“.",
 "It is certain it did not happen: “{right}”, not “{wrong}”.")
I(t,"mustn't have instead of can't have","w","mustn't have for a negative deduction",
 "Záporný záver o minulosti je „can't have“, nie „mustn't have“.",
 "Záporný závěr o minulosti je „can't have“, ne „mustn't have“.",
 "A negative deduction about the past is “can't have”, not “mustn't have”.")
I(t,"might instead of could","t","might have for an unused possibility",
 "„Might have“ je skôr dohad; nevyužitú možnosť presnejšie vyjadrí „{right}“.",
 "„Might have“ je spíš dohad; nevyužitou možnost přesněji vyjádří „{right}“.",
 "“might have” is more a guess; an unused chance is better “{right}”.")
I(t,"ought to have instead of should have","t","ought to have + participle",
 "Precvičuje sa „should have“: „{right}“.",
 "Procvičuje se „should have“: „{right}“.",
 "Practise “should have” here: “{right}”.")
I(t,"was supposed to instead","t","was supposed to + verb instead of should have + participle",
 "Precvičuje sa modálne sloveso + „have“ + past participle: „{right}“.",
 "Procvičuje se modální sloveso + „have“ + past participle: „{right}“.",
 "Practise modal + “have” + past participle here: “{right}”.")
I(t,"didn't need to instead of needn't have","t","didn't need to + verb for something done unnecessarily",
 "„Needn't have“ zdôrazní, že sa to urobilo zbytočne: „{right}“.",
 "„Needn't have“ zdůrazní, že se to udělalo zbytečně: „{right}“.",
 "“needn't have” shows it was done for nothing: “{right}”.")
I(t,"not after have","t","should have not / could have not + participle",
 "Zápor patrí k modálnemu slovesu: „{right}“.",
 "Zápor patří k modálnímu slovesu: „{right}“.",
 "The negative goes with the modal: “{right}”.")
I(t,"wrong tense in second clause","w","second clause in present instead of Past Simple",
 "Druhá časť je minulý dej: „{right}“, nie „{wrong}“.",
 "Druhá část je minulý děj: „{right}“, ne „{wrong}“.",
 "The second part is a past action: “{right}”, not “{wrong}”.")
I(t,"preposition after ask","w","ask to/at + person",
 "Po „ask“ nasleduje osoba priamo, bez predložky: „{right}“.",
 "Po „ask“ následuje osoba přímo, bez předložky: „{right}“.",
 "“ask” takes the person directly, no preposition: “{right}”.")
I(t,"missing possessive with body part","w","body part without his/her/their",
 "Pri častiach tela patrí v angličtine privlastňovacie zámeno: „{right}“.",
 "U částí těla patří v angličtině přivlastňovací zájmeno: „{right}“.",
 "Body parts take a possessive in English: “{right}”.")

# ---------------- 58 Inversion basic ----------------
t = 58
I(t,"missing inversion","w","negative adverbial first, then normal subject-verb order",
 "Po zápornom výraze na začiatku vety treba inverziu: „{right}“, nie „{wrong}“.",
 "Po záporném výrazu na začátku věty je potřeba inverze: „{right}“, ne „{wrong}“.",
 "After a negative opening word, invert: “{right}”, not “{wrong}”.")
I(t,"avoids inversion","t","ordinary word order with never/rarely inside the sentence",
 "Precvičuje sa inverzia: „{right}“.",
 "Procvičuje se inverze: „{right}“.",
 "Practise inversion here: “{right}”.")
I(t,"double negation","w","not added after the negative adverbial",
 "Úvodný výraz už je zápor, „not“ sem nepatrí: „{right}“.",
 "Úvodní výraz už je zápor, „not“ sem nepatří: „{right}“.",
 "The opening word is already negative; drop “not”: “{right}”.")
I(t,"Past Simple instead of participle","w","had + subject + Past Simple form (had we saw)",
 "Po „had“ patrí past participle: „{right}“, nie „{wrong}“.",
 "Po „had“ následuje past participle: „{right}“, ne „{wrong}“.",
 "After “had” use the past participle: “{right}”, not “{wrong}”.")
I(t,"Past Simple inversion","t","did-inversion instead of had-inversion for experience up to a past point",
 "Pri skúsenosti do určitého bodu je prirodzenejší Past Perfect: „{right}“.",
 "U zkušenosti do určitého bodu je přirozenější Past Perfect: „{right}“.",
 "For experience up to a past point, Past Perfect is more natural: “{right}”.")
I(t,"past form after did","w","did + subject + Past Simple form (did we saw)",
 "Po „did“ patrí základný tvar slovesa: „{right}“.",
 "Po „did“ následuje základní tvar slovesa: „{right}“.",
 "After “did” use the base form: “{right}”.")
I(t,"missing do-support","w","full verb inverted in a simple tense (Rarely saw we)",
 "Pri Present/Past Simple treba v inverzii „do/does/did“: „{right}“.",
 "U Present/Past Simple je v inverzi potřeba „do/does/did“: „{right}“.",
 "In Present/Past Simple, inversion needs “do/does/did”: “{right}”.")
I(t,"subject before auxiliary","w","subject placed before the auxiliary after the adverbial (Not only he did)",
 "Pomocné sloveso ide pred podmet: „{right}“, nie „{wrong}“.",
 "Pomocné sloveso jde před podmět: „{right}“, ne „{wrong}“.",
 "The auxiliary goes before the subject: “{right}”, not “{wrong}”.")
I(t,"wrong tense of auxiliary","w","have/has instead of had (or vice versa) in the inversion",
 "Čas pomocného slovesa nesedí: „{right}“, nie „{wrong}“.",
 "Čas pomocného slovesa nesedí: „{right}“, ne „{wrong}“.",
 "The auxiliary is in the wrong tense: “{right}”, not “{wrong}”.")
I(t,"auxiliary agreement","w","auxiliary does not agree with the subject (Never has they)",
 "Pomocné sloveso sa riadi podmetom: „{right}“, nie „{wrong}“.",
 "Pomocné sloveso se řídí podmětem: „{right}“, ne „{wrong}“.",
 "The auxiliary must agree with the subject: “{right}”, not “{wrong}”.")
I(t,"inversion in both clauses","w","second clause after but/when also inverted",
 "Inverzia je len v prvej časti; ďalej je bežný slovosled.",
 "Inverze je jen v první části; dál je běžný slovosled.",
 "Only the first part is inverted; the rest keeps normal order.")
I(t,"inversion in the wrong clause","w","inversion right after 'only when/after' instead of in the main clause",
 "Inverzia patrí do hlavnej vety, nie za „only when“: „{right}“.",
 "Inverze patří do hlavní věty, ne za „only when“: „{right}“.",
 "The inversion goes in the main clause, not after “only when”: “{right}”.")
I(t,"Hardly … than","w","than after hardly/scarcely instead of when",
 "Po „Hardly/Scarcely“ patrí „when“, nie „than“.",
 "Po „Hardly/Scarcely“ patří „when“, ne „than“.",
 "“Hardly/Scarcely” is followed by “when”, not “than”.")
I(t,"No sooner … when","w","when after no sooner instead of than",
 "Po „No sooner“ patrí „than“, nie „when“.",
 "Po „No sooner“ patří „than“, ne „when“.",
 "“No sooner” is followed by “than”, not “when”.")
I(t,"Past Perfect after than/when","w","second clause after than/when also in Past Perfect",
 "Druhá časť po „than/when“ je v Past Simple: „{right}“.",
 "Druhá část po „than/when“ je v Past Simple: „{right}“.",
 "The part after “than/when” is in Past Simple: “{right}”.")
I(t,"inversion after positive adverb","w","inversion after a non-negative adverb (Often had we seen)",
 "Inverzia patrí len po zápornom alebo obmedzujúcom výraze (never, rarely…).",
 "Inverze patří jen po záporném nebo omezujícím výrazu (never, rarely…).",
 "Invert only after a negative or limiting word (never, rarely…).")
I(t,"full verb before subject","w","main verb (not auxiliary) moved before the subject in a perfect tense",
 "Pred podmet ide pomocné sloveso, nie plnovýznamové: „{right}“.",
 "Před podmět jde pomocné sloveso, ne plnovýznamové: „{right}“.",
 "Only the auxiliary goes before the subject: “{right}”.")
I(t,"so instead of such a","w","so + adjective + noun (so quiet group)",
 "Pred podstatným menom patrí „such a“ alebo „a … so“: „{right}“.",
 "Před podstatným jménem patří „such a“ nebo „a … so“: „{right}“.",
 "Before a noun use “such a” or “a … so”: “{right}”.")
I(t,"such without a","w","such + adjective + singular noun without a",
 "Pri jednotnom čísle patrí „such a“: „{right}“.",
 "U jednotného čísla patří „such a“: „{right}“.",
 "A singular noun takes “such a”: “{right}”.")

# ---------------- 59 Causative HAVE/GET ----------------
t = 59
I(t,"no causative","w","subject does the action itself (She dyed her boots) instead of have/get + object + participle",
 "„{wrong}“ znamená, že to podmet robí sám. Treba Causative: „{right}“.",
 "„{wrong}“ znamená, že to podmět dělá sám. Je potřeba Causative: „{right}“.",
 "“{wrong}” means the subject did it. Use the Causative: “{right}”.")
I(t,"Passive instead of causative","t","object + was/were + participle (Her boots were dyed)",
 "Precvičuje sa Causative: „{right}“.",
 "Procvičuje se Causative: „{right}“.",
 "Practise the Causative here: “{right}”.")
I(t,"base form instead of participle","w","have/get + object + base form",
 "V Causative patrí za predmet past participle: „{right}“.",
 "V Causative následuje po předmětu past participle: „{right}“.",
 "In the Causative the object is followed by a past participle: “{right}”.")
I(t,"Past Simple instead of participle","w","have/get + object + Past Simple form (got it took)",
 "Za predmet patrí past participle, nie Past Simple: „{right}“.",
 "Po předmětu patří past participle, ne Past Simple: „{right}“.",
 "After the object use the past participle, not Past Simple: “{right}”.")
I(t,"regularised participle","w","irregular verb with a regular -ed participle",
 "Nepravidelné sloveso: past participle je „{right}“, nie „{wrong}“.",
 "Nepravidelné sloveso: past participle je „{right}“, ne „{wrong}“.",
 "Irregular verb: the past participle is “{right}”, not “{wrong}”.")
I(t,"word order in causative","w","have/get + participle + object (got checked her slides)",
 "Poradie je „have/get + vec + past participle“: „{right}“.",
 "Pořadí je „have/get + věc + past participle“: „{right}“.",
 "The order is “have/get + thing + past participle”: “{right}”.")
I(t,"Past Perfect instead of causative","w","had + participle + object (had dyed her boots)",
 "Toto je Past Perfect. Causative má poradie „had + vec + past participle“: „{right}“.",
 "Toto je Past Perfect. Causative má pořadí „had + věc + past participle“: „{right}“.",
 "That is Past Perfect. The Causative order is “had + thing + participle”: “{right}”.")
I(t,"to before participle","w","have + object + to + verb (had the kitchen to film)",
 "V Causative nie je „to“: „{right}“.",
 "V Causative není „to“: „{right}“.",
 "The Causative has no “to”: “{right}”.")
I(t,"have someone to do","w","have + person + to + verb",
 "Po „have + osoba“ je sloveso bez „to“: „{right}“.",
 "Po „have + osoba“ je sloveso bez „to“: „{right}“.",
 "After “have + person” use the verb without “to”: “{right}”.")
I(t,"get someone do","w","get + person + base form without to",
 "Po „get + osoba“ patrí „to“ + sloveso: „{right}“.",
 "Po „get + osoba“ následuje „to“ + sloveso: „{right}“.",
 "After “get + person” use “to” + verb: “{right}”.")
I(t,"calque with give","w","gave + object + to + verb for 'dať urobiť'",
 "„Dať urobiť“ nie je „give“; použi Causative: „{right}“.",
 "„Dát udělat“ není „give“; použij Causative: „{right}“.",
 "Do not use “give” here; use the Causative: “{right}”.")
I(t,"calque with let","w","let + object + verb for 'nechať si urobiť'",
 "„Let“ znamená „dovoliť“; „nechať si urobiť“ je Causative: „{right}“.",
 "„Let“ znamená „dovolit“; „nechat si udělat“ je Causative: „{right}“.",
 "“let” means “allow”; for a service use the Causative: “{right}”.")
I(t,"make instead of have","w","made + object + participle",
 "„Make“ znamená prinútiť; službu vyjadrí „have/get“: „{right}“.",
 "„Make“ znamená přinutit; službu vyjádří „have/get“: „{right}“.",
 "“make” means force; a service is “have/get”: “{right}”.")
I(t,"reflexive calque","w","extra reflexive pronoun (had herself her hair cut) from 'dala si'",
 "Zvratné „si“ sa neprekladá: „{right}“.",
 "Zvratné „si“ se nepřekládá: „{right}“.",
 "The reflexive is not translated: “{right}”.")
I(t,"wrong tense of have/get","w","has/gets for a past event (last summer, the night before)",
 "Dej bol v minulosti: „{right}“, nie „{wrong}“.",
 "Děj byl v minulosti: „{right}“, ne „{wrong}“.",
 "The event was in the past: “{right}”, not “{wrong}”.")
I(t,"Present Perfect with past time","w","has had + object + participle with a finished past time",
 "S minulým časovým údajom patrí Past Simple: „{right}“.",
 "S minulým časovým údajem patří Past Simple: „{right}“.",
 "A finished past time takes Past Simple: “{right}”.")
I(t,"wrong preposition for agent","w","from/of instead of by before the person who does it",
 "Kto činnosť robí, uvádza „by“: „{right}“, nie „{wrong}“.",
 "Kdo činnost dělá, uvádí „by“: „{right}“, ne „{wrong}“.",
 "The person who does it is introduced by “by”: “{right}”, not “{wrong}”.")
I(t,"wrong preposition with colour","w","preposition added before the colour (dyed on purple)",
 "Pri farbe sa predložka nepíše: „{right}“.",
 "U barvy se předložka nepíše: „{right}“.",
 "No preposition before the colour: “{right}”.")
I(t,"missing possessive","w","her/his/their dropped before the object or agent",
 "Chýba privlastňovacie zámeno: „{right}“.",
 "Chybí přivlastňovací zájmeno: „{right}“.",
 "The possessive is missing: “{right}”.")
I(t,"until instead of while","w","until instead of while for 'kým' (= during)",
 "„Kým“ tu znamená „počas“, teda „while“; „until“ je „až dovtedy, kým“.",
 "„Zatímco“ je „while“; „until“ znamená „až do doby, než“.",
 "Here it means “during”, so “while”; “until” means “up to the time”.")

# ---------------- 60 Wish clauses ----------------
t = 60
I(t,"present after wish","w","wish + Present Simple (is/are/have) about the present",
 "Po „wish“ o prítomnosti patrí past form: „{right}“, nie „{wrong}“.",
 "Po „wish“ o přítomnosti patří past form: „{right}“, ne „{wrong}“.",
 "“wish” about the present takes a past form: “{right}”, not “{wrong}”.")
I(t,"can instead of could","w","wish + can",
 "Po „wish“ patrí „could“, nie „can“: „{right}“.",
 "Po „wish“ patří „could“, ne „can“: „{right}“.",
 "After “wish” use “could”, not “can”: “{right}”.")
I(t,"will instead of would","w","wish + will",
 "Po „wish“ nepatrí „will“; zmenu vyjadrí „would“: „{right}“.",
 "Po „wish“ nepatří „will“; změnu vyjádří „would“: „{right}“.",
 "No “will” after “wish”; a wanted change takes “would”: “{right}”.")
I(t,"was instead of were","t","wish + I/he/she/it was",
 "V hovorovej reči sa „was“ používa, no po „wish“ je štandardné „were“.",
 "V hovorové řeči se „was“ používá, ale po „wish“ je standardní „were“.",
 "“was” is common in speech, but “were” is standard after “wish”.")
I(t,"would with a state","t","wish + would be for a state",
 "„Wish + would“ je pre zmenu správania. Pri stave je prirodzenejšie „{right}“.",
 "„Wish + would“ je pro změnu chování. U stavu je přirozenější „{right}“.",
 "“wish + would” is for changing behaviour. For a state use “{right}”.")
I(t,"would about own ability","w","I wish I would … about one's own ability/action",
 "Pri vlastnej schopnosti patrí „I wish I could“, nie „I would“.",
 "U vlastní schopnosti patří „I wish I could“, ne „I would“.",
 "For your own ability use “I wish I could”, not “I would”.")
I(t,"Past Perfect changes time","w","wish + had + participle about the present",
 "„Had + past participle“ je želanie o minulosti; ide o prítomnosť: „{right}“.",
 "„Had + past participle“ je přání o minulosti; jde o přítomnost: „{right}“.",
 "“had + past participle” is about the past; this is the present: “{right}”.")
I(t,"Past Simple for past regret","w","wish + Past Simple about a past event",
 "Ľútosť nad minulosťou vyjadrí Past Perfect: „{right}“, nie „{wrong}“.",
 "Lítost nad minulostí vyjádří Past Perfect: „{right}“, ne „{wrong}“.",
 "Regret about the past takes Past Perfect: “{right}”, not “{wrong}”.")
I(t,"would have for past regret","w","wish + would have + participle",
 "Po „wish“ o minulosti patrí Past Perfect: „{right}“, nie „would have“.",
 "Po „wish“ o minulosti patří Past Perfect: „{right}“, ne „would have“.",
 "“wish” about the past takes Past Perfect: “{right}”, not “would have”.")
I(t,"to after could","w","wish + could to + verb",
 "Po „could“ nasleduje sloveso bez „to“: „{right}“.",
 "Po „could“ následuje sloveso bez „to“: „{right}“.",
 "After “could” use the verb without “to”: “{right}”.")
I(t,"negation copied from Slovak","w","not added because the native sentence has 'škoda, že ne…'",
 "Po „wish“ sa zápor obracia: „škoda, že neviem“ = „{right}“.",
 "Po „wish“ se zápor obrací: „škoda, že neumím“ = „{right}“.",
 "With “wish” the negative flips: “{right}”, without “not”.")
I(t,"hope instead of wish","w","hope + past form for an unreal wish",
 "„Hope“ je nádej na reálne; neskutočné želanie je „wish“: „{right}“.",
 "„Hope“ je naděje na reálné; neskutečné přání je „wish“: „{right}“.",
 "“hope” is for real chances; an unreal wish is “wish”: “{right}”.")
I(t,"wish + person + to","w","wish + person/thing + to + verb (I wish my cat to be)",
 "„Wish + niekto + to“ je formálne „chcieť“; tu patrí „{right}“.",
 "„Wish + někdo + to“ je formální „chtít“; tady patří „{right}“.",
 "“wish + someone + to” is a formal “want”; use “{right}”.")
I(t,"missing -s on wishes","w","he/she/it + wish",
 "Pri „he/she/it“ patrí v Present Simple „wishes“.",
 "U „he/she/it“ patří v Present Simple „wishes“.",
 "With “he/she/it” Present Simple needs “wishes”.")
I(t,"calque would wish","t","would wish that … from 'by si prial/a'",
 "„Would wish“ znie neprirodzene; stačí „wish/wishes“.",
 "„Would wish“ zní nepřirozeně; stačí „wish/wishes“.",
 "“would wish” sounds unnatural; just “wish/wishes”.")
I(t,"avoids wish clause","t","It's a pity / would like / too bad instead of wish",
 "Precvičuje sa „wish“: „{right}“.",
 "Procvičuje se „wish“: „{right}“.",
 "Practise “wish” here: “{right}”.")
I(t,"so instead of as","w","so … as in a positive comparison",
 "„Taký … ako“ je v kladnej vete „as … as“: „{right}“.",
 "„Tak … jako“ je v kladné větě „as … as“: „{right}“.",
 "A positive comparison uses “as … as”: “{right}”.")
I(t,"like instead of as","w","as + adjective + like",
 "Porovnanie „as … as“ sa uzatvára „as“, nie „like“: „{right}“.",
 "Srovnání „as … as“ se uzavírá „as“, ne „like“: „{right}“.",
 "“as … as” ends with “as”, not “like”: “{right}”.")
I(t,"more with short adjective","w","more + short adjective (more thick)",
 "Krátke prídavné meno stupňujeme príponou: „{right}“, nie „{wrong}“.",
 "Krátké přídavné jméno stupňujeme příponou: „{right}“, ne „{wrong}“.",
 "A short adjective takes -er: “{right}”, not “{wrong}”.")
I(t,"present for a past time","w","present tense in a clause about a past time (last spring)",
 "Časový údaj je minulý, preto Past Simple: „{right}“, nie „{wrong}“.",
 "Časový údaj je minulý, proto Past Simple: „{right}“, ne „{wrong}“.",
 "The time is past, so Past Simple: “{right}”, not “{wrong}”.")

# ---------------- 61 Relative clauses ----------------
t = 61
I(t,"which instead of whose","w","which + noun for possession",
 "Vlastníctvo vyjadruje „whose“: „{right}“, nie „{wrong}“.",
 "Vlastnictví vyjadřuje „whose“: „{right}“, ne „{wrong}“.",
 "Possession takes “whose”: “{right}”, not “{wrong}”.")
I(t,"who instead of whose","w","who + noun for possession",
 "„Who“ nevyjadruje vlastníctvo; treba „whose“: „{right}“.",
 "„Who“ nevyjadřuje vlastnictví; je potřeba „whose“: „{right}“.",
 "“who” does not show possession; use “whose”: “{right}”.")
I(t,"double possessive","w","whose + his/her/its + noun",
 "„Whose“ už znamená „jeho/jej“; ďalšie zámeno je navyše: „{right}“.",
 "„Whose“ už znamená „jeho/její“; další zájmeno je navíc: „{right}“.",
 "“whose” already means “his/her”; drop the extra word: “{right}”.")
I(t,"article after whose","w","whose + the + noun",
 "Po „whose“ nepatrí člen: „{right}“.",
 "Po „whose“ nepatří člen: „{right}“.",
 "No article after “whose”: “{right}”.")
I(t,"pronoun instead of relative","w","comma + its/his/her + noun instead of whose (run-on)",
 "Cez „its/his/her“ sa vety takto spojiť nedajú; treba „whose“: „{right}“.",
 "Přes „its/his/her“ se věty takto spojit nedají; je potřeba „whose“: „{right}“.",
 "“its/his/her” cannot join the clauses; use “whose”: “{right}”.")
I(t,"resumptive pronoun","w","extra him/her/it/there inside the relative clause",
 "Vzťažné zámeno už nahrádza predmet; ďalšie „him/her/it“ je navyše.",
 "Vztažné zájmeno už nahrazuje předmět; další „him/her/it“ je navíc.",
 "The relative word already stands for it; drop the extra “him/her/it”.")
I(t,"which for people","w","which referring to a person",
 "Pri ľuďoch patrí „who“ alebo „that“, nie „which“: „{right}“.",
 "U lidí patří „who“ nebo „that“, ne „which“: „{right}“.",
 "For people use “who” or “that”, not “which”: “{right}”.")
I(t,"who for things","w","who referring to a thing",
 "Pri veciach patrí „which“ alebo „that“, nie „who“: „{right}“.",
 "U věcí patří „which“ nebo „that“, ne „who“: „{right}“.",
 "For things use “which” or “that”, not “who”: “{right}”.")
I(t,"what as relative pronoun","w","what instead of which/that after a noun",
 "„What“ nie je vzťažné zámeno za podstatným menom: „{right}“.",
 "„What“ není vztažné zájmeno za podstatným jménem: „{right}“.",
 "“what” cannot follow a noun as a relative word: “{right}”.")
I(t,"what for whole clause","w",", what … referring to the whole previous clause",
 "Na celú predchádzajúcu vetu odkazuje „which“, nie „what“.",
 "Na celou předchozí větu odkazuje „which“, ne „what“.",
 "To refer to the whole previous clause use “which”, not “what”.")
I(t,"that in non-defining clause","w","that after a comma (non-defining clause)",
 "Vedľajšia veta medzi čiarkami nezačína „that“: „{right}“.",
 "Vedlejší věta mezi čárkami nezačíná „that“: „{right}“.",
 "A clause between commas cannot start with “that”: “{right}”.")
I(t,"which without preposition for place","w","which alone for a place where 'where/on which' is needed",
 "Miesto vyjadrí „where“ alebo predložka + „which“: „{right}“.",
 "Místo vyjádří „where“ nebo předložka + „which“: „{right}“.",
 "A place needs “where” or a preposition + “which”: “{right}”.")
I(t,"where for non-place","w","where for a thing that is not a place",
 "„Where“ je len pre miesto; tu patrí „which“ alebo „that“: „{right}“.",
 "„Where“ je jen pro místo; tady patří „which“ nebo „that“: „{right}“.",
 "“where” is only for places; use “which” or “that”: “{right}”.")
I(t,"where with extra preposition","w","where + … + on/in at the end",
 "„Where“ už obsahuje predložku; tá na konci je navyše.",
 "„Where“ už obsahuje předložku; ta na konci je navíc.",
 "“where” already includes the preposition; drop the one at the end.")
I(t,"double preposition","w","preposition both before which and at the end",
 "Predložka je dvakrát; nechaj ju pred „which“ alebo na konci.",
 "Předložka je dvakrát; nech ji před „which“ nebo na konci.",
 "The preposition appears twice; keep it before “which” or at the end.")
I(t,"agreement in relative clause","w","verb in the relative clause does not agree with its subject",
 "Sloveso sa riadi podmetom vedľajšej vety: „{right}“, nie „{wrong}“.",
 "Sloveso se řídí podmětem vedlejší věty: „{right}“, ne „{wrong}“.",
 "The verb agrees with its own subject: “{right}”, not “{wrong}”.")
I(t,"adverb between verb and object","w","adverb (now, often) placed between verb and object",
 "Príslovka nepatrí medzi sloveso a predmet: „{right}“.",
 "Příslovce nepatří mezi sloveso a předmět: „{right}“.",
 "The adverb cannot go between the verb and object: “{right}”.")
I(t,"article instead of possessive","w","the instead of her/his with a body part",
 "Pri častiach tela patrí v angličtine privlastňovacie zámeno: „{right}“.",
 "U částí těla patří v angličtině přivlastňovací zájmeno: „{right}“.",
 "Body parts take a possessive in English: “{right}”.")
I(t,"avoids the relative clause","t","with + noun or another phrase instead of the relative clause",
 "Precvičuje sa relative clause: „{right}“.",
 "Procvičuje se relative clause: „{right}“.",
 "Practise the relative clause here: “{right}”.")
I(t,"which had instead of whose","t","which/who had + noun instead of whose + noun",
 "Vlastníctvo tu priamejšie vyjadrí „whose“: „{right}“.",
 "Vlastnictví tu přímočařeji vyjádří „whose“: „{right}“.",
 "“whose” expresses possession more directly: “{right}”.")
I(t,"calqued verb","t","literal calque that is grammatical but unidiomatic (is turned to)",
 "Znie to doslovne; po anglicky sa povie „{right}“.",
 "Zní to doslovně; anglicky se řekne „{right}“.",
 "That sounds word-for-word; in English say “{right}”.")

# ---------------- 62 Articles advanced ----------------
t = 62
I(t,"a before superlative","w","a/an + superlative",
 "Pred superlative patrí „the“, nie „a“: „{right}“.",
 "Před superlative patří „the“, ne „a“: „{right}“.",
 "A superlative takes “the”, not “a”: “{right}”.")
I(t,"missing the before superlative","w","superlative without the",
 "Superlative potrebuje člen „the“: „{right}“.",
 "Superlative potřebuje člen „the“: „{right}“.",
 "A superlative needs “the”: “{right}”.")
I(t,"demonstrative calque","w","that/this for SK/CZ 'ten/tá' where English needs the",
 "„Ten/tá“ tu len zdôrazňuje; v angličtine patrí „the“: „{right}“.",
 "„Ten/ta“ tu jen zdůrazňuje; v angličtině patří „the“: „{right}“.",
 "The native word only points; English needs “the”: “{right}”.")
I(t,"most with short adjective","w","the most + short adjective",
 "Krátke prídavné meno má superlative s -est: „{right}“.",
 "Krátké přídavné jméno má superlative s -est: „{right}“.",
 "A short adjective forms the superlative with -est: “{right}”.")
I(t,"of instead of in with superlative","t","superlative + of + place",
 "Pri superlative s miestom je prirodzenejšie „in“: „{right}“.",
 "U superlative s místem je přirozenější „in“: „{right}“.",
 "With a place after a superlative, “in” is more natural: “{right}”.")
I(t,"missing the before specific noun","w","the dropped before a noun that is specific/known",
 "Chýba člen „the“, ide o konkrétnu vec: „{right}“.",
 "Chybí člen „the“, jde o konkrétní věc: „{right}“.",
 "“the” is missing; it is a specific thing: “{right}”.")
I(t,"missing a before singular countable","w","a/an dropped before a singular countable noun",
 "Pred počítateľným podstatným menom v jednotnom čísle chýba „a/an“: „{right}“.",
 "Před počitatelným podstatným jménem v jednotném čísle chybí „a/an“: „{right}“.",
 "A singular countable noun needs “a/an”: “{right}”.")
I(t,"the instead of a","w","the where a/an classifies or introduces something new",
 "„The“ ukazuje na známu vec; tu patrí „a/an“: „{right}“.",
 "„The“ ukazuje na známou věc; tady patří „a/an“: „{right}“.",
 "“the” points to something known; use “a/an”: “{right}”.")
I(t,"the before abstract noun","w","the before an abstract/uncountable noun in a general sense",
 "Vo všeobecnom význame je podstatné meno bez člena: „{right}“.",
 "Ve všeobecném významu je podstatné jméno bez členu: „{right}“.",
 "In a general sense the noun takes no article: “{right}”.")
I(t,"the before general plural","w","the before a plural noun used in general",
 "O skupine všeobecne: množné číslo bez člena: „{right}“.",
 "O skupině obecně: množné číslo bez členu: „{right}“.",
 "Talking in general, a plural noun takes no article: “{right}”.")
I(t,"a before uncountable","w","a/an before an uncountable noun (a money, an advice)",
 "Nepočítateľné podstatné meno je bez „a/an“: „{right}“.",
 "Nepočitatelné podstatné jméno je bez „a/an“: „{right}“.",
 "An uncountable noun takes no “a/an”: “{right}”.")
I(t,"a vs an","w","a before a vowel sound or an before a consonant sound",
 "„A/an“ sa riadi výslovnosťou: „{right}“, nie „{wrong}“.",
 "„A/an“ se řídí výslovností: „{right}“, ne „{wrong}“.",
 "“a/an” depends on the sound: “{right}”, not “{wrong}”.")
I(t,"article after by with transport","w","by + a/the + means of transport",
 "Pri dopravnom prostriedku sa po „by“ člen nepíše: „{right}“.",
 "U dopravního prostředku se po „by“ člen nepíše: „{right}“.",
 "No article after “by” with transport: “{right}”.")
I(t,"with instead of by for transport","w","with (a/the) + vehicle for SK/CZ instrumental 'autom'",
 "Spôsob dopravy sa neprekladá cez „with“: „{right}“.",
 "Způsob dopravy se nepřekládá pomocí „with“: „{right}“.",
 "Means of transport is not “with”: “{right}”.")
I(t,"in + vehicle without article","w","in car / in bus without an article",
 "„In“ by potrebovalo člen („in a car“); spôsob dopravy je „{right}“.",
 "„In“ by potřebovalo člen („in a car“); způsob dopravy je „{right}“.",
 "“in” would need an article (“in a car”); transport is “{right}”.")
I(t,"in a car instead of by car","t","in a/their car instead of by car",
 "Pri spôsobe dopravy je ustálené „{right}“ bez člena.",
 "U způsobu dopravy je ustálené „{right}“ bez členu.",
 "For means of transport the fixed phrase is “{right}”, no article.")
I(t,"avoids the practised phrase","t","paraphrase avoiding the practised article phrase (drove across)",
 "Precvičuje sa spojenie „{right}“.",
 "Procvičuje se spojení „{right}“.",
 "Practise the phrase “{right}” here.")
I(t,"article with meals or institutions","w","the with meals or institutions in their usual sense (the breakfast, to the school)",
 "Pri jedlách a inštitúciách v bežnom význame sa člen nepíše: „{right}“.",
 "U jídel a institucí v běžném významu se člen nepíše: „{right}“.",
 "Meals and institutions in their usual sense take no article: “{right}”.")
I(t,"the with proper name","w","the before most country, city or lake names",
 "Väčšina názvov krajín, miest a jazier je bez člena: „{right}“.",
 "Většina názvů zemí, měst a jezer je bez členu: „{right}“.",
 "Most names of countries, cities and lakes take no article: “{right}”.")
I(t,"missing the with rivers or unique things","w","river/sea/unique thing (sun, sky) without the",
 "Rieky, moria a jedinečné veci majú „the“: „{right}“.",
 "Řeky, moře a jedinečné věci mají „the“: „{right}“.",
 "Rivers, seas and unique things take “the”: “{right}”.")
I(t,"the most for majority","w","the most + noun meaning 'most people/things'",
 "„Väčšina“ je „most“ bez „the“: „{right}“.",
 "„Většina“ je „most“ bez „the“: „{right}“.",
 "“most” meaning “the majority” takes no “the”: “{right}”.")

# ---------------- 63 Advanced linkers ----------------
t = 63
I(t,"even though instead of even so","w","even though/even if standing alone after a semicolon",
 "„Even though/if“ uvádza vedľajšiu vetu; samostatne patrí „{right}“.",
 "„Even though/if“ uvádí vedlejší větu; samostatně patří „{right}“.",
 "“even though/if” starts a clause; on its own use “{right}”.")
I(t,"although used as adverb","w","although standing alone after a semicolon/full stop",
 "„Although“ nemôže stáť samo; tu patrí „{right}“.",
 "„Although“ nemůže stát samo; tady patří „{right}“.",
 "“although” cannot stand alone; use “{right}”.")
I(t,"although at the end","w","although at the end of a sentence",
 "Na konci vety môže stáť len „though“, nie „although“.",
 "Na konci věty může stát jen „though“, ne „although“.",
 "Only “though” can end a sentence, not “although”.")
I(t,"although + but","w","although … , but … (calque of 'hoci …, ale')",
 "Pri „although“ sa „but“ nepíše; stačí jedno z nich.",
 "U „although“ se „but“ nepíše; stačí jedno z nich.",
 "Do not use “but” with “although”; one is enough.")
I(t,"despite of","w","despite of + noun",
 "„Despite“ je bez „of“; s „of“ je len „in spite of“.",
 "„Despite“ je bez „of“; s „of“ je jen „in spite of“.",
 "“despite” has no “of”; only “in spite of” does.")
I(t,"in spite without of","w","in spite + noun",
 "„In spite“ potrebuje „of“: „in spite of“.",
 "„In spite“ potřebuje „of“: „in spite of“.",
 "“in spite” needs “of”: “in spite of”.")
I(t,"although before noun phrase","w","although/even though + noun phrase without a verb",
 "Po „although“ nasleduje veta so slovesom; pred podstatným menom patrí „{right}“.",
 "Po „although“ následuje věta se slovesem; před podstatným jménem patří „{right}“.",
 "“although” needs a clause with a verb; before a noun use “{right}”.")
I(t,"despite before clause","w","despite/in spite of + full clause with a verb",
 "Po „despite“ nemôže nasledovať veta so slovesom: „{right}“.",
 "Po „despite“ nemůže následovat věta se slovesem: „{right}“.",
 "“despite” cannot be followed by a clause with a verb: “{right}”.")
I(t,"despite used as adverb","w","despite/in spite of standing alone as a sentence linker",
 "„Despite“ potrebuje podstatné meno; samostatne patrí „{right}“.",
 "„Despite“ potřebuje podstatné jméno; samostatně patří „{right}“.",
 "“despite” needs a noun; on its own use “{right}”.")
I(t,"although instead of despite","t","although + clause instead of the practised despite + noun",
 "Precvičuje sa „{right}“ s podstatným menom.",
 "Procvičuje se „{right}“ s podstatným jménem.",
 "Practise “{right}” with a noun here.")
I(t,"however instead of practised linker","t","however instead of even so / nevertheless",
 "„However“ vyjadrí len kontrast; „napriek tomu“ presnejšie vystihuje „{right}“.",
 "„However“ vyjádří jen kontrast; „přesto“ přesněji vystihuje „{right}“.",
 "“however” only shows contrast; “{right}” fits the meaning better.")
I(t,"but instead of practised linker","t","simple but instead of the practised linker",
 "Namiesto „but“ sa tu precvičuje „{right}“.",
 "Místo „but“ se tu procvičuje „{right}“.",
 "Practise “{right}” here instead of “but”.")
I(t,"still instead of practised linker","t","still/yet as the linker instead of the practised one",
 "Precvičuje sa „{right}“.",
 "Procvičuje se „{right}“.",
 "Practise “{right}” here.")
I(t,"even alone","w","even without so for 'aj tak'",
 "Samotné „even“ znamená „dokonca“; „aj tak“ je „{right}“.",
 "Samotné „even“ znamená „dokonce“; „i tak“ je „{right}“.",
 "“even” alone means something else; the linker is “{right}”.")
I(t,"so instead of contrast linker","w","so (result) instead of a contrast linker",
 "„So“ vyjadruje dôsledok, nie kontrast: „{right}“.",
 "„So“ vyjadřuje důsledek, ne kontrast: „{right}“.",
 "“so” shows a result, not contrast: “{right}”.")
I(t,"therefore instead of contrast","w","therefore/thus instead of a contrast linker",
 "„Therefore“ vyjadruje dôsledok, nie kontrast: „{right}“.",
 "„Therefore“ vyjadřuje důsledek, ne kontrast: „{right}“.",
 "“therefore” shows a result, not contrast: “{right}”.")
I(t,"moreover instead of contrast","w","moreover/furthermore instead of a contrast linker",
 "„Moreover“ pridáva informáciu, nevyjadruje kontrast: „{right}“.",
 "„Moreover“ přidává informaci, nevyjadřuje kontrast: „{right}“.",
 "“moreover” adds information; it shows no contrast: “{right}”.")
I(t,"because of instead of despite","w","because of instead of despite",
 "„Because of“ je príčina, nie protiklad: „{right}“.",
 "„Because of“ je příčina, ne protiklad: „{right}“.",
 "“because of” is a cause, not a contrast: “{right}”.")
I(t,"on the contrary misused","w","on the contrary for simple contrast between two facts",
 "„On the contrary“ popiera predošlé tvrdenie; tu patrí „{right}“.",
 "„On the contrary“ popírá předchozí tvrzení; tady patří „{right}“.",
 "“on the contrary” denies what came before; use “{right}”.")
I(t,"otherwise misused","w","otherwise for 'aj tak/napriek tomu'",
 "„Otherwise“ znamená „inak“; tu patrí „{right}“.",
 "„Otherwise“ znamená „jinak“; tady patří „{right}“.",
 "“otherwise” means “or else”; use “{right}”.")
I(t,"passive participle confused","w","active -ing instead of past participle after feel/seem (felt watching)",
 "Tvar s -ing je činný; pocit, že sa to deje podmetu, je „{right}“.",
 "Tvar s -ing je činný; pocit, že se to děje podmětu, je „{right}“.",
 "The -ing form is active; being on the receiving end is “{right}”.")

# ---------------- 64 Future in past ----------------
t = 64
I(t,"will instead of would","w","will after a past reporting/thinking verb",
 "Po minulom slovese sa „will“ mení na „would“: „{right}“.",
 "Po minulém slovese se „will“ mění na „would“: „{right}“.",
 "After a past verb “will” becomes “would”: “{right}”.")
I(t,"tense instead of would","w","Present/Past Simple instead of would + verb for a later action",
 "Dej je neskorší z pohľadu minulosti, preto „{right}“, nie „{wrong}“.",
 "Děj je pozdější z pohledu minulosti, proto „{right}“, ne „{wrong}“.",
 "It is later from a past viewpoint, so “{right}”, not “{wrong}”.")
I(t,"wrong verb form after would","w","would + past form or -ing",
 "Po „would“ patrí základný tvar slovesa: „{right}“.",
 "Po „would“ následuje základní tvar slovesa: „{right}“.",
 "After “would” use the base form: “{right}”.")
I(t,"to after would","w","would to + verb",
 "Po „would“ sa „to“ nepíše: „{right}“.",
 "Po „would“ se „to“ nepíše: „{right}“.",
 "No “to” after “would”: “{right}”.")
I(t,"is going to not shifted","w","is/are going to after a past verb",
 "Po minulom slovese patrí „was/were going to“: „{right}“, nie „{wrong}“.",
 "Po minulém slovese patří „was/were going to“: „{right}“, ne „{wrong}“.",
 "After a past verb use “was/were going to”: “{right}”, not “{wrong}”.")
I(t,"missing to in going to","w","was going + base form",
 "V „was going to“ nesmie chýbať „to“: „{right}“.",
 "Ve „was going to“ nesmí chybět „to“: „{right}“.",
 "“was going to” needs “to”: “{right}”.")
I(t,"would have changes meaning","w","would have + participle for a future-in-past promise/plan",
 "„Would have“ + past participle je neskutočná minulosť; tu patrí „{right}“.",
 "„Would have“ + past participle je neskutečná minulost; tady patří „{right}“.",
 "“would have” + participle is an unreal past; use “{right}”.")
I(t,"Past Perfect instead","w","had + participle for the later action",
 "„Had“ + past participle je skorší dej; neskorší je „{right}“.",
 "„Had“ + past participle je dřívější děj; pozdější je „{right}“.",
 "“had” + participle is an earlier action; the later one is “{right}”.")
I(t,"would in time clause","w","would after when/before/until/as soon as",
 "Po „when/before/until“ patrí Past Simple, nie „would“: „{right}“.",
 "Po „when/before/until“ patří Past Simple, ne „would“: „{right}“.",
 "After “when/before/until” use Past Simple, not “would”: “{right}”.")
I(t,"should instead of would","w","should for future in the past",
 "„Should“ znamená „mal by“; budúcnosť z minulosti je „{right}“.",
 "„Should“ znamená „měl by“; budoucnost z minulosti je „{right}“.",
 "“should” means obligation; future in the past is “{right}”.")
I(t,"would can","w","would can / would must",
 "„Would can“ nejde; použi „could“ alebo „would be able to“.",
 "„Would can“ nejde; použij „could“ nebo „would be able to“.",
 "“would can” is impossible; use “could” or “would be able to”.")
I(t,"would must","w","would must for a later obligation",
 "Namiesto „would must“ patrí „would have to“.",
 "Místo „would must“ patří „would have to“.",
 "Use “would have to”, not “would must”.")
I(t,"Present Continuous not shifted","t","is/are + -ing kept after a past verb for a planned action",
 "Po minulom slovese sa čas zvyčajne posúva: „{right}“.",
 "Po minulém slovese se čas obvykle posouvá: „{right}“.",
 "After a past verb the tense usually moves back: “{right}”.")
I(t,"was about to instead","t","was/were about to + verb (very soon) instead of would",
 "„Was about to“ = chystať sa hneď; precvičuje sa „{right}“.",
 "„Was about to“ = chystat se hned; procvičuje se „{right}“.",
 "“was about to” means very soon; practise “{right}”.")
I(t,"infinitive avoids future in past","t","promised/decided to + verb instead of that … would",
 "Precvičuje sa Future in the Past: „{right}“.",
 "Procvičuje se Future in the Past: „{right}“.",
 "Practise the Future in the Past here: “{right}”.")
I(t,"promise to + person","w","promised to me that … (to before the person)",
 "Po „promise“ nasleduje osoba bez „to“: „promised me“.",
 "Po „promise“ následuje osoba bez „to“: „promised me“.",
 "“promise” takes the person without “to”: “promised me”.")
I(t,"promise + -ing","w","promised + -ing",
 "Po „promise“ patrí „to“ + sloveso alebo „that … would“: „{right}“.",
 "Po „promise“ následuje „to“ + sloveso nebo „that … would“: „{right}“.",
 "“promise” takes “to” + verb or “that … would”: “{right}”.")
I(t,"double negation","w","never/nothing with an extra not (wouldn't never)",
 "V angličtine je len jeden zápor: „{right}“.",
 "V angličtině je jen jeden zápor: „{right}“.",
 "English allows only one negative here: “{right}”.")
I(t,"said + person","w","said me/him that …",
 "Po „say“ nenasleduje osoba priamo: „told me“ alebo „said to me“.",
 "Po „say“ nenásleduje osoba přímo: „told me“ nebo „said to me“.",
 "“say” takes no direct person: “told me” or “said to me”.")

# ---------------- 65 All Present Tenses ----------------
t = 65
I(t,"Present Simple for ongoing action","w","Present Simple for an action happening now",
 "Dej prebieha práve teraz, preto Present Continuous: „{right}“.",
 "Děj probíhá právě teď, proto Present Continuous: „{right}“.",
 "It is happening now, so Present Continuous: “{right}”.")
I(t,"Present Continuous for habit","w","is/are + -ing for a habit or permanent fact",
 "Zvyk alebo stály fakt vyjadrí Present Simple: „{right}“, nie „{wrong}“.",
 "Zvyk nebo stálý fakt vyjádří Present Simple: „{right}“, ne „{wrong}“.",
 "A habit or fact takes Present Simple: “{right}”, not “{wrong}”.")
I(t,"missing be","w","subject + -ing without am/is/are",
 "Present Continuous potrebuje pomocné sloveso: „{right}“.",
 "Present Continuous potřebuje pomocné sloveso: „{right}“.",
 "Present Continuous needs the auxiliary: “{right}”.")
I(t,"missing -ing","w","am/is/are + base form",
 "Present Continuous je „am/is/are“ + -ing: „{right}“.",
 "Present Continuous je „am/is/are“ + -ing: „{right}“.",
 "Present Continuous is “am/is/are” + -ing: “{right}”.")
I(t,"stative verb in continuous","w","state verb (know, like, want, belong) in the -ing form",
 "Stavové sloveso nemá tvar s -ing: „{right}“, nie „{wrong}“.",
 "Stavové sloveso nemá tvar s -ing: „{right}“, ne „{wrong}“.",
 "A state verb has no -ing form here: “{right}”, not “{wrong}”.")
I(t,"missing third person -s","w","he/she/it (or a singular noun) + verb without -s",
 "Pri „he/she/it“ má Present Simple koncovku -s: „{right}“.",
 "U „he/she/it“ má Present Simple koncovku -s: „{right}“.",
 "With “he/she/it” Present Simple takes -s: “{right}”.")
I(t,"extra -s","w","-s on the verb with I/you/we/they or a plural noun",
 "Pri množnom čísle a „I/you/we/they“ je sloveso bez -s: „{right}“.",
 "U množného čísla a „I/you/we/they“ je sloveso bez -s: „{right}“.",
 "With plurals and “I/you/we/they” the verb has no -s: “{right}”.")
I(t,"-s after does","w","does/doesn't + verb with -s",
 "Po „does/doesn't“ patrí základný tvar: „{right}“.",
 "Po „does/doesn't“ následuje základní tvar: „{right}“.",
 "After “does/doesn't” use the base form: “{right}”.")
I(t,"Present Simple for duration up to now","w","Present Simple/Continuous with for/since for duration up to now",
 "Trvanie až doteraz vyjadrí Present Perfect (Continuous): „{right}“.",
 "Trvání až doteď vyjádří Present Perfect (Continuous): „{right}“.",
 "Duration up to now takes Present Perfect (Continuous): “{right}”.")
I(t,"Present Perfect with finished past time","w","has/have + participle with yesterday/ago/last …",
 "S ukončeným minulým časom patrí Past Simple: „{right}“.",
 "S ukončeným minulým časem patří Past Simple: „{right}“.",
 "A finished past time takes Past Simple: “{right}”.")
I(t,"since instead of for","w","since + length of time",
 "Pri dĺžke trvania patrí „for“, nie „since“: „{right}“.",
 "U délky trvání patří „for“, ne „since“: „{right}“.",
 "For a length of time use “for”, not “since”: “{right}”.")
I(t,"continuous with a count","w","has/have been + -ing with a number of finished items",
 "Pri počte hotových vecí patrí Present Perfect Simple: „{right}“.",
 "U počtu hotových věcí patří Present Perfect Simple: „{right}“.",
 "A count of finished things takes Present Perfect Simple: “{right}”.")
I(t,"Present Perfect Simple for duration","t","has/have + participle where the ongoing duration is stressed",
 "Dôraz je na trvaní, lepšie sedí Present Perfect Continuous: „{right}“.",
 "Důraz je na trvání, lépe sedí Present Perfect Continuous: „{right}“.",
 "The duration is stressed, so Present Perfect Continuous fits better: “{right}”.")
I(t,"have been + base","w","has/have been + base form",
 "Po „have/has been“ patrí tvar s -ing: „{right}“.",
 "Po „have/has been“ následuje tvar s -ing: „{right}“.",
 "After “have/has been” use the -ing form: “{right}”.")
I(t,"has/have agreement","w","have with he/she/it or has with I/you/we/they",
 "Pri „he/she/it“ patrí „has“, inak „have“: „{right}“.",
 "U „he/she/it“ patří „has“, jinak „have“: „{right}“.",
 "“he/she/it” takes “has”, the others “have”: “{right}”.")
I(t,"extra possessive in fixed phrase","w","possessive added to a fixed phrase (shaking their hands)",
 "Ustálené spojenie je bez zámena: „{right}“.",
 "Ustálené spojení je bez zájmena: „{right}“.",
 "The fixed phrase has no possessive: “{right}”.")
I(t,"calqued verb in fixed phrase","w","literal verb in a fixed phrase (give hands, make a photo)",
 "Ustálené spojenie má iné sloveso: „{right}“, nie „{wrong}“.",
 "Ustálené spojení má jiné sloveso: „{right}“, ne „{wrong}“.",
 "The fixed phrase uses another verb: “{right}”, not “{wrong}”.")
I(t,"false friend","w","SK/CZ look-alike word with another English meaning (notebook for laptop)",
 "„{wrong}“ znamená po anglicky niečo iné; tu patrí „{right}“.",
 "„{wrong}“ znamená anglicky něco jiného; tady patří „{right}“.",
 "“{wrong}” means something else in English; use “{right}”.")
I(t,"missing article","w","a/an or the dropped before a singular countable noun",
 "Pred počítateľným podstatným menom v jednotnom čísle chýba člen: „{right}“.",
 "Před počitatelným podstatným jménem v jednotném čísle chybí člen: „{right}“.",
 "A singular countable noun needs an article: “{right}”.")
I(t,"missing of in in front of","w","in front + noun without of",
 "Predložka má tri slová: „in front of“.",
 "Předložka má tři slova: „in front of“.",
 "The preposition is three words: “in front of”.")
I(t,"before instead of in front of","t","before for place instead of in front of",
 "„Before“ o mieste znie zastarano; bežne sa hovorí „in front of“.",
 "„Before“ o místě zní zastarale; běžně se říká „in front of“.",
 "“before” for a place sounds old-fashioned; say “in front of”.")

# ---------------- 66 All Past Tenses ----------------
t = 66
I(t,"Past Perfect for later action","w","had + participle for the later of two past actions",
 "Neskorší dej je v Past Simple; Past Perfect patrí k skoršiemu: „{right}“.",
 "Pozdější děj je v Past Simple; Past Perfect patří k dřívějšímu: „{right}“.",
 "The later action is Past Simple; Past Perfect is for the earlier: “{right}”.")
I(t,"Past Simple for earlier action","w","Past Simple (with already) for the earlier action where Past Perfect is needed",
 "Dej sa skončil skôr, preto Past Perfect: „{right}“, nie „{wrong}“.",
 "Děj skončil dříve, proto Past Perfect: „{right}“, ne „{wrong}“.",
 "It finished earlier, so Past Perfect: “{right}”, not “{wrong}”.")
I(t,"Past Simple instead of Past Perfect with until","t","Past Simple for a state up to a later past event",
 "Past Perfect zdôrazní trvanie až po iný minulý dej: „{right}“.",
 "Past Perfect zdůrazní trvání až po jiný minulý děj: „{right}“.",
 "Past Perfect stresses it lasted up to another past event: “{right}”.")
I(t,"Past Continuous for short action","w","was/were + -ing for a short one-off event (notice, arrive)",
 "Krátky jednorazový dej je v Past Simple: „{right}“, nie „{wrong}“.",
 "Krátký jednorázový děj je v Past Simple: „{right}“, ne „{wrong}“.",
 "A short one-off event takes Past Simple: “{right}”, not “{wrong}”.")
I(t,"Past Continuous for completed action","t","was/were + -ing for a completed action that could be seen in progress",
 "Ukončený dej je prirodzenejší v Past Simple: „{right}“.",
 "Ukončený děj je přirozenější v Past Simple: „{right}“.",
 "A completed action is more natural in Past Simple: “{right}”.")
I(t,"Past Continuous with for + duration","w","was/were + -ing + for + time before another past event",
 "Trvanie až po iný minulý dej vyjadrí „{right}“, nie Past Continuous.",
 "Trvání až po jiný minulý děj vyjádří „{right}“, ne Past Continuous.",
 "Duration up to another past event needs “{right}”, not Past Continuous.")
I(t,"Past Continuous instead of Past Perfect","t","was/were + -ing for a state up to a past point, without duration",
 "Dej trvajúci po iný minulý moment sa tu precvičuje s Past Perfect: „{right}“.",
 "Děj trvající po jiný minulý okamžik se tu procvičuje s Past Perfect: „{right}“.",
 "Here the Past Perfect is practised for a state up to a past moment: “{right}”.")
I(t,"Past Simple or Past Perfect instead of PPC","t","Past Simple / had + participle instead of had been + -ing with a duration",
 "Pri trvaní je prirodzenejší Past Perfect Continuous: „{right}“.",
 "U trvání je přirozenější Past Perfect Continuous: „{right}“.",
 "With a duration Past Perfect Continuous is more natural: “{right}”.")
I(t,"Present Perfect in past story","w","has/have + participle or has/have been + -ing in a past story",
 "Príbeh je v minulosti, preto „had“, nie „has/have“: „{right}“.",
 "Příběh je v minulosti, proto „had“, ne „has/have“: „{right}“.",
 "The story is in the past, so “had”, not “has/have”: “{right}”.")
I(t,"present form in past story","w","Present Simple in a past story",
 "Dej sa odohral v minulosti, preto Past Simple: „{right}“.",
 "Děj se odehrál v minulosti, proto Past Simple: „{right}“.",
 "It happened in the past, so Past Simple: “{right}”.")
I(t,"negative after until","w","until + negative verb (calque of 'kým nedorazila')",
 "Po „until“ je sloveso kladné, hoci po slovensky je zápor: „{right}“.",
 "Po „until“ je sloveso kladné, i když česky je zápor: „{right}“.",
 "After “until” the verb is positive: “{right}”.")
I(t,"base form after had","w","had + base form",
 "Past Perfect je „had“ + past participle: „{right}“.",
 "Past Perfect je „had“ + past participle: „{right}“.",
 "Past Perfect is “had” + past participle: “{right}”.")
I(t,"regular form of irregular verb","w","irregular verb with a regular -ed form (throwed)",
 "Nepravidelné sloveso: správny tvar je „{right}“, nie „{wrong}“.",
 "Nepravidelné sloveso: správný tvar je „{right}“, ne „{wrong}“.",
 "Irregular verb: the correct form is “{right}”, not “{wrong}”.")
I(t,"past form after did","w","did/didn't + Past Simple form",
 "Po „did/didn't“ patrí základný tvar: „{right}“.",
 "Po „did/didn't“ následuje základní tvar: „{right}“.",
 "After “did/didn't” use the base form: “{right}”.")
I(t,"was + Past Simple","w","was/were + Past Simple form (was went)",
 "„Was/were“ + Past Simple nejde: „{right}“.",
 "„Was/were“ + Past Simple nejde: „{right}“.",
 "“was/were” + Past Simple is not possible: “{right}”.")
I(t,"used to misformed","w","use to in a positive past habit",
 "V kladnej vete je „used to“: „{right}“.",
 "V kladné větě je „used to“: „{right}“.",
 "In a positive sentence it is “used to”: “{right}”.")
I(t,"Present Perfect with ago","w","has/have + participle with ago",
 "S „ago“ patrí Past Simple: „{right}“.",
 "S „ago“ patří Past Simple: „{right}“.",
 "“ago” takes Past Simple: “{right}”.")
I(t,"since instead of for","w","since + length of time",
 "Pri dĺžke trvania patrí „for“, nie „since“: „{right}“.",
 "U délky trvání patří „for“, ne „since“: „{right}“.",
 "For a length of time use “for”, not “since”: “{right}”.")

# ---------------- 67 All Future Tenses ----------------
t = 67
I(t,"Future Simple after by","w","will + base with a 'by …' deadline",
 "„By …“ znamená hotové do toho času, preto Future Perfect: „{right}“.",
 "„By …“ znamená hotové do té doby, proto Future Perfect: „{right}“.",
 "“By …” means finished by then, so Future Perfect: “{right}”.")
I(t,"Future Continuous instead of Future Perfect","w","will be + -ing for an action finished by a deadline",
 "Future Continuous je dej v priebehu; hotový dej vyjadrí „{right}“.",
 "Future Continuous je děj v průběhu; hotový děj vyjádří „{right}“.",
 "Future Continuous is in progress; a finished action is “{right}”.")
I(t,"base form after will have","w","will have + base form",
 "Future Perfect je „will have“ + past participle: „{right}“.",
 "Future Perfect je „will have“ + past participle: „{right}“.",
 "Future Perfect is “will have” + past participle: “{right}”.")
I(t,"Past Simple after will have","w","will have + Past Simple form (will have took)",
 "Po „will have“ patrí past participle, nie Past Simple: „{right}“.",
 "Po „will have“ následuje past participle, ne Past Simple: „{right}“.",
 "After “will have” use the past participle, not Past Simple: “{right}”.")
I(t,"until instead of by","w","until/till instead of by before a deadline",
 "Termín „do …“ je „by“; „until“ znamená, že dej trvá celý čas.",
 "Termín „do …“ je „by“; „until“ znamená, že děj trvá celou dobu.",
 "A deadline takes “by”; “until” means it lasts the whole time.")
I(t,"will after when","w","will in a time clause after when/as soon as/before/after/if",
 "Po „when/if/as soon as“ o budúcnosti patrí Present Simple: „{right}“.",
 "Po „when/if/as soon as“ o budoucnosti patří Present Simple: „{right}“.",
 "After “when/if/as soon as” use Present Simple for the future: “{right}”.")
I(t,"Present Continuous after when","w","is/are + -ing in a time clause about one future event",
 "Časová veta o jednej budúcej udalosti je v Present Simple: „{right}“.",
 "Časová věta o jedné budoucí události je v Present Simple: „{right}“.",
 "A time clause about one future event takes Present Simple: “{right}”.")
I(t,"missing third person -s","w","he/she/it + verb without -s in the time clause",
 "Pri „he/she/it“ má Present Simple koncovku -s: „{right}“.",
 "U „he/she/it“ má Present Simple koncovku -s: „{right}“.",
 "With “he/she/it” Present Simple takes -s: “{right}”.")
I(t,"Present Simple instead of will","w","Present Simple in the main clause for a single future action",
 "Present Simple tu znie ako zvyk; o jednom budúcom deji treba „{right}“.",
 "Present Simple tu zní jako zvyk; o jednom budoucím ději je potřeba „{right}“.",
 "Present Simple sounds like a habit; one future action needs “{right}”.")
I(t,"Present Simple for offer or decision","w","Present Simple for a spontaneous offer/decision (I help you)",
 "Ponuku alebo rozhodnutie teraz vyjadrí „will“: „{right}“.",
 "Nabídku nebo rozhodnutí teď vyjádří „will“: „{right}“.",
 "An offer or instant decision takes “will”: “{right}”.")
I(t,"will for arranged plan","t","will + base for a fixed arrangement",
 "Pri dohodnutom pláne je prirodzenejší Present Continuous: „{right}“.",
 "U domluveného plánu je přirozenější Present Continuous: „{right}“.",
 "For a fixed arrangement Present Continuous is more natural: “{right}”.")
I(t,"Future Simple for action in progress","w","will + base for an action in progress at a future moment",
 "Dej bude v danom momente prebiehať: Future Continuous „{right}“.",
 "Děj bude v danou chvíli probíhat: Future Continuous „{right}“.",
 "It will be in progress at that moment: Future Continuous “{right}”.")
I(t,"Future Perfect Continuous for a result","t","will have been + -ing for a finished result",
 "Pri hotovom výsledku je vhodnejší Future Perfect Simple: „{right}“.",
 "U hotového výsledku je vhodnější Future Perfect Simple: „{right}“.",
 "For a finished result Future Perfect Simple fits better: “{right}”.")
I(t,"will to","w","will + to + verb",
 "Po „will“ sa „to“ nepíše: „{right}“.",
 "Po „will“ se „to“ nepíše: „{right}“.",
 "No “to” after “will”: “{right}”.")
I(t,"will be + base","w","will be + base form",
 "Po „will be“ patrí tvar s -ing: „{right}“, nie „{wrong}“.",
 "Po „will be“ následuje tvar s -ing: „{right}“, ne „{wrong}“.",
 "After “will be” use the -ing form: “{right}”, not “{wrong}”.")
I(t,"going without to","w","am/is/are going + base form",
 "V „going to“ nesmie chýbať „to“: „{right}“.",
 "Ve „going to“ nesmí chybět „to“: „{right}“.",
 "“going to” needs “to”: “{right}”.")
I(t,"will going to","w","will + going to / will be going to for a plan",
 "„Will“ a „going to“ sa nespájajú: „{right}“.",
 "„Will“ a „going to“ se nespojují: „{right}“.",
 "Do not combine “will” and “going to”: “{right}”.")
I(t,"would instead of will","w","would + base for a real future",
 "„Would“ je podmienka; istá budúcnosť je „{right}“.",
 "„Would“ je podmínka; jistá budoucnost je „{right}“.",
 "“would” is conditional; a real future is “{right}”.")
I(t,"other instead of another","w","other / an other for 'ďalší' with a singular noun",
 "Pre „ďalší“ pri jednej veci patrí „another“ (jedno slovo).",
 "Pro „další“ u jedné věci patří „another“ (jedno slovo).",
 "For “one more” with a singular noun use “another” (one word).")

# ---------------- build ----------------
FILL = 'x' * 26
bad = []
counts = {}
for t, items in sorted(L.items()):
    meta = topics[str(t)]
    out = []
    for n, (kind, v, pattern, sk, cz, en) in enumerate(items, 1):
        slots = []
        for s in re.findall(r'\{(\w+)\}', sk + cz + en):
            if s not in slots: slots.append(s)
        slots.sort(key=lambda s: {'right': 0, 'wrong': 1}.get(s, 2))
        iid = f"{t}.{n:02d}"
        for lang, txt in (('sk', sk), ('cz', cz), ('en', en)):
            filled = re.sub(r'\{\w+\}', FILL, txt)
            if len(filled) > 150: bad.append((iid, lang, len(filled)))
            if re.search(r'\b(použil|použila|napísal|napsal|napsala|urobil|udělal|zabudol|zapomněl)\s*(si|jsi)\b', txt) or 'príčast' in txt or 'příčest' in txt:
                bad.append((iid, lang, 'wording'))
        out.append({"id": iid, "kind": kind, "verdict": v, "pattern": pattern, "slots": slots,
                    "sk": sk, "cz": cz, "en": en})
    counts[t] = len(out)
    with open(f'mistakes/{t}.json', 'w', encoding='utf-8') as f:
        json.dump({"type_id": t, "topic": meta['topic'], "level": meta['level'], "items": out}, f, ensure_ascii=False, indent=1)
print(counts)
print('BAD', bad)
