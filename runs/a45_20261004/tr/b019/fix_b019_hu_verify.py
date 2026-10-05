import json
p='hu.json'; d=json.load(open(p,encoding='utf-8'))
F=[
('5102','phrases',0,'átpréselni magát egy férfi mellett','elpréselődni egy férfi mellett','"át-" means through/across; squeezing past someone is "elpréselődik valaki mellett"'),
('5102','answer',None,'Átpréseli magát egy férfi mellett a sikátorban.','Elpréselődik egy férfi mellett a sikátorban.','same fix as the phrase, same verb in one video'),
('5114','phrases',2,'felröppenni','felrepülni','"felröppen" is for small birds; flamingos "felrepülnek"'),
('5114','answer',None,'Felröppennek a tó fölött.','Felrepülnek a tó fölött.','same verb as the corrected phrase'),
('5140','question',None,'Mit csinál a tiszt?','Mit csinál a határőr?','"tiszt" is a military rank; a border control officer is "határőr"'),
('5146','phrases',2,'a térdén túl lelógni','a térde alá lelógni','"a térdén túl" is unidiomatic; dangling past/below the knees = "a térde alá lelóg"'),
('5150','answer',None,'A gyógyszerész a receptjét olvassa.','A gyógyszerész a fiatalember receptjét olvassa.','"a receptjét" reads as the pharmacist\'s own; "his" = the young man\'s'),
('5156','phrases',0,'elcselezni egy védő mellett','kicselezni egy védőt','the football idiom is "kicselezni valakit"'),
('5169','phrases',2,'élénksárgára festettnek lenni','élénksárgára festve lenni','"festettnek lenni" sounds like "to be considered painted"; stative passive is "festve van"'),
('5172','nouns',3,'szárított chilik','szárított chilipaprikák','"chilik" is not a standard plural noun; "chilipaprika"'),
('5177','phrases',2,'sorban állni','egy sorban állni','"sorban állni" means to queue; glasses standing in a row = "egy sorban állni"'),
('5182','phrases',0,'felvinni az utolsó ecsetvonásokat','meghúzni az utolsó ecsetvonásokat','brushstrokes collocate with "meghúzni", not "felvinni"'),
('5191','phrases',0,'felkúszni a rúdra','felkúszni a rúdon','going up along the pole takes -on, "-ra" means onto'),
('5203','phrases',0,'elöl menni befelé','elsőként bemenni','"elöl menni befelé" is unidiomatic; leading the way inside = "elsőként bemenni"'),
]
log=[]
for i,f,k,b,a,w in F:
    if k is None:
        assert d[i][f]==b,(i,f,d[i][f]); d[i][f]=a
    else:
        assert d[i][f][k]==b,(i,f,d[i][f][k]); d[i][f][k]=a
    log.append(f'- {i}, {f}{"" if k is None else f"[{k}]"}: "{b}" -> "{a}" ({w})')
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
open('_fixlog_b019_hu.txt','w').write('\n'.join(log))
print(len(F))
