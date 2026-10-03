# Wrong words for videos of the Body Parts group (A32)

A Body Parts video shows a person (or an animal), so every body-part word fits it. Its wrong words come
from the key words of OTHER groups at the SAME level. Use these rules for every new Body Parts video.

## Mechanical (script `bp_first.py`)
- M1 the word is a key word of another group at the video's level; never a key word of the Body Parts group;
- M2 never a body-part concept (`out/body_part_concepts.json`);
- R1 not linked to the media; R2 no shared translation or display form with the key word in any of the 9 languages;
  R3 no shared English stem with the key word; R4 the word (or an inflected form) is not in the description or transcript;
  R5 not one of A31's "generic" words (`data/generic_a31.json`).

## Judgement (first look: read description + transcript for every word)
1. Take concrete, specific things that would be named in the description if they were there: animals that do not
   live where the clip plays, single foods, small objects, far-away places and vehicles.
2. No people, clothes, feelings, health, beauty or sport words: a person on screen wears, feels or does them.
3. Nothing that belongs to the setting, named or not: no furniture or room words indoors (window, chair, shelf, lamp,
   mirror), no landscape or street words outdoors (tree, cloud, grass, fence, car, bench), no park animals in a park
   (dog, pigeon, squirrel, duck), no sea words on a beach, no office things in an office, no food or kitchen words
   when someone eats or cooks, no animal at all in a zoo or wildlife park.
4. Nothing that is another everyday sense of the KEY word or goes with it: chest - box; palm - trees, island; calf - cow,
   barn, meadow; spine - cactus, book; neck - bottle, guitar, swan, giraffe; hand - clock; foot - ruler; eye - potato,
   telescope; tooth - shark, crocodile; lid - jar, jug, flask, blender; liver / belly - pork, bacon, pie, alcohol;
   joint - pub, pork, bacon, barbecue; nose - onion (crying), garlic (smell).
5. Nothing that names what an object in the clip looks like or is used like (kitchen turner over the dog -> no pan, egg,
   sausage; reflex hammer -> no hammer; medal -> no coin; finish tape -> no rope, flag; tape measure -> no ruler).
6. Words with a second everyday meaning are left out of the pool altogether (bat, mouse, duck, fish, chicken, turkey,
   seal, bear, key on a keyboard clip, letter on a clip with a sign).
7. (second look) No noun that is also an everyday verb or slang word for what is done or where it plays:
   train (to exercise), wolf (to wolf down food), drum (to drum on the belly), paddle (to walk in liquid), dive (a cheap diner).
8. (second look) No shape word when something in the clip has that shape (pyramid - a teepee of sticks; also diamond, dome, circle).
9. (second look) No word that contains or resembles a word for something in the clip (corkscrew - screws).
10. (second look) No typical background object of the place, even if the description is silent (umbrella on a sunny
    patio, warehouse near crates on a pier).
11. (second look) Check the slang and food senses of the key word too (joint - barbecue joint, joint of meat).
12. Doubt = leave it out. A second, independent look over the list; every doubt / fit is removed.

## Size and order
15-25 words per video (stored: at most 25), at least 10. Same part of speech as the key word first.
