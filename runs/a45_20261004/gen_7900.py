from lib_7896_7897_7898_7900 import write
w = [(.16,.23,.46,.62),(.22,.23,.37,.62),(.15,.25,.38,.62),(.17,.25,.38,.63),(.17,.25,.36,.62),(.07,.25,.43,.64),(.07,.25,.42,.67),(.07,.25,.43,.67)]
p = [(.69,.31,.2,.24),(.68,.31,.2,.22),(.69,.31,.2,.26),(.68,.31,.21,.3),(.69,.31,.22,.33),(.69,.31,.22,.32),(.67,.32,.22,.3),(.67,.31,.22,.31)]
write(7900, "B", "match", "female",
 [("to take a mirror selfie", "the woman", "female", w),
  ("to stare in disbelief", "the porter", "male", p),
  ("to blend into the wallpaper", "the woman", "female", w)],
 1.2,
 [("wallpaper", .2, .14, "female"), ("a wall lamp", .47, .24, "female"), ("a potted palm", .66, .62, "female"), ("a carpet", .6, .9, "female")],
 "What does her new outfit match?", "Her new outfit matches the flamingo wallpaper.", "female",
 "Woman used for two phrases (selfie, blending in); porter is mostly hidden behind the brass trolley, box covers head and visible body. At t=0.2 her outfit is still burgundy (it changes by 0.7), so 'to blend into the wallpaper' only holds from 0.7 on.")
