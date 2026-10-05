import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
P=K([(0.0,0.26,0.27,0.34,0.45),(0.5,0.23,0.28,0.38,0.52),(1.0,0.29,0.25,0.37,0.67),(1.5,0.29,0.27,0.43,0.72),
(2.0,0.41,0.37,0.41,0.46),(2.5,0.18,0.56,0.82,0.25),(3.0,0.33,0.52,0.67,0.23),(3.5,0.44,0.52,0.56,0.23),(4.0,0.43,0.50,0.57,0.28),
(4.5,0.44,0.45,0.56,0.31),(5.0,0.44,0.48,0.56,0.31),(5.5,0.45,0.42,0.55,0.37),(6.0,0.44,0.44,0.56,0.36),(6.5,0.44,0.44,0.56,0.36),
(7.0,0.44,0.43,0.56,0.36),(7.5,0.44,0.41,0.56,0.38),(8.0,0.44,0.40,0.56,0.40),(8.5,0.43,0.40,0.57,0.40),(9.0,0.42,0.42,0.58,0.36)])
T=K([(0.0,),(0.5,),(1.0,),(1.5,),(2.0,),(2.5,),(3.0,0,0.16,0.33,0.54),(3.5,0,0.23,0.44,0.49),(4.0,0,0.22,0.43,0.45),
(4.5,0,0.17,0.44,0.50),(5.0,0,0.16,0.44,0.52),(5.5,0,0.14,0.45,0.55),(6.0,0,0.14,0.44,0.54),(6.5,0,0.13,0.44,0.55),
(7.0,0,0.14,0.44,0.57),(7.5,0,0.12,0.44,0.57),(8.0,0,0.13,0.44,0.55),(8.5,0,0.12,0.43,0.54),(9.0,0,0.13,0.42,0.57)])
S=K([(0.0,),(0.5,),(1.0,0.68,0.29,0.18,0.22),(1.5,),(2.0,0.22,0.23,0.18,0.21),(2.5,0.29,0.21,0.18,0.22),(3.0,0.34,0.17,0.18,0.22),
(3.5,0.48,0.14,0.18,0.22),(4.0,0.54,0.14,0.18,0.22),(4.5,0.60,0.14,0.18,0.23),(5.0,0.69,0.17,0.18,0.22),(5.5,0.71,0.17,0.18,0.22),
(6.0,0.72,0.18,0.19,0.22),(6.5,0.72,0.18,0.20,0.22),(7.0,0.71,0.17,0.20,0.23),(7.5,0.74,0.17,0.19,0.23),(8.0,0.73,0.17,0.19,0.22),
(8.5,0.73,0.18,0.19,0.21),(9.0,0.68,0.17,0.20,0.23)])
d={"mediaId":4583,"level":"B","keyWord":"calf","defaultVoice":"male",
"taps":[
 {"phrase":"to clutch his calf","target":"the player in light blue","voice":"male","keys":P},
 {"phrase":"to stretch the player's leg","target":"the man in the vest","voice":"male","keys":T},
 {"phrase":"to watch from a distance","target":"the player in stripes","voice":"male","keys":S}],
"stillS":8.0,
"nouns":[{"word":"floodlights","x":0.52,"y":0.06,"voice":"male"},{"word":"a vest","x":0.20,"y":0.32,"voice":"male"},
 {"word":"a calf","x":0.22,"y":0.55,"voice":"male"},{"word":"a fist","x":0.80,"y":0.74,"voice":"male"}],
"question":"What is the kneeling man doing?",
"answer":["He","is","stretching","the","player's","calf."],
"answerVoice":"male",
"notes":"One take, the camera moves. The player in light blue grabs his knee/leg at 1-2 s and holds the back of his lower leg on the ground at 2.5-4 s (the clutching), after that the man in the grey vest holds the leg up and pushes the foot back. Boxes: from 3 s the vest man is on the left and bends over / holds the player's lower leg in front of himself, so the two boxes are split by a vertical line (x 0.33 at 3.0, then about 0.44) - the player's feet and the held lower leg lie inside the vest man's box, the player's box holds his trunk, head and arms. At 2.0 the player's box leaves out the tip of his back foot to stay clear of the striped player's box. The player in stripes = the team-mate standing in the background (dark blue and light blue stripes), from 5 s with hands on hips; small, so minimum-size boxes; not visible at 0, 0.5 and 1.5 s. Doubt: at 0-1 s two other people stand far back (a yellow bib, a pale blue kit) for a moment; they are not boxed. 'a calf' pill sits on the bare lower leg held up by the vest man."}
json.dump(d,open("content/4583.json","w"),indent=1,ensure_ascii=False)
