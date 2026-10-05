import json
p='content/7100.json'; d=json.load(open(p))
d['taps'][1]['phrase']='to gaze at the seal'
d['notes']=d['notes'].split(' VERIFIER:')[0]+" VERIFIER: phrase 2 'to punch the air' replaced (fist only pumped at chest height, not punched upward) by 'to gaze at the seal' (she looks at it 1.7-3.7 s)."
json.dump(d,open(p,'w'),indent=1)
