import json
T=[i*0.5 for i in range(23)]
# woman box: (y_top, right edge); bottles: (x, y) to bottom-right corner
wy={0.0:0.0,0.5:0.0,1.0:0.0,1.5:0.0,2.0:0.05,2.5:0.11,3.0:0.15,3.5:0.16,4.0:0.16,4.5:0.16,5.0:0.16,5.5:0.15,6.0:0.15,
6.5:0.16,7.0:0.21,7.5:0.21,8.0:0.21,8.5:0.17,9.0:0.15,9.5:0.09,10.0:0.06,10.5:0.04,11.0:0.05}
bot={0.0:(0.54,0.51),0.5:(0.63,0.50),1.0:(0.60,0.42),1.5:(0.66,0.44),2.0:(0.66,0.56),2.5:(0.72,0.66),3.0:(0.74,0.68),
3.5:(0.82,0.77),4.0:(0.74,0.76),4.5:(0.80,0.76),5.0:(0.74,0.77),5.5:(0.82,0.78),6.0:(0.80,0.78),6.5:(0.79,0.76),
7.0:(0.73,0.70),7.5:(0.73,0.65),8.0:(0.73,0.61),8.5:(0.74,0.63),9.0:(0.78,0.68),9.5:(0.82,0.69)}
def r(v): return round(v,2)
wk=[];bk=[]
for t in T:
    if t in bot:
        bx,by=bot[t]; bk.append(dict(t=t,x=bx,y=by,w=r(1-bx),h=r(1-by)))
        wk.append(dict(t=t,x=0.0,y=wy[t],w=r(bx-0.01),h=r(1-wy[t])))
    else:
        bk.append({"t":t,"off":True}); wk.append(dict(t=t,x=0.0,y=wy[t],w=1.0,h=r(1-wy[t])))
c={"mediaId":5242,"level":"B","keyWord":"elegant","defaultVoice":"female",
"taps":[{"phrase":"to walk through the mist","target":"the woman","voice":"female","keys":wk},
{"phrase":"to crowd the patterned dresser","target":"the perfume bottles","voice":"female","keys":bk},
{"phrase":"to flick her hair back","target":"the woman","voice":"female","keys":wk}],
"stillS":2.5,
"nouns":[{"word":"rooftops","x":0.12,"y":0.22,"voice":"female"},{"word":"a necklace","x":0.42,"y":0.40,"voice":"female"},
{"word":"a robe","x":0.10,"y":0.62,"voice":"female"},{"word":"perfume bottles","x":0.84,"y":0.85,"voice":"female"}],
"question":"What is the woman walking through?","answer":["She","is","walking","through","the","perfume","mist."],"answerVoice":"female",
"notes":"Key word 'elegant' is an adjective, not placed as a noun. The bottles box and the woman box are split vertically, so her outstretched hand/elbow on the right is cut where it reaches over the dresser (0.0-2.0, 6.5-9.5). Bottles off from 10.0 (only a sliver at the right edge). 'dresser' = the painted/patterned chest the bottles stand on."}
json.dump(c,open('content/5242.json','w'),indent=1)
