from gen_6916_6917_6918_6919_lib import write
cam=[(.45,.35,.35,.33),(.45,.36,.35,.32),(.42,.38,.46,.31),(.40,.38,.46,.31),(.42,.38,.40,.33),(.45,.35,.38,.34),(.45,.32,.38,.37),(.45,.32,.39,.38)]
pig=[(.24,.02,.74,.32),(.08,.0,.84,.33),None,None,None,None,None,None]
bell=[(.0,.33,.22,.20),(.0,.34,.23,.19),(.0,.33,.21,.21),(.0,.33,.22,.21),(.0,.33,.20,.20),(.0,.34,.21,.19),(.0,.31,.21,.21),(.0,.31,.20,.20)]
write(6919,"B","cam","male",[
 ("to rotate on a metal shaft","the large cam","male",cam),
 ("to fly off through the sunbeams","the pigeons","male",pig),
 ("to hang above the rooftops","the bell","male",bell)],
 2.7,[("a bell",.13,.42,"male"),("a cam",.60,.50,"male"),("gears",.85,.33,"male"),("an oil can",.86,.95,"male")],
 "What is the large cam doing?","It is rotating on a metal shaft.","male",
 "No people. The pigeons are a group target and only visible at 0.2-0.7 (top of frame), off from 1.2. The bell phrase is a state (hangs in front of the city view) because no other action fits only one other thing; the vertical rod moving up and down sits in front of the cam and could not get its own box. Smaller cams on the bench do not turn, so 'rotate' fits only the large cam.")
