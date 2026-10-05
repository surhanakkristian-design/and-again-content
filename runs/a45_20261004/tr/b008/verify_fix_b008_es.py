import json, os
H = os.path.dirname(os.path.abspath(__file__)); p = f'{H}/es.json'
t = json.load(open(p)); s = json.load(open(f'{H}/source.json'))
F = [('632','phrases',2,'estar fuera de la ventana','estar fuera, delante de la ventana'),
     ('634','answer',None,'Está vertiendo arena en su mano.','Está vertiendo arena en la mano.'),
     ('642','phrases',0,'señalar su antebrazo','señalarse el antebrazo'),
     ('687','phrases',0,'montar en un monopatín','montar en monopatín'),
     ('687','answer',None,'Está montando en un monopatín.','Está montando en monopatín.'),
     ('695','phrases',0,'apoyarse en su mano','apoyarse en la mano')]
for i,f,k,a,b in F:
    if k is None: assert t[i][f]==a, (i,t[i][f]); t[i][f]=b
    else: assert t[i][f][k]==a, (i,t[i][f][k]); t[i][f][k]=b
json.dump(t, open(p,'w'), ensure_ascii=False, indent=1)
print(sum(5+len(v['nouns']) for v in s.values()))
