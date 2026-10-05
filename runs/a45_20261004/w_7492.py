from w_7482_7483_7488_7492_lib import build
P=[(.72,.20,.27,.47),(.74,.20,.25,.47),(.72,.20,.27,.47),(.74,.20,.26,.45),(.70,.18,.30,.46),(.70,.16,.30,.45),(.70,.13,.30,.47),(.72,.13,.28,.46)]
B=[(.03,.41,.35,.15),(.03,.41,.35,.15),(.03,.41,.35,.14),(.03,.41,.35,.14),(.03,.39,.35,.14),(.03,.37,.35,.14),(.03,.35,.35,.15),(.03,.34,.35,.15)]
C=[(.39,.39,.18,.18),(.39,.39,.18,.17),(.39,.39,.18,.17),(.39,.38,.18,.16),(.39,.37,.18,.16),(.39,.35,.18,.16),(.39,.33,.18,.16),(.39,.32,.18,.16)]
build(7492,'B','rainfall','female',[
 ('to spout rainwater','the pipe','female',P),
 ('to lean against a wall','the bicycles','female',B),
 ('to sit under plastic sheeting','the crates','female',C)],
 2.2,[('rainfall',.35,.12,'female'),('an awning',.22,.27,'female'),('bicycles',.17,.46,'female'),('an oil drum',.88,.55,'female')],
 'What is pouring off the roof?','Heavy rain is pouring off the tin roof.','female',
 'no people; pipe box includes the gushing stream and so also covers the oil drum (drum is not a target); bicycles and crates are static states, only action target is the pipe')
