from gen_7288_7290_7291_7292_lib import write
wom=[(0,.53,1,.47)]*4+[(0,.24,1,.76),(0,.23,1,.77),(0,.22,1,.78),(0,.22,1,.78)]
flk=[(.39,.39,.20,.14),(.40,.39,.20,.14),(.42,.39,.20,.14),(.40,.39,.20,.14),None,None,None,None]
lmp=[(.66,.06,.26,.24),(.67,.05,.26,.25),(.67,.04,.26,.26),(.67,.04,.27,.26),(.67,.02,.28,.22),(.68,.02,.27,.21),(.68,.02,.28,.20),(.68,.02,.28,.20)]
F="female"
write(7292,"B","lid",F,
 [("to burst out laughing","the young woman",F,wom),
  ("to melt on her eyelid","the snowflake",F,flk),
  ("to glow in the dusk","the street lamp",F,lmp)],
 0.2,[("an eyelid",.27,.46,F),("a street lamp",.79,.14,F),("an earring",.72,.65,F),("a knitted scarf",.50,.88,F)],
 "What is melting on her eyelid?","A snowflake is melting on her eyelid.",F,
 "Snowflake sits inside the face, so while it is visible (0.2-1.7 s) the woman's box is only the lower face and scarf (y >= .53); from 2.2 s the snowflake is gone (off) and her box grows. Key word 'lid' shown as 'an eyelid' on her other (left-in-picture) eye so it does not cover the snowflake.")
