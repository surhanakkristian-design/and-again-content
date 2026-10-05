import json
B={0.0:(.38,.17,.50,.42),0.5:(.18,.15,.72,.45),1.0:(.25,.14,.65,.50),1.5:(.10,.12,.87,.50),2.0:(.28,.11,.66,.50),2.5:(.30,.11,.68,.50),
3.0:(.44,.13,.56,.50),7.0:(.28,.00,.52,.62),7.5:(.12,.00,.76,.64),8.0:(.10,.19,.80,.47),8.5:(.22,.05,.72,.66),9.0:(.20,.06,.66,.62)}
times=[i*0.5 for i in range(19)]
keys=[dict(t=t,x=B[t][0],y=B[t][1],w=B[t][2],h=B[t][3]) if t in B else dict(t=t,off=True) for t in times]
T="the fruit seller"
c=dict(mediaId=5252,level="B",keyWord="tropical",defaultVoice="female",
taps=[dict(phrase=p,target=T,voice="female",keys=keys) for p in ["to weigh ripe mangoes","to hand over a bag","to hold out a pineapple"]],
stillS=0.0,nouns=[dict(word="a straw hat",x=.63,y=.24,voice="female"),dict(word="a hanging scale",x=.28,y=.50,voice="female"),
dict(word="rambutans",x=.12,y=.60,voice="female"),dict(word="mangoes",x=.50,y=.78,voice="female")],
question="What is the street seller doing?",answer=["She","is","selling","tropical","fruit."],answerVoice="female",
notes="Seller visible 0.0-3.0 and 7.0-9.0; 3.5-6.5 are close-ups of customers, hands, dragon fruit, rambutans, coins and a pineapple pyramid, where the seller cannot be identified (off). Customers at 3.5-4.0 also wear straw hats, so no hat phrase. Only one stable target, so all three phrases are hers. 'to weigh ripe mangoes' 0.0-2.0 (mangoes on the scale pan); 'to hand over a bag' 2.5-3.0 (reaches out with the paper bag); 'to hold out a pineapple' 7.0-8.0. Box at 7.0/7.5 includes the pineapple in her raised hand.")
json.dump(c,open('content/5252.json','w'),indent=1)
