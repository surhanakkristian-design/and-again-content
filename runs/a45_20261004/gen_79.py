import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def write(mid,level,kw,dv,taps,still,nouns,q,a,av,notes):
    json.dump({"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
      "taps":[{"phrase":p,"target":t,"voice":v,"keys":keys(k)} for p,t,v,k in taps],
      "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
      "question":q,"answer":a,"answerVoice":av,"notes":notes},open(f"content/{mid}.json","w"),indent=1)
bear={0.0:(.08,.18,.80,.58),0.5:(.11,.20,.81,.56),1.0:(.08,.20,.88,.66),1.5:(.08,.19,.82,.69),2.0:(.06,.17,.84,.60),
 2.5:(.08,.24,.84,.56),3.0:(.06,.21,.86,.67),3.5:(.06,.18,.82,.70),4.0:(.06,.25,.78,.57),4.5:(.08,.11,.76,.72),
 5.0:(.11,.03,.62,.85),5.5:(.11,.11,.77,.80),6.0:(.09,.09,.77,.82),6.5:(.06,.34,.80,.57),7.0:(.09,.34,.79,.64),
 7.5:(.06,.30,.80,.68),8.0:(.06,.28,.82,.62),8.5:(.06,.26,.84,.66),9.0:(.04,.25,.88,.72),9.5:(.01,.24,.95,.74),
 10.0:(0,.22,1,.77)}
bird={0.0:(.18,0,.82,.14),0.5:(.50,0,.50,.15),1.0:(.66,0,.34,.14),1.5:(.76,0,.24,.14),2.0:(.82,0,.18,.14),
 3.5:(.78,0,.22,.14),4.0:(.68,.01,.32,.14),4.5:(.65,0,.31,.10),5.0:(.74,.02,.26,.14),5.5:(.58,0,.34,.10),
 6.0:(.54,0,.33,.08),6.5:(.54,0,.32,.14)}
write(79,"A","bear","male",
 [("to walk in the river","the bear","male",bear),
  ("to stand on two legs","the bear","male",bear),
  ("to fly over the trees","the bird","male",bird)],
 1.0,[("a bear",.50,.45,"male"),("a bird",.84,.06,"male"),("trees",.25,.20,"male"),("a river",.50,.86,"male")],
 "What is the bear doing?",["It","is","walking","in","the","river."],"male",
 "At 0.0-0.5 s two birds fly at the top: one box holds both. At 4.5-6.0 s the bird flies right next to the bear's head, boxes are squeezed (5.0 s: bear box cut on the right; 5.5 s: the bear's ear tips lie outside its box). 2.0 s only a wing tip of the bird is in the picture.")
