import json
def r(v): return round(v+1e-9,2)
def box(t,x0,y0,x1,y1): return {"t":t,"x":r(x0),"y":r(y0),"w":r(x1-x0),"h":r(y1-y0)}
def T(n): return [i*0.5 for i in range(n)]
def dump(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),ensure_ascii=False,indent=1)

# 4211
hb={0.0:(.07,.09,.93,.92),0.5:(.07,.09,.93,.92),1.0:(.07,.09,.93,.92),1.5:(.07,.09,.93,.92),
2.0:(.02,.05,.96,.88),2.5:(.02,.05,.96,.88),3.0:(.02,.05,.96,.88),3.5:(.08,.07,.96,.87),
4.0:(.06,.06,.98,.87),4.5:(.06,.06,.98,.87),5.0:(.06,.08,.98,.90),5.5:(.12,.16,1.0,.98),
6.0:(.06,.11,.98,.89),6.5:(.10,.07,1.0,.87),7.0:(.02,.13,.91,.93),7.5:(.06,.09,.94,.92),
8.0:(.08,.08,.96,.88),8.5:(.08,.08,.96,.88),9.0:(0,.08,1.0,.92),9.5:(0,.08,1.0,.92),
10.0:(0,.08,1.0,.92),10.5:(.02,.09,.98,.88),11.0:(.02,.10,.98,.92),11.5:(.02,.07,.98,.92)}
k=[box(t,*hb[t]) for t in T(24)]
dump({"mediaId":4211,"level":"A","keyWord":"cheek","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the hamster","voice":"male","keys":k} for p in
 ["to drink through a straw","to wash its face","to touch its cheeks"]],
"stillS":10.5,
"nouns":[{"word":"a bow","x":.50,"y":.20,"voice":"male"},{"word":"a cheek","x":.80,"y":.47,"voice":"male"},
 {"word":"a box","x":.40,"y":.86,"voice":"male"}],
"question":"What is the hamster doing?",
"answer":["It","is","washing","its","face."],"answerVoice":"male",
"notes":"Only one possible target (the hamster), used for all three phrases; its box is almost the whole picture. 'a cheek' sits on the right cheek (there are two cheeks, no other noun is on the left one). The answer names the main action of the clip, not the key word; the key word is in phrase 3 and the nouns."})

# 4212
sp={0.0:.50,0.5:.50,1.0:.50,1.5:.50,2.0:.50,2.5:.50,3.0:.44,3.5:.46,4.0:.47,4.5:.47,5.0:.47,
5.5:.47,6.0:.47,6.5:.47,7.0:.47,7.5:.47,8.0:.50,8.5:.50,9.0:.50,9.5:.50,10.0:.49,10.5:.49,11.0:.48,11.5:.48,12.0:.48}
wl={t:(.0 if 8.0<=t<=9.5 else .05) for t in sp}
mr={t:(1.0 if 8.0<=t<=9.5 else .96) for t in sp}
kw=[box(t,wl[t],.12,sp[t],.98) for t in T(25)]
km=[box(t,sp[t],.06,mr[t],.98) for t in T(25)]
dump({"mediaId":4212,"level":"A","keyWord":"brown","defaultVoice":"female",
"taps":[{"phrase":"to carry a small bag","target":"the woman","voice":"female","keys":kw},
 {"phrase":"to wear high heels","target":"the woman","voice":"female","keys":kw},
 {"phrase":"to fix his sleeve","target":"the man","voice":"male","keys":km}],
"stillS":6.0,
"nouns":[{"word":"a woman","x":.30,"y":.30,"voice":"female"},{"word":"a man","x":.66,"y":.22,"voice":"male"},
 {"word":"a bag","x":.15,"y":.64,"voice":"female"},{"word":"a sofa","x":.86,"y":.72,"voice":"female"}],
"question":"What is the woman carrying?",
"answer":["She","is","carrying","a","small","bag."],"answerVoice":"female",
"notes":"'to fix his sleeve' is only seen in 0.0-2.5 s (he pulls at his rolled sleeve). 'to wear high heels' is a state; the woman also has a hand in her pocket in some looks, so pocket phrases were avoided. The two stand close; boxes are split along the line between them (heads touch at 3.5-5.0 s). Key word 'brown' is an adjective, not used as a noun."})

# 4213  P = ponytail, W = curly hair
kP=[];kW=[]
s1={0.0:.43,0.5:.43,1.0:.46,1.5:.46,2.0:.49,2.5:.49,3.0:.48}
s2={3.5:.47,4.0:.48,4.5:.48,5.0:.48,5.5:.48,6.0:.48,6.5:.47,7.0:.48,7.5:.47,8.0:.47,8.5:.47,9.0:.48,
 9.5:.46,10.0:.47,10.5:.47,11.0:.48,11.5:.47}
for t in T(24):
    if t<=3.0:
        kP.append(box(t,.01,.10,s1[t],.94)); kW.append(box(t,s1[t],.05,1.0,1.0))
    else:
        kW.append(box(t,.05,.07,s2[t],.98)); kP.append(box(t,s2[t],.07,(1.0 if t>=9.5 else .95),.98))
dump({"mediaId":4213,"level":"A","keyWord":"red","defaultVoice":"female",
"taps":[{"phrase":"to point at her friend","target":"the woman with curly hair","voice":"female","keys":kW},
 {"phrase":"to touch her friend's shoulder","target":"the woman with curly hair","voice":"female","keys":kW},
 {"phrase":"to wear a green necklace","target":"the woman with a ponytail","voice":"female","keys":kP}],
"stillS":10.5,
"nouns":[{"word":"a necklace","x":.66,"y":.25,"voice":"female"},{"word":"a dress","x":.28,"y":.42,"voice":"female"},
 {"word":"a bag","x":.50,"y":.58,"voice":"female"},{"word":"a wall","x":.25,"y":.07,"voice":"female"}],
"question":"What are the two women wearing?",
"answer":["They","are","wearing","long","dresses."],"answerVoice":"female",
"notes":"The women swap sides at 3.5 s (curly hair right in 0.0-3.0, left afterwards); boxes follow. Pointing (open hand towards the friend) is 0.0-3.0 s and the hand reaches into the other woman's box; the hand on the shoulder (10.0-11.5 s) also lies in the other box. The green necklace is only in the last look (9.5 s on). 'a dress' sits on the left dress (two dresses, no other noun on the right one). Key word 'red' is not a visible noun; the answer stays true for all looks, so it has no colour."})

# 4214
sp={0.0:.51,0.5:.52,1.0:.53,1.5:.53,2.0:.53,2.5:.53,3.0:.53,3.5:.51,4.0:.52,4.5:.53,5.0:.52,5.5:.53,6.0:.53,
6.5:.53,7.0:.54,7.5:.54,8.0:.54,8.5:.53,9.0:.53,9.5:.53,10.0:.53,10.5:.53,11.0:.53,11.5:.53}
def wl(t): return .14 if t<=3.0 else (.09 if t<=6.0 else (.07 if t<=8.5 else .13))
kw=[box(t,wl(t),.12,sp[t],.98) for t in T(24)]
km=[box(t,sp[t],.07,.84,.98) for t in T(24)]
kt=[box(t,.84,.14,1.0,.86) for t in T(24)]
dump({"mediaId":4214,"level":"A","keyWord":"blue","defaultVoice":"female",
"taps":[{"phrase":"to hold a small bag","target":"the woman","voice":"female","keys":kw},
 {"phrase":"to have short black hair","target":"the man","voice":"male","keys":km},
 {"phrase":"to grow in a pot","target":"the tree","voice":"female","keys":kt}],
"stillS":2.0,
"nouns":[{"word":"a woman","x":.32,"y":.33,"voice":"female"},{"word":"a man","x":.64,"y":.15,"voice":"male"},
 {"word":"a bag","x":.46,"y":.63,"voice":"female"},{"word":"a tree","x":.87,"y":.25,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","a","small","bag."],"answerVoice":"female",
"notes":"The man's phrase is a state: his only own action (a hand in his pocket all the time) does not fit in 3-5 natural words. The man's elbow reaches a little into the tree box (x 0.84-0.90); the tree box is 0.16 wide so the two do not overlap. Key word 'blue' is not a visible noun; the bag is blue only in the first two looks, so the answer has no colour."})
