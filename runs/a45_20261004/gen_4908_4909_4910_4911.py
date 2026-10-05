import json, sys
def K(times, spec):
    out=[]
    for t in times:
        b=spec.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(d):
    json.dump(d, open(f"content/{d['mediaId']}.json","w"), indent=1, ensure_ascii=False)
T=lambda n:[round(i*0.5,1) for i in range(n)]
vid=sys.argv[1]
if vid=='4908':
    t=T(19)
    ruler={0.0:(0.0,0.33,1.0,0.16),0.5:(0.0,0.31,1.0,0.18),1.0:(0.15,0.28,0.66,0.23),1.5:(0.22,0.25,0.52,0.26),2.0:(0.26,0.21,0.42,0.31)}
    girl={4.5:(0.10,0.17,0.90,0.78),5.0:(0.03,0.35,0.88,0.56),5.5:(0.05,0.35,0.86,0.55),6.0:(0.03,0.35,0.85,0.54),6.5:(0.03,0.35,0.85,0.54)}
    press={x:(0.15,0.0,0.75,0.48) for x in [7.0,7.5,8.0,8.5,9.0]}
    write({"mediaId":4908,"level":"B","keyWord":"branch","defaultVoice":"female",
     "taps":[{"phrase":"to bend into an S shape","target":"the plastic ruler","voice":"female","keys":K(t,ruler)},
             {"phrase":"to arch her back","target":"the girl","voice":"female","keys":K(t,girl)},
             {"phrase":"to press down on a beam","target":"the press","voice":"female","keys":K(t,press)}],
     "stillS":2.5,
     "nouns":[{"word":"leaves","x":0.40,"y":0.12,"voice":"female"},{"word":"a branch","x":0.55,"y":0.44,"voice":"female"},{"word":"a fence","x":0.62,"y":0.55,"voice":"female"},{"word":"a lawn","x":0.60,"y":0.78,"voice":"female"}],
     "question":"What is the girl doing?","answer":["She","is","arching","her","back."],"answerVoice":"female",
     "notes":"Four separate shots (ruler, branch, girl, press); each target only in its shot. Key word branch used as noun only (the ruler, beam and girl also bend, so no 'bend' phrase for the branch)."})
if vid=='4909':
    t=T(21)
    w={0.0:(0.10,0.20,0.90,0.80),0.5:(0.18,0.22,0.82,0.78),1.0:(0.0,0.26,0.85,0.74),1.5:(0.0,0.26,1.0,0.74),2.0:(0.0,0.20,0.85,0.80),
       2.5:(0.13,0.38,0.37,0.62),3.0:(0.18,0.34,0.54,0.64),3.5:(0.0,0.22,1.0,0.78),
       7.0:(0.0,0.18,1.0,0.82),7.5:(0.0,0.20,1.0,0.80),8.0:(0.0,0.22,1.0,0.78),8.5:(0.18,0.32,0.62,0.68),9.0:(0.22,0.43,0.52,0.57),
       9.5:(0.21,0.22,0.69,0.78),10.0:(0.12,0.22,0.78,0.78)}
    c={2.5:(0.65,0.47,0.35,0.43),3.0:(0.73,0.58,0.27,0.42),4.0:(0.0,0.56,1.0,0.44),4.5:(0.0,0.56,1.0,0.44),5.0:(0.0,0.58,1.0,0.42),
       5.5:(0.0,0.58,1.0,0.42),6.0:(0.0,0.56,1.0,0.44),6.5:(0.0,0.56,1.0,0.44),8.5:(0.81,0.30,0.19,0.50),9.0:(0.75,0.48,0.25,0.42),9.5:(0.0,0.50,0.20,0.40)}
    write({"mediaId":4909,"level":"A","keyWord":"famous","defaultVoice":"female",
     "taps":[{"phrase":"to climb a lamppost","target":"the woman","voice":"female","keys":K(t,w)},
             {"phrase":"to stand above the crowd","target":"the woman","voice":"female","keys":K(t,w)},
             {"phrase":"to hold up their phones","target":"the crowd","voice":"female","keys":K(t,c)}],
     "stillS":6.0,
     "nouns":[{"word":"the sky","x":0.35,"y":0.12,"voice":"female"},{"word":"the sun","x":0.33,"y":0.41,"voice":"female"},
              {"word":"buildings","x":0.82,"y":0.30,"voice":"female"},{"word":"people","x":0.50,"y":0.80,"voice":"female"}],
     "question":"What is the woman doing?","answer":["She","is","climbing","a","lamppost."],"answerVoice":"female",
     "notes":"Crowd box is off in the selfie close-ups (0-2.0, 3.5, 7.0-8.0) and at 10.0, where the background people sit behind the woman and a box would overlap hers; phones are clearly held up in the wide shots 4.0-6.5. Key word 'famous' is an adjective, not used as a noun."})
if vid=='4910':
    t=T(21)
    m={0.0:(0.05,0.24,0.95,0.76),0.5:(0.12,0.12,0.88,0.88),1.0:(0.05,0.08,0.85,0.92),4.0:(0.0,0.08,0.95,0.92),4.5:(0.05,0.0,0.95,1.0),
       5.0:(0.0,0.0,1.0,1.0),5.5:(0.05,0.20,0.95,0.80),6.0:(0.0,0.12,1.0,0.88),8.0:(0.24,0.48,0.46,0.52),8.5:(0.72,0.08,0.28,0.84),
       9.0:(0.15,0.22,0.80,0.78),9.5:(0.08,0.19,0.65,0.81)}
    f={1.5:(0.28,0.34,0.52,0.46),2.0:(0.45,0.12,0.50,0.68),2.5:(0.17,0.31,0.40,0.45),3.0:(0.15,0.42,0.48,0.42),3.5:(0.29,0.33,0.57,0.43)}
    write({"mediaId":4910,"level":"A","keyWord":"scarf","defaultVoice":"male",
     "taps":[{"phrase":"to shout at the camera","target":"the man","voice":"male","keys":K(t,m)},
             {"phrase":"to wear face paint","target":"the man","voice":"male","keys":K(t,m)},
             {"phrase":"to fly above the fans","target":"the flag","voice":"male","keys":K(t,f)}],
     "stillS":4.0,
     "nouns":[{"word":"hair","x":0.50,"y":0.13,"voice":"male"},{"word":"an eye","x":0.38,"y":0.42,"voice":"male"},
              {"word":"a mouth","x":0.53,"y":0.67,"voice":"male"},{"word":"a scarf","x":0.14,"y":0.84,"voice":"male"}],
     "question":"What is the man doing?","answer":["He","is","shouting","at","the","camera."],"answerVoice":"male",
     "notes":"Man box off at 1.5-3.5 (only the blurred top of his head at the bottom edge), 6.5-7.5 (other fans jumping/hugging, his face not visible) and 10.0 (back of another head). Flag only in the wide fisheye shot 1.5-3.5."})
if vid=='4911':
    t=T(21)
    w={0.0:(0.0,0.08,1.0,0.92),0.5:(0.0,0.07,1.0,0.93),1.0:(0.0,0.08,1.0,0.92),1.5:(0.04,0.25,0.74,0.75),2.0:(0.06,0.23,0.74,0.77),
       2.5:(0.17,0.26,0.62,0.74),3.0:(0.15,0.24,0.66,0.76),5.0:(0.05,0.23,0.90,0.77),5.5:(0.20,0.24,0.68,0.76),6.0:(0.18,0.36,0.58,0.26),
       6.5:(0.10,0.36,0.72,0.26),7.0:(0.09,0.34,0.70,0.29),7.5:(0.33,0.33,0.36,0.31),8.0:(0.37,0.33,0.34,0.39),8.5:(0.33,0.33,0.44,0.42),
       9.0:(0.20,0.35,0.64,0.39),9.5:(0.07,0.34,0.88,0.39),10.0:(0.02,0.31,0.93,0.40)}
    s={2.5:(0.82,0.15,0.18,0.24),3.0:(0.82,0.12,0.18,0.30),3.5:(0.30,0.15,0.52,0.34),4.0:(0.13,0.19,0.60,0.36),4.5:(0.27,0.25,0.50,0.30)}
    write({"mediaId":4911,"level":"A","keyWord":"owner","defaultVoice":"female",
     "taps":[{"phrase":"to hold up her keys","target":"the woman","voice":"female","keys":K(t,w)},
             {"phrase":"to put on an apron","target":"the woman","voice":"female","keys":K(t,w)},
             {"phrase":"to hang on the door","target":"the sign","voice":"female","keys":K(t,s)}],
     "stillS":7.5,
     "nouns":[{"word":"windows","x":0.80,"y":0.33,"voice":"female"},{"word":"a coffee machine","x":0.25,"y":0.47,"voice":"female"},
              {"word":"a woman","x":0.52,"y":0.60,"voice":"female"},{"word":"a counter","x":0.45,"y":0.80,"voice":"female"}],
     "question":"What is the woman putting on?","answer":["She","is","putting","on","an","apron."],"answerVoice":"female",
     "notes":"Woman box off at 3.5 (only her arms, one hand on the sign) and 4.0-4.5 (sign close-up). At 3.0 her box stops at x 0.81 so it does not overlap the sign box at the right edge; her arm to the door handle is cut. Key word 'owner' is not a visible noun."})
