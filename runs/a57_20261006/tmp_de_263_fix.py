import json
def ld(i): return json.load(open(f'content/de/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/de/{i}.json','w'),ensure_ascii=False,indent=1)
d=ld(260)
d['recall'][2]['parts'][1]['accept']=['Brot','Toast']
sv(260,d)
d=ld(263)
d['taps'][2]['phrase']='in Ufernähe liegen'
d['recall'][1]['parts'][1]['accept']=['Schwimmbrille','Brille']
d['recall'][2]['parts']=[{'text':'in'},{'text':'Ufernähe','gap':True,'accept':['Ufernähe']},{'text':'liegen'}]
d['recall'][3]['parts'][1]['accept']=['See','Wasser']
d['notes']="Phrase 3: the rowing boat lies still near the shore (verifier: 'in Ufernähe liegen' instead of 'in Ufernähe treiben', since no drifting is visible; Ufernähe keeps the B-level word)."
sv(263,d)
