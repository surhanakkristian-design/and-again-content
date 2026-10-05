import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
B=[(.44,.23,.53,.77),(.43,.24,.57,.76),(.32,.29,.60,.71),(.29,.31,.63,.69),(.06,.34,.30,.27),(.07,.34,.31,.27),(.07,.38,.34,.26),(.11,.38,.34,.28),(.14,.37,.30,.26),
   (.02,.07,.98,.93),(0,.17,.90,.83),(0,.39,.71,.61),(0,.57,.66,.43),(0,.59,.50,.41),(0,.63,.61,.37),(0,.63,.65,.37),(0,.61,.71,.39),(0,.61,.69,.39),(0,.63,.63,.37)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
W="the woman"
c=dict(mediaId=5383,level="B",keyWord="an avenue",defaultVoice="female",
 taps=[dict(phrase=p,target=W,voice="female",keys=keys) for p in ["to hail a yellow taxi","to pull a wheeled suitcase","to grin at the camera"]],
 stillS=0.0,
 nouns=[dict(word="an avenue",x=.80,y=.34,voice="female"),dict(word="a taxi",x=.22,y=.46,voice="female"),
        dict(word="a leopard-print coat",x=.70,y=.63,voice="female"),dict(word="a suitcase",x=.40,y=.94,voice="female")],
 question="What is the woman doing?",answer=["She","is","hailing","a","taxi","on","the","avenue."],answerVoice="female",
 notes="Only one person stands out; all three phrases target the woman. Many taxis, none singled out as a target. Shots 2.0-4.0 show her small at the kerb.")
json.dump(c,open('content/5383.json','w'),indent=1)
