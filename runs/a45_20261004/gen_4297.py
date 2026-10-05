import json
def keys(T,b):
    return [({"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]}) for t,k in zip(T,b)]
def R(x1,y1,x2,y2): return (round(x1,2),round(y1,2),round(x2-x1,2),round(y2-y1,2))
out={}
# ---------- 4297
T=[i*0.5 for i in range(19)]
wom=[(.33,.36,.6,.64),(.15,.36,.75,.64),(.22,.38,.68,.62),(.2,.38,.7,.62),(.35,.42,.65,.58),(.35,.42,.6,.58),(.33,.43,.67,.57),(.33,.43,.67,.57),
(.28,.4,.67,.6),(.25,.39,.7,.61),(.2,.43,.7,.57),(.27,.38,.73,.62),(.31,.4,.64,.6),(.36,.4,.6,.6),(.33,.42,.6,.58),(.36,.41,.6,.59),
(.33,.41,.6,.59),(.36,.4,.6,.6),(.33,.42,.6,.58)]
board=[None]*4+[(0,0,1,.42),(0,0,1,.42),(0,0,1,.43),(0,0,1,.43),(0,0,1,.4),(0,0,.9,.39),(0,0,.72,.37)]+[None]*8
fall=[None]*12+[(0,0,.3,.8),(0,0,.36,.75),(0,0,.63,.42),(.15,0,.7,.41),(.33,0,.67,.41),(.45,0,.55,.4),(.55,0,.45,.42)]
d={"mediaId":4297,"level":"B","keyWord":"departure","defaultVoice":"female",
"taps":[{"phrase":"to gaze up in amazement","target":"the woman","voice":"female","keys":keys(T,wom)},
{"phrase":"to display the flight departures","target":"the departures board","voice":"female","keys":keys(T,board)},
{"phrase":"to cascade from the ceiling","target":"the waterfall","voice":"female","keys":keys(T,fall)}],
"stillS":4.5,
"nouns":[{"word":"a departures board","x":.4,"y":.15,"voice":"female"},{"word":"luggage trolleys","x":.22,"y":.57,"voice":"female"},
{"word":"a neck pillow","x":.7,"y":.57,"voice":"female"},{"word":"a suitcase","x":.32,"y":.9,"voice":"female"}],
"question":"What is the woman gazing at?","answer":["She","is","gazing","up","at","the","departures","board."],"answerVoice":"female",
"notes":"Key word 'departure' appears as 'departures board' / 'flight departures'. Woman and board / waterfall overlap in the picture: split on a horizontal line at the top of her head (7.0-9.0 s the waterfall box is only the part above her head; at 6.0-6.5 s it is left of her). Board on 2.0-5.0 s, waterfall 6.0-9.0 s. The text on the board is AI gibberish but it reads as a departures board."}
json.dump(d,open("content/4297.json","w"),indent=1)
