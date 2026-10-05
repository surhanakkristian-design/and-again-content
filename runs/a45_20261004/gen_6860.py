import json,sys
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
young=[(0.25,0.30,0.50,0.62),(0.22,0.30,0.52,0.61),(0.36,0.31,0.37,0.60),(0.46,0.31,0.32,0.60),
       (0.47,0.32,0.29,0.56),(0.54,0.31,0.23,0.56),(0.49,0.32,0.24,0.54),(0.45,0.34,0.26,0.48)]
old=[(0.79,0.38,0.21,0.56),(0.80,0.38,0.20,0.55),(0.80,0.39,0.20,0.53),(0.80,0.39,0.20,0.53),
     (0.79,0.39,0.21,0.50),(0.79,0.39,0.21,0.49),(0.76,0.40,0.24,0.46),(0.74,0.39,0.26,0.45)]
pink=[None,None,None,None,None,(0.37,0.42,0.17,0.40),(0.17,0.42,0.31,0.43),(0.0,0.40,0.27,0.57)]
c={"mediaId":6860,"level":"B","keyWord":"baron","defaultVoice":"male",
 "taps":[
  {"phrase":"to swing the gate open","target":"the young man","voice":"male","keys":keys(T,young)},
  {"phrase":"to hold a ring of keys","target":"the old man","voice":"male","keys":keys(T,old)},
  {"phrase":"to carry a cake tin","target":"the woman in pink","voice":"female","keys":keys(T,pink)}],
 "stillS":2.7,
 "nouns":[{"word":"a castle","x":0.50,"y":0.25,"voice":"male"},
          {"word":"a cake tin","x":0.47,"y":0.56,"voice":"male"},
          {"word":"a folding table","x":0.22,"y":0.65,"voice":"male"},
          {"word":"gravel","x":0.30,"y":0.92,"voice":"male"}],
 "question":"What is the woman in pink carrying?",
 "answer":["She","is","carrying","a","cake","tin."],
 "answerVoice":"female",
 "notes":"Young man swings the gate open in 0.2-1.2 s, then stands aside. Woman in pink dress with cake tin appears only from 2.7 s (off before). Old man holds keys at waist all clip. Key word 'baron' is not a visible noun. Another woman carries the table, so the pink dress names the target."}
json.dump(c,open('content/6860.json','w'),indent=1)
