import json
p='content/218.json';d=json.load(open(p))
for k in d['taps'][0]['keys']:
    if k['t']==5.0: k['x']=0.19; k['w']=0.81
d['answer']=["A","woman","is","declaring","something","to","the","crowd."]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
