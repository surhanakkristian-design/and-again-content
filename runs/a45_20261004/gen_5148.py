from lib_5147_5148_5150_5151 import build
p = {0.0: (0.22, 0.7, 0.68, 0.3), 0.5: (0.24, 0.7, 0.76, 0.3), 1.0: (0.44, 0.86, 0.34, 0.14),
     2.5: (0.39, 0.48, 0.22, 0.3), 3.0: (0.39, 0.49, 0.22, 0.28), 3.5: (0.39, 0.49, 0.22, 0.28), 4.0: (0.37, 0.47, 0.23, 0.31),
     4.5: (0.14, 0.34, 0.86, 0.66), 5.0: (0.13, 0.34, 0.85, 0.66), 5.5: (0.14, 0.35, 0.86, 0.65), 6.0: (0.13, 0.33, 0.85, 0.67),
     6.5: (0.14, 0.33, 0.86, 0.67), 7.0: (0.12, 0.34, 0.86, 0.66),
     7.5: (0.37, 0.42, 0.18, 0.18), 8.0: (0.39, 0.42, 0.18, 0.18), 8.5: (0.39, 0.42, 0.18, 0.18), 9.0: (0.41, 0.42, 0.18, 0.18)}
b = {0.0: (0.04, 0.12, 0.83, 0.15), 0.5: (0.07, 0.22, 0.84, 0.14), 1.0: (0.05, 0.3, 0.87, 0.14), 1.5: (0.0, 0.32, 1.0, 0.18), 2.0: (0.0, 0.37, 1.0, 0.14)}
build(5148, 'A', 'morning', 'female', [
  ('to fly away', 'the birds', 'female', b),
  ('to drink from a bottle', 'the person in the coat', 'female', p),
  ('to walk across the street', 'the person in the coat', 'female', p)],
  8.0, [('the sky', 0.3, 0.12, 'female'), ('a traffic light', 0.47, 0.41, 'female'), ('a street', 0.5, 0.8, 'female')],
  'What are the birds doing?', 'The birds are flying away.', 'female',
  'Only one person (gender unclear, short bleached hair), so target named "the person in the coat"; defaultVoice female from evenId. 0.0-1.0 is a first-person shot: only the person\'s coat, leg and hand are visible (bottom); 1.5-2.0 person off. The bottle is a metal flask (6.0-7.0, drinking at 6.5/7.0); description says can. The birds (pigeons) are off from 2.5. Still 8.0: traffic light pill on the green light above the person.')
