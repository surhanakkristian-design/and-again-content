# A32 task 3, first look: for every Body Parts video the words I chose one by one after reading
# its description and transcript (positive selection from bp_pool; see out/BODY_PARTS_RULES.md).
# The script then enforces: other group, same level, not a body part, A31 rules R1-R5.
from load import *
from bodyparts import BODY
from bp_pool import POOL_NOUN, POOL_VERB
EXOTIC="camel crocodile dolphin elephant giraffe kangaroo penguin shark tiger snail frog owl"
KEEP={
156:EXOTIC+" watermelon garlic mushroom popcorn ketchup pizza soup stapler teapot toaster umbrella candle guitar broom",
437:"camel crocodile dolphin elephant kangaroo penguin shark tiger snail frog hamster owl watermelon garlic mushroom popcorn ketchup pizza soup cheese stapler teapot toaster umbrella candle guitar broom microwave",
4202:"camel crocodile dolphin elephant giraffe kangaroo penguin shark tiger snail owl parrot stapler umbrella candle guitar calculator envelope suitcase passport kite ladder helicopter train airplane",
4596:"camel crocodile dolphin elephant giraffe kangaroo penguin shark tiger snail frog owl wolf stapler hammer ladder helicopter airplane kite guitar calculator suitcase watermelon pizza mushroom ketchup carrot",
4710:"camel crocodile dolphin elephant giraffe kangaroo penguin shark tiger lion stapler teapot toaster microwave calculator envelope candle guitar hammer suitcase helicopter ship watermelon pizza garlic mushroom soup cheese popcorn",
4718:"camel crocodile dolphin elephant giraffe kangaroo penguin shark tiger snail frog hamster watermelon pizza garlic mushroom soup cheese popcorn ketchup teapot toaster umbrella guitar broom hammer ladder helicopter train",
4816:EXOTIC+" watermelon garlic mushroom popcorn ketchup pizza soup cheese stapler teapot toaster umbrella guitar broom candle ladder envelope",
4915:EXOTIC+" watermelon garlic mushroom popcorn ketchup pizza soup cheese stapler teapot toaster calculator broom hammer candle guitar suitcase envelope",
4977:"camel penguin kangaroo giraffe shark dolphin hamster sheep pizza popcorn ketchup cheese garlic mushroom soup bread cake chocolate stapler teapot toaster microwave calculator envelope eraser sharpener umbrella guitar broom hammer candle",
4982:EXOTIC+" watermelon garlic mushroom popcorn ketchup pizza soup cheese stapler teapot toaster microwave calculator envelope umbrella guitar broom candle suitcase",
5016:EXOTIC+" watermelon garlic mushroom popcorn ketchup pizza soup cheese teapot toaster umbrella guitar broom candle kite suitcase ladder helicopter train ship",
5103:"watermelon pizza garlic mushroom soup cheese popcorn ketchup mustard honey jam onion carrot cucumber teapot toaster microwave kettle broom mop candle matches umbrella kite ladder hammer drum helicopter ship train tram",
5346:"camel crocodile dolphin elephant giraffe kangaroo penguin shark tiger snail frog owl wolf lion turtle stapler umbrella guitar broom hammer candle kite suitcase ladder helicopter envelope passport drum",
5406:"elephant giraffe kangaroo penguin tiger lion owl hamster frog wolf squirrel pizza garlic mushroom soup cheese popcorn ketchup mustard bread stapler teapot toaster microwave calculator envelope guitar broom hammer candle ladder",
5409:"camel dolphin elephant giraffe kangaroo penguin snail frog owl hamster turtle pizza soup garlic mushroom popcorn ketchup cheese stapler teapot toaster umbrella guitar broom hammer candle ladder kite suitcase helicopter",
6885:"camel crocodile dolphin elephant giraffe kangaroo penguin shark tiger lion hamster pizza garlic mushroom soup cheese popcorn ketchup watermelon stapler teapot toaster microwave calculator envelope guitar hammer candle suitcase umbrella",
94:"defrost dissolve evaporate smuggle|to microwave|dig dive|to plant|robot tent hammock laundromat mosaic cactus canyon nest coal diamond keychain pyramid aquarium binoculars canoe cathedral compass dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht",
455:"robot laundromat mosaic canyon coal diamond keychain pyramid aquarium basement briefcase cathedral corkscrew dumpling lighthouse locomotive microscope submarine tablecloth blender|baking sheet|atm screwdriver vinegar bacon keyboard mattress warehouse prison tunnel",
642:"robot laundromat mosaic cactus canyon coal diamond keychain pyramid aquarium basement briefcase cathedral microscope locomotive tunnel skyscraper parliament keyboard mattress warehouse prison windmill atm bookstore paperclip screwdriver trumpet",
723:"tent hammock laundromat mosaic canyon champagne nest dumpling coal cocktail diamond keychain pyramid aquarium barbecue binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive otter paddle submarine windmill yacht bacon pie",
4080:"robot tent hammock laundromat mosaic cactus canyon champagne nest dumpling coal cocktail pyramid aquarium barbecue binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht bacon tunnel",
4460:"robot laundromat mosaic champagne dumpling cocktail diamond keychain pyramid aquarium basement briefcase cathedral corkscrew microscope locomotive tunnel skyscraper parliament keyboard mattress warehouse prison windmill atm bookstore paperclip screwdriver trumpet blender metro submarine",
4583:"robot tent hammock laundromat mosaic cactus canyon champagne nest dumpling coal cocktail diamond keychain pyramid aquarium binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht bookstore vase",
4592:"robot tent hammock laundromat mosaic cactus canyon nest dumpling coal diamond keychain pyramid aquarium binoculars canoe cathedral compass dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine skyscraper metro keyboard atm paperclip trumpet",
4684:"robot tent hammock laundromat mosaic canyon champagne nest dumpling coal cocktail diamond pyramid aquarium barbecue binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive otter paddle submarine windmill yacht bacon tunnel",
4818:"robot tent hammock laundromat mosaic canyon champagne nest dumpling coal cocktail diamond keychain pyramid aquarium barbecue binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht bacon tunnel",
4867:"tent hammock laundromat mosaic cactus canyon nest coal diamond pyramid aquarium binoculars canoe cathedral compass dune flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht tunnel harbour prison signpost wagon",
4950:"tent hammock laundromat mosaic cactus canyon champagne nest dumpling coal cocktail diamond keychain pyramid aquarium barbecue binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht bacon tunnel",
4963:"robot tent hammock laundromat mosaic cactus canyon champagne nest dumpling coal cocktail diamond pyramid aquarium barbecue binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht bacon tunnel",
5342:"robot tent hammock laundromat cactus canyon nest coal diamond keychain pyramid aquarium binoculars canoe cathedral compass dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht tunnel harbour prison signpost skyscraper",
5402:"robot tent hammock laundromat mosaic cactus canyon nest coal diamond keychain pyramid aquarium barbecue binoculars canoe cathedral compass dune fireworks flamingo lighthouse locomotive otter paddle submarine windmill yacht tunnel harbour prison signpost skyscraper",
5465:"robot mosaic cactus canyon champagne nest dumpling coal cocktail diamond keychain pyramid aquarium barbecue binoculars canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht bacon tunnel",
7268:"robot tent hammock laundromat cactus canyon champagne nest dumpling coal cocktail diamond keychain aquarium barbecue binoculars canoe compass corkscrew dune fireworks flamingo lighthouse locomotive otter paddle submarine windmill yacht vinegar hostel blender atm",
7292:"robot tent hammock laundromat mosaic cactus canyon champagne nest dumpling coal cocktail diamond keychain pyramid aquarium barbecue binoculars canoe cathedral compass dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine yacht bacon tunnel keyboard",
7298:"tent hammock laundromat mosaic cactus canyon nest coal diamond keychain pyramid aquarium binoculars canoe cathedral compass dune fireworks flamingo lighthouse locomotive otter paddle submarine windmill yacht tunnel harbour signpost skyscraper hostel prison",
7345:"robot hammock laundromat mosaic cactus champagne nest dumpling cocktail diamond keychain pyramid aquarium barbecue canoe cathedral compass corkscrew dune fireworks flamingo lighthouse locomotive microscope otter paddle submarine windmill yacht bacon tunnel keyboard atm",
}
def words(s):
    out=[]
    for part in s.split():
        out.append(part.replace("|"," ").strip()) if "|" not in part else out.extend([])
    return out
def parse(s):
    # "a b|c d" : '|' joins the tokens of one multi-word entry ("to|microwave" is written "|to microwave|")
    s=re.sub(r"\|([^|]+)\|",lambda mm:" "+mm.group(1).replace(" ","_")+" ",s)
    return [w.replace("_"," ") for w in s.split()]
gen=set(json.load(open("data/generic_a31.json")))
lev=collections.defaultdict(set); grp=collections.defaultdict(set)
for m,r in twd.items(): lev[r["concept"]].add(r["level"]); grp[r["concept"]].add(r["group"])
POOL=POOL_NOUN+POOL_VERB
byword=collections.defaultdict(list)
for c in POOL: byword[concepts[c]["word"]].append(c)
def build(keep=KEEP,verbose=True):
    res={}; why=collections.Counter()
    bp=[m for m,r in twd.items() if r["group"]==BP]
    assert set(keep)==set(bp),(set(bp)-set(keep),set(keep)-set(bp))
    for m in sorted(bp):
        r=twd[m]; key=r["concept"]; text=mtext(m); out=[]
        for w in parse(keep[m]):
            cs=byword.get(w)
            assert cs and len(cs)==1,(m,w,cs)
            c=cs[0]
            if r["level"] not in lev[c]: why["other level"]+=1; continue
            if BP in grp[c] or c in BODY: why["body"]+=1; continue
            if c in links[m]: why["R1"]+=1; continue
            if same_tr(key,c): why["R2"]+=1; continue
            if toks(concepts[key]["word"])&toks(concepts[c]["word"]): why["R3"]+=1; continue
            if text_has(concepts[c]["word"],text): why["R4"]+=1; continue
            if c in gen: why["R5"]+=1; continue
            if c not in out: out.append(c)
        pos=concepts[key]["part_of_speech"]
        out.sort(key=lambda c:(concepts[c]["part_of_speech"]!=pos,))
        res[m]=out
    if verbose: print("dropped by the mechanical rules:",dict(why))
    return res
if __name__=="__main__":
    res=build()
    n=[len(v) for v in res.values()]
    print("videos",len(res),"min",min(n),"avg",round(sum(n)/len(n),1),"max",max(n))
    for m,v in res.items(): print(m,twd[m]["level"],concepts[twd[m]["concept"]]["word"],len(v))
    json.dump({str(m):v for m,v in res.items()},open("out/bp_first_look.json","w"))
    # packet for the independent second look: only videos, descriptions, transcripts, candidate words
    pk=[dict(media=m,level=twd[m]["level"],key_word=concepts[twd[m]["concept"]]["word"],desc=media[m]["asset_description"],said=media[m]["transcript"] or "",wrong=[dict(c=c,w=concepts[c]["word"],pos=concepts[c]["part_of_speech"]) for c in v]) for m,v in res.items()]
    json.dump(pk,open("packets/bp_audit_in.json","w"),indent=1,ensure_ascii=False)
