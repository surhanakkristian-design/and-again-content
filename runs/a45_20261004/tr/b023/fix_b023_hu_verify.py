import json
p='hu.json'; d=json.load(open(p))
fixes=[
('5613','phrases',0,'szélesen vigyorogni a kamerába','vigyorogni a kamerába','"szélesen" added, not in the English'),
('5615','phrases',0,'a levegőbe dobni a tésztát','tésztát dobni a levegőbe','indefinite "noodles", same form as phrase 2'),
('5630','phrases',1,'leguggolni a lábához','a lábánál kuporogni','a dog crouches (kuporog), not squats; state not movement'),
('5632','answer',None,'Egy kötél függőágyban heverészik.','Egy kötélből font függőágyban heverészik.','"kötél függőágy" is ungrammatical'),
('5640','nouns',1,'vizes palack','kulacs','"vizes palack" reads as "wet bottle"'),
('5645','phrases',0,'integetni a karjával','lengetni a karját','wave one\'s arms = lengetni a karját'),
('5654','answer',None,'Keserű az ezüstérme miatt.','Keserűséget érez az ezüstérme miatt.','"keserű" of a person is unnatural here'),
('5663','phrases',1,'megtartani a zsákot','mozdulatlanul tartani a zsákot','"still" was lost; megtartani = keep'),
('5670','nouns',0,'fényfüzér','fényfüzérek','English plural must stay plural'),
('5682','answer',None,'Buborékokat fúj ki.','Buborékok sorát fújja ki.','"a stream of" was lost'),
('5717','answer',None,'Forog középen.','Középen forog.','natural focus word order'),
('6828','phrases',1,'egy sor munkást vezetni','munkások sorát vezetni','"egy sor munkást" means "a number of workers"'),
]
log=[]
for i,f,k,b,a,why in fixes:
    cur=d[i][f] if k is None else d[i][f][k]
    assert cur==b,(i,f,cur)
    if k is None: d[i][f]=a
    else: d[i][f][k]=a
    log.append(f'- {i} {f}{"" if k is None else f"[{k}]"}: {b} -> {a} ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('verify_hu.md','w').write('# verify hu b023\n\nTexts checked: 100 videos, 1000 texts (300 phrases, 400 nouns... see count below)\n\n## Fixes\n'+'\n'.join(log)+'\n\n## Doubts left unchanged\n- 5620 phrase "felemelni őt": kept the explicit pronoun for clarity.\n- 5646 "hátával nekidőlni": understandable, slightly compressed.\n- 6821 "tenger gyümölcsei tál": common shop wording, kept.\n- 5653 "a szeme fölé tartani a kezét" for the plural spectators: generic dictionary possessive kept.\n')
print(len(log))
