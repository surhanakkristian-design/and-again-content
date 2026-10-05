import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
wo={0.0:(0,0.25,0.64,0.28),0.5:(0,0.2,0.86,0.47),1.0:(0,0,1,0.76),1.5:(0,0,1,0.74),2.0:(0,0.25,0.18,0.20)}
un={2.5:(0.27,0,0.42,0.48),3.0:(0.31,0,0.35,0.60),3.5:(0.29,0,0.32,0.60),4.0:(0.33,0.03,0.31,0.44),4.5:(0.38,0.03,0.31,0.45)}
hh={5.0:(0.55,0.40,0.45,0.60),5.5:(0.58,0.38,0.42,0.62),6.0:(0.59,0.36,0.41,0.64),6.5:(0.66,0.35,0.34,0.65),7.0:(0.61,0.35,0.39,0.65)}
c={"mediaId":4540,"level":"B","keyWord":"equipment","defaultVoice":"female",
"taps":[
 {"phrase":"to scrub a kitchen worktop","target":"the woman","voice":"female","keys":keys(wo)},
 {"phrase":"to mop the office floor","target":"the man in uniform","voice":"male","keys":keys(un)},
 {"phrase":"to clean a skyscraper window","target":"the man in the hard hat","voice":"male","keys":keys(hh)}],
"stillS":5.5,
"nouns":[{"word":"a hard hat","x":0.86,"y":0.48,"voice":"female"},{"word":"a squeegee","x":0.56,"y":0.58,"voice":"female"},
 {"word":"a harness","x":0.88,"y":0.73,"voice":"female"},{"word":"a rope","x":0.90,"y":0.22,"voice":"female"}],
"question":"What is the man outside doing?",
"answer":["He","is","cleaning","a","skyscraper","window","with","a","squeegee."],
"answerVoice":"male",
"notes":"Four shots, four cleaners; defaultVoice from evenId (mixed group). Key word 'equipment' is a mass noun for all the kit, not one thing at one place, so it is not a noun slot; the nouns are pieces of equipment in the window shot. The man in the grey T-shirt (7.5-10.0 s) is not a target; he also pushes a mop at 7.5-8.0 s, which is why phrase 2 says 'the office floor'. Woman at 0.0 s and 2.0 s: only her gloved hands are in the picture."}
json.dump(c,open("content/4540.json","w"),indent=1)
