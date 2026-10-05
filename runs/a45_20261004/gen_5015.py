import json
def K(times, boxes):
    return [{"t":t,"off":True} if boxes.get(t) is None else dict(t=t,x=boxes[t][0],y=boxes[t][1],w=boxes[t][2],h=boxes[t][3]) for t in times]
T=[i*0.5 for i in range(21)]
young={0.0:(0.04,0.14,0.54,0.6),0.5:(0.04,0.14,0.56,0.6),1.0:(0.03,0.15,0.47,0.6),1.5:(0,0.15,0.48,0.62),2.0:(0,0.14,0.47,0.6),2.5:(0,0.15,0.5,0.58),3.0:(0,0.14,0.48,0.6),3.5:(0,0.13,0.48,0.62),4.0:(0,0.12,0.5,0.62),4.5:(0,0.17,0.5,0.62),5.0:(0,0.15,0.48,0.6),5.5:(0,0.13,0.48,0.62),6.0:(0,0.13,0.5,0.6),6.5:(0,0.13,0.5,0.6),7.0:(0,0.2,0.5,0.6),7.5:(0,0.18,0.5,0.6),8.0:(0,0.15,0.5,0.6),8.5:(0,0.14,0.48,0.62),9.0:(0,0.12,0.48,0.62),9.5:(0,0.13,0.48,0.62),10.0:(0.02,0.15,0.48,0.6)}
old={0.0:(0.6,0.2,0.4,0.56),0.5:(0.61,0.2,0.39,0.56),1.0:(0.5,0.18,0.5,0.6),1.5:(0.49,0.18,0.51,0.62),2.0:(0.48,0.19,0.52,0.6),2.5:(0.51,0.18,0.49,0.62),3.0:(0.49,0.18,0.51,0.6),3.5:(0.49,0.19,0.51,0.6),4.0:(0.51,0.18,0.49,0.6),4.5:(0.51,0.21,0.49,0.6),5.0:(0.49,0.18,0.51,0.6),5.5:(0.49,0.18,0.51,0.62),6.0:(0.51,0.18,0.49,0.62),6.5:(0.51,0.18,0.49,0.62),7.0:(0.51,0.2,0.49,0.6),7.5:(0.51,0.2,0.49,0.6),8.0:(0.51,0.19,0.49,0.6),8.5:(0.49,0.18,0.51,0.62),9.0:(0.49,0.18,0.51,0.62),9.5:(0.49,0.19,0.51,0.62),10.0:(0.51,0.19,0.49,0.62)}
d={"mediaId":5015,"level":"B","keyWord":"homemade","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a long braid","target":"the young woman","voice":"female","keys":K(T,young)},
 {"phrase":"to wear a rust-coloured apron","target":"the young woman","voice":"female","keys":K(T,young)},
 {"phrase":"to wear a patterned headscarf","target":"the older woman","voice":"female","keys":K(T,old)}],
"stillS":10.0,
"nouns":[{"word":"dough","x":0.5,"y":0.73,"voice":"female"},{"word":"a headscarf","x":0.78,"y":0.235,"voice":"female"},{"word":"an apron","x":0.25,"y":0.52,"voice":"female"},{"word":"pottery","x":0.14,"y":0.21,"voice":"female"}],
"question":"What are the two women doing?",
"answer":["They","are","kneading","the","dough","together."],
"answerVoice":"female",
"notes":"Both women knead the same dough the whole clip, so no action fits only one of them: all three phrases are states (braid + apron = young woman, headscarf = older woman). Women stand side by side; boxes split at about x 0.49-0.51 and stop above the dough. 'rust-coloured' is British spelling. 'homemade' is an adjective, not placed."}
json.dump(d,open("content/5015.json","w"),indent=1)
