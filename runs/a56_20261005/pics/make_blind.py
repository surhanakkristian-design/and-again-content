# A49: blind cards for one word: the original still + the current candidate of every variant, shuffled; the key apart.
#   python3 make_blind.py <id> <round> caption=path ...   -> blind/<id>_<round>/card_N.jpg + blind/<id>_<round>_key.json
import json, os, sys, random
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); vid, rnd = sys.argv[1], sys.argv[2]
items = [a.split('=', 1) for a in sys.argv[3:]]
random.seed(f'{vid}-{rnd}-a56'); random.shuffle(items)
d = f'{P}/blind/{vid}_{rnd}'; os.makedirs(d, exist_ok=True); key = {}
for i, (cap, path) in enumerate(items, 1):
    im = Image.open(path).convert('RGB'); im.thumbnail((720, 1280)); im.save(f'{d}/card_{i}.jpg', quality=85); key[i] = cap
json.dump(key, open(f'{P}/blind/{vid}_{rnd}_key.json', 'w'), indent=1); print(d, len(key), 'cards')
