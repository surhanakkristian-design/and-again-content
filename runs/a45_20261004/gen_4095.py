import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, d):
    out = []
    for t in times:
        if t in d:
            x, y, w, h = d[t]; out.append({"t": t, "x": x, "y": y, "w": w, "h": h})
        else: out.append({"t": t, "off": True})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def write(vid, c):
    json.dump(c, open(f'{HERE}/content/{vid}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 4095
t = T(30)
police = {0.5: (0, .42, .12, .13), 1.0: (0, .43, .09, .14), 1.5: (0, .42, .11, .14), 2.0: (0, .39, .33, .20), 2.5: (.14, .33, .61, .27)}
man = {6.5: (0, 0, .26, .32), 7.0: (0, .06, .29, .37), 7.5: (0, .12, .30, .46), 8.0: (0, .17, .29, .42), 8.5: (0, .21, .30, .40),
       9.0: (0, .24, .30, .40), 9.5: (.02, .26, .28, .40), 10.0: (.04, .27, .28, .40), 10.5: (.05, .27, .29, .40)}
woman = {7.0: (.87, .21, .13, .60), 7.5: (.81, .23, .19, .70), 8.0: (.76, .25, .24, .54), 8.5: (.75, .27, .25, .50),
         9.0: (.72, .30, .22, .60), 9.5: (.73, .31, .18, .58), 10.0: (.71, .30, .20, .46), 10.5: (.73, .31, .19, .46)}
write(4095, {"mediaId": 4095, "level": "A", "keyWord": "movie", "defaultVoice": "male",
 "taps": [
  {"phrase": "to follow another car", "target": "the police car", "voice": "male", "keys": keys(t, police)},
  {"phrase": "to wear a blue jacket", "target": "the woman in the blue jacket", "voice": "female", "keys": keys(t, woman)},
  {"phrase": "to wear sunglasses", "target": "the man in sunglasses", "voice": "male", "keys": keys(t, man)}],
 "stillS": 10.0,
 "nouns": [{"word": "the sky", "x": 0.45, "y": 0.10, "voice": "male"}, {"word": "sunglasses", "x": 0.18, "y": 0.35, "voice": "male"},
           {"word": "a tablet", "x": 0.77, "y": 0.47, "voice": "male"}, {"word": "a screen", "x": 0.37, "y": 0.56, "voice": "male"}],
 "question": "What are the people making?",
 "answer": ["They", "are", "making", "a", "movie."], "answerVoice": "male",
 "notes": "Clip with cuts: car chase (0-2.5), view from inside a car (3.0-5.5), film crew at a monitor (6.0-10.5), small camera on a car (11.0-12.0), two cars from behind (12.5-14.5). The chased car is red at 0.0-0.5 and yellow at 1.0-1.5, so no phrase uses its colour and it is not a target. Police car: off at 0.0 (only its lights behind the first car), narrow boxes at 0.5-1.5 because the first car covers it; off for the tiny flashing lights behind the crew (8.0-10.5) and for the two unclear cars at 13.0-14.5. The crew only stand and watch, and several of them hold a tablet or a notepad, so the woman on the right gets a state phrase (the only blue denim jacket); the noun 'a tablet' sits on her black tablet (the dark-haired woman next to her holds a smaller dark pad). The man in sunglasses also gets a state phrase for the same reason. Key word 'movie' is not a visible thing; it is in the answer (crew + monitor + camera show a film shoot). Mixed group, odd id -> default voice male."})

# ---------- 4096
t = T(31)
M = {0.5: (0, 0, .60, .21), 1.0: (0, 0, .62, .22), 1.5: (0, 0, .70, .18), 2.0: (0, 0, .68, .24), 2.5: (0, 0, .88, .28), 3.0: (0, 0, .72, .40),
     3.5: (0, 0, .82, .38), 4.0: (0, 0, .78, .29), 4.5: (0, 0, .80, .30), 5.0: (0, 0, .78, .29), 5.5: (0, 0, .80, .30), 6.0: (0, 0, .78, .26),
     6.5: (0, 0, .85, .26), 7.0: (0, 0, .88, .27), 7.5: (0, 0, .92, .27), 8.0: (0, 0, 1.0, .27), 8.5: (0, 0, 1.0, .25),
     10.5: (0, 0, 1.0, .30), 11.0: (0, 0, 1.0, .25), 11.5: (0, 0, .95, .26), 12.0: (.10, 0, .50, .14), 12.5: (0, 0, .30, .18), 15.0: (0, 0, .52, .58)}
Tu = {0.5: (.05, .22, .73, .45), 1.0: (.05, .23, .75, .47), 1.5: (.05, .19, .80, .50), 2.0: (0, .25, .85, .45), 2.5: (0, .29, 1.0, .31),
      3.0: (0, .41, .95, .34), 3.5: (0, .39, 1.0, .19), 4.0: (0, .30, 1.0, .22), 4.5: (0, .31, 1.0, .26), 5.0: (0, .30, 1.0, .30),
      5.5: (0, .31, 1.0, .30), 6.0: (0, .27, 1.0, .33), 6.5: (0, .27, 1.0, .34), 7.0: (0, .28, 1.0, .31), 7.5: (0, .28, 1.0, .31),
      8.0: (0, .28, 1.0, .31), 8.5: (0, .26, 1.0, .30), 10.0: (.15, .40, .58, .32), 10.5: (.10, .31, .90, .42), 11.0: (0, .33, 1.0, .38),
      11.5: (0, .30, 1.0, .40), 12.0: (0, .26, 1.0, .68), 12.5: (0, .22, 1.0, .64), 13.0: (.18, .37, .73, .44), 13.5: (.24, .35, .60, .28),
      14.0: (.23, .34, .49, .21), 14.5: (.46, .38, .36, .20), 15.0: (.56, .43, .40, .19)}
K = {3.5: (.66, .58, .34, .22), 4.0: (.56, .52, .44, .24), 4.5: (.48, .57, .52, .26), 5.0: (.40, .60, .60, .30), 5.5: (.46, .61, .54, .30),
     6.0: (.46, .60, .54, .30), 6.5: (.44, .61, .56, .30), 7.0: (.47, .59, .53, .30), 7.5: (.47, .59, .53, .20), 8.0: (.38, .59, .62, .22),
     8.5: (.47, .56, .53, .20)}
write(4096, {"mediaId": 4096, "level": "A", "keyWord": "free", "defaultVoice": "male",
 "taps": [
  {"phrase": "to swim away", "target": "the turtle", "voice": "male", "keys": keys(t, Tu)},
  {"phrase": "to cut the rope", "target": "the knife", "voice": "male", "keys": keys(t, K)},
  {"phrase": "to wear black shorts", "target": "the man", "voice": "male", "keys": keys(t, M)}],
 "stillS": 15.0,
 "nouns": [{"word": "a man", "x": 0.20, "y": 0.14, "voice": "male"}, {"word": "a turtle", "x": 0.74, "y": 0.52, "voice": "male"},
           {"word": "a net", "x": 0.22, "y": 0.70, "voice": "male"}, {"word": "sand", "x": 0.70, "y": 0.85, "voice": "male"}],
 "question": "What is the turtle doing?",
 "answer": ["It", "is", "swimming", "away", "from", "the", "net."], "answerVoice": "male",
 "notes": "Tight underwater close-up; targets lie on top of each other, so the boxes are split in horizontal bands: the man (snorkeller above, arms, black shorts, yellow fins) at the top, the turtle in the net in the middle, the knife with the hand that holds it below (3.5-8.5). The bands cut off parts: the man's hands on the net fall into the turtle band, the turtle's lower flipper into the knife band. The hands coming from the left and from below belong to the person filming and are in no box. All off at 0.0 (murky), 9.0 and 9.5 (only hands and rope). The man is only fins at 12.0-12.5; his shorts show at 0.5-8.0 and 15.0. He only helps with his hands like the filming person, so he gets a state phrase. Before 10.5 the turtle is inside the net (box = the turtle in the net). Key word 'free' (adjective) is not in the texts: the answer shows it (the turtle swims away from the net). Default voice male: the people shown are men."})

# ---------- 4097
t = T(31)
R = {0.0: (.37, .23, .18, .14), 0.5: (.36, .20, .18, .14), 1.0: (.35, .15, .18, .14), 1.5: (.36, .04, .18, .15), 2.0: (.39, .07, .19, .15),
     2.5: (.39, .15, .19, .15), 3.0: (.38, .23, .19, .15), 3.5: (.36, .30, .18, .15), 4.0: (.36, .36, .18, .15), 4.5: (.35, .42, .18, .15),
     5.0: (.35, .43, .18, .14), 5.5: (.36, .33, .18, .14), 6.0: (.38, .26, .19, .14), 6.5: (.40, .26, .21, .14), 7.0: (.37, .22, .20, .14),
     7.5: (.20, .19, .19, .17), 8.0: (.17, .24, .20, .15), 8.5: (.18, .27, .20, .14), 9.0: (.27, .27, .18, .14), 9.5: (.33, .25, .18, .14),
     10.0: (.33, .23, .18, .14), 10.5: (.34, .11, .18, .15), 11.0: (.34, .08, .21, .15), 11.5: (.33, .20, .22, .17), 12.0: (.33, .37, .18, .15),
     12.5: (.33, .45, .18, .14), 13.0: (.35, .38, .18, .14), 13.5: (.36, .27, .18, .14), 14.0: (.37, .21, .18, .14), 14.5: (.35, .18, .18, .14),
     15.0: (.32, .21, .18, .14)}
kk = keys(t, R)
write(4097, {"mediaId": 4097, "level": "A", "keyWord": "fast", "defaultVoice": "male",
 "taps": [
  {"phrase": "to jump high into the air", "target": "the rider", "voice": "male", "keys": kk},
  {"phrase": "to ride in front", "target": "the rider", "voice": "male", "keys": kk},
  {"phrase": "to wear a white shirt", "target": "the rider", "voice": "male", "keys": kk}],
 "stillS": 2.5,
 "nouns": [{"word": "the sky", "x": 0.28, "y": 0.07, "voice": "male"}, {"word": "a rider", "x": 0.50, "y": 0.22, "voice": "male"},
           {"word": "a hill", "x": 0.72, "y": 0.50, "voice": "male"}, {"word": "a wheel", "x": 0.46, "y": 0.63, "voice": "male"}],
 "question": "How fast is the rider going?",
 "answer": ["The", "rider", "is", "going", "very", "fast."], "answerVoice": "male",
 "notes": "Helmet-camera clip: the only person in the picture is the small rider ahead (white shirt, dark trousers, helmet), so all three phrases use this one target; the filming rider shows only his own front wheel, handlebar, gloves and shoes. The rider is small, so the box is the minimum size around him in every frame; he is in the air at 1.5-3.5 and 10.5-11.5. The rider's gender cannot be seen: target and answer say 'the rider', voice = default (odd id -> male). Still 2.5: 'a hill' is on the brown earth mound in the middle (green hills lie far behind it), 'a wheel' on the front wheel of the camera bike. 'rider' may be upper A2."})

# ---------- 4098
t = T(31)
H = {0.0: (.33, .14, .20, .18), 0.5: (.32, .11, .22, .24), 1.0: (.27, .09, .31, .33), 1.5: (0, .02, .64, .60),
     2.5: (.35, .16, .20, .13), 3.0: (.33, .16, .24, .15), 3.5: (.28, .11, .28, .22), 4.0: (.19, .03, .33, .31), 4.5: (.18, 0, .34, .31),
     5.0: (.22, 0, .35, .31), 5.5: (.27, .08, .35, .30), 6.0: (.31, .15, .32, .28), 6.5: (.33, .17, .32, .28), 7.0: (.33, .18, .32, .28),
     7.5: (.33, .19, .32, .27), 8.0: (.34, .17, .31, .28), 8.5: (.33, .18, .32, .27), 9.0: (.33, .18, .32, .28), 9.5: (.33, .19, .32, .27),
     10.0: (.34, .17, .31, .28), 10.5: (.36, .17, .32, .27), 11.0: (.36, .15, .34, .29), 11.5: (.33, .15, .35, .29), 12.0: (.24, .12, .38, .34),
     12.5: (0, .14, .55, .36), 13.0: (0, .14, .50, .56)}
C = {2.5: (.42, .29, .22, .15), 3.0: (.38, .31, .30, .21), 3.5: (.40, .33, .34, .27), 4.0: (.38, .34, .19, .34), 4.5: (.38, .40, .24, .32),
     5.0: (.28, .42, .37, .32), 5.5: (.38, .43, .52, .34), 6.0: (.45, .47, .47, .31), 6.5: (.47, .48, .47, .31), 7.0: (.47, .49, .47, .32),
     7.5: (.47, .48, .47, .32), 8.0: (.45, .48, .48, .31), 8.5: (.47, .48, .47, .31), 9.0: (.47, .49, .47, .32), 9.5: (.47, .48, .47, .32),
     10.0: (.45, .48, .48, .31), 10.5: (.47, .47, .50, .29), 11.0: (.50, .50, .50, .22), 11.5: (.58, .52, .42, .16)}
Rh = {0.0: (.80, .76, .20, .17), 0.5: (.82, .66, .18, .15), 1.0: (.82, .62, .18, .15), 1.5: (.82, .58, .18, .14), 2.0: (.82, .64, .18, .15),
      2.5: (.82, .62, .18, .15), 3.0: (.76, .60, .24, .14), 3.5: (.70, .60, .30, .16), 4.0: (.57, .40, .43, .50), 4.5: (.62, .42, .38, .50),
      5.0: (.65, .45, .35, .50), 5.5: (.74, .82, .26, .16), 6.0: (.72, .81, .28, .18), 6.5: (.75, .82, .25, .18), 7.0: (.75, .83, .25, .17),
      7.5: (.75, .83, .25, .17), 8.0: (.75, .82, .25, .18), 8.5: (.75, .82, .25, .18), 9.0: (.75, .83, .25, .17), 9.5: (.75, .83, .25, .17),
      10.0: (.75, .82, .25, .18), 10.5: (.78, .77, .22, .15), 11.0: (.76, .72, .24, .16), 11.5: (.78, .68, .22, .14), 12.0: (.82, .74, .18, .17),
      12.5: (.82, .72, .18, .16), 14.5: (.82, .72, .18, .16), 15.0: (.82, .76, .18, .17)}
write(4098, {"mediaId": 4098, "level": "B", "keyWord": "way", "defaultVoice": "male",
 "taps": [
  {"phrase": "to push the calf aside", "target": "the rider's right hand", "voice": "male", "keys": keys(t, Rh)},
  {"phrase": "to tilt its head sideways", "target": "the calf", "voice": "male", "keys": keys(t, C)},
  {"phrase": "to have long curved horns", "target": "the cow with horns", "voice": "male", "keys": keys(t, H)}],
 "stillS": 8.0,
 "nouns": [{"word": "a bell", "x": 0.47, "y": 0.35, "voice": "male"}, {"word": "a track", "x": 0.40, "y": 0.46, "voice": "male"},
           {"word": "a calf", "x": 0.68, "y": 0.60, "voice": "male"}, {"word": "a glove", "x": 0.86, "y": 0.90, "voice": "male"}],
 "question": "What are the animals doing?",
 "answer": ["They", "are", "blocking", "the", "rider's", "way."], "answerVoice": "male",
 "notes": "Helmet-camera clip; the rider shows only as gloves, an arm and knees. Target 1 is his right hand in the black glove: it pushes the calf's head aside at 4.0-5.0 and lies on the handlebar grip in the other frames (off at 13.0-14.0, out of frame); the left glove is in no box. At 4.0-5.0 the hand lies on the calf's head, so the two boxes are split by a vertical line and the calf box holds only the left part of its head. The calf = the young animal without horns with yellow ear tags (from 2.5); its head is tilted sideways from the push on (4.5-10.5). 'The cow with horns': the horned cow that walks at the camera at 0.0-1.5 has a brown face, the horned cow standing on the track from 2.5 has a white face - the clip treats them as one animal and so does the box (off at 2.0 where only a headless body passes; at 13.0 only its body, at 13.5 only the tail = off). Cows behind it at 0.0-1.0 have short horns too, hence 'long curved horns'. The cows wear bells, but no phrase uses that (the calf has a small one as well). Rider's gender is not certain (bare arm and knees look male) -> default voice male; if judged 'no main person', the even id would give female. Key word 'way' is in the answer."})
