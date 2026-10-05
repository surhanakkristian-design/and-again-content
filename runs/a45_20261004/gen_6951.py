from gen_6950_6951_6953_6954_lib import write
W=[(0.10,0.17,0.80,0.83),(0.09,0.16,0.87,0.84),(0.03,0.15,0.92,0.85),(0.02,0.13,0.98,0.87),(0.0,0.10,1.0,0.90),(0.0,0.10,1.0,0.90),(0.0,0.12,1.0,0.88),(0.0,0.08,1.0,0.92)]
write(6951,"A","cigarette","female",[
 ("to light a cigarette","the woman","female",W),
 ("to blow out smoke","the woman","female",W),
 ("to touch her hair","the woman","female",W)],
 3.2,[("the sky",0.25,0.06,"female"),("a ship",0.82,0.26,"female"),("a cigarette",0.86,0.64,"female"),("a coat",0.12,0.85,"female")],
 "What is the woman doing?","She is smoking a cigarette.","female",
 "Only one clear target (workers are tiny and alike), so all three phrases use the woman. Smoke is visible at 1.7 and 2.7 s.")
