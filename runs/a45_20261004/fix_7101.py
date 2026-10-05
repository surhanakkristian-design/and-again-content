import json
p='content/7101.json'; d=json.load(open(p))
d['taps'][2]['phrase']='to laugh with joy'
d['notes']+=" VERIFIER: phrase 3 'to sit on a scooter' replaced by 'to laugh with joy' (riders on scooters wait in the traffic line behind, so it did not fit only her)."
json.dump(d,open(p,'w'),indent=1)
