import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W={0.0:(.22,.25,.68,.47),0.5:(.34,.24,.62,.46),1.0:(.38,.32,.58,.45),1.5:(.14,.13,.85,.62),2.0:(0,.02,.96,.76)}
for t in [2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0]: W[t]=(0,0,1,.9)
W.update({7.5:(.30,.03,.70,.82),8.0:(.37,.04,.63,.66),8.5:(.45,.07,.55,.62),9.0:(.52,.10,.48,.62),9.5:(.55,.10,.45,.62),
 10.0:(.56,.10,.44,.60),10.5:(.50,.08,.50,.60),11.0:(.48,.12,.52,.60),11.5:(.38,.15,.62,.72),12.0:(.18,.05,.82,.73)})
G={7.5:(0,.28,.30,.52),8.0:(0,.27,.36,.45),8.5:(0,.28,.36,.45),9.0:(0,.31,.36,.42),9.5:(0,.31,.36,.42),10.0:(0,.29,.37,.42),
 10.5:(0,.29,.33,.42),11.0:(0,.32,.28,.40),11.5:(0,.38,.24,.42),12.0:(0,.56,.17,.25)}
c={"mediaId":5168,"level":"A","keyWord":"batch","defaultVoice":"female",
"taps":[{"phrase":"to bake small cakes","target":"the woman","voice":"female","keys":K(W)},
{"phrase":"to eat a small cake","target":"the girl","voice":"female","keys":K(G)},
{"phrase":"to carry a big tray","target":"the woman","voice":"female","keys":K(W)}],
"stillS":9.0,
"nouns":[{"word":"a girl","x":0.14,"y":0.45,"voice":"female"},{"word":"people","x":0.30,"y":0.24,"voice":"female"},
{"word":"a woman","x":0.74,"y":0.33,"voice":"female"},{"word":"a batch","x":0.55,"y":0.82,"voice":"female"}],
"question":"What is the girl doing?","answer":["She","is","eating","a","small","cake."],"answerVoice":"female",
"notes":"The tarts are Portuguese custard tarts; called 'small cakes' for level A. 'a batch' is placed on the trayful of tarts. 'people' = the crowd behind the girl."}
json.dump(c,open('content/5168.json','w'),indent=1)
