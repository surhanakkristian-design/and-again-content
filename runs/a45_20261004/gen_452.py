import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
woman={0.0:(.16,0,.84,.80),0.5:(.16,0,.84,.80),1.0:(.17,.03,.83,.80),1.5:(.18,.03,.82,.84),2.0:(.24,.07,.76,.60),2.5:(.28,.18,.72,.52),3.0:(.33,.25,.67,.60),8.0:(.49,.26,.51,.42),8.5:(.50,.30,.50,.30),9.0:(.50,.30,.48,.38)}
man={0.0:(0,.22,.14,.58),0.5:(0,.22,.14,.58),1.0:(0,0,.16,.88),1.5:(0,0,.17,.88),2.0:(0,0,.23,.80),2.5:(0,.15,.27,.67),3.0:(0,.18,.32,.72),7.5:(0,0,1,.26),8.0:(0,.22,.47,.46),8.5:(0,.26,.47,.34),9.0:(.14,.28,.35,.29)}
dog={8.0:(0,.72,.18,.17),8.5:(0,.61,.24,.14),9.0:(0,.58,.26,.14),9.5:(0,.27,1,.73),10.0:(0,.25,1,.75)}
c={"mediaId":452,"level":"B","keyWord":"logo","defaultVoice":"female",
"taps":[
 {"phrase":"to sketch a logo","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to have a thick beard","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to doze on the desk","target":"the dog","voice":"female","keys":keys(dog)}],
"stillS":2.0,
"nouns":[{"word":"a logo","x":.47,"y":.47,"voice":"female"},{"word":"glasses","x":.68,"y":.23,"voice":"female"},{"word":"a laptop","x":.85,"y":.87,"voice":"female"},{"word":"a desk","x":.35,"y":.70,"voice":"female"}],
"question":"What is the woman drawing?",
"answer":["She","is","sketching","a","logo","on","paper."],
"answerVoice":"female",
"notes":"Many cuts. Close-ups 3.5-7.0 and 9.5-10.0 show only hands of an unidentifiable person: people set off there. Man phrase is a state (beard) because every action of his (smiling, pointing, high five) is shared with the woman; at 0.0-1.5 only his arm/edge of head is visible at the left border. Dog at 8.0-9.0 is only its legs at the left edge."}
json.dump(c,open("content/452.json","w"),indent=1)
