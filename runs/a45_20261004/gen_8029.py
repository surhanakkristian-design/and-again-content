from gen_8024_8025_8026_8029_lib import build
PW = [(.57,.12,.31,.27),(.57,.12,.31,.27),(.57,.12,.31,.27),(.57,.12,.32,.27),(.57,.11,.32,.28),(.57,.11,.31,.28),(.59,.10,.35,.29),(.59,.10,.35,.29)]
MW = [(.55,.40,.45,.15),(.56,.40,.44,.15),(.56,.40,.44,.15),(.56,.40,.44,.15),(.51,.40,.49,.15),(.47,.40,.53,.15),(.47,.40,.53,.15),(.59,.40,.41,.15)]
BH = [(0,.56,1,.44),(0,.58,1,.42),(0,.58,1,.42),(0,.60,1,.40),(0,.62,1,.38),(0,.62,1,.38),(0,.63,1,.37),(0,.56,1,.44)]
M='male'; F='female'
build(8029,'B','total',M,[
 ('to cheer with raised arms','the woman in pink',F,PW),
 ('to chip in with coins','the man in the white T-shirt',M,MW),
 ('to gather up the cash','the hands in blue sleeves',M,BH)],
 2.7,[('a paper lantern',.50,.05,M),('cooks',.14,.24,M),('banknotes',.45,.62,M),('coins',.60,.72,M)],
 'What is the woman in pink doing?','She is cheering with raised arms.',M,
 'POV hands (blue sleeves) have no visible gender -> defaultVoice male (evenId false). Pink woman and man in white overlap: split horizontally at y .39/.40, so his head top (.31-.39) lies in her box; his box stops at y .55 because the blue hands start below (his lower torso cut). The rust-jumper woman is not a target: her laying down a note overlaps with the blue hands pushing notes. "gather up the cash" is clearest at 3.7 (at 0.2-1.2 the hands push notes onto the pile).')
