import json
times=[i*0.5 for i in range(24)]
def p(t):
    # split, woman x, woman y
    if t<5: return 0.45,0.05,0.15
    if t<6: return 0.50,0.04,0.14
    if t<8.5: return 0.48,0.04,0.12
    return 0.47,0.13,0.12
wk=[];mk=[]
for t in times:
    s,x,y=p(t)
    wk.append({"t":t,"x":x,"y":y,"w":round(s-x,2),"h":round(0.98-y,2)})
    mk.append({"t":t,"x":s,"y":0.05,"w":round(0.95-s,2),"h":0.93})
c={"mediaId":4216,"level":"A","keyWord":"white","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a white dress","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to wear a black shirt","target":"the man","voice":"male","keys":mk},
 {"phrase":"to wear high heels","target":"the woman","voice":"female","keys":wk}],
"stillS":7.0,
"nouns":[{"word":"a dress","x":0.28,"y":0.50,"voice":"female"},{"word":"a shirt","x":0.70,"y":0.32,"voice":"female"},
 {"word":"trousers","x":0.64,"y":0.62,"voice":"female"},{"word":"a sofa","x":0.90,"y":0.76,"voice":"female"}],
"question":"What is the woman wearing?",
"answer":["She","is","wearing","a","white","dress."],"answerVoice":"female",
"notes":"Outfits change at 5.0 and 8.5 s: the white dress is only 5.0-8.0 s (red before, black after), the man's black shirt only 0-4.5 s; her heels are visible from 5.0 s (hidden under the red gown before). Question/answer describe the middle look (the still is 7.0 s). The two stand close and overlap a little (his arm behind her / around her waist); boxes split on the line between them."}
json.dump(c,open('content/4216.json','w'),indent=1,ensure_ascii=False)
