import json,collections,re
BASE='https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/'
M={r['id']:r for r in json.load(open('sample_100_v2_media.json'))}
order_ids=[r['id'] for r in json.load(open('sample_100_v2_media.json'))]
R1={int(l.split('\t')[0]):l.rstrip('\n').split('\t')[1:] for l in open('pairs_r1_orig.tsv')}
P={int(l.split('\t')[0]):l.rstrip('\n').split('\t')[1:] for l in open('pairs_r2.tsv')}
v1={x['id']:x for x in json.load(open('verifier_r1.json'))}
v2={x['id']:x for x in json.load(open('verifier_r2.json'))}
final={i:(v2.get(i) or v1[i]) for i in P}
acc=[i for i in order_ids if final[i]['verdict']=='ACCEPT']; rej=[i for i in order_ids if final[i]['verdict']!='ACCEPT']
TONES=['Chill','Slang','Ironic','Dramatic','Business','Gossip','Nerd','Flirt','Low IQ']
DEVN={'exaggeration':'Exaggeration','understatement':'Understatement','excuse':'Bad excuse / cliché excuse','cliche':'Cliché','blame':'Blaming someone else','banter':'Men/women banter','cheap':'Cheap things / bad quality','guessing':'Guessing thoughts or what happens next','exclamation':'Exclamation-driven emotion','other':'Vacuous obviousness (Low IQ)','none':'No joke (body-part word)'}
dist=collections.Counter(P[i][0] for i in acc); dev=collections.Counter(P[i][1] for i in acc)
ban=collections.Counter(P[i][2] for i in acc if P[i][1]=='banter')
def rec(i):
    r=M[i]; tone,d,b,T,F=P[i]; ext='mp4' if r['media_type']=='video' else 'webp'
    return {"media_id":i,"word":r['words'],"media_type":r['media_type'],"level":r['level'],"category":r['cats'],"style":r['style'],
     "thumbnail_url":f"{BASE}Thumbnails/{r['title']}.webp","media_url":f"{BASE}Words/{r['title']}.{ext}","description":r['asset_description'],
     "true_sentence":T,"false_sentence":F,"tone":tone,"true_len":len(T),"false_len":len(F)}
recs=[rec(i) for i in acc]
json.dump(recs,open('SAMPLE_100_v2.json','w'),indent=1,ensure_ascii=False)
# chars over 50
over=[(i,P[i][3],P[i][4]) for i in acc if max(len(P[i][3]),len(P[i][4]))>50]
json.dump({'acc':len(acc),'rej':rej,'dist':dist,'dev':dev,'ban':ban,'over':len(over)},open('stats.json','w'),default=str)
print(len(acc),rej,dist,dev,ban,len(over))

def esc(s): return str(s).replace('|','\\|')
def one(s,n=160):
    s=' '.join(s.split()); return s if len(s)<=n else s[:n-1].rstrip()+'…'
cont=re.compile(r"\b(is|are|am)\s+\w+ing\b")
over_cont=sum(1 for i,T,F in over if cont.search(T) or cont.search(F))
over_true=sum(1 for i,T,F in over if len(T)>50)
lens=[len(P[i][3]) for i in acc]+[len(P[i][4]) for i in acc]
tw=[i for i in acc]
L=["# Tinder sentence pairs: sample 2 (English only)","",
"Written 25 Sept 2026 after the owner's review of sample 1. Nothing was written to the database and nothing is live. Every sentence was written from `media.asset_description`, plus the transcript when there is one. None of these 100 media or their words were in sample 1.","",
"## What changed from sample 1","",
"- The target word is in every TRUE sentence (the verifier checked this for each pair).",
"- The limit is 60 characters, up from 50. Actions happening in the media use the present continuous (\"She is jumping into the pool\"). The present simple is kept for states, habits and one-off moments.",
"- Every pair uses one humour device, and no device appears twice in a row in writing order.",
"- The register rules and the men/women banter rules from the brief were applied. None of the banned words appear, and none of the allowed swear words were needed.","",
"## Summary","",
f"- **Pairs counted (writer and verifier both accept): {len(acc)} / 100.**",
f"- Round 1: the independent Opus verifier rejected {sum(1 for x in v1.values() if x['verdict']!='ACCEPT')} of 100. I rewrote those 17 and the same verifier checked them again. Round 2 rejected {len(rej)}: {', '.join(str(i) for i in rej)} (see the end of this file).",
"- **Humour devices (counted pairs):** "+", ".join(f"{DEVN[k]} {v}" for k,v in dev.most_common()),
f"- **Men/women banter:** {sum(ban.values())} pairs. {ban['he']} have him as the one who thinks he is the best, {ban['she']} have her as the one who thinks she is the best, and {ban['both']} has both (4036: she thinks she is a model, he thinks he is a pro). So it is 6 on each side. None is about looks or intelligence.",
"- **Tone distribution (counted pairs):** "+", ".join(f"{t} {dist[t]}" for t in TONES),
f"- **Longer than 50 characters:** {len(over)} of {len(acc)} pairs have at least one sentence over 50 ({over_true} of them are TRUE sentences). The longest is {max(lens)} and the median is {sorted(lens)[len(lens)//2]}. The reason is structural. Most pairs now have two parts: a correct description of the media, then the joke (\"The leaf is missing a bite. The insect blames the snail.\"). {over_cont} of the {len(over)} use a present continuous (\"is/are …ing\"), which adds a word and 3 letters compared with sample 1's present simple. The description alone would almost always fit in 50. The extra room is used by the joke.",
"",
"## Tone balance: what to watch",
"",
"Chill (35) and Dramatic (25) are over-represented. Nerd (1), Flirt (2), Gossip (3) and Low IQ (3) are thin. The humour devices push that way: exclamations and exaggeration read as Dramatic, and Nerd forbids invented facts, which rules out most jokes. The verifier rejected the only other Nerd joke (4823), and 5239 failed twice for the same reason. For the full run, I suggest either loosening Nerd to allow a dry joke or accepting that Nerd pairs will be plain.","",
"## How the 100 were picked","",
"- The pool was all live media with an asset description, minus the 100 media in sample 1 and every word that appeared in sample 1. Levels follow the same rule as sample 1.",
"- Quotas: 22 each of A1, A2, B1 and B2, plus 6 A and 6 B. Within each level I alternated image and video. A seeded greedy pick favoured categories, visual styles and upload dates that were not yet represented.",
"- Result: 56 images and 44 videos. All 40 categories appear. Styles: Videos 25, Anime 18, Illustrations 18, Photos 18, Disney 17, 80s Cartoons 4. Upload dates: 17 Sept 66, 21 Aug 17, 24 Aug 9, 23 Aug 8.","",
"Columns: device = the humour device used; T = TRUE sentence, F = FALSE sentence, each with its character count.",""]
for t in TONES:
    ids=[i for i in acc if P[i][0]==t]
    if not ids: continue
    L+=[f"## {t} ({len(ids)})","","| id | word | type | level | category | what the media shows | device | TRUE | chars | FALSE | chars |","|---|---|---|---|---|---|---|---|---|---|---|"]
    for i in sorted(ids,key=lambda i:(M[i]['level'],i)):
        r=M[i]; tone,d,b,T,F=P[i]
        dv=DEVN[d]+(f" ({'him' if b=='he' else 'her' if b=='she' else 'both'})" if d=='banter' else '')
        L.append(f"| {i} | {esc(r['words'])} | {r['media_type']} | {r['level']} | {esc(r['cats'])} | {esc(one(r['asset_description']))} | {dv} | {esc(T)} | {len(T)} | {esc(F)} | {len(F)} |")
    L.append("")
L+=["## Round 1 rejections (the verifier's reason, then the fix)","","| id | round-1 TRUE / FALSE | rule | reason | round-2 TRUE / FALSE | round 2 |","|---|---|---|---|---|---|"]
for i in order_ids:
    x=v1[i]
    if x['verdict']!='ACCEPT':
        o=R1[i]; n=P[i]
        L.append(f"| {i} | {esc(o[3])} / {esc(o[4])} | {x['rule']} | {esc(x['reason'])} | {esc(n[3])} / {esc(n[4])} | {final[i]['verdict']}{(': '+esc(final[i]['reason'])) if final[i]['verdict']!='ACCEPT' else ''} |")
if rej:
    L+=["","## Not counted (still rejected after round 2)",""]+[f"- **{i}** ({M[i]['words']}, {P[i][0]}): *{P[i][3]}* / *{P[i][4]}*. Reason: {final[i]['reason']} The verifier suggested a plain Nerd description with no joke. I did not use it, because the brief asks for humour." for i in rej]
L+=["","Verifier rules: 1 the target word is in TRUE; 2 TRUE is true; 3 FALSE is clearly false on one checkable fact; 4 grammar and exact tense; 5 at most 60 characters; 6 the tone fits and is allowed at the level; 7 survives translation; 8 register and safety (banned words, body/looks, banter); 9 humour (soft).","",
"## Token estimate for all 3,664 media","",
"This sample used about 330k tokens per 100 media: about 90k for selection and writing, about 112k for the verifier's full pass, and about 118k for its re-check. The re-check was expensive only because it resumed the verifier with its whole first pass still in context. Scaled up as run here, that is about 12 million tokens (37 batches). With a fresh, small verifier for the re-check (about 15–20k), it is about 220k per 100, or **about 8 million tokens** for all 3,664. Giving the verifier only one line of description per media would bring it to roughly 6 million.",""]
open('SAMPLE_100_v2.md','w').write('\n'.join(L))
# HTML
h=open('../SAMPLE_100.html').read()
data=[dict(rec(i),device=DEVN[P[i][1]].split(' (')[0] if P[i][1]!='banter' else 'Men/women banter') for i in acc]
a=h.index('const DATA = ')
b=h.index(';\n',a)
h=h[:a]+'const DATA = '+json.dumps(data,ensure_ascii=False)+h[b:]
h=h.replace('<title>Tinder Sample Review</title>','<title>Tinder Sample 2</title>')
h=h.replace('<h1>Tinder sentence pairs, sample of 100','<h1>Tinder sentence pairs, sample 2')
h=h.replace("const keys=['tone','level','media_type','category'];","const keys=['tone','device','level','media_type','category'];")
h=h.replace("const sel={tone:null,level:null,media_type:null,category:null}","const sel={tone:null,device:null,level:null,media_type:null,category:null}")
h=h.replace('<div class="row" id="f-level">','<div class="row" id="f-device"><span>Humour</span></div>\n<div class="row" id="f-level">')
h=h.replace("l>50?' over':''","l>60?' over':''")
h=h.replace('<span class="tone">${esc(d.tone)}</span>','<span class="tone">${esc(d.tone)}</span> <span class="tone">${esc(d.device)}</span>')
h=h.replace("d.category,d.tone]","d.category,d.tone,d.device]")
open('SAMPLE_100_v2.html','w').write(h)
print('built')
