from lib_5290_5291_5292_5293 import write
W = {0.0:(.24,.43,.74,.57),0.5:(.20,.49,.62,.51),1.0:(.30,.62,.56,.38),1.5:(.57,.80,.40,.20),
     2.5:(.03,.34,.82,.66),3.0:(.04,.38,.88,.62),3.5:(.06,.46,.78,.54),4.0:(.15,.57,.68,.43),4.5:(.38,.86,.48,.14),
     6.0:(.10,.39,.80,.61),6.5:(.11,.47,.87,.53),7.0:(.19,.65,.67,.35),7.5:(.50,.86,.33,.14)}
S = {0.0:(.03,0,.95,.42),0.5:(.03,0,.95,.48),1.0:(.06,0,.90,.61),1.5:(.08,0,.88,.79),2.0:(.02,0,.95,1),
     2.5:(0,0,.88,.33),3.0:(0,0,.92,.37),3.5:(0,0,.88,.45),4.0:(.12,0,.76,.56),4.5:(.15,0,.75,.85),
     5.0:(.12,0,.86,1),5.5:(.18,0,.80,1),6.0:(0,0,1,.38),6.5:(0,0,1,.46),7.0:(.03,0,.95,.64),7.5:(.05,0,.93,.85),
     8.0:(0,0,1,1),8.5:(0,.06,1,.94),9.0:(0,.12,.98,.88)}
write(5290, {"mediaId":5290,"level":"B","keyWord":"skyscraper","defaultVoice":"female",
 "taps":[{"phrase":"to gaze up in amazement","target":"the woman","voice":"female","boxes":W},
         {"phrase":"to swing her long braids","target":"the woman","voice":"female","boxes":W},
         {"phrase":"to rise into the blue sky","target":"the skyscraper","voice":"female","boxes":S}],
 "stillS":0.0,
 "nouns":[{"word":"a skyscraper","x":.50,"y":.20,"voice":"female"},
          {"word":"palm trees","x":.26,"y":.53,"voice":"female"},
          {"word":"bollards","x":.20,"y":.66,"voice":"female"},
          {"word":"a trench coat","x":.55,"y":.82,"voice":"female"}],
 "question":"What is the woman gazing up at?",
 "answer":["She","is","gazing","up","at","a","huge","skyscraper."],
 "answerVoice":"female",
 "notes":"Several towers: the residential tower (0.0-4.5) and the spire tower (5.0-9.0) are both labelled 'the skyscraper'; its box is cut off above the woman's box where she stands in front of it. Woman off at 2.0, 5.0-5.5, 8.0-9.0; only her face at the bottom edge at 1.5, 4.5, 7.5. Braids swing clearly at 2.5-3.5."})
