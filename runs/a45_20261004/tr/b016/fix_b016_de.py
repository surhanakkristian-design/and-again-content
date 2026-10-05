import json
p='tr/b016/de.json'
d=json.load(open(p))
fixes=[
("4752","answer",None,"Er verzieht das Gesicht über seine verbrannten Kekse.","Er verzieht beim Anblick seiner verbrannten Kekse das Gesicht.","'das Gesicht über etw. verziehen' is unidiomatic"),
("4759","phrases",0,"an einem Baguette lauschen","an einem Baguette horchen","'lauschen an' is not idiomatic; 'an etw. horchen' is"),
("4772","nouns",2,"ein Marschland","ein Sumpf","'Marschland' is uncountable lowland, not the dictionary equivalent of 'a marsh'"),
("4773","phrases",2,"über ihre Schulter schauen","über die Schulter schauen","own body part takes the definite article in German"),
("4793","phrases",0,"zu den Kindern gestikulieren","den Kindern ein Zeichen geben","'zu jdm. gestikulieren' is unidiomatic"),
("4821","answer",None,"Sie liefert eine Pizza zum Auto.","Sie bringt eine Pizza zum Auto.","'liefern zu' is awkward; 'bringen' natural"),
("4829","phrases",0,"einen Metallschaber fest halten","einen Metallschaber festhalten","spelling: festhalten is one word"),
("4836","phrases",1,"eine Kettensäge fest halten","eine Kettensäge festhalten","spelling: festhalten is one word"),
("4846","phrases",1,"ein Seidenkleid dämpfen","ein Seidenkleid mit Dampf glätten","'dämpfen' means steam-cook/muffle, not steam clothes"),
("4850","phrases",2,"den Daumen nach oben zeigen","den Daumen hochhalten","natural idiom for giving a thumbs up"),
]
log=[]
for vid,f,i,b,a,why in fixes:
    cur=d[vid][f] if i is None else d[vid][f][i]
    assert cur==b,(vid,cur)
    if i is None: d[vid][f]=a
    else: d[vid][f][i]=a
    log.append(f"- {vid} {f}{'' if i is None else '['+str(i)+']'}: {b} -> {a} ({why})")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('tr/b016/verify_de.md','w').write(f"# verify de b016\n\nTexts checked: {n}\n\n## Fixes ({len(fixes)})\n"+"\n".join(log)+"""

## Doubts left unchanged
- 4764 phrases[0] "auf dem Sofa springen": "hüpfen" would be livelier, but correct as is.
- 4815 phrases[2] "den Kopf hinlegen": acceptable for laying the head down on the desk.
- 4813 phrases[1] "über dem Hafen schweben": "soar" could be "segeln", kept.
- 4757 phrases[0] / 4771 "Tor": farm gate could be "Gatter", "Tor" kept for consistency with the gate theme.
- 4795/4805/4854/4855/4859 "glasses" -> "eine Brille": singular is the German equivalent of eyeglasses.
- 4754 "eine Gelbe Karte": capitalised form is accepted (Duden allows both).
""")
print(n,len(fixes))
