import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True}); continue
        x,y,w,h=b; w=min(w,1-x); h=min(h,1-y)
        out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
boy=keys({0.0:(0,0.23,0.7,0.43),0.5:(0,0.23,0.72,0.43),1.0:(0,0.23,0.72,0.43),5.5:(0,0.27,0.22,0.26),
 6.0:(0,0.29,0.31,0.27),6.5:(0,0.3,0.36,0.27),7.0:(0,0.32,0.39,0.26),7.5:(0,0.32,0.38,0.27),
 8.0:(0.03,0.37,0.27,0.15),8.5:(0.05,0.37,0.24,0.15),9.0:(0.05,0.38,0.23,0.15),9.5:(0.03,0.38,0.25,0.15),10.0:(0.02,0.38,0.26,0.14)})
girl=keys({3.0:(0.82,0.38,0.18,0.4),3.5:(0,0.38,0.18,0.22),4.0:(0,0.26,0.37,0.37),4.5:(0.12,0.26,0.44,0.38),
 5.0:(0.29,0.26,0.44,0.41),5.5:(0.43,0.26,0.45,0.4),6.0:(0.52,0.27,0.46,0.43),6.5:(0.54,0.27,0.46,0.43),
 7.0:(0.6,0.29,0.4,0.41),7.5:(0.6,0.3,0.4,0.4),
 8.0:(0.3,0.41,0.19,0.14),8.5:(0.3,0.4,0.18,0.15),9.0:(0.28,0.41,0.19,0.15),9.5:(0.28,0.41,0.19,0.15),10.0:(0.28,0.42,0.19,0.14)})
wom=keys({4.5:(0,0.28,0.12,0.28),5.0:(0.1,0.28,0.18,0.28),5.5:(0.23,0.28,0.2,0.26),6.0:(0.31,0.28,0.21,0.27),6.5:(0.36,0.28,0.18,0.27),
 7.0:(0.4,0.29,0.2,0.28),7.5:(0.39,0.31,0.21,0.27),
 8.0:(0.38,0.31,0.18,0.1),8.5:(0.4,0.31,0.18,0.09),9.0:(0.38,0.32,0.18,0.09),9.5:(0.38,0.32,0.18,0.09),10.0:(0.37,0.32,0.18,0.1)})
c={"mediaId":5495,"level":"A","keyWord":"rumor","defaultVoice":"male",
"taps":[{"phrase":"to wear a striped tie","target":"the boy","voice":"male","keys":boy},
{"phrase":"to open her eyes wide","target":"the girl in the white T-shirt","voice":"female","keys":girl},
{"phrase":"to hold a red book","target":"the old woman","voice":"female","keys":wom}],
"stillS":7.0,
"nouns":[{"word":"bookshelves","x":0.13,"y":0.12,"voice":"male"},
{"word":"a window","x":0.72,"y":0.17,"voice":"male"},
{"word":"a lamp","x":0.15,"y":0.3,"voice":"male"},
{"word":"a table","x":0.5,"y":0.82,"voice":"male"}],
"question":"What are the students doing?",
"answer":["They","are","whispering","in","the","library."],
"answerVoice":"male",
"notes":"Several cuts; the boy is the only one in a tie (state phrase, chosen because whispering/leaning/giggling is done by several students). Boy off 1.5-5.0 (a white-shirt sliver at the left edge at 5.0 not boxed). The girl in the white T-shirt is a sliver at the right edge at 3.0 and left edge at 3.5; in the wide shot 8.0-10.0 she is assumed to be the second student from the left (white top). Old woman (librarian, white hair, dark coat) holds the red book 5.0-7.5; she is probably the grey-haired figure hidden behind the boy at 0.5-1.0 (boxed off). In 8.0-10.0 she stands behind the students and her box is cut at the girls' heads (h ~0.09-0.10, below the 0.14 minimum) to avoid overlapping the white T-shirt girl's box. Still 7.0: a second small lamp at the right edge (0.95,0.43); the lamp pill sits on the big green lamp. Mixed group -> defaultVoice male (evenId false)."}
json.dump(c,open('/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/content/5495.json','w'),indent=1)
