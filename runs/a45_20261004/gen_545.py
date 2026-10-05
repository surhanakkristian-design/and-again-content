import json
T=[i*0.5 for i in range(21)]
# jugglers extents (x0,x1,y0,y1), dog (x0,x1,y0,y1), denim woman box or None
J=[(.25,.82,.28,.52),(.27,.83,.30,.53),(.28,.82,.31,.56),(.29,.83,.34,.58),(.29,.83,.37,.61),(.29,.82,.38,.62),(.27,.82,.37,.60),(.27,.82,.35,.59),(.27,.80,.34,.57),(.27,.80,.34,.57),(.32,.70,.36,.59),(.33,.70,.30,.60),(.30,.72,.40,.60),(.28,.72,.42,.60),(.25,.72,.42,.60),(.27,.72,.41,.59),(.33,.68,.30,.57),(.33,.70,.30,.58),(.37,.72,.32,.57),(.42,.74,.33,.57),(.42,.70,.38,.56)]
D=[(.85,.93,.41,.48),(.85,.94,.42,.49),(.85,.93,.44,.51),(.85,.93,.45,.53),(.85,.93,.47,.52),(.84,.92,.47,.52),(.84,.92,.45,.53),(.83,.91,.44,.52),(.83,.91,.45,.52),(.82,.90,.45,.52),(.81,.90,.45,.53),(.80,.89,.45,.53),(.80,.89,.45,.52),(.79,.88,.44,.51),(.80,.89,.43,.51),(.79,.89,.42,.50),(.80,.90,.41,.49),(.81,.91,.43,.50),(.82,.91,.44,.52),(.82,.92,.45,.52),(.80,.90,.44,.52)]
W=[(0,.35,.21,.52),(0,.36,.22,.50),(0,.48,.23,.50),(0,.40,.23,.55),(0,.43,.24,.52),(0,.44,.22,.53),(0,.43,.22,.55),(0,.43,.23,.55),(0,.42,.23,.55),(0,.43,.23,.55),(0,.44,.20,.55),(0,.44,.22,.56),(0,.43,.22,.55),(0,.42,.23,.55)]+[None]*7
r=lambda v:round(v,2)
kj=[];kd=[];kw=[]
for i,t in enumerate(T):
    jx0,jx1,jy0,jy1=J[i];dx0,dx1,dy0,dy1=D[i];w=W[i]
    left=jx0-.03
    if w: left=max(left,w[0]+w[2]+.01)
    right=min(jx1+.03,dx0-.03)
    kj.append({"t":t,"x":r(left),"y":r(jy0-.03),"w":r(right-left),"h":r(jy1-jy0+.06)})
    x0=right+.01; x1=min(1,x0+.18); cy=(dy0+dy1)/2
    kd.append({"t":t,"x":r(x0),"y":r(cy-.075),"w":r(x1-x0),"h":.15})
    kw.append({"t":t,"off":True} if w is None else {"t":t,"x":w[0],"y":w[1],"w":w[2],"h":w[3]})
d={"mediaId":545,"level":"B","keyWord":"performance","defaultVoice":"male",
"taps":[{"phrase":"to juggle colourful clubs","target":"the jugglers","voice":"male","keys":kj},
{"phrase":"to sit beside the spectators","target":"the dog","voice":"male","keys":kd},
{"phrase":"to wear a denim jacket","target":"the woman in the jacket","voice":"female","keys":kw}],
"stillS":8.5,
"nouns":[{"word":"spectators","x":.2,"y":.34,"voice":"male"},{"word":"jugglers","x":.52,"y":.44,"voice":"male"},{"word":"a hat","x":.52,"y":.68,"voice":"male"},{"word":"cobblestones","x":.5,"y":.86,"voice":"male"}],
"question":"What are the jugglers doing?","answer":["They","are","juggling","clubs","in","a","street","performance."],"answerVoice":"male",
"notes":"VERIFIER: target 'the jugglers' is the pair (man + woman) in one box: they do exactly the same all the time (juggle, pick up, bow), so no action phrase fits only one of them; a tap on either should count. If a pair is not allowed, change it. The woman in the denim jacket (front left) only has a state phrase and leaves the picture at 7.0 s (off from then). Her box is cut on the right at 0-0.5 s (her shoe) so it does not overlap the jugglers. Dog box is small and close to the jugglers. Key word 'performance' is abstract: used in the answer, not as a noun. 'spectators' labels the crowd on the left; the crowd also stands behind the jugglers."}
json.dump(d,open("content/545.json","w"),indent=1,ensure_ascii=False)
