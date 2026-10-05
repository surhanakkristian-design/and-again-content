import json,os,sys
H=os.path.dirname(os.path.abspath(__file__))
def keys(times,d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T=[i*0.5 for i in range(21)]
man={0.0:(0,0.05,0.66,0.95),0.5:(0,0.0,0.63,1.0),1.0:(0,0.05,0.69,0.95),1.5:(0,0.13,0.70,0.87),2.0:(0.08,0.19,0.63,0.81),2.5:(0.39,0.19,0.41,0.74)}
gate={0.0:(0.67,0.56,0.31,0.44),0.5:(0.64,0.56,0.34,0.44),1.0:(0.70,0.60,0.30,0.40),1.5:(0.71,0.65,0.29,0.35),2.0:(0.72,0.64,0.28,0.36),2.5:(0.81,0.68,0.19,0.32)}
wom={3.0:(0.19,0.07,0.81,0.93),3.5:(0.15,0.09,0.85,0.91),4.0:(0.30,0.13,0.70,0.87),4.5:(0.32,0.13,0.68,0.87),5.0:(0.56,0.12,0.44,0.88),5.5:(0.64,0.14,0.36,0.86),6.0:(0.42,0.15,0.58,0.85),6.5:(0.45,0.23,0.55,0.77),7.0:(0.45,0.29,0.55,0.71),7.5:(0.38,0.25,0.62,0.38),8.0:(0.21,0.20,0.79,0.36),8.5:(0.17,0.29,0.83,0.35),9.5:(0.60,0.06,0.40,0.94),10.0:(0.51,0.12,0.49,0.88)}
c={"mediaId":5076,"level":"A","keyWord":"member","defaultVoice":"female",
"taps":[
 {"phrase":"to walk into the gym","target":"the young man","voice":"male","keys":keys(T,man)},
 {"phrase":"to show a green tick","target":"the gate","voice":"female","keys":keys(T,gate)},
 {"phrase":"to move a chess piece","target":"the old woman","voice":"female","keys":keys(T,wom)}],
"stillS":6.0,
"nouns":[{"word":"books","x":0.30,"y":0.17,"voice":"female"},{"word":"a woman","x":0.82,"y":0.36,"voice":"female"},
 {"word":"a chessboard","x":0.28,"y":0.73,"voice":"female"},{"word":"a table","x":0.50,"y":0.86,"voice":"female"}],
"question":"What is the old woman doing?","answer":["She","is","moving","a","chess","piece."],"answerVoice":"female",
"notes":"Two shots: gym (0.0-2.5, young man + turnstile post with green tick) and library chess club (3.0-10.0). At 7.5-8.5 only the old woman's hand and cardigan sleeve are visible moving the white king; at 9.0 she is out of frame (off). Man and gate boxes split at the card reader, the man's hand with the card is cut a little at 0.0-1.5. The 'gate' is the turnstile post with the green tick; its kiosk screen above is not in the box. Key word 'member' is not a visible noun."}
json.dump(c,open(f"{H}/content/5076.json","w"),indent=1)
