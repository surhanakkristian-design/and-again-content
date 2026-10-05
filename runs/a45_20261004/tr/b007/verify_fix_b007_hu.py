import json,os
H=os.path.dirname(os.path.abspath(__file__))
s=json.load(open(H+'/source.json'));p=H+'/hu.json';t=json.load(open(p))
F=[("454","phrases",2,"megölelni a nőt","átölelni a nőt","same verb as the answer (Átöleli) inside one video; ongoing embrace"),
("469","answer",None,"Gyufával meggyújt egy lámpát.","Gyufával gyújt meg egy lámpát.","ongoing action with focused instrument needs the split verb; the unsplit form reads as future/habitual"),
("476","phrases",0,"állítani az élességállító gombot","az élességállító gombot állítani","natural entry word order for a verb without prefix"),
("483","phrases",2,"egy kalappal integetni","egy kalapot lengetni","he waves the hat itself at the monkey; 'kalappal integetni' = to wave hello with a hat"),
("486","phrases",0,"felmenni a hegyre","felvezetni a hegyre","the subject is a path; a path 'felvezet', it does not 'felmegy'"),
("530","phrases",0,"kitárni egy piros szárnyát","kitárni az egyik piros szárnyát","'egy' + possessed noun is ungrammatical; 'az egyik' is the natural form"),
("546","phrases",0,"parfümöt tenni magára","parfümöt fújni magára","natural collocation for putting on (sprayed) perfume"),
("546","answer",None,"Parfümöt tesz a karjára.","Parfümöt fúj a karjára.","same verb as the phrase; natural collocation"),
("549","phrases",0,"egy arany karikát betenni","egy aranykarikát betenni","spelling: material name + noun is written as one word (like aranyérem)"),
("556","phrases",0,"feltartani egy ujját","feltartani az egyik ujját","'egy' + possessed noun is ungrammatical; 'az egyik' is the natural form")]
L=[]
for i,f,k,a,b,w in F:
    cur=t[i][f] if k is None else t[i][f][k]
    assert cur==a,(i,cur)
    if k is None: t[i][f]=b
    else: t[i][f][k]=b
    L.append(f"- {i}, {f}{'' if k is None else '['+str(k+1)+']'}: {a} -> {b} ({w})")
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(5+len(v['nouns']) for v in s.values())
D=["468 mat => 'matrac': the usual word is 'jógamatrac'; bare 'matrac' can read as mattress, kept because the English says only 'mat' and the yoga context is in the answer.",
"513 answer 'A házon kívül esznek.': literal and correct; 'házon kívül enni' without article can mean eating out, 'a ház előtt' would be clearer but changes the English.",
"524 'kétségbeesetten' for 'frantically': close; 'kapkodva' is an alternative.",
"546 'sárga kendőt' for 'a yellow scarf': correct if it is a headscarf/shawl; other videos use 'sál' for a neck scarf. Not visible from the text.",
"549 answer 'fülpiercingjébe': understandable, slightly unusual compound; kept.",
"553 'lapos sapka' for 'a flat cap': calque; 'sildes sapka' is an alternative, no exact Hungarian term.",
"532 'szürke pólót' for 'a grey shirt' (football context) while other videos use 'ing' for shirt; kept as right for the clip.",
"561 'rasztatincsek' for 'dreadlocks': also written 'raszta tincsek'; kept."]
open(H+'/verify_hu.md','w').write(f"# b007 hu verification\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(L)})\n"+"\n".join(L)+"\n\n## Doubts left unchanged\n"+"\n".join("- "+d for d in D)+"\n")
print(n,len(L))
