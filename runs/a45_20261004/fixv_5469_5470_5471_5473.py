import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setkey(c,ti,t,**kw):
    for k in c['taps'][ti]['keys']:
        if abs(k['t']-t)<0.01:
            k.clear(); k.update({'t':t}); k.update(kw)
# 5469
c=load(5469)
c['taps'][2]['phrase']='to shoot a jet of water'
save(5469,c)
# 5470
c=load(5470)
c['stillS']=9.5
c['nouns']=[{'word':'billboards','x':0.45,'y':0.12,'voice':'female'},
 {'word':'a traffic light','x':0.8,'y':0.34,'voice':'female'},
 {'word':'a crowd','x':0.45,'y':0.47,'voice':'female'},
 {'word':'a zebra crossing','x':0.22,'y':0.88,'voice':'female'}]
c['answer']=['He','is','carrying','a','bulky','backpack.']
save(5470,c)
# 5471
c=load(5471)
for ti in (0,1):
    setkey(c,ti,3.5,x=0.0,y=0.78,w=0.72,h=0.22)
    setkey(c,ti,4.0,x=0.0,y=0.36,w=0.46,h=0.64)
    setkey(c,ti,4.5,x=0.0,y=0.38,w=0.46,h=0.62)
setkey(c,2,3.5,x=0.53,y=0.23,w=0.19,h=0.55)
setkey(c,2,4.0,x=0.46,y=0.29,w=0.18,h=0.33)
setkey(c,2,4.5,x=0.46,y=0.30,w=0.18,h=0.30)
for n in c['nouns']:
    if n['word']=='a wooden shelf': n['x'],n['y']=0.33,0.58
save(5471,c)
# 5473
c=load(5473)
for n in c['nouns']:
    if n['word']=='a wallet': n['word']='a coin purse'
c['question']='What is pouring onto the table?'
c['answer']=['Loose','coins','are','pouring','onto','the','table.']
save(5473,c)
