import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 6920
woman=K([(0.04,0.25,0.65,0.55)]*8); toilet=K([(0.69,0.43,0.19,0.36)]*8)
save({"mediaId":6920,"level":"B","keyWord":"can","defaultVoice":"female",
 "taps":[{"phrase":"to sip coffee from a glass","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to sit barefoot on a toilet","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to stand on a salt flat","target":"the toilet","voice":"female","keys":toilet}],
 "stillS":2.7,
 "nouns":[{"word":"a toilet","x":0.78,"y":0.56,"voice":"female"},
          {"word":"sunglasses","x":0.55,"y":0.32,"voice":"female"},
          {"word":"a satin dress","x":0.30,"y":0.66,"voice":"female"},
          {"word":"a salt flat","x":0.50,"y":0.88,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","sipping","coffee","on","a","toilet."],"answerVoice":"female",
 "notes":"Key word 'can' = slang for toilet; pill says 'a toilet' since 'a can' on a toilet would mislead learners - verifier may prefer 'a can'. Toilet box split from woman at x=.69; toilet base under her dress (x .52-.69) falls in the woman box. Drink is a small glass of dark steaming liquid (coffee per description)."})

# 6922
plough=K([(0.74,0.36,0.26,0.16),(0.73,0.41,0.27,0.15),(0.71,0.45,0.28,0.15),(0.70,0.49,0.27,0.14),(0.69,0.53,0.25,0.14),(0.68,0.57,0.26,0.14),(0.67,0.60,0.23,0.14),(0.66,0.62,0.22,0.14)])
birds=K([None,None,(0.48,0.0,0.24,0.14),(0.29,0.0,0.45,0.15),(0.28,0.0,0.46,0.19),(0.28,0.0,0.46,0.21),(0.28,0.0,0.47,0.25),(0.29,0.05,0.45,0.23)])
glove=K([(0.08,0.58,0.18,0.14),(0.08,0.62,0.18,0.14),(0.08,0.67,0.18,0.14),(0.08,0.71,0.18,0.14),(0.08,0.75,0.18,0.14),(0.08,0.79,0.18,0.14),(0.08,0.83,0.18,0.14),(0.08,0.86,0.18,0.14)])
save({"mediaId":6922,"level":"B","keyWord":"capitol","defaultVoice":"female",
 "taps":[{"phrase":"to clear the snowy road","target":"the snowplough","voice":"female","keys":plough},
         {"phrase":"to swirl above the dome","target":"the birds","voice":"female","keys":birds},
         {"phrase":"to lie in the snow","target":"the glove","voice":"female","keys":glove}],
 "stillS":2.7,
 "nouns":[{"word":"a capitol","x":0.50,"y":0.30,"voice":"female"},
          {"word":"a snowplough","x":0.80,"y":0.655,"voice":"female"},
          {"word":"a handrail","x":0.60,"y":0.76,"voice":"female"},
          {"word":"a glove","x":0.20,"y":0.87,"voice":"female"}],
 "question":"What is the yellow snowplough doing?","answer":["It","is","clearing","the","snowy","road."],"answerVoice":"female",
 "notes":"Camera tilts up so everything drifts down. Birds appear from 1.2 s. 'to lie in the snow' is a plain state (only the glove fits). No main person (group) -> evenId true -> female."})

# 6923
man=K([(0.08,0.15,0.44,0.55),(0.06,0.14,0.48,0.58),(0.05,0.13,0.49,0.62),(0.04,0.12,0.52,0.64),(0.02,0.11,0.54,0.70),(0.01,0.10,0.55,0.73),(0.0,0.09,0.56,0.79),(0.0,0.08,0.55,0.85)])
wom=K([(0.52,0.19,0.30,0.50),(0.54,0.20,0.32,0.49),(0.54,0.17,0.32,0.55),(0.56,0.17,0.33,0.58),(0.56,0.18,0.36,0.58),(0.56,0.16,0.40,0.62),(0.56,0.15,0.44,0.69),(0.55,0.15,0.45,0.75)])
dog=K([(0.67,0.70,0.33,0.21),(0.69,0.73,0.31,0.22),(0.71,0.76,0.29,0.19),(0.73,0.80,0.27,0.20),(0.75,0.84,0.25,0.16),(0.82,0.86,0.18,0.14),None,None])
save({"mediaId":6923,"level":"B","keyWord":"care for","defaultVoice":"female",
 "taps":[{"phrase":"to bandage a scraped knee","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to wince in pain","target":"the man","voice":"male","keys":man},
         {"phrase":"to sniff the wrappers","target":"the dog","voice":"female","keys":dog}],
 "stillS":0.7,
 "nouns":[{"word":"a bandage","x":0.48,"y":0.49,"voice":"female"},
          {"word":"a first-aid kit","x":0.30,"y":0.77,"voice":"female"},
          {"word":"a crate","x":0.75,"y":0.74,"voice":"female"},
          {"word":"a skateboard","x":0.40,"y":0.92,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","bandaging","his","scraped","knee."],"answerVoice":"female",
 "notes":"Man and woman overlap at his knee: split around x .52-.56; her reaching arm falls in the man's box, his shins/shoes fall in hers. Dog only partly visible at 2.2/2.7, gone after. Background skaters ignored."})

# 6924
w=K([(0.16,0.37,0.54,0.40),(0.27,0.38,0.53,0.40),(0.17,0.25,0.72,0.62),(0.13,0.34,0.71,0.63),(0.10,0.34,0.74,0.64),(0.08,0.33,0.72,0.65),(0.10,0.25,0.66,0.73),(0.08,0.25,0.66,0.73)])
m=K([(0.71,0.43,0.23,0.16),(0.80,0.50,0.18,0.14),None,None,(0.84,0.53,0.16,0.14),(0.80,0.49,0.20,0.15),(0.76,0.43,0.24,0.22),(0.74,0.39,0.26,0.26)])
save({"mediaId":6924,"level":"B","keyWord":"career","defaultVoice":"female",
 "taps":[{"phrase":"to career down the hill","target":"the woman","voice":"female","keys":w},
         {"phrase":"to punch the air","target":"the woman","voice":"female","keys":w},
         {"phrase":"to dive into the hay","target":"the marshal","voice":"male","keys":m}],
 "stillS":0.2,
 "nouns":[{"word":"a bathtub","x":0.48,"y":0.56,"voice":"female"},
          {"word":"hay bales","x":0.40,"y":0.88,"voice":"female"},
          {"word":"a church tower","x":0.38,"y":0.15,"voice":"female"},
          {"word":"a balcony","x":0.20,"y":0.27,"voice":"female"}],
 "question":"What is the woman in goggles doing?","answer":["She","is","careering","down","the","cobbled","street."],"answerVoice":"female",
 "notes":"Woman box includes the bathtub cart. Marshal hidden at 1.2/1.7, small at 0.7/2.2 behind tub edge; boxes split from the tub where they touch, so the tub's right rim falls in the marshal box at 3.2/3.7 and her raised right fist falls outside both. 'to punch the air' only from 3.2 s."})
