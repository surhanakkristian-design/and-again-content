"""Brief 20 Part 6: a piece never ends on a determiner, a preposition + determiner, or a numeral that
belongs to the noun in the next piece; and a piece is never a bare determiner.

The defect is a determiner STRANDED from its noun phrase, so two things must hold at once:
  (1) the piece ends on a determiner/numeral word with no punctuation after it (a comma or full stop
      means the phrase is closed: "meine," "ein." "zeigte acht," are pronouns, prefixes, clock times);
  (2) the NEXT piece begins the noun phrase: its first word is not a conjunction, preposition, pronoun,
      finite verb, adverb or negation (per-language stop lists below). "Das | ist", "ein | und",
      "alle drei | auf", "los dos | fueron" are pronoun / separable-prefix uses, not stranded articles.
Numerals get two more exemptions: a clock-time / pronoun trigger before them ("um halb sieben",
"los dos", "at six"), and in German a capitalised noun before them ("Woche fünf", "Nummer 7").
Pronoun homographs (German 'sein', 'ihr'; English 'that', 'her', 'this') stay out of the lists on purpose.
scripts/brief19/determiners.py and supabase/functions/chunk-sentences/index.ts carry the same tables."""
import re
DET = {
    "de": r"der|die|das|den|dem|des|ein|eine|einen|einem|einer|eines|kein|keine|keinen|keinem|keiner|"
          r"mein|meine|meinen|meinem|meiner|dein|deine|deinen|deinem|deiner|seine|seinen|seinem|seiner|"
          r"ihre|ihren|ihrem|ihrer|unser|unsere|unseren|unserem|unserer|eure|euren|eurem|eurer|"
          r"dieser|diese|dieses|diesen|diesem|jener|jene|jenes|jenen|jenem|jeder|jede|jedes|jeden|jedem|"
          r"welcher|welche|welches|welchen|welchem|im|am|ans|ins|zum|zur|vom|beim|"
          r"zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|zwanzig|dreißig|hundert|tausend|dreizehn|vierzehn|fünfzehn|sechzehn|siebzehn|achtzehn|neunzehn|vierzig|fünfzig|sechzig|siebzig|achtzig|neunzig",  # Part 15
    "en": r"the|a|an|my|your|his|its|our|their|these|those|each|every|"
          r"two|three|four|five|six|seven|eight|nine|ten|twenty|hundred|thousand|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|thirty|forty|fifty|sixty|seventy|eighty|ninety",  # Part 15
    "es": r"el|la|los|las|un|una|unos|unas|del|al|ese|esa|esos|esas|este|esta|estos|estas|aquel|aquella|aquellos|aquellas|"
          r"mi|tu|su|mis|tus|sus|nuestro|nuestra|nuestros|nuestras|cada|otro|otra|otros|otras|mismo|misma|mismos|mismas|"
          r"dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|veinte|treinta|cien|mil|once|doce|trece|catorce|quince|dieciséis|diecisiete|dieciocho|diecinueve|cuarenta|cincuenta|sesenta|setenta|ochenta|noventa|ciento",  # Part 15
    "fr": r"le|la|les|un|une|des|du|au|aux|ce|cet|cette|ces|mon|ma|mes|ton|ta|tes|son|sa|ses|notre|nos|votre|vos|leur|leurs|chaque|"
          r"deux|trois|quatre|cinq|six|sept|huit|neuf|dix|vingt|cent|mille|"
          r"onze|douze|treize|quatorze|quinze|seize|dix-sept|dix-huit|dix-neuf|trente|quarante|cinquante|soixante|soixante-dix|quatre-vingts|quatre-vingt-dix|quatre-vingt",  # Part 14: 11-19 and the tens
}
NUM = r"[0-9]+"
NUMWORDS = {
    "de": r"zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|zwanzig|dreißig|hundert|tausend|dreizehn|vierzehn|fünfzehn|sechzehn|siebzehn|achtzehn|neunzehn|vierzig|fünfzig|sechzig|siebzig|achtzig|neunzig",
    "en": r"one|two|three|four|five|six|seven|eight|nine|ten|twenty|hundred|thousand|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|thirty|forty|fifty|sixty|seventy|eighty|ninety",
    "es": r"dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|veinte|treinta|cien|mil|once|doce|trece|catorce|quince|dieciséis|diecisiete|dieciocho|diecinueve|cuarenta|cincuenta|sesenta|setenta|ochenta|noventa|ciento",
    "fr": r"deux|trois|quatre|cinq|six|sept|huit|neuf|dix|vingt|cent|mille|onze|douze|treize|quatorze|quinze|seize|dix-sept|dix-huit|dix-neuf|trente|quarante|cinquante|soixante|soixante-dix|quatre-vingts|quatre-vingt-dix|quatre-vingt",
}
# word before a numeral that makes it a clock time, an arithmetic term or a pronoun ("the two")
TIME_OR_PRONOUN = {
    "de": r"(?:um|halb|punkt|die|den|der|zu|bis|ab|seit|gegen|nach|vor|von|bei|unter|über|plus|minus|und|mal|alle|diese|beide)\s+(?:%s)$",
    "en": r"(?:at|half|past|the|by|until|till|around|about|to|of|plus|minus|and|times|all|these|those|both|gate|room|page|week|number|no\.|platform|line|bus|train|chapter|floor|seat|table|track|lane|grade|level|round|day|year|hour|minute|size|step|stage|unit|lesson|part|act|scene|episode|season|flight|door|row|aisle|terminal|exit|highway|route|channel|class)\s+(?:%s)$",
    "es": r"(?:a\s+las|a\s+la|las|los|la|hasta\s+las|desde\s+las|sobre\s+las|de\s+las|de\s+los|y|más|menos|por|todos|todas|estos|estas|ambos|"
          r"número|n\.º|nº|página|capítulo|habitación|puerta|línea|autobús|bus|tren|fila|talla|nivel|piso|calle|semana|día|año|hora|minuto|paso|"
          r"episodio|temporada|vuelo|mesa|asiento|andén|sala|aula|clase|grupo|equipo|zona|ruta|canal|planta|edificio|bloque|apartamento|"
          r"kilómetro|km|lección|parte|acto|escena|ronda|dorsal|camiseta|salida|terminal|carril|pista|vía|sector|lote|modelo|versión|tomo|"
          r"volumen|serie|unidad|tema|ejercicio|pregunta|punto|artículo|grado|curso|ciclo|edad|edición)\s+(?:%s)$",
    "fr": r"(?:à|les|des|vers|jusqu'à|de|depuis|et|plus|moins|fois|tous|toutes|ces|"
          r"numéro|n°|page|chapitre|chambre|porte|ligne|bus|train|rang|rangée|taille|niveau|étage|rue|semaine|jour|année|an|heure|minute|étape|"
          r"épisode|saison|vol|table|siège|quai|salle|classe|groupe|équipe|zone|route|chaîne|bâtiment|bloc|appartement|kilomètre|km|leçon|"
          r"partie|acte|scène|tour|dossard|maillot|sortie|terminal|voie|piste|secteur|lot|modèle|version|tome|volume|série|unité|thème|"
          r"exercice|question|point|article|degré|cours|cycle|âge|édition)\s+(?:%s)$",
}
# first word of the NEXT piece that cannot open a noun phrase (so the determiner before it is a pronoun,
# a separable prefix, a number or a clock time, not a stranded article)
STOP = {
    "de": set("""und oder aber sondern denn als wie dass ob wenn weil obwohl sobald bevor nachdem während damit also deshalb trotzdem
        an auf in im am ans ins aus bei mit nach von vom vor zu zum zur über unter hinter neben zwischen durch für gegen ohne um seit ab bis entlang aufs
        ist sind war waren wird werden wurde wurden hat haben hatte hatten kann können konnte muss müssen musste soll sollen sollte will wollen wollte
        darf dürfen mag möchte bleibt bleiben geht gehen ging kommt kommen kam macht machen machte sieht sehen sah zeigt zeigen liegt liegen steht stehen
        sitzt sitzen fällt fliegt schläft schwimmt gibt gab sagt sagte fragt fragte weint lacht sein lässt fiel weg
        er sie es wir ihr ich du man sich mir dir ihm ihn uns euch ihnen nicht nie nur auch noch schon jetzt gerade heute gestern morgen dann da dort hier
        wieder weiter zurück los hinaus heraus hinein herein hinunter herunter hinauf herauf raus rein runter rauf sehr so ganz immer oft meistens sonst
        selbst sogar genau ja nein doch mal eben schnell langsam leise laut zu
        der die das den dem des ein eine einen einem einer eines kein keine keinen jeden jede jedes jeder alle beide viele einige jemand niemand etwas nichts""".split()),
    "en": set("""and or but nor so yet because if when while as than that which who whom whose where why how
        is are was were be been being has have had do does did can could will would shall should may might must
        goes went come came get got make made take took give gave
        at in on of to for with from by about into onto over under up down off out through across along around between behind before after during without within near past
        i you he she it we they me him her us them not never only also still just now then there here very too again away back even always often usually sometimes""".split()),
    "es": set("""y e o u pero sino ni que quien quienes cual cuales donde cuando como porque si aunque mientras
        es son era eran fue fueron está están estaba estaban hay ha han había tiene tienen tenía puede pueden debe deben va van iba viene vienen
        hace hacen dice dicen quiere quieren sabe saben ve ven da dan pone ponen sale salen llega llegan parece parecen
        a ante bajo con contra de desde en entre hacia hasta para por según sin sobre tras
        no nunca también tampoco sí ya aún todavía ahora hoy ayer mañana luego después antes aquí ahí allí muy más menos tan bien mal siempre casi solo sólo
        se lo le les me te nos os
        alrededor delante detrás encima debajo dentro fuera cerca lejos junto frente enfrente arriba abajo adelante atrás
        yo tú él ella usted nosotros nosotras vosotros vosotras ellos ellas ustedes
        el la los las un una unos unas cada otro otra otros otras este esta estos estas ese esa esos esas aquel aquella
        mi tu su mis tus sus nuestro nuestra algún alguna ningún ninguna todo toda todos todas mucho mucha muchos muchas poco poca pocos pocas varios varias""".split()),
    "fr": set("""et ou mais ni car donc que qui dont où quand comme parce si lorsque tandis puis
        est sont était étaient a ont avait avaient peut peuvent doit doivent va vont fait font dit disent veut veulent sait savent voit voient vient viennent
        prend prennent met mettent reste restent semble
        à au aux de du des en dans sur sous par pour avec sans chez vers entre derrière devant après avant depuis pendant contre
        ne n' pas jamais plus aussi encore déjà toujours souvent maintenant ici là très trop bien mal ensuite alors ainsi
        se s' le la les lui leur y me te nous vous il elle ils elles on je tu
        autour devant derrière dessus dessous dedans dehors près loin ensemble face en-face au-dessus au-dessous
        le la les un une des du au aux ce cet cette ces mon ma mes ton ta tes son sa ses notre nos votre vos leur leurs chaque quelques plusieurs tout toute tous toutes""".split()),
}
# a piece that is ONLY a preposition (not the last piece) whose noun phrase starts the next piece:
# "auf | dem Tablett", "in | the kitchen" — the same stranding one word earlier
PREP = {
    "de": r"an|auf|in|mit|nach|von|vor|zu|über|unter|hinter|neben|zwischen|durch|für|gegen|ohne|um|aus|bei|seit|bis|ab|entlang|gegenüber|während|wegen|trotz|innerhalb|außerhalb|statt|außer",  # Part 15 ("laut" is phrase-only, see PREP_PHRASE_ONLY)
    "en": r"at|in|on|of|to|for|with|from|by|about|into|onto|over|under|through|across|along|around|between|behind|before|after|during|without|within|near|past|towards|toward|against|among|beneath|beside|inside|outside|underneath|above|below|than|since|until",  # Part 15 ("like" is phrase-only, see PREP_PHRASE_ONLY)
    "es": r"a|ante|bajo|con|contra|de|desde|en|entre|hacia|hasta|para|por|según|sin|sobre|tras|durante|mediante|incluso|salvo",  # Part 15
    "fr": r"à|dans|sur|sous|par|pour|avec|sans|chez|vers|entre|derrière|devant|après|avant|depuis|pendant|contre|de|en|parmi|malgré|selon|"
          r"jusqu'à|jusqu'au|jusqu'aux|jusqu'en",  # Part 14
}
def _first_word(piece):
    w = piece.strip().split()[0] if piece.strip() else ""
    return re.sub(r"[^\w']", "", w).lower()
def _numeral_exempt(p, lang):
    if not re.search(r"(?:^|\s)(?:" + NUMWORDS[lang] + "|" + NUM + r")$", p, re.I): return False
    if re.search(TIME_OR_PRONOUN[lang] % (NUMWORDS[lang] + "|" + NUM), p, re.I): return True
    if lang == "de" and re.search(r"(?:^|\s)[A-ZÄÖÜ][\wäöüß-]*\s+(?:" + NUMWORDS[lang] + "|" + NUM + r")$", p): return True  # "Woche fünf"
    return False
def strands(piece, nxt, lang):
    """piece ends on a determiner/numeral (no punctuation) and nxt opens a noun phrase."""
    p = piece.rstrip()
    if not re.search(r"(?:^|\s)(?:" + DET[lang] + "|" + NUM + r")$", p, re.I): return False
    if _numeral_exempt(p, lang): return False
    # Spanish "ahora mismo", "aquí mismo": mismo is an adverb intensifier there, not a determiner
    if lang == "es" and re.search(r"(?:^|\s)(?:ahora|aquí|ahí|allí|hoy|ya|así|ayer|mañana|luego|entonces|yo|tú|él|ella|usted|nosotros|nosotras|vosotros|vosotras|ellos|ellas|ustedes|sí|uno|una|lo)\s+mism[oa]s?$", p, re.I): return False
    return _opens_noun_phrase(nxt, lang)
def ends_on_determiner(piece, nxt, lang): return strands(piece, nxt, lang)
def is_bare_determiner(piece, nxt, lang):
    return re.fullmatch(r"(?:" + DET[lang] + "|" + NUM + r")", piece.strip(), re.I) is not None and strands(piece, nxt, lang)
def _opens_noun_phrase(nxt, lang):
    w = _first_word(nxt)
    if not w or w in STOP[lang]: return False
    if lang == "de" and not nxt.strip()[0].isupper() and not re.search(r"(?:e|er|es|en|em)$", w): return False
    return True
def is_bare_preposition(piece, nxt, lang):
    # after a bare preposition a determiner DOES open the noun phrase ("auf | dem Tablett"), so the
    # determiner words in STOP (there for the pronoun case "das | die Seide") do not exempt it here
    if re.fullmatch(r"(?:" + PREP[lang] + r")", piece.strip(), re.I) is None: return False
    return re.fullmatch(r"(?:" + DET[lang] + r")", _first_word(nxt), re.I) is not None or _opens_noun_phrase(nxt, lang)
# Part 15: prepositions that are also a verb or an adverb ("I like", "laut rufen"): they may OPEN a whole phrase
# ("like a cat", "laut dem Plan") but a lone piece of that word is not a stranded preposition
PREP_PHRASE_ONLY = {"en": r"like", "de": r"laut"}
# a compound preposition ("detrás de", "antes de", "près de", "à côté de") is never cut before its "de":
# the locative/temporal head at the end of a piece with de/del (es) or de/du/des/d' (fr) opening the next piece
COMPOUND_HEAD = {
    "es": r"encima|debajo|delante|detrás|dentro|fuera|cerca|lejos|alrededor|antes|después|enfrente|junto|frente|arriba|abajo|además|acerca|través",
    "fr": r"au-dessus|au-dessous|devant|derrière|dedans|dehors|près|loin|autour|avant|après|face|côté|lors|hors",
}
COMPOUND_TAIL = {"es": r"de|del", "fr": r"de|du|des|d'[^\s]*"}
def cuts_compound_preposition(piece, nxt, lang):
    if lang not in COMPOUND_HEAD: return False
    if not re.search(r"(?:^|\s)(?:" + COMPOUND_HEAD[lang] + r")$", piece.rstrip(), re.I): return False
    # es homographs: "no fuera | de cristal" (fuera = verb), "boca abajo | del techo" (fixed adverb)
    if lang == "es" and re.search(r"(?:^|\s)(?:no|se|me|te|le|nos|os|ojalá|si|que|quien|nunca)\s+fuera$|(?:^|\s)boca\s+abajo$", piece.rstrip(), re.I): return False
    return re.fullmatch(r"(?:" + COMPOUND_TAIL[lang] + r")", (nxt.split() or [""])[0], re.I) is not None
def determiner_faults(chunks, lang):
    if lang not in DET: return []
    out = []
    pairs = list(zip(chunks[:-1], chunks[1:]))
    if any(cuts_compound_preposition(a, b, lang) for a, b in pairs): out.append("compound_preposition_cut")
    if any(strands(a, b, lang) for a, b in pairs): out.append("piece_ends_on_determiner")
    if any(is_bare_determiner(a, b, lang) for a, b in pairs): out.append("bare_determiner_piece")
    if any(is_bare_preposition(a, b, lang) for a, b in pairs): out.append("bare_preposition_piece")
    joins = [a.strip() + " | " + b.strip() for a, b in pairs]
    if lang in GROUP_CUT and any(GROUP_CUT[lang].search(j) for j in joins): out.append("verb_group_cut")     # Part 15
    if lang in QUANT_CUT and any(QUANT_CUT[lang].search(j) for j in joins): out.append("quantifier_cut")     # Part 15
    return out


# ---------------------------------------------------------------------------
# Brief 20 Part 8: the phrase is the unit. Two proxies (the half-sentence cap, the four-piece floor at
# nine words) may be exceeded ONLY when the split is already at the minimum piece count the other rules
# allow: every piece is uncuttable, i.e. one word, an answer part, a whole phrase (preposition/determiner
# + content words), or a piece whose every internal cut would strand a determiner or a preposition.
# Every such exemption is named, counted per run and reported.
# ---------------------------------------------------------------------------
LEAD_ADV = {  # an adverb that may open a prepositional phrase: "all along the table", "encima de la mesa", "ganz oben"
    "de": r"ganz|direkt|genau|gleich|kurz|tief|weit|mitten|hoch|dicht|oben|unten|vorn|hinten|links|rechts|innen|außen",
    "en": r"all|right|just|straight|even|way|deep|far|high|halfway|inside|outside|instead|ahead|next|close|near|because|out|up|down|off",
    "es": r"justo|muy|encima|debajo|delante|detrás|dentro|fuera|cerca|lejos|alrededor|antes|después|enfrente|junto|frente|arriba|abajo|además|acerca|través|como",
    "fr": r"juste|tout|très|au-dessus|au-dessous|devant|derrière|dedans|dehors|près|loin|autour|avant|après|face|côté|lors|hors|comme|travers",  # Part 14: "à travers"
}
# a preposition or conjunction INSIDE a noun phrase ("manta de picnic", "un deporte duro y rápido"); it must be
# followed by determiners/numerals and then content again, never close the phrase
LINK = {
    "de": r"und|oder|von|vom|mit|für|aus|zu|zum|zur|an|am|in|im|auf|über|unter|ohne|gegen|nach|bei|beim",
    "en": r"and|or|nor|of|with|for|in|on|at|from|by|about|without|between|under|over|to",
    "es": r"y|e|o|u|ni|de|del|con|sin|para|por|en|a|al|entre|sobre|contra|hasta|desde|según",
    "fr": r"et|ou|ni|de|du|des|d'|à|au|aux|avec|sans|pour|par|en|sur|sous|entre|contre|vers|chez",
}
# determiner homographs that the strand rule leaves out (pronoun readings) but that DO open a noun phrase when
# content words follow: "her book", "this old shirt", "sein Hund", "muchos años"
PHRASE_DET = {
    "de": r"sein|ihr|alle|viele|einige|wenige|mehrere|manche|solche|beide|welch|lauter",
    "en": r"her|that|this|some|any|no|several|many|few|much|more|most|all|both|half|such|what|which|whose|another|either|neither",
    "es": r"algún|alguna|algunos|algunas|ningún|ninguna|muchos|muchas|mucho|mucha|pocos|pocas|poco|poca|varios|varias|todos|todas|todo|toda|tanto|tanta|tantos|tantas|cuántos|cuántas|cuánto|cuánta|qué|cuyo|cuya|ambos|ambas|más|menos|bastante|bastantes|demasiado|demasiada|demasiados|demasiadas",
    "fr": r"quel|quelle|quels|quelles|plusieurs|quelques|tout|toute|tous|toutes|aucun|aucune|certains|certaines|chaque|nul|nulle|plus|moins|beaucoup|peu|trop|assez|tant|autant|combien",
}
# Part 14 (fr) / Part 15 (en, es): after one of these quantifiers the partitive (de/d', of) belongs to the determiner
# group ("beaucoup de sable", "one of the boys", "un poco de sal"); it is not a stranded preposition. QUANT_EXTRA are
# quantifier words that are in no determiner table but may sit in the determiner run ("a lot of", "plenty of", "algo de").
QUANTIFIER = {
    "fr": r"beaucoup|peu|trop|assez|tant|autant|plus|moins|combien",
    "en": r"one|half|all|some|most|none|plenty|lot|lots",
    "es": r"poco|poca|pocos|pocas|más|menos|mucho|mucha|muchos|muchas|algo",
}
QUANT_EXTRA = {"en": r"plenty|lot|lots|none", "es": r"algo"}
PARTITIVE = {"fr": "de", "en": "of", "es": "de"}
# Part 14 (fr) / Part 15 (en, de, es): the existential verb group is one unit for the exemption test; a negation particle
# (pas, not, kein-) may follow; the inverted question form counts too ("y a-t-il", "is there", "gibt es")
VERB_GROUP = {
    "fr": re.compile(r"(?:qu['’]est-ce\s+)?(?:qu['’]\s*)?(?:il y a|il n['’]y a|y a-t-il|il y avait|il n['’]y avait)(?:\s+(?:pas|plus|jamais|rien))?", re.I),
    "en": re.compile(r"(?:there(?:'s|’s| is| are| was| were| isn't| aren't| wasn't| weren't)|(?:is|are|was|were) there)(?: not)?", re.I),
    "de": re.compile(r"(?:es (?:gibt|gab)|(?:gibt|gab) es)(?: (?:kein|keine|keinen|keinem|keiner|nicht))?", re.I),
    "es": re.compile(r"(?:no hay que|no hay|hay que)", re.I),
}
# Part 15: a cut INSIDE one of these groups is a fault (the run must reject it, not route around it): the boundary is
# tested on "piece | next piece"
GROUP_CUT = {
    "fr": re.compile(r"(?:^|\s)il \| y a|(?:^|\s)il n['’] ?\| ?y a|(?:^|\s)il y \| a\b|(?:^|\s)y \| a-t-il|(?:^|\s)il \| n['’]y a", re.I),
    "en": re.compile(r"(?:^|\s)there \| (?:is|are|was|were|isn't|aren't|wasn't|weren't)\b|^(?:is|are|was|were) \| there\b", re.I),   # inverted form only when the piece IS the verb ("Is | there"), not "I were | there"
    "de": re.compile(r"(?:^|\s)es \| (?:gibt|gab)\b|(?:^|\s)(?:gibt|gab) \| es\b", re.I),
    "es": re.compile(r"(?:^|\s)no \| hay\b|(?:^|\s)hay \| que\b", re.I),
}
QUANT_CUT = {
    "fr": re.compile(r"(?:^|\s)(?:beaucoup|peu|trop|assez|tant|autant|plus|moins|combien) \| d(?:e\b|')", re.I),
    "en": re.compile(r"(?:^|\s)(?:one|half|all|some|most|none|plenty|lot|lots) \| of\b", re.I),
    "es": re.compile(r"(?:^|\s)(?:poco|poca|pocos|pocas|más|menos|mucho|mucha|muchos|muchas|algo) \| de\b", re.I),
}
# degree adverbs that sit INSIDE a noun phrase ("una cama muy grande", "ein sehr freundlicher Hund", "a very old house");
# they are stop words for the strand rule but content for the whole-phrase test
DEGREE = {
    "de": r"sehr|ganz|ziemlich|recht|so|zu|besonders|wirklich|extrem|total|echt|super|richtig|äußerst",
    "en": r"very|really|quite|rather|pretty|so|too|more|most|less|least|extremely|incredibly|super|fairly",
    "es": r"muy|tan|más|menos|bastante|demasiado|realmente|súper|solo|sólo|casi|poco|bien|mucho",
    "fr": r"très|si|plus|moins|assez|trop|vraiment|tout|toute|presque|bien|fort",
}
MAX_WORDS_FOR_EXEMPTION = 9
MAX_LONG_PIECE_WORDS = 6  # Part 10: the long-sentence cap exemption bounds the oversized piece, not the sentence
MAX_FLOOR_EXEMPTION_WORDS = 11  # Part 10 decision 1: three uncuttable pieces are enough up to 11 words (data: nothing at 12+)
def _word_count(s):
    return sum(1 for t in s.split() if re.search(r"[^\W_]", t))
def _tokens(piece):
    return [re.sub(r"^[^\w]+|[^\w]+$", "", t).lower() for t in piece.split()]
def _is(word, pattern): return re.fullmatch(r"(?:" + pattern + r")", word, re.I) is not None
def is_whole_phrase(piece, lang):
    """^ [preposition] [lead adverb] [preposition] (determiner | numeral)* content ( LINK (determiner | numeral)* content )* $
    — a phrase with no internal cut point that the rules could accept: a cut before the content words strands
    a function word, a cut among the content words separates an adjective from its noun, a cut at a LINK word
    ("manta de picnic", "duro y rápido") strands a preposition or conjunction."""
    w = [t for t in _tokens(piece) if t]
    if not w: return False
    i = 0
    # "por encima de la mesa", "hasta dentro del aro": a preposition may precede the lead adverb
    prep = PREP[lang] + ("|" + PREP_PHRASE_ONLY[lang] if lang in PREP_PHRASE_ONLY else "")
    if _is(w[i], prep) and len(w) > 2 and _is(w[i + 1], LEAD_ADV[lang]): i += 1
    if _is(w[i], LEAD_ADV[lang]) and len(w) > i + 1: i += 1
    if i < len(w) and _is(w[i], prep): i += 1
    dn = DET[lang] + "|" + PHRASE_DET[lang] + "|" + NUMWORDS[lang] + "|" + NUM
    dq = dn + ("|" + QUANT_EXTRA[lang] if lang in QUANT_EXTRA else "")
    while i < len(w) and _is(w[i], dq): i += 1
    if lang in QUANTIFIER and 0 < i < len(w) and _is(w[i - 1], QUANTIFIER[lang]):
        # Part 14/15: the partitive after a quantifier ("beaucoup de", "one of", "un poco de") is part of the determiner group
        if w[i] == PARTITIVE[lang]:
            i += 1
            while i < len(w) and _is(w[i], dq): i += 1   # "plus de deux chaises", "one of the two boys"
        elif lang == "fr" and re.match(r"d['’]\S", w[i]):
            w[i] = w[i][2:]                               # "d'espace" -> "espace"
    if i == 0: return False                      # no preposition/determiner at the front: not a phrase we can vouch for
    rest = w[i:]
    if not rest: return False
    hard = set(DET[lang].split("|")) | set(PHRASE_DET[lang].split("|")) | set(PREP[lang].split("|")) | set(NUMWORDS[lang].split("|"))
    fn = STOP[lang] | hard
    deg = set(DEGREE[lang].split("|"))
    j = 0; saw_content = False
    while j < len(rest):
        t = rest[j]; last = j == len(rest) - 1
        if _is(t, LINK[lang]) and saw_content and not last:
            j += 1
            while j < len(rest) and _is(rest[j], dn): j += 1
            if j >= len(rest): return False       # the phrase may not close on a link word or a determiner
            continue
        # "la barba más larga", "le pain le moins cher": a degree word after the noun is content, not a determiner
        if (t in hard and not (saw_content and t in deg)) or re.fullmatch(NUM, t): return False
        if t in fn and t not in deg:
            # the head noun comes last and may be a verb/pronoun homograph ("trash can") when content precedes it
            if last and saw_content: j += 1; continue
            return False
        saw_content = True; j += 1
    return saw_content
def _answer_parts(answer):
    return {x.strip() for x in (answer or "").split("...") if x.strip()}
def is_uncuttable(piece, lang, answer_parts=()):
    # Part 12: a punctuation-only token (French " ?", " !", a spaced dash) is not a word, so "fait-il ?" is one word
    ws = [t for t in piece.split() if re.search(r"[^\W_]", t)]
    if len(ws) <= 1: return True
    core = re.sub(r"^[^\w¿¡„“\"']+|[^\w.!?,;:\"“”']+$", "", piece.strip())
    if core in answer_parts or re.sub(r"[.!?,;:]+$", "", core) in answer_parts: return True
    if lang in VERB_GROUP and VERB_GROUP[lang].fullmatch(re.sub(r"[.!?,;:\s]+$", "", core)): return True   # Part 14/15: "il y a", "there is", "es gibt", "no hay"
    if is_whole_phrase(piece, lang): return True
    # every internal cut strands a determiner or a preposition
    return all(determiner_faults([" ".join(ws[:k]), " ".join(ws[k:])], lang) for k in range(1, len(ws)))
def exemptions(full_sentence, chunks, lang, answer=None):
    """Names of the proxies this split is allowed to exceed (empty when none is needed or none is allowed).
    cap_whole_phrase : a piece holds more than half of the words, but it is one whole phrase and the split
                       is at the minimum the other rules allow (sentence of up to 9 words).
    floor_min_pieces : a sentence of 9 to 11 words with three pieces, each of them uncuttable (Part 10: 9 -> 11).
    cap_whole_phrase_long : Brief 20 Part 10 — the cap exemption at ANY length when every piece is uncuttable,
                       the oversized piece is a whole phrase (not merely uncuttable by the cut test) and it holds
                       at most 6 words. Counted under its own name so the extension never hides in the original."""
    import math
    if lang not in DET: return []
    n = _word_count(full_sentence)
    parts = _answer_parts(answer)
    if not all(is_uncuttable(p, lang, parts) for p in chunks): return []
    out = []
    mx = max(_word_count(p) for p in chunks)
    if n <= MAX_WORDS_FOR_EXEMPTION:
        if mx > math.ceil(n / 2): out.append("cap_whole_phrase")
    elif mx > math.ceil(n / 2) and mx <= MAX_LONG_PIECE_WORDS:
        big = [p for p in chunks if _word_count(p) == mx]
        if all(is_whole_phrase(p, lang) for p in big): out.append("cap_whole_phrase_long")
    if 9 <= n <= MAX_FLOOR_EXEMPTION_WORDS and len(chunks) == 3: out.append("floor_min_pieces")
    return out
