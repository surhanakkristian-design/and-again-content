import json,os
H=os.path.dirname(os.path.abspath(__file__));p=H+'/tr.json';t=json.load(open(p))
F=[('69','phrases',2,'bacaklarını düzleştirmek','bacaklarını doğrultmak','düzleştirmek = to flatten; straightening legs is doğrultmak'),
('78','answer',None,'Onlar plajda bir kumdan kale inşa ediyor.','Onlar plajda kumdan bir kale inşa ediyor.','word order: "bir" goes before the head noun'),
('103','phrases',2,'bir beyaz tahtanın üzerinde asılı durmak','bir beyaz tahtanın yukarısında asılı durmak','"üzerinde" reads as "on the whiteboard"; English is "above"'),
('110','answer',None,'O büyük bir kutuyu paketliyor.','O büyük bir kutuyu dolduruyor.','paketlemek = to wrap the box; she is putting things into it'),
('116','answer',None,'O çekiçle fayansları kırıyor.','O çekiçle fayans kırıyor.','indefinite "tiles": no accusative'),
('129','phrases',1,'gri bir kapüşonlu sweatshirt giymek','gri kapüşonlu bir sweatshirt giymek','adjective order, "bir" before the head noun'),
('133','phrases',2,'kameranın içine bakmak','kameraya bakmak','"kameranın içine" is a calque; Turkish says kameraya bakmak'),
('180','question',None,'Kadın nasıl hissediyor?','Kadın kendini nasıl hissediyor?','hissetmek needs the reflexive object'),
('187','question',None,'Kadın nasıl hissediyor?','Kadın kendini nasıl hissediyor?','hissetmek needs the reflexive object'),
('187','answer',None,'O küçük resimler yüzünden şaşkın.','Küçük resimler yüzünden kafası karışmış.','şaşkın = astonished; confused = kafası karışmış'),
('186','phrases',1,'gruba bağırmak','gruba doğru bağırmak','"-e bağırmak" = to shout AT (scold); she shouts to the band'),
('184','phrases',1,'sıkılmış bir yumruğu kaldırmak','sıkılmış bir yumruk kaldırmak','indefinite object: no accusative')]
out=[]
for i,f,k,a,b,w in F:
    cur=t[i][f] if k is None else t[i][f][k]
    assert cur==a,(i,f,cur)
    if k is None: t[i][f]=b
    else: t[i][f][k]=b
    out.append(f'- {i}, {f}{"" if k is None else "["+str(k+1)+"]"}: {a} -> {b} ({w})')
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(3+len(v['nouns'])+2 for v in t.values())
open(H+'/verify_tr.md','w').write(f'''# b004 tr verification

Texts checked: {n} ({len(t)} videos). Fixes: {len(F)}.

## Fixes
'''+'\n'.join(out)+'''

## Doubts left unchanged
- 74: `about` describes a fruit bat, but the phrases/question (woman holding a bat, ball in the air, people on the grass) describe a sports bat; "beyzbol sopası" kept. If the clip is cricket, it should be "kriket sopası".
- 55: "a paddle" = "levha" (auction paddle); Turkish has no fixed short term, "numara levhası" would be clearer but adds a word.
- 58: "to pack her clothes" = "kıyafetlerini yerleştirmek"; acceptable, "kıyafetlerini çantaya koymak" would add a word.
- 123/128: "berries" = "orman meyvesi/meyveleri"; Turkish has no generic word (the clip in 123 shows blueberries).
- 138: "to turn his cap around" = "kepini çevirmek" kept neutral (he turns it backwards and then forward again).
- 158: "a nut" = "fındık" (strictly hazelnut); the generic "kuruyemiş" is unnatural for a single nut.
- 173: "on a high cliff" = "yüksek bir uçurumun tepesinde" (adds "top", natural).
- 176/183: "a sleeve" = "giysi kolu" to avoid the ambiguity of bare "kol" (arm).
- Answers keep the explicit pronoun "O / Onlar" throughout; grammatical, textbook-like, a native speaker would often drop it.
- Several phrases use "bir" + accusative (bir engeli aşmak, bir mektubu sansürlemek, bir biniş kartını okutmak); acceptable as specific indefinites.
''')
print(n,len(F))
