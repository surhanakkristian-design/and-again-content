import json, math, re, sys, os, collections
T='/Users/kristiansurhanak/Projects/and-again-content/translation-offline'; P=T+'/phase2k'
def jl(p): return [json.loads(l) for l in open(p) if l.strip()]
def cp(x,n,a=0.05):
    if n==0: return (float('nan'),)*2
    def cdf(k,p):
        if p<=0: return 1.0
        if p>=1: return 0.0 if k<n else 1.0
        s=0.0
        for i in range(0,k+1): s+=math.exp(math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1)+i*math.log(p)+(n-i)*math.log1p(-p))
        return s
    def bis(f):
        lo,hi=0.0,1.0
        for _ in range(100):
            m=(lo+hi)/2
            if f(m): hi=m
            else: lo=m
        return (lo+hi)/2
    lo=0.0 if x==0 else bis(lambda p: 1-cdf(x-1,p)>=a/2)
    hi=1.0 if x==n else bis(lambda p: cdf(x,p)<=a/2)
    return (100*lo,100*hi)
SETS={'2I':(T+'/phase2i/set/items.jsonl',T+'/phase2i/run/results.jsonl',P+'/run_S2_2i/results.jsonl'),
      '2J':(T+'/phase2j/partD/set/items.jsonl',T+'/phase2j/partD/run/results.jsonl',P+'/run_S2_2j/results.jsonl')}
def load_res(p,tonly):
    d={}
    for r in jl(p):
        if tonly and r.get('stack','tonly')!='tonly': continue
        d[r['jid']]=r
    return d
# cause tables from reports
docs={'2J':T+'/phase2j/analysis/ANALYSIS.md','2I':T+'/phase2i/TRANSLATION_PRODUCTION_PHASE2I_REPORT.md'}
def tables(path):
    hdr=None; out=[]
    for line in open(path):
        s=line.strip()
        if not s.startswith('|'): hdr=None; continue
        cells=[c.strip() for c in s.strip('|').split('|')]
        if 'jid' in cells and 'cause' in cells: hdr=cells; continue
        if hdr and not set(s)<=set('|-: '): 
            if len(cells)==len(hdr): out.append(dict(zip(hdr,cells)))
    return out
data={}; changed_all=[]; summ={}
for S,(ip,op,np_) in SETS.items():
    items=jl(ip); old=load_res(op,True); new=load_res(np_,False)
    assert len(items)==900 and len(old)>=900 and len(new)==900, (S,len(items),len(old),len(new))
    cause={}
    for dn,dp in docs.items():
        for row in tables(dp):
            j=row.get('jid'); ans=row.get('answer')
            cause.setdefault((j,ans),[]).append((dn,row.get('cause')))
    rows=[]
    for it in items:
        j=it['jid']; o=old[j]; n=new[j]
        c=[x for x in cause.get((j,it['answer']),[])]
        rows.append(dict(set=S,jid=j,level=it['level'],label=it['judge_label'],wtype=it.get('writer_type'),slovak=it['slovak'],answer=it['answer'],
            ref=' ‖ '.join(it.get('v') or []),old_acc=bool(o['accept']),new_acc=bool(n['accept']),old_layer=o.get('layer'),old_l3=o.get('l3_reply'),
            new_layer=n.get('layer'),new_l3=n.get('l3_reply'),old_cause=(c[0][1] if c else None),old_cause_doc=(c[0][0] if c else None)))
    data[S]=rows
def metr(rows):
    C=[r for r in rows if r['label']=='correct']; W=[r for r in rows if r['label']=='wrong']
    out={}
    for k in ('old','new'):
        xc=sum(r[k+'_acc'] for r in C); xw=sum(r[k+'_acc'] for r in W)
        out[k]={'cov':[xc,len(C),round(100*xc/len(C),2),[round(v,2) for v in cp(xc,len(C))]],'fa':[xw,len(W),round(100*xw/len(W),2),[round(v,2) for v in cp(xw,len(W))]]}
    return out
res={}
groups={'2I':data['2I'],'2J':data['2J'],'pooled':data['2I']+data['2J']}
for g,rows in groups.items():
    res[g]={'all':metr(rows)}
    for L in ('A1','A2','B1','B2'): res[g][L]=metr([r for r in rows if r['level']==L])
def mech(r):
    o='%s%s'%(r['old_layer'],('/'+r['old_l3']) if r['old_l3'] and str(r['old_layer']).startswith('L3') else '')
    n='%s%s'%(r['new_layer'],('/'+r['new_l3']) if r['new_l3'] and str(r['new_layer']).startswith('L3') else '')
    if r['new_acc']:
        if str(r['old_layer']).startswith('AG'): m='reference-reading AG removed; source-only L3 SAME'
        elif str(r['old_layer']).startswith('L3'): m='source-only L3 SAME where reference-based L3 said %s'%r['old_l3']
        else: m='reference layer %s removed; source-only L3 SAME'%r['old_layer']
    else:
        if str(r['new_layer']).startswith('AG'): m='source-only AG fires (no reference alignment)'
        elif str(r['new_layer']).startswith('F4'): m='%s fires'%r['new_layer']
        elif str(r['old_layer']).startswith('L3'): m='source-only L3 %s where reference-based L3 said %s'%(r['new_l3'],r['old_l3'])
        else: m='reference layer %s accept gone; source-only L3 %s'%(r['old_layer'],r['new_l3'])
    return o,n,m
ch=[]
for g in ('2I','2J'):
    for r in data[g]:
        if r['old_acc']!=r['new_acc']:
            o,n,m=mech(r); ok=(r['new_acc']==(r['label']=='correct'))
            ch.append(dict(r,old=o,new=n,mech=m,effect=('fixed' if ok else 'broken')))
ref25=[r for r in data['2J'] if r['old_cause']=='reference wrong or too narrow' and r['old_cause_doc']=='2J' and r['label']=='correct' and not r['old_acc']]
ref25_acc=[r for r in ref25 if r['new_acc']]
fa_add={g:[r for r in data[g] if r['label']=='wrong' and r['new_acc'] and not r['old_acc']] for g in data}
fa_rem={g:[r for r in data[g] if r['label']=='wrong' and r['old_acc'] and not r['new_acc']] for g in data}
fr_add={g:[r for r in data[g] if r['label']=='correct' and not r['new_acc'] and r['old_acc']] for g in data}
fr_rem={g:[r for r in data[g] if r['label']=='correct' and r['new_acc'] and not r['old_acc']] for g in data}
layers={g:dict(collections.Counter(r['new_layer'] for r in data[g])) for g in data}
led=json.load(open(P+'/GEMINI_LEDGER.json'))
spend=sum(json.loads(l).get('cost_usd',0) for d in ('run_S2_2i','run_S2_2j') for l in open(P+'/'+d+'/ledger.jsonl') if l.strip() and json.loads(l).get('counted'))
pfa=res['pooled']['all']['new']['fa'][2]; stop=pfa>8.0
out=dict(res=res,changed=len(ch),ref25=[len(ref25),len(ref25_acc)],fa_added={g:len(v) for g,v in fa_add.items()},fa_removed={g:len(v) for g,v in fa_rem.items()},
  fr_added={g:len(v) for g,v in fr_add.items()},fr_removed={g:len(v) for g,v in fr_rem.items()},new_layers=layers,ledger=led,spend_usd=round(spend,4),safety_stop=stop,
  mech_counts=dict(collections.Counter((c['set'],c['label'],c['effect'],c['mech']) .__str__() for c in ch)))
json.dump(out,open(P+'/analysis/part3.json','w'),indent=1,ensure_ascii=False)
def f(m): return '%d/%d = %.2f %% [%.2f, %.2f]'%(m[0],m[1],m[2],m[3][0],m[3][1])
L=['# Part 3 - CLOSED-SET RE-SCORE of SOURCE-ONLY on the Slovak sets (Phase 2K S2, 21.9.2026)','',
 'Closed-set re-score: the 2I set (900 items) and the 2J Part D set (900 items) were judged in earlier phases; their EXISTING judge labels are used. '
 'No new writers, no new judges, no headless Claude. Stack = frozen S1 SOURCE-ONLY (FREEZE_COMMIT_S1 e394bc2), gemini-3.1-flash-lite, temp 0, thinkingBudget 0, TIP-as-rejection ON. '
 'Reference-based column = the stored per-item results of the 2I translation-only stack (phase2i/run/results.jsonl, stack tonly) and the 2J fixed stack (phase2j/partD/run/results.jsonl) on the same items. '
 'Closed sets were seen while the reference-based stacks were built, and the source-only prompt was written after reading their failures, so these are not fresh-set numbers.','',
 'Gemini calls: S2_2i %s, S2_2j %s (ledger %s); spend $%.4f. New-stack layers: %s.'%(led.get('S2_2i'),led.get('S2_2j'),json.dumps(led),spend,json.dumps(layers)),'',
 '## Coverage and FA (exact 95 %% Clopper-Pearson)','','| set | level | coverage ref-based | coverage SOURCE-ONLY | FA ref-based | FA SOURCE-ONLY |','|---|---|---|---|---|---|']
for g in ('2I','2J','pooled'):
    for lv in ('all','A1','A2','B1','B2'):
        m=res[g][lv]; L.append('| %s | %s | %s | %s | %s | %s |'%(g,lv,f(m['old']['cov']),f(m['new']['cov']),f(m['old']['fa']),f(m['new']['fa'])))
L+=['','Targets (coverage >= 90 %%, FA < 5 %%), pooled SOURCE-ONLY: coverage %s on the point, %s on the interval; FA %s on the point, %s on the interval.'%(
 'MET' if res['pooled']['all']['new']['cov'][2]>=90 else 'MISSED','MET' if res['pooled']['all']['new']['cov'][3][0]>=90 else 'MISSED',
 'MET' if pfa<5 else 'MISSED','MET' if res['pooled']['all']['new']['fa'][3][1]<5 else 'MISSED'),'',
 '**SAFETY STOP (pooled FA > 8.0 %%): %s** (pooled FA %.2f %%).'%('FIRED - STOP_part3.md written' if stop else 'not fired',pfa),'',
 '## What moved','',
 '| set | FR removed (correct now accepted) | FR added (correct now rejected) | FA removed | FA added |','|---|---|---|---|---|']
for g in ('2I','2J'): L.append('| %s | %d | %d | %d | %d |'%(g,len(fr_rem[g]),len(fr_add[g]),len(fa_rem[g]),len(fa_add[g])))
L.append('| pooled | %d | %d | %d | %d |'%tuple(sum(len(x[g]) for g in ('2I','2J')) for x in (fr_rem,fr_add,fa_rem,fa_add)))
L+=['','2J reference-caused false rejections ("reference wrong or too narrow", phase2j/analysis/ANALYSIS.md): **%d of %d now accepted**.'%(len(ref25_acc),len(ref25)),
 'Still rejected: '+(', '.join('%s (%s)'%(r['jid'],r['new']if 'new' in r else r['new_layer']+'/'+str(r['new_l3'])) for r in ref25 if not r['new_acc']) or 'none'),'',
 'Mechanism counts (set, label, effect, mechanism):','']
for k,v in sorted(out['mech_counts'].items(),key=lambda x:-x[1]): L.append('- %s: %d'%(k,v))
L+=['','## Every item whose verdict changed (%d)'%len(ch),'','Cause = mechanical cause of the flip (old layer -> new layer); "earlier cause" = the cause label the 2I/2J analysis gave that item when it was an FR/FA (blank if it was not listed).','',
 '| # | set | jid | level | label | writer | Slovak | reference(s) | answer | ref-based | SOURCE-ONLY | effect | cause | earlier cause |','|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
esc=lambda s:str(s).replace('|','/')
for i,c in enumerate(sorted(ch,key=lambda c:(c['set'],c['effect'],c['label'],c['jid'])),1):
    L.append('| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |'%(i,c['set'],c['jid'],c['level'],c['label'],c['wtype'] or '',esc(c['slovak']),esc(c['ref']),esc(c['answer']),c['old'],c['new'],c['effect'],c['mech'],esc(c['old_cause'] or '')))
open(P+'/analysis/part3.md','w').write('\n'.join(L)+'\n')
if stop:
    open(P+'/STOP_part3.md','w').write('# STOP part 3\n\nPooled SOURCE-ONLY FA %.2f %% > 8.0 %% on the closed-set re-score (analysis/part3.md). Per the brief: stop here, no Czech, orchestrator writes the report.\n'%pfa)
print(json.dumps({k:out[k] for k in ('changed','ref25','fa_added','fa_removed','fr_added','fr_removed','safety_stop','spend_usd','ledger')}))
for g in ('2I','2J','pooled'):
    m=res[g]['all']; print(g,'old',f(m['old']['cov']),f(m['old']['fa']),'| new',f(m['new']['cov']),f(m['new']['fa']))
