import json
T=[i*0.5 for i in range(25)]
N=None
Wm=[(.42,0,.58,.57),(.42,0,.58,.55),(.45,0,.55,.51),(.48,0,.52,.46),(.45,0,.55,.46),(.47,0,.53,.45),(.45,0,.55,.56),
(.18,.03,.30,.44),(.06,.03,.42,.38),(.08,.03,.40,.40),(.20,.03,.28,.33),(.10,.03,.38,.35),(.22,.05,.26,.27),(.22,.03,.26,.25),(.28,.05,.20,.18),(.36,.04,.24,.18),
N,N,N,N,N,(.10,.05,.80,.62),(.12,.05,.76,.62),(.12,.04,.76,.63),(.11,.04,.75,.62)]
Wa=[N,N,(.45,.52,.30,.46),(.45,.48,.30,.50),(.45,.47,.30,.51),(.45,.46,.30,.52),(.47,.57,.30,.43),
(.49,.12,.20,.34),(.49,.11,.18,.30),(.49,.11,.18,.28),(.49,.11,.18,.24),(.49,.11,.18,.22),(.49,.11,.18,.24),(.49,.10,.18,.18),(.49,.10,.18,.14)]+[N]*10
def keys(B):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
c={"mediaId":4380,"level":"A","keyWord":"fill","defaultVoice":"female",
"taps":[{"phrase":"to turn on the tap","target":"the woman","voice":"female","keys":keys(Wm)},
{"phrase":"to lie in the bath","target":"the woman","voice":"female","keys":keys(Wm)},
{"phrase":"to fall into the bath","target":"the water","voice":"female","keys":keys(Wa)}],
"stillS":2.5,
"nouns":[{"word":"a woman","x":.72,"y":.18,"voice":"female"},{"word":"bottles","x":.18,"y":.36,"voice":"female"},{"word":"a tap","x":.82,"y":.48,"voice":"female"},{"word":"a bath","x":.30,"y":.72,"voice":"female"}],
"question":"What is the woman filling?","answer":["She","is","filling","the","bath","with","water."],"answerVoice":"female",
"notes":"Only two targets: the woman (two phrases, same keys) and the water = the stream falling from the tap (1.0-7.0 s; it is thin and pale in the first shot). In the low shot (3.5-7.0) the stream runs in front of the woman, so her box is cut at the stream (x 0.48) and loses the right half of her face. 7.5-10.0: foam covers the lens, woman barely visible at 7.5, off after. The bottles stand in two groups on the still; the pill is on the left group."}
json.dump(c,open('content/4380.json','w'),indent=1)
