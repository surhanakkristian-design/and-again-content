import json, os
R=os.path.expanduser('~/Projects/and-again-content/runs/a55_20261005/tr')
def build(lang, T):
    src=json.load(open(f'{R}/source_{lang}.json')); out={}
    for vid,s in src.items():
        ph,no,q,a,cap,ans_r=T[vid]
        m={s['phrases'][i]['text']:ph[i] for i in range(3)}
        m.update(dict(zip(s['captions'],cap)))
        n_map=dict(zip(s['nouns'],no))
        rec=[]
        for r in s['recall']:
            if r in m: rec.append(m[r])
            elif r in n_map: rec.append(n_map[r])
            else: rec.append(ans_r)
        out[vid]={'phrases':ph,'nouns':no,'question':q,'answer':a,'captions':dict(zip(s['captions'],cap)),'recall':rec}
    json.dump(out,open(f'{R}/{lang}/en.json','w'),ensure_ascii=False,indent=1)
DE={
'8055':(["to carry a man","to hold a rope","to hang from a rope"],["the hot-air balloon","the clouds","the rope","the man"],"What is the man doing?","He is hanging from a big hot-air balloon.",["to fly in a hot-air balloon","to land a hot-air balloon","the basket of the hot-air balloon"],"is hanging from a big hot-air balloon"),
'236':(["to swim in the sea","to jump into the air","to fall back into the water"],["the sky","the dolphin","the tail fin","the water"],"What is the dolphin doing?","It is jumping out of the water.",["a group of dolphins","to swim with a dolphin","to feed a dolphin"],"is jumping out of the water"),
'624':(["to run after a hat","to fly in the wind","to catch a hat"],["the trees","the hat","the girl","the grass"],"What is the girl doing?","She is running after a hat.",["ran after a hat","will run after a hat","to run to the bus"],"is running after a hat"),
'7071':(["to wear a golden crown","to roll through the mud","to reflect the grey sky"],["the crown","the king","the quad bike","the puddle"],"What is the king doing?","He is steering the quad bike through a puddle.",["a young king","king and queen","to bow to the king"],"is steering the quad bike through a puddle"),
'4265':(["to storm into the room","to laze on the sofa","to calm an angry friend"],["the door","the wings","the parrot","the sofa"],"What is the blue parrot doing?","It is calming the angry parrot with a hug.",["was calmed by a knight","to calm a barking dog","to calm a crying baby"],"is calming the angry parrot with a hug"),
'461':(["to dress a mannequin","to wear a scarf around the neck","to copy the mannequin's pose"],["the scarf","the shirt","the cat","the mannequin"],"What is the man doing?","He is copying the mannequin's pose.",["to carry a mannequin","the mannequin in the window","to dress a mannequin"],"is copying the mannequin's pose"),
'62':(["to lift a heavy bag","to be full of food","to wear sunglasses"],["the shirt","the bread","the apples","the bag"],"What is the man doing?","He is packing food into the bag.",["to drop a bag","the beach bag","the sports bag"],"is packing food into the bag"),
'8039':(["to shovel out a narrow path","to run along the path","to gesture behind the window"],["the snow","the shovel","the dog","the path"],"What is the woman doing outside?","She is shovelling a path through the snow.",["to block the passage","the narrow passage","to look for a passage"],"is shovelling a path through the snow"),
'432':(["to lead the group through the forest","to glow in the dark","to wear wire-rimmed glasses"],["the lantern","the valley","the jacket","the backpack"],"What is the woman doing?","She is leading the group with a lantern.",["led knights to a castle","will lead robots on Mars","to lead a horse"],"is leading the group with a lantern"),
'8056':(["to read a book","to look up at the man","to sit on a bench"],["the trees","the book","the bench","the dog"],"What is the man doing?","He is reading a book on a bench.",["the weight bench","to paint a bench","to share a bench"],"is reading a book on a bench"),
}
ES={
'8055':(["to carry a man","to hold a rope","to hang from a rope"],["the balloon","the clouds","the rope","the man"],"What is the man doing?","He is hanging from a big balloon.",["to fly in a balloon","to land a balloon","the basket of the balloon"],"is hanging from a big balloon"),
'236':(["to swim in the sea","to jump very high","to fall into the water"],["the sky","the dolphin","the tail","the water"],"What is the dolphin doing?","It is jumping out of the water.",["a group of dolphins","to swim with a dolphin","to feed a dolphin"],"is jumping out of the water"),
'624':(["to run after a hat","to fly in the wind","to catch a hat"],["the trees","the hat","the girl","the grass"],"What is the girl doing?","She is running after a hat.",["ran after a hat","will run after a hat","to run to catch the bus"],"is running after a hat"),
'7071':(["to sport a gold crown","to move through the mud","to reflect the grey sky"],["the crown","the king","the quad bike","the puddle"],"What is the king doing?","He is crossing a puddle on a quad bike.",["a young king","the king and the queen","to bow to the king"],"is crossing a puddle on a quad bike"),
'4265':(["to burst into the room","to be lounging on the sofa","to calm a furious friend"],["the door","the wings","the parrot","the sofa"],"What is the blue parrot doing?","It is calming the furious parrot with a hug.",["was calmed by a knight","to calm a barking dog","to calm a crying baby"],"is calming the furious parrot with a hug"),
'461':(["to dress a mannequin","to wear a scarf around the neck","to copy the mannequin's pose"],["the scarf","the shirt","the cat","the mannequin"],"What is the young man doing?","He is copying the mannequin's pose.",["to carry a mannequin on one's shoulder","the shop-window mannequin","to dress a mannequin"],"is copying the mannequin's pose"),
'62':(["to lift a heavy bag","to be full of food","to wear sunglasses"],["the shirt","the bread","the apples","the bag"],"What is the man doing?","He is filling the bag with food.",["to drop a bag","the beach bag","the sports bag"],"is filling the bag with food"),
'8039':(["to clear a path through the snow","to run along the cleared path","to point through the glass"],["the snow","the shovel","the dog","the path"],"What is the girl outside doing?","She is clearing a path through the snow.",["to block the passage","the narrow passage","to look for a passage"],"is clearing a path through the snow"),
'432':(["to guide the group","to shine in the dark","to wear round-rimmed glasses"],["the lantern","the valley","the jacket","the backpack"],"What is the girl doing?","She is guiding the group with a lantern.",["was guiding some knights towards a castle","will guide some robots across Mars","to guide a horse"],"is guiding the group with a lantern"),
'8056':(["to read a book","to look at the man","to be sitting on a bench"],["the trees","the book","the bench","the dog"],"What is the man doing?","He is reading a book on a bench.",["the weight bench","to paint a bench","to share a bench"],"is reading a book on a bench"),
}
FR={
'8055':(["to carry a man","to hold a rope","to hang from a rope"],["the hot-air balloon","the clouds","the rope","the man"],"What is the man doing?","He is hanging from a big hot-air balloon.",["to fly in a hot-air balloon","to land a hot-air balloon","the basket of the hot-air balloon"],"is hanging from a big hot-air balloon"),
'236':(["to swim in the sea","to jump into the air","to fall back into the water"],["the sky","the dolphin","the tail","the water"],"What is the dolphin doing?","It is jumping out of the water.",["a group of dolphins","to swim with a dolphin","to feed a dolphin"],"is jumping out of the water"),
'624':(["to run after a hat","to fly away in the wind","to catch a hat"],["the trees","the hat","the girl","the grass"],"What is the girl doing?","She is running after a hat.",["ran after a hat","will run after a hat","to run to catch the bus"],"is running after a hat"),
'7071':(["to sport a gold crown","to spray mud","to reflect the grey sky"],["the crown","the king","the quad bike","the puddle"],"What is the king doing?","He is crossing a puddle on a quad bike.",["a young king","the king and the queen","to bow to the king"],"is crossing a puddle on a quad bike"),
'4265':(["to storm into the room","to lounge on the sofa","to calm a furious friend"],["the door","the wings","the parrot","the sofa"],"What is the blue parrot doing?","It is calming the furious parrot with a hug.",["was calmed by a knight","to calm a barking dog","to calm a crying baby"],"is calming the furious parrot with a hug"),
'461':(["to dress a mannequin","to be draped in a scarf","to copy the mannequin's pose"],["the scarf","the shirt","the cat","the mannequin"],"What is the young man doing?","He is copying the mannequin's pose.",["to carry a mannequin","shop-window mannequin","to dress a mannequin"],"is copying the mannequin's pose"),
'62':(["to lift a heavy bag","to be full of food","to wear sunglasses"],["the polo shirt","the baguette","the apples","the bag"],"What is the man doing?","He is filling the bag with food.",["to drop a bag","beach bag","sports bag"],"is filling the bag with food"),
'8039':(["to clear a passage","to run along the passage","to gesture behind the window"],["the snow","the shovel","the dog","the passage"],"What is the woman doing outside?","She is clearing a passage through the snow.",["to block the passage","narrow passage","to look for a passage"],"is clearing a passage through the snow"),
'432':(["to guide the group","to light up the path","to wear round-rimmed glasses"],["the lantern","the valley","the jacket","the backpack"],"What is the young woman doing?","She is guiding the group with a lantern.",["was guiding knights towards a castle","will guide robots on Mars","to guide a horse"],"is guiding the group with a lantern"),
'8056':(["to read a book","to look at the man","to be sitting on a bench"],["the trees","the book","the bench","the dog"],"What is the man doing?","He is reading a book on a bench.",["weight bench","to paint a bench","to share a bench"],"is reading a book on a bench"),
}
build('de',DE); build('es',ES); build('fr',FR)
