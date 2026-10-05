import json
times=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in times:
        if t in d:
            x1,y1,x2,y2=d[t]; out.append({"t":t,"x":round(x1,2),"y":round(y1,2),"w":round(x2-x1,2),"h":round(y2-y1,2)})
        else: out.append({"t":t,"off":True})
    return out
Bc={0.0:(.73,.15,1.0,.34),0.5:(.60,.29,.80,.45),1.0:(.37,.34,.50,.46),1.5:(.19,.29,.32,.40),2.0:(.13,.29,.27,.40),2.5:(.30,.35,.43,.46),
3.0:(.59,.32,.75,.46),3.5:(.73,.26,.97,.41),4.0:(.58,.30,.76,.46),4.5:(.32,.34,.46,.47),5.0:(.13,.32,.27,.43),5.5:(.13,.30,.27,.41),
6.0:(.32,.35,.45,.47),6.5:(.62,.33,.79,.47),7.0:(.77,.27,.99,.43),7.5:(.60,.33,.78,.47),8.0:(.35,.36,.50,.46),8.5:(.15,.33,.29,.44),
9.0:(.05,.29,.18,.41),9.5:(.04,.30,.18,.41),10.0:(.15,.33,.27,.45),10.5:(.41,.37,.55,.48),11.0:(.66,.34,.81,.47),11.5:(.68,.34,.86,.47),
12.0:(.46,.37,.60,.49),12.5:(.20,.36,.34,.46),13.0:(.05,.32,.20,.45),13.5:(.16,.35,.30,.46),14.0:(.40,.37,.54,.49),14.5:(.63,.33,.82,.47),15.0:(.61,.31,.80,.47)}
B={t:(max(0,a-.03),max(0,b-.03),min(1,c+.03),d+.03) for t,(a,b,c,d) in Bc.items()}
# overrides (x1,y1,x2,y2) where the bottle is close to a man
def ov(t,**k):
    a=list(B[t])
    for n,v in k.items(): a["x1 y1 x2 y2".split().index(n)]=v
    B[t]=tuple(a)
ov(0.0,y2=.34); ov(0.5,x2=.80,y2=.45); ov(1.0,x2=.51); ov(3.0,x2=.74,y2=.45); ov(3.5,y2=.41); ov(4.0,x2=.74,y2=.45)
ov(4.5,x2=.48); ov(6.0,x2=.47); ov(6.5,x2=.78,y2=.47); ov(7.0,y2=.43); ov(7.5,x2=.78,y2=.47); ov(8.0,x2=.52)
ov(10.5,x2=.55); ov(11.0,x2=.81,y2=.49); ov(11.5,y2=.47); ov(12.0,x2=.60,y2=.49); ov(14.0,x2=.55); ov(14.5,x2=.82,y2=.46); ov(15.0,x2=.80,y2=.46)
N={t:(.51,.41,.74,.70) for t in times if t<8}
N.update({0.0:(.50,.38,.74,.70),0.5:(.50,.46,.76,.70),3.0:(.50,.46,.74,.70),4.0:(.50,.46,.74,.70),5.0:(.49,.40,.74,.70),6.0:(.49,.40,.74,.70),
6.5:(.49,.48,.75,.70),7.0:(.49,.41,.72,.70),7.5:(.47,.48,.74,.70),
8.0:(.48,.49,.70,.66),8.5:(.50,.38,.72,.64),9.0:(.50,.38,.71,.64),9.5:(.50,.38,.72,.64),10.0:(.50,.38,.72,.64),10.5:(.56,.39,.73,.64),
11.0:(.50,.50,.81,.64),11.5:(.53,.48,.77,.68),12.0:(.52,.50,.73,.68),12.5:(.54,.46,.77,.69),13.0:(.50,.47,.71,.69),13.5:(.52,.47,.73,.69),
14.0:(.56,.45,.72,.69),14.5:(.52,.47,.82,.69),15.0:(.53,.47,.80,.69)})
S={t:(.75,.36,.96,.65) for t in times if t<8}
S.update({0.5:(.81,.35,.97,.64),3.5:(.75,.42,.96,.65),6.5:(.79,.36,.96,.65),7.0:(.73,.44,.95,.65),7.5:(.79,.36,.96,.65),
8.0:(.71,.36,.95,.65),8.5:(.73,.36,.96,.65),9.0:(.72,.36,.96,.65),9.5:(.73,.36,.97,.65),10.0:(.73,.36,.97,.65),10.5:(.74,.36,.98,.65),
11.0:(.82,.36,.97,.74),11.5:(.78,.48,.97,.66),12.0:(.74,.39,.96,.60),12.5:(.78,.39,.97,.60),13.0:(.72,.39,.95,.61),13.5:(.74,.39,.96,.61),
14.0:(.73,.36,.95,.62),14.5:(.83,.36,.97,.63),15.0:(.81,.36,.96,.64)})
def inter(a,b): return min(a[2],b[2])-max(a[0],b[0])>0.001 and min(a[3],b[3])-max(a[1],b[1])>0.001
for t in times:
    for n1,n2,a,b in (("B","N",B,N),("B","S",B,S),("N","S",N,S)):
        if inter(a[t],b[t]): print("OVERLAP",t,n1,n2,a[t],b[t])
c={"mediaId":4029,"level":"B","keyWord":"knock","defaultVoice":"male",
"taps":[
 {"phrase":"to swing on a rope","target":"the water bottle","voice":"male","keys":keys(B)},
 {"phrase":"to get knocked over backwards","target":"the man in the navy shirt","voice":"male","keys":keys(N)},
 {"phrase":"to watch without a blindfold","target":"the man with no shirt","voice":"male","keys":keys(S)}],
"stillS":2.0,
"nouns":[{"word":"a rope","x":0.31,"y":0.12,"voice":"male"},
 {"word":"a water bottle","x":0.21,"y":0.34,"voice":"male"},
 {"word":"blindfolds","x":0.44,"y":0.46,"voice":"male"},
 {"word":"dry leaves","x":0.50,"y":0.80,"voice":"male"}],
"question":"What does the water bottle do?",
"answer":["It","knocks","a","man","off","his","seat."],
"answerVoice":"male",
"notes":"Bottle passes in front of the navy-shirt man's head (0.5, 3.0, 4.0, 6.5, 7.5 s) and the shirtless man's head (3.5, 7.0, 11.5 s): boxes split along the bottle's lower edge, so those men's boxes lose the head at those times. From 8.0 s the navy-shirt man lies / sits on the ground partly behind the man in red and with his legs in front of the shirtless man's block; split by a vertical line, his feet fall outside his box at 11.5-13.5 s. Question is in the present simple (one completed event, not an ongoing action)."}
json.dump(c,open("content/4029.json","w"),indent=1)
