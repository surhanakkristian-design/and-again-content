import json
T=[i*0.5 for i in range(19)]
N=None
H={0:N,0.5:N,1:N,1.5:N,2:N,2.5:(0.48,0.32,0.52,0.68),3:(0.28,0.29,0.72,0.71),3.5:(0.18,0.15,0.68,0.67),4:(0.12,0.18,0.73,0.68),
4.5:(0.24,0.30,0.50,0.33),5:(0.23,0.30,0.52,0.33),5.5:N,6:N,6.5:(0.44,0.08,0.56,0.47),7:(0.47,0.07,0.53,0.46),7.5:(0,0,1.0,1.0),8:N,8.5:N,9:N}
P={0:N,0.5:N,1:(0.48,0.61,0.19,0.20),1.5:(0.18,0.64,0.26,0.24),2:(0,0.24,0.32,0.56),2.5:(0,0.21,0.27,0.57),3:(0,0.22,0.27,0.48),3.5:N,4:N,4.5:N,5:N,5.5:N,
6:(0,0.31,0.40,0.56),6.5:N,7:N,7.5:N,8:(0,0.32,0.32,0.66),8.5:(0,0.27,0.37,0.73),9:(0,0.29,0.37,0.71)}
B={0:N,0.5:N,1:(0.68,0.61,0.18,0.20),1.5:(0.45,0.63,0.18,0.20),2:(0.33,0.29,0.36,0.51),2.5:(0.28,0.27,0.19,0.48),3:N,3.5:N,4:N,4.5:N,5:N,5.5:N,
6:(0.41,0.32,0.26,0.53),6.5:N,7:N,7.5:N,8:(0.33,0.31,0.35,0.58),8.5:(0.38,0.28,0.28,0.57),9:(0.38,0.31,0.29,0.62)}
def keys(d): return [dict(t=t,off=True) if d[t] is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c=dict(mediaId=4919,level="B",keyWord="membership",defaultVoice="female",
 taps=[dict(phrase="to sign a membership form",target="the woman in the white hoodie",voice="female",keys=keys(H)),
       dict(phrase="to stick his tongue out",target="the man in the checked shirt",voice="male",keys=keys(P)),
       dict(phrase="to wear a denim jacket",target="the blonde woman",voice="female",keys=keys(B))],
 stillS=2.0,
 nouns=[dict(word="bunting",x=0.22,y=0.21,voice="female"),dict(word="a banner",x=0.66,y=0.13,voice="female"),
        dict(word="a denim jacket",x=0.50,y=0.56,voice="female"),dict(word="a clipboard",x=0.32,y=0.86,voice="female")],
 question="What are the three students doing?",answer=["They","are","raising","their","cameras","over","their","heads."],answerVoice="female",
 notes="Many cuts. Signing is shown only as a close-up hand with a white sleeve (6.5-7.0 s), taken to be the newcomer in the white hoodie; 7.5 s is a close-up of her hoodie (box = whole frame). Tongue out only at 6.0 s. defaultVoice female = the newcomer is the main person. 'denim jacket' is a state: the blonde has no action of her own. Question refers to the end (8.0-9.0 s).")
json.dump(c,open('content/4919.json','w'),indent=1)
