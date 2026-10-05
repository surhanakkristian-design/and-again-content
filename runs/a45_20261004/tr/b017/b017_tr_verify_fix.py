import json
p='tr.json'; d=json.load(open(p))
fixes=[
('4865','phrases',2,'fotoğraf makinesini taşımak','"desteklemek" is figurative support; a tripod physically bears the camera'),
('4871','phrases',0,'bir yaka kartı almak','"name badge" is "yaka kartı"; indefinite object without accusative'),
('4871','phrases',1,'bir yaka kartı vermek','"name badge" is "yaka kartı"'),
('4871','answer',None,'Konuğa bir yaka kartı veriyor.','same word as phrases: "yaka kartı"'),
('4878','phrases',0,'tek başına suya atlamak','"atlayış yapmak" is stilted; natural verb'),
('4879','phrases',1,'ağaç kabuğuyla kaplı olmak','"kabuk" alone is ambiguous (shell/peel); bark = ağaç kabuğu'),
('4884','phrases',0,'gökyüzünü ilk işaret etmek','"ilk işaret eden olmak" changed the structure; plain verb entry'),
('4887','phrases',2,'kanyona doğru inmek','"boğaz" reads as throat/strait; the clip shows a canyon gorge'),
('4896','phrases',0,'meydanı koşarak geçmek','"meydan boyunca" means along, not across'),
('4896','answer',None,'Meydanı koşarak geçiyorlar.','same as phrase: across, not along'),
('4899','phrases',2,'bütün bir ağacı kaldırmak','"whole tree" = "bütün bir ağaç"; "koca" means huge'),
('4904','phrases',1,'gökyüzünün önünde sallanmak','"gökyüzüne karşı" is a calque of "against the sky"'),
('4906','phrases',2,'ortasından bel vermek','"buckle" (sag in the middle) = "bel vermek"; "bükülmek" is bend'),
('4917','phrases',1,'bir duvarı tırmanıp aşmak','"duvarın üzerinden tırmanmak" is ungrammatical for "climb over"'),
('4928','phrases',0,'gider borusunu sıkıştırmak','tightening a pipe fitting is "sıkıştırmak"; "sıkmak" = squeeze'),
('4932','phrases',0,'trafiğin arasından araç sürmek','"trafiğin içinden aracı sürmek" awkward word order/definiteness'),
('4932','answer',None,'Taksiyi trafiğin arasından sürüyor.','natural wording, consistent with phrase'),
('4935','nouns',2,'ceket kolu','"kol" alone reads as arm; sleeve of her jacket'),
('4938','phrases',1,'siparişi not almak','"write down an order" = "siparişi not almak"; "sipariş yazmak" unnatural'),
('4946','phrases',0,'ahşap bara yaslanmak','dance barre is "bar"; "tutamak" is a handle'),
('4949','phrases',1,'adamı yokuş yukarı takip etmek','word order: object before adverbial'),
('4950','phrases',1,'ciddiyetini korumak','"keep a straight face" idiom; "yüzünü ciddi tutmak" is a calque'),
('4954','phrases',0,'birkaç çiçek taşımak','"biraz" is for mass nouns; countable flowers = "birkaç"'),
('4959','phrases',2,'yansıma havuzunun yanında poz vermek','"reflecting pool" = "yansıma havuzu"'),
('4968','phrases',0,'bir kart almak','indefinite object: no accusative with "bir"'),
]
log=[]
for vid,f,i,new,why in fixes:
    if i is None: old=d[vid][f]; d[vid][f]=new
    else: old=d[vid][f][i]; d[vid][f][i]=new
    log.append(f'- {vid}, {f}{"" if i is None else "["+str(i)+"]"}: {old} -> {new} ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('b017_tr_verify_log.txt','w').write('\n'.join(log)+'\n')
print(len(log))
