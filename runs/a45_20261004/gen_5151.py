from lib_5147_5148_5150_5151 import build
man = {0.0: (0, 0.03, 1, 0.97), 0.5: (0, 0.03, 1, 0.49), 1.0: (0, 0.04, 1, 0.37), 1.5: (0, 0.04, 1, 0.31),
       2.0: (0, 0.03, 1, 0.32), 2.5: (0, 0.03, 1, 0.32), 3.0: (0, 0.04, 1, 0.31), 3.5: (0, 0.04, 1, 0.31),
       4.0: (0, 0.03, 1, 0.3), 4.5: (0, 0.03, 1, 0.3),
       5.0: (0.52, 0.23, 0.48, 0.3), 5.5: (0.53, 0.22, 0.47, 0.3),
       6.0: (0.26, 0.7, 0.74, 0.3), 6.5: (0.25, 0.68, 0.75, 0.32), 7.0: (0.15, 0.68, 0.85, 0.32), 7.5: (0.15, 0.68, 0.85, 0.32),
       8.0: (0.15, 0.68, 0.85, 0.32), 8.5: (0.15, 0.68, 0.85, 0.32), 9.0: (0.15, 0.68, 0.85, 0.32),
       9.5: (0.66, 0.35, 0.34, 0.65), 10.0: (0.68, 0.35, 0.32, 0.6), 10.5: (0.7, 0.35, 0.3, 0.57), 11.0: (0.7, 0.37, 0.3, 0.52),
       11.5: (0.7, 0.37, 0.3, 0.52), 12.0: (0.69, 0.36, 0.31, 0.49)}
pic = {0.5: (0, 0.53, 0.84, 0.35), 1.0: (0, 0.42, 0.88, 0.58), 1.5: (0, 0.36, 0.9, 0.6), 2.0: (0, 0.36, 0.92, 0.6),
       2.5: (0, 0.36, 0.95, 0.6), 3.0: (0.05, 0.36, 0.85, 0.55), 3.5: (0.03, 0.36, 0.91, 0.55), 4.0: (0.02, 0.34, 0.92, 0.57),
       4.5: (0.01, 0.34, 0.93, 0.57),
       5.0: (0.48, 0.54, 0.46, 0.28), 5.5: (0.5, 0.53, 0.45, 0.29),
       6.0: (0.28, 0.2, 0.6, 0.49), 6.5: (0.2, 0.19, 0.6, 0.48), 7.0: (0.18, 0.2, 0.6, 0.47), 7.5: (0.18, 0.2, 0.6, 0.47),
       8.0: (0.18, 0.2, 0.6, 0.47), 8.5: (0.18, 0.2, 0.6, 0.47), 9.0: (0.18, 0.2, 0.6, 0.47),
       9.5: (0.43, 0.36, 0.18, 0.16), 10.0: (0.43, 0.36, 0.18, 0.15), 10.5: (0.44, 0.36, 0.18, 0.15), 11.0: (0.42, 0.35, 0.18, 0.15),
       11.5: (0.42, 0.36, 0.18, 0.15), 12.0: (0.42, 0.35, 0.18, 0.15)}
build(5151, 'A', 'frame', 'male', [
  ('to hold up a picture', 'the old man', 'male', man),
  ('to use a hammer', 'the old man', 'male', man),
  ('to show a white house', 'the new picture', 'male', pic)],
  4.0, [('glasses', 0.5, 0.18, 'male'), ('mountains', 0.55, 0.5, 'male'), ('a house', 0.46, 0.64, 'male'), ('a frame', 0.5, 0.86, 'male')],
  'What is the old man doing?', 'He is hanging a picture on the wall.', 'male',
  'Only one person; the new picture (silver frame, mountain valley with a white red-roofed house) is the second target. Picture still wrapped in brown paper at 0.0 (off). He holds the picture in front of his body (0.5-4.5) and in the wall shots his hands are on it (5.0-9.0), so man and picture boxes are split horizontally: man above (head/shoulders) or below (arm) or the hammer hand (5.0-5.5); some hand parts fall in the picture box. At 5.0-5.5 the upper part of the frame sits in the man/hammer box. Wide shots 9.5-12.0: picture box is my best guess at the silver frame with mountains in the middle of the wall (small, min-size box) - verifier please check. Still 4.0: frame pill on the bottom of the silver frame.')
