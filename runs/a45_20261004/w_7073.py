from w_7070_7072_7073_7074_lib import *
splits=[.71,.71,.72,.72,.73,.74,.75,.76]
wx=[.08,.08,.08,.08,.07,.08,.07,.21]
woman=[(x,.30,s-x,.46) for x,s in zip(wx,splits)]
mid=[(s,.07,.18,.54) for s in splits]
write(7073,"B","ease","female",[
 ("to steady a stained-glass window","the woman","female",woman),
 ("to kneel on a padded blanket","the woman","female",woman),
 ("to reach above his head","the man in the middle","male",mid)],
 0.2,[("a stained-glass window",.22,.25,"female"),("a blanket",.38,.72,"female"),("rope",.85,.73,"female"),("a spirit level",.74,.92,"female")],
 "What is the woman doing?","She is steadying a stained-glass window.","female",
 "woman box is cut at the line to the middle man (her back/boots overlap his legs); middle man's arm is raised to the scaffolding the whole clip")
