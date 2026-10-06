import json
def row(frm, text, gap, acc=None):
    i = text.index(gap); a, b = text[:i].strip(), text[i+len(gap):].strip()
    parts = ([{"text": a}] if a else []) + [{"text": gap, "gap": True, "accept": acc or [gap]}] + ([{"text": b}] if b else [])
    assert " ".join(p["text"] for p in parts) == text
    return {"from": frm, "parts": parts}
def taps(l): return [{"phrase": p, "target": t, "voice": v} for p, t, v in l]
def nouns(l): return [{"word": w, "voice": v} for w, v in l]
F, M = "female", "male"
D = {}
D[269] = dict(level="B", keyWord="la envidia",
  taps=taps([("mirar por la ventanilla con envidia", "la chica", F), ("pasar pedaleando junto al autobús", "la ciclista", F), ("descansar sobre su regazo", "el manillar oxidado", F)]),
  nouns=nouns([("la ciclista", F), ("el pelo rizado", F), ("la camiseta sin mangas", F), ("el manillar", F)]),
  question="¿Qué está haciendo la chica del pelo rizado?",
  answer="Está mirando a la ciclista con envidia.".split(), answerVoice=F,
  recall=[row("taps", "mirar por la ventanilla con envidia", "ventanilla"), row("taps", "pasar pedaleando junto al autobús", "pedaleando"),
          row("taps", "descansar sobre su regazo", "regazo"), row("answer", "Está mirando a la ciclista con envidia", "envidia")],
  notes="The cyclist is a woman (pink top, long hair): 'la ciclista'. Phrase 1 carries the key word 'con envidia' (B-level collocation). Answer: 'con envidia' could also stand before 'a la ciclista' ('Está mirando con envidia a la ciclista'), both natural; the given order is the default. No noun row: 'la envidia' is not a noun of the set.")
D[270] = dict(level="A", keyWord="la goma",
  taps=taps([("tener la goma en la mano", "la chica", F), ("parecer una montaña", "la goma", F), ("tener un sol rojo", "la caja", F)]),
  nouns=nouns([("la caja", F), ("la mano", F), ("la goma", F), ("el papel", F)]),
  question="¿A qué se parece la goma?",
  answer="La goma se parece a una montaña pequeña.".split(), answerVoice=F,
  recall=[row("taps", "tener la goma en la mano", "goma"), row("taps", "parecer una montaña", "montaña"),
          row("taps", "tener un sol rojo", "sol"), row("answer", "se parece a una montaña pequeña", "parece")],
  notes="Phrase 1: English 'smile at the camera' is true only in the face frames; most boxed frames of the girl show only her hand rubbing out the scribbles or holding the eraser, so I wrote 'tener la goma en la mano' (the face frames she holds the box, not the eraser). 'la goma' is the everyday Spain word for eraser (= la goma de borrar). No noun row: tap row 1 already contains 'goma'.")
D[272] = dict(level="B", keyWord="evaporarse",
  taps=taps([("inclinar la sartén vacía", "la mujer", F), ("evaporarse en la sartén", "el agua", F), ("producir una llama azul", "el hornillo de camping", F)]),
  nouns=nouns([("las gafas protectoras", F), ("el vapor", F), ("la sartén", F), ("el hornillo de camping", F)]),
  question="¿Qué le está pasando al agua?",
  answer="El agua se está evaporando en la sartén caliente.".split(), answerVoice=F,
  recall=[row("taps", "inclinar la sartén vacía", "inclinar"), row("taps", "evaporarse en la sartén", "evaporarse"),
          row("taps", "producir una llama azul", "llama"), row("answer", "se está evaporando en la sartén caliente", "sartén")],
  notes="Phrase 2 'evaporarse en la sartén' (more natural than 'de la sartén'). The woman box also covers frames where she only looks at the pan; she tilts the empty pan towards the camera in the later boxed frames. Answer clitic could also be 'está evaporándose' (different chips, not an alternative order).")
D[273] = dict(level="A", keyWord="la tarde",
  taps=taps([("ponerse detrás de las colinas", "el sol", M), ("tener el pelo largo", "la mujer", F), ("llevar un jersey verde", "el hombre", M)]),
  nouns=nouns([("el cielo", M), ("el sol", M), ("las casas", M), ("la mujer", F)]),
  question="¿Qué hace el sol?",
  answer="El sol se pone detrás de las colinas.".split(), answerVoice=M,
  recall=[row("taps", "ponerse detrás de las colinas", "colinas"), row("taps", "tener el pelo largo", "pelo"),
          row("taps", "llevar un jersey verde", "jersey"), row("answer", "se pone detrás de las colinas", "pone")],
  notes="Key word: in Spain 'la tarde' covers the time until sunset/dusk, while the darker second half of the clip (town lights, moon) would already be 'la noche' for many speakers; 'la tarde' fits the sunset part. The key word does not appear in any exercise text (not a noun of the set). The man's sweater looks dark green in the dark frames.")
D[274] = dict(level="A", keyWord="todo el mundo",
  taps=taps([("levantar una bufanda", "el hombre de la bufanda", M), ("ir subido a los hombros de alguien", "el niño", M), ("brillar en el techo", "las luces", M)]),
  nouns=nouns([("las luces", M), ("el niño", M), ("la bufanda", M)]),
  question="¿Qué hace todo el mundo?",
  answer="Todo el mundo grita en el estadio.".split(), answerVoice=M,
  recall=[row("taps", "levantar una bufanda", "bufanda"), row("taps", "ir subido a los hombros de alguien", "hombros"),
          row("taps", "brillar en el techo", "brillar"), row("answer", "grita en el estadio", "grita", ["grita", "celebra"])],
  notes="Key word 'todo el mundo' is the subject of the answer, so the answer recall row (subject removed) does not contain it. Small rainbow flags are also waved in the crowd, but only the boxed man lifts a big rainbow scarf. The lights box covers the roof floodlights in all frames.")
for i, d in D.items():
    out = {"mediaId": i, "lang": "es", **{k: d[k] for k in ["level", "keyWord", "taps", "nouns", "question", "answer", "answerVoice"]}, "carousel": [], "recall": d["recall"], "notes": d["notes"]}
    json.dump(out, open(f"content/es/{i}.json", "w"), ensure_ascii=False, indent=2)
