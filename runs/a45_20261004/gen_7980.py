from gen_7977_7978_7979_7980_lib import *
bw = keys([(.21,.31,.29,.66),(.21,.30,.30,.69),(.18,.30,.33,.70),(.19,.30,.33,.70),(.16,.29,.34,.71),(.12,.26,.40,.74),(.10,.25,.39,.75),(.07,.25,.43,.75)])
bl = keys([(.50,.31,.26,.66),(.51,.30,.27,.69),(.51,.30,.28,.70),(.52,.30,.29,.70),(.50,.27,.33,.73),(.52,.26,.32,.74),(.49,.25,.37,.75),(.50,.25,.38,.75)])
mn = keys([(.76,.35,.24,.22),(.78,.34,.22,.22),(.79,.34,.21,.22),(.81,.33,.19,.22),(.83,.31,.17,.24),(.84,.30,.16,.25),(.86,.29,.14,.25),(.88,.29,.12,.27)])
write(7980, {"mediaId": 7980, "level": "A", "keyWord": "share", "defaultVoice": "female",
 "taps": [
  {"phrase": "to hold her dress", "target": "the woman with braids", "voice": "female", "keys": bw},
  {"phrase": "to touch her hair", "target": "the blonde woman", "voice": "female", "keys": bl},
  {"phrase": "to pour a drink", "target": "the man", "voice": "male", "keys": mn}],
 "stillS": 0.2,
 "nouns": [{"word": "lights", "x": .30, "y": .13, "voice": "female"}, {"word": "a building", "x": .83, "y": .24, "voice": "female"},
           {"word": "a tree", "x": .12, "y": .38, "voice": "female"}, {"word": "a bar", "x": .84, "y": .70, "voice": "female"}],
 "question": "What are the two women wearing?",
 "answer": ["They", "are", "wearing", "the", "same", "green", "dress."],
 "answerVoice": "female",
 "notes": "Both women point and laugh, so each gets a short action only she does: the woman with braids holds the hem of her dress (2.2-3.2), the blonde woman touches her hair/ear (2.2, 2.7, 3.7). Both moments are short. The man pours only at 0.2-1.2 (holds the bottle after); he is at the right edge behind the bar, narrow box (0.12-0.17 wide) from 2.2 on. Women's boxes split at about x 0.50 where they touch. Bags and dresses are doubled, so not used as nouns. Key word 'share' is a verb."})
