import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]

# ---------- 575
t=T(21)
man={0.0:(.05,.13,.95,.87),0.5:(.05,.10,.95,.90),2.0:(0,.18,1,.82),2.5:(0,.20,1,.80),3.0:(.53,.20,.47,.80),
 4.5:(.71,.25,.29,.75),5.0:(.58,.35,.42,.65),5.5:(.54,.35,.46,.65),6.0:(.52,.22,.48,.65),6.5:(.48,.08,.52,.74),
 7.0:(.47,0,.53,.90),7.5:(.52,0,.48,.76),8.0:(.53,0,.47,.72),8.5:(.56,.08,.44,.72),9.0:(.54,.17,.46,.76),
 9.5:(.35,.20,.65,.62),10.0:(.57,.18,.43,.60)}
wom={3.0:(0,.08,.50,.92),3.5:(.08,0,.92,.93),4.0:(0,.08,.93,.85),4.5:(0,.16,.70,.76),5.0:(0,.25,.57,.75),
 5.5:(0,.30,.53,.70),6.0:(0,.17,.51,.68),6.5:(0,.02,.47,.76),7.0:(0,0,.46,.74),7.5:(0,0,.34,.66),8.0:(0,0,.36,.65),
 8.5:(0,.12,.50,.60),9.0:(0,.17,.50,.70),9.5:(0,.18,.34,.68),10.0:(0,.13,.38,.62)}
j={"mediaId":575,"level":"B","keyWord":"power bank","defaultVoice":"male",
 "taps":[
  {"phrase":"to throw his hands up","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to rummage through her bag","target":"the woman","voice":"female","keys":K(t,wom)},
  {"phrase":"to hold up a power bank","target":"the woman","voice":"female","keys":K(t,wom)}],
 "stillS":10.0,
 "nouns":[{"word":"a power bank","x":.40,"y":.74,"voice":"male"},{"word":"pigeons","x":.50,"y":.64,"voice":"male"},
          {"word":"roses","x":.45,"y":.46,"voice":"male"},{"word":"a bench","x":.50,"y":.90,"voice":"male"}],
 "question":"What are they plugging the phone into?",
 "answer":["They","are","plugging","the","phone","into","a","power","bank."],
 "answerVoice":"male",
 "notes":"Two targets only (man, woman): the pigeons are small and sit under the man's stretched arm at 9.5 s. At 5.0-5.5 s the woman's raised arm with the power bank crosses in front of the man; boxes split on a vertical line, so the right edge of the power bank at 5.5 s falls in the man's box. Dark shape bottom-left at 0-0.5 s (probably her knee) not boxed. The phone lies right next to the power bank, so 'a phone' was left out of the nouns."}
json.dump(j,open("content/575.json","w"),indent=1)
