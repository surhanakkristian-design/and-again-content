from w_7482_7483_7488_7492_lib import build
W=[(.37,.20,.45,.48),(.40,.20,.42,.48),(.43,.18,.39,.50),(.45,.18,.37,.50),(.47,.17,.35,.49),(.48,.17,.34,.50),(.52,.18,.30,.50),(.56,.17,.29,.51)]
M=[(.82,.37,.18,.36),(.82,.37,.18,.36),(.82,.37,.18,.36),(.82,.37,.18,.36),(.82,.36,.18,.36),(.82,.36,.18,.36),(.82,.37,.18,.36),(.85,.36,.15,.36)]
C=[(.52,.75,.48,.25),(.52,.73,.48,.27),(.52,.74,.48,.26),(.52,.74,.48,.26),(.52,.73,.48,.27),(.52,.73,.48,.27),(.52,.74,.48,.26),(.52,.74,.48,.26)]
build(7482,'B','put down','female',[
 ('to lower a wooden block','the woman','female',W),
 ('to crouch behind the railing','the bald man','male',M),
 ('to cover their mouths','the crowd','female',C)],
 2.7,[('a harness',.73,.33,'female'),('balloons',.14,.48,'female'),('a tower',.30,.68,'female'),('a crowd',.72,.88,'female')],
 'What is the woman doing?','She is lowering a block onto the tower.','female',
 'crowd target is a group; man partly cut at the right edge; tower top wobbles slightly but stands')
