import json, sys
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(vid, c, times, taps):
    c["taps"]=[{"phrase":p,"target":tg,"voice":v,"keys":keys(times,d)} for p,tg,v,d in taps]
    json.dump(c, open(f"content/{vid}.json","w"), indent=1, ensure_ascii=False)
if __name__=="__main__":
    times=[i*0.5 for i in range(21)]
    man={0.0:(0.26,0.22,0.68,0.78),0.5:(0.04,0.24,0.86,0.76),1.0:(0.18,0.27,0.75,0.73),1.5:(0.20,0.18,0.80,0.82),
         2.0:(0.08,0.23,0.84,0.77),2.5:(0.06,0.28,0.90,0.72),6.0:(0.0,0.31,0.20,0.69),6.5:(0.0,0.30,0.45,0.70),
         7.0:(0.02,0.30,0.46,0.70),7.5:(0.13,0.31,0.39,0.69),8.0:(0.10,0.31,0.40,0.69),8.5:(0.03,0.30,0.42,0.70),
         9.0:(0.0,0.28,0.40,0.72),9.5:(0.0,0.26,0.40,0.74),10.0:(0.0,0.22,0.50,0.78)}
    wom={3.0:(0.34,0.29,0.66,0.50),3.5:(0.34,0.31,0.66,0.50),4.0:(0.36,0.30,0.64,0.50),4.5:(0.32,0.41,0.68,0.47),
         6.0:(0.56,0.48,0.44,0.52),6.5:(0.45,0.31,0.53,0.69),7.0:(0.48,0.32,0.28,0.68),7.5:(0.52,0.31,0.32,0.69),
         8.0:(0.50,0.32,0.30,0.68),8.5:(0.45,0.38,0.45,0.62),9.0:(0.40,0.37,0.52,0.63),9.5:(0.40,0.35,0.52,0.65),10.0:(0.50,0.24,0.48,0.76)}
    bike={3.0:(0.08,0.33,0.20,0.24),3.5:(0.12,0.32,0.20,0.24),4.0:(0.20,0.29,0.16,0.24),4.5:(0.62,0.27,0.23,0.14)}
    c={"mediaId":5254,"level":"A","keyWord":"partner","defaultVoice":"male",
       "stillS":3.5,
       "nouns":[{"word":"trees","x":0.50,"y":0.12,"voice":"male"},{"word":"a bike","x":0.22,"y":0.44,"voice":"male"},
                {"word":"a woman","x":0.78,"y":0.47,"voice":"female"},{"word":"flowers","x":0.50,"y":0.85,"voice":"male"}],
       "question":"What are the old people doing?",
       "answer":["They","are","dancing","with","their","partners."],"answerVoice":"male",
       "notes":"Three shots: man in flat cap alone (0-2.5), woman in lilac smelling marigolds with a cyclist behind (3-4.5), couples dancing (5-10). The lilac woman of the flower shot is treated as the same woman who dances with the cap man from 6.0 (same hair and cardigan). Key word 'partner' is not a placeable noun, so it is used only in the answer. Man/woman boxes split along the line between them from 6.5; at 4.5 the woman's box starts at y 0.41 so it does not overlap the cyclist (top of her hair cut). 4.0: cyclist is partly behind her hair, split at x 0.36."}
    write(5254,c,times,[("to touch his cap","the man in the cap","male",man),
                        ("to smell the flowers","the woman in purple","female",wom),
                        ("to ride a bike","the man on the bike","male",bike)])
