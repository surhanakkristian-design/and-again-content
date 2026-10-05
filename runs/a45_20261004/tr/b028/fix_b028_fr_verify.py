import json
p='fr.json'; d=json.load(open(p)); log=[]
def fx(i,field,idx,old,new,why):
    cur = d[i][field] if idx is None else d[i][field][idx]
    assert cur==old,(i,field,cur)
    if idx is None: d[i][field]=new
    else: d[i][field][idx]=new
    log.append(f"- {i} {field}{'' if idx is None else '['+str(idx)+']'}: \"{old}\" -> \"{new}\" ({why})")
fx('7328','phrases',2,"courir en haut rose","courir avec un haut rose","'en haut' reads as 'upstairs'; garment needs 'avec un'")
fx('7337','phrases',2,"être assis sur sa tête","être posé sur sa tête","a bird is 'posé', not 'assis'")
fx('7339','phrases',1,"se poser au nid","se poser sur le nid","unidiomatic preposition")
fx('7352','question',None,"Que fait le mannequin ?","Que fait la mannequin ?","female model; feminine 'la mannequin' agrees with 'Elle' in the answer")
fx('7367','phrases',0,"faire la moue","avancer les lèvres","'faire la moue' = to pout/sulk, not to purse the lips like a fish")
fx('7367','answer',None,"Elle fait la moue comme un poisson.","Elle avance les lèvres comme un poisson.","same as phrase")
fx('7372','phrases',2,"tenir la corde depuis le bas","tenir la corde d'en bas","natural form")
fx('7372','answer',None,"Elle hisse un lourd ballot sur la véranda.","Elle hisse un lourd ballot sur la terrasse.","'véranda' is a glazed conservatory in France; a treehouse porch is a 'terrasse'")
fx('7386','phrases',1,"courir vers son ami","foncer vers son ami","'sprint' = run at full speed; plain 'courir' lost it")
fx('7389','phrases',0,"brandir une hache","manier une hache","'brandir' = raise/wave; swinging to chop is 'manier'")
fx('7392','nouns',0,"une boîte de conserve","une boîte en métal","it is an open tin of oil, not a food can")
fx('7396','phrases',2,"refléter les lumières scintillantes","refléter les lumières qui brillent","'scintillantes' = twinkling, not glowing")
fx('7407','nouns',1,"un manteau en poil de chameau","un manteau camel","a camel coat is the colour/style; 'manteau camel' is the French term")
fx('7411','phrases',2,"se prendre la tête","se tenir la tête","'se prendre la tête' alone is the colloquial 'get worked up'")
fx('7411','answer',None,"Il se prend la tête entre les mains.","Il se tient la tête entre les mains.","same word as the phrase")
fx('7415','nouns',3,"des mots croisés","une grille de mots croisés","English is singular 'a crossword'")
fx('7420','phrases',0,"montrer le champ du doigt","montrer l'autre côté du champ","she points across the field, not at it")
fx('7420','answer',None,"Elle montre le champ du doigt.","Elle montre l'autre côté du champ.","same as phrase")
fx('7434','nouns',2,"une plaque","un marbre","home plate in baseball is 'le marbre'")
fx('7434','phrases',2,"écarter grand les bras","ouvrir grand les bras","English 'open'; idiomatic form")
fx('7473','nouns',0,"des chaumières","des maisonnettes","'chaumière' = thatched cottage; these are stone cottages")
fx('7492','nouns',3,"un bidon de pétrole","un baril de pétrole","an oil drum is a 'baril', a 'bidon' is a can")
fx('7742','phrases',1,"se prendre la tête, incrédule","se tenir la tête, incrédule","'se prendre la tête' = colloquial 'get worked up'")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('fix_b028_fr_verify.log','w').write('\n'.join(log))
print(len(log))
