from gen_7502_7529_7738_7740_lib import write
ref={0.2:(0.33,0.27,0.30,0.73),0.7:(0.25,0.27,0.60,0.73),1.2:(0.19,0.28,0.81,0.72),1.7:(0.0,0.30,1.0,0.70),
     2.2:(0.0,0.27,1.0,0.73),2.7:(0.0,0.27,1.0,0.73),3.2:(0.0,0.28,1.0,0.72),3.7:(0.0,0.28,1.0,0.72)}
box={0.2:(0.0,0.16,0.32,0.84),0.7:(0.0,0.15,0.24,0.85),1.2:(0.0,0.15,0.18,0.80)}
write(7502,"B","referee","male",[
 ("to separate the two boxers","the referee","male",ref),
 ("to stretch out both arms","the referee","male",ref),
 ("to wear brown boxing gloves","the boxer with brown gloves","male",box)],
 2.2,[("a referee",0.40,0.55,"male"),("spectators",0.78,0.35,"male"),("ropes",0.78,0.645,"male")],
 "What is the referee doing?","He is separating the two boxers.","male",
 "Two phrases share the referee (clip shows only him from 1.7). Boxer with brown gloves is the left boxer, visible 0.2-1.2 only; at 0.2/0.7 his box is split from the referee's along the referee's hand. Referee box spans the full width from 1.7 because his arms reach both edges. 'a referee' is a male person -> male voice.")
