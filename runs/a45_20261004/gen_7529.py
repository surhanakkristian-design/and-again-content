from gen_7502_7529_7738_7740_lib import write
yacht={0.2:(0.30,0.28,0.35,0.54),0.7:(0.25,0.27,0.33,0.54),1.2:(0.15,0.32,0.20,0.38),1.7:(0.65,0.05,0.35,0.80),
       2.2:(0.38,0.0,0.62,0.82),2.7:(0.19,0.0,0.81,0.82),3.2:(0.0,0.0,1.0,0.90),3.7:(0.0,0.0,1.0,0.90)}
buoy={0.2:(0.66,0.28,0.34,0.66),0.7:(0.59,0.27,0.41,0.63),1.2:(0.36,0.27,0.52,0.62),1.7:(0.11,0.29,0.53,0.56),
      2.2:(0.0,0.27,0.37,0.54),2.7:(0.0,0.27,0.18,0.45)}
write(7529,"B","round","female",[
 ("to round a huge buoy","the yacht","female",yacht),
 ("to kick up spray","the yacht","female",yacht),
 ("to bob on the rough sea","the orange buoy","female",buoy)],
 2.2,[("a buoy",0.18,0.42,"female"),("a sail",0.84,0.20,"female"),("a hull",0.62,0.70,"female"),("waves",0.45,0.90,"female")],
 "What is the yacht doing?","It is rounding a huge buoy.","female",
 "Targets yacht + buoy only: the crew sit on the yacht, so a crew target would overlap the yacht box. Yacht box is the boat incl. crew; at 1.2 the buoy hides the middle, yacht box = the crew/hull part left of the buoy (the bow right of the buoy is left out). Buoy at 2.7 is a thin sliver at the left edge (min width 0.18 cuts a bit of the crew), off at 3.2-3.7. 'to bob' is the weakest phrase (the yacht also moves on the sea, but it sails/races). defaultVoice female = the woman in red is the main person.")
