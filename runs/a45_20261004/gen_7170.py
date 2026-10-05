from gen_7167_7168_7169_7170_lib import write
bird = [(.32,.07,.18,.14),(.40,.07,.18,.14),(.48,.06,.18,.14),(.56,.05,.18,.14),(.65,.04,.18,.14),(.74,.03,.18,.14),(.80,.02,.20,.14),None]
cat = [(.40,.54,.30,.28),(.37,.54,.32,.28),(.32,.55,.37,.28),(.29,.56,.42,.28),(.28,.56,.42,.28),(.28,.56,.43,.28),(.27,.56,.43,.28),(.28,.56,.43,.29)]
stag = [(.68,.34,.18,.14),(.68,.34,.18,.14),(.69,.34,.18,.14),(.70,.34,.18,.14),(.71,.34,.18,.14),(.71,.34,.18,.14),(.72,.33,.18,.14),(.72,.33,.18,.14)]
write(7170, "B", "glen", "female",
 [("to soar above the valley", "the bird", "female", bird),
  ("to walk in single file", "the cattle", "female", cat),
  ("to stand on the hillside", "the stag", "female", stag)],
 0.2,
 [("a rainbow", .62, .25, "female"), ("a glen", .62, .37, "female"),
  ("a stream", .26, .61, "female"), ("cattle", .62, .70, "female")],
 "What are the cattle doing?", ["They", "are", "walking", "in", "single", "file."], "female",
 "Wide landscape, all targets small. Bird and stag are tiny: minimum-size boxes around them; bird at the right edge, mostly out of frame at 3.7 s (off). Cattle = the whole line of cows as one target. 'a glen' pill sits on the distant valley floor (the glen is the whole valley, weakest noun). Stag: state phrase, no action fits.")
