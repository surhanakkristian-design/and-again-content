from w_7403_7406_7407_7408_lib import build
b = [(.05,.24,.94,.40),(.06,.22,.92,.41),(.05,.25,.94,.39),(.05,.24,.94,.39),(.05,.24,.94,.40),(.05,.24,.94,.39),(.05,.24,.93,.42),(.05,.24,.94,.40)]
build(7406,'A','pants','female',[
 ('to dry in the sun','the pants','female',b),
 ('to move in the wind','the pants','female',b),
 ('to hang on a line','the pants','female',b)],
 0.2,[('the sky',.48,.22,'female'),('a balcony',.80,.10,'female'),('pants',.38,.53,'female')],
 'What are the pants doing?','They are drying in the sun.','female',
 'No people or animals: the row of pants on the line is the only real target, so all three phrases use it (one box over the whole row). Pants = underpants here (British sense), as in the key word. Only 3 nouns: the rest is many similar windows/shutters with no single clear spot.')
