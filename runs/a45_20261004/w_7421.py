from w_7421_7422_7425_7427_lib import build
D=[[.33,.13,.35,.72],[.33,.13,.39,.73],[.32,.10,.40,.77],[.30,.10,.44,.77],[.17,.15,.62,.80],[.30,.14,.44,.78],[.34,.16,.38,.80],[.27,.05,.55,.91]]
G=[[.69,.43,.18,.31],[.73,.44,.17,.30],[.73,.46,.22,.28],[.75,.46,.23,.28],[.80,.44,.20,.24],[.82,.45,.18,.20],None,None]
build(7421,'B','performer','male',
 [("to stamp on the dusty stage","the dancer","male",D),
  ("to toss his long hair","the dancer","male",D),
  ("to strum an acoustic guitar","the guitarist","male",G)],
 1.2,
 [("a spotlight",.32,.12,"male"),("hams",.90,.31,"male"),("a performer",.50,.40,"male"),("a guitarist",.80,.58,"male")],
 "What is the dancer doing?","He is stamping on the dusty stage.","male",
 "Dancer and guitarist overlap in depth: boxes split vertically at x~.70-.80, so the dancer's right elbow/hand is partly cut at some times. Guitarist off at 3.2/3.7 (only a guitar edge at the frame border). 'a performer' placed on the dancer; the guitarist carries his own label.")
