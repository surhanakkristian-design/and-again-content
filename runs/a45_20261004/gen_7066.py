from gen_7064_7065_7066_7068_lib import write
man=[(.26,.24,.93,.98),(.22,.37,1.0,.98),(.27,.23,.93,.98),(.29,.21,.99,.98),(.27,.19,.99,.98),(.27,.20,1.0,.98),(.28,.16,1.0,.98),(.32,.17,1.0,.98)]
woman=[(0,.41,.18,.60)]*2+[(0,.41,.18,.60),(0,.41,.18,.60),(0,.40,.18,.60),(0,.39,.18,.60),(0,.40,.18,.60),(0,.40,.18,.60)]
dog=[(0,.61,.21,.83),(0,.61,.21,.83),(0,.61,.22,.85),(0,.61,.23,.88),(0,.61,.22,.89),(0,.62,.23,.93),(0,.65,.27,1.0),(0,.68,.31,1.0)]
write(7066,"B","dream","male",[
 ("to cheer in his sleep","the sleeping man","male",man),
 ("to stifle a laugh","the woman on the left","female",woman),
 ("to sniff around the seats","the dog","male",dog)],
 1.2,[("a suitcase",.38,.08,"male"),("a window",.88,.52,"male"),("a dog",.11,.76,"male"),("a sandwich",.74,.70,"male")],
 "What is the sleeping man doing?","He is waving his arms in his sleep.","male",
 "defaultVoice male (main person = the sleeping man). The dog never reaches the sandwich in these frames; it stays at the left by the passengers' knees, so its phrase is 'to sniff around the seats'. The woman (far left) laughs behind her hand; the young man next to her only smiles. Man's legs are dark at the bottom; box runs to 0.98.")
