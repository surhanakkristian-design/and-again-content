#!/usr/bin/env python3
# Phase 1m - annotations for the NEW sentences sid 150071..150140 (label: annotate-2).
# Hand-written, 0 model calls. Emits data/annotations_part2.json in the Phase 1k fresh
# annotation schema: {"<sid>": {"hygienised": ann, "raw": ann, <5 gold metadata keys>}}
# with ann = {id, t, lv, v, lk, alt}; t synthetic 9000 + (sid - 150001); no m (synthetic t),
# no g (arm B states the subject). hygienised == raw (sentences authored clean).
# Conventions: v[0] = primary reference (one faithful natural rendering); further entries are
# other fully faithful renderings; lk is parallel to v; Slovak agent stays the subject; Slovak
# time frame kept; perfective present = future.
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SENT = os.path.join(HERE, "data", "sentences.json")
OUT = os.path.join(HERE, "data", "annotations_part2.json")
LOG = os.path.join(HERE, "access_log.jsonl")

# (sid, refs, locks, alt, tf_gold, voice_sk, agent_nom, perfective_present, tense_open)
ROWS = [
(150071, ["My sister writes a letter to Grandma every month.",
          "My sister writes Grandma a letter every month."],
 ["writes", "writes"],
 {"Grandma": ["Granny", "Grandmother", "her grandmother"], "letter": ["letter"]},
 "present", "active_agent", True, False, False),

(150072, ["You told me that you always buy the tickets online.",
          "You told me you always buy the tickets online.",
          "You told me that you always bought the tickets online."],
 ["told + buy", "told + buy", "told + bought"],
 {"online": ["on the internet", "over the internet"], "buy": ["purchase"], "tickets": ["tickets"]},
 "mixed", "active_agent", True, False, True),

(150073, ["This morning it was very cold in the kitchen.",
          "It was very cold in the kitchen this morning."],
 ["was", "was"],
 {"cold": ["chilly"]},
 "past", "impersonal", False, False, False),

(150074, ["They clean the whole house and the garage on Saturday.",
          "They clean the whole house and the garage on Saturdays.",
          "They are cleaning the whole house and the garage on Saturday."],
 ["clean", "clean", "are cleaning"],
 {"clean": ["tidy", "tidy up"], "garage": ["garage"]},
 "present", "active_agent", True, False, True),

(150075, ["The lady from the bakery always sets aside two rolls for us.",
          "The woman from the bakery always keeps two rolls for us.",
          "The lady at the bakery always puts aside two rolls for us."],
 ["sets aside", "keeps", "puts aside"],
 {"lady": ["woman"], "bakery": ["baker's"], "rolls": ["bread rolls", "crescent rolls"]},
 "present", "active_agent", True, False, False),

(150076, ["The birds have been singing in the garden since early morning.",
          "Birds have been singing in the garden since early in the morning.",
          "The birds sing in the garden from early morning."],
 ["have been singing", "have been singing", "sing"],
 {"garden": ["garden"], "early morning": ["early in the morning"]},
 "present", "active_agent", False, False, True),

(150077, ["He reworked that presentation three times until he was satisfied.",
          "He redid the presentation three times until he was happy with it.",
          "He reworked the presentation three times before he was satisfied."],
 ["reworked", "redid", "reworked"],
 {"reworked": ["redid", "revised", "reworked"], "satisfied": ["happy", "content"]},
 "past", "active_agent", True, False, False),

(150078, ["She asked him why he had been late for the exam.",
          "She asked him why he was late for the exam.",
          "She asked him why he had been late for that exam."],
 ["asked + had been", "asked + was", "asked + had been"],
 {"exam": ["test", "examination"], "late for": ["late to"]},
 "past", "active_agent", True, False, True),

(150079, ["We only have a little butter and two eggs in the fridge.",
          "We have only a little butter and two eggs in the fridge.",
          "We have just a little butter and two eggs in the fridge."],
 ["have", "have", "have"],
 {"fridge": ["refrigerator"], "a little": ["a bit of"], "only": ["just"]},
 "present", "active_agent", False, False, False),

(150080, ["The architect designed the library so that daylight would come into it.",
          "The architect designed that library in such a way that daylight would get inside.",
          "The architect designed the library so that daylight could come in."],
 ["designed + so that", "designed + in such a way that", "designed + so that"],
 {"architect": ["architect"], "daylight": ["natural light", "the daylight"], "library": ["library"]},
 "past", "active_agent", True, False, False),

(150081, ["We cleared the snow off the pavement before dawn.",
          "We shovelled the snow off the pavement before dawn.",
          "We cleared the snow from the sidewalk before daybreak."],
 ["cleared", "shovelled", "cleared"],
 {"pavement": ["sidewalk", "footpath"], "cleared": ["shovelled", "shoveled", "cleared away"],
  "dawn": ["daybreak", "sunrise"]},
 "past", "active_agent", True, False, False),

(150082, ["There is no smoking here, not even on the terrace in front of the entrance.",
          "You can't smoke here, not even on the terrace by the entrance.",
          "Smoking is not allowed here, not even on the terrace in front of the entrance."],
 ["there is no smoking", "can't smoke", "is not allowed"],
 {"terrace": ["patio"], "entrance": ["entrance", "door"]},
 "present", "impersonal", False, False, False),

(150083, ["The neighbour claims that his father planted that old cherry tree.",
          "The neighbour says that it was his father who planted the old cherry tree.",
          "The neighbor claims his father planted that old cherry tree."],
 ["claims + planted", "says + planted", "claims + planted"],
 {"neighbour": ["neighbor"], "claims": ["says", "maintains"], "cherry tree": ["cherry tree"]},
 "mixed", "active_agent", True, False, False),

(150084, ["Dad parked the car in front of the garage and turned off the engine.",
          "Father parked the car in front of the garage and switched off the engine.",
          "Dad parked the car outside the garage and turned the engine off."],
 ["parked + turned off", "parked + switched off", "parked + turned off"],
 {"Dad": ["Father", "My dad", "My father"], "turned off": ["switched off", "shut off"],
  "engine": ["motor"]},
 "past", "active_agent", True, False, False),

(150085, ["There is a small eighteenth-century chapel on that hill.",
          "A small chapel from the eighteenth century stands on that hill.",
          "There is a small chapel from the eighteenth century on the hill."],
 ["there is", "stands", "there is"],
 {"chapel": ["chapel"], "hill": ["hill"], "eighteenth-century": ["18th-century"]},
 "present", "active_agent", False, False, False),

(150086, ["By the evening we will have got the hall ready for tomorrow's celebration.",
          "By evening we will have prepared the hall for tomorrow's party.",
          "We will get the hall ready for tomorrow's celebration by the evening."],
 ["will have got ready", "will have prepared", "will get ready"],
 {"hall": ["room", "function room"], "celebration": ["party"]},
 "future", "active_agent", True, True, False),

(150087, ["She drives the children to swimming practice every Tuesday.",
          "Every Tuesday she takes the kids to swimming training.",
          "She drives the children to swimming training every Tuesday."],
 ["drives", "takes", "drives"],
 {"children": ["kids"], "drives": ["takes"], "practice": ["training", "lessons"]},
 "present", "active_agent", True, False, False),

(150088, ["Today is Saturday and we are at home all day.",
          "It is Saturday today and we are at home all day.",
          "Today is Saturday and we're home the whole day."],
 ["is + are", "is + are", "is + are"],
 {"at home": ["home"], "all day": ["the whole day"]},
 "present", "active_agent", False, False, False),

(150089, ["They announced on the board that they had moved the trip to June.",
          "They announced on the noticeboard that they moved the trip to June.",
          "They announced on the board that they had postponed the trip until June."],
 ["announced + had moved", "announced + moved", "announced + had postponed"],
 {"board": ["noticeboard", "notice board", "bulletin board"], "trip": ["excursion", "outing"],
  "moved": ["rescheduled", "postponed", "put off"]},
 "past", "active_agent", True, False, False),

(150090, ["The dentist pulled out my bad tooth last Thursday.",
          "The dentist took out that bad tooth last Thursday.",
          "The dentist extracted the decayed tooth last Thursday."],
 ["pulled out", "took out", "extracted"],
 {"pulled out": ["took out", "extracted"], "bad": ["decayed", "rotten"], "dentist": ["dentist"]},
 "past", "active_agent", True, False, False),

(150091, ["The exhibition was moved to a smaller hall without any explanation.",
          "The exhibition was moved to a smaller room without explanation.",
          "That exhibition was relocated to a smaller hall without any explanation."],
 ["was moved", "was moved", "was relocated"],
 {"hall": ["room"], "moved": ["relocated", "transferred"], "exhibition": ["exhibition", "show"]},
 "past", "passive", False, False, False),

(150092, ["I will bring you the poppy seed cake recipe after lunch.",
          "After lunch I will bring you that recipe for poppy seed cake.",
          "I'll bring you the recipe for the poppy seed cake after lunch."],
 ["will bring", "will bring", "will bring"],
 {"poppy seed cake": ["poppy-seed cake", "poppy seed roll"], "lunch": ["lunch"]},
 "future", "active_agent", True, True, False),

(150093, ["The new colleague has been managing our website since January.",
          "The new colleague has been running our website since January.",
          "Our new colleague has managed our site since January."],
 ["has been managing", "has been running", "has managed"],
 {"website": ["site", "page", "web page"], "managing": ["running", "looking after"],
  "colleague": ["co-worker", "colleague"]},
 "present", "active_agent", True, False, True),

(150094, ["If the hall were not so noisy, the guests would talk more easily.",
          "If the hall wasn't so noisy, the guests would talk better.",
          "If that room were not so loud, the guests would talk more easily."],
 ["were + would talk", "wasn't + would talk", "were + would talk"],
 {"noisy": ["loud"], "hall": ["room"], "guests": ["guests"]},
 "conditional", "active_agent", False, False, False),

(150095, ["We think that she is still only considering the offer.",
          "We think she is still just considering that offer.",
          "We believe that she is still only thinking about the offer."],
 ["think + is considering", "think + is considering", "believe + is thinking about"],
 {"think": ["believe"], "considering": ["thinking about", "weighing up"], "offer": ["offer"]},
 "present", "active_agent", True, False, False),

(150096, ["He always feeds the cat at seven in the evening.",
          "He always feeds the cat at seven o'clock in the evening.",
          "He always feeds the cat at seven p.m."],
 ["feeds", "feeds", "feeds"],
 {"seven": ["7"], "in the evening": ["p.m.", "at night"]},
 "present", "active_agent", True, False, False),

(150097, ["There is no free space in the car park in front of the stadium.",
          "There isn't a free space in the parking lot in front of the stadium.",
          "There is no empty spot in the car park outside the stadium."],
 ["there is no", "there isn't", "there is no"],
 {"car park": ["parking lot", "parking"], "free": ["empty", "vacant"], "space": ["spot", "place"]},
 "present", "active_agent", False, False, False),

(150098, ["By Saturday the baker will have baked three hundred Easter cakes.",
          "By Saturday the baker will bake three hundred Easter cakes.",
          "The baker will have baked 300 Easter cakes by Saturday."],
 ["will have baked", "will bake", "will have baked"],
 {"cakes": ["pastries", "buns"], "three hundred": ["300"], "baker": ["baker"]},
 "future", "active_agent", True, True, False),

(150099, ["She told me on the phone that she had left the key under the doormat.",
          "She told me over the phone that she left the key under the doormat.",
          "She said on the phone that she had left the key under the mat."],
 ["told + had left", "told + left", "said + had left"],
 {"doormat": ["mat", "door mat"], "on the phone": ["over the phone", "by phone"], "key": ["key"]},
 "past", "active_agent", True, False, True),

(150100, ["The post office closes as early as four in the afternoon.",
          "That post office closes at four in the afternoon.",
          "The post office already closes at four p.m."],
 ["closes", "closes", "closes"],
 {"four": ["4"], "in the afternoon": ["p.m."], "post office": ["post office"]},
 "present", "passive", False, False, False),

(150101, ["The committee rejected our application because of a single missing stamp.",
          "The commission turned down our application over one missing stamp.",
          "The committee refused our request because of one missing stamp."],
 ["rejected", "turned down", "refused"],
 {"committee": ["commission", "board", "panel"], "rejected": ["turned down", "refused", "denied"],
  "application": ["request"], "stamp": ["stamp"]},
 "past", "active_agent", True, False, False),

(150102, ["You told us at the time that nobody knew about the change.",
          "You told us then that nobody knows about that change.",
          "At the time you told us that no one knew about the change."],
 ["told + knew", "told + knows", "told + knew"],
 {"nobody": ["no one"], "at the time": ["then", "back then"], "change": ["change"]},
 "mixed", "active_agent", True, False, True),

(150103, ["By morning the snow on the pavements will certainly melt.",
          "The snow on the pavements will definitely have melted by morning.",
          "By morning the snow on the sidewalks will surely melt."],
 ["will melt", "will have melted", "will melt"],
 {"pavements": ["sidewalks", "footpaths"], "certainly": ["definitely", "surely", "for sure"]},
 "future", "active_agent", False, True, False),

(150104, ["Our school has a big gym and a new playground.",
          "Our school has a large gym and a new playground.",
          "Our school has a big gymnasium and a new playing field."],
 ["has", "has", "has"],
 {"gym": ["gymnasium", "sports hall"], "playground": ["playing field", "pitch"],
  "big": ["large"]},
 "present", "active_agent", False, False, False),

(150105, ["The light blue jumper suits her more than the black one.",
          "The light blue sweater suits her better than the black one.",
          "That pale blue sweater looks better on her than the black one."],
 ["suits + than", "suits + than", "looks better + than"],
 {"jumper": ["sweater", "pullover"], "light blue": ["pale blue"], "suits": ["looks good on"]},
 "present", "active_agent", False, False, False),

(150106, ["Grandpa reads the children a fairy tale every evening.",
          "Grandpa reads a fairy tale to the children every evening.",
          "Granddad reads the kids a bedtime story every evening."],
 ["reads", "reads", "reads"],
 {"Grandpa": ["Granddad", "Grandfather"], "fairy tale": ["story", "bedtime story"],
  "children": ["kids"]},
 "present", "active_agent", True, False, False),

(150107, ["He told us that he had rented out the cottage for the whole summer.",
          "He told us he rented out the cottage for the whole summer.",
          "He told us that he had let the cottage for the entire summer."],
 ["told + had rented out", "told + rented out", "told + had let"],
 {"cottage": ["cabin", "chalet", "holiday cottage"], "rented out": ["let"],
  "whole": ["entire"]},
 "past", "active_agent", True, False, True),

(150108, ["In autumn it gets dark early here and it is often windy.",
          "In the autumn it gets dark early here and it's often windy.",
          "In fall it gets dark early here and it is often windy."],
 ["gets dark + is windy", "gets dark + is windy", "gets dark + is windy"],
 {"autumn": ["fall", "the autumn"], "windy": ["windy"], "early": ["early"]},
 "present", "impersonal", False, False, False),

(150109, ["You wear the same shoes almost every day.",
          "You wear those same shoes nearly every day."],
 ["wear", "wear"],
 {"almost": ["nearly"], "shoes": ["shoes"]},
 "present", "active_agent", True, False, False),

(150110, ["The bus driver dropped the tourists off right by the castle.",
          "The bus driver let the tourists out right by the castle.",
          "The bus driver dropped off the tourists right next to the castle."],
 ["dropped off", "let out", "dropped off"],
 {"right": ["just"], "castle": ["castle"], "tourists": ["tourists"]},
 "past", "active_agent", True, False, False),

(150111, ["There is a new cake shop in our street.",
          "There is a new patisserie on our street.",
          "There's a new pastry shop in our street."],
 ["there is", "there is", "there is"],
 {"cake shop": ["patisserie", "pastry shop", "confectionery", "sweet shop"], "in": ["on"]},
 "present", "active_agent", False, False, False),

(150112, ["They recalculated the budget once more before the vote.",
          "They went through the budget again before the vote.",
          "They recalculated that budget one more time before the voting."],
 ["recalculated", "went through", "recalculated"],
 {"recalculated": ["recounted", "went over", "recomputed"], "vote": ["voting"],
  "once more": ["again", "one more time"]},
 "past", "active_agent", True, False, False),

(150113, ["I asked her whether she had already finished reading the book.",
          "I asked her if she had finished the book yet.",
          "I asked her if she had already finished reading that book."],
 ["asked + had finished", "asked + had finished", "asked + had finished"],
 {"whether": ["if"], "finished reading": ["finished", "read to the end"], "book": ["book"]},
 "past", "active_agent", True, False, True),

(150114, ["After dinner all the guests were tired and sleepy.",
          "All the guests were tired and sleepy after dinner.",
          "After supper all the guests were tired and drowsy."],
 ["were", "were", "were"],
 {"dinner": ["supper", "the dinner"], "sleepy": ["drowsy"], "guests": ["guests"]},
 "past", "active_agent", False, False, False),

(150115, ["The ministry published the results only after midnight.",
          "The ministry only released the results after midnight.",
          "The ministry did not publish the results until after midnight."],
 ["published", "released", "did not publish until"],
 {"published": ["released", "made public"], "ministry": ["ministry", "department"],
  "results": ["results"]},
 "past", "active_agent", True, False, False),

(150116, ["She looked after our flat and two cats for the whole summer.",
          "She was looking after our flat and our two cats all summer.",
          "She watched our apartment and two cats the whole summer."],
 ["looked after", "was looking after", "watched"],
 {"flat": ["apartment"], "looked after": ["watched", "took care of", "minded"],
  "whole summer": ["entire summer"]},
 "past", "active_agent", True, False, True),

(150117, ["Breakfast is served from seven to ten at that hotel.",
          "In that hotel breakfast is served from seven until ten.",
          "At that hotel they serve breakfast from seven to ten."],
 ["is served", "is served", "they serve"],
 {"seven": ["7", "7 a.m."], "ten": ["10", "10 a.m."], "breakfast": ["breakfast"]},
 "present", "passive", False, False, False),

(150118, ["The coach stressed to the children that he doesn't let anyone onto the pitch without a warm-up.",
          "The coach emphasised to the kids that he lets nobody onto the field without a warm-up.",
          "The coach stressed to the children that without warming up he doesn't let anyone onto the field."],
 ["stressed + doesn't let", "emphasised + lets nobody", "stressed + doesn't let"],
 {"pitch": ["field", "playing field"], "stressed": ["emphasised", "emphasized"],
  "warm-up": ["warm up", "warming up"], "children": ["kids"]},
 "mixed", "active_agent", True, False, False),

(150119, ["Katka brought homemade lemonade to the party.",
          "Katka brought some homemade lemonade to the celebration.",
          "Katka brought home-made lemonade to the party."],
 ["brought", "brought", "brought"],
 {"homemade": ["home-made"], "party": ["celebration"], "lemonade": ["lemonade"]},
 "past", "active_agent", True, False, False),

(150120, ["Given the weather, the view from the lookout tower was surprisingly sharp.",
          "Considering the weather, the view from the observation tower was surprisingly clear.",
          "In view of the weather, the view from the lookout tower was surprisingly crisp."],
 ["Given + was", "Considering + was", "In view of + was"],
 {"Given": ["Considering", "In view of"],
  "lookout tower": ["observation tower", "viewing tower"], "sharp": ["clear", "crisp"]},
 "past", "active_agent", False, False, False),

(150121, ["By Thursday I will have gone through all those contracts once more.",
          "By Thursday I will go through all the contracts again.",
          "I will have been through all those contracts one more time by Thursday."],
 ["will have gone through", "will go through", "will have been through"],
 {"gone through": ["been through", "reviewed"], "contracts": ["contracts"],
  "once more": ["again", "one more time"]},
 "future", "active_agent", True, True, False),

(150122, ["We send each other the notes through a shared document.",
          "We send the notes to each other via a shared document.",
          "We share the notes with each other in a shared document."],
 ["send", "send", "share"],
 {"through": ["via", "in"], "shared": ["common"], "notes": ["notes"]},
 "present", "active_agent", True, False, False),

(150123, ["Despite two coffees, sleepiness overcame me after lunch.",
          "In spite of two coffees, drowsiness got the better of me after lunch.",
          "Despite two coffees, I got sleepy after lunch."],
 ["overcame", "got the better of", "got sleepy"],
 {"sleepiness": ["drowsiness"], "Despite": ["In spite of"], "coffees": ["cups of coffee"]},
 "past", "active_agent", False, False, False),

(150124, ["In that interview she admitted that she had stolen the idea from a colleague.",
          "In the interview she admitted she stole the idea from a colleague.",
          "She admitted in that interview that she had stolen a colleague's idea."],
 ["admitted + had stolen", "admitted + stole", "admitted + had stolen"],
 {"interview": ["conversation"], "idea": ["idea"], "colleague": ["co-worker", "colleague"]},
 "past", "active_agent", True, False, True),

(150125, ["The post office delivered the parcel a whole week later.",
          "The post delivered that parcel a full week later.",
          "The post office delivered the package a whole week later."],
 ["delivered", "delivered", "delivered"],
 {"parcel": ["package", "shipment", "delivery"], "post office": ["post", "postal service"],
  "whole": ["full", "entire"]},
 "past", "active_agent", True, False, False),

(150126, ["The documents had been signed before we arrived.",
          "The documents were signed before our arrival.",
          "Those documents had been signed before our arrival."],
 ["had been signed", "were signed", "had been signed"],
 {"documents": ["papers"], "before we arrived": ["before our arrival"]},
 "past", "passive", False, False, False),

(150127, ["We will move the sofa into the new room for you over the weekend.",
          "We'll move that couch to the new room for you at the weekend.",
          "Over the weekend we will move the sofa into the new room for you."],
 ["will move", "will move", "will move"],
 {"sofa": ["couch", "settee"], "over the weekend": ["at the weekend", "on the weekend"],
  "room": ["room"]},
 "future", "active_agent", True, True, False),

(150128, ["The neighbour's children regularly walk our dog after school.",
          "The neighbour's kids regularly take our dog for a walk after school.",
          "Our neighbor's children walk our dog regularly after school."],
 ["walk", "take for a walk", "walk"],
 {"neighbour's": ["neighbor's"], "children": ["kids"], "regularly": ["regularly"]},
 "present", "active_agent", True, False, False),

(150129, ["If it had not been for the delay, we would have made it to the concert as well.",
          "But for the delay, we would have caught the concert too.",
          "If there had not been that delay, we would have made the concert too."],
 ["had not been + would have made", "But for + would have caught", "had not been + would have made"],
 {"delay": ["hold-up", "delay"], "as well": ["too"], "concert": ["concert"]},
 "conditional", "active_agent", False, False, False),

(150130, ["They are asking us whether we still rent out the room.",
          "They ask us if we are still renting out the room.",
          "They are asking us if we still let the room."],
 ["are asking + rent out", "ask + are renting out", "are asking + let"],
 {"whether": ["if"], "rent out": ["let"], "room": ["room"]},
 "present", "active_agent", True, False, True),

(150131, ["I do my homework right after lunch.",
          "I do homework straight after lunch.",
          "I do my homework immediately after lunch."],
 ["do", "do", "do"],
 {"right": ["straight", "immediately"], "homework": ["homework"], "lunch": ["lunch"]},
 "present", "active_agent", True, False, False),

(150132, ["There are a lot of quiet places to read in that library.",
          "There are many quiet spots for reading in the library.",
          "In that library there are lots of quiet places to read."],
 ["there are", "there are", "there are"],
 {"a lot of": ["lots of", "many"], "places": ["spots"], "quiet": ["quiet"]},
 "present", "active_agent", False, False, False),

(150133, ["By the end of the summer the town will have repaired the bridge over the stream.",
          "By the end of summer the city will repair that bridge over the creek.",
          "The town will have fixed the bridge over the brook by the end of the summer."],
 ["will have repaired", "will repair", "will have fixed"],
 {"town": ["city"], "stream": ["creek", "brook"], "repaired": ["fixed", "mended"]},
 "future", "active_agent", True, True, False),

(150134, ["On Monday I wrote to them that we would pay the invoice by Friday.",
          "I wrote to them on Monday that we will pay the invoice by Friday.",
          "On Monday I wrote to them that we would settle the invoice by Friday."],
 ["wrote + would pay", "wrote + will pay", "wrote + would settle"],
 {"invoice": ["bill"], "pay": ["settle"], "wrote to": ["wrote"]},
 "mixed", "active_agent", True, True, True),

(150135, ["People drive very carefully on this bend.",
          "You drive very carefully on this bend.",
          "One drives very carefully on this curve."],
 ["drive", "drive", "drives"],
 {"bend": ["curve", "corner"], "carefully": ["cautiously"]},
 "present", "impersonal", False, False, False),

(150136, ["The photographer captured that moment in exactly the right light.",
          "The photographer caught the moment in just the right light.",
          "The photographer captured the moment in precisely the right light."],
 ["captured", "caught", "captured"],
 {"captured": ["caught"], "exactly": ["precisely", "just"], "moment": ["instant"]},
 "past", "active_agent", True, False, False),

(150137, ["In that email you wrote that they had already processed the order.",
          "You wrote in the email that they already processed the order.",
          "In that e-mail you wrote that they had processed the order already."],
 ["wrote + had processed", "wrote + processed", "wrote + had processed"],
 {"email": ["e-mail"], "processed": ["dealt with", "handled"], "order": ["order"]},
 "past", "active_agent", True, False, True),

(150138, ["During the holidays there are more people here than in winter.",
          "In the holidays there are usually more people here than in the winter.",
          "During the holidays there tend to be more people here than in winter."],
 ["there are + than", "there are + than", "there tend to be + than"],
 {"holidays": ["school holidays", "vacation"], "winter": ["the winter"]},
 "present", "active_agent", False, False, False),

(150139, ["Our house stands right next to a small park.",
          "Our house is right next to a small park.",
          "Our house stands just beside a small park."],
 ["stands", "is", "stands"],
 {"right": ["just"], "next to": ["beside", "by"], "stands": ["is"]},
 "present", "active_agent", False, False, False),

(150140, ["The concert lasted almost three hours without a break.",
          "That concert went on for nearly three hours without a break.",
          "The concert lasted nearly three hours with no interval."],
 ["lasted", "went on for", "lasted"],
 {"almost": ["nearly"], "break": ["interval", "intermission"], "lasted": ["went on for", "ran for"]},
 "past", "active_agent", False, False, False),
]


def log(n, purpose, what):
    rec = {"ts": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
           "side": "1m:new", "what": what, "caller": "make_annotations_part2.py (annotate-2)",
           "n": n, "purpose": purpose}
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    sents = json.load(open(SENT, encoding="utf-8"))
    log(len(sents), "annotate sid 150071..150140 (references, variants, locks, gold metadata); 0 model calls",
        "sentences.json (slovak + level + tags)")
    by_sid = {s["sid"]: s for s in sents}

    out = {}
    for (sid, refs, locks, alt, tf, voice, agent_nom, perf, topen) in ROWS:
        s = by_sid[sid]
        assert len(refs) == len(locks), sid
        assert len(set(refs)) == len(refs), sid
        # gold metadata must agree with the sentence writer's tags
        assert bool(s["tags"]["nom_agent"]) == agent_nom, ("agent_nom", sid)
        assert bool(s["tags"]["perfective_future"]) == perf, ("perf", sid)
        assert bool(s["tags"]["impersonal_or_passive"]) == (voice in ("impersonal", "passive")), ("voice", sid)
        for k in alt:
            assert any(k in r for r in refs), ("alt key not in a reference", sid, k)
        ann = {"id": sid, "t": 9000 + (sid - 150001), "lv": s["level"],
               "v": list(refs), "lk": list(locks), "alt": alt}
        out[str(sid)] = {"hygienised": ann, "raw": json.loads(json.dumps(ann)),
                         "tf_gold": tf, "voice_sk": voice, "agent_nom": agent_nom,
                         "perfective_present": perf, "tense_open": topen}

    assert sorted(int(k) for k in out) == list(range(150071, 150141)), "sid coverage"
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)

    tf_counts, voice_counts = {}, {}
    for r in out.values():
        tf_counts[r["tf_gold"]] = tf_counts.get(r["tf_gold"], 0) + 1
        voice_counts[r["voice_sk"]] = voice_counts.get(r["voice_sk"], 0) + 1
    print("n =", len(out))
    print("refs total =", sum(len(r["hygienised"]["v"]) for r in out.values()))
    print("tf_gold", tf_counts)
    print("voice_sk", voice_counts)
    print("agent_nom", sum(1 for r in out.values() if r["agent_nom"]),
          "perf_present", sum(1 for r in out.values() if r["perfective_present"]),
          "tense_open", sum(1 for r in out.values() if r["tense_open"]))


if __name__ == "__main__":
    main()
