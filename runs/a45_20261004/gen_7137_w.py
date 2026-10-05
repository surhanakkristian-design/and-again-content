from lib_w_7137_7138_7140_7141 import write
car = [(.15,.20,.53,.27),(.10,.20,.56,.27),(.03,.20,.62,.30),(0,.20,.63,.31),(0,.19,.62,.35),(0,.19,.61,.40),(0,.19,.58,.47),(0,.18,.56,.52)]
sheep = [(.71,.32,.29,.17)]*8
walker = [(.78,.15,.20,.165)]*8
write(7137, "B", "ford", "male", [
  ("to ford a shallow river", "the off-road vehicle", "male", car),
  ("to wait on the stepping stones", "the sheep", "male", sheep),
  ("to watch from the far bank", "the walker", "male", walker)],
  1.2, [("sheep", .86, .40, "male"), ("a wooden post", .72, .55, "male"), ("stepping stones", .88, .68, "male"), ("a rubber boot", .58, .85, "male")],
  "What is the off-road vehicle doing?", "It is fording a shallow river.", "male",
  "walker is tiny in the background (fixed box); sheep group uses one box")
