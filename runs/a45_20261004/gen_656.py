import json
P="the chess player"; M="the man behind the rope"; S="the woman behind the rope"
OFF=None
m=(0,.17,.19,.46); s=(.20,.20,.20,.40); p=(.41,.19,.59,.52)
K={
0.0:((0,.04,1,.70),OFF,OFF),
0.5:((0,.04,1,.70),OFF,OFF),
1.0:((0,.04,1,.70),OFF,OFF),
1.5:((.43,.20,.57,.64),(0,.17,.19,.57),(.20,.20,.22,.54)),
2.0:(p,m,s),2.5:(p,m,s),3.0:(p,m,s),3.5:(p,m,s),4.0:(p,m,s),4.5:(p,m,s),5.0:(p,m,s),
5.5:(p,m,s),6.0:(p,m,s),6.5:(p,m,s),7.0:((.41,.19,.59,.54),m,s),7.5:(p,m,s),8.0:(p,m,s),8.5:(p,m,s),
9.0:((.41,.18,.59,.56),m,s),9.5:((.41,.18,.59,.56),m,s),10.0:((.41,.18,.59,.50),m,s),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":656,"level":"B","keyWord":"distract","defaultVoice":"female",
"taps":[
 {"phrase":"to press the chess clock","target":P,"voice":"female","keys":keys(0)},
 {"phrase":"to clasp his hands together","target":M,"voice":"male","keys":keys(1)},
 {"phrase":"to raise both clenched fists","target":S,"voice":"female","keys":keys(2)}],
"stillS":6.0,
"nouns":[{"word":"arched windows","x":.55,"y":.10,"voice":"female"},
 {"word":"a rope","x":.30,"y":.47,"voice":"female"},
 {"word":"a chess clock","x":.17,"y":.66,"voice":"female"},
 {"word":"a chessboard","x":.68,"y":.80,"voice":"female"}],
"question":"What is the chess player doing?",
"answer":["She","is","pressing","the","chess","clock","after","her","move."],
"answerVoice":"female",
"notes":"The two spectators are small and blurred in the background on the left, next to each other (split at x 0.19/0.20). The player's box holds head and body; her outstretched hand (moving a piece 4.0/7.0-7.5 s, on the clock 4.5-5.0/8.5 s) reaches left under the spectators' boxes and is outside her box where it passes x < 0.41. The man gestures with one arm at 1.5-2.5 s and stands with clasped hands from 3.0 s on; the woman behind the rope keeps both fists raised the whole time (at 1.5-2.0 s the man's raised arm could briefly look similar - verifier please check). The spectator in grey with the lanyard is read as a woman. The opponent is only a blurred edge at the left / bottom left, not used. Key word 'distract' is a verb; no phrase uses it because both spectators do it."}
json.dump(d,open("content/656.json","w"),indent=1,ensure_ascii=False)
