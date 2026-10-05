import json
times=[i*0.5 for i in range(21)]
R={0.0:(0,.37,.86,.64),0.5:(0,.42,.90,.66),1.0:(0,.42,.84,.76),1.5:(.19,.36,.68,.76),2.0:(.02,.38,.62,.78),2.5:(.25,.36,1,.80),3.0:(.27,.18,1,.77),3.5:(.24,.22,1,.84),
4.0:(.22,.22,1,.88),4.5:(.26,.19,1,.90),5.0:(.19,.45,1,1),5.5:(.27,.43,1,.69),6.0:(.29,.44,1,.79),6.5:(.38,.40,1,.81),7.0:(.38,.38,1,.95),7.5:(.38,.38,1,.88),
8.0:(.36,.38,1,.69),8.5:(.30,.43,1,.63),9.0:(.53,.52,1,.69),9.5:(.47,.52,.67,.69)}
B={0.0:(.60,0,1,.36),0.5:(0,0,1,.41),1.0:(0,0,.68,.41),1.5:(0,0,.18,.48)}
def keys(d):
    out=[]
    for t in times:
        if t in d:
            a,b,c,e=d[t]; out.append({"t":t,"x":a,"y":b,"w":round(c-a,2),"h":round(e-b,2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":600,"level":"A","keyWord":"rat","defaultVoice":"female",
"taps":[
 {"phrase":"to stand on two legs","target":"the rat","voice":"female","keys":keys(R)},
 {"phrase":"to pull a pizza slice","target":"the rat","voice":"female","keys":keys(R)},
 {"phrase":"to have big black wheels","target":"the bike","voice":"female","keys":keys(B)}],
"stillS":6.5,
"nouns":[{"word":"a rat","x":.60,"y":.52,"voice":"female"},{"word":"pizza","x":.20,"y":.61,"voice":"female"},{"word":"stairs","x":.80,"y":.34,"voice":"female"},{"word":"a window","x":.84,"y":.08,"voice":"female"}],
"question":"What is the rat doing?",
"answer":["It","is","pulling","a","pizza","slice."],
"answerVoice":"female",
"notes":"Only one animal; third phrase is a state on the bike (visible 0.0-1.5 only, rat runs under its wheel: boxes split at y .41, the lower wheel arc lies inside the rat's box at 0.5-1.0). 9.0-9.5 only the rat's tail is still visible (box on the tail); 10.0 off. Background stairs/window are slightly blurred."}
json.dump(c,open('content/600.json','w'),indent=1,ensure_ascii=False)
