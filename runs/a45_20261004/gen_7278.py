from gen_7275_7276_7277_7278_lib import *
def b(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
S=[.32,.32,.33,.34,.35,.37,.37,.38]
LT=[.29,.28,.27,.27,.28,.30,.32,.33]; LB=[.64,.64,.68,.73,.75,.77,.79,.81]
AT=[.39,.38,.40,.40,.41,.41,.43,.43]; AB=[.63,.63,.64,.65,.67,.67,.69,.71]
leo=[b(S[i],LT[i],.99,LB[i]) for i in range(8)]
ant=[b(.11,AT[i],S[i],AB[i]) for i in range(8)]
write(7278,"A","killer","female",
 [("to yawn in the tree","the leopard","female",leo),
  ("to rest its head","the leopard","female",leo),
  ("to hang over the branch","the antelope","female",ant)],
 3.7,
 [("a leopard",0.68,0.44,"female"),("the sky",0.28,0.29,"female"),("a tree",0.87,0.86,"female"),("grass",0.25,0.85,"female")],
 "Where is the leopard lying?","The leopard is lying in a tree.","female",
 "Leopard and antelope overlap: boxes split vertically at x .32-.38, so part of the leopard's head (esp. 3.2-3.7, head on the antelope) falls in the antelope box. 'to rest its head' = 3.2-3.7 only, yawn = 0.7-2.2. Key word 'killer' not used as a noun label (not a natural label).")
