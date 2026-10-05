import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(d): return [dict(t=t,x=round(d[t][0],2),y=round(d[t][1],2),w=round(d[t][2]-d[t][0],2),h=round(d[t][3]-d[t][1],2)) for t in T]
fox={0.2:(.03,.05,.40,.20),0.7:(.09,.04,.41,.21),1.2:(.02,.04,.40,.20),1.7:(.03,.04,.40,.21),2.2:(.02,.03,.41,.20),2.7:(.02,.03,.46,.20),3.2:(.05,.03,.51,.22),3.7:(.06,.03,.54,.23)}
bad={t:(.28,.44,.46,.58) for t in T}
clump={0.2:(.50,.38,.82,.61),0.7:(.58,.56,.90,.74),1.2:(.66,.60,.98,.77),1.7:(.67,.61,.98,.78),2.2:(.65,.60,.95,.77),2.7:(.68,.61,.97,.77),3.2:(.65,.61,.96,.78),3.7:(.68,.61,.97,.78)}
c=dict(mediaId=7198,level="B",keyWord="ground",defaultVoice="female",
 taps=[dict(phrase="to peer over the edge",target="the fox",voice="female",keys=k(fox)),
       dict(phrase="to peek from a burrow",target="the badger",voice="female",keys=k(bad)),
       dict(phrase="to break off the bank",target="the clump of earth",voice="female",keys=k(clump))],
 stillS=2.7,
 nouns=[dict(word="a fox",x=.24,y=.12,voice="female"),dict(word="ground",x=.22,y=.30,voice="female"),
        dict(word="a badger",x=.39,y=.51,voice="female"),dict(word="a plough",x=.75,y=.81,voice="female")],
 question="What is the fox doing?",answer=["It","is","peering","over","the","edge."],answerVoice="female",
 notes="Clump box follows the big falling lump of earth until it lies on the pile (lower right). 'ground' pill sits on the dark earth of the bank; could be read as soil.")
json.dump(c,open('content/7198.json','w'),indent=1)
