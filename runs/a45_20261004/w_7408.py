from w_7403_7406_7407_7408_lib import build
man = [(.29,.03,.71,.33),(.42,.02,.58,.34),(.38,.05,.62,.32),(.37,.10,.63,.34),(.35,.11,.65,.36),(.35,.06,.64,.40),(.41,.04,.59,.43),(.48,.02,.52,.45)]
dog = [(.23,.37,.70,.48),(.26,.37,.70,.47),(.24,.38,.58,.47),(.26,.45,.56,.38),(.30,.48,.46,.27),(.30,.47,.52,.27),(.27,.48,.47,.27),(.26,.48,.52,.27)]
bt = [(.10,.16,.18,.20),(.15,.17,.19,.19),(.10,.17,.21,.20),(.08,.17,.21,.25),(.08,.16,.20,.21),(.10,.18,.20,.20),(.10,.18,.19,.25),(.09,.18,.20,.27)]
build(7408,'A','park','male',[
 ('to lift a dog','the man','male',man),
 ('to stand on a stool','the dog','male',dog),
 ('to work behind the bar','the woman','female',bt)],
 3.7,[('a man',.78,.32,'male'),('a newspaper',.15,.47,'male'),('a dog',.42,.60,'male'),('a stool',.40,.83,'male')],
 'What is the man doing?','He is putting the dog on a stool.','male',
 'Man holds the dog against his body, so the boxes are split horizontally: man box = head and shoulders above the dog (his lower body beside/behind the dog is not tappable). Woman = blurred bartender in the background, small but visible in every frame. He lifts the dog at 0.2-1.7 and sets it down; stool pill on the empty front stool (the dog stands on another stool).')
