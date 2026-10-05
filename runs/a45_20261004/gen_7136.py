from gen_7131_7132_7134_7136_lib import write
truck=[(.04,.45,.53,.27),(.04,.45,.53,.27),(0,.44,.56,.32),(0,.44,.56,.31),(0,.44,.56,.33),(0,.44,.55,.33),(0,.43,.54,.37),(0,.42,.53,.38)]
hik=[(.58,.52,.40,.18),(.58,.52,.40,.18),(.57,.52,.41,.18),(.57,.52,.41,.18),(.57,.52,.41,.18),(.56,.52,.42,.18),(.55,.52,.44,.18),(.54,.51,.45,.19)]
steam=[(.64,.26,.20,.14)]*8
write(7136,"B","ford","female",[
 ("to plough through the river","the orange truck","female",truck),
 ("to wade across holding hands","the hikers","female",hik),
 ("to billow into the sky","the steam","female",steam)],
 2.2,[("a glacier",.45,.31,"female"),("a tent",.85,.44,"female"),("hikers",.76,.61,"female"),("an off-road truck",.25,.58,"female")],
 "What are the hikers doing?","They are fording the river hand in hand.","female",
 "Hikers treated as one group target (they wade in one line holding hands). Truck and hiker boxes meet near x 0.54-0.58; split on the gap between the truck's rear and the first hiker. Steam is a small target in the distance (box at minimum size).")
import json, os
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'content/7136.json')
c=json.load(open(p)); c['answer']=["They","are","fording","the","river","hand in hand."]; json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
