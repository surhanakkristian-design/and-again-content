import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
W={0.0:(0,.07,.52,.63),0.5:(0,.07,.52,.63),1.0:(0,.07,.52,.63),1.5:(0,.07,.52,.63),2.0:(0,.08,.52,.62),2.5:(0,.07,.53,.63),3.0:(0,.07,.54,.63),3.5:(0,.07,.53,.63),
4.0:(0,.08,.52,.62),4.5:(0,.08,.53,.62),5.0:(0,.08,.53,.70),5.5:(0,.10,.50,.65),6.0:(0,.10,.49,.60),6.5:(0,.10,.50,.60),7.0:(0,.14,.50,.52),7.5:(0,.16,.49,.50),
8.0:(0,.17,.50,.48),8.5:(0,.17,.50,.48),9.0:(0,.17,.49,.50),9.5:(0,.17,.49,.50),10.0:(0,.15,.42,.50)}
M={0.0:(.52,.08,.48,.62),0.5:(.52,.08,.48,.62),1.0:(.52,.08,.48,.62),1.5:(.52,.08,.48,.62),2.0:(.52,.08,.48,.62),2.5:(.53,.08,.47,.62),3.0:(.54,.08,.46,.62),3.5:(.53,.08,.47,.62),
4.0:(.52,.10,.48,.38),4.5:(.53,.10,.47,.38),5.0:(.53,.10,.47,.42),5.5:(.50,.10,.50,.68),6.0:(.49,.10,.51,.58),6.5:(.50,.12,.50,.56),7.0:(.50,.14,.50,.60),7.5:(.49,.14,.51,.60),
8.0:(.50,.17,.50,.55),8.5:(.50,.17,.50,.55),9.0:(.49,.17,.51,.50),9.5:(.49,.17,.51,.42),10.0:(.42,.15,.58,.40)}
c={"mediaId":205,"level":"A","keyWord":"crying","defaultVoice":"female",
"taps":[tap("to wipe her tears","the woman","female",W),tap("to hug the woman","the man","male",M),tap("to take a tissue","the woman","female",W)],
"stillS":0.0,
"nouns":[noun("a woman",.22,.28,"female"),noun("a man",.73,.22,"male"),noun("a blanket",.62,.60,"female"),noun("tissues",.20,.72,"female")],
"question":"What is the woman doing?","answer":["She","is","crying","and","wiping","her","tears."],"answerVoice":"female",
"notes":"The two sit close and overlap from 7.0 (hug): boxes are split on a vertical line between the heads, the man's arm around her lies in her box and from 7.5 his head leans a little over the line. At 4.0-5.0 her hand with the tissue is in front of his chest, his box is cut to his head and shoulders there. A cat comes in bottom right at 9.0-10 (not used). 'tissues' = the tissue box with a tissue sticking out. The man also has wet eyes, so no 'to cry' phrase."}
json.dump(c,open('content/205.json','w'),indent=1)
