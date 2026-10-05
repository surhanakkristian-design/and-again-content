from w_7206_7207_7208_7210_lib import build, xyxy
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
stag=xyxy((.20,.37,.70,.75),(.20,.37,.71,.75),(.18,.36,.71,.76),(.17,.32,.72,.77),(.14,.33,.69,.78),(.11,.33,.58,.77),(.09,.32,.53,.81),(.07,.31,.58,.82))
van=xyxy((.74,.43,1.0,.70),(.74,.43,1.0,.70),(.74,.44,1.0,.71),(.74,.44,1.0,.71),(.74,.43,1.0,.72),(.73,.44,1.0,.72),(.72,.43,1.0,.73),(.71,.44,1.0,.74))
build(7207,"B","hart","male",[
 ("to bellow into the cold air","the hart","male",stag),
 ("to stride across the zebra crossing","the hart","male",stag),
 ("to shine its headlights","the van","male",van)],
 0.2,[("a hart",.42,.56,"male"),("a bakery",.18,.36,"male"),("a church spire",.67,.18,"male"),("a van",.86,.58,"male")],
 "What is the hart doing?","It is bellowing into the cold air.","male",
 "Black bird skipped as a target: it flies right beside/over the antlers in every frame, boxes would overlap. Hinds in background too small and behind the stag. 'bellow' shown visually (head raised, mouth open, steaming breath) 0.2-1.2 s; stride 2.2-3.7 s.",T)
