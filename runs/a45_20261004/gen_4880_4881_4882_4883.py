import json, sys
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        if t in d: x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    taps2=[{"phrase":p,"target":tg,"voice":v,"keys":keys(k)} for p,tg,v,k in taps]
    nn=[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns]
    json.dump({"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,"taps":taps2,"stillS":still,
               "nouns":nn,"question":q,"answer":ans.split(),"answerVoice":av,"notes":notes},
              open(f"content/{mid}.json","w"),indent=1)
which=int(sys.argv[1])
if which==4880:
    man={0.0:(0,0.06,0.58,0.72),2.0:(0,0.10,0.80,0.88),2.5:(0,0.12,0.75,0.86),3.0:(0,0.0,0.60,0.75),
         4.5:(0,0.13,0.64,0.85),6.0:(0.05,0.19,0.50,0.24),6.5:(0.12,0.13,0.38,0.23),8.5:(0,0,0.88,0.95),9.0:(0,0.12,1.0,0.88)}
    bot={6.0:(0.22,0.44,0.78,0.35),6.5:(0.13,0.37,0.85,0.35),7.0:(0.31,0.28,0.58,0.43),7.5:(0.46,0.41,0.22,0.16)}
    write(4880,"A","bottle","male",
      [("to drop a watermelon","the man","male",man),("to raise his arms","the man","male",man),
       ("to have a blue cap","the bottle","male",bot)],
      6.0,[("the sky",0.5,0.08,"male"),("a man",0.28,0.40,"male"),("a bottle",0.55,0.60,"male"),("a wall",0.72,0.90,"male")],
      "What is the man doing?","He is dropping a bottle from the roof.","male",
      "Man head-only boxes at 6.0/6.5 so they do not overlap the bottle; arms-only frames (0.5, 5.0, 7.0) marked off. Water balloon also blue but has no cap.")
if which==4881:
    wom={0.0:(0,0.12,0.47,0.53),0.5:(0,0.14,0.52,0.46),1.0:(0,0.12,0.62,0.56),1.5:(0,0.15,0.72,0.56)}
    bus={2.0:(0.04,0.10,0.96,0.47),2.5:(0.06,0.12,0.94,0.46),3.0:(0.05,0.12,0.92,0.45),3.5:(0.04,0.15,0.90,0.42),4.0:(0.04,0.15,0.88,0.41)}
    grp={t:(0,0.66,1.0,0.18) for t in [6.5,7.0,7.5,8.0,8.5,9.0]}
    write(4881,"A","bus","male",
      [("to close her eyes","the woman","female",wom),("to have the number 230","the bus","male",bus),
       ("to push a big stone","the big group","male",grp)],
      2.5,[("the sky",0.2,0.06,"male"),("a bus",0.6,0.25,"male"),("people",0.5,0.55,"male"),("the street",0.65,0.85,"male")],
      "What are the people doing?","They are pushing a big bus.","male",
      "defaultVoice male: mixed group (evenId false). Woman phrase uses closed eyes because a second, mostly hidden person also pushes the car. Group target only in the boulder shot (6.5-9.0).")
if which==4882:
    wom={4.5:(0.38,0.40,0.38,0.32),5.0:(0.47,0.40,0.38,0.32)}
    plane={5.5:(0,0.07,1,0.39),6.0:(0,0.07,1,0.39),6.5:(0,0.05,1,0.43),7.0:(0,0.06,1,0.43),7.5:(0,0.06,1,0.44),
           8.0:(0,0.06,1,0.45),8.5:(0,0.06,1,0.46),9.0:(0,0.06,1,0.48)}
    team={5.5:(0.05,0.47,0.82,0.33),6.0:(0.04,0.47,0.84,0.33),6.5:(0.12,0.48,0.82,0.33),7.0:(0.18,0.50,0.82,0.31),
          7.5:(0.25,0.51,0.75,0.30),8.0:(0.33,0.51,0.67,0.29),8.5:(0.40,0.53,0.60,0.28),9.0:(0.45,0.55,0.55,0.28)}
    write(4882,"B","aircraft","female",
      [("to drag a pickup truck","the woman in maroon","female",wom),("to tow a military aircraft","the team","female",team),
       ("to have enormous jet engines","the aircraft","female",plane)],
      6.0,[("an aircraft",0.13,0.32,"female"),("a jet engine",0.62,0.27,"female"),("a rope",0.85,0.69,"female"),("the tarmac",0.45,0.88,"female")],
      "What are the people doing?","They are dragging an aircraft along the tarmac.","female",
      "defaultVoice female: mixed group, evenId true. Aircraft and team boxes split horizontally at the top of the people's heads (team stands in front of the landing gear). Team target only in the airfield shot; the field shot (sled, car) has the same team but they do not tow the plane there.")
if which==4883:
    w={0.5:(0.03,0.21,0.97,0.79),1.0:(0,0.22,1,0.78),1.5:(0.06,0.26,0.72,0.74),2.0:(0.12,0.24,0.55,0.76),2.5:(0.41,0.31,0.18,0.69),
       3.0:(0.19,0.28,0.62,0.72),3.5:(0,0.26,1,0.74),4.0:(0,0.24,1,0.76),4.5:(0.33,0.29,0.34,0.71),5.0:(0.07,0.27,0.84,0.73),
       5.5:(0,0.23,1,0.77),6.5:(0.40,0.43,0.18,0.57),7.0:(0.32,0.41,0.30,0.59),7.5:(0.21,0.42,0.53,0.54),8.0:(0.21,0.43,0.57,0.45),
       8.5:(0.26,0.42,0.48,0.45),9.0:(0.29,0.44,0.45,0.41)}
    write(4883,"A","reveal","female",
      [("to open two big doors","the woman","female",w),("to smile at the camera","the woman","female",w),
       ("to raise her arms","the woman","female",w)],
      8.0,[("the sky",0.5,0.2,"female"),("a door",0.88,0.30,"female"),("hills",0.2,0.5,"female"),("a woman",0.5,0.62,"female")],
      "What is the woman doing?","She is opening two big doors.","female",
      "Only one person in the clip, so all three phrases use the woman. Frames 0.0 and 6.0 show closed doors only (off).")
