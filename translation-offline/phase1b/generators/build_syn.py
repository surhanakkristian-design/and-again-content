#!/usr/bin/env python3
"""Builds phase1b/synonyms/table.json from scratchpad/syn_ctx.txt (+ PATCH below).
Line: id | pos | members | ok with {a/b} | bad with {a/b} [| head=N] [| irr=lemma:f;f]
Lines with a '-- ' placeholder in members/ok/bad (drafts) are skipped; trailing ' -- note' is stripped."""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1b/synonyms/table.json')

SAFE = """
someone | x | someone, somebody
anyone | x | anyone, anybody
everyone | x | everyone, everybody
no_one | x | no one, nobody
toward | x | toward, towards
among | x | among, amongst
okay | x | okay, ok
colour | v | colour, color
grey | a | grey, gray
favourite | n | favourite, favorite
neighbour | n | neighbour, neighbor
neighbourhood | n | neighbourhood, neighborhood
centre | v | centre, center
theatre | n | theatre, theater
litre | n | litre, liter
realise | v | realise, realize
recognise | v | recognise, recognize
organise | v | organise, organize
apologise | v | apologise, apologize
analyse | v | analyse, analyze
jewellery | x | jewellery, jewelry
jeweller | n | jeweller, jeweler
pyjamas | x | pyjamas, pajamas
mum_mom | n | mum, mom
cosy | a | cosy, cozy
traveller | n | traveller, traveler
flavour | v | flavour, flavor
humour | v | humour, humor
behaviour | n | behaviour, behavior
honour | v | honour, honor
"""

# id -> None (delete) or (ok, bad) replacement
PATCH = {
    'stand_is_standing': None, 'have_got': None, 'eyelash_length': None, 'this_time_tomorrow': None,
    'waste_miss_penalty': None, 'incredibly_unbelievably': None, 'further_farther': None, 'bigger_larger': None,
    'fill_fill_up': None, 'get_up_wake': None, 'grow_increase': None, 'boots_wellies': None, 'big_huge': None,
    'mum_mother': None, 'arrive_get_to': None,
    'noticeboard': ('The evidence is on the {noticeboard/pinboard}.', 'Sam posted the ad on an online {bulletin board/cork board}.'),
    'burst_laughing': ('The hall {burst out laughing/burst into laughter}.', 'Alone in her room, she {burst out laughing/erupted in laughter}.'),
    'reach_get_to': ('We {reached/got to} the summit at noon.', 'She {reached/got to} for the salt.'),
    'friend_buddy': ('She is my best {friend/buddy}.', 'I got a {friend/buddy} request on Facebook.'),
    'fall_apart': ('The old chair {fell apart/collapsed}.', 'The runner {collapsed/fell apart} at the finish line.'),
    'jump_leap': ('The dolphins {jump/leap} out of the water.', 'The car won\'t start, can you {jump/leap} it?'),
    'barely_hardly': ('She {barely/hardly} lifted her eyes.', 'It\'s {hardly/barely} surprising that he left.'),
    'quick_fast': ('She is a {quick/fast} runner.', 'Is your watch {fast/quick}? It says ten past.'),
    'brought_down': ('He {knocked down/brought down} the striker.', 'The scandal {brought down/knocked down} the government.'),
    'try_taste': ('Can I {try/taste} the salsa?', '{Try/Taste} this jacket on.'),
    'destroy_ruin': ('The rain {ruined/destroyed} the fruit.', 'The army {destroyed/ruined} the bridge with bombs.'),
    'tear_rip': ('She {tore/ripped} the letter in half.', 'That shop {rips/tears} tourists off.'),
    'allow_permit': ('Dogs are not {allowed/permitted} inside.', 'Did you get your fishing {permit/allow}?'),
    'meet_encounter': ('I {ran into/bumped into} Tom yesterday.', 'The river {runs into/bumps into} the sea.'),
    'travel_go': ('We {travelled/went} to Spain.', 'How is it {going/travelling}?'),
    'arrange_organise': ('She {arranged/organised} the party.', 'She {arranged/organised} the song for piano.'),
    'fetch_go_get': ('{Fetch/Go and get} your coat.', 'The dog loves playing {fetch/go and get}.'),
    'include_contain': ('The price {includes/contains} breakfast.', 'Try to {contain/include} your anger.'),
    'test_examine': ('The doctor {examined/tested} the patient.', 'Her patience was {tested/examined} by the kids.'),
    'pour_tip': ('She {poured/tipped} the water into the sink.', 'She {tipped/poured} the waiter generously.'),
    'shine_sparkle': ('The stars {twinkled/sparkled}.', 'The sun {shone/twinkled} all day.'),
    'crawl_creep': ('The baby {crawled/crept} across the floor.', 'He is such a {creep/crawl}!'),
    'persuade_convince': ('She {persuaded/convinced} him to come.', 'She is a {convinced/persuaded} vegan.'),
    'order_ask_for': ('She {ordered/asked for} a coffee.', 'She {ordered/asked for} her books by size.'),
    'look_after_take_care': ('She {looks after/takes care of} her little brother.', 'Bye, {take care/look after}!'),
    'repair_sort_out': ('I\'ll {sort out/deal with} the tickets.', '{Sort out/Deal with} your socks by colour.'),
    'mistake_error': ('There\'s a {mistake/error} in the bill.', 'I took your coat by {mistake/error}.'),
    'sea_ocean': ('Dolphins jump out of the {sea/ocean}.', 'I\'m all at {sea/ocean} with this maths.'),
    'fire_flame': ('The house went up in {flames/fire}.', 'The soldiers opened {fire/flames}.'),
    'show_programme': ('My favourite TV {show/programme} is on.', '{Show/Programme} me the photos.'),
    'finally_at_last': ('{At last/Finally}, the bus came.', '{Finally/At last}, I\'d like to thank my parents.'),
    'kind_of_sort_of': ('I\'m {kind of/sort of} tired.', 'What {kind of/a bit} music do you like?'),
    'happy_glad_pleased': ('I\'m {glad/happy} you came.', '{Happy/Glad} birthday!'),
    'wet_damp_soaked': ('Her hair was {wet/soaked}.', '{Wet/Soaked} paint!'),
    'bored_fed_up': ('I\'m {bored/fed up} with this job.', 'I was {bored/fed up} stiff.'),
    'surprised_amazed_shocked': ('She was {amazed/astonished} by the view.', 'I\'m {surprised/amazed} at you, how rude!'),
    'ready_prepared': ('Dinner is {ready/prepared}.', 'Get {ready/prepared}, set, go!'),
    'empty_vacant': ('Is this seat {empty/vacant}?', 'The bottle is {empty/vacant}.'),
    'rarely_seldom': ('She {rarely/seldom} eats meat.', '{Rarely/Hardly ever} have I seen such a mess.'),
    'often_frequently': ('She {often/frequently} works late.', 'Every so {often/frequently} she calls.'),
    'sometimes_occasionally': ('She {sometimes/occasionally} cooks.', '{Sometimes/Occasionally} I love you, sometimes I hate you.'),
    'chef_cook': ('The {chef/cook} made pasta.', '{Cook/Chef} the rice for ten minutes.'),
    'prize_award': ('She won a {prize/award}.', 'They {awarded/prized} him a medal.'),
    'thin_slim_skinny': ('She is very {thin/slim}.', 'a {thin/skinny} soup'),
    'terrible_horrible_dreadful': ('The weather was {terrible/horrible}.', 'Ivan the {Terrible/Horrible}'),
    'over_more_than': ('{Over/More than} a hundred people came.', 'I\'d be {more than/over} happy to help.'),
    'these_days_nowadays': ('{Nowadays/These days} everyone has a phone.', 'One of {these days/nowadays} I\'ll quit.'),
    'all_day_the_whole_day': ('She stayed in bed {all day/the whole day}.', '{All day/The whole day} breakfast served here.'),
    'all_winter': ('The pond was frozen {all winter/the whole winter}.', 'She packed away {all winter/throughout the winter} clothes.'),
    'all_afternoon': ('It rained {all afternoon/the whole afternoon}.', '{All afternoon/The whole afternoon} classes are cancelled this week.'),
    'on_repeat': ('She played the song {on repeat/over and over}.', 'The doctor put the prescription {on repeat/over and over}.'),
    'at_full_power': ('The fan was {on full/on full power}.', 'The TV was {at full blast/at full speed}.'),
    'maybe_perhaps': ('{Maybe/Perhaps} she is ill.', '"{Maybe/Perhaps}" is not an answer.'),
    'put_up_with_tolerate': ('I can\'t {stand/bear} him.', 'Please {stand/bear} in the queue.'),
    'run_out_of': ('We {ran out of/used up} milk.', 'She {ran out of/used up} the room crying.'),
    'fill_in_complete': ('{Fill in/Fill out} the form.', 'Can you {fill in/fill out} for me tomorrow?'),
    'throw_away_out': ('{Throw away/Throw out} the old food.', 'The judge {threw out/threw away} the case.'),
    'slip_slide': ('She {slipped/slid} on the ice.', 'Sorry, it {slipped/slid} my mind.'),
    'rub_massage': ('She {rubbed/massaged} his shoulders.', 'Don\'t {rub/massage} it in!'),
    'cool_chill': ('Leave the cake to {cool/chill}.', 'We {chilled/cooled} at home all weekend.'),
    'blink_wink': ('She {winked/blinked} at him.', 'It was over in the {blink/wink} of an eye.'),
    'wander_roam': ('They {wandered/roamed} around the old town.', 'The {roaming/wandering} charges were huge.'),
    'climb_go_up': ('She {climbed/went up} the stairs.', 'The lights {went up/climbed} as the play ended.'),
    'wipe_clean_dust': ('She {wiped/cleaned} the table.', 'She {dusted/wiped} the cake with sugar.'),
    'fridge_refrigerator': ('Put the milk in the {fridge/refrigerator}.', 'He is built like a {fridge/refrigerator}.'),
    'cash_machine_atm': ('I took money from the {cash machine/ATM}.', 'The pressure is one {atm/cash machine}.'),
    'noon_midday': ('We meet at {noon/midday}.', 'The sun is at its highest at {noon/lunchtime}.'),
    'beach_shore_coast': ('We walked along the {shore/beach}.', 'The {coast/beach} is clear, let\'s go.'),
    'huge_gigantic': ('Her lashes look {huge/gigantic}.', 'Thanks, that\'s a {huge/giant} help.'),
    'nice_lovely': ('What a {lovely/nice} day!', 'Nice one! vs {Nice/Lovely} one!'),
}
PATCH['nice_lovely'] = ('What a {lovely/nice} day!', '"Did you pass?" "Yes!" "{Nice/Lovely} one!"')

EXTRA = r"""
look_at_watch | v | look at, watch | We {watched/looked at} the birds for an hour. | Let me {look at/watch} your homework.
lend_loan | v | lend, loan | Can you {lend/loan} me ten euros? | Can you {lend/loan} me a hand?
suggest_recommend | v | suggest, recommend | She {suggested/recommended} the fish. | Are you {suggesting/recommending} I'm lying?
warn_alert | v | warn, alert | They {warned/alerted} us about the storm. | I {warned/alerted} you not to touch it!
comfort_console | v | comfort, console | She {comforted/consoled} her friend. | Dress for {comfort/console}.
calm_down_relax | v | calm down, relax | {Calm down/Relax}, it's fine. | {Relax/Calm down} the rules a bit.
escape_run_away | v | escape, run away, get away | The prisoner {escaped/ran away}. | Gas was {escaping/running away} from the pipe.
flee_run_away | v | flee, run away | They {fled/ran away} from the fire. | The kids {ran away/fled} with the prize.
swallow_gulp | v | swallow, gulp, gulp down | She {swallowed/gulped} the pill. | That story is hard to {swallow/gulp}.
sip_drink | v | sip, drink | She {sipped/drank} her tea. | He {drinks/sips} too much, he's an alcoholic.
plant_sow | v | plant, sow | She {sowed/planted} carrot seeds. | She {planted/sowed} a kiss on his cheek.
bake_roast | v | bake, roast | She {roasted/baked} the potatoes. | They {roasted/baked} him at his birthday party.
dirty_filthy | a | dirty, filthy | His shoes were {dirty/filthy}. | They're {filthy/dirty} rich.
tasty_delicious | a | tasty, delicious, yummy | The soup was {delicious/tasty}. | She's a {tasty/delicious} player (skilful).
cold_freezing | a | cold, freezing | It's {freezing/cold} outside. | She caught a {cold/freezing}.
brave_courageous | a | brave, courageous | a {brave/courageous} firefighter | {Brave/Courageous} the storm.
famous_well_known | a | famous, well-known | a {famous/well-known} singer | We had a {famous/well-known} time!
stupid_silly_dumb | a | stupid, silly, dumb | That was a {silly/stupid} idea. | She was struck {dumb/stupid} with shock.
same_identical | x | same, identical | They wore the {same/identical} dress. | {Same/Identical} here!
abroad_overseas | x | abroad, overseas | She studied {abroad/overseas}. | There's a rumour {abroad/overseas} that he quit.
everywhere_all_over | x | everywhere, all over the place | Toys lay {everywhere/all over the place}. | His essay is {all over the place/everywhere} (badly organised).
quickly_rapidly | x | quickly, rapidly, swiftly | Prices rose {rapidly/quickly}. | Can I {quickly/rapidly} ask you something?
totally_absolutely | x | totally, absolutely | You're {absolutely/totally} right! | "Can I borrow it?" "{Absolutely/Totally} not!"
at_first_initially | x | at first, initially | {At first/Initially} I didn't like it. | It was love at {first/initially} sight.
each_other_one_another | x | each other, one another | They love {each other/one another}. | --
sweets_candy | n | sweets, candy | The kids ate too many {sweets/candy}. | Arm {candy/sweets} (a pretty partner)
thief_robber | n | thief, robber, burglar | A {thief/robber} took her bag. | Time is a {thief/robber}.
adult_grown_up | n | adult, grown-up | Ask a {grown-up/adult} for help. | This film is for {adults/grown-ups} only (explicit).
tourist_visitor | n | tourist, visitor | The city is full of {tourists/visitors}. | The {visitors/tourists} won 2-0.
combination_combo | n | combination, combo | She threw a fast {combination/combo}. | What's the {combination/combo} of the safe?
bank_card | n | bank card, card | Insert your {bank card/card}. | She sent me a birthday {card/bank card}.
hill_slope | n | hill, slope | The kids sledged down the {hill/slope}. | Lower the {slope/hill} of the line on the graph.
river_stream | n | river, stream | A small {stream/river} ran through the farm. | Can I {stream/river} this film online?
rock_stone_pebble | n | pebble, stone | She skimmed a flat {pebble/stone}. | He lost two {stone/pebble} this year.
snow_frost | n | frost, ice | There was {frost/ice} on the windscreen. | Put some {ice/frost} in my drink.
glass_tumbler | n | glass, tumbler | a {glass/tumbler} of water | The {tumbler/glass} did five backflips.
curtain_blind | n | curtain, blind | Close the {curtains/blinds}. | He is {blind/curtain} in one eye.
blanket_duvet | n | duvet, quilt | She pulled the {duvet/quilt} over her head. | Her grandma made a patchwork {quilt/duvet}.
shelf_rack | n | shelf, rack | Put the plates on the {rack/shelf}. | He was on the {rack/shelf} (tortured).
door_gate | n | door, gate | She opened the garden {gate/door}. | Answer the {door/gate}, someone knocked.
wall_fence | n | fence, hedge | A tall {fence/hedge} separated the gardens. | He sold the stolen goods to a {fence/hedge}.
clothes_clothing | n | clothes, clothing | She bought new {clothes/clothing}. | She needs a {clothes/clothing} peg.
hat_cap | n | hat, cap | She wore a baseball {cap/hat}. | Put the {cap/hat} back on the pen.
wallet_purse | n | wallet, purse | She lost her {wallet/purse}. | Her {purse/wallet} was a million for the fight.
doctor_gp | n | doctor, GP | She went to see her {doctor/GP}. | She's a {doctor/GP} of philosophy.
hospital_clinic | n | hospital, clinic | She went to a skin {clinic/hospital}. | The coach gave a passing {clinic/hospital} (masterclass).
danger_risk | n | danger, risk | There's a {risk/danger} of flooding. | Don't {risk/danger} it.
reason_cause | n | reason, cause | What was the {cause/reason} of the fire? | They fought for a good {cause/reason}.
result_outcome | n | result, outcome | We're waiting for the {outcome/result}. | The football {results/outcomes} are on at five.
bottom_base | n | bottom, base | at the {base/bottom} of the mountain | Army {base/bottom} in the desert.
corner_angle | n | corner, angle | --
amount_quantity | n | amount, quantity | a large {amount/quantity} of sugar | Quality over {quantity/amount}.
number_figure | n | number, figure | Sales {figures/numbers} are up. | She has a great {figure/number}.
size_measurement | n | size, measurements | The tailor took her {measurements/size}. | What shoe {size/measurements} are you?
shape_form | n | shape, form | a cake in the {shape/form} of a heart | Fill in this {form/shape}.
thing_object_item | n | thing, object, item | Each {item/object} has a price tag. | The {object/item} of the game is to win.
card_postcard | n | card, postcard | Send us a {postcard/card} from Rome. | She paid by {card/postcard}.
computer_laptop | n | computer, laptop, PC | She works on her {laptop/computer}. | Put the {laptop/computer} on your knees.
screen_display | n | screen, display | The phone has a big {screen/display}. | They {screen/display} all passengers at the airport.
price_cost | n | price, cost | The {price/cost} of bread rose. | Win at any {cost/price}.
shopping_groceries | n | shopping, groceries | She carried the {shopping/groceries} home. | We went {shopping/groceries} yesterday.
lunch_meal | n | meal, dinner | We had a nice {meal/dinner} out. | {Dinner/Meal} is at eight, don't be late.
jam_jelly | n | jam, jelly | toast with strawberry {jam/jelly} | We were stuck in a traffic {jam/jelly}.
oven_cooker | n | oven, cooker | Put the cake in the {oven/cooker}. | The {cooker/oven} top is dirty.
drawer_box | n | drawer, box | --
window_pane | n | --
body_figure | n | --
face_expression | n | face, expression | Did you see his {face/expression}? | She {faced/expressed} the problem.
arm_hand | n | hand, arm | --
leg_foot | n | --
bottom_bum | n | bottom, bum, backside | She fell on her {bottom/bum}. | The {bottom/bum} of the sea.
animal_creature | n | animal, creature | A strange {creature/animal} lived in the lake. | We are {creatures/animals} of habit.
dog_puppy | n | dog, puppy | --
bird_chick | n | --
homework_assignment | n | homework, assignment | She finished her {homework/assignment}. | He is on a secret {assignment/homework}.
school_college | n | --
sport_game | n | --
fun_enjoyment | n | fun, enjoyment | --
hobby_pastime | n | hobby, pastime | Her favourite {hobby/pastime} is knitting. | --
party_celebration | n | party, celebration | a birthday {party/celebration} | The Labour {Party/celebration} won.
fight_battle | n | fight, battle | a {battle/fight} against cancer | a pillow {fight/battle}
war_conflict | n | war, conflict | --
rule_law | n | rule, law | It's against the {rules/law} to run. | She studies {law/rules} at Oxford.
crowd_group | n | crowd, group | A {crowd/group} gathered outside. | She sings in a pop {group/crowd}.
group_team | n | --
people_folk | n | people, folk | Country {folk/people} are friendly. | She loves {folk/people} music.
family_relatives | n | family, relatives | All her {relatives/family} came. | They want to start a {family/relatives}.
grandma_granny | n | grandma, granny, grandmother, nan | Her {grandma/granny} bakes cakes. | --
grandpa_granddad | n | grandpa, granddad, grandfather | Her {grandpa/granddad} fishes. | a {grandfather/grandpa} clock
aunt_auntie | n | aunt, auntie | Her {aunt/auntie} lives in Rome. | --
teenager_teen | n | teenager, teen | Her son is a {teenager/teen}. | She's in her late {teens/teenagers}.
stranger_foreigner | n | stranger, foreigner | --
driver_chauffeur | n | --
pilot_captain | n | pilot, captain | The {captain/pilot} spoke to the passengers. | The team {captain/pilot} lifted the cup.
shop_assistant | n | shop assistant, sales assistant | The {shop assistant/sales assistant} helped me. | --
waiter_server | n | waiter, server | The {waiter/server} brought the menu. | The {server/waiter} is down, the website crashed.
teacher_tutor | n | teacher, tutor | Her maths {tutor/teacher} is patient. | --
girl_young_woman | n | --
husband_partner | n | --
cold_flu | n | --
illness_disease | n | illness, disease, sickness | a serious {illness/disease} | She gets travel {sickness/disease}.
peace_calm | n | --
music_song | n | --
voice_sound | n | --
news_information | n | --
story_tale | n | story, tale | a fairy {tale/story} | The building has five {storeys/tales}.
fact_detail | n | --
plan_scheme | n | plan, scheme | a {plan/scheme} to save money | The colour {scheme/plan} of the room is blue.
wooden_board | n | --
weather_climate | n | --
rain_shower | n | shower, rain | --
storm_thunderstorm | n | storm, thunderstorm | A {storm/thunderstorm} hit the city. | She took the city by {storm/thunderstorm}.
smoke_steam | n | smoke, steam | --
ice_frost | n | --
sky_heavens | n | --
coast_seaside | n | --
town_city | n | town, city | --
car_vehicle | n | car, vehicle | Park your {car/vehicle} here. | The party is a {vehicle/car} for his ambitions.
ticket_fare | n | --
journey_travel | n | --
path_track | n | --
floor_storey | n | --
tiny_minute | x | tiny, minuscule | --
high_high_up | a | --
long_lengthy | a | --
narrow_thin | a | --
fat_overweight | a | --
heavy_weighty | a | --
slow_gradual | a | --
new_brand_new | a | --
young_little | a | --
good_nice_fine | a | --
wonderful_marvellous | a | --
excellent_perfect | a | excellent, perfect | --
handsome_good_looking | a | handsome, good-looking, attractive | a {handsome/good-looking} man | a {handsome/good-looking} sum of money
ugly_unattractive | a | --
happy_cheerful | a | --
cross_annoyed | a | --
excited_thrilled | x | excited, thrilled | She was {excited/thrilled} about the trip. | Don't get {excited/thrilled}, it's only a test drive.
free_gratis | x | free, for free, free of charge | Kids get in {free/for free}. | Feel {free/for free} to ask.
cheap_inexpensive | a | cheap, inexpensive | a {cheap/inexpensive} hotel | That was a {cheap/inexpensive} trick.
expensive_dear_pricey | a | expensive, pricey, dear | a {pricey/expensive} restaurant | She's a {dear/pricey} friend.
poor_broke | a | poor, broke | I'm {broke/poor} until payday. | {Poor/Broke} you, you look ill.
tough_strong | a | --
weak_feeble | a | weak, feeble | a {feeble/weak} old man | {Weak/Feeble} coffee.
important_significant | a | important, significant | an {important/significant} change | She's the most {important/significant} person to me.
main_major_chief | a | main, chief, principal | The {main/chief} reason is cost. | Her {main/chief} course was fish.
interesting_fascinating | a | --
popular_well_liked | a | --
correct_accurate | a | --
true_correct | a | --
fake_false | a | fake, false | {Fake/False} eyelashes. | True or {false/fake}?
different_other | a | --
similar_alike | a | --
possible_likely | a | --
clean_spotless | a | --
dry_arid | a | --
hot_warm | a | --
fresh_new | a | --
raw_uncooked | a | raw, uncooked | {raw/uncooked} rice | Her hands were {raw/uncooked} from the cold.
hard_firm | a | hard, firm | a {firm/hard} mattress | She's a {hard/firm} worker.
smooth_even | a | smooth, even | a {smooth/even} surface | Now we're {even/smooth}.
rough_bumpy | a | rough, bumpy | a {bumpy/rough} road | I had a {rough/bumpy} idea of the price.
sharp_pointed | a | --
dangerous_risky | a | dangerous, risky | It's {dangerous/risky} to swim here. | Watch out, that dog is {dangerous/risky}.
well_fine | a | --
alright_ok | x | all right, alright | Is everything {all right/alright}? | --
dead_lifeless | a | --
alive_living | a | --
early_premature | a | --
far_distant | a | far, distant | a {distant/far} country | How {far/distant} is it?
whole_complete_total | a | --
main_central | a | --
special_particular | a | --
common_frequent | a | --
modern_up_to_date | a | --
gentle_kind | a | --
polite_well_mannered | a | --
shy_timid | a | shy, timid | a {shy/timid} child | He's two years {shy/timid} of fifty.
lazy_idle | a | lazy, idle | a {lazy/idle} student | The machines stood {idle/lazy} all week.
honest_truthful | a | honest, truthful | an {honest/truthful} answer | To be {honest/truthful}, I hate it.
generous_kind | a | --
proud_pleased | a | --
sorry_apologetic | a | --
lonely_alone | a | --
favourite_best | a | --
cosy_comfy | a | --
usually_generally | x | usually, generally | --
almost_practically | x | --
together_with_each_other | x | --
somewhere_someplace | x | --
upstairs_up | x | --
home_at_home | x | --
here_over_here | x | --
far_away | x | far away, a long way away | She lives {far away/a long way away}. | --
approximately_roughly | x | approximately, roughly | It costs {approximately/roughly} ten euros. | He treated her {roughly/approximately}.
under_less_than | x | under, less than | It costs {under/less than} ten euros. | The cat is {under/less than} the table.
behind_at_the_back_of | x | behind, at the back of | She sat {at the back of/behind} the class. | The police are {behind/at the back of} you all the way (support).
opposite_across_from | x | opposite, across from | The bank is {opposite/across from} the church. | Hot is the {opposite/across from} of cold.
between_among | x | --
around_round | x | --
towards_to | x | --
off_from | x | --
during_in | x | --
for_during | x | --
until_till | x | until, till | Wait {until/till} I come back. | She works on the {till/until} at the supermarket.
because_as | x | --
because_of_due_to | x | because of, due to | The match was cancelled {because of/due to} rain. | The rent is {due to/because of} be paid on Monday.
however_but | x | --
but_yet | x | --
so_therefore | x | --
about_regarding | x | about, regarding | a letter {about/regarding} your account | It's {about/regarding} time you left.
with_using | x | --
without_with_no | x | --
besides_as_well_as | x | as well as, besides | She speaks French {as well as/besides} German. | She speaks French {as well as/besides} he does.
instead_of_rather_than | x | --
according_to | x | --
next_following | x | next, following | the {next/following} day | Who's {next/following}?
first_initial | x | --
top_best | x | --
own_personal | x | --
today_this_day | x | --
at_the_end_finally | x | --
in_time_on_time | x | --
by_ten | x | by ten, by ten o'clock | --
a_day_trip | x | --
for_a_while | x | --
of_course_certainly | x | --
no_problem | x | no problem, no worries | "Thanks!" "{No problem/No worries}." | We had {no problem/no worries} finding it.
wow_amazing | x | --
a_lot_much | x | --
plenty_enough | x | --
some_a_few | x | --
look_forward_can_t_wait | v | --
figure_out | v | --
set_up_arrange | v | --
find_look_up | v | --
go_back_return | v | --
carry_on_continue | v | --
hang_out_spend_time | v | hang out, spend time | We {hang out/spend time} at the park. | Let the washing {hang out/spend time} to dry.
chill_relax | v | --
turn_up_increase_volume | v | --
get_rid_of_remove | v | get rid of, remove | {Get rid of/Remove} the old files. | We need to {remove/get rid of} the guests' shoes at the door.
cut_down_reduce | v | cut down on, reduce | {Cut down on/Reduce} sugar. | The doctor {reduced/cut down on} his dislocated shoulder.
break_in_burgle | v | break into, burgle | Someone {broke into/burgled} the flat. | She {broke into/burgled} a smile.
calm_down | v | --
work_out_exercise | v | --
take_part_participate | v | take part in, participate in | She {took part in/participated in} the race. | --
take_time_last | v | --
spend_pass | v | --
stamp_stamp | v | --
pin_attach | v | --
hang_dangle | v | hang, dangle | Her legs {dangled/hung} over the edge. | {Hang/Dangle} your coat up.
splash_spray | v | splash, spray | The kids {splashed/sprayed} each other with water. | He {sprayed/splashed} graffiti on the wall.
spread_smear | v | spread, smear | She {spread/smeared} butter on the toast. | The news {spread/smeared} fast.
peel_skin | v | peel, skin | {Peel/Skin} the tomatoes. | {Peel/Skin} the orange and eat it.
grate_shred | v | grate, shred | {Grate/Shred} the cabbage. | {Shred/Grate} the documents.
fry_saute | v | --
heat_warm | v | --
stare_look | v | --
yawn_stretch | v | --
sneeze_cough | v | --
limp_hobble | v | limp, hobble | She {limped/hobbled} off the pitch. | He has a {limp/hobble} handshake.
drag_haul | v | drag, haul | They {hauled/dragged} the boat onto the beach. | The film was a {drag/haul} (boring).
lift_pick_up | v | --
hang_up_end_call | v | --
shut_up_be_quiet | v | shut up, be quiet | {Be quiet/Shut up}, the baby's asleep. | They {shut up/were quiet} the shop at six.
tidy_clear_up | v | tidy up, clear up | {Tidy up/Clear up} your room. | The weather should {clear up/tidy up} later.
decorate_do_up | v | decorate, do up | They {decorated/did up} the old house. | {Do up/Decorate} your coat, it's cold.
paint_decorate | v | --
water_irrigate | v | --
dig_shovel | v | --
chew_bite | v | chew, bite | She {chewed/bit} her nails. | Does your dog {bite/chew}?
lick_taste | v | --
feed_give_food | v | --
tickle_scratch | v | --
scratch_itch | v | scratch, itch | --
shave_trim | v | --
wash_shower | v | --
bathe_bath | v | --
mumble_mutter | v | mumble, mutter | He {mumbled/muttered} something. | --
kiss_peck | v | --
text_message | v | --
write_note_down | v | --
print_type | v | --
photograph_take_photo | v | --
add_include | v | --
explain_describe | v | --
receive_accept | v | --
agree_approve | v | --
want_wish | v | --
prefer_rather | v | --
hope_expect | v | --
kill_murder | v | --
bring_take | v | --
say_tell | v | --
cover_hide | v | --
spill_drop | v | --
freeze_ice | v | --
sail_cruise | v | --
nod_agree | v | --
dance_move | v | --
point_show | v | --
imagine_picture | v | --
dream_imagine | v | --
bring_back_return | v | --
borrow_use | v | --
consist_be_made_of | v | --
belong_own | v | --
get_become_tired | v | --
light_set_fire | v | --
wait_await | v | --
lose_miss | v | --
attack_assault | v | --
touch_feel | v | --
knock_bang | v | knock, bang | She {knocked/banged} on the door. | Two {knocks/bangs} on the head.
pay_spend | v | --
cost_be | v | --
sell_market | v | --
live_reside | v | --
exist_be | v | --
kill_time | v | --
stay_live | v | --
repair_restore | v | --
erupt_break_out | v | --
shake_hands | v | --
rob_burgle | v | --
lie_fib | v | --
force_make | v | --
manage_succeed | v | --
fail_miss | v | --
swim_bathe | v | --
climb_scramble | v | --
shop_go_shopping | v | --
serve_bring | v | --
put_up_raise | v | --
exchange_trade | v | --
separate_part | v | --
compare_contrast | v | --
measure_weigh | v | --
dress_up | v | --
lose_weight | v | --
unpack_empty | v | --
load_fill | v | --
fly_travel | v | --
fly_travel_by_air | v | --
feed_nourish | v | --
mention_say | v | --
advise_recommend | v | --
deny_refuse | v | --
thank_appreciate | v | --
celebrate_party | v | --
avoid_escape | v | --
kick_off_start | v | --
"""
# EXTRA overrides same-id drafts of CTX (and adds new ones)

def expand(s, sep):
    m = re.search(r'\{([^{}/]+)/([^{}/]+)\}', s)
    if not m:
        raise ValueError('no {a/b} slot in: ' + s)
    a = s[:m.start()] + m.group(1) + s[m.end():]
    b = s[:m.start()] + m.group(2) + s[m.end():]
    cap = lambda x: x[0].upper() + x[1:] if x[0].isalpha() else x
    return f'{cap(a)} {sep} {cap(b)}'

def parse(text):
    rows = {}
    order = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.strip() for p in line.split('|')]
        gid = parts[0]
        if gid not in rows:
            order.append(gid)
        rows[gid] = parts
    return rows, order

ctx_rows, order = parse(open(os.path.join(HERE, 'syn_ctx.txt')).read())
extra_rows, extra_order = parse(EXTRA)
for gid in extra_order:
    if gid not in ctx_rows:
        order.append(gid)
    ctx_rows[gid] = extra_rows[gid]

groups, ids, errs, skipped = [], set(), [], []
for line in SAFE.strip().splitlines():
    gid, pos, mem = [p.strip() for p in line.split('|')]
    groups.append({'id': gid, 'kind': 'safe', 'pos': pos, 'm': [x.strip() for x in mem.split(',')]})
    ids.add(gid)

for gid in order:
    if gid in PATCH and PATCH[gid] is None:
        skipped.append(gid); continue
    parts = ctx_rows[gid]
    if len(parts) < 5:
        skipped.append(gid); continue
    _, pos, mem, ok, bad = parts[:5]
    if gid in PATCH:
        ok, bad = PATCH[gid]
    ok = re.sub(r'\s+--(\s.*)?$', '', ok).strip()
    bad = re.sub(r'\s+--(\s.*)?$', '', bad).strip()
    if '--' in mem or not ok or not bad or ok.startswith('--') or bad.startswith('--') or not mem:
        skipped.append(gid); continue
    if gid in ids:
        errs.append(f'duplicate id {gid}'); continue
    if pos not in ('v', 'n', 'a', 'x'):
        errs.append(f'{gid}: bad pos {pos}')
    m = [x.strip() for x in mem.split(',') if x.strip()]
    if len(m) < 2 or len(set(m)) != len(m):
        errs.append(f'{gid}: members {m}')
    g = {'id': gid, 'kind': 'contextual', 'pos': pos, 'm': m}
    for extra in parts[5:]:
        if extra.startswith('head='):
            g['head'] = int(extra[5:])
        elif extra.startswith('irr='):
            g.setdefault('irr', {})
            for spec in extra[4:].split(','):
                lem, forms = spec.split(':')
                g['irr'][lem.strip()] = [f.strip() for f in forms.split(';')]
        elif extra:
            errs.append(f'{gid}: unknown extra {extra}')
    try:
        g['ok'] = expand(ok, '=')
        g['bad'] = expand(bad, '≠')
    except ValueError as e:
        errs.append(f'{gid}: {e}')
    groups.append(g); ids.add(gid)

for g in groups:
    if not re.fullmatch(r'[a-z0-9_]+', g['id']):
        errs.append('id not snake_case: ' + g['id'])
if errs:
    print('\n'.join(errs)); sys.exit(1)
with open(OUT, 'w') as f:
    f.write('{"groups":[\n' + ',\n'.join(json.dumps(g, ensure_ascii=False) for g in groups) + '\n]}\n')
kinds = {}
for g in groups:
    kinds[g['kind']] = kinds.get(g['kind'], 0) + 1
print(kinds, os.path.getsize(OUT), 'bytes; skipped drafts:', len(skipped))
