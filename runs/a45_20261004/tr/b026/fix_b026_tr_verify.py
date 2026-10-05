import json
t=json.load(open('tr.json'))
fixes=[
('7070','nouns',0,'barmen kız','kadın barmen','"barmen kız" is colloquial; neutral dictionary form for barmaid'),
('7070','nouns',2,'yer fıstığı','yer fıstıkları','English plural must stay plural'),
('7073','phrases',2,'baş üstündeki iskeleyi tutmak','başının üstündeki iskeleyi tutmak','"baş üstü" is an idiom (gladly); overhead = başının üstündeki'),
('7075','nouns',1,'kara tahta','karatahta','TDK spelling is one word'),
('7083','phrases',2,'alnına vurmak','alnına hafifçe vurmak','tap = light touch, not hit'),
('7083','answer',None,'Alnına vuruyor.','Alnına hafifçe vuruyor.','same as phrase: tap, not hit'),
('7089','phrases',0,'dev bir süngere yüklenmek','dev bir süngeri itmek','"yüklenmek" is vague/colloquial; push against = itmek'),
('7089','question',None,'Fil sünger ne yapıyor?','Fil şeklindeki sünger ne yapıyor?','"fil sünger" is ungrammatical; elephant-shaped sponge'),
('7089','answer',None,'Fil sünger şişiyor.','Fil şeklindeki sünger şişiyor.','same as question'),
('7092','phrases',1,'heykele sırıtmak','heykele bakıp sırıtmak','"sırıtmak" does not take a dative object naturally; grin at = bakıp sırıtmak'),
('7092','answer',None,'Eriyen heykele sırıtıyor.','Eriyen heykele bakıp sırıtıyor.','same as phrase'),
('7096','phrases',1,'direksiyonda oturmak','direksiyon başında oturmak','natural collocation for sitting at the wheel'),
('7097','nouns',3,'kulak çubukları','pamuklu çubuklar','restoration swabs, not ear buds'),
('7097','answer',None,'Büstü bir kulak çubuğuyla ovuyor.','Büstü pamuklu bir çubukla ovuyor.','same as noun'),
('7100','phrases',1,'foka bakmak','foka uzun uzun bakmak','gaze = look long, not just look'),
('7100','nouns',3,'deniz kanosu','deniz kayağı','standard Turkish term for sea kayak'),
('7104','question',None,'Yeşilli adam ne yapıyor?','Yeşil giyimli adam ne yapıyor?','"yeşilli" is slangy; standard = yeşil giyimli'),
('7105','phrases',1,'varak altın sürmek','altın varak sürmek','fixed term is "altın varak"'),
('7107','phrases',1,'başını arkaya eğmek','başını geriye yatırmak','tilt the head back = geriye yatırmak'),
('7110','nouns',2,'peri ışıkları','süs ışıkları','"peri ışıkları" is a calque; Turkish says süs ışıkları'),
('7113','question',None,'Sarılı kadın ne yapıyor?','Sarı giyimli kadın ne yapıyor?','"sarılı" also means "wrapped"; standard = sarı giyimli'),
('7114','question',None,'Sarılı kadın ne yapıyor?','Sarı giyimli kadın ne yapıyor?','"sarılı" ambiguous (wrapped)'),
('7116','phrases',0,'pirinç bir direkten kaymak','pirinç bir direkten kayarak inmek','slide down = kayarak inmek (as in 7157)'),
('7117','question',None,'Sarılı kadın ne yapıyor?','Sarı giyimli kadın ne yapıyor?','"sarılı" ambiguous (wrapped)'),
('7121','phrases',0,'güçlü bir ışık huzmesi göndermek','güçlü bir ışık huzmesi yaymak','a beam is "yaymak", not "göndermek"'),
('7125','phrases',0,'havada bir bozuk parayı yakalamak','bir bozuk parayı havada yakalamak','natural word order'),
('7125','answer',None,'Yazı tura atıyor.','Bozuk parayı havaya atıyor.','"yazı tura atmak" = decide by coin toss; English only says flipping'),
('7131','phrases',2,'beyaz bir gelinlik giymek','beyaz bir elbise giymek','English says dress, not wedding dress'),
('7134','question',None,'Beyazlı oyuncu ne yapıyor?','Beyaz formalı oyuncu ne yapıyor?','"beyazlı" is slangy; player in white = beyaz formalı (cf. 7095)'),
('7136','phrases',1,'el ele tutuşarak karşıya yürümek','el ele tutuşarak suyun içinden karşıya geçmek','wade = walk through water; missing'),
('7140','phrases',1,'sandalyesinden el kol hareketleri yapmak','oturduğu sandalyeden el kol hareketleri yapmak','"sandalyesinden" alone reads as moving off the chair'),
('7142','nouns',0,'gönye testere','gönye testeresi','compound needs the possessive suffix'),
('7147','phrases',1,'havada bir tavayı yakalamak','bir tavayı havada yakalamak','natural word order'),
('7147','phrases',2,'kumda yürüyüş yapmak','kumda gezinmek','stroll = gezinmek; yürüyüş yapmak = go for a hike/walk'),
('7147','answer',None,'Havada bir tavayı yakalıyor.','Bir tavayı havada yakalıyor.','natural word order'),
('7148','nouns',3,'galeri','veranda','here "gallery" is the covered porch; galeri is the wrong sense'),
('7153','answer',None,'Bir sis makinesinin yanında çömeliyor.','Bir sis makinesinin yanında çömelmiş duruyor.','ongoing posture = çömelmiş duruyor (cf. 7169)'),
('7162','phrases',0,'bir tutam yüne sarılmak','bir yığın yüne sarılmak','"tutam" is a pinch; a bundle you hug is a yığın'),
('7162','answer',None,'Bir tutam yüne sarılıyor.','Bir yığın yüne sarılıyor.','same as phrase'),
('7163','phrases',0,None,None,None),
('7163','question',None,'Beyazlı kadın ne yapıyor?','Beyaz giyimli kadın ne yapıyor?','"beyazlı" is slangy; standard = beyaz giyimli'),
('7168','phrases',1,'yolcu koltuğuna binmek','yolcu koltuğuna oturmak','one does not "binmek" a seat'),
('7168','nouns',3,'taç yaprakları','çiçek yaprakları','botanical term; everyday word for loose petals'),
('7169','nouns',0,'peri ışıkları','süs ışıkları','calque; Turkish says süs ışıkları'),
('7172','phrases',2,'ellerini kavuşturarak izlemek','ellerini kenetleyerek izlemek','"kavuşturmak" is for arms; clasped hands = kenetlemek'),
('7172','question',None,'Sarılı kadın ne yapıyor?','Sarı giyimli kadın ne yapıyor?','"sarılı" ambiguous (wrapped)'),
('7183','question',None,'Sarılı kadın ne yapıyor?','Sarı giyimli kadın ne yapıyor?','"sarılı" ambiguous (wrapped)'),
('7192','phrases',2,'zaferle yumruğunu havaya savurmak','yumruğunu havaya savurmak','"zaferle" is added, not in English'),
('7194','phrases',0,'bir güve baskısı tutmak','bir gece kelebeği baskısı tutmak','güve = clothes moth; a blue moth print is a gece kelebeği'),
('7194','answer',None,'Bir güve baskısını yerine iğneliyor.','Bir gece kelebeği baskısını yerine iğneliyor.','same as phrase'),
]
log=[]
for vid,f,i,b,a,why in fixes:
    if b is None: continue
    cur = t[vid][f][i] if i is not None else t[vid][f]
    assert cur==b,(vid,f,cur)
    if i is None: t[vid][f]=a
    else: t[vid][f][i]=a
    log.append(f'- {vid} {f}{"" if i is None else "["+str(i)+"]"}: {b} -> {a} ({why})')
json.dump(t,open('tr.json','w'),ensure_ascii=False,indent=1)
src=json.load(open('source.json'))
n=sum(3+len(v['nouns'])+2 for v in src.values())
doubts='''
Doubts left unchanged:
- 7075/7097/7178/7185 "sekreterlik" for clipboard: standard Turkish stationery term, kept; learners may know "klipsli dosya".
- 7086 "lor" for fresh curd: the cheese-making term is "teleme", but "lor" is the widely known word; kept.
- 7104 "balon şişirmek" for blow a bubble: if it is bubble gum, "sakızla balon şişirmek" would be clearer; the context does not say.
- 7114 "yalak" for a trough of soapy water: mainly an animal trough; no better single word.
- 7137 "basamak taşları" for stepping stones: semi-calque, understood; "atlama taşları" also used.
- 7176 "tasma takmak" for the goat wearing a collar: can read as putting it on; kept as entry form.
- 7087 "tırıs gitmek" for a dog trotting: horse-gait word, but used for dogs too.
'''
open('verify_tr.md','w').write(f'# verify b026 tr\n\nTexts checked: {n}\n\nFixes ({len(log)}):\n'+'\n'.join(log)+'\n'+doubts)
print(n,len(log))
