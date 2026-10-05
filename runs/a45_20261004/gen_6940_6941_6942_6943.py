import json, sys
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            x = max(0, x); y = max(0, y); w = min(w, 1 - x); h = min(h, 1 - y)
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(w, 2), "h": round(h, 2)})
    return out
def write(c):
    json.dump(c, open(f"content/{c['mediaId']}.json", "w"), indent=1, ensure_ascii=False)
V = {}
V[6940] = dict(mediaId=6940, level="A", keyWord="change trains", defaultVoice="female",
  taps=[
    dict(phrase="to jump onto a train", target="the woman", voice="female", keys=keys([
      (.27,.23,.45,.53),(.41,.28,.52,.56),(.5,.23,.43,.64),(.56,.16,.4,.7),(.6,.14,.37,.72),(.6,.13,.37,.74),(.6,.13,.37,.76),(.61,.12,.36,.79)])),
    dict(phrase="to pull a suitcase", target="the man with the suitcase", voice="male", keys=keys([
      None,None,(.29,.43,.21,.3),(.24,.42,.28,.32),(.2,.41,.29,.32),(.15,.41,.29,.33),(.11,.4,.33,.36),(.07,.4,.35,.39)])),
    dict(phrase="to wave a green flag", target="the man with the flag", voice="male", keys=keys([
      (0,.26,.27,.26),(0,.24,.25,.28),(0,.22,.2,.16),(0,.22,.2,.14),(0,.18,.18,.14),None,None,None])),
  ],
  stillS=2.2,
  nouns=[dict(word="a train", x=.15, y=.38, voice="female"), dict(word="a dog", x=.6, y=.62, voice="female"),
         dict(word="an apple", x=.15, y=.84, voice="female"), dict(word="a cup", x=.57, y=.88, voice="female")],
  question="What is the woman doing?", answer=["She","is","jumping","onto","a","train."], answerVoice="female",
  notes="Man with the suitcase is small and hidden behind the woman at 0.2/0.7 -> off. Flag man: only arm+flag from 1.2, flag at the edge at 2.2, gone from 2.7. Right-hand conductor is not a target (no flag).")

V[6941] = dict(mediaId=6941, level="B", keyWord="change", defaultVoice="male",
  taps=[
    dict(phrase="to hold up an old photograph", target="the hands", voice="male", keys=keys([
      (.14,.44,.74,.3),(.18,.45,.7,.31),(.17,.46,.72,.3),(.17,.48,.72,.3),(.11,.49,.78,.3),(.1,.53,.8,.32),(.08,.58,.9,.4),(.1,.6,.9,.4)])),
    dict(phrase="to point at the wrecked hut", target="the man", voice="male", keys=keys([
      None,None,None,None,(.72,.17,.18,.2),(.73,.18,.18,.2),(.72,.18,.18,.22),(.72,.18,.18,.2)])),
    dict(phrase="to crash against the rocks", target="the waves", voice="male", keys=keys([
      (0,.22,.62,.21),(0,.2,.72,.24),(0,.23,.72,.22),(0,.2,.75,.27),(0,.22,.6,.26),(0,.3,.55,.22),(0,.25,.5,.3),(0,.27,.5,.3)])),
  ],
  stillS=3.7,
  nouns=[dict(word="a beach hut", x=.45, y=.22, voice="male"), dict(word="rocks", x=.3, y=.5, voice="male"),
         dict(word="a photograph", x=.42, y=.7, voice="male"), dict(word="a mug", x=.79, y=.85, voice="male")],
  question="What is the man doing?", answer=["He","is","pointing","at","the","wrecked","hut."], answerVoice="male",
  notes="POV hands hold the photo (no visible person -> 'the hands', default voice). The man only appears from 2.2 (a sliver of his head at the right edge at 1.7 -> off); the woman in yellow is not a target and stands right next to him, his box stops at x .90. Waves calm down from 2.7 but still wash over the rocks on the left. Key word 'change' is abstract, not a noun slot.")

V[6942] = dict(mediaId=6942, level="B", keyWord="channel", defaultVoice="female",
  taps=[
    dict(phrase="to gush through the open gate", target="the water", voice="female", keys=keys([
      (.1,.44,.48,.3),(.12,.44,.46,.32),(.1,.44,.48,.32),(.1,.44,.52,.32),(.08,.44,.52,.32),(.08,.44,.56,.32),(.06,.46,.54,.33),(.04,.46,.54,.33)])),
    dict(phrase="to swim through the foam", target="the frog", voice="female", keys=keys([
      (.61,.55,.2,.15),(.63,.55,.2,.15),(.67,.55,.2,.15),(.76,.56,.22,.15),(.8,.57,.2,.15),None,None,None])),
    dict(phrase="to span the narrow channel", target="the footbridge", voice="female", keys=keys([
      (.35,.2,.42,.15),(.35,.2,.42,.15),(.35,.2,.42,.15),(.35,.2,.42,.15),(.35,.2,.42,.15),(.35,.2,.42,.15),(.34,.21,.42,.15),(.33,.21,.44,.16)])),
  ],
  stillS=0.2,
  nouns=[dict(word="a sluice gate", x=.15, y=.25, voice="female"), dict(word="a footbridge", x=.58, y=.27, voice="female"),
         dict(word="a channel", x=.55, y=.4, voice="female"), dict(word="foam", x=.75, y=.72, voice="female")],
  question="What is the water doing?", answer=["It","is","gushing","through","the","open","gate."], answerVoice="female",
  notes="No people. The water box covers only the brown jet by the gate, not the whole channel, so it stays clear of the frog. The frog is small (a few % of the frame), visible 0.2-2.2 drifting right in the foam, gone from 2.7 - check that it reads as a frog and that 'swim' is fair. A tiny bird sits on the gate at 1.7 and flies off (not used). Footbridge phrase is a state (no action fits a bridge).")

ACT = keys([(.29,.18,.55,.72),(.3,.13,.55,.77),(.29,.13,.56,.77),(.29,.22,.55,.68),(.24,.3,.62,.7),(.22,.29,.64,.71),(.19,.28,.68,.72),(.21,.27,.66,.73)])
V[6943] = dict(mediaId=6943, level="A", keyWord="character", defaultVoice="male",
  taps=[
    dict(phrase="to lift a long stick", target="the man in the helmet", voice="male", keys=ACT),
    dict(phrase="to shout at the audience", target="the man in the helmet", voice="male", keys=ACT),
    dict(phrase="to wear a black hat", target="the man in the black hat", voice="male", keys=keys([
      (0,.4,.28,.6),(0,.4,.27,.6),(0,.39,.27,.61),(0,.39,.27,.61),(0,.38,.24,.62),(0,.38,.21,.62),(0,.37,.18,.63),(0,.37,.19,.63)])),
  ],
  stillS=2.7,
  nouns=[dict(word="the sea", x=.7, y=.12, voice="male"), dict(word="a helmet", x=.62, y=.36, voice="male"),
         dict(word="a hat", x=.12, y=.42, voice="male"), dict(word="a stick", x=.82, y=.86, voice="male")],
  question="What is the actor doing?", answer=["He","is","shouting","at","the","audience."], answerVoice="male",
  notes="Two men: the actor in the horned helmet and the stagehand in black. Stagehand has no clear action (stands by the ropes), so his phrase is a state ('to wear a black hat'). Two phrases share the actor. Boxes split at the stagehand's hand/cape edge (x .18-.24 from 2.2). 'stick' used instead of 'staff' for level A.")
for i in sys.argv[1:]:
    write(V[int(i)])
