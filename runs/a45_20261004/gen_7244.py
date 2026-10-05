from gen_7242_7243_7244_7245_lib import write
w = [(.33,.54,.33,.40),(.33,.48,.34,.43),(.32,.44,.37,.55),(.33,.43,.48,.56),(.32,.44,.48,.51),(.32,.44,.49,.51),(.29,.42,.52,.57),(.32,.37,.50,.58)]
write(7244, "B", "infrastructure", "female",
 [("to climb a metal ladder", "the worker", "female", w),
  ("to grip a riveted pipe", "the worker", "female", w),
  ("to glance up at the street", "the worker", "female", w)],
 2.2,
 [("a car", .33, .18, "female"), ("cables", .62, .33, "female"), ("a tunnel", .30, .52, "female"), ("a water main", .82, .72, "female")],
 "What is the worker doing?", "She is climbing a metal ladder.", "female",
 "Only one person (woman in white hard hat and orange hi-vis jacket), so all three phrases use her. She looks up at the street at 0.7-1.2 s and 3.7 s. 'a water main' = the huge riveted iron pipe on the right; 'a tunnel' = the round brick sewer opening; 'a car' = the car passing on the street above (different cars over the clip). Key word 'infrastructure' is abstract, not placed.")
