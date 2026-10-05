import json
T=[i*0.5 for i in range(24)]
h=[[.21,.22,.58,.44],[.21,.21,.60,.45],[.21,.23,.58,.43],[.21,.23,.60,.43],[.21,.23,.58,.48],[.21,.19,.59,.52],[.21,.23,.58,.48],[.21,.19,.58,.51],
[.21,.19,.57,.51],[.21,.19,.57,.51],[.21,.24,.57,.47],[.21,.24,.57,.47],[.21,.24,.57,.47],[.21,.22,.74,.47],[.21,.23,.73,.44],[.21,.23,.74,.44],
[.21,.23,.57,.48],[.21,.23,.57,.48],[.21,.23,.57,.48]]+[[0,.32,.96,.37]]*5
p=[[0,.02,.20,.33]]*19+[[0,.02,.22,.29]]*5
def keys(b): return [{"t":t,"x":x,"y":y,"w":w,"h":hh} for t,(x,y,w,hh) in zip(T,b)]
d={"mediaId":4208,"level":"A","keyWord":"snack","defaultVoice":"female",
"taps":[
 {"phrase":"to eat a burger","target":"the hamster","voice":"female","keys":keys(h)},
 {"phrase":"to lie on its back","target":"the hamster","voice":"female","keys":keys(h)},
 {"phrase":"to hang from a shelf","target":"the plant","voice":"female","keys":keys(p)}],
"stillS":0.0,
"nouns":[{"word":"a burger","x":.50,"y":.52,"voice":"female"},{"word":"a cup","x":.87,"y":.60,"voice":"female"},
 {"word":"a sofa","x":.30,"y":.70,"voice":"female"},{"word":"a plant","x":.13,"y":.15,"voice":"female"}],
"question":"What is the hamster eating?",
"answer":["It","is","eating","a lot of","snacks."],
"answerVoice":"female",
"notes":"Key word 'snack' is in the model answer only: no single thing is 'a snack' more than the others, so it is not a noun slot. The clip shows burger, noodles, a pink drink, yoghurt, a corn dog, cake and crisps one after another. Third target is the hanging plant top left (small, in the background, visible all the time); its box is cut at the hamster's left edge and, in the last shot, just above the lying hamster. The two toy animals on the shelf are not used. 'a lot of' is one chip."}
json.dump(d,open("content/4208.json","w"),indent=1,ensure_ascii=False)
