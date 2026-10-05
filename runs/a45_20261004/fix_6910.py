import json
p='content/6910.json'; d=json.load(open(p))
d['taps'][0]['phrase']='to speed away from the apple'
d['answer']=["It","is","speeding","away","from","the","apple."]
json.dump(d,open(p,'w'),indent=1)
