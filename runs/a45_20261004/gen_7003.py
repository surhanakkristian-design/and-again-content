import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
man=K([(0.17,0.50,0.70,0.30),(0.14,0.55,0.77,0.27),(0.09,0.54,0.84,0.28),(0.33,0.50,0.45,0.36),(0.31,0.46,0.44,0.45),(0.26,0.40,0.47,0.51),(0.26,0.38,0.47,0.58),(0.25,0.33,0.56,0.65)])
cr=K([(0.21,0.14,0.42,0.35),(0.24,0.31,0.37,0.23),None,None,None,None,None,None])
mk=K([None,None,None,(0.80,0.24,0.20,0.14),(0.80,0.24,0.20,0.14),(0.80,0.24,0.20,0.14),(0.80,0.24,0.20,0.14),(0.82,0.24,0.18,0.14)])
c={"mediaId":7003,"level":"B","keyWord":"cure","defaultVoice":"male",
"taps":[
 {"phrase":"to wade through the water","target":"the young man","voice":"male","keys":man},
 {"phrase":"to tumble through the air","target":"the crutches","voice":"male","keys":cr},
 {"phrase":"to perch on the roof","target":"the monkey on the roof","voice":"male","keys":mk}],
"stillS":2.7,
"nouns":[{"word":"a cliff","x":0.80,"y":0.12,"voice":"male"},
 {"word":"pine trees","x":0.15,"y":0.32,"voice":"male"},
 {"word":"steam","x":0.22,"y":0.43,"voice":"male"},
 {"word":"a bathhouse","x":0.90,"y":0.50,"voice":"male"}],
"question":"What is the young man doing?",
"answer":["He","is","wading","out","of","the","hot","spring."],
"answerVoice":"male",
"notes":"Crutches only at 0.2 and 0.7 (off afterwards); at 0.7 the crutch box stops at y 0.54 so it does not overlap the man's raised arms, the lower crutch tip (to y 0.65) is cut. Monkey on the bathhouse roof appears from 1.7; other monkeys sit on the snow by the bathhouse, so 'a monkey' is not a noun pill. Bathers behind also raise arms, so no phrase about cheering. Key word 'cure' (verb) is not a visible noun."}
json.dump(c,open('content/7003.json','w'),indent=1,ensure_ascii=False)
