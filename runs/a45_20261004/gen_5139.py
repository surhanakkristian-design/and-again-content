import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
M={0.0:(.18,.13,.62,.6),0.5:(.1,0.0,.9,.8),1.0:(0.0,0.0,1.0,.97),1.5:(0.0,.06,1.0,.94),2.0:(0.0,0.0,1.0,1.0),2.5:(0.0,0.0,1.0,1.0),
   3.0:(0.0,.52,.5,.22),3.5:(0.0,.52,.42,.21),4.5:(0.0,.48,.7,.5),5.0:(0.0,.53,.26,.16),5.5:(0.0,.12,1.0,.88),6.0:(0.0,.1,1.0,.9),
   6.5:(0.0,0.0,1.0,.8),7.0:(.06,0.0,.94,.85),7.5:(.1,0.0,.9,.85),8.0:(.1,0.0,.9,.95),8.5:(.17,0.0,.72,.88),9.0:(.2,.1,.65,.57)}
c={"mediaId":5139,"level":"A","keyWord":"blank","defaultVoice":"male",
 "taps":[
  {"phrase":"to open his passport","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to close his eyes","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to smile at the camera","target":"the man","voice":"male","keys":keys(M)}],
 "stillS":9.0,
 "nouns":[{"word":"lights","x":.22,"y":.1,"voice":"male"},{"word":"a passport","x":.52,"y":.47,"voice":"male"},
          {"word":"a backpack","x":.88,"y":.56,"voice":"male"},{"word":"a table","x":.5,"y":.84,"voice":"male"}],
 "question":"What is the man holding?","answer":["He","is","holding","a","passport."],"answerVoice":"male",
 "notes":"Only one real target: the young man (the border officer is only a hand at 4.0/5.0 and a blurred woman at the right edge at 5.0, so all three phrases use the man). At 3.0-3.5 and 5.0 only his hand on the passport is visible; 4.0 off (the hand with the watch is the officer's). 'to close his eyes' is true at 1.5-2.5 only. Key word 'blank' is an adjective (blank pages at 0.5-1.0), not used as a noun. Still 9.0: 'lights' = ceiling lamps, 'a table' = the wooden table in front."}
json.dump(c,open('content/5139.json','w'),indent=1)
