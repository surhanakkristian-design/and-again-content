import json
OFF=None
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
C={}
# ---------- 293
t=T(21)
scarf={0.0:[0.15,0.33,0.24,0.40],0.5:[0.15,0.34,0.22,0.39],1.0:[0.13,0.35,0.22,0.39],1.5:[0.13,0.35,0.22,0.39],2.0:[0.14,0.35,0.23,0.39],2.5:[0.16,0.36,0.24,0.39],3.0:[0.18,0.37,0.24,0.38],3.5:[0.19,0.38,0.23,0.40],4.0:[0.18,0.38,0.24,0.39],4.5:[0.18,0.38,0.23,0.39],5.0:[0.18,0.38,0.23,0.40],5.5:[0.14,0.38,0.25,0.40],6.0:[0.13,0.36,0.26,0.42],6.5:[0.08,0.37,0.33,0.42],7.0:[0.14,0.39,0.30,0.58],7.5:[0.24,0.42,0.22,0.56],8.0:[0.22,0.44,0.26,0.52],8.5:[0.14,0.45,0.34,0.52],9.0:[0.18,0.42,0.30,0.54],9.5:[0.15,0.40,0.33,0.56],10.0:[0.09,0.38,0.32,0.54]}
cap={0.0:[0.44,0.55,0.56,0.45],0.5:[0.40,0.55,0.60,0.45],1.0:[0.38,0.56,0.62,0.44],1.5:[0.42,0.56,0.58,0.44],2.0:[0.42,0.60,0.58,0.40],2.5:[0.41,0.62,0.59,0.38],3.0:[0.68,0.75,0.32,0.25],3.5:[0.76,0.78,0.24,0.22],4.0:[0.66,0.62,0.34,0.38],4.5:[0.64,0.63,0.36,0.37],5.0:[0.63,0.63,0.37,0.37],5.5:[0.68,0.62,0.32,0.38],6.0:[0.62,0.62,0.38,0.38],6.5:[0.62,0.63,0.38,0.37],7.0:[0.60,0.62,0.40,0.38],7.5:[0.63,0.62,0.37,0.38],8.0:[0.56,0.48,0.40,0.52],8.5:[0.52,0.46,0.46,0.54],9.0:[0.57,0.40,0.42,0.60],9.5:[0.52,0.57,0.48,0.43],10.0:[0.42,0.64,0.58,0.36]}
pig={0.0:[0.82,0.41,0.18,0.14],0.5:[0.80,0.41,0.18,0.14],1.0:[0.80,0.42,0.18,0.14],1.5:[0.80,0.42,0.18,0.14],2.0:[0.82,0.45,0.18,0.14],2.5:[0.82,0.46,0.18,0.14],3.5:[0.82,0.46,0.18,0.14],4.0:[0.82,0.48,0.18,0.14],4.5:[0.82,0.47,0.18,0.14],5.0:[0.81,0.45,0.18,0.14],5.5:[0.79,0.45,0.18,0.14],6.0:[0.77,0.47,0.18,0.14],6.5:[0.73,0.47,0.18,0.14],7.0:[0.69,0.45,0.18,0.14],7.5:[0.66,0.45,0.18,0.14],10.0:[0.59,0.46,0.18,0.14]}
C[293]={"mediaId":293,"level":"B","keyWord":"filmmaking","defaultVoice":"female",
"taps":[{"phrase":"to shield her eyes","target":"the woman in the scarf","voice":"female","keys":keys(t,scarf)},
{"phrase":"to crouch behind the camera","target":"the woman in the cap","voice":"female","keys":keys(t,cap)},
{"phrase":"to perch on the ledge","target":"the pigeon","voice":"female","keys":keys(t,pig)}],
"stillS":0.0,
"nouns":[{"word":"a microphone","x":0.56,"y":0.13,"voice":"female"},{"word":"a reflector","x":0.24,"y":0.37,"voice":"female"},{"word":"a pigeon","x":0.88,"y":0.50,"voice":"female"},{"word":"a tripod","x":0.40,"y":0.80,"voice":"female"}],
"question":"What is the camera mounted on?",
"answer":["The","camera","is","mounted","on","a","tripod."],"answerVoice":"female",
"notes":"Pigeon is small and hidden at 3.0 and 8.0-9.5 (off). The woman in the scarf shields her eyes only at about 4.5-6.5 s. Reflector pill sits on the top of the white disc just above the actress's head. Key word filmmaking is not a visible noun."}
# ---------- 294
W={0.0:[0,0.14,0.40,0.54],0.5:[0,0.15,0.42,0.53],1.0:[0,0.16,0.43,0.52],1.5:[0,0.16,0.42,0.47],2.0:[0,0.13,0.47,0.46],2.5:[0,0.12,0.47,0.46],3.0:[0,0.15,0.47,0.44],3.5:[0,0.15,0.41,0.47],4.0:[0,0.13,0.41,0.50],4.5:[0,0.16,0.41,0.48],5.0:[0,0.27,0.44,0.47],5.5:[0,0.34,0.40,0.46],6.0:[0,0.40,0.38,0.45],6.5:[0,0.47,0.36,0.45],7.0:[0,0.50,0.36,0.46],7.5:[0,0.52,0.36,0.46],8.0:[0,0.50,0.35,0.42],8.5:[0,0.47,0.36,0.42],9.0:[0,0.47,0.36,0.42],9.5:[0,0.44,0.37,0.42],10.0:[0,0.41,0.38,0.40]}
M={0.0:[0.50,0.08,0.50,0.39],0.5:[0.66,0.08,0.34,0.50],1.0:[0.62,0.12,0.38,0.53],1.5:[0.58,0.13,0.42,0.48],2.0:[0.60,0.08,0.40,0.46],2.5:[0.60,0.09,0.40,0.46],3.0:[0.60,0.10,0.40,0.46],3.5:[0.60,0.10,0.40,0.45],4.0:[0.63,0.12,0.37,0.43],4.5:[0.63,0.15,0.37,0.43],5.0:[0.63,0.19,0.37,0.55],5.5:[0.64,0.28,0.36,0.52],6.0:[0.64,0.37,0.36,0.48],6.5:[0.62,0.43,0.38,0.47],7.0:[0.66,0.58,0.34,0.38],7.5:[0.66,0.59,0.34,0.39],8.0:[0.66,0.47,0.34,0.40],8.5:[0.66,0.44,0.34,0.42],9.0:[0.66,0.52,0.34,0.36],9.5:[0.69,0.49,0.31,0.38],10.0:[0.66,0.37,0.34,0.40]}
F={0.0:[0.41,0.47,0.40,0.42],0.5:[0.43,0.37,0.23,0.50],1.0:[0.43,0.34,0.19,0.55],1.5:[0.43,0.62,0.40,0.27],2.0:[0.38,0.59,0.44,0.30],2.5:[0.38,0.58,0.44,0.30],3.0:[0.38,0.59,0.44,0.30],3.5:[0.42,0.56,0.40,0.33],4.0:[0.42,0.55,0.42,0.34],4.5:[0.42,0.58,0.42,0.33],5.0:[0.38,0.75,0.42,0.25],5.5:[0.36,0.81,0.42,0.19],6.0:[0.39,0.70,0.24,0.30],6.5:[0.38,0.72,0.23,0.28],7.0:[0.37,0.84,0.28,0.16],7.5:[0.37,0.85,0.28,0.15],8.0:[0.36,0.74,0.29,0.26],8.5:[0.37,0.68,0.28,0.32],9.0:[0.37,0.72,0.28,0.28],9.5:[0.38,0.69,0.30,0.31],10.0:[0.39,0.67,0.27,0.28]}
C[294]={"mediaId":294,"level":"A","keyWord":"fire","defaultVoice":"female",
"taps":[{"phrase":"to hold a long stick","target":"the woman","voice":"female","keys":keys(t,W)},
{"phrase":"to put wood on the fire","target":"the man","voice":"male","keys":keys(t,M)},
{"phrase":"to burn between the stones","target":"the fire","voice":"female","keys":keys(t,F)}],
"stillS":3.0,
"nouns":[{"word":"trees","x":0.35,"y":0.12,"voice":"female"},{"word":"a man","x":0.80,"y":0.35,"voice":"male"},{"word":"a fire","x":0.50,"y":0.72,"voice":"female"},{"word":"stones","x":0.50,"y":0.93,"voice":"female"}],
"question":"What is the man doing?",
"answer":["He","is","putting","wood","on","the","fire."],"answerVoice":"male",
"notes":"The man puts the log on only at 0.0-1.5 s. Fire box is cut where the man's arm or the woman's stick reaches over the flames (0.5-1.5 s the box follows the tall flame and standing log, not the whole fire ring). Mixed couple -> default voice by evenId."}
# ---------- 295
t25=T(25)
H={0.0:[0.45,0.34,0.55,0.32],0.5:[0.17,0.43,0.83,0.45],1.0:[0.50,0.67,0.50,0.23],1.5:[0.33,0.28,0.67,0.72],2.0:[0.66,0.38,0.34,0.24],2.5:[0.26,0.29,0.74,0.71],3.0:[0.30,0.50,0.70,0.26],3.5:[0.61,0.49,0.39,0.24],4.0:[0.30,0.27,0.70,0.29],4.5:[0.33,0.23,0.67,0.28],5.0:[0.16,0.48,0.84,0.48],5.5:[0.63,0.46,0.37,0.33],6.0:[0.14,0.46,0.86,0.54],6.5:[0.34,0.61,0.66,0.33],7.0:[0.53,0.53,0.47,0.25],7.5:[0.68,0.41,0.32,0.25],8.0:[0.43,0.31,0.57,0.63],8.5:[0.26,0.36,0.74,0.64],9.0:[0.41,0.46,0.59,0.54],9.5:[0.23,0.56,0.77,0.36],10.0:[0.66,0.40,0.34,0.60],10.5:[0.09,0.43,0.91,0.31],11.0:[0.50,0.34,0.50,0.28],11.5:[0.48,0.58,0.52,0.26]}
TP={x:[0.10,0.0,0.84,0.21] for x in t25}
TP[8.5]=[0.10,0.0,0.84,0.25];TP[10.0]=[0.10,0.0,0.84,0.23];TP[12.0]=[0.10,0.0,0.84,0.24]
C[295]={"mediaId":295,"level":"A","keyWord":"mix","defaultVoice":"male",
"taps":[{"phrase":"to mix the grey paste","target":"the hand","voice":"male","keys":keys(t25,H)},
{"phrase":"to hold a black handle","target":"the hand","voice":"male","keys":keys(t25,H)},
{"phrase":"to stick to the floor","target":"the blue tape","voice":"male","keys":keys(t25,TP)}],
"stillS":3.0,
"nouns":[{"word":"tape","x":0.58,"y":0.12,"voice":"male"},{"word":"a bucket","x":0.38,"y":0.27,"voice":"male"},{"word":"a hand","x":0.78,"y":0.62,"voice":"male"},{"word":"a shoe","x":0.22,"y":0.92,"voice":"male"}],
"question":"What is the hand doing?",
"answer":["The","hand","is","mixing","the","grey","paste."],"answerVoice":"male",
"notes":"First-person clip: only a hand with a tool, a bucket, two shoes and tape are visible. The bucket could not be a tap target because the hand is always inside it; hand box = hand + tool, off at 12.0 s (only the blade is in the picture). 'paste' is the simplest fitting word (A2/B1); the paste is blue-grey. 'a shoe' pill sits on the left shoe; there is a second shoe at the right bottom. Hand's gender unknown -> default voice by evenId (male)."}
# ---------- 296
MA={0.0:[0.82,0.33,0.18,0.18],0.5:[0.81,0.36,0.19,0.22],1.0:[0.82,0.31,0.18,0.16],2.0:[0.38,0.08,0.62,0.37],2.5:[0.36,0.0,0.64,0.40],3.0:[0.0,0.03,1.0,0.50],3.5:[0.0,0.0,1.0,0.52],4.0:[0.0,0.0,1.0,0.49],4.5:[0.42,0.0,0.58,0.48],5.0:[0.10,0.0,0.90,0.57]}
WO={5.5:[0.0,0.0,1.0,0.56],6.0:[0.0,0.0,1.0,0.50],6.5:[0.0,0.0,1.0,0.53],7.0:[0.0,0.0,1.0,0.71],7.5:[0.0,0.0,1.0,0.76],8.0:[0.0,0.0,1.0,0.66],8.5:[0.0,0.0,1.0,0.66],9.0:[0.25,0.02,0.67,0.42]}
FI={0.0:[0.08,0.39,0.74,0.26],0.5:[0.07,0.47,0.74,0.28],1.0:[0.03,0.30,0.79,0.50],1.5:[0.04,0.35,0.96,0.32],2.0:[0.0,0.45,1.0,0.31],2.5:[0.0,0.40,1.0,0.36],3.0:[0.03,0.53,0.97,0.32],3.5:[0.0,0.52,1.0,0.37],4.0:[0.0,0.49,1.0,0.43],4.5:[0.03,0.48,0.90,0.30],5.0:[0.0,0.58,0.92,0.24],5.5:[0.0,0.56,1.0,0.33],6.0:[0.0,0.50,1.0,0.30],6.5:[0.0,0.54,1.0,0.30],7.0:[0.0,0.72,1.0,0.27],7.5:[0.0,0.77,1.0,0.23],8.0:[0.0,0.67,1.0,0.28],8.5:[0.0,0.67,1.0,0.28],9.0:[0.0,0.45,1.0,0.55],9.5:[0.0,0.44,1.0,0.23],10.0:[0.0,0.46,1.0,0.24]}
C[296]={"mediaId":296,"level":"A","keyWord":"fish","defaultVoice":"female",
"taps":[{"phrase":"to hold half a lemon","target":"the man","voice":"male","keys":keys(t,MA)},
{"phrase":"to eat with a fork","target":"the woman","voice":"female","keys":keys(t,WO)},
{"phrase":"to cook over the fire","target":"the fish","voice":"female","keys":keys(t,FI)}],
"stillS":0.0,
"nouns":[{"word":"the sea","x":0.65,"y":0.16,"voice":"female"},{"word":"a boat","x":0.50,"y":0.25,"voice":"female"},{"word":"a fish","x":0.45,"y":0.51,"voice":"female"},{"word":"a fire","x":0.47,"y":0.74,"voice":"female"}],
"question":"What is the woman eating?",
"answer":["She","is","eating","fish","with","a","fork."],"answerVoice":"female",
"notes":"Many cuts. At 0.0-2.5 s only the man's hand/arm is in the picture (boxed as the man; off at 1.5). 9.0 s is a dissolve (ghost woman + two ghost fish). Fish box = fish in its wire basket; the fish is over the fire only until about 4.0 s, afterwards it lies on a board. The woman's fork piece above the fish belongs to the woman's box. Mixed couple -> default voice by evenId."}
import sys
for i in C:
    json.dump(C[i],open(f"content/{i}.json","w"),ensure_ascii=False,indent=1)
