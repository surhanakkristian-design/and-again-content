from gen_7874_7875_7876_7877_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
L=[.11,.10,.09,.08,.07,.07,.08,.08]; S=[.495,.505,.505,.515,.52,.53,.54,.545]
YM=[(.31,.96),(.31,.97),(.31,.98),(.31,.99),(.29,1),(.29,1),(.29,1),(.29,1)]
WR=[.82,.82,.83,.83,.85,.86,.87,.87]
man=[(l,ym[0],s-.005,ym[1]) for l,s,ym in zip(L,S,YM)]
woman=[(s+.005,.34,r,.92 if i<4 else .97) for i,(s,r) in enumerate(zip(S,WR))]
build(7876,"A","in my opinion","male",[
 ("to hold up a phone","the man","male",man),
 ("to hold out her hand","the woman","female",woman),
 ("to look at his shirt","the man","male",man)],
 0.2,[("a hat",.21,.43,"male"),("a shirt",.38,.56,"male"),("a plant",.83,.55,"male"),("a chair",.78,.74,"male")],
 "What is the man holding?","He is holding a phone.","male",
 "mirror selfie; man and woman stand close, split line between phone hand and her cardigan; 'look at his shirt' clearest from 2.7 s",T)
