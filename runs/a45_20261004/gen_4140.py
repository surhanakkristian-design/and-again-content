import json
T=[i*0.5 for i in range(24)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
white={0.0:(0.13,0.21,0.71,0.79),0.5:(0.22,0.26,0.53,0.74),1.0:(0.30,0.24,0.36,0.42),1.5:(0.31,0.42,0.38,0.23),2.0:(0.38,0.56,0.22,0.16),
 4.0:(0.41,0.33,0.18,0.14),4.5:(0.42,0.32,0.18,0.14),5.0:(0.43,0.34,0.18,0.14),5.5:(0.43,0.34,0.18,0.14),
 10.5:(0.26,0.42,0.66,0.58),11.0:(0.14,0.43,0.68,0.57),11.5:(0.26,0.43,0.66,0.57)}
orange={6.0:(0.35,0.36,0.38,0.26),6.5:(0.33,0.37,0.40,0.25),7.0:(0.31,0.38,0.39,0.26),7.5:(0.30,0.37,0.40,0.26),8.0:(0.23,0.36,0.40,0.26)}
moon={t:(0.38,0.07,0.18,0.14) for t in (8.5,9.0,9.5,10.0)}
c={"mediaId":4140,"level":"A","keyWord":"adventure","defaultVoice":"male",
"taps":[
 {"phrase":"to jump into the water","target":"the man in the white shirt","voice":"male","keys":keys(white)},
 {"phrase":"to run down the hill","target":"the man in orange shorts","voice":"male","keys":keys(orange)},
 {"phrase":"to shine in the sky","target":"the moon","voice":"male","keys":keys(moon)}],
"stillS":9.0,
"nouns":[{"word":"a mountain","x":0.35,"y":0.27,"voice":"male"},{"word":"friends","x":0.48,"y":0.56,"voice":"male"},
 {"word":"a bridge","x":0.40,"y":0.67,"voice":"male"},{"word":"a river","x":0.50,"y":0.86,"voice":"male"}],
"question":"Where are the three friends sitting?",
"answer":["They","are","sitting","on","a","bridge","over","a","river."],
"answerVoice":"male",
"notes":"Key word 'adventure' is abstract, not used as a noun. White-shirt man: jump shot 0-2.0, hidden under the splash 2.5-3.5 (off), small head in the water 4.0-5.5 (shirt not recognisable there), and the selfie man of the last shot is assumed to be the same man (white shirt). Moon is tiny (minimum box). 'friends' pill and 'a bridge' pill are 0.11 apart in y."}
json.dump(c,open("content/4140.json","w"),indent=1)
