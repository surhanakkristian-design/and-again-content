import json,shutil
p='tr/b002/fr/ua.json'
shutil.copy(p,p+'.bak_verify_ua')
t=json.load(open(p))
log=[]
def rep(i,old,new,why,fields=('phrases','nouns','question','answer','recall')):
    v=t[i]
    for f in fields:
        if isinstance(v[f],list):
            for j,x in enumerate(v[f]):
                if old in x:
                    y=x.replace(old,new); v[f][j]=y; log.append(f"- {i} {f}[{j}]: \"{x}\" -> \"{y}\" ({why})")
        elif isinstance(v[f],str) and old in v[f]:
            y=v[f].replace(old,new); log.append(f"- {i} {f}: \"{v[f]}\" -> \"{y}\" ({why})"); v[f]=y
    assert any(i in l for l in log),(i,old)
rep('7962','коробку з-під піци','коробку для піци','the box still holds pizza; "з-під" means an emptied box')
rep('7962','коробка з-під піци','коробка для піци','same')
rep('7748','коробка з-під піци','коробка для піци','same word as for le carton/la boîte à pizza elsewhere')
rep('7858','фліска','флісова кофта','dictionary form instead of slang')
rep('7124','вітати з балкона','радісно вітати з балкона','acclamer = cheer; bare "вітати" reads as greet')
rep('5273','підкреслювати свій піджак','демонструвати свою куртку','veste here is a denim jacket (куртка); "підкреслювати" a garment is unidiomatic')
rep('747','паперова тяганина','папери','the clip shows stacks of paper, not bureaucracy')
rep('4918','бігти сходами через три сходинки','вибігати сходами, перестрибуючи через сходинки','quatre à quatre is an idiom for running up fast; literal count was wrong')
rep('7997','Вона є зіркою шоу.','Вона — зірка шоу.','"є" is unnatural in a Ukrainian present-tense sentence',('answer',))
rep('7369','обпливати кита на веслах','обпливати кита, гребучи веслом','one paddle on a paddle board')
rep('7453','лизати дно вока','облизувати дно вока','flames licking: "облизувати" is the natural verb')
rep('7845','бігати по траві','гасати по траві','gambader = frolic, not plain running')
rep('5358',"'жилет'","'кардиган'",'x') if False else None
v=t['5358'];j=v['nouns'].index('жилет');v['nouns'][j]='кардиган';log.append('- 5358 nouns['+str(j)+']: "жилет" -> "кардиган" (le gilet = the beige cardigan in the clip)')
v=t['7'];j=v['nouns'].index('шарф');v['nouns'][j]='стрічка';log.append('- 7 nouns['+str(j)+']: "шарф" -> "стрічка" (l\'écharpe = the graduation sash, not a scarf)')
rep('5671','розмахувати кулаком','піднімати кулак угору','encouraging fist pump; "розмахувати кулаком" reads as threatening')
rep('5517','тримати вудку','нести вудку','porter = carry; the man walks along the waves with it')
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
open('tr/b002/fr/tmp_ua_fixlog_b002.txt','w').write('\n'.join(log))
print('\n'.join(log))
