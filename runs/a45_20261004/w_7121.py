from gen_7120_7121_7125_7127_w import K,write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
lh=[(.60,.20,.22,.39)]*8
wave=[(.13,.27,.46,.45),(.12,.23,.47,.49),(.14,.21,.45,.52),(.14,.21,.45,.52),(.12,.24,.47,.49),(.15,.29,.44,.44),(.03,.45,.56,.33),(.03,.47,.56,.31)]
rope=[(.51,.82,.47,.17)]*8
write(7121,{"mediaId":7121,"level":"B","keyWord":"flash","defaultVoice":"male",
"taps":[
 {"phrase":"to send out a powerful beam","target":"the lighthouse","voice":"male","keys":K(T,lh)},
 {"phrase":"to crash against the rocks","target":"the huge wave","voice":"male","keys":K(T,wave)},
 {"phrase":"to lie coiled on the pier","target":"the rope","voice":"male","keys":K(T,rope)}],
"stillS":3.7,
"nouns":[{"word":"a lighthouse","x":0.71,"y":0.35,"voice":"male"},{"word":"a cliff","x":0.37,"y":0.47,"voice":"male"},
 {"word":"rocks","x":0.42,"y":0.68,"voice":"male"},{"word":"a rope","x":0.75,"y":0.94,"voice":"male"}],
"question":"What is the lighthouse doing?",
"answer":["The","lighthouse","is","flashing","in","the","storm."],
"answerVoice":"male",
"notes":"Wave spray overlaps the lighthouse in the picture at 0.2-2.2; boxes split at x=0.60. Wave box after 2.7 holds the falling foam around the rocks. The small marker light also blinks once at 1.7, so 'flash' phrase avoided in taps; the beam phrase fits only the lighthouse. Rope is static, so a state phrase."})
