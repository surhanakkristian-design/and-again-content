import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(.19,.32,.72,1),0.5:(.20,.28,.84,1),1.0:(.14,.23,.80,1),1.5:(.12,.22,.76,1),2.0:(.08,.20,.78,1),2.5:(.04,.17,.78,1),
3.0:(.02,.15,.80,1),3.5:(.02,.14,.80,1),4.0:(.10,.13,.82,1),4.5:(.17,.13,.88,1),5.0:(.15,.13,.95,1),5.5:(.11,.13,1,1),
6.0:(.11,.13,1,1),6.5:(.21,.13,.96,1),7.0:(.30,.14,1,1),7.5:(.30,.14,1,1),8.0:(.18,.51,.83,1),8.5:(.33,.51,.67,1),
9.0:(.25,.52,.65,1),9.5:(.14,.52,.75,1),10.0:(.14,.54,.83,1),10.5:(.12,.55,.87,1),11.0:(.14,.56,.87,1),11.5:(.13,.57,.87,1),12.0:(.15,.58,.86,1)}
M={0.0:(.82,.52,1,.68),0.5:(.85,.55,1,.72),1.0:(.80,.61,1,.77),1.5:(.77,.62,1,.77),2.0:(.79,.64,1,.80),2.5:(.79,.66,1,.82),
3.0:(.80,.67,1,.82),3.5:(.80,.69,1,.84)}
c={"mediaId":5205,"level":"B","keyWord":"oath","defaultVoice":"female",
"taps":[{"phrase":"to take an oath","target":"the woman","voice":"female","keys":K(W)},
{"phrase":"to hold a leather-bound book","target":"the man on the right","voice":"male","keys":K(M)},
{"phrase":"to spread her arms wide","target":"the woman","voice":"female","keys":K(W)}],
"stillS":8.0,
"nouns":[{"word":"a dome","x":.50,"y":.08,"voice":"female"},{"word":"columns","x":.50,"y":.41,"voice":"female"},
{"word":"a sash","x":.58,"y":.75,"voice":"female"},{"word":"photographers","x":.20,"y":.93,"voice":"female"}],
"question":"Why is the woman raising her hand?","answer":["She","is","taking","an","oath."],"answerVoice":"female",
"notes":"The woman resembles a real politician; texts only say 'the woman'. 'The man on the right' is only a hand with a white cuff and dark sleeve at the right edge holding the red leather-bound book from below (0.0-3.5); his boxes are small and the woman's box is cut just left of the book, so her hand resting on the book falls in his box. From 4.0 he is off (other men's arms put the sash on her, a man shakes her hand at 6.5-7.5). Oath = right hand raised, other hand on the book (1.0-3.5, hand still raised up to 6.0). Arms spread wide 10.0-12.0 (back view). Still 8.0 wide shot: dome, columns, sash, photographers in the bottom row."}
json.dump(c,open('content/5205.json','w'),indent=1)
