import json
p='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b007/sk.json'
t=json.load(open(p))
def rep(i,f,k,a,b):
    if k is None:
        assert t[i][f]==a,(i,f,t[i][f]); t[i][f]=b
    else:
        assert t[i][f][k]==a,(i,f,t[i][f][k]); t[i][f][k]=b
rep('448','phrases',1,'poklepať si na spodnú peru','poklepať si po spodnej pere')
rep('474','answer',None,'Meditujú na drevenej terase.','Medituje na drevenej terase.')
rep('476','phrases',1,'nazerať do okuláru','nazerať do okulára')
rep('496','phrases',0,'nasadiť si náhrdelník','dať si náhrdelník')
rep('507','nouns',3,'cop','konský chvost')
rep('566','nouns',0,'cop','konský chvost')
rep('542','phrases',1,'kĺzať sa po bruchu','kĺzať sa na bruchu')
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
