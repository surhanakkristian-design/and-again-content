from lib_7884_7887_7888_7889 import build
W = [(0,.43,.47,.29),(0,.43,.46,.29),(0,.43,.45,.29),(0,.42,.47,.31),(0,.43,.47,.29),(0,.42,.46,.30),(0,.42,.47,.31),(0,.41,.46,.32)]
H = [(.47,.38,.28,.17),(.46,.34,.29,.21),(.45,.38,.31,.18),(.47,.39,.30,.17),(.48,.40,.29,.16),(.48,.40,.29,.16),(.48,.39,.31,.18),(.48,.37,.31,.19)]
M = [(.76,.27,.24,.50),(.77,.28,.23,.47),(.78,.28,.22,.46),(.80,.28,.20,.44),(.81,.25,.19,.46),(.81,.23,.19,.48),(.82,.23,.18,.48),(.82,.22,.18,.48)]
build(7887,'B','laying','female',[
 ('to catch a freshly laid egg','the woman','female',W),
 ('to flap its wings','the hen','female',H),
 ('to drop a laundry bag','the man','male',M)],
 2.2,[('a paper lantern',.36,.07,'female'),('a hen',.63,.46,'female'),('a laundry basket',.60,.67,'female'),('a bedspread',.40,.85,'female')],
 'What is the woman holding?',['She','is','holding','a','freshly','laid','egg.'],'female',
 'Woman box cut at x .47 so it does not overlap the hen (her hands reach under the basket at 0.2-1.2). Hen flaps at 0.7-1.2. Man drops the bag at ~1.5 (on the floor at 1.7).')
