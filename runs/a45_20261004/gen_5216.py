from gen_5212_5213_5214_5216_lib import build
w = {0.0:(.2,.27,.6,.73),0.5:(.1,.28,.78,.72),1.0:(0,.32,.9,.68),1.5:(0,.29,.93,.71),2.0:(.18,.29,.76,.71),2.5:(.13,.3,.75,.7),
 3.0:(.18,.3,.69,.7),3.5:(.21,.3,.72,.7),4.0:(.45,.31,.31,.69),4.5:(.4,.32,.48,.68),5.0:(.5,.34,.44,.66),5.5:(.49,.33,.44,.62),
 6.0:(.47,.32,.43,.62),6.5:(.41,.33,.53,.62),7.0:(.42,.32,.56,.68),7.5:(.39,.3,.6,.7),8.0:(.34,.31,.5,.62),8.5:(.28,.34,.51,.66),
 9.0:(.26,.36,.51,.64),9.5:(.2,.35,.56,.65),10.0:(.27,.35,.43,.65),10.5:(.22,.33,.69,.67),11.0:(.03,.35,.77,.65),
 11.5:(.28,.36,.56,.64),12.0:(.11,.34,.83,.66)}
s = {6.5:(.01,.32,.2,.16),7.0:(.07,.31,.2,.16),7.5:(.07,.32,.21,.17),8.0:(.01,.33,.2,.16)}
build(5216,'B','stroll','female',[
 ('to touch a crumbling wall','the woman in yellow','female',w),
 ('to stand behind a flower stall','the older woman','female',s),
 ('to spread her arms wide','the woman in yellow','female',w)],
 2.0,[('power lines',.8,.08,'female'),('a lantern',.47,.19,'female'),('a crumbling wall',.15,.6,'female'),('a film camera',.7,.7,'female')],
 'What is she doing on the rooftop?',['She','is','spreading','her','arms','wide.'],'female',
 'Key word "stroll" is not a visible noun, so no pill for it. The older woman is only visible 6.5-8.0 s, a small smiling head behind the white flowers at the left; "stand behind a flower stall" separates her from the woman in yellow, who stands in front of the stall. Man in black T-shirt at 4.0 s ignored (one frame).')
