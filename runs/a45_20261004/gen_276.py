import json
def K(times, d):
    out=[]
    for t in times:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
def T(n): return [i*0.5 for i in range(n)]
def dump(o): json.dump(o, open(f"content/{o['mediaId']}.json","w"), indent=1, ensure_ascii=False)

# 276
t=T(21)
sheep={5.5:(0.0,0.35,0.90,0.14),6.0:(0.15,0.20,0.72,0.19),10.0:(0.15,0.22,0.72,0.18)}
fall={6.5:(0.30,0.25,0.32,0.27),7.0:(0.33,0.33,0.32,0.26),7.5:(0.38,0.15,0.36,0.47),8.0:(0.46,0.11,0.40,0.40),
      8.5:(0.44,0.04,0.40,0.42),9.0:(0.42,0.08,0.40,0.47),9.5:(0.44,0.04,0.40,0.50)}
phone={8.5:(0.32,0.63,0.30,0.30),9.0:(0.31,0.64,0.29,0.30),9.5:(0.28,0.68,0.31,0.30)}
dump({"mediaId":276,"level":"B","keyWord":"excursion","defaultVoice":"female",
 "taps":[{"phrase":"to graze on a hillside","target":"the sheep","voice":"female","keys":K(t,sheep)},
         {"phrase":"to plunge over a cliff","target":"the waterfall","voice":"female","keys":K(t,fall)},
         {"phrase":"to rest on a boulder","target":"the phone","voice":"female","keys":K(t,phone)}],
 "stillS":9.0,
 "nouns":[{"word":"a waterfall","x":0.60,"y":0.25,"voice":"female"},{"word":"a rainbow","x":0.25,"y":0.43,"voice":"female"},
          {"word":"a phone","x":0.45,"y":0.80,"voice":"female"},{"word":"a boulder","x":0.30,"y":0.93,"voice":"female"}],
 "question":"What are the friends doing?",
 "answer":["They","are","posing","in front of","a","waterfall."],"answerVoice":"female",
 "notes":"Clip has many cuts and five similar hikers (two women with braids, three bearded men), so no person is used as a tap target; targets are the sheep (5.5, 6.0, 10.0), the waterfall (6.5-9.5) and the phone (8.5-9.5). Nothing tappable before 5.5 s. The phone is touched by the kneeling man at 8.5/9.0 while it stands on the rock. Key word 'excursion' is abstract, not a noun slot. Rainbow is faint."})

# 279
t=T(11)
man={0.0:(0.12,0.28,0.30,0.47),0.5:(0.12,0.29,0.28,0.46),1.0:(0.0,0.0,1.0,0.82),1.5:(0.0,0.12,0.86,0.74),
     2.0:(0.0,0.28,0.50,0.36),2.5:(0.0,0.0,0.68,0.88),3.0:(0.0,0.24,0.40,0.74),3.5:(0.0,0.24,0.60,0.64),
     4.0:(0.0,0.52,1.0,0.36),4.5:(0.0,0.04,0.70,0.84),5.0:(0.0,0.23,0.68,0.73)}
cart={0.0:(0.42,0.08,0.58,0.80),0.5:(0.40,0.06,0.60,0.82),1.5:(0.10,0.86,0.90,0.14),2.0:(0.50,0.0,0.50,0.92),
      2.5:(0.68,0.0,0.32,0.97),3.0:(0.40,0.03,0.60,0.97),3.5:(0.60,0.12,0.40,0.76),4.0:(0.45,0.12,0.55,0.40),
      4.5:(0.70,0.12,0.30,0.33),5.0:(0.68,0.12,0.32,0.50)}
dump({"mediaId":279,"level":"B","keyWord":"exert","defaultVoice":"male",
 "taps":[{"phrase":"to exert all his strength","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to clench his fist","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to roll through a puddle","target":"the cart","voice":"male","keys":K(t,cart)}],
 "stillS":0.5,
 "nouns":[{"word":"sacks","x":0.75,"y":0.17,"voice":"male"},{"word":"a wheel","x":0.57,"y":0.60,"voice":"male"},
          {"word":"a puddle","x":0.35,"y":0.88,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","exerting","all","his","strength."],"answerVoice":"male",
 "notes":"Man and cart overlap in most shots; boxes are split along a vertical (or at 4.0 horizontal) line, so the man's far arm/hand on the handle sometimes lies in the cart box (3.5, 4.5, 5.0). 1.0 s shows only his legs (cart off). 1.5: cart = only the handle strip at the bottom. Only 3 nouns: 'a cart' left out because it could label the wheel's place."})

# 280
t=T(13)
kit={x:(0.0,0.05,1.0,0.73) for x in T(8)}
kit[4.0]=(0.0,0.02,0.80,0.77); kit[4.5]=(0.0,0.0,1.0,0.78)
for x in (5.0,5.5,6.0): kit[x]=(0.0,0.0,1.0,1.0)
dump({"mediaId":280,"level":"A","keyWord":"kitten","defaultVoice":"female",
 "taps":[{"phrase":"to look at the camera","target":"the kitten","voice":"female","keys":K(t,kit)},
         {"phrase":"to sit on a bed","target":"the kitten","voice":"female","keys":K(t,kit)},
         {"phrase":"to come very close","target":"the kitten","voice":"female","keys":K(t,kit)}],
 "stillS":0.5,
 "nouns":[{"word":"a kitten","x":0.50,"y":0.24,"voice":"female"},{"word":"a nose","x":0.50,"y":0.59,"voice":"female"},
          {"word":"a phone","x":0.65,"y":0.88,"voice":"female"}],
 "question":"What is the kitten doing?",
 "answer":["It","is","looking","at","the","camera."],"answerVoice":"female",
 "notes":"Only one possible target (the kitten) for all three phrases. 'a kitten' pill sits on the forehead, 'a nose' on the nose of the same (large) animal: check that this is acceptable. From 4.5 s the picture is a blurry extreme close-up."})

# 281
t=T(21)
full=(0.0,0.10,1.0,0.90)
wom={x:full for x in T(10)}
wom.update({5.0:(0.0,0.30,1.0,0.70),5.5:(0.72,0.20,0.28,0.75),6.0:(0.66,0.19,0.34,0.56),6.5:(0.55,0.0,0.45,0.65),
 7.0:(0.0,0.0,1.0,1.0),7.5:(0.0,0.0,1.0,1.0),8.0:(0.0,0.0,1.0,1.0),8.5:(0.0,0.0,1.0,1.0),
 9.0:(0.60,0.28,0.40,0.72),9.5:(0.61,0.30,0.39,0.70),10.0:(0.63,0.28,0.37,0.62)})
fr={5.0:(0.48,0.16,0.32,0.14),5.5:(0.30,0.17,0.42,0.56),6.0:(0.33,0.08,0.33,0.43),6.5:(0.31,0.0,0.24,0.42),
 9.0:(0.44,0.14,0.16,0.46),9.5:(0.45,0.15,0.16,0.50),10.0:(0.46,0.16,0.17,0.50)}
dump({"mediaId":281,"level":"B","keyWord":"eyeliner","defaultVoice":"female",
 "taps":[{"phrase":"to apply winged eyeliner","target":"the dark-haired woman","voice":"female","keys":K(t,wom)},
         {"phrase":"to hold a cotton swab","target":"the dark-haired woman","voice":"female","keys":K(t,wom)},
         {"phrase":"to give a thumbs up","target":"the blonde friend","voice":"female","keys":K(t,fr)}],
 "stillS":0.0,
 "nouns":[{"word":"light bulbs","x":0.50,"y":0.06,"voice":"female"},{"word":"a mirror","x":0.45,"y":0.19,"voice":"female"},
          {"word":"eyeliner","x":0.70,"y":0.52,"voice":"female"},{"word":"a cotton swab","x":0.80,"y":0.87,"voice":"female"}],
 "question":"What is the dark-haired woman doing?",
 "answer":["She","is","applying","winged","eyeliner."],"answerVoice":"female",
 "notes":"The woman is seen twice (herself on the left and her reflection). While the friend is not identifiable the woman's box covers both; when the friend is visible in the mirror (5.0-6.5, 9.0-10.0) the woman's box is only her REFLECTION (right), because the friend stands between the two - a tap on the real woman at the left edge misses in those frames. Friend is set off where only a strip of blonde hair shows behind the reflection (0-4.5, 7.0-8.5). At 9.0-10.0 the friend's box holds the thumb and shirt, not the strip of blonde hair above the reflection. Friend's gender assumed female (short blonde hair). 'eyeliner' pill is on the eyeliner pen."})
