from w_7206_7207_7208_7210_lib import build, xyxy
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=xyxy((.35,.43,.62,.88),(.35,.43,.62,.88),(.36,.44,.62,.90),(.31,.44,.62,.90),(.27,.43,.62,.91),(.28,.43,.62,.91),(.27,.44,.63,.95),(.26,.43,.63,.95))
man=xyxy((.62,.40,.80,.68),(.63,.40,.81,.68),(.63,.40,.81,.68),(.63,.40,.82,.68),(.63,.38,.82,.70),(.63,.38,.84,.70),(.64,.37,.85,.71),(.64,.37,.86,.71))
gull=[(.79,.10,.18,.14),(.79,.10,.18,.14),(.81,.08,.18,.14),(.82,.07,.18,.14),(.82,.05,.18,.14),(.82,.04,.18,.14),(.82,.01,.18,.14),(.82,.0,.18,.14)]
build(7206,"B","harper","female",[
 ("to pluck the harp strings","the woman","female",woman),
 ("to hold up a huge fish","the man with the fish","male",man),
 ("to perch on a steel beam","the seagull","female",gull)],
 0.2,[("a harper",.50,.62,"female"),("a harp",.22,.76,"female"),("rubber boots",.64,.80,"female"),("a seagull",.88,.17,"female")],
 "What is the harper doing?","She is plucking the harp strings.","female",
 "Small distant gull also sits on the forklift roof (~.62,.39) but not on a beam; harp neck in blurry foreground. Woman/fishmonger boxes split at x~.62.",T)
