from w_7482_7483_7488_7492_lib import build
P=[(.08,.35,.92,.28),(.05,.34,.95,.31),(.0,.30,1.0,.36),(.02,.29,.98,.40),(.09,.30,.91,.42),(.06,.28,.94,.45),(.04,.26,.96,.48),(.03,.25,.97,.49)]
build(7483,'B','put down','male',[
 ('to touch down on the grass','the plane','male',P),
 ('to kick up grass','the plane','male',P),
 ('to roll past a windsock','the plane','male',P)],
 2.7,[('a windsock',.65,.13,'male'),('a glacier',.25,.22,'male'),('a plane',.82,.46,'male'),('sheep',.85,.62,'male')],
 'What is the plane doing?','It is touching down on the grass.','male',
 'all three phrases on the plane: sheep, windsock pole and pilot all sit behind/inside the plane box at every frame, so no non-overlapping second target; pilot only visible from 1.2 s')
