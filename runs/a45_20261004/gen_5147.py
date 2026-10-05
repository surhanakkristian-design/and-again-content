from lib_5147_5148_5150_5151 import build
man = {0.0: (0.0, 0.0, 0.66, 0.46), 0.5: (0.0, 0.0, 0.62, 0.5), 1.0: (0.04, 0.0, 0.66, 0.68)}
market = {t: (0.0, 0.28, 1.0, 0.72) for t in [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]}
crowd = {5.0: (0.0, 0.47, 1.0, 0.53), 5.5: (0.0, 0.47, 1.0, 0.53), 6.0: (0.0, 0.44, 1.0, 0.56)}
for t in [6.5, 7.0, 7.5, 8.0, 8.5, 9.0]: crowd[t] = (0.0, 0.46, 1.0, 0.54)
build(5147, 'A', 'people', 'male', [
  ('to carry a white bag', 'the man with the white bag', 'male', man),
  ('to look at the food', 'the people in the market', 'male', market),
  ('to fill the whole street', 'the crowd on the street', 'male', crowd)],
  7.0, [('the sky', 0.57, 0.07, 'male'), ('a screen', 0.33, 0.25, 'male'), ('people', 0.5, 0.78, 'male')],
  'What are the people doing?', 'They are crossing a busy street.', 'male',
  'Three shots, crowds everywhere, so two targets are groups. Shot 1 (0-1.0): man in dark suit with the white paper bag (centre at 0.0/0.5, left at 1.0); other people carry black bags only. Shot 2 (1.5-4.5): the whole market crowd as one target (many shoppers bend over the stalls); box covers all people. Shot 3 (5.0-9.0): the crowd on the junction, box over the lower half. Still 7.0: screen pill on the big video screen (shows a watch).')
