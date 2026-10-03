# A32 task 1: body-part concepts (judged by reading word + definition of all 2,987 key words).
# kind: H = human body part (also on animals), A = animal-only part
BODY = {
 126:("H","definition"),139:("H","definition"),263:("H","definition; also reads as a box"),484:("H","definition; also part of a shoe"),
 492:("H","definition"),566:("H","definition"),601:("H","definition: facial hair, like beard"),1002:("H","definition"),
 1017:("H","word: defined as the back of a place, but the bare word reads as the body part"),
 2212:("H","word: adverb 'back', the bare word reads as the body part"),2213:("H","definition"),
 3751:("H","word: adjective 'back', the bare word reads as the body part"),
 1040:("H","definition"),1066:("H","definition"),
 1073:("H","word: defined as the sea bottom, but the bare word reads as the part you sit on"),4969:("H","definition"),
 1297:("H","definition"),1300:("H","definition"),5845:("H","word: verb 'to face', the bare word reads as the body part"),
 1319:("H","definition"),1340:("H","definition"),1404:("H","definition"),1413:("H","definition"),
 5264:("H","word: defined as a farm worker, but the bare word reads as the body part"),
 1424:("H","definition"),1494:("H","definition"),1513:("H","definition"),1588:("H","definition"),1598:("H","definition"),
 1610:("H","definition"),1832:("H","definition"),1853:("H","definition"),2002:("H","definition"),2064:("H","definition"),
 2067:("H","definition"),2069:("H","definition"),2121:("H","definition"),2200:("H","definition"),2232:("H","definition"),
 2295:("H","definition"),2497:("H","definition"),2592:("H","definition"),2781:("H","definition"),3117:("H","definition"),
 3176:("H","definition"),3252:("H","definition"),3263:("H","definition"),3350:("H","definition; also a tree"),
 3589:("H","definition"),3664:("H","definition"),
 4973:("H","word: defined as a clever person, but the bare word reads as the organ"),
 4982:("H","definition"),4998:("H","word: defined as the end of a handle, but the bare word reads as the part you sit on"),
 5194:("H","definition"),5326:("H","definition"),5332:("H","definition"),5354:("H","definition"),
 5348:("H","definition: the eyelid"),5399:("H","definition: the front of the body below the chest"),
 5344:("H","definition: the left hand"),5176:("H","definition: a part of the face"),
 3149:("H","doubt: defined as the shape of a human body; every person on screen has one"),
 5183:("H","doubt: same bare word as 3149 'figure' (the shape of a body)"),
 855:("H","doubt: defined as a building, but 'temple' is also the side of the head"),
 424:("A","definition: animal hair"),2157:("A","definition: body part for flying"),
 3655:("A","word: defined as an airplane wing, but the bare word reads as the animal part"),
 737:("A","doubt: defined as a weighing device, but 'scale' is also what covers a fish or reptile"),
 5974:("A","doubt: same bare word as 737 'scale'"),
}
# read and NOT counted (not a part of the body); listed for the owner
NOT_COUNTED = {
 221:"braid: a hairstyle, not a part",232:"bun: a hairstyle",674:"ponytail: a hairstyle",1406:"haircut",1407:"hairstyle",133:"wig: worn",
 116:"scar: a mark on the skin",975:"wrinkle: a line in the skin",853:"tattoo: a picture on the skin",654:"piercing",
 3582:"tears: a fluid / crying",1958:"sweat: a fluid",2976:"breath: a process",2425:"fat (adjective)",5173:"fat: grease in meat",
 5803:"cardiac (adjective)",5828:"dental (adjective)",4959:"blood pressure",45:"chicken drumstick: food",
 5317:"ivory: a material",1511:"leather: a material",2166:"wool: a material",25:"bill: also a bird's beak, rare sense",
 1183:"comb: also a rooster's comb, rare sense",1174:"coat: also an animal's coat, rare sense",1433:"hide: also an animal's skin, rare sense",
 22:"bark: of a tree",7:"root: of a plant",5396:"membrane: a sheet of material",417:"footprints: marks",1837:"side",
 847:"swelling: a condition",3372:"pit",6076:"lens: of a camera",2712:"seat",5044:"column",2322:"column",5122:"disc",5073:"cord",
}
HUMAN={c for c,(k,_) in BODY.items() if k=="H"}; ANIMAL={c for c,(k,_) in BODY.items() if k=="A"}
if __name__=="__main__":
    from load import *
    keys={r["concept"] for r in twd.values()}
    assert set(BODY)<=keys and not set(BODY)&set(NOT_COUNTED)
    out=[dict(id=c,word=concepts[c]["word"],pos=concepts[c]["part_of_speech"],definition=concepts[c]["definition"],kind="human" if k=="H" else "animal",why=w) for c,(k,w) in sorted(BODY.items())]
    json.dump(out,open("out/body_part_concepts.json","w"),indent=1,ensure_ascii=False)
    with open("out/body_part_concepts.md","w") as f:
        f.write(f"# A32 body-part concepts ({len(out)}: {len(HUMAN)} human, {len(ANIMAL)} animal-only)\n\nRead: word, part of speech and definition of all {len(keys)} key words. A concept counts when its definition is a body part, or when the bare English word also reads as one (the card shows only the bare word; doubt = body part).\n\n| id | word | pos | definition | kind | why |\n|---|---|---|---|---|---|\n")
        for o in out: f.write(f"| {o['id']} | {o['word']} | {o['pos']} | {o['definition']} | {o['kind']} | {o['why']} |\n")
        f.write("\n## Read and not counted (for the owner to overrule)\n\n| id | word | definition | why not |\n|---|---|---|---|\n")
        for c,w in sorted(NOT_COUNTED.items()): f.write(f"| {c} | {concepts[c]['word']} | {concepts[c]['definition']} | {w} |\n")
    print(len(out),len(HUMAN),len(ANIMAL))
