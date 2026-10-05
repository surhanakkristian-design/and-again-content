import json
vid=7764
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(rows): return [{"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=[(.58,.23,.42,.77),(.58,.22,.42,.78),(.58,.23,.42,.77),(.58,.22,.42,.78),(.58,.19,.42,.81),(.59,.18,.41,.82),(.58,.19,.42,.81),(.58,.18,.42,.82)]
face=[(.40,.48,.18,.24),(.40,.47,.18,.22),(.40,.49,.18,.22),(.40,.49,.18,.22),(.40,.48,.18,.24),(.39,.48,.19,.24),(.38,.48,.20,.24),(.38,.49,.20,.24)]
phone=[(.22,.43,.18,.22),(.22,.44,.18,.20),(.22,.44,.18,.20),(.22,.45,.18,.20),(.21,.44,.19,.21),(.19,.45,.19,.20),(.18,.46,.19,.20),(.18,.46,.19,.20)]
c={"mediaId":vid,"level":"A","keyWord":"bit","defaultVoice":"female",
"taps":[{"phrase":"to eat a bit of cake","target":"the woman in black","voice":"female","keys":keys(woman)},
{"phrase":"to film with his phone","target":"the man in the dark shirt","voice":"male","keys":keys(phone)},
{"phrase":"to cover his face","target":"the man in the white shirt","voice":"male","keys":keys(face)}],
"stillS":1.7,
"nouns":[{"word":"a balloon","x":.17,"y":.25,"voice":"female"},{"word":"a cake","x":.12,"y":.62,"voice":"female"},
{"word":"plates","x":.12,"y":.88,"voice":"female"},{"word":"a dress","x":.78,"y":.75,"voice":"female"}],
"question":"What is the woman in black eating?",
"answer":["She","is","eating","a","bit","of","cake."],
"answerVoice":"female",
"notes":"Key word 'bit' (noun): the tiny piece of cake on her fork is too small to place as a noun slot; it is used in phrase 1 and the answer. The woman's box starts at her body (x 0.58) so it does not overlap the man in the white shirt sitting behind her arm; her raised fork hand is outside the box. The man in the white shirt covers his face at 0.2 s and 2.2-3.7 s; at 0.7-1.7 s he laughs half hidden behind her arm."}
json.dump(c,open(f'content/{vid}.json','w'),indent=1)
