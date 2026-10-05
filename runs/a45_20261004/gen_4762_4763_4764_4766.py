import json
def keys(F,k,times):
    out=[]
    for t in times:
        if t in F and k in F[t]:
            x,y,w,h=F[t][k]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(d): json.dump(d,open("content/%d.json"%d["mediaId"],"w"),indent=1,ensure_ascii=False)

# ---------- 4762
M="m";P="p"
F={0.0:{M:(0.12,0.33,0.70,0.67)},0.5:{M:(0.17,0.33,0.64,0.67)},1.0:{M:(0.22,0.36,0.63,0.64)},
1.5:{M:(0.15,0.34,0.63,0.66)},2.0:{M:(0.04,0.35,0.66,0.65)},2.5:{M:(0,0.34,0.66,0.66)},
3.0:{M:(0,0.32,0.63,0.68)},3.5:{M:(0,0.33,0.52,0.67)},4.0:{M:(0,0.32,0.47,0.68)},
4.5:{M:(0,0.32,0.49,0.68)},5.0:{M:(0,0.32,0.49,0.68)},
5.5:{M:(0.38,0.65,0.24,0.26),P:(0.25,0.39,0.52,0.25)},
6.0:{M:(0.37,0.65,0.24,0.25),P:(0.23,0.38,0.54,0.26)},
6.5:{M:(0.39,0.65,0.24,0.25),P:(0.24,0.38,0.54,0.26)},
7.0:{M:(0.38,0.66,0.24,0.25),P:(0.22,0.37,0.56,0.28)},
7.5:{M:(0.36,0.66,0.26,0.25),P:(0.23,0.35,0.56,0.30)},
8.0:{M:(0.32,0.65,0.36,0.27),P:(0.20,0.34,0.60,0.30)},
8.5:{M:(0.30,0.65,0.40,0.28),P:(0.18,0.32,0.64,0.32)},
9.0:{M:(0.30,0.66,0.40,0.28),P:(0.17,0.32,0.66,0.33)}}
tt=T(19)
save({"mediaId":4762,"level":"B","keyWord":"gallery","defaultVoice":"male",
"taps":[
 {"phrase":"to clutch a leather briefcase","target":"the man","voice":"male","keys":keys(F,M,tt)},
 {"phrase":"to gaze up at a canvas","target":"the man","voice":"male","keys":keys(F,M,tt)},
 {"phrase":"to cover the far wall","target":"the huge painting","voice":"male","keys":keys(F,P,tt)}],
"stillS":2.0,
"nouns":[{"word":"the ceiling","x":0.50,"y":0.07,"voice":"male"},
 {"word":"a sculpture","x":0.77,"y":0.55,"voice":"male"},
 {"word":"a plinth","x":0.78,"y":0.76,"voice":"male"},
 {"word":"a briefcase","x":0.27,"y":0.93,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","gazing","at","paintings","in","a","gallery."],
"answerVoice":"male",
"notes":"Only the man is a clean single target through the clip (visitors and sculptures are several, scattered and half hidden behind him), so two phrases share him; third target = the enormous painting of the last shot (5.5-9.0 s), its box ends above the man's head, his box starts there. The abstract canvas at 3.5-5.0 s hangs on a side wall and is not boxed. 'gallery' is the whole room, not placeable as a noun slot: used in the answer. Still 2.0 s: a second sculpture/plinth stands at the left edge; no other noun labels it."})

# ---------- 4763
S="s";W="w";G="g"
F={0.0:{S:(0,0.25,0.74,0.50)},0.5:{S:(0,0.26,0.74,0.50)},1.0:{S:(0,0.25,0.74,0.50)},1.5:{S:(0,0.27,0.74,0.50)},
2.0:{S:(0,0.29,0.72,0.50)},
2.5:{W:(0,0.34,1.0,0.66)},3.0:{W:(0,0.09,0.48,0.86)},3.5:{W:(0,0.15,0.48,0.80)},4.0:{W:(0,0.17,0.50,0.78)},
8.0:{G:(0.16,0.14,0.66,0.28)},8.5:{G:(0.16,0.12,0.72,0.29)},9.0:{G:(0.01,0,0.98,0.36)},
9.5:{G:(0,0,1.0,0.25)},10.0:{G:(0,0,1.0,0.15)}}
tt=T(21)
save({"mediaId":4763,"level":"B","keyWord":"gamer","defaultVoice":"male",
"taps":[
 {"phrase":"to slouch on the sofa","target":"the man on the sofa","voice":"male","keys":keys(F,S,tt)},
 {"phrase":"to tap a glowing keyboard","target":"the woman at the desk","voice":"female","keys":keys(F,W,tt)},
 {"phrase":"to display the champion","target":"the giant screen","voice":"male","keys":keys(F,G,tt)}],
"stillS":1.5,
"nouns":[{"word":"a gamer","x":0.17,"y":0.44,"voice":"male"},
 {"word":"a controller","x":0.42,"y":0.56,"voice":"male"},
 {"word":"a television","x":0.66,"y":0.34,"voice":"male"},
 {"word":"a sofa","x":0.50,"y":0.85,"voice":"male"}],
"question":"Who is slouching on the sofa?",
"answer":["A","gamer","is","slouching","on","the","sofa."],
"answerVoice":"male",
"notes":"Four shots; one target per shot, the living-room shot of friends (4.5-7.5 s) has no target (all off). Woman at the desk: at 2.5 s only her two hands are in the picture (box = both hands, includes the keyboard between them); 3.0-4.0 s box = head, body and the hand on the keyboard, the far mouse hand is left out to keep the monitor outside. Giant screen grows and slides up out of frame, at 10.0 s only its bottom strip is left. defaultVoice male: mixed group, evenId false. The question names its subject by place because several men appear."})

# ---------- 4764
W="w";M="m";B="b"
F={
0.0:{W:(0,0.23,0.55,0.53),M:(0.61,0.27,0.39,0.73),B:(0.36,0.77,0.25,0.15)},
0.5:{W:(0,0.23,0.55,0.53),M:(0.63,0.27,0.37,0.73),B:(0.37,0.77,0.26,0.15)},
1.0:{W:(0,0.24,0.52,0.53),M:(0.53,0.28,0.47,0.49),B:(0.34,0.77,0.25,0.15)},
1.5:{W:(0,0.20,0.52,0.57),M:(0.54,0.25,0.46,0.52),B:(0.39,0.77,0.25,0.15)},
2.0:{W:(0,0.23,0.52,0.53),M:(0.54,0.26,0.46,0.50),B:(0.36,0.77,0.26,0.15)},
2.5:{W:(0,0.24,0.52,0.53),M:(0.53,0.26,0.47,0.51),B:(0.36,0.77,0.27,0.15)},
3.0:{W:(0,0.24,0.55,0.54),M:(0.57,0.26,0.43,0.52),B:(0.35,0.78,0.27,0.15)},
3.5:{W:(0,0.25,0.49,0.53),M:(0.50,0.28,0.50,0.50),B:(0.32,0.78,0.27,0.15)},
4.0:{W:(0,0.13,0.52,0.64),M:(0.54,0.27,0.46,0.50),B:(0.36,0.77,0.26,0.15)},
4.5:{W:(0,0.04,0.58,0.76),M:(0.59,0.31,0.41,0.49),B:(0.37,0.80,0.28,0.15)},
5.0:{W:(0,0.17,0.52,0.62),M:(0.53,0.30,0.47,0.49),B:(0.32,0.79,0.28,0.15)},
5.5:{W:(0,0.17,0.58,0.62),M:(0.59,0.29,0.41,0.50),B:(0.34,0.79,0.28,0.15)},
6.0:{W:(0,0.16,0.60,0.63),M:(0.61,0.30,0.39,0.49),B:(0.36,0.79,0.26,0.15)},
6.5:{W:(0,0,0.64,0.80),M:(0.65,0.30,0.35,0.50),B:(0.36,0.80,0.28,0.15)},
7.0:{W:(0,0,0.57,0.86),M:(0.58,0.54,0.42,0.46),B:(0.35,0.86,0.23,0.14)},
7.5:{W:(0.07,0,0.50,0.86),M:(0.60,0.55,0.40,0.31),B:(0.42,0.86,0.30,0.14)},
8.0:{W:(0.04,0,0.55,0.86),M:(0.61,0.56,0.39,0.30),B:(0.42,0.86,0.30,0.14)},
8.5:{W:(0,0,0.58,0.86),M:(0.62,0.56,0.38,0.30),B:(0.46,0.86,0.29,0.14)},
9.0:{W:(0,0.49,0.62,0.37),M:(0.64,0.53,0.36,0.33),B:(0.46,0.86,0.30,0.14)},
9.5:{W:(0,0.48,0.69,0.38),M:(0.70,0.48,0.30,0.38),B:(0.43,0.86,0.30,0.14)},
10.0:{W:(0,0.46,0.69,0.32),M:(0.71,0.43,0.29,0.57),B:(0.41,0.78,0.29,0.14)}}
save({"mediaId":4764,"level":"A","keyWord":"sofa","defaultVoice":"female",
"taps":[
 {"phrase":"to jump on the sofa","target":"the woman","voice":"female","keys":keys(F,W,tt)},
 {"phrase":"to wear a green hoodie","target":"the man","voice":"male","keys":keys(F,M,tt)},
 {"phrase":"to be full of crisps","target":"the bowl","voice":"female","keys":keys(F,B,tt)}],
"stillS":10.0,
"nouns":[{"word":"a sofa","x":0.18,"y":0.54,"voice":"female"},
 {"word":"a woman","x":0.30,"y":0.66,"voice":"female"},
 {"word":"a man","x":0.80,"y":0.72,"voice":"male"},
 {"word":"a bowl","x":0.55,"y":0.84,"voice":"female"}],
"question":"Where is the woman jumping?",
"answer":["She","is","jumping","on","the","sofa."],
"answerVoice":"female",
"notes":"Both play and both laugh, so the man gets a state (green hoodie) and the bowl a state. The bowl sits between her knees and his legs: the woman's and the man's boxes end at the top of the bowl box, so her lower legs / feet and his lap are partly outside their boxes. 6.5-7.0 s her raised right arm reaches over the man's side and is left out of her box. 9.5-10.0 s the two lean head to head: split on the line between the heads. 'crisps' (British) follows the packet description."})

# ---------- 4766
W="w";H="h"
F={0.0:{W:(0.32,0.29,0.30,0.28)},0.5:{W:(0.23,0.28,0.31,0.64)},1.0:{W:(0.21,0.27,0.44,0.73)},
1.5:{W:(0.19,0.25,0.61,0.75)},2.0:{W:(0.16,0.24,0.69,0.76)},2.5:{W:(0,0.27,0.61,0.73)},
3.0:{W:(0.06,0.25,0.66,0.75)},3.5:{W:(0.03,0.24,0.69,0.76)},4.0:{W:(0,0.21,0.81,0.79)},
4.5:{W:(0,0.22,0.72,0.78)},5.0:{W:(0,0.17,0.59,0.83)},5.5:{W:(0,0.14,0.41,0.86)},
6.0:{W:(0,0.04,0.53,0.96)},6.5:{W:(0,0,0.53,1.0)},7.0:{W:(0,0,0.50,1.0)},7.5:{W:(0,0,0.53,1.0)},
8.0:{W:(0,0,0.58,1.0)},
8.5:{W:(0.34,0.30,0.66,0.50),H:(0.02,0.12,0.60,0.18)},
9.0:{W:(0.41,0.31,0.33,0.60),H:(0,0.14,0.60,0.17)},
9.5:{W:(0.27,0.31,0.44,0.58),H:(0,0.14,0.60,0.17)},
10.0:{W:(0.12,0.31,0.71,0.47),H:(0,0.14,0.58,0.17)},
10.5:{W:(0.07,0.31,0.86,0.46),H:(0,0.14,0.58,0.17)},
11.0:{W:(0.07,0.32,0.88,0.46),H:(0,0.14,0.58,0.18)},
11.5:{W:(0.08,0.32,0.86,0.46),H:(0,0.14,0.58,0.18)},
12.0:{W:(0.09,0.32,0.83,0.46),H:(0,0.14,0.60,0.18)}}
tt=T(25)
save({"mediaId":4766,"level":"A","keyWord":"garden","defaultVoice":"female",
"taps":[
 {"phrase":"to open the garden gate","target":"the woman","voice":"female","keys":keys(F,W,tt)},
 {"phrase":"to touch the red tomatoes","target":"the woman","voice":"female","keys":keys(F,W,tt)},
 {"phrase":"to have a red roof","target":"the house","voice":"female","keys":keys(F,H,tt)}],
"stillS":10.5,
"nouns":[{"word":"the sky","x":0.60,"y":0.08,"voice":"female"},
 {"word":"a house","x":0.28,"y":0.27,"voice":"female"},
 {"word":"a woman","x":0.68,"y":0.50,"voice":"female"},
 {"word":"flowers","x":0.66,"y":0.83,"voice":"female"}],
"question":"What is the woman opening?",
"answer":["She","is","opening","the","garden","gate."],
"answerVoice":"female",
"notes":"Key word is the verb 'garden', but she never digs or plants: she walks through her garden, so the word appears as 'garden gate' in a phrase and the answer. One person in the clip, two phrases share her; second target = the house behind the garden in the last shot (state, nothing else there acts). At 0.0 s only her hat and one hand show behind the gate. 'flowers' sits on the cut flowers in the wheelbarrow; flowers also grow in the beds around."})
