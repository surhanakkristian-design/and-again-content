import json,sys
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1)
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
if __name__=="__main__":
    woman=[(0.27,0.27,0.31,0.70),(0.27,0.27,0.31,0.70),(0.27,0.26,0.31,0.73),(0.26,0.25,0.32,0.74),
           (0.16,0.26,0.36,0.74),(0.11,0.28,0.42,0.72),(0.01,0.27,0.46,0.73),(0.08,0.25,0.48,0.75)]
    giraffe=[(0.58,0.14,0.41,0.24),(0.58,0.14,0.41,0.24),(0.58,0.12,0.41,0.27),(0.58,0.12,0.41,0.27),
             (0.52,0.11,0.47,0.26),(0.53,0.10,0.46,0.27),(0.68,0.02,0.31,0.28),None]
    cat=[(0.08,0.15,0.18,0.14),(0.08,0.15,0.18,0.14),(0.07,0.14,0.18,0.14),(0.07,0.13,0.18,0.14),
         (0.06,0.12,0.18,0.14),(0.04,0.11,0.18,0.15),(0.04,0.12,0.18,0.14),(0.03,0.10,0.19,0.14)]
    write({"mediaId":7297,"level":"B","keyWord":"live in","defaultVoice":"female",
     "taps":[{"phrase":"to clutch her toothbrush","target":"the woman","voice":"female","keys":K(T,woman)},
             {"phrase":"to poke its head indoors","target":"the giraffe","voice":"female","keys":K(T,giraffe)},
             {"phrase":"to perch on the wardrobe","target":"the cat","voice":"female","keys":K(T,cat)}],
     "stillS":0.2,
     "nouns":[{"word":"a giraffe","x":0.76,"y":0.25,"voice":"female"},
              {"word":"a uniform","x":0.16,"y":0.40,"voice":"female"},
              {"word":"pyjamas","x":0.42,"y":0.66,"voice":"female"},
              {"word":"a hen","x":0.66,"y":0.90,"voice":"female"}],
     "question":"What is the giraffe doing?",
     "answer":["It","is","poking","its","head","through","the","window."],
     "answerVoice":"female",
     "notes":"key word 'live in' is a phrasal verb, not visible as a noun; giraffe leaves frame at 3.7 (off). Woman box cut at the giraffe's snout where her hand touches it. 'a uniform' = zoo shirt hanging on the wardrobe."})
