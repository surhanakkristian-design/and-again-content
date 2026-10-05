import json
times=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in times:
        if t in d:
            x1,y1,x2,y2=d[t]; out.append({"t":t,"x":round(x1,2),"y":round(y1,2),"w":round(x2-x1,2),"h":round(y2-y1,2)})
        else: out.append({"t":t,"off":True})
    return out
# left man: (top, right edge); middle man: (left, top, right). Men's boxes end at y .53, the box on the table starts at .54
Lr={0.0:(.11,.40),0.5:(.09,.43),1.0:(.07,.38),1.5:(.07,.33),2.0:(.28,.29),2.5:(.28,.29),3.0:(.29,.29),3.5:(.29,.30),4.0:(.27,.29),4.5:(.27,.28),
5.0:(.28,.28),5.5:(.28,.27),6.0:(.27,.26),6.5:(.27,.25),7.0:(.28,.21),7.5:(.28,.21),8.0:(.28,.20),8.5:(.28,.20),9.0:(.29,.30),9.5:(.28,.27),
10.0:(.27,.31),10.5:(.16,.34),11.0:(.09,.41),11.5:(.09,.40),12.0:(.08,.36),12.5:(.28,.32),13.0:(.28,.30),13.5:(.30,.28),14.0:(.30,.26),14.5:(.30,.28),15.0:(.31,.28)}
Mr={0.0:(.41,.28,.73),0.5:(.44,.30,.73),1.0:(.39,.28,.73),1.5:(.34,.30,.73),2.0:(.30,.29,.70),2.5:(.30,.29,.72),3.0:(.30,.28,.71),3.5:(.31,.28,.72),
4.0:(.30,.27,.73),4.5:(.29,.27,.73),5.0:(.29,.28,.74),5.5:(.28,.28,.80),6.0:(.27,.26,.76),6.5:(.26,.25,.81),7.0:(.22,.24,.82),7.5:(.22,.17,.85),
8.0:(.21,.07,.84),8.5:(.21,.05,.85),9.0:(.31,.04,.74),9.5:(.28,.27,.84),10.0:(.32,.25,.73),10.5:(.35,.26,.73),11.0:(.42,.28,.73),11.5:(.41,.29,.73),
12.0:(.37,.28,.72),12.5:(.33,.28,.72),13.0:(.31,.27,.72),13.5:(.29,.29,.74),14.0:(.27,.26,.74),14.5:(.29,.23,.74),15.0:(.29,.29,.75)}
L={t:(0,a,b,.53) for t,(a,b) in Lr.items()}
M={t:(a,b,c,.53) for t,(a,b,c) in Mr.items()}
T={t:(.19,.54,.92,.77) for t in times}
def inter(a,b): return min(a[2],b[2])-max(a[0],b[0])>0.001 and min(a[3],b[3])-max(a[1],b[1])>0.001
for t in times:
    for n1,n2,a,b in (("L","M",L,M),("L","T",L,T),("M","T",M,T)):
        if inter(a[t],b[t]): print("OVERLAP",t,n1,n2,a[t],b[t])
c={"mediaId":4032,"level":"B","keyWord":"mess","defaultVoice":"male",
"taps":[
 {"phrase":"to tip out the slime","target":"the man on the left","voice":"male","keys":keys(L)},
 {"phrase":"to get covered in slime","target":"the man in the middle","voice":"male","keys":keys(M)},
 {"phrase":"to catch the dripping slime","target":"the big box","voice":"male","keys":keys(T)}],
"stillS":12.5,
"nouns":[{"word":"a sleep mask","x":0.86,"y":0.36,"voice":"male"},
 {"word":"slime","x":0.53,"y":0.46,"voice":"male"},
 {"word":"a plastic box","x":0.70,"y":0.59,"voice":"male"},
 {"word":"a table","x":0.30,"y":0.77,"voice":"male"}],
"question":"What are the three men making?",
"answer":["They","are","making","a","mess","with","slime."],
"answerVoice":"male",
"notes":"Key word 'a mess' is not one clear place, so it is in the answer, not a noun slot. All three men sit behind the big box: every man's box ends at the box's upper rim (y .53) and the box's box starts there, so the men's forearms and hands on the table are outside their boxes. While the left man tips the tub (0-1.5 s, 10.5-12 s) his arms and the tub reach over the middle man: split by a vertical line at his reaching arm. 7.0-8.5 s: the middle man's raised left arm is in front of the left man's shoulder. The clip repeats from 10.0 s (second pour). Two sleep masks are visible in the still (left and right man); the slot is on the right man's mask and no other noun is on the left one. The left man's smaller tub stands on the table edge from 3.0 s, hence the target name 'the big box' for the box in the middle."}
json.dump(c,open("content/4032.json","w"),indent=1)
