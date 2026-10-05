from gen_5212_5213_5214_5216_lib import build
w = {0.0:(0,.12,1,.88),0.5:(0,.28,.9,.72),1.0:(0,.29,.98,.71),1.5:(0,.28,.97,.72),2.0:(.02,.26,.98,.74),2.5:(0,.27,.98,.73),
 3.0:(0,.27,1,.73),3.5:(0,.27,1,.73),4.0:(.36,.16,.42,.46),4.5:(.37,.17,.4,.45),5.0:(.37,.19,.36,.45),5.5:(.38,.2,.34,.46),
 6.0:(.36,.17,.43,.49),6.5:(.21,.14,.43,.58),7.0:(.2,.15,.57,.56),7.5:(.26,.13,.47,.6),8.0:(.24,.08,.52,.66),
 8.5:(.2,.33,.56,.45),9.0:(.18,.32,.55,.46),9.5:(.13,.3,.69,.54),10.0:(.15,.29,.77,.62),10.5:(.11,.28,.85,.66),
 11.0:(.05,.26,.82,.7),11.5:(.09,.26,.85,.68),12.0:(.15,.22,.82,.7)}
build(5214,'A','desert','female',[
 ('to ride a scooter','the woman','female',w),
 ('to sit on a camel','the woman','female',w),
 ('to smile at the camera','the woman','female',w)],
 10.0,[('the sun',.75,.13,'female'),('a woman',.5,.35,'female'),('camels',.25,.44,'female'),('a desert',.8,.5,'female')],
 'What is she doing in the desert?',['She','is','sitting','on','a','camel.'],'female',
 'Only one usable target: other cyclists ride bikes too (so no "ride a bike"), the far camels may carry riders and are tiny, so all three phrases use the red-haired woman (same keys). Box covers almost the whole frame in the close bike shots 0-3.5 s. "a desert" pill sits on the dunes right of her; "camels" = the line of camels far behind.')
