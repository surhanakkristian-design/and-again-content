import json,sys,os
H=os.path.dirname(os.path.abspath(__file__))
# per id: phrases, nouns, Q, A, captions(list in source order), answer-recall row
D={
'de':{
'8055':(["nést muže","držet lano","viset na laně"],["horkovzdušný balón","mraky","lano","muž"],"Co dělá muž?","Visí na velkém horkovzdušném balónu.",["letět horkovzdušným balónem","přistát s horkovzdušným balónem","koš horkovzdušného balónu"],"visí na velkém horkovzdušném balónu"),
'236':(["plavat v moři","skočit do vzduchu","spadnout zpátky do vody"],["nebe","delfín","ocasní ploutev","voda"],"Co dělá delfín?","Vyskakuje z vody.",["skupina delfínů","plavat s delfínem","krmit delfína"],"vyskakuje z vody"),
'624':(["běžet za kloboukem","poletovat ve větru","chytit klobouk"],["stromy","klobouk","dívka","tráva"],"Co dělá dívka?","Běží za kloboukem.",["běžel za kloboukem","poběží za kloboukem","běžet na autobus"],"běží za kloboukem"),
'7071':(["nosit zlatou korunu","projíždět bahnem","odrážet šedé nebe"],["koruna","král","čtyřkolka","louže"],"Co dělá král?","Řídí čtyřkolku přes louži.",["mladý král","král a královna","uklonit se před králem"],"řídí čtyřkolku přes louži"),
'4265':(["vtrhnout do pokoje","lenošit na pohovce","uklidnit rozzlobeného kamaráda"],["dveře","křídla","papoušek","pohovka"],"Co dělá modrý papoušek?","Uklidňuje rozzlobeného papouška objetím.",["byl uklidněn rytířem","uklidnit štěkajícího psa","uklidnit plačící miminko"],"uklidňuje rozzlobeného papouška objetím"),
'461':(["obléknout figurínu","nosit šálu kolem krku","napodobit pózu figuríny"],["šála","košile","kočka","figurína"],"Co dělá muž?","Napodobuje pózu figuríny.",["nést figurínu","figurína ve výloze","obléknout figurínu"],"napodobuje pózu figuríny"),
'62':(["zvednout těžkou tašku","být plná jídla","nosit sluneční brýle"],["košile","chleba","jablka","taška"],"Co dělá muž?","Balí jídlo do tašky.",["upustit tašku","plážová taška","sportovní taška"],"balí jídlo do tašky"),
'8039':(["prokopat úzkou cestu","běžet po cestě","gestikulovat za oknem"],["sníh","lopata","pes","cesta"],"Co dělá žena venku?","Prokopává cestu sněhem.",["zatarasit průchod","úzký průchod","hledat průchod"],"prokopává cestu sněhem"),
'432':(["vést skupinu lesem","svítit ve tmě","nosit kulaté drátěné brýle"],["lucerna","údolí","bunda","batoh"],"Co dělá žena?","Vede skupinu s lucernou.",["vedl rytíře k hradu","povede roboty na Marsu","vést koně"],"vede skupinu s lucernou"),
'8056':(["číst knihu","vzhlížet k muži","sedět na lavičce"],["stromy","kniha","lavička","pes"],"Co dělá muž?","Čte si knihu na lavičce.",["posilovací lavice","natřít lavičku","dělit se o lavičku"],"čte si knihu na lavičce"),
},
'es':{
'8055':(["nést muže","držet lano","viset na laně"],["balón","mraky","lano","muž"],"Co dělá muž?","Visí na velkém balónu.",["letět balónem","přistát s balónem","koš balónu"],"visí na velkém balónu"),
'236':(["plavat v moři","vyskočit vysoko","spadnout do vody"],["nebe","delfín","ocas","voda"],"Co dělá delfín?","Vyskakuje z vody.",["skupina delfínů","plavat s delfínem","krmit delfína"],"vyskakuje z vody"),
'624':(["běžet za kloboukem","poletovat ve větru","chytit klobouk"],["stromy","klobouk","dívka","tráva"],"Co dělá dívka?","Běží za kloboukem.",["běžel za kloboukem","poběží za kloboukem","běžet na autobus"],"běží za kloboukem"),
'7071':(["nosit zlatou korunu","projíždět bahnem","odrážet šedé nebe"],["koruna","král","čtyřkolka","louže"],"Co dělá král?","Projíždí na čtyřkolce louží.",["mladý král","král a královna","uklonit se před králem"],"projíždí na čtyřkolce louží"),
'4265':(["vtrhnout do pokoje","rozvalovat se na pohovce","uklidnit rozzuřeného kamaráda"],["dveře","křídla","papoušek","pohovka"],"Co dělá modrý papoušek?","Uklidňuje rozzuřeného papouška objetím.",["byl uklidněn rytířem","uklidnit štěkajícího psa","uklidnit plačící miminko"],"uklidňuje rozzuřeného papouška objetím"),
'461':(["obléknout figurínu","nosit šátek kolem krku","napodobit pózu figuríny"],["šátek","košile","kočka","figurína"],"Co dělá kluk?","Napodobuje pózu figuríny.",["nést figurínu na rameni","výlohová figurína","obléknout figurínu"],"napodobuje pózu figuríny"),
'62':(["zvednout těžkou tašku","být plná jídla","nosit sluneční brýle"],["košile","chleba","jablka","taška"],"Co dělá muž?","Plní tašku jídlem.",["upustit tašku","plážová taška","sportovní taška"],"plní tašku jídlem"),
'8039':(["prokopat cestu ve sněhu","běžet po odklizené cestě","ukazovat přes sklo"],["sníh","lopata","pes","cesta"],"Co dělá dívka, která je venku?","Prokopává cestu ve sněhu.",["zatarasit průchod","úzký průchod","hledat průchod"],"prokopává cestu ve sněhu"),
'432':(["vést skupinu","svítit ve tmě","nosit brýle s kulatými obroučkami"],["lucerna","údolí","bunda","batoh"],"Co dělá dívka?","Vede skupinu s lucernou.",["vedl několik rytířů k hradu","povede několik robotů po Marsu","vést koně"],"vede skupinu s lucernou"),
'8056':(["číst knihu","dívat se na muže","sedět na lavičce"],["stromy","kniha","lavička","pes"],"Co dělá muž?","Čte si knihu na lavičce.",["posilovací lavice","natřít lavičku","dělit se o lavičku"],"čte si knihu na lavičce"),
},
'fr':{
'8055':(["nést muže","držet lano","viset na laně"],["horkovzdušný balón","mraky","lano","muž"],"Co dělá muž?","Visí na velkém horkovzdušném balónu.",["letět horkovzdušným balónem","přistát s horkovzdušným balónem","koš horkovzdušného balónu"],"visí na velkém horkovzdušném balónu"),
'236':(["plavat v moři","skočit do vzduchu","dopadnout zpátky do vody"],["nebe","delfín","ocas","voda"],"Co dělá delfín?","Vyskakuje z vody.",["skupina delfínů","plavat s delfínem","krmit delfína"],"vyskakuje z vody"),
'624':(["běžet za kloboukem","uletět ve větru","chytit klobouk"],["stromy","klobouk","dívka","tráva"],"Co dělá dívka?","Běží za kloboukem.",["běžel za kloboukem","poběží za kloboukem","běžet na autobus"],"běží za kloboukem"),
'7071':(["nosit zlatou korunu","rozstřikovat bláto","odrážet šedé nebe"],["koruna","král","čtyřkolka","louže"],"Co dělá král?","Projíždí na čtyřkolce louží.",["mladý král","král a královna","uklonit se před králem"],"projíždí na čtyřkolce louží"),
'4265':(["vtrhnout do pokoje","lenošit na pohovce","uklidnit rozzuřeného kamaráda"],["dveře","křídla","papoušek","pohovka"],"Co dělá modrý papoušek?","Uklidňuje rozzuřeného papouška objetím.",["byl uklidněn rytířem","uklidnit štěkajícího psa","uklidnit plačící miminko"],"uklidňuje rozzuřeného papouška objetím"),
'461':(["obléknout figurínu","mít přes sebe přehozenou šálu","napodobit pózu figuríny"],["šála","košile","kočka","figurína"],"Co dělá mladý muž?","Napodobuje pózu figuríny.",["nést figurínu","výlohová figurína","obléknout figurínu"],"napodobuje pózu figuríny"),
'62':(["zvednout těžkou tašku","být plná jídla","nosit sluneční brýle"],["polokošile","bageta","jablka","taška"],"Co dělá muž?","Plní tašku jídlem.",["upustit tašku","plážová taška","sportovní taška"],"plní tašku jídlem"),
'8039':(["prokopat průchod","běžet podél průchodu","gestikulovat za sklem"],["sníh","lopata","pes","průchod"],"Co dělá žena venku?","Prokopává průchod ve sněhu.",["zatarasit průchod","úzký průchod","hledat průchod"],"prokopává průchod ve sněhu"),
'432':(["vést skupinu","osvětlovat stezku","nosit brýle s kulatými obroučkami"],["lucerna","údolí","bunda","batoh"],"Co dělá mladá žena?","Vede skupinu s lucernou.",["vedl rytíře k hradu","povede roboty na Marsu","vést koně"],"vede skupinu s lucernou"),
'8056':(["číst knihu","dívat se na muže","sedět na lavičce"],["stromy","kniha","lavička","pes"],"Co dělá muž?","Čte si knihu na lavičce.",["posilovací lavice","natřít lavičku","dělit se o lavičku"],"čte si knihu na lavičce"),
}}
for lang,T in D.items():
    src=json.load(open(f'{H}/source_{lang}.json')); out={}
    for vid,s in src.items():
        ph,no,q,a,ca,ar=T[vid]
        m={}
        for p,t in zip(s['phrases'],ph): m[p['text']]=t
        caps=dict(zip(s['captions'],ca)); m.update(caps)
        for n,t in zip(s['nouns'],no): m.setdefault(n,t)
        m.setdefault(s['answer'][:-1].split(' ',1)[1] if lang!='fr' or True else '',None)
        rec=[]
        for r in s['recall']:
            rec.append(m[r] if m.get(r) else ar)
        assert sum(1 for r in s['recall'] if not m.get(r))==1,(lang,vid)
        out[vid]={"phrases":ph,"nouns":no,"question":q,"answer":a,"captions":caps,"recall":rec}
    json.dump(out,open(f'{H}/{lang}/cz.json','w'),ensure_ascii=False,indent=1)
