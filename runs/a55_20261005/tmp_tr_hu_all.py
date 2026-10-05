# hu translations for de/es/fr (helper: hu, de+es+fr)
import json, os
H = os.path.dirname(os.path.abspath(__file__))
# per lang, per id: phrases, nouns, q, a, answer-recall-row, captions(list in source order), extra recall map
T = {
'de': {
'8055': (["egy férfit szállítani","egy kötelet tartani","egy kötélen lógni"],["hőlégballon","felhők","kötél","férfi"],"Mit csinál a férfi?","Egy nagy hőlégballonon lóg.","egy nagy hőlégballonon lóg",["hőlégballonnal repülni","leszállni egy hőlégballonnal","a hőlégballon kosara"]),
'236': (["úszni a tengerben","a levegőbe ugrani","visszaesni a vízbe"],["ég","delfin","farokuszony","víz"],"Mit csinál a delfin?","Kiugrik a vízből.","kiugrik a vízből",["egy csapat delfin","egy delfinnel úszni","megetetni egy delfint"]),
'624': (["egy kalap után szaladni","repülni a szélben","elkapni egy kalapot"],["fák","kalap","lány","fű"],"Mit csinál a lány?","Egy kalap után szalad.","egy kalap után szalad",["egy kalap után szaladt","egy kalap után fog szaladni","a buszhoz szaladni"]),
'7071': (["aranykoronát viselni","átgurulni a sáron","tükrözni a szürke eget"],["korona","király","quad","pocsolya"],"Mit csinál a király?","Átvezeti a quadot egy pocsolyán.","átvezeti a quadot egy pocsolyán",["egy fiatal király","király és királynő","meghajolni a király előtt"]),
'4265': (["berontani a szobába","lustálkodni a kanapén","megnyugtatni egy dühös barátot"],["ajtó","szárnyak","papagáj","kanapé"],"Mit csinál a kék papagáj?","Egy öleléssel megnyugtatja a dühös papagájt.","egy öleléssel megnyugtatja a dühös papagájt",["egy lovag nyugtatta meg","megnyugtatni egy ugató kutyát","megnyugtatni egy síró babát"]),
'461': (["felöltöztetni egy próbababát","sálat viselni a nyaka körül","utánozni a próbababa pózát"],["sál","ing","macska","próbababa"],"Mit csinál a férfi?","Utánozza a próbababa pózát.","utánozza a próbababa pózát",["próbababát cipelni","a próbababa a kirakatban","felöltöztetni egy próbababát"]),
'62': (["felemelni egy nehéz táskát","tele lenni étellel","napszemüveget viselni"],["ing","kenyér","almák","táska"],"Mit csinál a férfi?","Ételt pakol a táskába.","ételt pakol a táskába",["leejteni egy táskát","strandtáska","sporttáska"]),
'8039': (["kilapátolni egy keskeny utat","végigszaladni az úton","gesztikulálni az ablak mögött"],["hó","lapát","kutya","út"],"Mit csinál kint a nő?","Utat lapátol a hóban.","utat lapátol a hóban",["elzárni az átjárót","a keskeny átjáró","átjárót keresni"]),
'432': (["átvezetni a csoportot az erdőn","világítani a sötétben","drótkeretes szemüveget viselni"],["lámpás","völgy","kabát","hátizsák"],"Mit csinál a nő?","Egy lámpással vezeti a csoportot.","egy lámpással vezeti a csoportot",["lovagokat vezetett egy várhoz","robotokat fog vezetni a Marson","lovat vezetni"]),
'8056': (["könyvet olvasni","felnézni a férfira","egy padon ülni"],["fák","könyv","pad","kutya"],"Mit csinál a férfi?","Könyvet olvas egy padon.","könyvet olvas egy padon",["edzőpad","lefesteni egy padot","osztozni egy padon"]),
},
'es': {
'8055': (["egy férfit szállítani","egy kötelet tartani","egy kötélen lógni"],["hőlégballon","felhők","kötél","férfi"],"Mit csinál a férfi?","Egy nagy hőlégballonon lóg.","egy nagy hőlégballonon lóg",["hőlégballonnal repülni","leszállni egy hőlégballonnal","a hőlégballon kosara"]),
'236': (["úszni a tengerben","nagyon magasra ugrani","a vízbe esni"],["ég","delfin","farok","víz"],"Mit csinál a delfin?","Kiugrik a vízből.","kiugrik a vízből",["egy csapat delfin","egy delfinnel úszni","megetetni egy delfint"]),
'624': (["egy kalap után szaladni","repülni a széllel","elkapni egy kalapot"],["fák","kalap","lány","fű"],"Mit csinál a lány?","Egy kalap után szalad.","egy kalap után szalad",["egy kalap után szaladt","egy kalap után fog szaladni","szaladni a busz után"]),
'7071': (["aranykoronát viselni","haladni a sárban","tükrözni a szürke eget"],["korona","király","quad","pocsolya"],"Mit csinál a király?","Quaddal hajt át egy pocsolyán.","quaddal hajt át egy pocsolyán",["egy fiatal király","a király és a királynő","meghajolni a király előtt"]),
'4265': (["berontani a szobába","elterülni a kanapén","megnyugtatni egy dühös barátot"],["ajtó","szárnyak","papagáj","kanapé"],"Mit csinál a kék papagáj?","Egy öleléssel megnyugtatja a dühös papagájt.","egy öleléssel megnyugtatja a dühös papagájt",["egy lovag nyugtatta meg","megnyugtatni egy ugató kutyát","megnyugtatni egy síró babát"]),
'461': (["felöltöztetni egy próbababát","sálat viselni a nyakában","utánozni a próbababa pózát"],["sál","ing","macska","próbababa"],"Mit csinál a fiú?","Utánozza a próbababa pózát.","utánozza a próbababa pózát",["próbababát vinni a vállán","kirakati próbababa","felöltöztetni egy próbababát"]),
'62': (["felemelni egy nehéz táskát","tele lenni étellel","napszemüveget viselni"],["ing","kenyér","almák","táska"],"Mit csinál a férfi?","Megtölti a táskát étellel.","megtölti a táskát étellel",["leejteni egy táskát","strandtáska","sporttáska"]),
'8039': (["utat vágni a hóban","végigszaladni a megtisztított úton","mutogatni az üvegen át"],["hó","lapát","kutya","út"],"Mit csinál a lány, aki kint van?","Utat vág a hóban.","utat vág a hóban",["elzárni az átjárót","a keskeny átjáró","átjárót keresni"]),
'432': (["vezetni a csoportot","világítani a sötétben","kerek keretes szemüveget viselni"],["lámpás","völgy","kabát","hátizsák"],"Mit csinál a lány?","Egy lámpással vezeti a csoportot.","egy lámpással vezeti a csoportot",["lovagokat vezetett egy vár felé","robotokat fog vezetni a Marson","lovat vezetni"]),
'8056': (["könyvet olvasni","a férfira nézni","egy padon ülni"],["fák","könyv","pad","kutya"],"Mit csinál a férfi?","Könyvet olvas egy padon.","könyvet olvas egy padon",["edzőpad","lefesteni egy padot","osztozni egy padon"]),
},
'fr': {
'8055': (["egy férfit szállítani","egy kötelet tartani","egy kötélen lógni"],["hőlégballon","felhők","kötél","férfi"],"Mit csinál a férfi?","Egy nagy hőlégballonon lóg.","egy nagy hőlégballonon lóg",["hőlégballonnal repülni","leszállni egy hőlégballonnal","a hőlégballon kosara"]),
'236': (["úszni a tengerben","a levegőbe ugrani","visszaesni a vízbe"],["ég","delfin","farok","víz"],"Mit csinál a delfin?","Kiugrik a vízből.","kiugrik a vízből",["egy csapat delfin","egy delfinnel úszni","megetetni egy delfint"]),
'624': (["egy kalap után szaladni","elrepülni a széllel","elkapni egy kalapot"],["fák","kalap","lány","fű"],"Mit csinál a lány?","Egy kalap után szalad.","egy kalap után szalad",["egy kalap után szaladt","egy kalap után fog szaladni","szaladni a busz után"]),
'7071': (["aranykoronát viselni","sarat fröcskölni","tükrözni a szürke eget"],["korona","király","quad","pocsolya"],"Mit csinál a király?","Quaddal hajt át egy pocsolyán.","quaddal hajt át egy pocsolyán",["egy fiatal király","a király és a királynő","meghajolni a király előtt"]),
'4265': (["berontani a szobába","lustálkodni a kanapén","megnyugtatni egy dühös barátot"],["ajtó","szárnyak","papagáj","kanapé"],"Mit csinál a kék papagáj?","Egy öleléssel megnyugtatja a dühös papagájt.","egy öleléssel megnyugtatja a dühös papagájt",["egy lovag nyugtatta meg","megnyugtatni egy ugató kutyát","megnyugtatni egy síró babát"]),
'461': (["felöltöztetni egy próbababát","sállal be lenni tekerve","utánozni a próbababa pózát"],["sál","ing","macska","próbababa"],"Mit csinál a fiatalember?","Utánozza a próbababa pózát.","utánozza a próbababa pózát",["próbababát cipelni","kirakati próbababa","felöltöztetni egy próbababát"]),
'62': (["felemelni egy nehéz táskát","tele lenni étellel","napszemüveget viselni"],["pólóing","bagett","almák","táska"],"Mit csinál a férfi?","Megtölti a táskát étellel.","megtölti a táskát étellel",["leejteni egy táskát","strandtáska","sporttáska"]),
'8039': (["kitakarítani egy átjárót","végigszaladni az átjárón","gesztikulálni az üveg mögött"],["hó","lapát","kutya","átjáró"],"Mit csinál kint a nő?","Kitakarít egy átjárót a hóban.","kitakarít egy átjárót a hóban",["elzárni az átjárót","keskeny átjáró","átjárót keresni"]),
'432': (["vezetni a csoportot","megvilágítani az ösvényt","kerek keretes szemüveget viselni"],["lámpás","völgy","kabát","hátizsák"],"Mit csinál a fiatal nő?","Egy lámpással vezeti a csoportot.","egy lámpással vezeti a csoportot",["lovagokat vezetett egy vár felé","robotokat fog vezetni a Marson","lovat vezetni"]),
'8056': (["könyvet olvasni","a férfira nézni","egy padon ülni"],["fák","könyv","pad","kutya"],"Mit csinál a férfi?","Könyvet olvas egy padon.","könyvet olvas egy padon",["edzőpad","lefesteni egy padot","osztozni egy padon"]),
},
}
for lang, vids in T.items():
    src = json.load(open(f'{H}/tr/source_{lang}.json'))
    out = {}
    for vid, s in src.items():
        ph, no, q, a, arow, caps = vids[vid]
        m = {}
        for x, y in zip([p['text'] for p in s['phrases']], ph): m[x] = y
        for x, y in zip(s['captions'], caps): m.setdefault(x, y)
        for x, y in zip(s['nouns'], no): m.setdefault(x, y)
        m.setdefault(s['recall'][len(ph)] if s['recall'][len(ph)] not in m else '__', arow)
        rec = []
        for r in s['recall']:
            if r in m: rec.append(m[r])
            else: rec.append(arow)
        out[vid] = {"phrases": ph, "nouns": no, "question": q, "answer": a,
                    "captions": dict(zip(s['captions'], caps)), "recall": rec}
    os.makedirs(f'{H}/tr/{lang}', exist_ok=True)
    json.dump(out, open(f'{H}/tr/{lang}/hu.json', 'w'), ensure_ascii=False, indent=1)
