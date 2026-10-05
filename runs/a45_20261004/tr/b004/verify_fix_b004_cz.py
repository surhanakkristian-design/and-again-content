import json
p='tr/b004/cz.json'
raw=open(p,encoding='utf-8').read()
d=json.loads(raw)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
F=[
('55','answer',None,'Přihazuje v aukci.','Přihazuje na aukci.','being at an auction event is "na aukci"'),
('65','phrases',0,'skládat zeleninu','rozkládat zeleninu','she spreads the vegetables out in one layer; "skládat" = stack/fold'),
('76','phrases',1,'mít na sobě šedou čepici','mít na hlavě šedou čepici','headwear is worn "na hlavě"'),
('84','phrases',1,'nasadit si pásek','vzít si pásek','"nasadit si" is not used with a belt; natural collocation'),
('88','phrases',1,'otáčet hlavu','otáčet hlavou','moving a body part takes the instrumental'),
('110','phrases',1,'dotýkat se kočičích zad','dotýkat se zad kočky','"kočičích" reads as "cat-like/of cats"; the back of this one cat'),
('146','phrases',2,'viset z větve','viset na větvi','idiomatic Czech: something hangs "na větvi"'),
('147','phrases',1,'mít na sobě žlutou helmu','mít na hlavě žlutou helmu','headwear is worn "na hlavě"'),
('149','phrases',2,'být otevřený dokořán','být otevřená dokořán','agreement with "zásuvka" (feminine), the word used in this video'),
('157','phrases',0,'otevírat žvýkačku','rozbalovat žvýkačku','a stick of gum is unwrapped, "otevírat žvýkačku" is not Czech'),
('157','question',None,'Co otevírá žena?','Co rozbaluje žena?','same verb as the phrase'),
('157','answer',None,'Otevírá žvýkačku.','Rozbaluje žvýkačku.','same verb as the phrase'),
('162','phrases',0,'ukazovat na svá ústa','ukazovat si na ústa','own body part: dative reflexive, not possessive'),
('170','phrases',1,'čistit okno','mýt okno','windows are "mýt" (spray and wipe), natural collocation'),
]
lines=[]
for i,f,ix,b,a,why in F:
    if ix is None:
        assert d[i][f]==b,(i,f,d[i][f]); d[i][f]=a; fn=f
    else:
        assert d[i][f][ix]==b,(i,f,d[i][f][ix]); d[i][f][ix]=a; fn=f'{f}[{ix+1}]'
    lines.append(f'- {i}, {fn}: "{b}" -> "{a}" ({why})')
open(p,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=1)+('\n' if raw.endswith('\n') else ''))
doubts=[
'- 55 "cedulka" for the auction paddle: "dražební plácačka/terčík" is the trade word, "cedulka" is understandable and consistent in the video.',
'- 74 "pálka": the about text describes a fruit bat, the phrases (woman holding it, ball in the air) point to the sports bat; kept.',
'- 75 "kožnatými křídly": literal "leathery"; "blanitými" is the zoological word. Kept as the closer rendering of the English.',
'- 91/152/171/180 "zkřížit si ruce": correct; "založit si ruce" (used in 85 for "fold") is the more common idiom.',
'- 171 answer "Má zkřížené ruce." renders the ongoing action as a state; natural Czech, kept.',
'- 120 "péct maso" for a patty on a grill: "opékat/grilovat" would be more exact than the English "cook".',
'- 123/128 "bobule": correct generic for "berries" but bookish; the clip shows blueberries.',
'- 127 "trny": colloquial for cactus spines; "ostny" is also used.',
'- 170 "uklízečka": matches "cleaner"; a hotel cleaner is usually "pokojská".',
'- 174 "laboratorní plášť": literal; a doctor wears a "lékařský/bílý plášť".',
'- 176 "obsahovat plápolající oheň": stiff, mirrors the equally stiff English "contain".',
'- 180 "vysoké boty" for "boots": acceptable; "boty" alone would lose the sense.',
]
open('tr/b004/verify_cz.md','w',encoding='utf-8').write(
 f'# b004 cz verification\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(F)})\n'+'\n'.join(lines)+'\n\n## Doubts left unchanged\n'+'\n'.join(doubts)+'\n')
print(n,len(F))
