import json
p='content/es/5626.json'; d=json.load(open(p))
d['taps'][0]['phrase']='estar arrodillado en la acera'
d['taps'][1]['phrase']='estar sentado entre las naranjas'
d['recall'][0]['parts']=[{"text":"estar"},{"text":"arrodillado","gap":True,"accept":["arrodillado"]},{"text":"en la acera"}]
d['recall'][1]['parts']=[{"text":"estar sentado entre las"},{"text":"naranjas","gap":True,"accept":["naranjas"]}]
d['notes']+=" Verifier: taps 1-2 changed from 'arrodillarse'/'sentarse' (the act of kneeling/sitting down) to the state the clip shows ('estar arrodillado', 'estar sentado'), matching 'sentado' in the answer."
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
