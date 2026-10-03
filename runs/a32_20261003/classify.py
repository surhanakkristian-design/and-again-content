# A32 task 2: class of every video (person / animal_only / none) and whether an animal is visible.
# Keyword rules mark the clear cases; every description without a clear person word (143) and every
# one with only a weak person word (69) was READ by me; the lists below are the reading result.
# Both errors of the keyword rules go to the safe side (a video wrongly called "person" loses the words).
from load import *
PERSON=r"\b(man|men|woman|women|girl|girls|boy|boys|guy|guys|person|people|child|children|kid|kids|baby|babies|toddler|teen|teenager|teenagers|lady|ladies|he|she|his|her|him|they|their|someone|somebody|hand|hands|finger|fingers|arm|arms|face|faces|worker|workers|student|students|teacher|friend|friends|couple|family|families|crowd|player|players|chef|driver|doctor|nurse|mother|father|mom|dad|son|daughter|brother|sister|grandmother|grandfather|grandma|grandpa|tourist|tourists|customer|customers|waiter|waitress|athlete|athletes|runner|runners|dancer|dancers|officer|soldier|soldiers|passenger|passengers|character|characters|himself|herself|themselves|who|wearing|smiles|smiling|laughs|human|humans|adult|adults|figure|figures|team|audience|villagers|pedestrians|shoppers|commuters|cyclist|cyclists|hikers|hiker|bride|groom|king|queen|knight|robot|clown|mannequin|statue|doll|puppet|pov|feet|foot|legs|leg)\b"
ANIM=r"\b(animal|animals|dog|dogs|puppy|puppies|cat|cats|kitten|kittens|bird|birds|horse|horses|cow|cows|pig|pigs|sheep|goat|goats|chicken|chickens|hen|hens|rooster|duck|ducks|goose|geese|swan|swans|fish|shark|dolphin|dolphins|whale|lion|tiger|bear|bears|wolf|wolves|fox|deer|rabbit|rabbits|bunny|mouse|mice|rat|rats|hamster|hamsters|squirrel|squirrels|monkey|monkeys|ape|gorilla|elephant|elephants|giraffe|zebra|zebras|hippo|camel|kangaroo|penguin|penguins|parrot|owl|eagle|pigeon|pigeons|seagull|seagulls|gull|gulls|dove|flamingo|frog|turtle|tortoise|lizard|snake|crocodile|dinosaur|dragon|insect|insects|bee|bees|butterfly|butterflies|ladybug|spider|ant|ants|worm|snail|caterpillar|otter|seal|donkey|pony|bull|calf|lamb|turkey|crab|octopus|creature|creatures|pet|pets|flock|herd|livestock|cattle|buffalo|moose|panda|pandas|koala|raccoon|hedgehog|bat|bats|mosquito|fly|flies|beetle|cricket|t rex|griffin|unicorn|pup|cub|cubs|chick|chicks|duckling|ducklings|fawn|doe|stag|crow|crows|sparrow|hawk|jay|drake|polar|beast|monster|mascot|gecko|chameleon|lobster|shrimp|jellyfish|starfish|peacock|ostrich|llama|alpaca|reindeer|boar|badger|beaver|mole|ferret|ferrets|guinea|goldfish|puppet|robin|marmot|trout|egrets|hare|hares|moths|chimpanzee|leopard|antelope|macaw|bumblebee|koi)\b"
# read: no person and no animal (object / landscape only)
NONE={259,4017,4090,4093,4152,4153,4160,4164,4193,4233,4748,4826,6888,6890,6891,6910,6942,6958,6997,7102,7121,7236,7237,7293,7300,7425,7492,7806,7996,189,4906,5538,7203}
# read: a person (or a human-like figure, or a hand that must be doing the action) although the keyword rule missed it
PERSON_READ={9,104,114,293,369,382,393,406,508,596,724,4015,4095,4830,4898,4900,4902,4905,550,4702,6866,7059,7116,7483,7870,387,4167,5176,4037}
# read: only animals (the weak person word was a leg / face / foot of an animal, a statue of an animal ...)
ANIMAL_READ={79,89,90,133,250,280,332,359,595,600,817,4009,4011,4020,4025,4028,4061,4103,4128,4130,4134,4143,4149,4176,4192,4205,4207,4209,4210,4211,4221,4224,4225,4226,4258,4259,4261,4266,6899,7122,7170,7196,7278,7315,7946,7987}
def classify():
    out={}
    for m in twd:
        d=norm(media[m]["asset_description"])
        p=bool(re.search(PERSON,d)); a=bool(re.search(ANIM,d))
        if m in NONE: cls,a="none",False
        elif m in PERSON_READ: cls="person"
        elif m in ANIMAL_READ or not p: cls,a="animal_only",True
        else: cls="person"
        out[m]=dict(cls=cls,animal=a)
    return out
if __name__=="__main__":
    c=classify()
    print(collections.Counter(v["cls"] for v in c.values()), "person with animal",sum(v["cls"]=="person" and v["animal"] for v in c.values()))
    json.dump({str(m):v for m,v in sorted(c.items())},open("out/video_classes.json","w"))
