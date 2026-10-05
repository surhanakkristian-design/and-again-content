import json, sys
def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        if b is None: out.append({"t": t, "off": True})
        else:
            x0, y0, x1, y1 = [max(0.0, min(1.0, v)) for v in b]
            out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out
def write(vid, spec):
    times = json.load(open(f'frames/{vid}/info.json'))['times']
    taps = []
    for p, tg, v, d in spec['taps']:
        taps.append({"phrase": p, "target": tg, "voice": v, "keys": keys(times, d)})
    c = {"mediaId": vid, "level": spec['level'], "keyWord": spec['keyWord'], "defaultVoice": spec['dv'], "taps": taps,
         "stillS": spec['stillS'], "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in spec['nouns']],
         "question": spec['q'], "answer": spec['a'].split(), "answerVoice": spec['av'], "notes": spec['notes']}
    json.dump(c, open(f'content/{vid}.json', 'w'), indent=1, ensure_ascii=False)
if __name__ == '__main__':
    F = 1.0
    G = {0.0:(.68,.16,1,.6), 0.5:(.6,.14,1,.62), 1.0:(.36,.08,1,.84), 1.5:(.15,.04,1,.9), 2.0:(.1,0,1,.84), 2.5:(.4,0,1,.76),
         3.0:(.45,0,1,.86), 3.5:(.42,0,1,.86), 4.0:(.42,.02,1,.86), 4.5:(.45,.02,1,.86), 5.0:(.42,.04,1,1), 5.5:(.45,.04,1,1),
         6.0:(0,0,1,1), 6.5:(0,0,1,1), 7.0:(0,0,1,1), 7.5:(0,0,1,1), 8.0:(0,0,1,1), 8.5:(0,0,1,1), 9.0:(0,.02,1,1), 9.5:(.04,.04,1,1),
         10.0:(.56,.21,1,.8), 10.5:(.53,.21,1,.72), 11.0:(.55,.24,1,.7), 11.5:(.5,.27,1,.7), 12.0:(.45,.25,1,.66)}
    W = {0.0:(.54,.21,.68,.52), 0.5:(.46,.2,.6,.47), 2.5:(.22,.18,.4,.5), 3.0:(.25,.2,.45,.52), 3.5:(.26,.22,.42,.52),
         4.0:(.24,.22,.42,.48), 4.5:(.27,.22,.45,.48), 5.0:(.24,.25,.42,.52), 5.5:(.28,.25,.45,.5),
         10.0:(.38,.25,.56,.63), 10.5:(.39,.25,.53,.63), 11.0:(.39,.26,.55,.62), 11.5:(.34,.26,.5,.62), 12.0:(.27,.27,.45,.62)}
    M = {0.0:(.16,.19,.47,.57), 0.5:(.08,.17,.35,.56), 1.0:(0,.16,.3,.56), 1.5:(0,.15,.14,.56),
         10.0:(0,.23,.3,.52), 10.5:(0,.24,.33,.56), 11.0:(0,.25,.32,.56), 11.5:(0,.25,.2,.56), 12.0:(0,.26,.19,.52)}
    write(4968, dict(level='A', keyWord='card', dv='female',
        taps=[("to pick up a card", "the red-haired girl", "female", G),
              ("to take a photo", "the woman with the phone", "female", W),
              ("to clap his hands", "the man with the moustache", "male", M)],
        stillS=11.0, nouns=[("a man", .13, .37, "male"), ("papers", .12, .57, "female"), ("a phone", .51, .47, "female"),
                            ("a card", .82, .62, "female"), ("a computer", .8, .88, "female")][1:] if False else
              [("papers", .12, .57, "female"), ("a phone", .51, .33, "female"), ("a card", .82, .47, "female"), ("a computer", .78, .9, "female")],
        q="What is the red-haired girl holding?", a="She is holding a card with her photo.", av="female",
        notes="Woman with the phone stands behind the girl from 2.5 to 5.5 and at 10-12: boxes split, the girl's box starts right of her (girl's hands on the left cut there). Woman off 1.0-2.0 and 6.0-9.5 (hidden / not identifiable). Man off 2.0-9.5; he claps only at 11-12 (gives thumbs up at 10.5). The clerk's arm (thumbs up) is not a target."))
