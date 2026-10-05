import json
p='ua.json'; d=json.load(open(p))
fixes=[
 ("5038","nouns",2,"кросівок","кросівка"),
 ("5009","phrases",1,"копати м'яч","бити по м'ячу"),
 ("5009","question",None,"Що копає хлопчик?","По чому б'є хлопчик?"),
 ("5009","answer",None,"Він копає м'яч.","Він б'є по м'ячу."),
 ("5061","answer",None,"Він задивляється вгору на акул.","Він пильно дивиться вгору на акул."),
 ("4987","phrases",2,"звалюватися на стіл","безсило схилятися над столом"),
]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f,d[k][f]); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,d[k][f][i]); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
