import json
p='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/fr/hu.json'
h=json.load(open(p))
def rep(i,old,new):
    n=0
    for k in ('phrases','nouns','recall'):
        h[i][k]=[ (new if x==old else x) for x in h[i][k]]
    for k in ('question','answer'):
        pass
def setf(i,k,idx,old,new):
    if idx is None:
        assert h[i][k]==old,(i,k,h[i][k]); h[i][k]=new
    else:
        assert h[i][k][idx]==old,(i,k,h[i][k][idx]); h[i][k][idx]=new
# gilet = cardigan
setf('36','nouns',3,'mellény','kardigán')
setf('6','nouns',1,'mellény','kardigán')
# costume = suit (white suit)
setf('4125','nouns',2,'jelmez','öltöny')
# state, not falling asleep
for k in ('phrases','recall'):
    idx=h['4209'][k].index('mély álomba merülni'); h['4209'][k][idx]='mély álomba merülve aludni'
setf('7844','answer',None,'Két nemzedék női forgatják a palacsintákat.','Két nemzedékhez tartozó nő forgatja a palacsintákat.')
for k in ('phrases','recall'):
    i2=h['7849'][k].index('egy deszkán pihenni'); h['7849'][k][i2]='egy deszkán feküdni'
    i3=h['7962'][k].index('a pizzamaradékot tartalmazni'); h['7962'][k][i3]='tartalmazni a pizzamaradékot'
    i4=h['4918'][k].index('nehezen cipelni a nehéz szatyrokat'); h['4918'][k][i4]='küszködni a nehéz szatyrok cipelésével'
    i5=h['5671'][k].index('rázni az öklét'); h['5671'][k][i5]='a magasba emelni az öklét'
    i6=h['376'][k].index('bugyogni a sziklák között'); h['376'][k][i6]='zubogni a sziklák között'
json.dump(h,open(p,'w'),ensure_ascii=False,indent=2)
