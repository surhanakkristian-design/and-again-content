from w_7403_7406_7407_7408_lib import build
wo = [(.22,.20,.52,.45),(.30,.19,.60,.50),(.27,.21,.45,.40),(.10,.21,.57,.60),(.14,.21,.55,.60),(.15,.21,.56,.62),(.27,.25,.39,.59),(.19,.25,.36,.60)]
co = [None,None,(.82,.25,.18,.37),(.80,.25,.19,.38),(.78,.24,.20,.38),(.77,.24,.20,.37),(.75,.25,.20,.39),(.69,.24,.20,.38)]
bag = [(.12,.80,.38,.15),(.10,.80,.39,.15),(.06,.81,.40,.17),(.05,.82,.42,.15),(.04,.83,.43,.13),(.05,.83,.44,.13),(.07,.84,.45,.14),(.05,.85,.47,.14)]
build(7407,'B','papa','female',[
 ('to leap into his arms','the woman','female',wo),
 ('to grin from the doorway','the conductor','male',co),
 ('to lie on the platform','the cloth bag','female',bag)],
 2.7,[('a conductor',.86,.31,'male'),('a camel coat',.43,.50,'female'),('a suitcase',.70,.80,'female'),('a cloth bag',.22,.90,'female')],
 'What is the woman doing?','She is leaping into his arms.','female',
 'Man and woman are tangled in a hug the whole clip, so the man is not a tap target (no clean split). Conductor only a sliver at the right edge at 0.7 (off) and absent at 0.2. Woman leaps into his arms at 0.2-1.7, later stands and hugs him: answer/phrase fit the start best. Bag phrase is weaker on B level (platform). Woman box bottom trimmed at 3.2/3.7 to stay above the bag box.')
