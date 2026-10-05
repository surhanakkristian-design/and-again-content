import json
from gen_5208_5209_5210_5211_lib import build
times=json.load(open("frames/5209/info.json"))["times"]
worker={0.0:(0,0,1,1),0.5:(0,.14,1,.86),1.0:(0,.17,1,.83),1.5:(0,.17,1,.83)}
lounger={4.0:(0,.33,1,.67),4.5:(0,.33,1,.67),5.0:(0,.32,1,.68),5.5:(0,.25,1,.75),6.0:(0,.32,1,.68)}
grass={6.5:(0,.55,.95,.29),7.0:(0,.61,1,.23),7.5:(0,.61,1,.23),8.0:(0,.61,1,.23)}
build(5209,"B","lounge","male",[
 ("to collapse onto a sofa","the worker","male",worker),
 ("to sip an iced drink","the man under the umbrella","male",lounger),
 ("to lie flat on the grass","the man in the field","male",grass)],
 10.0,[("the sun",.62,.37,"male"),("the sea",.20,.47,"male"),("a hammock",.15,.69,"male"),("sand",.84,.88,"male")],
 "What is the woman at sunset doing?",["She","is","lounging","in","a","hammock."],"female",
 "Five separate shots, one person each, so every target is visible only in its own shot. The drink on the lounger is a glass with ice (description says can). Two hammock women: question names the one on the beach at sunset (8.5-10.0); the first woman's hammock hangs over grass under palms, not a beach. defaultVoice male (mixed group, evenId false).",times)
