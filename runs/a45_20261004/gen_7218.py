from gen_7217_7218_7219_7220_lib import build
man = [(0.22,0.35,0.64,0.63),(0.23,0.35,0.67,0.63),(0.18,0.35,0.74,0.63),(0.15,0.35,0.76,0.63),
       (0.11,0.33,0.82,0.65),(0.08,0.32,0.86,0.66),(0.0,0.31,0.86,0.67),(0.0,0.31,0.78,0.67)]
cc = [(.42,.09),(.41,.09),(.41,.08),(.39,.08),(.39,.08),(.38,.07),(.38,.07),(.38,.05)]
crow = [(round(x-.09,2), max(0.0, round(y-.07,2)), .18, .14) for x, y in cc]
build(7218, "B", "historian", "male",
 [("to examine an old plan", "the historian", "male", man),
  ("to break into a smile", "the historian", "male", man),
  ("to take off from the wall", "the crow", "male", crow)],
 0.2,
 [("a historian", 0.40, 0.53, "male"), ("an archway", 0.62, 0.28, "male"), ("a laptop", 0.14, 0.73, "male"), ("a sketchbook", 0.66, 0.86, "male")],
 "What is the historian holding?", "He is holding an old plan against the wall.", "male",
 "Crow is small and sits on top of the main wall until it flies off at 3.7 (small birds also perch on the far battlements, but only this crow takes off). Man box includes the plan he holds; table covers his legs.")
