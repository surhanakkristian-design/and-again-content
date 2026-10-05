import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [{"t":t,"x":round(a,2),"y":round(b,2),"w":round(c-a,2),"h":round(d-b,2)} for t,(a,b,c,d) in zip(T,L)]
TR=[(0,.58,.27,.80),(0,.57,.29,.80),(0,.58,.29,.80),(0,.58,.29,.79),(0,.57,.30,.78),(.01,.57,.31,.77),(.03,.57,.31,.76),(.03,.57,.30,.75)]
SI=[(.54,.33,.84,.44)]*8
SK=[(0,0,1,.33)]*8
c={"mediaId":5538,"level":"B","keyWord":"agriculture","defaultVoice":"female",
"taps":[
{"phrase":"to tow a loaded trailer","target":"the tractor","voice":"female","keys":K(TR)},
{"phrase":"to stand on the horizon","target":"the grain silos","voice":"female","keys":K(SI)},
{"phrase":"to glow orange and pink","target":"the sky","voice":"female","keys":K(SK)}],
"stillS":2.2,
"nouns":[{"word":"silos","x":.68,"y":.385,"voice":"female"},
{"word":"a combine harvester","x":.65,"y":.57,"voice":"female"},
{"word":"a tractor","x":.15,"y":.68,"voice":"female"},
{"word":"wheat","x":.55,"y":.85,"voice":"female"}],
"question":"What are the machines doing?",
"answer":["They","are","harvesting","wheat","at sunset."],
"answerVoice":"female",
"notes":"No person visible. The combine harvesters are not a tap target: all three cut wheat and the second one also seems to unload, so no phrase fits only one. Silos are tiny: their box (0.30 x 0.11) is squeezed between the sky box and the far harvesters and touches the top of the far harvester. A second, tiny tractor is far away next to the middle harvester (about x .52, y .47); 'the tractor' means the near one. Key word 'agriculture' is abstract: not a noun slot and not natural in the answer."}
json.dump(c,open("content/5538.json","w"),indent=1,ensure_ascii=False)
