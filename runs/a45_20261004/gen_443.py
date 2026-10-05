import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
woman={0.5:(0,.18,.2,1),1.0:(0,.2,.2,1),1.5:(0,.2,.18,1),6.0:(0,.18,.4,1),6.5:(.05,.2,.5,1),7.0:(.05,.3,.52,1),
7.5:(0,.22,.55,1),8.0:(0,.18,.52,1),8.5:(0,.2,.5,1),9.0:(0,.25,.48,1),9.5:(0,.27,.47,1),10.0:(0,.25,.46,1)}
man={0.0:(.58,.15,1,1),0.5:(.52,.12,1,1),1.0:(.55,.18,1,1),1.5:(.62,.08,1,1),2.0:(.58,.12,1,1),
6.5:(.52,.08,1,1),7.0:(.55,.18,1,1),7.5:(.62,.05,1,1),8.0:(.8,0,1,1),8.5:(.78,0,1,1),9.0:(.8,.05,1,1),9.5:(.8,.15,1,1),10.0:(.84,.1,1,1)}
horse={4.5:(0,.42,.52,.84),5.0:(.2,.54,.7,.95),5.5:(.42,.58,.93,1),6.0:(.56,.52,.92,.95),
8.0:(.6,.62,.8,1),8.5:(.6,.62,.78,1),9.0:(.58,.7,.8,1),9.5:(.58,.72,.8,1),10.0:(.6,.6,.84,1)}
c={"mediaId":443,"level":"A","keyWord":"light","defaultVoice":"male",
"taps":[
{"phrase":"to hold a flashlight","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to wear a blue sweater","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to look like a horse","target":"the toy horse","voice":"male","keys":keys(horse)}],
"stillS":10.0,
"nouns":[{"word":"light","x":.52,"y":.33,"voice":"male"},{"word":"a woman","x":.16,"y":.55,"voice":"female"},
{"word":"boxes","x":.38,"y":.80,"voice":"male"},{"word":"a toy horse","x":.72,"y":.72,"voice":"male"}],
"question":"What is coming through the window?",
"answer":["Light","is","coming","through","the","window."],
"answerVoice":"male",
"notes":"First 3 s are almost black: the two people are only dim shapes there (woman at the left edge 0.5-1.5 s, man's blue back on the right 0-2 s). The flashlight in the woman's hand is only clearly seen from 9.0 s. Horse phrase is a state (the toy does nothing itself). Man/horse boxes split at x ~0.8 from 8.0 s. 'light' pill sits on the bright window glass; no 'a window' noun to avoid two labels on one place."}
json.dump(c,open("content/443.json","w"),indent=1,ensure_ascii=False)
