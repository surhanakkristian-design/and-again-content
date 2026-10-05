import json
p='cz.json'; d=json.load(open(p))
fixes=[
('5351','answer',None,'S úžasem hledí vzhůru na světelné řetězy.','Hledí vzhůru na světelné řetězy.'),
('5364','nouns',1,'baseballová čepice','kšiltovka'),
('5364','answer',None,'Podpírají vyčerpanou běžkyni.','Pomáhají vyčerpané běžkyni.'),
('5367','phrases',0,'hltavě vypít svou vodu','hltavě vypít vodu'),
('5388','answer',None,'Drží sáček mimo její dosah.','Drží sáček mimo dosah.'),
('5391','phrases',0,'kutálet se po betonu','jet po betonu'),
('5396','phrases',0,'sklonit se nad mapu','sklonit se nad mapou'),
('5436','phrases',2,'zakroutit dlouhým balonkem','zkroutit dlouhý balonek'),
('5448','phrases',2,'zvedat pochodeň','třímat pochodeň'),
('5460','phrases',1,'podpírat svého nemocného kamaráda','podpírat kamaráda, kterému je zle'),
('5469','phrases',1,'kouknout na své chytré hodinky','letmo se podívat na chytré hodinky'),
('5480','nouns',1,'brýle','sklenice'),
]
for i,f,k,old,new in fixes:
    if k is None:
        assert d[i][f]==old,(i,f,d[i][f]); d[i][f]=new
    else:
        assert d[i][f][k]==old,(i,f,d[i][f][k]); d[i][f][k]=new
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
