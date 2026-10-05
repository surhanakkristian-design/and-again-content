import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
woman={2.0:(0,0.18,0.24,0.24),2.5:(0,0.04,0.34,0.76),3.0:(0,0.2,0.48,0.75),3.5:(0,0.28,0.40,0.72),4.0:(0,0.34,0.55,0.50),
 4.5:(0,0.31,0.32,0.41),5.0:(0,0.31,0.31,0.67),7.5:(0,0.28,0.18,0.40),8.0:(0,0.25,0.18,0.50),8.5:(0,0.29,0.24,0.50),
 9.0:(0,0.32,0.24,0.58),9.5:(0.02,0.34,0.25,0.58),10.0:(0,0.33,0.28,0.48)}
man={2.0:(0.80,0.06,0.20,0.24),2.5:(0.60,0.06,0.40,0.46),3.0:(0.62,0.18,0.38,0.50),3.5:(0.74,0.26,0.26,0.46),4.0:(0.55,0.33,0.45,0.32),
 4.5:(0.70,0.28,0.30,0.36),5.0:(0.50,0.31,0.50,0.36),7.0:(0.80,0.34,0.20,0.16),7.5:(0.74,0.33,0.26,0.30),8.0:(0.68,0.24,0.32,0.36),
 8.5:(0.72,0.27,0.28,0.34),9.0:(0.74,0.30,0.26,0.34),9.5:(0.72,0.30,0.28,0.37),10.0:(0.70,0.31,0.30,0.36)}
dog={4.0:(0,0.84,0.34,0.16),4.5:(0,0.72,0.64,0.28),5.0:(0.31,0.68,0.56,0.32),8.0:(0.82,0.60,0.18,0.16),8.5:(0.80,0.61,0.20,0.24),
 9.0:(0.78,0.64,0.22,0.32),9.5:(0.78,0.67,0.22,0.31),10.0:(0.77,0.67,0.23,0.23)}
c={"mediaId":860,"level":"A","keyWord":"washing","defaultVoice":"female",
"taps":[
 {"phrase":"to wear blue jeans","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to hold a yellow sponge","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to walk around the car","target":"the dog","voice":"female","keys":keys(dog)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":0.5,"y":0.15,"voice":"female"},{"word":"a car","x":0.5,"y":0.55,"voice":"female"},
 {"word":"a dog","x":0.88,"y":0.74,"voice":"female"},{"word":"a bucket","x":0.10,"y":0.79,"voice":"female"}],
"question":"What are the man and woman doing?",
"answer":["They","are","washing","the","car","with","sponges."],
"answerVoice":"female",
"notes":"Woman phrase is a state (both people wash the car, so no action fits only her; the man wears shorts). At 2.0, 7.0, 7.5 only arms / an edge strip of the people are visible; boxes sit on those parts. The hand with the hose at 5.5-6.5 cannot be attributed, so both are off. The dog mostly walks in front of / beside the car; 'around' follows the description. Bucket is at the left edge, pill at x 0.10."}
json.dump(c,open("content/860.json","w"),indent=1)
