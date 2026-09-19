# Phase 1T / Task B — second-language probe, part 3.1 + preparation of 3.2 (0 model calls, READ-ONLY on the DB)

Write ONLY under ~/Projects/and-again-content/translation-offline/phase1t/taskB/. No Gemini calls. NO database writes of any kind — SELECT only.
Budget: about 14 tool calls.

## Background
The offline translation checker (translate-the-sentence exercise: learner sees a sentence in their NATIVE language, types English) reads SLOVAK morphology everywhere: arm B explicit subject pronouns, the time-frame guard, the person/number guard F4v2, the agent-drop rule AG (nominative agent). The app supports more native languages (sk and cz get native feedback; other natives get English at B1/B2). Nothing was ever tested on another native language. This is a PROBE, not a measurement.

## 3.1 Report what exists
Live DB, read-only, from ~/Projects/and-again:
`~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase db query "<sql>" --linked -o json`
(project ref abyrutykpvmzkfbesire). Start from information_schema: find every table/column that holds exercise sentences and their translations per native language (candidates: exercises, sentence_translations, chunk sentences, translation_* tables; also look in ~/Projects/and-again/supabase/migrations and the app's translate-format code under ~/Projects/and-again for which table the translate format reads and how it chooses the native language).
Report: which native languages have exercise sentences, HOW MANY each (total and per CEFR level if available), and specifically for the translate-the-sentence format.
Then the annotation side: the offline stack needs per-sentence fields `voice_sk`, `agent_nom`, `tense_open`, `perfective_present`, and the `p` and `g` chains (person / gender chains). Find where they live (DB columns? or only in translation-offline/phase1p/data/annotations.json and the like — grep the repo) and state for each field: exists for which languages / Slovak-only / offline-file-only. If a language has no sentences, say so. Do NOT invent sentences.

## 3.2 preparation (Czech) — only if Czech sentences exist
- Pull a sample of up to 120 Czech sentences with their English reference (and the Slovak sibling of the same sentence if one exists — same sentence id), stratified by level if possible; save as taskB/cz_sample.json. No invention: only what the DB holds.
- Locate, in translation-offline/ (phase1i … phase1s), each deterministic guard and HOW its gold validation was run on Slovak: time-frame guard, person/number guard F4v2, the AG nominative-agent reader, passive / reflexive-passive detection. For each: file path, entry function, what inputs it needs (raw sentence? annotation fields? which), and the gold-validation script + gold file format + the agree / conservative / ERROR definitions used.
- List every place in those guards where a SLOVAK-specific word list, suffix table, regex or annotation field is read (file:line, what it is: e.g. SK_PRON, `sa/si` reflexive regex, auxiliary forms som/si/je/sme/ste/sú, budem…, past-tense -l endings, že/keď subordinators). For each say what the Czech equivalent would be (e.g. se/si, jsem/jsi/je/jsme/jste/jsou, budu…, že/když) and whether the guard would silently ABSTAIN, silently MISFIRE, or crash on Czech input.
- Do not run the guards on Czech yet and do not write gold; that is the next step and depends on your findings.

## Output
taskB/INVENTORY_1T.md (≤ 150 lines: the language/count table with the exact SQL used, the annotation-field table, the guard table, the Slovak-specific-spots list) + taskB/cz_sample.json if applicable.
Final message to me: ≤ 15 lines with the headline facts and your tool-call count.
