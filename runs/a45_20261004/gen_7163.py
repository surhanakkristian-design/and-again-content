from gen_7162_7163_7164_7166_lib import write
W=[(0.32,0.29,0.41,0.71),(0.31,0.31,0.44,0.69),(0.30,0.29,0.48,0.71),(0.30,0.26,0.50,0.74),(0.31,0.26,0.49,0.74),(0.31,0.25,0.50,0.75),(0.30,0.24,0.52,0.76),(0.30,0.23,0.57,0.77)]
S=[(0.04,0.26,0.27,0.44),(0.04,0.26,0.26,0.44),(0.02,0.25,0.27,0.45),(0.02,0.23,0.27,0.47),(0.00,0.23,0.30,0.47),(0.00,0.20,0.30,0.48),(0.00,0.19,0.29,0.50),(0.00,0.19,0.29,0.50)]
B=[(0.74,0.49,0.26,0.51),(0.76,0.49,0.24,0.51),(0.79,0.49,0.21,0.51),(0.81,0.49,0.19,0.51),(0.81,0.49,0.19,0.51),(0.82,0.49,0.18,0.51),(0.82,0.55,0.18,0.45),None]
write(7163, {"mediaId":7163,"level":"A","keyWord":"get sick","defaultVoice":"female",
 "taps":[{"phrase":"to sneeze into a tissue","target":"the woman in white","voice":"female","keys":W},
         {"phrase":"to pull up his scarf","target":"the man in the scarf","voice":"male","keys":S},
         {"phrase":"to read a book","target":"the man with the book","voice":"male","keys":B}],
 "stillS":0.2,
 "nouns":[{"word":"gloves","x":0.47,"y":0.53,"voice":"female"},{"word":"a book","x":0.86,"y":0.71,"voice":"female"},
          {"word":"bread","x":0.65,"y":0.79,"voice":"female"},{"word":"a bag","x":0.67,"y":0.93,"voice":"female"}],
 "question":"What is the woman in white doing?",
 "answer":["She","is","sneezing","into","a","tissue."],"answerVoice":"female",
 "notes":"'get sick' is a phrase, not placed. Two women wear red hats, so the sick one is 'the woman in white' (cream puffer). Her box is cut on the left at the scarf man's face (her left sleeve partly outside). The man with the book is mostly hidden at 3.7 s (only a book corner), set off. The curly-haired woman also holds tissues, so the noun 'a tissue' was avoided; 'gloves' = the sick woman's pair of gloves."})
