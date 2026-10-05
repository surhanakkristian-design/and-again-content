import json
T=[i*0.5 for i in range(19)]
def K(rows):
    return [{"t":t,"off":True} if r is None else dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
w=[None,(.13,.34,.52,.66),(.07,.28,.93,.72),(.3,.28,.7,.72),(.35,.28,.65,.72),(.24,.27,.76,.73),
 (.2,.33,.55,.48),(.21,.33,.57,.48),(.25,.3,.56,.45),(.37,.34,.32,.38),(.36,.34,.33,.38),(.35,.34,.32,.38),
 (.5,.32,.33,.44),(0,.3,1,.6),(0,.31,.97,.62),(0,.31,.97,.62),(0,.31,.95,.6),(0,.31,.95,.6),(0,.31,.95,.6)]
d={"mediaId":5109,"level":"A","keyWord":"sweet","defaultVoice":"female",
"taps":[
 {"phrase":"to carry a tray","target":"the woman","voice":"female","keys":K(w)},
 {"phrase":"to knock on the door","target":"the woman","voice":"female","keys":K(w)},
 {"phrase":"to take a cupcake","target":"the woman","voice":"female","keys":K(w)}],
"stillS":3.5,
"nouns":[{"word":"a door","x":0.55,"y":0.26,"voice":"female"},
 {"word":"a plant","x":0.14,"y":0.62,"voice":"female"},
 {"word":"cupcakes","x":0.48,"y":0.74,"voice":"female"},
 {"word":"a table","x":0.50,"y":0.92,"voice":"female"}],
"question":"What is the woman carrying?",
"answer":["She","is","carrying","a","tray","of","cupcakes."],
"answerVoice":"female",
"notes":"Only one person, so all three phrases target the woman. 0.0: she is only a blur behind the frosted glass door -> off. 1.5-2.5 her box includes the arm holding the tray. Key word 'sweet' is an adjective, not used as a noun; not in the answer."}
json.dump(d,open("content/5109.json","w"),indent=1)
