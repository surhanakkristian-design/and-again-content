# F6 - ADDITION GUARD: build + validation on the closed 1N set

Phase 1Q, Task B2/B3. 0 model calls, 0 DB. Data: `phase1n` (100 sentences, 900 items, 900 judged labels).

## Design (10 lines)

1. Owner's rule: an OMISSION is accepted, an ADDITION is rejected. F5 (frozen) covers omissions; F6 is its mirror.
2. F6 is 100% offline and deterministic: `check(slovak, annotation, answer)`, same calling style as phase1n/f8.py, and it unwraps the 1N/1P annotation container (`hygienised` / `raw`) itself.
3. The LICENSED VOCABULARY of a sentence = content lemmas of ALL stored renderings `v` + every `alt` key + every `alt` synonym + a closed function-word list (articles, auxiliaries, modals, pronouns, light prepositions, contractions, degree words, just/already/that ...).
4. Matching is done under light lemmatisation: plural -s/-es/-ies, -ed, -ing (with consonant doubling), -ly, -ise/-ize, -our/-or, digits -> number words, plus an irregular table (children, took, wrote, ground, mum/dad ...).
5. Every answer content token whose lemma is not licensed is an EXTRA; adjacent extras (separated by at most one function word) are merged into one addition GROUP.
6. Rejection is allowed only where it is safe: content overlap with the licensed vocabulary must be high AND the number of addition groups small. A free paraphrase full of unknown words ABSTAINS - never rejects.
7. An addition group is ANCHORED if it sits inside a prepositional phrase ("in the pot", "at night") or forms a determined noun phrase of its own (an extra object).
8. Variant A is aggressive (overlap >= 0.70, <= 3 groups, a lone extra adjective/adverb suffices), B is middle (overlap >= 0.85, <= 2 groups, lone modifier suffices), C is conservative (overlap >= 0.80, <= 2 groups, at least one STRICTLY anchored group - the extra phrase must be introduced by a preposition, optionally with one article - and a lone extra modifier abstains).
9. Verdicts: `reject` with the blamed phrase(s) and reason "added meaning"; `accept` when every content word is licensed; `abstain` in every unsafe case (no references, <3 content tokens, low overlap, diffuse unknowns, modifier-only under C).
10. Validation is two-sided: hand gold (does it catch a planted addition without hurting a faithful reword?) and MEASURED COST on the real judged 1N answers - and only the measured cost selects the variant.

## Variants

| variant | min overlap | max addition groups | anchored group required | lone modifier rejects |
|---|---|---|---|---|
| A | 0.70 | 3 | no | yes |
| B | 0.85 | 2 | no | yes |
| C | 0.80 | 2 | yes (strict) | no |

## (a) Hand gold - 100 sentences x 2 answers (`f6_gold_1n.json`)

`faithful` = a correct reworded answer, gold = must NOT be rejected. `added` = the same answer plus one content
addition the Slovak lacks, gold = should be rejected. agree = addition rejected; conservative = addition not
rejected (missed catch, harmless); ERROR = a faithful answer rejected.

| variant | agree | conservative | ERROR |
|---|---|---|---|
| A | 99/100 | 1 | 0 |
| B | 52/100 | 48 | 0 |
| C | 63/100 | 37 | 0 |

### A - every ERROR (faithful answer rejected)

none.

### B - every ERROR (faithful answer rejected)

none.

### C - every ERROR (faithful answer rejected)

none.

## (b) MEASURED COST on the judged 1N answers (this selects the variant)

| variant | cost (judged-CORRECT rejected) | cost %% | catches (judged-WRONG rejected) | by wrong type |
|---|---|---|---|---|
| A | 73/426 | 17.14 | 203/474 | M 69/474, S 17/474, T 35/474, W 82/474 |
| B | 21/426 | 4.93 | 63/474 | M 30/474, S 5/474, T 6/474, W 22/474 |
| C | 2/426 | 0.47 | 33/474 | M 17/474, S 1/474, T 1/474, W 14/474 |

### A - every cost item (judged CORRECT, F6 rejected)

- `C:160002:2838066364` - "My classmate wrote to me that he had read three chapters of the manual in one evening alone." -> blamed `['alone']`
- `C:160003:2135372361` - "We're planning to lend you the big tent for the whole weekend." -> blamed `['planning']`
- `C:160003:3517424121` - "You are going to be lent the big tent by us for the whole weekend." -> blamed `['lent']`
- `C:160004:4269033017` - "The manuscript only surfaced during the demolition of the old rectory." -> blamed `['surfaced']`
- `C:160004:1967106358` - "The manuscript only turned up during the demolition of the old rectory." -> blamed `['turned']`
- `C:160004:4169223286` - "The manuscript only emerged during the demolition of the old rectory." -> blamed `['emerged']`
- `C:160005:3321050425` - "He's gluing the broken bowl on the kitchen counter at the moment." -> blamed `['moment']`
- `C:160010:1534777773` - "In the evenings, I water the small cacti on the windowsill." -> blamed `['evenings']`
- `W:160013:1795021316` - "The tinsmith has been polishing the copper pot since early morning." -> blamed `['pot']`
- `C:160017:906073326` - "He claims that the stamp collection is managed by his older brother." -> blamed `['managed']`
- `C:160023:1062113214` - "You can open the stuck drawer with a single motion." -> blamed `['single']`
- `C:160023:3426530632` - "With a single motion, you can open the stuck drawer." -> blamed `['single']`
- `C:160023:93773052` - "The stuck drawer can be opened by you with a single motion." -> blamed `['single']`
- `C:160024:1306812566` - "Klára told us that the old viola had been brought to the rehearsal by her alone." -> blamed `['alone']`
- `C:160024:2621707485` - "Klára told us that the old viola had been brought to the rehearsal without any help." -> blamed `['help']`
- `C:160025:1880231209` - "There isn't much free shelf space in that old warehouse." -> blamed `['space']`
- `C:160026:1450188755` - "They spent months translating the dictionary until they found a publisher." -> blamed `['spent']`
- `C:160027:3353548770` - "If the wire is bent too quickly by you, it always breaks." -> blamed `['bent']`
- `C:160029:2056183729` - "She took the portrait to the local framer to have it framed." -> blamed `['took']`
- `C:160030:49187296` - "From that small tower, they observe the old water power station." -> blamed `['observe']`
- `C:160031:1129994621` - "When they were students, they would rewrite old scores in the evenings." -> blamed `['rewrite']`
- `C:160031:2320019973` - "As students, they rewrote old sheet music in the evenings." -> blamed `['rewrote']`
- `C:160031:1866579597` - "As students, old scores were rewritten by them in the evenings." -> blamed `['rewritten']`
- `C:160032:1791944256` - "This morning there was a hard frost, and the stone steps were slippery." -> blamed `['frost']`
- `C:160033:1495618468` - "The bookseller told us that his partner sold the whole edition already last year." -> blamed `['whole']`
- `C:160034:3253945012` - "The potter living by the river fired our new bowl." -> blamed `['living']`
- `C:160035:4294101760` - "Look! She is right now nailing the last slat onto the birdhouse." -> blamed `['right now']`
- `C:160035:1168408523` - "Look! She's putting the last slat on the birdhouse." -> blamed `['putting']`
- `W:160035:3468432598` - "Look! She's nailing the last plank onto the birdhouse." -> blamed `['plank']`
- `C:160037:3711600977` - "The vet told us that he had treated the paw right away that evening." -> blamed `['right']`
- `C:160037:556661395` - "The vet informed us that he treated the paw immediately that evening." -> blamed `['immediately']`
- `C:160037:532456777` - "The vet let us know that he had treated the paw that very evening." -> blamed `['know']`
- `C:160037:3707987030` - "The vet told us that the paw had been treated by him right away that evening." -> blamed `['right']`
- `C:160038:1882478471` - "What are you currently drawing on the big piece of paper?" -> blamed `['currently']`
- `C:160039:1077518600` - "In this village, people will turn the old barns into craft workshops." -> blamed `['people']`
- `C:160039:516320789` - "The old barns in this village will become craft workshops." -> blamed `['become']`
- `C:160041:492941432` - "The leather backpack is worn by you more often than the lighter one from the closet." -> blamed `['worn']`
- `C:160043:301156123` - "He declined to sign the protocol without his lawyer." -> blamed `['declined']`
- `C:160044:2954733988` - "He will spend all day tomorrow hauling his tools to the new workshop." -> blamed `['spend']`
- `C:160047:466707344` - "He only plays the old tape for his guests on rare occasions." -> blamed `['occasions']`
- `C:160048:2618399930` - "The seamstress hems trousers every Wednesday afternoon." -> blamed `['hems']`
- `C:160049:1297275637` - "Grandpa will spend all week repairing the old alarm clock for us." -> blamed `['spend']`
- `C:160051:2890458528` - "Someone had covered the old well even before the first frost." -> blamed `['someone']`
- `C:160053:639438428` - "By evening he'll have been sanding the parquet floor for a full eight hours." -> blamed `['full']`
- `C:160053:1788043720` - "He will have been sanding the floor for eight straight hours by the time evening comes." -> blamed `['time evening comes']`
- `C:160057:2302201563` - "If he manages to catch the first ferry, he'll unload the material before lunch." -> blamed `['manages']`
- `C:160058:7291403` - "They stop working in this workshop after eight in the evening." -> blamed `['stop']`
- `C:160059:1075562601` - "The optician, who came recommended to us, ground the new lenses within two days." -> blamed `['came']`
- `C:160061:3263714663` - "You'll be moving the new chairs into the hall all morning." -> blamed `['moving']`
- `C:160061:84504196` - "You will spend all morning putting the new chairs into the hall." -> blamed `['spend']`
- `C:160063:1871774504` - "The ranger told us that he had marked the trail with new signs." -> blamed `['ranger']`
- `C:160063:4286975244` - "The ranger told us that he'd marked the trail using new signs." -> blamed `['ranger', 'using']`
- `C:160063:3105715525` - "The ranger told us that the trail had been marked with new signs by him." -> blamed `['ranger']`
- `C:160072:4116318361` - "If she finds the original plan, the whole tower will be assembled correctly by her." -> blamed `['assembled']`
- `C:160072:274946338` - "If she finds the original plan, the whole tower will be assembled correctly." -> blamed `['assembled']`
- `W:160072:3478128531` - "If she finds the original plan, she will be assembling the whole tower correctly." -> blamed `['assembling']`
- `C:160073:3063388935` - "Every Thursday, you bring the heavy crates down to the cellar." -> blamed `['bring']`
- `C:160078:1602676086` - "My mother used to make us costumes for school pageants." -> blamed `['pageants']`
- `C:160082:4084815432` - "She's putting the glass cups into the wooden crate right now." -> blamed `['cups']`
- `C:160082:266462698` - "Right now she is placing the glasses into the wooden box." -> blamed `['placing']`
- `C:160083:1323310080` - "He is currently putting together the white tent structure on the extension's roof." -> blamed `['currently']`
- `C:160086:428996114` - "By the end of the month, they will have finished cataloguing the entire parish archive." -> blamed `['finished']`
- `W:160086:22552553` - "By the end of the month they will have catalogued the entire church archive." -> blamed `['church']`
- `C:160089:2138348670` - "The collector is planning to lend the drawings to the small town museum." -> blamed `['planning']`
- `C:160089:2122673680` - "The drawings are going to be lent to the small city museum by the collector." -> blamed `['lent']`
- `C:160090:1614246231` - "Paper and glass are sorted into two large bins by us." -> blamed `['sorted']`
- `C:160091:4175648795` - "You'll be drying the winter jackets near the stove for the whole evening." -> blamed `['whole']`
- `C:160093:1903262848` - "The librarian told me that he had already skimmed through three thick catalogues today." -> blamed `['skimmed']`
- `C:160094:1386141952` - "Tonight I'll lock the back gate and turn the lamp off." -> blamed `['tonight']`
- `C:160096:1295681235` - "If we get hold of a longer ladder, we will fix the roof antenna ourselves." -> blamed `['hold']`
- `C:160098:967233374` - "Every morning, someone winds the old clock in this museum." -> blamed `['someone']`
- `C:160099:1418700867` - "The painters will be repainting the building's facade throughout next week." -> blamed `['throughout']`
- `C:160099:1305040546` - "Next week the painters will be repainting the facade all week long." -> blamed `['long']`

### A - every catch (judged WRONG, F6 rejected)

- [M] `W:160006:3928976931` - "While the pan was heating up, Martin quickly cut the onion into thin slices." -> blamed `['quickly']`
- [M] `W:160008:4188891391` - "There are three capsized boats on the wooden pier this morning." -> blamed `['morning']`
- [M] `W:160010:1624476389` - "In the evening, I carefully water the small cacti on the windowsill." -> blamed `['carefully']`
- [M] `W:160016:4174469790` - "He is pouring a little more olive oil into the pan on the stove." -> blamed `['stove']`
- [M] `W:160027:2586756093` - "If you bend the wire too quickly, it always breaks immediately." -> blamed `['immediately']`
- [M] `W:160028:2935212793` - "You must take the empty bottles to the container in front of the house today." -> blamed `['today']`
- [M] `W:160029:563782658` - "She had the portrait framed twice at the local framer's." -> blamed `['twice']`
- [M] `W:160030:3254405789` - "From that little tower, they watch the old hydroelectric power plant every day." -> blamed `['day']`
- [M] `W:160031:746312126` - "As students, they used to copy out old scores in the evenings and mornings." -> blamed `['mornings']`
- [M] `W:160033:2240312050` - "The bookseller explained to us that his partner had sold out the edition already last year in Bratislava." -> blamed `['bratislava']`
- [M] `W:160034:2087879417` - "The potter who lives by the river fired our new bowl yesterday." -> blamed `['yesterday']`
- [M] `W:160035:2887988769` - "Look! She's nailing the last slat onto the new birdhouse." -> blamed `['new']`
- [M] `W:160036:2313877179` - "She was supposed to reinforce the frame before it was moved to the new gallery." -> blamed `['new']`
- [M] `W:160037:949323144` - "The vet told us that he treated the paw right away that evening at the clinic." -> blamed `['right', 'clinic']`
- [M] `W:160038:3418813463` - "What are you drawing on the big paper today?" -> blamed `['today']`
- [M] `W:160039:1428404458` - "In this village, they will convert the old barns into craft workshops next year." -> blamed `['next year']`
- [M] `W:160040:2115077106` - "When the bell rang, Emma was still putting the tools away in the cabinet quickly." -> blamed `['quickly']`
- [M] `W:160041:141773969` - "You wear the leather backpack more often than the lighter one from the closet these days." -> blamed `['days']`
- [M] `W:160042:3232135601` - "The glazier will put the last piece of colored glass into the window only on Monday morning." -> blamed `['morning']`
- [M] `W:160043:228518651` - "He refused to sign the protocol without his lawyer yesterday." -> blamed `['yesterday']`
- [M] `W:160045:3585801245` - "She confirmed to us that she had photographed the whole platform twice before the train left." -> blamed `['twice']`
- [M] `W:160046:3537202060` - "She usually writes the notes by hand, but today she's quickly dictating them into her phone." -> blamed `['quickly']`
- [M] `W:160047:1026559451` - "Only rarely does he play the old tape for his guests in the evening." -> blamed `['evening']`
- [M] `W:160048:3962462903` - "The seamstress always shortens trousers quickly on Wednesday afternoons." -> blamed `['quickly']`
- [M] `W:160050:3988563744` - "The restorer explained to us that she had removed three layers of varnish from the canvas carefully." -> blamed `['carefully']`
- [M] `W:160051:1051389211` - "They covered the old well in the back garden before the first frost." -> blamed `['garden']`
- [M] `W:160052:2545533513` - "You sanded down the wooden bench on the terrace on Saturday morning." -> blamed `['morning']`
- [M] `W:160054:3190258738` - "The electrician has already replaced all the old switches in our house and garage." -> blamed `['garage']`
- [M] `W:160056:2484990955` - "He claims that he restocks the display case with new samples every week at the shop." -> blamed `['shop']`
- [M] `W:160057:2952792659` - "If he catches the first ferry, he will unload the material before lunch at the warehouse." -> blamed `['warehouse']`
- [M] `W:160058:1498558162` - "People don't work in this workshop after eight in the evening on weekdays." -> blamed `['weekdays']`
- [M] `W:160059:3158723589` - "The optician who was recommended to us ground the new lenses in two days at the shop." -> blamed `['shop']`
- [M] `W:160060:2372897725` - "While the train stood in the station for ten minutes, the engineer topped up the water in the tank." -> blamed `['ten minutes']`
- [M] `W:160062:3478262337` - "If she had arrived at the venue an hour earlier, she would have won the auction." -> blamed `['venue']`
- [M] `W:160064:3150362732` - "My aunt knits thick woolen socks for the kids every winter in her cottage." -> blamed `['cottage']`
- [M] `W:160065:77340970` - "The blacksmith will forge two new iron hinges for the gate by the end of the week." -> blamed `['iron']`
- [M] `W:160066:3317709807` - "You will have to return the borrowed tools to the shop this week." -> blamed `['shop']`
- [M] `W:160067:1064388204` - "Tomáš locked the workshop and turned off all the lights above the workbench before leaving." -> blamed `['leaving']`
- [M] `W:160068:2206489589` - "The carpenter didn't have exact measurements, but he nevertheless hung the shelf completely straight in the kitchen." -> blamed `['kitchen']`
- [M] `W:160069:3804322864` - "I will return the two books about the mountains to you on Tuesday morning." -> blamed `['morning']`
- [M] `W:160070:178260700` - "There is a small glass elevator at the end of the long hallway." -> blamed `['long']`
- [M] `W:160071:4235946203` - "She stated in the email that she had rewritten the entire conclusion of the annual report twice already." -> blamed `['annual']`
- [M] `W:160072:2231180239` - "If she finds the original plan, she will assemble the whole tower correctly by tomorrow." -> blamed `['tomorrow']`
- [M] `W:160073:2095805535` - "You carry the heavy crates down to the cellar every Thursday morning." -> blamed `['morning']`
- [M] `W:160074:767667309` - "Someone must have changed the lock yesterday, because the old key no longer fit." -> blamed `['yesterday']`
- [M] `W:160075:232261743` - "They informed us that they had already fixed the elevator on Wednesday morning." -> blamed `['morning']`
- [M] `W:160077:1581836163` - "The archivist put the letters into new protective covers yesterday." -> blamed `['yesterday']`
- [M] `W:160078:4175667485` - "My mother used to sew us costumes for school shows every autumn." -> blamed `['autumn']`
- [M] `W:160079:1568287400` - "On Fridays they hang the washing in the yard behind the old house." -> blamed `['old']`
- [M] `W:160080:3072555526` - "I wish he hadn't cut down that old walnut tree in the garden so soon." -> blamed `['garden']`
- [M] `W:160081:2577126122` - "The bookbinder who accompanied us also opened the locked cellar downstairs." -> blamed `['downstairs']`
- [M] `W:160082:1337566022` - "She is just putting the glasses into the wooden crate in the cellar." -> blamed `['cellar']`
- [M] `W:160083:3115191267` - "Right now he is assembling the white tent frame on the roof of the extension alone." -> blamed `['alone']`
- [M] `W:160084:1494980830` - "They say he is varnishing the boat alone for the second week already." -> blamed `['alone']`
- [M] `W:160085:509122295` - "Dad carried the old magazines up to the attic yesterday." -> blamed `['yesterday']`
- [M] `W:160086:1753395699` - "By the end of the month they will have catalogued the entire parish archive twice." -> blamed `['twice']`
- [M] `W:160087:925865824` - "Nina sands the edges more precisely than any of her classmates every time." -> blamed `['time']`
- [M] `W:160088:1803966261` - "Our uncle carves wooden whistles for the children every summer in the barn." -> blamed `['barn']`
- [M] `W:160089:1979506313` - "The collector is going to lend the drawings to the small city museum next month." -> blamed `['next month']`
- [M] `W:160090:2166122707` - "We sort paper and glass into two large bins in the garage." -> blamed `['garage']`
- [M] `W:160091:604480205` - "You will be drying those winter jackets near the stove all evening tomorrow." -> blamed `['tomorrow']`
- [M] `W:160092:659753260` - "You will send us the signed forms by Sunday morning." -> blamed `['morning']`
- [M] `W:160093:1375639567` - "The librarian told me that he had already leafed through three thick catalogues at his desk today." -> blamed `['desk']`
- [M] `W:160094:603959753` - "This evening I'll lock the back gate and turn off the lamp in the hallway." -> blamed `['hallway']`
- [M] `W:160095:2582455917` - "You told us that your colleague had installed the new server yesterday." -> blamed `['yesterday']`
- [M] `W:160096:1520601244` - "If we get a longer ladder, we'll fix the antenna on the roof ourselves this weekend." -> blamed `['weekend']`
- [M] `W:160097:2748705831` - "There are still a few unused envelopes in that small box." -> blamed `['small']`
- [M] `W:160098:2868378039` - "In this museum, they carefully wind the old clock every morning." -> blamed `['carefully']`
- [M] `W:160099:3469279537` - "The painters will be repainting the facade all next week using new paint." -> blamed `['using new']`
- [S] `W:160009:3113223159` - "The boatman told us that he had pull up the anchor before the storm." -> blamed `['pull']`
- [S] `W:160011:104839409` - "If he had packed a spare inner tube, he would have change the burst tire right away." -> blamed `['change']`
- [S] `W:160015:2444777832` - "Despite the strong wind, Viktor brung the seedlings all the way to the upper terrace." -> blamed `['brung']`
- [S] `W:160017:2966050552` - "He claims that his older brother manage the stamp collection." -> blamed `['manage']`
- [S] `W:160023:3124882936` - "You can opens the stuck drawer with a single motion." -> blamed `['single']`
- [S] `W:160034:3106874878` - "The potter who live by the river fired our new bowl." -> blamed `['live']`
- [S] `W:160035:1850597999` - "Look! She's nailing the last slat on the birdhouses." -> blamed `['birdhouses']`
- [S] `W:160036:2198134728` - "She was suppose to reinforce the frame before it was moved to the gallery." -> blamed `['suppose']`
- [S] `W:160063:1002738839` - "The ranger told us that he had marked the trail with new sign." -> blamed `['ranger']`
- [S] `W:160074:2683293539` - "Someone must have change the lock, because the old key no longer fit." -> blamed `['change']`
- [S] `W:160080:681453355` - "I wish he hadn't cut down that old walnut trees so soon." -> blamed `['trees']`
- [S] `W:160087:1971952769` - "Nina sands the edges more precisely than any of her classmate." -> blamed `['classmate']`
- [S] `W:160088:2332679073` - "Our uncle carve wooden whistles for the children every summer." -> blamed `['carve']`
- [S] `W:160093:1637774775` - "The librarian told me that he had already leafed through three thick catalogue today." -> blamed `['catalogue']`
- [S] `W:160096:2035367221` - "If we get a longer ladder, we'll fix the antenna on the roof ourself." -> blamed `['ourself']`
- [S] `W:160097:2222056282` - "There are still a few unused envelope in that box." -> blamed `['envelope']`
- [S] `W:160100:171208197` - "Next season he will run the workshop and train two new apprentice." -> blamed `['apprentice']`
- [T] `W:160003:2580127930` - "We lent you the big tent for the whole weekend." -> blamed `['lent']`
- [T] `W:160009:1124264627` - "The boatman told us that he pulls up the anchor before the storm." -> blamed `['pulls']`
- [T] `W:160009:2100234577` - "The boatman told us that he will pull up the anchor before the storm." -> blamed `['pull']`
- [T] `W:160011:755801872` - "If he packs a spare inner tube, he will change the burst tire right away." -> blamed `['change']`
- [T] `W:160011:2802632660` - "If he packed a spare inner tube, he would change the burst tire right away." -> blamed `['change']`
- [T] `W:160017:3925847377` - "He claims that his older brother managed the stamp collection." -> blamed `['managed']`
- [T] `W:160017:3576228434` - "He claims that his older brother will manage the stamp collection." -> blamed `['manage']`
- [T] `W:160020:2131529315` - "When we arrive, Janka has already set up the whole stall." -> blamed `['arrive']`
- [T] `W:160023:3700906187` - "You could open the stuck drawer with a single motion." -> blamed `['single']`
- [T] `W:160023:3500537672` - "You will be able to open the stuck drawer with a single motion." -> blamed `['single']`
- [T] `W:160027:1698233647` - "If you bent the wire too quickly, it always broke." -> blamed `['bent']`
- [T] `W:160032:1769850561` - "This morning it will freeze hard, and the stone steps will be slippery." -> blamed `['freeze']`
- [T] `W:160034:3882308682` - "The potter who lives by the river will fire our new bowl." -> blamed `['fire']`
- [T] `W:160037:1770464692` - "The vet will tell us that he treated the paw right away that evening." -> blamed `['right']`
- [T] `W:160040:1958628180` - "When the bell rings, Emma is still putting the tools away in the cabinet." -> blamed `['rings']`
- [T] `W:160041:929431187` - "You wore the leather backpack more often than the lighter one from the closet." -> blamed `['wore']`
- [T] `W:160043:669049242` - "He refuses to sign the protocol without his lawyer." -> blamed `['refuses']`
- [T] `W:160044:3840918748` - "He was carrying his tools to the new workshop all day yesterday." -> blamed `['yesterday']`
- [T] `W:160045:2934779696` - "She confirms to us that she photographs the whole platform before the train leaves." -> blamed `['leaves']`
- [T] `W:160045:4071300766` - "She will confirm to us that she photographed the whole platform before the train leaves." -> blamed `['leaves']`
- [T] `W:160050:250181732` - "The restorer explains to us that she removes three layers of varnish from the canvas." -> blamed `['removes']`
- [T] `W:160051:4182599872` - "They cover the old well before the first frost every year." -> blamed `['year']`
- [T] `W:160054:3660290647` - "The electrician will replace all the old switches in our house." -> blamed `['replace']`
- [T] `W:160054:2991901165` - "The electrician replaces all the old switches in our house every month." -> blamed `['month']`
- [T] `W:160063:2581623565` - "The ranger tells us that he marks the trail with new signs." -> blamed `['ranger']`
- [T] `W:160063:2563379946` - "The ranger told us that he will mark the trail with new signs." -> blamed `['ranger']`
- [T] `W:160072:3344401763` - "If she found the original plan, she assembled the whole tower correctly." -> blamed `['assembled']`
- [T] `W:160074:2436279832` - "Someone must change the lock, because the old key no longer fits." -> blamed `['change']`
- [T] `W:160074:889570342` - "Someone will have to change the lock, because the old key no longer fits." -> blamed `['change']`
- [T] `W:160076:1290359431` - "Don't worry, he pumped up that front wheel for you yesterday evening." -> blamed `['yesterday']`
- [T] `W:160083:4078334035` - "He will assemble the white tent frame on the roof of the extension." -> blamed `['assemble']`
- [T] `W:160086:636477818` - "By the end of the month they catalogue the entire parish archive." -> blamed `['catalogue']`
- [T] `W:160089:417449013` - "The collector lent the drawings to the small city museum." -> blamed `['lent']`
- [T] `W:160090:2085026142` - "We sorted paper and glass into two large bins." -> blamed `['sorted']`
- [T] `W:160099:1515929851` - "The painters were repainting the facade all last week." -> blamed `['last']`
- [W] `W:160002:2583597915` - "A classmate wrote to me that he had read three chapters of the novel in a single evening." -> blamed `['novel']`
- [W] `W:160003:2098541045` - "We are going to lend you the small tent for the whole weekend." -> blamed `['small']`
- [W] `W:160005:3472438787` - "He is gluing the broken plate on the kitchen counter right now." -> blamed `['plate']`
- [W] `W:160006:777519295` - "While the pan was heating up, Martin cut the pepper into thin slices." -> blamed `['pepper']`
- [W] `W:160007:3692739909` - "By Saturday, she will have digitized all the family photographs." -> blamed `['photographs']`
- [W] `W:160009:792463771` - "The boatman told us that he had pulled up the rope before the storm." -> blamed `['rope']`
- [W] `W:160010:2579519228` - "In the evening, I water the small cacti on the balcony." -> blamed `['balcony']`
- [W] `W:160011:269314103` - "If he had packed a spare inner tube, he would have changed the flat battery right away." -> blamed `['flat battery']`
- [W] `W:160012:1057727893` - "Zuzana will be polishing the copper window handles all afternoon." -> blamed `['window']`
- [W] `W:160014:2784220578` - "Today the bookbinder will sew eighteen old letters into one volume." -> blamed `['letters']`
- [W] `W:160015:3371435989` - "Despite the strong wind, Viktor brought the seedlings all the way to the lower terrace." -> blamed `['lower']`
- [W] `W:160016:435720202` - "He is pouring a little more sunflower oil into the pan." -> blamed `['sunflower']`
- [W] `W:160017:366149980` - "He claims that his younger brother manages the stamp collection." -> blamed `['younger']`
- [W] `W:160018:120191724` - "If she hadn't broken her ankle last year, she would be playing the sonata from memory today." -> blamed `['ankle']`
- [W] `W:160019:3375095162` - "She is hanging the two maps above the desk in the small kitchen." -> blamed `['kitchen']`
- [W] `W:160020:2303126489` - "When we arrived, Janka had already set up the whole tent." -> blamed `['tent']`
- [W] `W:160021:175431379` - "You will clean the clogged drain only after the first rain." -> blamed `['drain']`
- [W] `W:160024:1879534076` - "Klára told us that she had brought the old cello to the rehearsal herself." -> blamed `['cello']`
- [W] `W:160025:3431272717` - "There aren't many free shelves in that old garage." -> blamed `['garage']`
- [W] `W:160026:3805685081` - "They translated the novel for months until they found a publisher." -> blamed `['novel']`
- [W] `W:160028:3612433847` - "You must take the empty cans to the container in front of the house." -> blamed `['cans']`
- [W] `W:160029:4114308985` - "She had the painting framed at the local framer's." -> blamed `['painting']`
- [W] `W:160030:3803648068` - "From that little tower, they watch the old wind power plant." -> blamed `['wind']`
- [W] `W:160031:3322922544` - "As students, they used to copy out old letters in the evenings." -> blamed `['letters']`
- [W] `W:160032:3803709862` - "This morning it was freezing hard, and the wooden steps were slippery." -> blamed `['wooden']`
- [W] `W:160033:1935520559` - "The bookseller explained to us that his brother had sold out the edition already last year." -> blamed `['brother']`
- [W] `W:160034:789166685` - "The potter who lives by the river fired our new vase." -> blamed `['vase']`
- [W] `W:160036:221344268` - "She was supposed to reinforce the canvas before it was moved to the gallery." -> blamed `['canvas']`
- [W] `W:160039:3346842208` - "In this village, they will convert the old mills into craft workshops." -> blamed `['mills']`
- [W] `W:160040:754125721` - "When the bell rang, Emma was still putting the books away in the cabinet." -> blamed `['books']`
- [W] `W:160041:652690445` - "You wear the leather backpack more often than the lighter one from the drawer." -> blamed `['drawer']`
- [W] `W:160042:3107984404` - "The glazier will put the last piece of colored glass into the door only on Monday." -> blamed `['door']`
- [W] `W:160043:2870518479` - "He refused to sign the contract without his lawyer." -> blamed `['contract']`
- [W] `W:160044:3886744523` - "Tomorrow he will be carrying his tools to the new factory all day." -> blamed `['factory']`
- [W] `W:160045:4130518605` - "She confirmed to us that she had photographed the whole waiting room before the train left." -> blamed `['waiting room']`
- [W] `W:160046:2590077163` - "She usually writes the notes by hand, but today she's dictating them into her tablet." -> blamed `['tablet']`
- [W] `W:160048:3843784637` - "The seamstress always shortens skirts on Wednesday afternoons." -> blamed `['skirts']`
- [W] `W:160049:3846996108` - "Grandpa will be repairing the old watch for us all week." -> blamed `['watch']`
- [W] `W:160051:1886506052` - "They covered the old barn before the first frost." -> blamed `['barn']`
- [W] `W:160052:2402388794` - "You sanded down the wooden table on the terrace on Saturday." -> blamed `['table']`
- [W] `W:160053:991834334` - "By evening, he will have been sanding the table for eight hours straight." -> blamed `['table']`
- [W] `W:160054:870956606` - "The electrician has already replaced all the old sockets in our house." -> blamed `['sockets']`
- [W] `W:160055:2853330100` - "The new backpack is light and surprisingly spacious." -> blamed `['backpack']`
- [W] `W:160056:1764933359` - "He claims that he restocks the display case with new tools every week." -> blamed `['tools']`
- [W] `W:160057:97017393` - "If he catches the first ferry, he will unload the material before dinner." -> blamed `['dinner']`
- [W] `W:160058:3950276389` - "People don't work in this warehouse after eight in the evening." -> blamed `['warehouse']`
- [W] `W:160059:934567951` - "The optician who was recommended to us ground the new frames in two days." -> blamed `['frames']`
- [W] `W:160060:3385822710` - "While the train stood in the station, the engineer topped up the oil in the tank." -> blamed `['oil']`
- [W] `W:160061:2235458425` - "You will be putting the new tables into the hall all morning." -> blamed `['tables']`
- [W] `W:160062:4058537934` - "If she had arrived an hour earlier, she would have won the contract." -> blamed `['contract']`
- [W] `C:160063:786654740` - "The ranger told us he marked the trail with new signs." -> blamed `['ranger']`
- [W] `W:160064:2901669164` - "My aunt knits thick woolen scarves for the kids every winter." -> blamed `['scarves']`
- [W] `W:160065:4029605372` - "The blacksmith will forge two new hinges for the door by the end of the week." -> blamed `['door']`
- [W] `W:160067:337966924` - "Tomáš locked the workshop and turned off all the lights above the shelf." -> blamed `['shelf']`
- [W] `W:160068:2796834291` - "The carpenter didn't have exact measurements, but he nevertheless hung the cabinet completely straight." -> blamed `['cabinet']`
- [W] `W:160069:380454155` - "I will return the two books about the sea to you on Tuesday." -> blamed `['sea']`
- [W] `W:160070:1321132523` - "There is a small glass elevator at the end of the kitchen." -> blamed `['kitchen']`
- [W] `W:160071:4147820342` - "She stated in the email that she had rewritten the entire introduction of the report twice already." -> blamed `['introduction']`
- [W] `W:160072:2179265392` - "If she finds the original plan, she will assemble the whole bridge correctly." -> blamed `['bridge']`
- [W] `W:160074:207540240` - "Someone must have changed the padlock, because the old key no longer fit." -> blamed `['padlock']`
- [W] `W:160075:2376955677` - "They informed us that they had already fixed the escalator on Wednesday." -> blamed `['escalator']`
- [W] `W:160077:2765661329` - "The archivist put the photographs into new protective covers." -> blamed `['photographs']`
- [W] `W:160078:790376510` - "My mother used to sew us curtains for school shows." -> blamed `['curtains']`
- [W] `W:160080:3241612325` - "I wish he hadn't cut down that old oak tree so soon." -> blamed `['oak']`
- [W] `W:160081:2619424140` - "The bookbinder who accompanied us also opened the locked attic." -> blamed `['attic']`
- [W] `W:160082:3183706490` - "She is just putting the glasses into the wooden drawer." -> blamed `['drawer']`
- [W] `W:160083:106751501` - "Right now he is assembling the white tent frame on the roof of the garage." -> blamed `['garage']`
- [W] `W:160084:2080146466` - "They say he is varnishing the canoe for the second week already." -> blamed `['canoe']`
- [W] `W:160085:2936149097` - "Dad carried the old newspapers up to the attic." -> blamed `['newspapers']`
- [W] `W:160087:4258314838` - "Nina sands the corners more precisely than any of her classmates." -> blamed `['corners']`
- [W] `W:160089:502312985` - "The collector is going to lend the paintings to the small city museum." -> blamed `['paintings']`
- [W] `W:160090:2552003450` - "We sort paper and plastic into two large bins." -> blamed `['plastic']`
- [W] `W:160091:2754700349` - "You will be drying those winter jackets near the fireplace all evening." -> blamed `['fireplace']`
- [W] `W:160092:1820402762` - "You will send us the signed contracts by Sunday." -> blamed `['contracts']`
- [W] `W:160093:117196401` - "The librarian told me that he had already leafed through three thick books today." -> blamed `['books']`
- [W] `W:160094:507248919` - "This evening I'll lock the front gate and turn off the lamp." -> blamed `['front']`
- [W] `W:160095:315245074` - "You told us that your colleague installed the new router." -> blamed `['router']`
- [W] `W:160096:3765672169` - "If we get a longer ladder, we'll fix the antenna on the wall ourselves." -> blamed `['wall']`
- [W] `W:160097:1961800427` - "There are still a few unused stamps in that box." -> blamed `['stamps']`
- [W] `W:160098:3876526430` - "In this museum, they wind the old clock every evening." -> blamed `['evening']`
- [W] `W:160099:1384572640` - "The painters will be repainting the roof all next week." -> blamed `['roof']`
- [W] `W:160100:1627888490` - "Next season he will run the workshop and train two new employees." -> blamed `['employees']`

### B - every cost item (judged CORRECT, F6 rejected)

- `C:160002:2838066364` - "My classmate wrote to me that he had read three chapters of the manual in one evening alone." -> blamed `['alone']`
- `C:160024:1306812566` - "Klára told us that the old viola had been brought to the rehearsal by her alone." -> blamed `['alone']`
- `C:160024:2621707485` - "Klára told us that the old viola had been brought to the rehearsal without any help." -> blamed `['help']`
- `C:160030:49187296` - "From that small tower, they observe the old water power station." -> blamed `['observe']`
- `C:160033:1495618468` - "The bookseller told us that his partner sold the whole edition already last year." -> blamed `['whole']`
- `C:160039:1077518600` - "In this village, people will turn the old barns into craft workshops." -> blamed `['people']`
- `C:160044:2954733988` - "He will spend all day tomorrow hauling his tools to the new workshop." -> blamed `['spend']`
- `C:160049:1297275637` - "Grandpa will spend all week repairing the old alarm clock for us." -> blamed `['spend']`
- `C:160053:639438428` - "By evening he'll have been sanding the parquet floor for a full eight hours." -> blamed `['full']`
- `C:160057:2302201563` - "If he manages to catch the first ferry, he'll unload the material before lunch." -> blamed `['manages']`
- `C:160059:1075562601` - "The optician, who came recommended to us, ground the new lenses within two days." -> blamed `['came']`
- `C:160072:4116318361` - "If she finds the original plan, the whole tower will be assembled correctly by her." -> blamed `['assembled']`
- `C:160072:274946338` - "If she finds the original plan, the whole tower will be assembled correctly." -> blamed `['assembled']`
- `W:160072:3478128531` - "If she finds the original plan, she will be assembling the whole tower correctly." -> blamed `['assembling']`
- `C:160082:4084815432` - "She's putting the glass cups into the wooden crate right now." -> blamed `['cups']`
- `C:160083:1323310080` - "He is currently putting together the white tent structure on the extension's roof." -> blamed `['currently']`
- `C:160086:428996114` - "By the end of the month, they will have finished cataloguing the entire parish archive." -> blamed `['finished']`
- `C:160089:2138348670` - "The collector is planning to lend the drawings to the small town museum." -> blamed `['planning']`
- `C:160093:1903262848` - "The librarian told me that he had already skimmed through three thick catalogues today." -> blamed `['skimmed']`
- `C:160099:1418700867` - "The painters will be repainting the building's facade throughout next week." -> blamed `['throughout']`
- `C:160099:1305040546` - "Next week the painters will be repainting the facade all week long." -> blamed `['long']`

### B - every catch (judged WRONG, F6 rejected)

- [M] `W:160006:3928976931` - "While the pan was heating up, Martin quickly cut the onion into thin slices." -> blamed `['quickly']`
- [M] `W:160028:2935212793` - "You must take the empty bottles to the container in front of the house today." -> blamed `['today']`
- [M] `W:160030:3254405789` - "From that little tower, they watch the old hydroelectric power plant every day." -> blamed `['day']`
- [M] `W:160031:746312126` - "As students, they used to copy out old scores in the evenings and mornings." -> blamed `['mornings']`
- [M] `W:160033:2240312050` - "The bookseller explained to us that his partner had sold out the edition already last year in Bratislava." -> blamed `['bratislava']`
- [M] `W:160034:2087879417` - "The potter who lives by the river fired our new bowl yesterday." -> blamed `['yesterday']`
- [M] `W:160040:2115077106` - "When the bell rang, Emma was still putting the tools away in the cabinet quickly." -> blamed `['quickly']`
- [M] `W:160041:141773969` - "You wear the leather backpack more often than the lighter one from the closet these days." -> blamed `['days']`
- [M] `W:160042:3232135601` - "The glazier will put the last piece of colored glass into the window only on Monday morning." -> blamed `['morning']`
- [M] `W:160045:3585801245` - "She confirmed to us that she had photographed the whole platform twice before the train left." -> blamed `['twice']`
- [M] `W:160046:3537202060` - "She usually writes the notes by hand, but today she's quickly dictating them into her phone." -> blamed `['quickly']`
- [M] `W:160048:3962462903` - "The seamstress always shortens trousers quickly on Wednesday afternoons." -> blamed `['quickly']`
- [M] `W:160050:3988563744` - "The restorer explained to us that she had removed three layers of varnish from the canvas carefully." -> blamed `['carefully']`
- [M] `W:160056:2484990955` - "He claims that he restocks the display case with new samples every week at the shop." -> blamed `['shop']`
- [M] `W:160057:2952792659` - "If he catches the first ferry, he will unload the material before lunch at the warehouse." -> blamed `['warehouse']`
- [M] `W:160059:3158723589` - "The optician who was recommended to us ground the new lenses in two days at the shop." -> blamed `['shop']`
- [M] `W:160064:3150362732` - "My aunt knits thick woolen socks for the kids every winter in her cottage." -> blamed `['cottage']`
- [M] `W:160065:77340970` - "The blacksmith will forge two new iron hinges for the gate by the end of the week." -> blamed `['iron']`
- [M] `W:160067:1064388204` - "Tomáš locked the workshop and turned off all the lights above the workbench before leaving." -> blamed `['leaving']`
- [M] `W:160068:2206489589` - "The carpenter didn't have exact measurements, but he nevertheless hung the shelf completely straight in the kitchen." -> blamed `['kitchen']`
- [M] `W:160071:4235946203` - "She stated in the email that she had rewritten the entire conclusion of the annual report twice already." -> blamed `['annual']`
- [M] `W:160072:2231180239` - "If she finds the original plan, she will assemble the whole tower correctly by tomorrow." -> blamed `['tomorrow']`
- [M] `W:160074:767667309` - "Someone must have changed the lock yesterday, because the old key no longer fit." -> blamed `['yesterday']`
- [M] `W:160077:1581836163` - "The archivist put the letters into new protective covers yesterday." -> blamed `['yesterday']`
- [M] `W:160078:4175667485` - "My mother used to sew us costumes for school shows every autumn." -> blamed `['autumn']`
- [M] `W:160080:3072555526` - "I wish he hadn't cut down that old walnut tree in the garden so soon." -> blamed `['garden']`
- [M] `W:160083:3115191267` - "Right now he is assembling the white tent frame on the roof of the extension alone." -> blamed `['alone']`
- [M] `W:160086:1753395699` - "By the end of the month they will have catalogued the entire parish archive twice." -> blamed `['twice']`
- [M] `W:160088:1803966261` - "Our uncle carves wooden whistles for the children every summer in the barn." -> blamed `['barn']`
- [M] `W:160093:1375639567` - "The librarian told me that he had already leafed through three thick catalogues at his desk today." -> blamed `['desk']`
- [S] `W:160011:104839409` - "If he had packed a spare inner tube, he would have change the burst tire right away." -> blamed `['change']`
- [S] `W:160015:2444777832` - "Despite the strong wind, Viktor brung the seedlings all the way to the upper terrace." -> blamed `['brung']`
- [S] `W:160074:2683293539` - "Someone must have change the lock, because the old key no longer fit." -> blamed `['change']`
- [S] `W:160093:1637774775` - "The librarian told me that he had already leafed through three thick catalogue today." -> blamed `['catalogue']`
- [S] `W:160100:171208197` - "Next season he will run the workshop and train two new apprentice." -> blamed `['apprentice']`
- [T] `W:160011:755801872` - "If he packs a spare inner tube, he will change the burst tire right away." -> blamed `['change']`
- [T] `W:160011:2802632660` - "If he packed a spare inner tube, he would change the burst tire right away." -> blamed `['change']`
- [T] `W:160050:250181732` - "The restorer explains to us that she removes three layers of varnish from the canvas." -> blamed `['removes']`
- [T] `W:160072:3344401763` - "If she found the original plan, she assembled the whole tower correctly." -> blamed `['assembled']`
- [T] `W:160074:2436279832` - "Someone must change the lock, because the old key no longer fits." -> blamed `['change']`
- [T] `W:160074:889570342` - "Someone will have to change the lock, because the old key no longer fits." -> blamed `['change']`
- [W] `W:160002:2583597915` - "A classmate wrote to me that he had read three chapters of the novel in a single evening." -> blamed `['novel']`
- [W] `W:160005:3472438787` - "He is gluing the broken plate on the kitchen counter right now." -> blamed `['plate']`
- [W] `W:160006:777519295` - "While the pan was heating up, Martin cut the pepper into thin slices." -> blamed `['pepper']`
- [W] `W:160014:2784220578` - "Today the bookbinder will sew eighteen old letters into one volume." -> blamed `['letters']`
- [W] `W:160015:3371435989` - "Despite the strong wind, Viktor brought the seedlings all the way to the lower terrace." -> blamed `['lower']`
- [W] `W:160018:120191724` - "If she hadn't broken her ankle last year, she would be playing the sonata from memory today." -> blamed `['ankle']`
- [W] `W:160030:3803648068` - "From that little tower, they watch the old wind power plant." -> blamed `['wind']`
- [W] `W:160033:1935520559` - "The bookseller explained to us that his brother had sold out the edition already last year." -> blamed `['brother']`
- [W] `W:160042:3107984404` - "The glazier will put the last piece of colored glass into the door only on Monday." -> blamed `['door']`
- [W] `W:160046:2590077163` - "She usually writes the notes by hand, but today she's dictating them into her tablet." -> blamed `['tablet']`
- [W] `W:160056:1764933359` - "He claims that he restocks the display case with new tools every week." -> blamed `['tools']`
- [W] `W:160059:934567951` - "The optician who was recommended to us ground the new frames in two days." -> blamed `['frames']`
- [W] `W:160060:3385822710` - "While the train stood in the station, the engineer topped up the oil in the tank." -> blamed `['oil']`
- [W] `W:160064:2901669164` - "My aunt knits thick woolen scarves for the kids every winter." -> blamed `['scarves']`
- [W] `W:160065:4029605372` - "The blacksmith will forge two new hinges for the door by the end of the week." -> blamed `['door']`
- [W] `W:160068:2796834291` - "The carpenter didn't have exact measurements, but he nevertheless hung the cabinet completely straight." -> blamed `['cabinet']`
- [W] `W:160071:4147820342` - "She stated in the email that she had rewritten the entire introduction of the report twice already." -> blamed `['introduction']`
- [W] `W:160072:2179265392` - "If she finds the original plan, she will assemble the whole bridge correctly." -> blamed `['bridge']`
- [W] `W:160074:207540240` - "Someone must have changed the padlock, because the old key no longer fit." -> blamed `['padlock']`
- [W] `W:160083:106751501` - "Right now he is assembling the white tent frame on the roof of the garage." -> blamed `['garage']`
- [W] `W:160093:117196401` - "The librarian told me that he had already leafed through three thick books today." -> blamed `['books']`
- [W] `W:160100:1627888490` - "Next season he will run the workshop and train two new employees." -> blamed `['employees']`

### C - every cost item (judged CORRECT, F6 rejected)

- `C:160005:3321050425` - "He's gluing the broken bowl on the kitchen counter at the moment." -> blamed `['moment']`
- `C:160010:1534777773` - "In the evenings, I water the small cacti on the windowsill." -> blamed `['evenings']`

### C - every catch (judged WRONG, F6 rejected)

- [M] `W:160016:4174469790` - "He is pouring a little more olive oil into the pan on the stove." -> blamed `['stove']`
- [M] `W:160033:2240312050` - "The bookseller explained to us that his partner had sold out the edition already last year in Bratislava." -> blamed `['bratislava']`
- [M] `W:160047:1026559451` - "Only rarely does he play the old tape for his guests in the evening." -> blamed `['evening']`
- [M] `W:160056:2484990955` - "He claims that he restocks the display case with new samples every week at the shop." -> blamed `['shop']`
- [M] `W:160057:2952792659` - "If he catches the first ferry, he will unload the material before lunch at the warehouse." -> blamed `['warehouse']`
- [M] `W:160058:1498558162` - "People don't work in this workshop after eight in the evening on weekdays." -> blamed `['weekdays']`
- [M] `W:160059:3158723589` - "The optician who was recommended to us ground the new lenses in two days at the shop." -> blamed `['shop']`
- [M] `W:160062:3478262337` - "If she had arrived at the venue an hour earlier, she would have won the auction." -> blamed `['venue']`
- [M] `W:160066:3317709807` - "You will have to return the borrowed tools to the shop this week." -> blamed `['shop']`
- [M] `W:160067:1064388204` - "Tomáš locked the workshop and turned off all the lights above the workbench before leaving." -> blamed `['leaving']`
- [M] `W:160068:2206489589` - "The carpenter didn't have exact measurements, but he nevertheless hung the shelf completely straight in the kitchen." -> blamed `['kitchen']`
- [M] `W:160072:2231180239` - "If she finds the original plan, she will assemble the whole tower correctly by tomorrow." -> blamed `['tomorrow']`
- [M] `W:160080:3072555526` - "I wish he hadn't cut down that old walnut tree in the garden so soon." -> blamed `['garden']`
- [M] `W:160082:1337566022` - "She is just putting the glasses into the wooden crate in the cellar." -> blamed `['cellar']`
- [M] `W:160088:1803966261` - "Our uncle carves wooden whistles for the children every summer in the barn." -> blamed `['barn']`
- [M] `W:160090:2166122707` - "We sort paper and glass into two large bins in the garage." -> blamed `['garage']`
- [M] `W:160094:603959753` - "This evening I'll lock the back gate and turn off the lamp in the hallway." -> blamed `['hallway']`
- [S] `W:160035:1850597999` - "Look! She's nailing the last slat on the birdhouses." -> blamed `['birdhouses']`
- [T] `W:160074:889570342` - "Someone will have to change the lock, because the old key no longer fits." -> blamed `['change']`
- [W] `W:160002:2583597915` - "A classmate wrote to me that he had read three chapters of the novel in a single evening." -> blamed `['novel']`
- [W] `W:160009:792463771` - "The boatman told us that he had pulled up the rope before the storm." -> blamed `['rope']`
- [W] `W:160010:2579519228` - "In the evening, I water the small cacti on the balcony." -> blamed `['balcony']`
- [W] `W:160041:652690445` - "You wear the leather backpack more often than the lighter one from the drawer." -> blamed `['drawer']`
- [W] `W:160042:3107984404` - "The glazier will put the last piece of colored glass into the door only on Monday." -> blamed `['door']`
- [W] `W:160057:97017393` - "If he catches the first ferry, he will unload the material before dinner." -> blamed `['dinner']`
- [W] `W:160060:3385822710` - "While the train stood in the station, the engineer topped up the oil in the tank." -> blamed `['oil']`
- [W] `W:160065:4029605372` - "The blacksmith will forge two new hinges for the door by the end of the week." -> blamed `['door']`
- [W] `W:160067:337966924` - "Tomáš locked the workshop and turned off all the lights above the shelf." -> blamed `['shelf']`
- [W] `W:160069:380454155` - "I will return the two books about the sea to you on Tuesday." -> blamed `['sea']`
- [W] `W:160070:1321132523` - "There is a small glass elevator at the end of the kitchen." -> blamed `['kitchen']`
- [W] `W:160083:106751501` - "Right now he is assembling the white tent frame on the roof of the garage." -> blamed `['garage']`
- [W] `W:160091:2754700349` - "You will be drying those winter jackets near the fireplace all evening." -> blamed `['fireplace']`
- [W] `W:160096:3765672169` - "If we get a longer ladder, we'll fix the antenna on the wall ourselves." -> blamed `['wall']`

## Selection (pre-declared rule)

Rule declared before the run: take the variant with the lowest MEASURED COST, ties broken by more catches;
F6 counts as SELECTED for the stack only if that cost is <= 1.0 %% of the judged-correct answers.

- selected variant: **C** (cost 0.47 %)
- <= 1.0 % rule met: **YES** -> F6 is SELECTED for the stack

## (c) B3 - F5 on the same items, on its OWN lines

F5 and F6 figures are never added together.

- F5 source: `phase1i/checker_1i.py::f5_adjunct_deletion`, signature `(it)`
- **F5 cost**: 0/426 judged-correct answers rejected (0.00 %)
- **F5 catches**: 0/474 judged-wrong answers rejected (by type: -)
- **overlap** (items both F5 and F6[C] reject): 0

### F5 cost items

none.

### F5 catches

none.

## Files

- `phase1q/f6.py` - the guard (VARIANT set to the selected one)
- `phase1q/f6_gold_1n.json` - hand gold, 100 x 2 answers
- `phase1q/f6_eval_1n.py` - re-runnable, `--data-dir` points it at another set
- `phase1q/f6_eval_1n.json` - the raw numbers behind this file
