import json
p='tr/b001/fr/cz.json'; d=json.load(open(p)); log=[]
def rep(i,field,old,new,why):
    v=d[i][field]
    if isinstance(v,list):
        n=0
        for j,x in enumerate(v):
            if x==old: v[j]=new; n+=1
        assert n, (i,field,old)
    else:
        assert v==old,(i,field,v); d[i][field]=new
    log.append(f"- {i} {field}: {old} -> {new} ({why})")
wo='more natural word order'
for i,o,n in [('646','otevřít doširoka pusu','doširoka otevřít pusu'),('5468','otevřít doširoka oči','doširoka otevřít oči'),('665','otevřít doširoka tlamu','doširoka otevřít tlamu'),('4568','rozpřáhnout široce ruce','široce rozpřáhnout ruce'),('291','rozpřáhnout široce ruce','široce rozpřáhnout ruce')]:
    rep(i,'phrases',o,n,wo); rep(i,'recall',o,n,wo)
for f in ['phrases','recall']: rep('472',f,'držet nářadí','držet nástroj','outil is one tool; nářadí is collective')
rep('472','nouns','nářadí','nástroj','outil is one tool; nářadí is collective')
rep('5129','nouns','helma','sluchátka','le casque here = headphones round his neck, not a helmet')
rep('5108','answer','Mávají z jednoho domu ve vesnici.','Mávají z domu ve vesnici.','"z jednoho" adds emphasis not in the source')
rep('5108','recall','mávají z jednoho domu ve vesnici','mávají z domu ve vesnici','same as answer')
rep('358','question','Na co tluče kladivo?','Do čeho tluče kladivo?','Czech: tlouct do něčeho')
rep('358','answer','Kladivo tluče na hřebík.','Kladivo tluče do hřebíku.','Czech: tlouct do něčeho')
rep('358','recall','tluče na hřebík','tluče do hřebíku','Czech: tlouct do něčeho')
for f in ['phrases','recall']:
    rep('225',f,'sednout si ke stolu','sednout si k psacímu stolu','same word for le bureau as noun/answer (psací stůl)')
    rep('225',f,'chodit po stole','chodit po psacím stole','same word for le bureau as noun/answer (psací stůl)')
    rep('7809',f,'zaplatit koláč','zaplatit za koláč','natural: zaplatit za něco')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('tmp_fix_cz_fr_b001.log','w').write('\n'.join(log)+'\n')
print(len(log))
