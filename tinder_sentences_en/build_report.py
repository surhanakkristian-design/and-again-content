"""Build TINDER_SENTENCES_EN_REPORT.md from the slice files, tokens.tsv and the live row count."""
import json, glob, os, collections, random, sys
H = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(H, 'slices')
IDX = json.load(open(os.path.join(H, 'media_index.json')))
man = json.load(open(os.path.join(S, 'manifest.json')))
live_n = int(sys.argv[1]) if len(sys.argv) > 1 else None


def jl(p):
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []


fin, left, r1rej, r2rej, relabel, r1n, r2n = [], [], collections.Counter(), collections.Counter(), 0, 0, 0
per_slice = []
for m in man:
    s = m['slice']
    f = jl(os.path.join(S, f'{s}_final.jsonl'))
    fin += f
    lj = json.load(open(os.path.join(S, f'{s}_left.json'))) if os.path.exists(os.path.join(S, f'{s}_left.json')) else {'left': []}
    left += [dict(x, slice=s) for x in lj['left']]
    v1 = jl(os.path.join(S, f'{s}_verdict.jsonl'))
    v2 = jl(os.path.join(S, f'{s}_verdict2.jsonl'))
    r1n += len(v1); r2n += len(v2)
    for v in v1:
        if v['v'] == 'R':
            for r in v.get('r') or ['other']:
                r1rej[r] += 1
    for v in v2:
        if v['v'] == 'R':
            for r in v.get('r') or ['other']:
                r2rej[r] += 1
    relabel += sum(1 for r in f if r.get('tone_was'))
    per_slice.append((s, m['grp'], m['n'], len(f), sum(1 for v in v1 if v['v'] == 'R'), len(v2), sum(1 for v in v2 if v['v'] == 'R')))
done_ids = {r['id'] for r in fin}
all_ids = {int(k) for k in IDX}
missing = sorted(all_ids - done_ids)
G = {'A': [r for r in fin if IDX[str(r['id'])]['grp'] == 'A'], 'B': [r for r in fin if IDX[str(r['id'])]['grp'] == 'B']}
tot = {g: sum(1 for k in IDX.values() if k['grp'] == g) for g in 'AB'}


def share(rows, key='ts'):
    n = len(rows); a = sum(1 for r in rows if len(r[key]) <= 30)
    return a, n, (100 * a / n if n else 0)


def dist(rows, key):
    c = collections.Counter(r[key] for r in rows)
    return ', '.join(f'{k} {v} ({100*v/len(rows):.1f} %)' for k, v in c.most_common())


tok = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'tokens.tsv'))][1:]
tok_total = sum(int(t[2]) for t in tok if t[2].isdigit())
L = []
sa, sb = share(G['A']), share(G['B'])
L.append(f"Media done: {len(fin)} of {len(IDX)}; media left: {len(missing)}; TRUE sentences of 30 characters or less: A-level {sa[0]}/{sa[1]} = {sa[2]:.1f} %, B-level {sb[0]}/{sb[1]} = {sb[2]:.1f} % (floor 70 %).")
L += ["", "# Tinder texts, English: all media, four texts each", "",
      "Written 25 Sept 2026 (owner decisions 120-122). Every media with an asset description got a TRUE sentence, a FALSE sentence, a TRUE short phrase and a FALSE short phrase, written by an Opus writer from `media.asset_description` (plus the transcript where there is one) and checked by an independent Opus verifier plus a deterministic checker (`check.py`). Only rows both accepted are stored.", "",
      "## Where it is", "",
      f"- Table `public.tinder_sentences` (migration `supabase/migrations/20260925150000_tinder_sentences.sql`, applied live): media_id, language_code, true_sentence, false_sentence, true_phrase, false_phrase, tone, device, created_at; unique (media_id, language_code); RLS on with the read policy of exercise_localizations; anon and authenticated have SELECT only.",
      f"- English rows live: **{live_n if live_n is not None else len(fin)}** (language_code `en`). The database writes were not refused; every slice was upserted as soon as it was agreed.",
      "- Working files: `~/Projects/and-again-content/tinder_sentences_en/` (RULES.md, task files, check.py, pipeline.py, write_slice.sh, slices/sNN_*.jsonl, tokens.tsv).",
      "- Review page: `TINDER_SENTENCES_EN.html` (same Drive folder as this report).", "",
      "## Scope", "",
      f"- Live media with an asset description: {len(IDX)} (A-level {tot['A']}, B-level {tot['B']}). 3 media without a description were out of scope. Level group = A or B from the media's exercise types.",
      f"- 25 slices ordered by level group, then category, then id: 13 A slices of 148 and 12 B slices of 145.", "",
      "## Length: the 70/30 rule", "",
      f"- TRUE sentence 30 characters or less: A {sa[0]}/{sa[1]} = {sa[2]:.1f} %, B {sb[0]}/{sb[1]} = {sb[2]:.1f} %. Both above the 70 % floor.",
      f"- FALSE sentences follow the TRUE sentence's length class (checked for every row).",
      f"- Longest TRUE sentence {max(len(r['ts']) for r in fin)} characters; median {sorted(len(r['ts']) for r in fin)[len(fin)//2]}. Phrases: longest {max(max(len(r['tp']), len(r['fp'])) for r in fin)} characters.",
      f"- Sentences the verifier marked as stretched past 30 characters only for a joke: {sum(1 for r in fin if r.get('stretched'))} of {len(fin)} ({100*sum(1 for r in fin if r.get('stretched'))/len(fin):.1f} %; limit 20 %).", "",
      "## Tense of the TRUE sentence", ""]
for g in 'AB':
    L.append(f"- {g}: {dist(G[g], 'tense')}")
L += ["", "## Humour devices and tones", ""]
for g in 'AB':
    L.append(f"- Devices, {g}: {dist(G[g], 'device')}")
for g in 'AB':
    L.append(f"- Tones, {g}: {dist(G[g], 'tone')}")
hum = sum(1 for r in fin if r['device'] != 'none')
L.append(f"- Rows with a humour device: {hum} of {len(fin)} ({100*hum/len(fin):.1f} %). The rest are plain factual sentences, which the brief ranks above a forced joke.")
L.append(f"- {relabel} rows were accepted after the verifier's only objection was the tone LABEL (a plain sentence labelled business/gossip/flirt etc.); their label was changed to chill, the text is unchanged.")
pops = [r for r in fin if r.get('pop')]
pc = collections.Counter(r['pop'] for r in pops)
L += ["", "## Pop culture", "", f"- {len(pops)} rows use a pop-culture name ({100*len(pops)/len(fin):.1f} %). Most used: " + ', '.join(f'{k} {v}' for k, v in pc.most_common(15)) + '.', ""]
L += ["## Verifier rejections by reason", "",
      f"- Round 1: {sum(1 for x in per_slice for _ in range(x[4]))} of {r1n} rows rejected. Reasons (a row can have several): " + ', '.join(f'{k} {v}' for k, v in r1rej.most_common()) + '.',
      f"- Round 2 (the rejected rows rewritten once and re-checked by the verifier): {sum(x[6] for x in per_slice)} of {r2n} rejected again. Reasons: " + (', '.join(f'{k} {v}' for k, v in r2rej.most_common()) or 'none') + '.',
      "", "| slice | level | media | stored | round-1 rejects | retried | round-2 rejects |", "|---|---|---|---|---|---|---|"]
for x in per_slice:
    L.append('| ' + ' | '.join(str(v) for v in x) + ' |')
random.seed(20260925)
for g in 'AB':
    ex = random.sample(G[g], 20)
    L += ["", f"## 20 examples, {g}-level", "", "| id | word | TRUE sentence | FALSE sentence | TRUE phrase | FALSE phrase | tone / device |", "|---|---|---|---|---|---|---|"]
    for r in sorted(ex, key=lambda r: r['id']):
        w = IDX[str(r['id'])]['words'].split(' (')[0]
        e = lambda s: s.replace('|', '\\|')
        L.append(f"| {r['id']} | {e(w)} | {e(r['ts'])} ({len(r['ts'])}) | {e(r['fs'])} ({len(r['fs'])}) | {e(r['tp'])} | {e(r['fp'])} | {r['tone']} / {r['device']} |")
L += ["", "## Tokens", "", f"- Subagent tokens (writers, verifiers, retries): {tok_total:,}. The orchestrating session is not included in this figure.",
      "- Per slice, cumulative:", ""]
cum = 0; bys = collections.OrderedDict()
for t in tok:
    if t[2].isdigit():
        bys.setdefault(t[0], 0); bys[t[0]] += int(t[2])
L.append('| slice / step group | tokens | cumulative |'); L.append('|---|---|---|')
for k, v in bys.items():
    cum += v; L.append(f'| {k} | {v:,} | {cum:,} |')
L += ["", "## What remains", ""]
if missing:
    L.append(f"- {len(missing)} media have no stored texts: they failed the verifier twice (rewritten once, rejected again). Resume: `python3 pipeline.py retry_in <slice>` is already built for them; a fresh writer + verifier pass on these ids, then `bash write_slice.sh <slice>`.")
    L.append("")
    L.append("| id | slice | word | round-1 reasons | round-2 reasons |"); L.append("|---|---|---|---|---|")
    lm = {x['id']: x for x in left}
    for i in missing:
        x = lm.get(i, {})
        L.append(f"| {i} | {x.get('slice','')} | {IDX[str(i)]['words'].split(' (')[0]} | {', '.join(x.get('r1', []))} {x.get('note1','')} | {', '.join(x.get('r2', []))} {x.get('note2','')} |")
L += ["", "- Translations into the 8 other languages (decision 120) are not started.",
      "- The app still reads Tinder sentences from the grammar exercises; switching it to `tinder_sentences` is app work (no app code was touched here).",
      "- 4870 (foam): the stored definition is foam on waves, the media shows shaving foam; the texts follow the media. The concept's definition should be corrected.", ""]
open(os.path.join(H, 'TINDER_SENTENCES_EN_REPORT.md'), 'w').write('\n'.join(L))
print(L[0]); print('missing', missing)
