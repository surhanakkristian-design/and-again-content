import json,copy
p='content/4898.json'; d=json.load(open(p))
dome=d['taps'][2]
d['taps'][1]={"phrase":"to sparkle in the sunlight","target":"the glass dome","voice":dome['voice'],"keys":copy.deepcopy(dome['keys'])}
d['notes']+=" | VERIFIER: 'to wear beige work trousers' did not fit only its target (other gardeners in khaki trousers at 4.5-5.5 s) and no unique gardener action exists -> phrase 2 now on the dome: 'to sparkle in the sunlight' (same keys as the dome)."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
