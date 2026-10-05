from lib_5147_5148_5150_5151 import build
man = {0.0: (0.3, 0.48, 0.52, 0.52), 0.5: (0.26, 0.43, 0.62, 0.57), 1.0: (0.2, 0.34, 0.77, 0.66), 1.5: (0.32, 0.28, 0.68, 0.72),
       2.0: (0.19, 0.24, 0.81, 0.76), 2.5: (0.34, 0.18, 0.66, 0.82), 3.0: (0.46, 0.15, 0.54, 0.85), 3.5: (0.55, 0.15, 0.45, 0.85),
       4.0: (0.53, 0.15, 0.47, 0.85), 4.5: (0.61, 0.13, 0.39, 0.87), 5.0: (0.63, 0.1, 0.37, 0.9), 5.5: (0.61, 0.12, 0.39, 0.88),
       6.0: (0.63, 0.1, 0.37, 0.9), 6.5: (0.64, 0.12, 0.36, 0.88), 7.0: (0.66, 0.12, 0.34, 0.88), 7.5: (0.67, 0.12, 0.33, 0.88),
       8.0: (0.6, 0.15, 0.4, 0.85), 8.5: (0.43, 0.15, 0.57, 0.85), 9.0: (0.41, 0.2, 0.59, 0.8), 9.5: (0.5, 0.3, 0.5, 0.7),
       10.0: (0.35, 0.41, 0.61, 0.59)}
ph = {2.0: (0.0, 0.52, 0.18, 0.28), 2.5: (0.0, 0.35, 0.33, 0.43), 3.0: (0.0, 0.35, 0.45, 0.53), 3.5: (0.08, 0.34, 0.46, 0.54),
      4.0: (0.02, 0.32, 0.5, 0.43), 4.5: (0.05, 0.31, 0.55, 0.43), 5.0: (0.12, 0.32, 0.5, 0.42), 5.5: (0.1, 0.32, 0.5, 0.42),
      6.0: (0.08, 0.31, 0.54, 0.43), 6.5: (0.07, 0.3, 0.56, 0.44), 7.0: (0.08, 0.3, 0.57, 0.44), 7.5: (0.08, 0.31, 0.58, 0.43),
      8.0: (0.07, 0.31, 0.52, 0.43), 8.5: (0.0, 0.33, 0.42, 0.42), 9.0: (0.0, 0.35, 0.31, 0.39)}
cr = {0.0: (0.3, 0.03, 0.34, 0.24), 0.5: (0.41, 0.03, 0.34, 0.23), 1.0: (0.65, 0.0, 0.34, 0.25), 10.0: (0.6, 0.02, 0.34, 0.24)}
build(5150, 'B', 'prescription', 'male', [
  ('to hold out a prescription', 'the young man', 'male', man),
  ('to search the shelves', 'the pharmacist', 'female', ph),
  ('to glow above the door', 'the green cross', 'male', cr)],
  4.0, [('shelves', 0.3, 0.15, 'male'), ('a pharmacist', 0.18, 0.53, 'female'), ('a prescription', 0.48, 0.64, 'male'), ('a counter', 0.3, 0.86, 'male')],
  'What is the young man doing?', 'He is giving the pharmacist a prescription.', 'male',
  'Main person = the young man (defaultVoice male). The folded paper is read as the prescription (description). Pharmacist and man are split along a vertical line where their hands meet over the counter (2.5-8.5), so the paper/hands sit in one box or the other. Pharmacist only a sliver at the left edge at 2.0 (min-size box). Green cross only in the door shots (0.0-1.0, 10.0). Still 4.0: she reads the paper; prescription pill on the paper in her hands.')
