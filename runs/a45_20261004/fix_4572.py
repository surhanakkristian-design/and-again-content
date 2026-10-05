import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
# 4572
c=load(4572)
keys=c['taps'][0]['keys']
new={0.0:(.16,.04,.82,.70),0.5:(.16,.04,.82,.70),1.0:(.16,.04,.82,.70),1.5:(.16,.04,.82,.70),2.0:(.16,.04,.82,.70),
     2.5:(.14,.04,.86,.70),3.0:(.16,.06,.70,.68),3.5:(.18,.06,.68,.68),4.0:(.14,.05,.86,.67),4.5:(.16,.05,.80,.65),
     5.5:(.28,.08,.52,.57),6.0:(.20,.08,.46,.54)}
for k in keys:
    if k['t'] in new: k['x'],k['y'],k['w'],k['h']=new[k['t']]
c['taps'][1]['keys']=json.loads(json.dumps(keys))
c['taps'][2]={"phrase":"to stare in disbelief","target":"the woman","voice":"female","keys":json.loads(json.dumps(keys))}
c['notes']="Verifier: 'to tower above her head' (right pile) replaced - the right pile is only just above her head at the very end and the left pile reads the same; third phrase now 'to stare in disbelief' (the woman, 8-10 s). All three phrases share the woman, so her box now also holds her hands and the sheet (0-4.5 s). She touches her glasses only around 4.5 s."
save(4572,c)
# 4573
c=load(4573)
for k in c['taps'][0]['keys']:
    if k['t']==2.0: k['w']=0.84
c['answer']=["They","are","shaking","hands","across","the","table."]
c['notes']+=" Verifier: answer changed from 'over a wheelbarrow' to 'across the table' (the hands meet above the table, the wheelbarrow stands in front of it); woman's box at 2.0 s widened to the picture edge."
save(4573,c)
# 4575
c=load(4575)
c['taps'][2]['phrase']="to ask for quiet"
c['notes']+=" Verifier: 'to ask for silence' -> 'to ask for quiet' (level A)."
save(4575,c)
# 4576
c=load(4576)
c['taps'][0]['phrase']="to hold up a paper"
c['question']="What is the woman in green doing?"
c['notes']="Verifier: 'to count the papers' replaced by 'to hold up a paper' (8-9 s) because everybody at the table counts papers in the wide shot; 'count' stays in the answer. Question names 'the woman in green' (many women in the hall). Only one target. She is small from 5.5 s (minimum-size box). Both arms go up with a sheet only at 8-9 s. A second (white) chair stands at the right edge at 0 s; the pill is on the nearer pink one."
save(4576,c)
