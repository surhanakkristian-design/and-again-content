from gen_6997_6998_6999_7000_lib import build
cov=[(0,.19,.74,.60),(0,.19,.74,.55),(0,.18,.74,.42),(0,.19,.74,.56),(0,.19,.74,.60),(0,.19,.74,.60),(0,.19,.74,.60),(0,.19,.74,.60)]
tree=[(.74,.08,.21,.36)]*8
build(6997,"B","covering","male",[
 ("to flap in the wind","the car cover","male",cov),
 ("to hide an old sports car","the car cover","male",cov),
 ("to stand in a square planter","the potted tree","male",tree)],
 2.2,[("a covering",.25,.35,"male"),("a headlight",.50,.59,"male"),("a garage door",.62,.10,"male"),("cobblestones",.45,.88,"male")],
 "What is happening to the covering?","A gust of wind is lifting the covering.","male",
 "No person; the cover and the car overlap completely, so the car/headlight is not a tap target (boxes cannot overlap). Two phrases on the cover, third on the potted tree (state). Cover box cut at x .74 where its right edge touches the tree pot.")
