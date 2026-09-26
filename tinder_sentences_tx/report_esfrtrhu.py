"""Builds TINDER_TRANSLATIONS_ES_FR_TR_HU_REPORT.md from report_parts.json + tokens.tsv + slice files."""
import json, os, collections, glob
H = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(H, 'report_parts.json')))
L = ['es', 'fr', 'tr', 'hu']; NAME = {'es': 'Spanish', 'fr': 'French', 'tr': 'Turkish', 'hu': 'Hungarian'}
N = 3664
tok = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'tokens.tsv'))]
def cum(l):
    out, c = [], 0
    for p in tok:
        if len(p) == 4 and p[0] == l and p[3].isdigit():
            c += int(p[3]); out.append((p[1], p[2], int(p[3]), c))
    return out
def esc(s): return str(s).replace('|', '\\|')
o = []
o.append('Rows written: ' + ', '.join(f"{l} **{P[l]['rows']}**" for l in L) + f" of {N}. Remaining in English: " +
         ', '.join(f"{l} {len(P[l]['missing'])} ({', '.join(map(str, P[l]['missing']))})" for l in L) + '. Nothing else remains.')
o.append('\n# Tinder translations: es, fr, tr, hu\n')
o.append('Brief of 26 Sept 2026, owner decision 132 (recorded in `translation-offline/upload_skcz/OWNER_DECISIONS_2L.md`, and-again-content commit 6b8afe9). '
         'Same pipeline, rules and verifier as sk/cz/de/ua (`tinder_sentences_tx/`: `RULES_TX.md`, `TASK_TX.md`, `TASK_TXV.md`, `build.py`, `write_tx.sh`), unchanged. '
         'Per language: 12 slices of ~306 media; one Claude Opus translator per slice, `build.py check` (deterministic: empty, TRUE = FALSE, end punctuation, lengths, phrase 1-6 words, untranslated), '
         'an independent Claude Opus verifier over every row that passed the checker, `final` writes only agreed rows (upsert into `public.tinder_sentences`, slice by slice as soon as agreed), '
         'then one retry round (translator + new verifier) over all rejects. Rows without agreement stay English (the app falls back). No Gemini, no app code, no deploy.\n')
o.append('## Rows per language (live in `tinder_sentences`, counted in the database after the last write)\n')
o.append('| language | rows | of 3,664 | round 1 rejected (checker + verifier) | agreed on retry | still English | tokens (translator + verifier) |')
o.append('|---|---|---|---|---|---|---|')
for l in L:
    s = P[l]
    o.append(f"| {l} {NAME[l]} | **{s['rows']}** | {100*s['rows']/N:.2f} % | {s['r1_rows']} | {s['r1_rows']-len(s['missing'])} | {len(s['missing'])} | {s['tx']+s['txv']:,} |")
o.append('\nFor comparison (earlier run): sk 3,662, cz 3,661, de 3,660, ua 3,663.\n')
o.append('## Verifier rejections by reason\n')
o.append('| language | round 1: verifier | round 1: checker | retry round: still rejected |')
o.append('|---|---|---|---|')
for l in L:
    s = P[l]
    f = lambda d: ', '.join(f'{k} {v}' for k, v in d.items()) or 'none'
    o.append(f"| {l} | {f(s['r1'])} | {f(s['hard'])} | {f(s['r2'])} |")
o.append('''
- The checker rejects are almost all phrases of 7-8 words: Spanish and French articles and prepositions push a 5-word English label past the 6-word limit (rows: es 215 of 288, fr 359 of 446 round-1 rejects; the table counts flags, one row can carry two). The retry translators shortened them and nearly all passed. Turkish and Hungarian had no checker rejects at all.
- As in sk/cz/de/ua, `unnatural` (calques, stiff jokes) is the main verifier reason, then meaning drift and grammar.
- The verifiers used `register` correctly on words that are harmless in English but loaded in the target language: es 4174/4178 "la zorra" (vixen = slur for women, now "el zorro"), es 4409 "está ciega" (= wasted), fr 991 "sa poitrine est nue" (reads as bare breasts, now "torse nu"), hu 1920/4101 bare "farka" (sexual double meaning). All were fixed on retry except fr 991, which stays English (the retry still used \"poitrine\" where French says \"torse\").
''')
o.append('## Rows left in English\n')
for l in L:
    for x in P[l]['left2']:
        o.append(f"- {l} {x['id']}: {', '.join(x['r'])}. {x['note'][:260] or 'phrase still longer than 6 words after the retry (checker).'}")
    extra = [i for i in P[l]['missing'] if i not in {x['id'] for x in P[l]['left2']}]
    for i in extra: o.append(f'- {l} {i}: rejected by the checker on retry.')
for l in L:
    for lg in ['sk','cz','de','ua']: pass
o.append('')
for l in L:
    o.append(f'## 10 examples, {NAME[l]} (random sample, seed 131)\n')
    o.append('| id | word | English TRUE / FALSE sentence | translated TRUE / FALSE sentence | translated TRUE / FALSE phrase |')
    o.append('|---|---|---|---|---|')
    for e in P[l]['examples']:
        en, t = e['en'], e['tx']
        o.append(f"| {e['id']} | {esc(e['word'])} | {esc(en['ts'])} / {esc(en['fs'])} | {esc(t['ts'])} / {esc(t['fs'])} | {esc(t['tp'])} / {esc(t['fp'])} |")
    o.append('')
o.append('## Tokens\n')
o.append('Subagent tokens (the final context size of each Claude agent, as the harness reports it; log `tinder_sentences_tx/tokens.tsv`).\n')
o.append('| language | translator | verifier | total | per translator slice | per verifier slice |')
o.append('|---|---|---|---|---|---|')
tot = 0
for l in L:
    s = P[l]; c = cum(l); tot += s['tx'] + s['txv']
    txs = [x[2] for x in c if x[1] == 'tx' and x[0].startswith('t')]; vs = [x[2] for x in c if x[1] == 'txv' and x[0].startswith('t')]
    o.append(f"| {l} | {s['tx']:,} | {s['txv']:,} | **{s['tx']+s['txv']:,}** | {sum(txs)//len(txs):,} | {sum(vs)//len(vs):,} |")
o.append(f'\nTotal for the four languages: **{tot:,}** subagent tokens. A language costs 2.28-2.42M, the same as sk/cz/de/ua (2.25-2.37M). French cost the most because its retry round was the largest (446 rows, split over two translators). The orchestrating session is not included (as in earlier reports). Gemini: 0 calls.\n')
o.append('### Cumulative tokens per slice\n')
for l in L:
    o.append(f'{l}: ' + '; '.join(f"{sl} {st} {t:,} (cum {c:,})" for sl, st, t, c in cum(l)) + '\n')
o.append('''## For the owner

- **Media 5464** ("She is slim." / "He is slim.", phrases "a slim woman in jeans / in shorts") was accepted by all four verifiers as a plain description, so es/fr/tr/hu now carry it. The earlier report already flagged the English row as breaking the looks rule (Czech rejected it). If the English row is rewritten, these four (and sk/de/ua) need a re-translation of that one media.
- **Hungarian phrases of one word.** Hungarian writes compounds as one word ("gitárhúr", "sakktorna"), so 273 Hungarian TRUE/FALSE phrases are a single word (es 2, fr 0, tr 0; sk 8, cz 14, de 9, ua 32). The checker allows 1-6 words, the verifiers accepted them as natural labels (one verifier noted they could be padded with "egy"). No change made; say if the 2-word minimum should be enforced for Hungarian.
- **Word swaps.** Translators replaced the app's word where it did not fit the sense, each with a note in column 6 of `slices/<lang>/tNN_out.tsv` (es 46, fr 43, tr 50, hu 60 notes, not all of them swaps). Examples: tr 900 "ajan" means spy, used "temsilci"; fr 2850 drum kit = "batterie", not "tambour"; es 4086 mosquitoes "pican", not "muerden"; tr 5297 ruins = "harabe", not "yıkım"; hu 1544 "mosnivaló" wrong for washed laundry. These point to `word_localizations` entries worth a review.
- **Gender in Hungarian and Turkish.** Neither language has he/she; FALSE sentences that swap only the pronoun carry the swap with "férfi/nő" (hu) or "adam/kadın" (tr), e.g. 5464 "A nő karcsú." / "A férfi karcsú.".
- tr 3266 stays English: the retry translator had assumed a bicycle without seeing the media, the verifier refused to accept an unverified fact.

## How it ran / how to resume

All four languages are complete, nothing to resume. Files per language in `~/Projects/and-again-content/tinder_sentences_tx/slices/<lang>/` (inputs, outputs, checks, verdicts, final rows, upsert SQL). One deviation from the recipe: the French retry input (446 rows) was split in two translator halves (`r1a`, `r1b`, concatenated to `r1_out.tsv`) to keep each agent within one read/write budget; the verifier ran over the whole retry as usual. A third attempt on the 33 English-only rows would follow the same retry recipe with `r2`.
''')
open(os.path.expanduser('~/Projects/and-again/docs/features/reports/TINDER_TRANSLATIONS_ES_FR_TR_HU_REPORT.md'), 'w').write('\n'.join(o))
print('ok')
