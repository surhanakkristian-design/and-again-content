import json,collections
S={r['id']:r for r in json.load(open('sample_100.json'))}
P={int(l.split('\t')[0]):l.rstrip('\n').split('\t')[1:] for l in open('pairs_v2.tsv')}
v1={x['id']:x for x in json.load(open('verifier_v1.json'))}
v2={x['id']:x for x in json.load(open('verifier_v2.json'))}
V1={int(l.split('\t')[0]):l.rstrip('\n').split('\t')[1:] for l in open('pairs_v1.tsv')}
final={i:(v2[i] if i in v2 else v1[i]) for i in P}
acc=[i for i in P if final[i]['verdict']=='ACCEPT']; rej=[i for i in P if final[i]['verdict']!='ACCEPT']
order=['Chill','Slang','Ironic','Dramatic','Business','Gossip','Nerd','Flirt','Low IQ']
dist=collections.Counter(P[i][0] for i in acc)
def one(s,n=160):
    s=' '.join(s.split()); return s if len(s)<=n else s[:n-1].rstrip()+'…'
def esc(s): return s.replace('|','\\|')
L=[]
L+=["# Tinder sentence pairs: sample of 100 (English only)","",
"Written 25 Sept 2026. This is a sample for the owner to review. Nothing was written to the database and nothing is live. Every sentence was written from `media.asset_description`, plus the transcript when there is one.","",
"## Summary","",
f"- **Pairs counted (writer and verifier both accept): {len(acc)} / 100.**",
f"- Round 1: the verifier rejected {sum(1 for x in v1.values() if x['verdict']!='ACCEPT')} of 100 (see the list below). I rewrote those {len(v2)} pairs and the same verifier checked them again. Round 2 rejected {sum(1 for x in v2.values() if x['verdict']!='ACCEPT')}.",
"- **Tone distribution (counted pairs):** "+", ".join(f"{t} {dist[t]}" for t in order),
"- **Over 50 characters:** one draft only, 5370 *\"Paddle, walk, cinnamon bun. Kinda perfect day, bro.\"* (51 characters). I cut it to 45 before verification. No final sentence is over 50 characters.",
"- **Token estimate for all 3,664 media:** this sample used about 155k tokens per 100 media: roughly 30k to write, about 105k for the independent Opus check, and about 20k for the rewrite-and-recheck round. Scaled up, that is **about 5.5–6 million tokens** (37 batches). The verifier is about two thirds of the cost. Giving it only one line of description per media would bring the total to roughly 3.5–4 million.","",
"## How the 100 were picked","",
"- The pool was all 3,667 live media that have an asset description (3 had none). Level is the most frequent specific CEFR level among the media's exercises. 1,373 media only have generic A or B exercise types, so they are labelled A or B.",
"- Quotas: 22 each of A1, A2, B1 and B2, plus 6 A and 6 B. Within each level I alternated image and video. A seeded greedy pick favoured categories, visual styles, upload dates and words that were not yet represented.",
"- Result: 56 images and 44 videos. All 40 categories appear. All 6 visual styles appear (Videos 24, Disney 18, Illustrations 18, Photos 18, Anime 17, 80s Cartoons 5). Upload dates: 21 Aug 17, 23 Aug 8, 24 Aug 9, 17 Sept 66. The newest batch is over-represented because it makes up 40 % of the library.",
"- The tones are the app's nine styles from `supabase/functions/_shared/toneStyles.json`: Chill, Slang, Ironic, Dramatic, Business, Gossip, Nerd, Flirt, Low IQ. I kept each style's level gates (Nerd B1+, Ironic and Gossip A2+, Low IQ A1–B1). Flirt is used only on adults and compliments actions and style only.","",
"Columns: T = TRUE sentence, F = FALSE sentence, and the character count of each.",""]
for t in order:
    ids=[i for i in acc if P[i][0]==t]
    if not ids: continue
    L+=[f"## {t} ({len(ids)})","","| id | word | type | level | category | what the media shows | TRUE | chars | FALSE | chars |","|---|---|---|---|---|---|---|---|---|---|"]
    for i in sorted(ids,key=lambda i:(S[i]['level'],i)):
        r=S[i]; tone,T,F=P[i]
        L.append(f"| {i} | {esc(r['words'])} | {r['media_type']} | {r['level']} | {esc(r['cats'] or '')} | {esc(one(r['asset_description']))} | {esc(T)} | {len(T)} | {esc(F)} | {len(F)} |")
    L.append("")
L+=["## Round 1 rejections (the verifier's reasons, then the fix)","","| id | tone | round-1 TRUE / FALSE | reason | round-2 result |","|---|---|---|---|---|"]
for i,x in v1.items():
    if x['verdict']!='ACCEPT':
        L.append(f"| {i} | {V1[i][0]} | {esc(V1[i][1])} / {esc(V1[i][2])} | rule {x['rule']}: {esc(x['reason'])} | {final[i]['verdict']}{(': '+esc(final[i]['reason'])) if final[i]['verdict']!='ACCEPT' else ''} |")
if rej:
    L+=["","## Not counted (still rejected after round 2)",""]+[f"- **{i}** ({P[i][0]}): {P[i][1]} / {P[i][2]}. Reason: {final[i]['reason']}" for i in rej]
L+=["","Verifier rules: 1 TRUE is true; 2 FALSE is visibly false; 3 grammar; 4 at most 50 characters; 5 tone fits and is allowed at the level; 6 survives translation (no wordplay or idioms); 7 safe for 13+.",""]
open('SAMPLE_100.md','w').write('\n'.join(L)); print(len(acc),dist)
