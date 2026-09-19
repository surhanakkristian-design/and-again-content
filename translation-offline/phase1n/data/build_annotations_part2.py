#!/usr/bin/env python3
"""Phase 1n — reference annotations, part 2 (sids 160051..160100), label annotator-2.

Deterministic, 0 model calls. Emits data/annotations_part2.json in EXACTLY the 1m format:
{"<sid>": {"hygienised": {...}, "raw": {...}, "tf_gold", "voice_sk", "agent_nom",
           "perfective_present", "tense_open"}}
Schema per phase1m/DATA_HANDOFF.md: inner = {id, t (synthetic 9000+), lv, v, lk (parallel to v), alt}.
Arm B: explicit subject pronouns, no `g` chain. t = 9000 + (sid - 160001).
"""
import json, os, re

# sid: (lv, v, lk, alt, voice_sk, agent_nom, perfective_present, tense_open)
R = {
160051: ("B1",
 ["The old well was covered before the first frost.",
  "That old well was covered up before the first frost.",
  "The old well had been covered before the first frost."],
 ["was covered", "was covered up", "had been covered"],
 {"well": ["well shaft"], "covered": ["covered over", "capped"], "frost": ["freeze"]},
 "passive", False, False, False),

160052: ("A2",
 ["You sanded down the wooden bench on the terrace on Saturday.",
  "On Saturday you sanded that wooden bench on the terrace.",
  "You sanded down the wooden bench on the patio on Saturday."],
 ["sanded down", "sanded", "sanded down"],
 {"terrace": ["patio", "deck"], "bench": ["seat"], "wooden": ["wood"]},
 "active_agent", True, False, False),

160053: ("B2",
 ["By the evening he will have been sanding that parquet floor for eight hours straight.",
  "He will have been sanding the parquet for eight hours in a row by evening."],
 ["will have been sanding", "will have been sanding"],
 {"parquet floor": ["parquet", "hardwood floor", "wooden floor"],
  "straight": ["in a row", "non-stop", "without a break"], "evening": ["tonight"]},
 "active_agent", False, False, False),

160054: ("B1",
 ["The electrician has already replaced all the old switches in our house.",
  "The electrician has replaced all the old light switches in our house already.",
  "The electrician already replaced all the old switches in our house."],
 ["has already replaced", "has replaced", "already replaced"],
 {"switches": ["light switches"], "house": ["home", "building"], "replaced": ["changed", "swapped"]},
 "active_agent", True, False, True),

160055: ("A1",
 ["The new suitcase is light and surprisingly roomy.",
  "That new suitcase is light and surprisingly spacious."],
 ["is", "is"],
 {"suitcase": ["case", "travel case"], "light": ["lightweight"], "roomy": ["spacious"]},
 "active_agent", False, False, False),

160056: ("B2",
 ["He claims that he restocks the display case with new samples every week.",
  "He says he adds new samples to that display cabinet every week.",
  "He claims he tops up the showcase with new samples every week."],
 ["restocks", "adds", "tops up"],
 {"display case": ["display cabinet", "showcase", "cabinet"], "samples": ["specimens"],
  "claims": ["says", "maintains"]},
 "active_agent", True, False, False),

160057: ("B1",
 ["If he catches the first ferry, he will unload the material before lunch.",
  "If he makes the first ferry, he will unload that material before noon."],
 ["will unload", "will unload"],
 {"catches": ["makes", "gets"], "material": ["materials", "load"], "lunch": ["noon", "midday"]},
 "active_agent", True, True, False),

160058: ("A2",
 ["Nobody works in this workshop after eight in the evening.",
  "No one works in this workshop after eight p.m.",
  "People do not work in this workshop after eight in the evening."],
 ["works", "works", "do not work"],
 {"workshop": ["shop", "workroom"], "evening": ["p.m."], "Nobody": ["No one", "Nobody"]},
 "impersonal", False, False, False),

160059: ("B2",
 ["The optician whom they recommended to us ground the new lenses in two days.",
  "The optician they recommended to us ground the new lenses in two days.",
  "The optician that they recommended to us polished the new lenses in two days."],
 ["whom they recommended", "they recommended", "that they recommended"],
 {"optician": ["optometrist"], "ground": ["polished", "cut"], "lenses": ["glasses", "spectacle lenses"]},
 "active_agent", True, False, False),

160060: ("B1",
 ["While the train was standing in the station, the driver topped up the water in the tank.",
  "While the train stood at the station, the engine driver filled the tank with water.",
  "The driver topped up the water in the tank while the train was waiting at the station."],
 ["was standing", "stood", "was waiting"],
 {"driver": ["engine driver", "train driver", "engineer"], "tank": ["water tank"],
  "topped up": ["filled up", "refilled"]},
 "active_agent", True, False, True),

160061: ("A2",
 ["You will be putting those new chairs into the hall all morning.",
  "You are going to be arranging the new chairs in the hall all morning.",
  "You will be stacking those new chairs in the hall all morning."],
 ["will be putting", "are going to be arranging", "will be stacking"],
 {"hall": ["auditorium", "room"], "chairs": ["seats"], "morning": ["morning long"]},
 "active_agent", True, False, False),

160062: ("B2",
 ["If she had come an hour earlier, she would have won that auction.",
  "If she had arrived an hour sooner, she would have won the auction."],
 ["would have won", "would have won"],
 {"come": ["arrived", "got there"], "earlier": ["sooner"], "auction": ["sale"]},
 "active_agent", True, False, False),

160063: ("B1",
 ["The rescuer told us that he had marked the path with new signs.",
  "The paramedic told us he marked the trail with new markers.",
  "The rescuer said to us that he had marked out the path with new signs."],
 ["had marked", "marked", "had marked out"],
 {"rescuer": ["rescue worker", "mountain rescuer", "paramedic"],
  "path": ["trail", "footpath"], "signs": ["markers", "waymarks"]},
 "active_agent", True, False, True),

160064: ("A1",
 ["My aunt knits thick woollen socks for the children every winter.",
  "Every winter my aunt knits the children thick woollen socks."],
 ["knits", "knits"],
 {"woollen": ["woolen", "wool"], "thick": ["heavy"], "children": ["kids"]},
 "active_agent", True, False, False),

160065: ("B2",
 ["The blacksmith will forge two new hinges for that gate by the end of the week.",
  "The smith is going to forge two new hinges for the gate by the end of the week.",
  "The blacksmith will have forged two new hinges for that gate by the end of the week."],
 ["will forge", "is going to forge", "will have forged"],
 {"blacksmith": ["smith"], "gate": ["gateway"], "forge": ["make", "hammer out"]},
 "active_agent", True, True, False),

160066: ("B1",
 ["You will have to return the borrowed tools this week.",
  "You will have to give back the borrowed tools this week.",
  "You are going to have to return those borrowed tools this week."],
 ["will have to return", "have to give back", "have to return"],
 {"tools": ["instruments", "equipment"], "borrowed": ["loaned"], "return": ["bring back"]},
 "active_agent", True, False, False),

160067: ("A2",
 ["Tomas locked the workshop and turned off all the lights above the workbench.",
  "Tomas locked up the workshop and switched off all the lights over the bench."],
 ["locked", "locked up"],
 {"Tomas": ["Tomáš", "Thomas"], "turned off": ["switched off", "put out"],
  "workbench": ["bench", "work table"], "workshop": ["shop"]},
 "active_agent", True, False, False),

160068: ("B2",
 ["The carpenter did not have exact measurements, and nevertheless he hung that shelf perfectly straight.",
  "The joiner had no exact measurements; even so, he hung the shelf perfectly level.",
  "Although the carpenter did not have exact measurements, he hung the shelf completely straight."],
 ["nevertheless", "even so", "Although"],
 {"carpenter": ["joiner", "cabinetmaker"], "measurements": ["measures", "dimensions"],
  "straight": ["level", "even"]},
 "active_agent", True, False, False),

160069: ("B1",
 ["I will return those two books about mountains to you on Tuesday.",
  "On Tuesday I will give you back the two books about the mountains.",
  "I am going to return the two books about mountains to you on Tuesday."],
 ["will return", "give you back", "am going to return"],
 {"return": ["bring back", "give back"], "mountains": ["the mountains", "hills"]},
 "active_agent", True, True, False),

160070: ("A2",
 ["There is a small glass lift at the end of the corridor.",
  "At the end of the corridor there is a small glass elevator."],
 ["There is", "there is"],
 {"lift": ["elevator"], "corridor": ["hallway", "hall", "passage"]},
 "active_agent", False, False, False),

160071: ("B2",
 ["She stated in the email that she had already rewritten the whole conclusion of that report twice.",
  "In her email she said she had rewritten the entire ending of the report twice already.",
  "She wrote in the e-mail that she has already rewritten the whole conclusion of the report twice."],
 ["had already rewritten", "had rewritten", "has already rewritten"],
 {"conclusion": ["ending", "final part", "closing section"], "email": ["e-mail", "mail"],
  "report": ["message"]},
 "active_agent", True, False, True),

160072: ("B1",
 ["If she finds the original plan, she will assemble the whole tower correctly.",
  "If she finds that original plan, she will put together the entire tower properly."],
 ["will assemble", "will put together"],
 {"plan": ["design", "blueprint"], "tower": ["turret"], "correctly": ["properly", "right"]},
 "active_agent", True, True, False),

160073: ("B1",
 ["Every Thursday you carry those heavy crates down to the cellar.",
  "You carry the heavy crates down to the basement every Thursday."],
 ["carry", "carry"],
 {"crates": ["boxes", "cases"], "cellar": ["basement"], "carry": ["take", "haul"]},
 "active_agent", True, False, False),

160074: ("B2",
 ["Somebody must have changed the lock, because the old key no longer fitted.",
  "Someone must have replaced that lock, because the old key did not fit any more."],
 ["must have changed", "must have replaced"],
 {"Somebody": ["Someone"], "fitted": ["fit", "worked"], "lock": ["door lock"]},
 "active_agent", True, False, False),

160075: ("B1",
 ["They informed us that they had repaired the lift back on Wednesday.",
  "They told us they had fixed the elevator as early as Wednesday.",
  "They let us know that they repaired the lift on Wednesday."],
 ["had repaired", "had fixed", "repaired"],
 {"lift": ["elevator"], "repaired": ["fixed", "mended"], "informed": ["told", "notified"]},
 "active_agent", True, False, True),

160076: ("A2",
 ["Do not worry, he will pump up the front wheel for you this evening.",
  "Do not worry, he will inflate your front tyre tonight."],
 ["will pump up", "will inflate"],
 {"pump up": ["inflate", "blow up"], "wheel": ["tyre", "tire"], "this evening": ["tonight"]},
 "active_agent", True, True, False),

160077: ("B1",
 ["The archivist put those letters into new protective covers.",
  "The archivist placed the letters in new protective sleeves."],
 ["put", "placed"],
 {"covers": ["sleeves", "folders", "wrappers"], "letters": ["documents"], "put": ["placed", "filed"]},
 "active_agent", True, False, False),

160078: ("B1",
 ["My mum used to sew costumes for us for the school shows.",
  "My mother would sew costumes for us for school performances.",
  "My mum used to make our costumes for the school shows."],
 ["used to sew", "would sew", "used to make"],
 {"mum": ["mother", "mom"], "shows": ["performances", "concerts", "parties"],
  "costumes": ["outfits"]},
 "active_agent", True, False, True),

160079: ("A2",
 ["On Fridays they hang the washing in the yard behind the house.",
  "They hang the laundry out in the yard behind the house on Friday."],
 ["hang", "hang"],
 {"washing": ["laundry"], "yard": ["courtyard", "garden"], "hang": ["hang out", "put out"]},
 "active_agent", True, False, False),

160080: ("B2",
 ["I wish he had not cut down that old walnut tree so soon.",
  "If only he had not felled the old walnut tree so early."],
 ["had not cut down", "had not felled"],
 {"cut down": ["felled", "chopped down"], "walnut tree": ["walnut", "nut tree"],
  "soon": ["early"]},
 "active_agent", True, False, False),

160081: ("B1",
 ["The bookbinder who was showing us around also opened the locked cellar.",
  "The bookbinder who accompanied us opened even the locked basement.",
  "The bookbinder that guided us also opened the locked cellar."],
 ["who was showing", "who accompanied", "that guided"],
 {"bookbinder": ["binder", "book binder"], "cellar": ["basement"],
  "was showing us around": ["accompanied us", "guided us"]},
 "active_agent", True, False, True),

160082: ("A1",
 ["She is just putting those glass jars into a wooden crate.",
  "Right now she is packing the glasses into a wooden box."],
 ["is just putting", "is packing"],
 {"jars": ["glasses", "tumblers"], "crate": ["box", "case"], "just": ["right now"]},
 "active_agent", True, False, False),

160083: ("B2",
 ["Right now he is assembling that white tent frame on the roof of the annexe.",
  "At this moment he is putting together the white tent structure on the annex roof."],
 ["is assembling", "is putting together"],
 {"tent frame": ["tent structure", "marquee frame"],
  "annexe": ["annex", "extension", "outbuilding"], "Right now": ["At this moment", "Just now"]},
 "active_agent", True, False, False),

160084: ("B1",
 ["They say that he has been varnishing that boat for two weeks now.",
  "They say he has been varnishing the boat for the second week already.",
  "They are saying that he has been lacquering that boat for two weeks."],
 ["has been varnishing", "has been varnishing", "has been lacquering"],
 {"boat": ["dinghy", "small boat"], "varnishing": ["lacquering"]},
 "active_agent", True, False, True),

160085: ("A2",
 ["Dad carried those old magazines up to the attic.",
  "Father took the old magazines up to the loft."],
 ["carried", "took"],
 {"Dad": ["Father", "My father"], "attic": ["loft"], "magazines": ["journals"]},
 "active_agent", True, False, False),

160086: ("B2",
 ["By the end of the month they will have catalogued the whole parish archive.",
  "They will have catalogued the entire parish archive by the end of the month."],
 ["will have catalogued", "will have catalogued"],
 {"catalogued": ["cataloged", "indexed"], "archive": ["archives"], "whole": ["entire"]},
 "active_agent", True, True, False),

160087: ("B1",
 ["Nina grinds those edges more precisely than any of her classmates.",
  "Nina sands the edges more accurately than any of her schoolmates."],
 ["more precisely than", "more accurately than"],
 {"grinds": ["sands", "polishes"], "classmates": ["schoolmates", "fellow students"]},
 "active_agent", True, False, False),

160088: ("B1",
 ["Our uncle carves wooden whistles for the children every summer.",
  "Every summer our uncle whittles wooden whistles for the kids."],
 ["carves", "whittles"],
 {"carves": ["whittles"], "whistles": ["pipes", "flutes"], "children": ["kids"]},
 "active_agent", True, False, False),

160089: ("B2",
 ["The collector is going to lend those drawings to the small town museum.",
  "The collector is going to loan the drawings to a small municipal museum."],
 ["is going to lend", "is going to loan"],
 {"drawings": ["sketches"], "town museum": ["municipal museum", "city museum", "local museum"],
  "lend": ["loan"]},
 "active_agent", True, False, False),

160090: ("B1",
 ["We sort paper and glass into two big bins.",
  "We separate paper and glass into two large baskets."],
 ["sort", "separate"],
 {"bins": ["baskets", "containers"], "big": ["large"], "sort": ["separate", "sort out"]},
 "active_agent", True, False, False),

160091: ("A2",
 ["You will be drying those winter jackets by the stove all evening.",
  "You are going to be drying the winter coats by the stove all evening."],
 ["will be drying", "are going to be drying"],
 {"jackets": ["coats", "anoraks"], "stove": ["fire", "heater", "furnace"]},
 "active_agent", True, False, False),

160092: ("B2",
 ["You will send us the signed forms by Sunday.",
  "You are going to send us those signed forms by Sunday.",
  "You will have sent us the signed forms by Sunday."],
 ["will send", "are going to send", "will have sent"],
 {"forms": ["documents", "form sheets"], "send": ["send in", "mail"]},
 "active_agent", True, True, False),

160093: ("B1",
 ["The librarian told me that he had already leafed through three thick catalogues today.",
  "The librarian told me he has already gone through three thick catalogues today.",
  "The librarian said that he had already flicked through three thick catalogues today."],
 ["had already leafed through", "has already gone through", "had already flicked through"],
 {"catalogues": ["catalogs"], "leafed through": ["gone through", "flicked through", "browsed"],
  "thick": ["fat", "heavy"]},
 "active_agent", True, False, True),

160094: ("A1",
 ["In the evening I will lock the back gate and turn off the lamp.",
  "I am going to lock the back gate and switch off the lamp in the evening."],
 ["will lock", "am going to lock"],
 {"gate": ["garden gate", "little gate"], "turn off": ["switch off", "put out"],
  "lamp": ["light"]},
 "active_agent", True, True, False),

160095: ("B2",
 ["You claimed to us that your colleague had installed the new server.",
  "You told us that your colleague installed the new server.",
  "You maintained to us that your colleague had set up the new server."],
 ["had installed", "installed", "had set up"],
 {"claimed": ["maintained", "insisted", "told us"], "colleague": ["co-worker", "workmate"],
  "installed": ["set up"]},
 "active_agent", True, False, True),

160096: ("B1",
 ["If we get a longer ladder, we will fix the aerial on the roof ourselves.",
  "If we find a longer ladder, we will secure the antenna on the roof ourselves."],
 ["will fix", "will secure"],
 {"get": ["find", "obtain"], "aerial": ["antenna"], "fix": ["secure", "fasten", "mount"]},
 "active_agent", True, True, False),

160097: ("A2",
 ["There are still a few unused envelopes in that box.",
  "In that box there are still a few unused envelopes."],
 ["a few", "a few"],
 {"box": ["carton"], "still": ["left"], "unused": ["new", "unopened"]},
 "active_agent", False, False, False),

160098: ("B2",
 ["In this museum the old clocks are wound every morning.",
  "The old clocks in this museum are wound up every morning.",
  "In this museum they wind the old clocks every morning."],
 ["are wound", "are wound up", "wind"],
 {"clocks": ["timepieces"], "wound": ["wound up"], "museum": ["museum"]},
 "impersonal", False, False, False),

160099: ("B1",
 ["The painters will be repainting that facade all next week.",
  "The painters are going to be repainting the front of the building all next week."],
 ["will be repainting", "are going to be repainting"],
 {"facade": ["façade", "front", "front wall"], "painters": ["decorators"],
  "repainting": ["painting over"]},
 "active_agent", True, False, False),

160100: ("B2",
 ["Next season he will be running that workshop and training two new apprentices.",
  "Next season he will run the workshop and train two new apprentices."],
 ["will be running", "will run"],
 {"running": ["managing", "leading"], "workshop": ["shop", "studio"],
  "apprentices": ["trainees"]},
 "active_agent", True, False, False),
}

HERE = os.path.dirname(os.path.abspath(__file__))
sents = {s["sid"]: s for s in json.load(open(os.path.join(HERE, "sentences.json")))}

out = {}
for sid in range(160051, 160101):
    lv, v, lk, alt, voice_sk, agent_nom, perf, topen = R[sid]
    inner = {"id": sid, "t": 9000 + (sid - 160001), "lv": lv, "v": list(v), "lk": list(lk),
             "alt": {k: list(x) for k, x in alt.items()}}
    out[str(sid)] = {
        "hygienised": json.loads(json.dumps(inner)),
        "raw": json.loads(json.dumps(inner)),
        "tf_gold": sents[sid]["tf_gold"],
        "voice_sk": voice_sk,
        "agent_nom": agent_nom,
        "perfective_present": perf,
        "tense_open": topen,
    }

path = os.path.join(HERE, "annotations_part2.json")
with open(path, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write("\n")

# ---- validation ----
d = json.load(open(path))
errs = []
if len(d) != 50:
    errs.append("key count %d" % len(d))
if sorted(d) != sorted(str(s) for s in range(160051, 160101)):
    errs.append("key set mismatch")
TOP = ["hygienised", "raw", "tf_gold", "voice_sk", "agent_nom", "perfective_present", "tense_open"]
IN = ["id", "t", "lv", "v", "lk", "alt"]
ts, lvs, tfs = set(), {}, {}
for k, a in d.items():
    for f in TOP:
        if f not in a:
            errs.append("%s missing %s" % (k, f))
    if list(a) != TOP:
        errs.append("%s field order %s" % (k, list(a)))
    if a["hygienised"] != a["raw"]:
        errs.append("%s hyg!=raw" % k)
    h = a["hygienised"]
    for f in IN:
        if f not in h:
            errs.append("%s inner missing %s" % (k, f))
    if h["id"] != int(k):
        errs.append("%s id" % k)
    if len(h["v"]) != len(h["lk"]):
        errs.append("%s v/lk %d/%d" % (k, len(h["v"]), len(h["lk"])))
    if not (2 <= len(h["v"]) <= 4):
        errs.append("%s v count %d" % (k, len(h["v"])))
    if h["lv"] != sents[int(k)]["level"]:
        errs.append("%s lv" % k)
    if a["tf_gold"] != sents[int(k)]["tf_gold"]:
        errs.append("%s tf_gold" % k)
    t = sents[int(k)]["tags"]
    if a["agent_nom"] != (t["nom_agent"] and t["passivizable"]):
        errs.append("%s agent_nom" % k)
    if a["perfective_present"] != t["perfective_future"]:
        errs.append("%s perfective_present" % k)
    if (a["voice_sk"] != "active_agent") != t["impersonal_or_passive"] and k not in ("160051",):
        errs.append("%s voice_sk vs tag" % k)
    for ref, lock in zip(h["v"], h["lk"]):
        if lock.lower() not in ref.lower():
            errs.append("%s lock not in ref: %r" % (k, lock))
    for w in h["alt"]:
        if w.lower() not in " ".join(h["v"]).lower():
            errs.append("%s alt key not in v: %r" % (k, w))
    ts.add(h["t"])
    lvs[h["lv"]] = lvs.get(h["lv"], 0) + 1
    tfs[a["tf_gold"]] = tfs.get(a["tf_gold"], 0) + 1
if len(ts) != 50:
    errs.append("t not unique")
# passive-voice references only where the Slovak has no nominative agent
for k, a in d.items():
    for ref in a["hygienised"]["v"]:
        # be-form immediately followed by a past participle = English passive
        pas = re.search(r"\b(am|is|are|was|were|be|been|being)\s+"
                        r"(covered|wound|recommended|installed|replaced|sold|made|built|written|"
                        r"taken|given|sent|opened|locked|marked|repaired|catalogued|forged)\b",
                        ref.lower())
        if pas and a["agent_nom"]:
            errs.append("%s passive-looking ref under agent_nom: %r" % (k, ref))

print("keys", len(d), "| levels", lvs, "| tf", tfs,
      "| tense_open", sum(1 for a in d.values() if a["tense_open"]),
      "| perf_pres", sum(1 for a in d.values() if a["perfective_present"]),
      "| voice", {v: sum(1 for a in d.values() if a["voice_sk"] == v)
                  for v in {a["voice_sk"] for a in d.values()}},
      "| agent_nom", sum(1 for a in d.values() if a["agent_nom"]),
      "| refs", sum(len(a["hygienised"]["v"]) for a in d.values()))
print("ERRORS:", len(errs))
for e in errs:
    print("  -", e)
