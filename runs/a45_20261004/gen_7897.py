from lib_7896_7897_7898_7900 import write
h = [(.12,.16,.52,.69),(.09,.13,.63,.72),(.05,.09,.68,.8),(.02,.05,.75,.8),(0,0,.86,.85),(0,0,.94,.88),(0,0,1,.97),(0,0,1,.98)]
write(7897, "A", "love", "male",
 [("to close its eyes", "the horse", "male", h),
  ("to stand in the grass", "the horse", "male", h),
  ("to lower its head", "the horse", "male", h)],
 0.2,
 [("a barn", .14, .18, "male"), ("a horse", .45, .38, "male"), ("a gate", .88, .4, "male"), ("grass", .12, .62, "male")],
 "What is the man doing?", "He is touching the horse's face.", "male",
 "Horse used for all three phrases: the man is only arms and hands lying over the horse's face, so a separate box for him cannot avoid overlapping the horse box. Key word 'love' is abstract, not placed.")
