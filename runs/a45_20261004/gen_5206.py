import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(.19,.30,1,1),0.5:(.17,.31,1,1),1.0:(.19,.31,1,1),1.5:(.47,.32,1,1),2.0:(.11,.29,1,1),2.5:(.11,.28,1,1),
3.0:(.38,.29,1,1),3.5:(.30,.28,1,1),4.0:(.25,.23,1,1),4.5:(.38,.24,1,1),5.0:(.18,.27,1,1),5.5:(.28,.30,1,1),
6.0:(.11,.20,1,1),6.5:(0,.22,1,1),7.0:(.09,.20,1,1),7.5:(0,.25,1,1),8.0:(.61,.31,1,1),8.5:(.62,.35,1,1),9.0:(.72,.38,1,1)}
k=K(W)
c={"mediaId":5206,"level":"A","keyWord":"evidence","defaultVoice":"female",
"taps":[{"phrase":"to pin notes to the board","target":"the woman","voice":"female","keys":k},
{"phrase":"to turn the pages","target":"the woman","voice":"female","keys":k},
{"phrase":"to look at the board","target":"the woman","voice":"female","keys":k}],
"stillS":8.0,
"nouns":[{"word":"string","x":.22,"y":.30,"voice":"female"},{"word":"glasses","x":.84,"y":.40,"voice":"female"},
{"word":"a computer","x":.66,"y":.63,"voice":"female"},{"word":"a book","x":.40,"y":.84,"voice":"female"}],
"question":"What is in the woman's mouth?","answer":["She","has","a","pen","in","her","mouth."],"answerVoice":"female",
"notes":"Only one person, so all three phrases have the woman as target. Key word evidence is abstract, not placed. Pinning notes 0.0-2.5 and 5.0-7.5; turning pages of a big book 3.0-4.0 (and papers at 4.5-5.5); looking at the finished board 8.0-9.0. Pen in her mouth from 4.5 to the end. Still 8.0: red string on the board, glasses on her face (no person noun), the computer screen, the open book on the desk."}
json.dump(c,open('content/5206.json','w'),indent=1)
