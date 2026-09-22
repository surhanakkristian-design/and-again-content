"""Build docs/features/reports/TRANSLATION_DATAPASS_REPORT.md from the data-pass files."""
import glob, json, os, sys, collections, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
J = lambda p: json.load(open(os.path.join(ROOT, p)))
LANGS6 = ["de", "ua", "es", "fr", "tr", "hu"]
ex = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}
sets = J("snapshot/sets.json"); E = sets["empty_ids"]; S = {r["exercise_id"] for r in sets["selected"]}
index = {x["slice"]: x for x in J("part3/slices/index.json")}
state = J("part3/state.json")
done = sorted(k for k, v in state.items() if v.get("done"))
V = J("verify_db.json")
ledger = [l.rstrip("\n").split("\t") for l in open(os.path.join(ROOT, "token_ledger.tsv"))][1:]
tok = collections.Counter(); [tok.__setitem__(p, tok[p] + int(t)) for p, _, t in ledger]
MAIN = int(sys.argv[1]) if len(sys.argv) > 1 else 0
PARTIAL = sum(1 for p in glob.glob(os.path.join(ROOT, 'backups/*/write_log.jsonl')) for l in open(p) if (lambda d: not d.get('dry') and d['already'] > 0 and d['written'] > 0)(json.loads(l)))
L = []
w = L.append
def esc(s):
    return (s if s is not None else "∅").replace("|", "\\|").replace("\n", " ")

# ---------------- Part 3 aggregates
p3 = collections.Counter(); p3lvl = collections.Counter(); left = []; corr = 0; cells = 0; ex_by_lang = collections.defaultdict(list)
for sl in done:
    f = J(f"part3/final/{sl}.json")
    cells += len(index[sl]["ids"]) * 6
    corr += len(f["corrections"]) + sum(1 for x in f["left_empty"] if x[2].startswith("reviewer"))
    for c in f["changes"]:
        p3[c["lang"]] += 1; p3lvl[(c["lang"], ex[c["exercise_id"]]["type_level"])] += 1
        ex_by_lang[c["lang"]].append(c)
    left += f["left_empty"]
# the one reviewer line applied by hand (s031, 32647 tr) is in backups/part3/s031_reviewfix_32647.jsonl
ids_done = {i for sl in done for i in index[sl]["ids"]}
rest = [i for i in E if i not in ids_done]
sel_done = len([i for i in ids_done if i in S]); sel_total = len([i for i in E if i in S])
lvl_total = collections.Counter(ex[i]["type_level"] for i in E)
lvl_done = collections.Counter(ex[i]["type_level"] for i in ids_done)
remaining_slices = [k for k in sorted(index) if k not in done]

w("# Translation data pass — SK/CZ grammar fix, six-language translation, explicit subjects, punctuation (22 Sept 2026)")
w("")
w("## FIRST: status")
w("")
if remaining_slices:
    w(f"**STOPPED at the token budget; resumable.** The remaining slices (≈ 6.9M tokens at the measured rate) would have exceeded the 16,000,000-token budget, so no new slice was started after about 13M were committed. Every started slice was finished and written. Parts 1, 2, 4 and 5 are DONE. Part 3 is PARTLY done: "
      f"{len(ids_done):,} of {len(E):,} exercises translated, reviewed and written into all six languages "
      f"(all {sel_done:,} of the {sel_total:,} selected ones first, then {len(ids_done)-sel_done:,} of the 8,268 others). "
      f"{len(rest):,} exercises ({len(remaining_slices)} slices) remain.")
    w("")
    w(f"**Resume:** `~/Projects/and-again-content/translation-offline/datapass/` — `python3 part3/run_slice.py status` lists every slice; "
      f"the next slices are {', '.join(remaining_slices)}. For each: one translator subagent on `part3/BRIEF_translate.md` with "
      f"`part3/slices/<slice>.txt` → `part3/out/<slice>_N.txt`; then `part3/done.sh translate <slice> <tokens>` (machine check + review file); "
      f"one reviewer subagent on `part3/BRIEF_review.md` → `part3/review/<slice>_out.txt`; then `part3/done.sh review <slice> <tokens>` "
      f"(re-check, backup, rollback file, guarded write, verify). Nothing is ever translated twice: a written slice is `done` in `part3/state.json`, "
      f"and every write is guarded on the empty target fields.")
else:
    w("**DONE.** All five parts are complete.")
w("")
# ---------------- Part 1
p1 = J("part1/part1_final.json")
w("## Part 1 — SK and CZ grammar check and fix (4,064 selected exercises)")
w("")
w(f"- The proposer read all 4,064 × sk + cz rows (8 subagents, 508 exercises each) and listed **430** errors. The machine check passed all 430 "
  f"(the gap count is unchanged; full_sentence = intro_text + correct_answer via `derive_full_sentence`).")
w(f"- The independent verifier (2 subagents) **agreed on 426** and disagreed on 4. **426 fixes were written** "
  f"(sk {sum(1 for c in p1['written'] if c['lang']=='sk')}, cz {sum(1 for c in p1['written'] if c['lang']=='cz')}); 4 were not written.")
w("- Of the 426: 289 are a missing final period on full_sentence (sentence-final gap: intro_text keeps ending on `...`, and the mechanical fill adds the period). "
  "The other 137 are agreement, case, clitic order, reflexive, wrong-language words, a stray `?`/`.` in correct_answer, a capital mid-sentence, and `??`.")
w("- chunks and correct_alternative were not touched (sk/cz selected rows have no chunks).")
w("")
w("**Not written (the verifier disagreed):**")
w("")
w("| id | lang | old full_sentence | proposed | verifier |")
w("|---|---|---|---|---|")
for r in p1["rejected"]:
    w(f"| {r['exercise_id']} | {r['lang']} | {esc(r['old'][2])} | {esc(r['new'][2])} | {esc(r['verdict'][1] if len(r['verdict'])>1 else '')} |")
w("")
w("**Every fix written** (old → new; the field shown is full_sentence, and intro_text/correct_answer changed with it where the reason says so):")
w("")
w("| id | lang | old | new | reason |")
w("|---|---|---|---|---|")
props = {(p["exercise_id"], p["lang"]): p for p in J("part1/props_checked.json")["props"]}
for c in p1["written"]:
    p = props[(c["exercise_id"], c["lang"])]
    extra = ""
    if c["old"]["correct_answer"] != c["new"]["correct_answer"] and (c["old"]["correct_answer"] or "") != (c["new"]["correct_answer"] or ""):
        extra = f" [answer {esc(c['old']['correct_answer'])} → {esc(c['new']['correct_answer'])}]"
    w(f"| {c['exercise_id']} | {c['lang']} | {esc(c['old']['full_sentence'])} | {esc(c['new']['full_sentence'])}{extra} | {esc(p['why'])} |")
w("")
# ---------------- Part 2
p2 = J("part2/part2_changes.json")
w("## Part 2 — punctuation fixes")
w("")
w(f"**142 rows written:** ua 139 (138 without a final period + 720), es 2 (720, 10819), de 1 (3046). intro_text and full_sentence are consistent: "
  "full_sentence equals `derive_full_sentence(intro_text, correct_answer)` on every row. Where the intro ends on the gap, it keeps ending on `...` "
  "and only full_sentence gains the period. es 720 and 10819 also lose the leading `¿` of intro_text: the tag carries its own `¿…?`. chunks were not touched (decision 27).")
w("")
w("| id | lang | old full_sentence | new full_sentence | intro_text change | reason |")
w("|---|---|---|---|---|---|")
for c in p2:
    ic = "" if c["old"]["intro_text"] == c["new"]["intro_text"] else f"{esc(c['old']['intro_text'])} → {esc(c['new']['intro_text'])}"
    w(f"| {c['exercise_id']} | {c['lang']} | {esc(c['old']['full_sentence'])} | {esc(c['new']['full_sentence'])} | {ic} | {esc(c['reason'])} |")
w("")
# ---------------- Part 3
w("## Part 3 — translation of the 10,283 exercises into de, ua, es, fr, tr, hu")
w("")
w(f"- **Method:** {len(index)} slices of about 150 exercises, ordered with the 2,015 selected first, grouped by level (A slices read the six "
  "`RULES_<lang>.md` files of the 6.9.2026 pass; B has no rules files) and by media. The rules come from `PROMPT_translations.md` + the "
  "production subagent brief: options in position, natural form, identical options allowed, the empty-cell rule, typography, the loanword lock, "
  "and the slang/idiom exception. Translation is from the en row, with the sk/cz rows and the MEDIA meaning/scene given as a check. "
  "SEL exercises in es/ua/tr/hu carry an explicit subject pronoun (arm B).")
w("- **Fields written:** intro_text (one `...`), correct_answer (`''` when the empty-cell rule leaves it empty, as in sk/cz), distractor_1/2 "
  "(NULL when empty), and full_sentence = `validate_part.derive_full_sentence` (exactly as the importer). chunks and correct_alternative "
  "stay NULL. Where the target language has the word, the article/copula cells are filled even where sk/cz leave them empty "
  "(de/fr/es/hu articles): that is the pass's per-language rule.")
w("- **Machine check per cell** (`lib/check3.py`): non-empty intro; exactly one gap marker; right script (Cyrillic for ua, no Russian-only letters; "
  "no Cyrillic elsewhere); not English (function-word ratio); not identical to en; full_sentence derivable; final punctuation; length ratio 0.45–2.3 "
  "to the English; distractor_2 empty when options = 2. Warnings (diacritics missing in tr/hu, Latin words in ua, SEL pronoun, ratio 0.6–1.9) went to the reviewer.")
w("- **Review:** an independent reviewer subagent read every row of every slice (en + the six), with the machine flags, and corrected or emptied cells. "
  "Its corrections were re-checked by machine before writing.")
w("")
w(f"**Exercises done:** {len(ids_done):,} of {len(E):,} (selected {sel_done:,}/{sel_total:,}). Per level: " +
  ", ".join(f"{k} {lvl_done[k]:,}/{lvl_total[k]:,}" for k in ("A1", "A2", "B1", "B2")) + ".")
w("")
w("**Cells written per language and level** (one cell = one exercise × one language):")
w("")
w("| lang | A1 | A2 | B1 | B2 | total written | left empty |")
w("|---|---:|---:|---:|---:|---:|---:|")
le = collections.Counter(x[1] for x in left)
for Lg in LANGS6:
    w(f"| {Lg} | " + " | ".join(f"{p3lvl[(Lg, k)]:,}" for k in ("A1", "A2", "B1", "B2")) + f" | {p3[Lg]:,} | {le[Lg]} |")
w("")
w(f"**Left empty:** {len(left)} cells in the done slices:")
w("")
for x in left:
    w(f"- {x[0]} {x[1]}: {x[2]}")
w(f"- plus every cell of the {len(rest):,} exercises not yet translated (budget stop).")
w("")
w(f"**Reviewer disagreement rate:** {corr} of {cells:,} cells corrected or emptied by the reviewer = **{100*corr/max(1,cells):.2f} %**. "
  "One malformed reviewer line (s031, 32647 tr, 6 fields) was applied by hand as the reviewer meant it (intro reordered, options empty) "
  "with its own backup and rollback file.")
w("")
w("**Five examples per language** (intro_text | correct_answer | distractor_1 | distractor_2 → full_sentence; en for reference):")
w("")
random.seed(7)
enrows = {json.loads(l)["exercise_id"]: json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl")) if '"language_code": "en"' in l}
for Lg in LANGS6:
    w(f"*{Lg}*")
    w("")
    for c in random.sample(ex_by_lang[Lg], min(5, len(ex_by_lang[Lg]))):
        n = c["new"]; e = enrows[c["exercise_id"]]
        w(f"- {c['exercise_id']} ({ex[c['exercise_id']]['type_level']}{', SEL' if c['exercise_id'] in S else ''}) — en: {e['intro_text']} [{e['correct_answer']}] — "
          f"{Lg}: {n['intro_text']} | {n['correct_answer']} | {n['distractor_1'] or ''} | {n['distractor_2'] or ''} → {n['full_sentence']}")
    w("")
# ---------------- Part 4
p4 = J("part4/part4_final.json")
w("## Part 4 — explicit-subject rewrite of the existing selected rows (es, ua, tr, hu)")
w("")
w("Input: the 2,049 selected exercises that already have text, per language, read fresh after Part 2. Two proposer subagents per language "
  "inserted ONE nominative subject pronoun where the main clause (else a subordinate clause) drops the subject, in intro_text and full_sentence "
  "together, never inside the gap. The machine check is the wave-1 arm-B check: new tokens = old tokens + exactly one allowed pronoun, "
  "punctuation and order unchanged, the same pronoun in intro_text and full_sentence, and full_sentence = intro + answer. One relaxation "
  "was added: a capitalised pronoun at a mid-text sentence start may take the next word's capital. Then an independent verifier per language. "
  "Only changes that both passes agree on were written. chunks untouched.")
w("")
w("| lang | rows | proposed | machine-check fail | of which: gap opens the sentence (answer would need re-casing, left) | verifier NO | **written** |")
w("|---|---:|---:|---:|---:|---:|---:|")
for Lg in ("es", "ua", "tr", "hu"):
    d = p4[Lg]; mf = d["machine_fail"]
    w(f"| {Lg} | 2,049 | {len(d['written'])+len(d['verifier_no'])+len(mf)} | {len(mf)} | {sum(1 for m in mf if 'gap opens' in (m.get('why') or ''))} | {len(d['verifier_no'])} | **{len(d['written'])}** |")
w("")
w("The ua count is low because most Ukrainian rows already have a noun or pronoun subject. 17 unchanged ua rows without a pronoun were sampled, and all had a noun subject.")
w("")
for Lg in ("es", "ua", "tr", "hu"):
    w(f"*{Lg} — 10 examples (old → new full_sentence)*")
    w("")
    for c in random.sample(p4[Lg]["written"], min(10, len(p4[Lg]["written"]))):
        w(f"- {c['exercise_id']}: {c['old']['full_sentence']} → {c['new']['full_sentence']}")
    w("")
    if p4[Lg]["verifier_no"]:
        w(f"Verifier NO ({len(p4[Lg]['verifier_no'])}, not written): " + "; ".join(f"{x['exercise_id']} ({x['verifier']})" for x in p4[Lg]["verifier_no"][:40]))
        w("")
# ---------------- backups
w("## Backups and rollback files")
w("")
w("All under `~/Projects/and-again-content/translation-offline/datapass/`: `backups/<part>/<batch>.jsonl` holds the full rows before the write, "
  "each with a `.sha256` next to it. `rollback/<part>/<batch>_rollback.sql` is NOT run: it restores the backed-up values only where a row "
  "still holds exactly what this pass wrote. `backups/<part>/write_log.jsonl` has one line per write run. The full pre-pass snapshot is "
  "`snapshot/loc_rows.jsonl` (all 9 languages of the 12,332 exercises the pass could touch, SHA256SUMS) and `snapshot/rowhash_before.json`.")
w("")
for part in ("part1", "part2", "part3", "part4"):
    fs = sorted(p for p in glob.glob(os.path.join(ROOT, "backups", part, "*.jsonl")) if not p.endswith("write_log.jsonl"))
    rows = sum(1 for p in fs for l in open(p) if l.strip())
    w(f"- {part}: {len(fs)} backup files, {rows:,} rows; {len(glob.glob(os.path.join(ROOT, 'rollback', part, '*.sql')))} rollback files.")
w("")
# ---------------- DB verification
w("## DB verification")
w("")
w("Every batch was re-selected after its write and compared field by field. Untouched columns (chunks, correct_alternative, non-target fields) "
  "were checked equal to the backup: 0 mismatches in every batch. "
  "Writes: guarded UPDATEs of at most 500 rows (100 from slice s005 on, after API transport errors). Each statement is its own transaction and is idempotent. "
  "A transport error was retried, and a failed run was re-run. Where the batch had in fact committed, the re-run found those rows `already` written "
  f"({PARTIAL} runs) and wrote only the rest. No row was written twice or skipped.")
w("")
w("**Whole table, per language** (row md5 of all 48,572 rows per language, before vs after; changed rows must be rows this pass backed up):")
w("")
w("| lang | rows | rows changed | changed but not written by this pass | rows added/removed |")
w("|---|---:|---:|---:|---:|")
for Lg, d in V["per_lang"].items():
    w(f"| {Lg} | {d['rows']:,} | {d['changed']:,} | {d['n_changed_not_touched']} | {d['added']}/{d['removed']} |")
w("")
w("**Filled text (intro_text or full_sentence) on the 10,283 exercises, before → after:** " +
  ", ".join(f"{Lg} {V['filled_10283'][Lg]['before']:,} → {V['filled_10283'][Lg]['after']:,}" for Lg in ["sk","en","cz"]+LANGS6))
w("")
w("**Filled text, whole table, after (before = after − Part 3 cells written, since Part 3 only fills empty rows):** " +
  ", ".join(f"{Lg} {V['filled_table_now'].get(Lg,0) - p3.get(Lg,0):,} → {V['filled_table_now'].get(Lg,0):,}" for Lg in ["sk","en","cz"]+LANGS6))
w("")
w("**Other tables** (row count + order-independent md5 of all rows):")
w("")
for t, d in V["tables"].items():
    w(f"- {t}: {d['after']['n']:,} rows, {'unchanged' if d['same'] else 'CHANGED'}")
w("")
# ---------------- Part 5
w("## Part 5 — import safeguard")
w("")
w("In `~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts/` (and-again-content commit fd95c82, after f1958c9 had "
  "committed the working-tree scripts as found):")
w("- `validate_part.py`: new `blank_text_gaps()` and `filled_text_counts()`, and a new error **E20**. It fires when any of the nine languages "
  "has a blank row (intro_text and full_sentence both empty, or the row missing) on an exercise where sk or en has text. The §0p scope does "
  "NOT exempt a row (decision 28). It runs in the full phase, not in `--phase en`.")
w("- `import_db.py`: `text_safeguard()` runs **before anything else** in both paths (REST upsert and the one-transaction SQL import). "
  "It prints the per-language filled-text counts and exits with `IMPORT REFUSED` and per-language examples on any gap. "
  "The SQL verification (`tail()`, in every dry-run chunk and in the import transaction) now asserts, per language, that the "
  "rows with text among the imported localizations equal the workbook's count, so a blank or shifted column rolls the transaction back.")
w("- `test_text_safeguard.py`: **14 tests, all pass.** They cover the gap rules (blank, whitespace, missing row, full_sentence-only, "
  "no-stem types, en-only source, scope not exempting), the counts, the import refusal/pass, and the verification SQL for all 9 "
  "languages. Two tests run on the real workbook that caused the gap (`6.9.2026_A_part2.xlsx`, read-only): validate reports E20 for all "
  "six languages (1,723 each), and the import dry run exits `IMPORT REFUSED`.")
w("- Effect: the §0p grammar scope (en/sk/cz only) can no longer be imported; a future part must carry all nine languages.")
w("")
# ---------------- tokens
w("## Claude tokens")
w("")
tot = sum(tok.values())
w(f"Subagent tokens from the Agent results (the same measure as earlier passes): Part 1 {tok['p1']:,}, Part 4 {tok['p4']:,}, Part 3 {tok['p3']:,}. "
  f"Subagents total **{tot:,}**; main session ≈ {MAIN:,}; **total ≈ {tot+MAIN:,} of 16,000,000.** Cumulative tokens were printed after every "
  "slice (about every 150 exercises) in `token_ledger.tsv`. There was no Gemini, no headless session, no deploy, no push, and no schema change.")
w("")
nt = [x for x in ledger if x[0] == "p3" and x[1].startswith("translate")]; nr = [x for x in ledger if x[0] == "p3" and x[1].startswith("review")]
w(f"Per slice: translator ≈ {sum(int(x[2]) for x in nt)//max(1,len(nt)):,} (A slices, which read the rules, ≈ 200k; B ≈ 180k), reviewer ≈ {sum(int(x[2]) for x in nr)//max(1,len(nr)):,}. "
  f"That is about {(sum(int(x[2]) for x in nt)+sum(int(x[2]) for x in nr))//max(1,len(ids_done)):,} tokens per exercise × 6 languages.")
w("")
# ---------------- remaining
w("## What remains")
w("")
if remaining_slices:
    w(f"- **Part 3:** {len(rest):,} exercises (all non-selected B1/B2) in slices {', '.join(remaining_slices)}. "
      f"At the measured rate that is ≈ {len(rest)*((sum(int(x[2]) for x in nt)+sum(int(x[2]) for x in nr))//max(1,len(ids_done))):,} tokens. Resume as in the first section.")
w("- The 4 Part 1 fixes the verifier refused (the `napriek tomu, / přesto,` comma rows) are still open. The proposals put the clitic in the wrong place.")
gapo = {Lg: sum(1 for m in p4[Lg]["machine_fail"] if "gap opens" in (m.get("why") or "")) for Lg in ("es", "ua", "tr", "hu")}
w(f"- Part 4 left alone: {sum(gapo.values())} rows (" + ", ".join(f"{k} {v}" for k, v in gapo.items() if v) + ") where the gap opens a sentence and the pronoun would need correct_answer re-cased; 1 hu row (7816) whose proposal also added a word; and the "
  + str(sum(len(p4[Lg]['verifier_no']) for Lg in p4)) + " verifier-NO rows. Some of the verifier-NO rows (ua 2, tr 3, hu 14) were refused because the ORIGINAL sentence is already ungrammatical; those rows need their own grammar fix, which was outside Part 4's scope.")
w("- Several English source rows look wrong (translators flagged them, e.g. options with a full stop while the gap is mid-sentence, `use to`, `housees`, `thirdty`). They were translated as written: the translator renders the intended form, and the English was not changed. The ids were named in the translators' one-line replies during the run; they are not compiled in a file. Examples: 34800, 36066, 36193, 35899, 38431, 42777, 42115, 44493, 40603, 37910.")
w("- **The `gate` / `bar` / `cool` loanword lock was applied only in its sense.** For a pet safety gate or a kite bar, the translators used the ordinary word, as the lock rule says.")
open(os.path.expanduser("~/Projects/and-again/docs/features/reports/TRANSLATION_DATAPASS_REPORT.md"), "w").write("\n".join(L) + "\n")
print(len(L), "lines")
