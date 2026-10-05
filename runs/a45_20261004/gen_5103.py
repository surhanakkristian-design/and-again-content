import json
T=[i*0.5 for i in range(19)]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        out.append({"t":t,"off":True} if r is None else dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]))
    return out
woman=[(0,.17,1,.83),(0,.1,1,.9),(0,.12,1,.88),(0,.11,1,.89),(0,.15,1,.85),(0,.13,1,.87),
 (0,0,1,1),(0,0,1,1),(0,0,1,1),(0,0,1,1),(0,0,1,1),
 (0,.46,.52,.54),(0,.46,.52,.54),(0,.47,.52,.53),(0,.49,.5,.51),(0,.5,.5,.5),(.01,.48,.44,.52),(.01,.48,.45,.52),(0,.48,.44,.52)]
gir=[None]*11+[(.4,0,.45,.4),(.4,0,.58,.42),(.42,0,.58,.45),(.42,0,.58,.48),(.42,0,.58,.49),(.46,0,.52,.56),(.47,0,.51,.6),(.45,0,.53,.66)]
d={"mediaId":5103,"level":"A","keyWord":"neck","defaultVoice":"female",
"taps":[
 {"phrase":"to touch her neck","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to tie a scarf","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to bend its long neck","target":"the giraffe","voice":"female","keys":K(gir)}],
"stillS":7.0,
"nouns":[{"word":"a neck","x":0.80,"y":0.12,"voice":"female"},
 {"word":"trees","x":0.14,"y":0.30,"voice":"female"},
 {"word":"a scarf","x":0.18,"y":0.84,"voice":"female"},
 {"word":"a fence","x":0.76,"y":0.86,"voice":"female"}],
"question":"What is the giraffe doing?",
"answer":["It","is","bending","its","long","neck."],
"answerVoice":"female",
"notes":"Cuts: office 0-2.5, scarf close-up 3.0-5.0 (woman fills frame), crossfade at 5.5, park 6.0-9.0. Woman and giraffe boxes split along y/x where the giraffe head comes down near her (7.5-9.0). 'a neck' pill is on the giraffe's neck; the woman's neck is hidden by the scarf at 7.0."}
json.dump(d,open("content/5103.json","w"),indent=1)
