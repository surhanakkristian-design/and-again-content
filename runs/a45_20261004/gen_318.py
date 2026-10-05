import json
T=[i*0.5 for i in range(23)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
P={0.0:(0,.24,.50,.62),0.5:(0,.24,.50,.62),1.0:(0,.24,.50,.64),1.5:(0,.20,.44,.68)}
G={0.5:(.78,0,.22,.84),1.0:(.52,0,.48,.90),1.5:(.44,.12,.56,.76)}
D={0.0:(.50,.83,.36,.14),0.5:(.50,.84,.38,.14),1.0:(.48,.90,.42,.10),1.5:(.50,.88,.42,.12)}
for t in (2.0,2.5,3.0,3.5,4.0,4.5):
    P[t]=(0,.17,.42,.69); G[t]=(.42,.08,.58,.80); D[t]=(.50,.88,.42,.12)
P[5.0]=(0,.20,.44,.66); G[5.0]=(.44,.14,.56,.74); D[5.0]=(.50,.88,.42,.12)
for t,s in ((5.5,.76),(6.0,.70),(6.5,.76),(7.0,.68),(7.5,.76)):
    P[t]=(0,0,s,1.0); G[t]=(s,0,round(1-s,2),1.0)
P[8.0]=(0,.16,.50,.74); G[8.0]=(.50,0,.50,1.0)
P[8.5]=(0,.16,.54,.76); G[8.5]=(.54,.08,.46,.92)
P[9.0]=(0,.18,.50,.82); G[9.0]=(.50,.18,.50,.82)
P[9.5]=(0,.22,.48,.76); G[9.5]=(.48,.06,.52,.94)
P[10.0]=(.18,.30,.29,.47); G[10.0]=(.47,.25,.30,.52)
P[10.5]=(.22,.33,.25,.40); G[10.5]=(.47,.28,.22,.45)
P[11.0]=(.29,.37,.20,.44); G[11.0]=(.49,.31,.19,.50)
c={"mediaId":318,"level":"A","keyWord":"friendship","defaultVoice":"female",
"taps":[
{"phrase":"to look very sad","target":"the girl in purple","voice":"female","keys":keys(P)},
{"phrase":"to share her ice cream","target":"the girl in green","voice":"female","keys":keys(G)},
{"phrase":"to lie on the ground","target":"the dropped ice cream","voice":"female","keys":keys(D)}],
"stillS":0.0,
"nouns":[{"word":"a girl","x":.22,"y":.42,"voice":"female"},{"word":"the sky","x":.60,"y":.15,"voice":"female"},
{"word":"the sea","x":.72,"y":.53,"voice":"female"},{"word":"an ice cream","x":.66,"y":.90,"voice":"female"}],
"question":"What is the girl in green doing?",
"answer":["She","is","sharing","her","ice","cream","with","her","friend."],
"answerVoice":"female",
"notes":"Cartoon. The bald friend in the green jacket is called 'her friend' (she) in the description; named 'the girl in green'. Key word 'friendship' is abstract: not a noun slot; the answer uses 'friend'. The two girls sit shoulder to shoulder 1.5-9.5 s, boxes split along the line between them (close-ups 5.5-7.5 s split at x 0.68-0.76; the friend's hand on the purple shoulder falls in the purple box). 'to look very sad' is a state true 0-6 s (she smiles from 6.5 s). The dropped ice cream: box is only 0.10-0.12 high at 1.0-5.0 s because the friend's boots stand right above it; OFF from 5.5 s (close-up, then mostly hidden behind the boots 8.0-9.5 s). A stray flying ice cream appears at 10.5 s (generation glitch), ignored."}
json.dump(c,open("content/318.json","w"),indent=1,ensure_ascii=False)
