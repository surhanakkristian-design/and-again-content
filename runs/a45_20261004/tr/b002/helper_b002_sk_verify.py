import json,re
p='tr/b002/sk.json'
raw=open(p,encoding='utf-8').read()
fixes=[
('484','phrases[2]','byť plný vody','byť plné vody','target is "vedro" (neuter): adjective must agree'),
('5117','phrases[2]','byť napchatý knihami','byť napchaté knihami','target is "knižné police" (feminine plural): adjective must agree'),
('5458','phrases[1]','šumieť a sfarbiť sa na oranžovo','šumieť a sfarbiť sa naoranžovo','colour adverbs of this type are written as one word (naoranžovo, nazeleno)'),
('7744','phrases[2]','zalapať po dychu v šoku','zalapať po dychu od šoku','cause is expressed with "od" (as in "od úžasu", "od ľaknutia"); "v šoku" is a calque'),
('36','phrases[2]','vziať svojho miláčika do náručia','vziať svojho domáceho miláčika do náručia','"miláčik" alone means "darling"; "pet" is "domáci miláčik"'),
('376','phrases[1]','peniť cez skaly','peniť na skalách','"peniť cez" is not natural Slovak; the river foams on the rocks'),
('4920','phrases[2]','vyčnievať nad davom','týčiť sa nad davom','"vyčnievať nad" takes the accusative; "týčiť sa nad davom" is the natural static form'),
]
for i,f,a,b,w in fixes:
    assert raw.count('"'+a+'"')==1,(i,raw.count('"'+a+'"'))
    raw=raw.replace('"'+a+'"','"'+b+'"')
json.loads(raw)
open(p,'w',encoding='utf-8').write(raw)
d=json.loads(raw)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
doubts=[
'5149 phrases[2] "svietiť jasnozeleno" / 4206 phrases[2] "žiariť jasnozeleno": adverb is correct, "jasnozeleným svetlom" would be a little more usual.',
'676 phrases[1] "riadiť gondolu": "kormidlovať gondolu" is more precise, "riadiť" is acceptable.',
'278 phrases[1] "nosiť dlhý vrkoč": "mať dlhý vrkoč" is more common, both correct.',
'278 answer "Robia drepy na trávniku." after the singular "skupina" in the question: follows the English "They", acceptable.',
'7154 phrases[1] "popíjať kávu so sebou": colloquial but the established term for takeaway coffee.',
'7145 phrases[1] "fŕkať na muža": "odfrkovať" is closer to "snort", "fŕkať" is acceptable.',
'7450 phrases[1] "siahať dovnútra vázy": "dovnútra" with genitive is codified; "do vnútra vázy" also possible.',
'5417 phrases[1] "naberať cestujúceho": generic masculine kept although the passenger shown is a woman.',
]
with open('tr/b002/verify_sk.md','w',encoding='utf-8') as o:
    o.write(f'# b002 sk verification\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(fixes)})\n')
    for i,f,a,b,w in fixes: o.write(f'- {i} {f}: "{a}" -> "{b}" ({w})\n')
    o.write('\n## Doubts left unchanged\n'); [o.write('- '+x+'\n') for x in doubts]
print(n,len(fixes))
