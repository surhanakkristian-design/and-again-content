import json
def L(i): return json.load(open(f'content/es/{i}.json'))
def S(i,d): json.dump(d,open(f'content/es/{i}.json','w'),ensure_ascii=False,indent=1)
d=L(34)
d['taps'][1]['phrase']='tener la barba corta'
d['taps'][2]['phrase']='correr por el césped'
d['recall'][1]['parts'][0]['text']='tener la'
d['recall'][2]['parts'][1]['text']='por el césped'
S(34,d)
d=L(35)
d['recall'][3]['parts'][1]['accept']=['llorando','gritando']
S(35,d)
d=L(37)
d['nouns'][2]['word']='las gafas de nieve'
S(37,d)
d=L(40)
d['answer']=['Levanta','una','carta.']
d['recall'][3]['parts'][1]['text']='una carta'
d['recall'][3]['parts'][0]['accept']=['Levanta','Enseña','Muestra']
S(40,d)
