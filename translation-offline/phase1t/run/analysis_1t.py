#!/usr/bin/env python3
"""Phase 1T post-run analysis (0 model calls). Reads results_1t.json rows + raw judge verdicts. Written AFTER the run; changes no verdict."""
import json,os,sys,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import score_1t as S
H=os.path.dirname(os.path.abspath(__file__)); SET=os.path.join(H,'..','set')
rows=json.load(open(os.path.join(H,'results_1t.json')))['rows']
items={i['id']:i for i in json.load(open(os.path.join(SET,'data','items.json')))}
sents={s['sid']:s for s in json.load(open(os.path.join(SET,'data','sentences.json')))}
key=json.load(open(os.path.join(SET,'judge','_private','_key.json')))
V={}
for p in 'P1 P2 P3 P4'.split():
    for v in json.load(open(os.path.join(SET,'judge','verdicts_%s.json'%p))):
        k=key[v['jid']]
        if not k.get('duplicate_of') or k['item'] not in V: V[k['item']]=v
cp=None
for n in dir(S):
    if n.lower() in('cp','clopper','clopper_pearson','cp_interval'): cp=getattr(S,n)
def acc(r):
    for k in ('final_accept','accept','accepted'):
        if k in r: return bool(r[k])
    raise KeyError(list(r.keys()))
def fig(k,n):
    lo,hi=cp(k,n); return '%d/%d = %.2f %% [%.2f, %.2f]'%(k,n,100*k/n if n else 0,lo,hi)
out=[]
def P(*a): out.append(' '.join(str(x) for x in a))
def line(r):
    it=items[r['item_id']]; s=sents[r['sid']]; v=V[r['item_id']]
    return '- %s [%s %s] tags=%s layer=%s model=%s | SK: %s | ANS: %s | judge: %s%s'%(r['item_id'],r['level'],r['half'],','.join(r['tags']),r['layers']['main_layer'],r['layers'].get('model'),s['slovak'],it['answer'],v.get('note') or v.get('dropped') or '',' (borderline)' if v.get('borderline') else '')
lab=[r for r in rows if r.get('judged') in('correct','wrong')]
def cov_fa(jud):
    c=[r for r in lab if jud(r)=='correct']; w=[r for r in lab if jud(r)=='wrong']
    return sum(acc(r) for r in c),len(c),sum(acc(r) for r in w),len(w)
prim=lambda r:r['judged']
P('# ANALYSIS_1T (post-run, 0 calls)\n')
a=cov_fa(prim); P('primary: coverage',fig(a[0],a[1]),'· FA',fig(a[2],a[3]))
bw=lambda r:'correct' if (r['judged']=='wrong' and V[r['item_id']].get('borderline')) else r['judged']
a=cov_fa(bw); P('S2-wide (all 17 judged-wrong borderline items scored correct): coverage',fig(a[0],a[1]),'· FA',fig(a[2],a[3]))
bc=lambda r:'wrong' if (r['judged']=='correct' and V[r['item_id']].get('borderline')) else r['judged']
a=cov_fa(bc); P('S3 (all judged-correct borderline items scored wrong): coverage',fig(a[0],a[1]),'· FA',fig(a[2],a[3]))
both=lambda r:('correct' if r['judged']=='wrong' else 'wrong') if V[r['item_id']].get('borderline') else r['judged']
a=cov_fa(both); P('S4 (every borderline flipped): coverage',fig(a[0],a[1]),'· FA',fig(a[2],a[3]))
nb=[r for r in lab if not V[r['item_id']].get('borderline')]
c=[r for r in nb if r['judged']=='correct']; w=[r for r in nb if r['judged']=='wrong']
P('S5 (borderline items excluded): coverage',fig(sum(map(acc,c)),len(c)),'· FA',fig(sum(map(acc,w)),len(w)))
P('\n## 16 false accepts')
for r in lab:
    if r['judged']=='wrong' and acc(r): P(line(r))
P('\n## 32 false rejections')
for r in lab:
    if r['judged']=='correct' and not acc(r): P(line(r))
P('\n## agent-drop items AG v3 did NOT reject (tag agentdrop-*, judged wrong)')
ad=[r for r in lab if any(t.startswith('agentdrop') for t in r['tags']) and r['judged']=='wrong']
miss=[r for r in ad if not r['ag']['fired']]
P('AG fired on %d of %d; missed %d, of which L3 accepted %d'%(len(ad)-len(miss),len(ad),len(miss),sum(map(acc,miss))))
cnt=collections.Counter()
for r in miss:
    et=sents[r['sid']]['tags']['writer_tags'].get('emb_type') if 'writer_tags' in sents[r['sid']]['tags'] else None
    cnt[(','.join(t for t in r['tags'] if t.startswith('agentdrop')),et,r['ag']['reason'][:70])]+=1
    P(line(r),'| AG:',r['ag']['reason'],'| emb_type',et,'| ACCEPTED' if acc(r) else '| rejected')
P('\nmiss reasons:'); [P(' ',n,k) for k,n in cnt.most_common()]
P('\nAG catches by emb_type (embedded tag): ')
ce=collections.Counter(); te=collections.Counter()
for r in ad:
    if 'agentdrop-embedded' in r['tags']:
        et=sents[r['sid']]['tags'].get('writer_tags',{}).get('emb_type'); te[et]+=1; ce[et]+=r['ag']['fired']
[P('  %s: %d/%d'%(k,ce[k],te[k])) for k in sorted(te,key=str)]
P('\n## the 21 S-intent answers judged CORRECT')
s21=[r for r in lab if r.get('intent')=='S' and r['judged']=='correct']
P('n=%d, accepted by the stack %d'%(len(s21),sum(map(acc,s21))))
for r in s21: P(line(r),'| ACCEPTED' if acc(r) else '| rejected')
P('\n## other intent/judge disagreements')
for r in lab:
    if (r.get('intent')=='C' and r['judged']=='wrong') or (r.get('intent') in('T','W','M') and r['judged']=='correct') or (r.get('intent')=='S' and r.get('judged_type') not in(None,'S')): P(line(r),'| ACCEPTED' if acc(r) else '| rejected')
open(os.path.join(H,'ANALYSIS_1T.md'),'w').write('\n'.join(out)+'\n')
print('\n'.join(out[:8])); print(len(out),'lines')
