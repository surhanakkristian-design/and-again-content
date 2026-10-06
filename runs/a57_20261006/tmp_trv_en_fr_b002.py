import json
p='tr/b002/fr/en.json'; d=json.load(open(p))
fixes=[]
def rep(i,field,idx,old,new):
    cur=d[i][field] if idx is None else d[i][field][idx]
    assert cur==old,(i,field,cur)
    if idx is None: d[i][field]=new
    else: d[i][field][idx]=new
    fixes.append((i,field if idx is None else f"{field}[{idx}]",old,new))
rep('68','answer',None,"He is putting a bandage on his wrist.","He is putting a bandage on her wrist.")
rep('68','recall',3,"puts a bandage on his wrist","puts a bandage on her wrist")
rep('347','answer',None,"She is whispering gossip in her ear.","She is whispering gossip in his ear.")
rep('347','recall',3,"whispers gossip in her ear","whispers gossip in his ear")
for i,k in (('7744',2),('98',0)):
    rep(i,'phrases',k,"to stand open-mouthed","to be left open-mouthed")
    rep(i,'recall',k,"to stand open-mouthed","to be left open-mouthed")
rep('4125','phrases',0,"to pull on a veil","to pull on a sheet")
rep('4125','recall',0,"to pull on a veil","to pull on a sheet")
rep('4125','nouns',2,"the costume","the suit")
rep('5671','phrases',0,"to shake one's fist","to pump one's fist")
rep('5671','recall',0,"to shake one's fist","to pump one's fist")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
for f in fixes: print(f)
