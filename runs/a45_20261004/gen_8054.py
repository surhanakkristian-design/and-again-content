from gen_8053_8054_8057_8058_lib import K, write
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman = K(T, [None,None,(0,.19,.45,.88),(0,.19,.45,.88),(0,.17,.47,.90),(0,.17,.45,.90),(0,.17,.47,.95),(0,.17,.48,.95)])
man = K(T, [None,None,(.56,.06,1,.98),(.56,.06,1,.98),(.47,.06,1,.72),(.45,.07,1,.74),(.47,.08,1,.76),(.48,.08,1,.78)])
candle = K(T, [(.80,.06,.98,.50),(.80,.05,.99,.50),(.45,.68,.56,.84),(.45,.68,.56,.84),(.47,.72,.62,.88),(.45,.74,.60,.88),(.47,.76,.62,.93),(.48,.78,.62,.94)])
write(8054, {"mediaId": 8054, "level": "A", "keyWord": "anniversary", "defaultVoice": "female",
 "taps": [
  {"phrase": "to cut the cake", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to put his arm around her", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to burn on the cake", "target": "the candle", "voice": "female", "keys": candle}],
 "stillS": 1.2,
 "nouns": [{"word": "a lamp", "x": 0.43, "y": 0.08, "voice": "female"},
           {"word": "a woman", "x": 0.20, "y": 0.55, "voice": "female"},
           {"word": "a man", "x": 0.80, "y": 0.55, "voice": "male"},
           {"word": "a cake", "x": 0.52, "y": 0.89, "voice": "female"}],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "cutting", "the", "cake."],
 "answerVoice": "female",
 "notes": "0.2-0.7 is a close-up of knife, cake and candle only (woman's hand not in shot -> woman and man off). The candle sits between the couple: its box is a narrow strip (w ~.14) between the woman's and man's boxes; the woman's box ends at her face/jacket edge and the man's box at 2.2-3.7 stops above the cake, so his legs are outside. Man puts his arm around her from 2.2. Key word 'anniversary' is not a placeable noun."})
