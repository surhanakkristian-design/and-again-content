import json
W = [(0.0,0.46,0.90,0.54),(0.0,0.46,1.0,0.54),(0.08,0.46,0.92,0.54),(0.21,0.46,0.42,0.54),(0.18,0.45,0.67,0.55),
     (0.29,0.16,0.71,0.84),(0.29,0.17,0.71,0.83),(0.33,0.17,0.67,0.83),(0.31,0.18,0.69,0.82),(0.34,0.19,0.66,0.81),
     (0.33,0.20,0.67,0.80),(0.32,0.20,0.68,0.80),(0.32,0.18,0.68,0.82),(0.0,0.15,1.0,0.85),(0.0,0.14,1.0,0.86),
     (0.0,0.14,1.0,0.86),(0.03,0.15,0.97,0.85),(0.0,0.09,1.0,0.91),(0.0,0.09,1.0,0.91),(0.0,0.09,1.0,0.91),
     (0.0,0.08,1.0,0.92),(0.0,0.08,1.0,0.92),(0.0,0.06,1.0,0.94),(0.0,0.05,1.0,0.95),(0.0,0.0,1.0,1.0)]
def keys(L): return [dict(t=i*0.5,x=a,y=b,w=c,h=d) for i,(a,b,c,d) in enumerate(L)]
c = {"mediaId":5230,"level":"A","keyWord":"a doll","defaultVoice":"female",
 "taps":[
  {"phrase":"to drink hot tea","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to eat a bun","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to open a little doll","target":"the woman","voice":"female","keys":keys(W)}],
 "stillS":9.0,
 "nouns":[{"word":"lights","x":0.30,"y":0.07,"voice":"female"},
          {"word":"a hat","x":0.50,"y":0.22,"voice":"female"},
          {"word":"a doll","x":0.44,"y":0.58,"voice":"female"},
          {"word":"a coat","x":0.70,"y":0.82,"voice":"female"}],
 "question":"What is the woman opening?",
 "answer":["She","is","opening","a","little","doll."],
 "answerVoice":"female",
 "notes":"Only one real target (the woman) in three shots: square, train, market, so all three phrases use her. The description omits it, but at t=6.5-8.0 she eats a round fried bun/pie from a napkin ('to eat a bun'). 'to drink hot tea': holding the glass from 2.5, sipping 4.0-6.0. Small background people at the market are not targets."}
json.dump(c, open('content/5230.json','w'), indent=1)
