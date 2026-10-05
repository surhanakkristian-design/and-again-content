import json
times=[i*0.5 for i in range(24)]
def split(t):
    if t<4: return 0.51
    if t<7: return 0.49
    if t<9.5: return 0.51
    return 0.50
wk=[{"t":t,"x":0.03,"y":0.12,"w":round(split(t)-0.03,2),"h":0.86} for t in times]
mk=[{"t":t,"x":split(t),"y":0.06,"w":round(0.97-split(t),2),"h":0.91} for t in times]
c={"mediaId":4215,"level":"A","keyWord":"orange","defaultVoice":"female",
"taps":[
 {"phrase":"to wear an orange top","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to wear orange trousers","target":"the man","voice":"male","keys":mk},
 {"phrase":"to hold a small bag","target":"the woman","voice":"female","keys":wk}],
"stillS":6.0,
"nouns":[{"word":"a shirt","x":0.70,"y":0.28,"voice":"female"},{"word":"a top","x":0.30,"y":0.38,"voice":"female"},
 {"word":"a bag","x":0.16,"y":0.62,"voice":"female"},{"word":"a sofa","x":0.90,"y":0.76,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","a","small","bag."],"answerVoice":"female",
"notes":"Outfits change at 4.0, 7.0 and 9.5 s: the orange top is true 0-6.5 s, the man's orange trousers 0-6.5 s (rust-red after 9.5). In the first shot (0-3.5 s) the woman holds two bags, later one. People stand shoulder to shoulder; boxes split on the line between them, her second bag (first and third shot) reaches a little into the man's box."}
json.dump(c,open('content/4215.json','w'),indent=1,ensure_ascii=False)
