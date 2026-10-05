import json
OFF=None
def keys(times, boxes):
    assert len(times)==len(boxes), (len(times),len(boxes))
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
t=[round(i*0.5,2) for i in range(21)]
B=[(0.31,0.30,0.38,0.58),(0.24,0.25,0.60,0.75),(0.10,0.70,0.90,0.30),OFF,OFF,(0.10,0,0.88,0.73),(0.03,0,0.66,0.86),
   (0.46,0,0.42,1.0),(0.34,0.35,0.30,0.48),(0.26,0.36,0.42,0.57),(0.08,0.59,0.62,0.41),(0,0.44,0.70,0.56),(0,0.14,0.69,0.86),
   (0.03,0.43,0.97,0.52),(0.03,0.46,0.97,0.52),(0.03,0.45,0.97,0.53),(0.05,0.48,0.95,0.50),(0.05,0.49,0.95,0.48),
   (0.80,0.28,0.20,0.57),(0.72,0.30,0.28,0.54),(0.57,0.39,0.18,0.18)]
R=[OFF,OFF,(0.33,0.37,0.30,0.22),(0.18,0.27,0.70,0.52),(0.16,0.25,0.63,0.40)]+[OFF]*16
H=[OFF]*13+[(0.06,0.12,0.30,0.29),(0.05,0.15,0.30,0.29),(0.06,0.14,0.30,0.29),(0.17,0.19,0.57,0.29),(0.17,0.19,0.60,0.30),
   (0.82,0.06,0.18,0.20),(0.80,0.08,0.20,0.19),OFF]
json.dump({"mediaId":393,"level":"B","keyWord":"hostel","defaultVoice":"male",
 "taps":[
  {"phrase":"to hand over a key","target":"the receptionist","voice":"female","keys":keys(t,R)},
  {"phrase":"to grip the wooden ladder","target":"the backpacker","voice":"male","keys":keys(t,B)},
  {"phrase":"to offer a bag of crisps","target":"the woman with red hair","voice":"female","keys":keys(t,H)}],
 "stillS":2.0,
 "nouns":[{"word":"a staircase","x":0.55,"y":0.28,"voice":"male"},{"word":"a receptionist","x":0.38,"y":0.52,"voice":"female"},
          {"word":"a desk","x":0.75,"y":0.70,"voice":"male"},{"word":"a key","x":0.30,"y":0.81,"voice":"male"}],
 "question":"What is the red-haired woman offering?",
 "answer":["She","is","offering","a","bag","of","crisps."],"answerVoice":"female",
 "notes":"Animated clip with many cuts. Key word 'hostel' is the whole place, not one visible thing, so not a noun. The backpacker's gender is not clear (short white-blond hair, denim jacket): target named 'the backpacker', voice = defaultVoice male (evenId false). Backpacker: 1.0 s only hand + backpack at the bottom, 2.5-3.5 s only the legs / boots climbing the stairs, 10.0 s tiny in the doorway; grips the ladder at 5.0-6.0. Receptionist only 1.0-2.0 (key held out at 1.5, on the desk at 2.0). Woman with red hair: 6.5-8.5 on the top bunk (crisps at 8.0-8.5), top right corner at 9.0-9.5; a red-haired figure at 3.5 s left and a red tuft at 4.0 s are left off (not surely her). Other travellers (bearded man with ukulele, man with dreadlocks reading, woman with shaved head) are not targets."},
 open("content/393.json","w"),indent=1,ensure_ascii=False)
