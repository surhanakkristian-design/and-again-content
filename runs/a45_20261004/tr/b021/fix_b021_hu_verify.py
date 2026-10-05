import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hu.json')
d = json.load(open(P))
fixes = [
 ("5351","answer",None,"Ámulva néz fel a fényfüzérekre.","Felnéz a fényfüzérekre.","'in amazement' added; English answer only says gazing up"),
 ("5355","phrases",1,"felpúposítani a hátát","felpúpozni a hátát","standard verb for a cat arching its back is felpúpozni"),
 ("5356","phrases",2,"a lába fölé hajolva nyújtani","a lábára hajolva nyújtózkodni","'nyújtani' without object is unidiomatic; she lies along her leg"),
 ("5365","phrases",1,"megadóan feltenni a kezét","megadása jeléül feltenni a kezét","'megadóan' means resignedly, not in surrender"),
 ("5365","answer",None,"Megadóan felteszi a kezét.","Megadása jeléül felteszi a kezét.","same fix as the phrase"),
 ("5366","phrases",1,"megadóan feltenni mindkét kezét","megadása jeléül feltenni mindkét kezét","'megadóan' means resignedly, not in surrender"),
 ("5371","phrases",2,"levelekkel borítottnak lenni","levelekkel borítva lenni","natural stative form"),
 ("5373","phrases",0,"ámulatában levegő után kapkodni","ámulatában levegő után kapni","a gasp is a single catch of breath; kapkodni = panting"),
 ("5381","phrases",2,"kávéspoharat tartani","kávéscsészét tartani","cappuccino cups in a cafe are csészék, not poharak"),
 ("5392","phrases",1,"átkarolni a lányt","átkarolni a nőt","same word for the woman as in question/answer"),
 ("5393","nouns",1,"dinoszaurusz-jelmez","dinoszauruszjelmez","two-member compound is written solid (no hyphen)"),
 ("5410","phrases",1,"a tükörre mosolyogni","a tükörbe mosolyogni","one smiles into the mirror (at the reflection)"),
 ("5416","phrases",1,"élénk narancssárgára festettnek lenni","élénk narancssárgára festve lenni","natural stative form"),
 ("5428","phrases",0,"előreinteni a kamiont","beinteni a kamiont","standard verb for waving a truck in"),
 ("5432","phrases",2,"megkongatni a rézharangokat","megcsengetni a rézcsengőket","small stall bells are csengők; harang/kongat = big bells"),
 ("5432","nouns",0,"harangok","csengők","same word as the phrase; small bells"),
 ("5463","phrases",0,"integetni a partnak","integetni a part felé","'integet vminek' unnatural for waving towards the shore"),
 ("5463","nouns",2,"szikla","sziklafal","a cliff is a sziklafal; szikla = rock"),
 ("5471","nouns",1,"fa polc","fapolc","compound written solid (cf. fapadló)"),
 ("5477","phrases",2,"egy kupacba összeesni","egy kupacban összerogyni","natural wording for collapsing in a heap"),
 ("5480","answer",None,"Egy tányért mosogat el.","Egy tányért mosogat.","ongoing action: perfective el- with focus reads as completed"),
]
log = []
for vid, f, i, before, after, why in fixes:
    cur = d[vid][f][i] if i is not None else d[vid][f]
    assert cur == before, (vid, f, cur)
    if i is not None: d[vid][f][i] = after
    else: d[vid][f] = after
    log.append(f"- {vid} {f}{'' if i is None else f'[{i}]'}: {before} -> {after} ({why})")
json.dump(d, open(P, 'w'), ensure_ascii=False, indent=1)
open(os.path.join(os.path.dirname(P), 'verify_hu.md'), 'w').write(
"# verify b021 hu\n\nTexts checked: %d (100 videos: phrases, nouns, question, answer).\n\n## Fixes (%d)\n%s\n\n## Doubts left unchanged\n" % (
 sum(3+len(v['nouns'])+2 for v in d.values()), len(log), "\n".join(log)) +
"- 5439 phrases[2] 'négy férfit betakarni': betakarni leans to blanket-covering; acceptable for an umbrella, left.\n"
"- 5438 'gombóc' for half-moon fruit dumplings (closer: derelye); English is generic 'dumpling', left.\n"
"- 5372 answer 'Összesöpri a leveleket.' perfective for an ongoing action; acceptable in Hungarian, left.\n"
"- 5442 'aláöltözetre vetkőzni' (strip to his thermals); colloquially fine, left.\n"
"- 5360 'szőkített hajat viselni' for 'to have bleached hair'; acceptable entry form, left.\n")
print(len(log))
