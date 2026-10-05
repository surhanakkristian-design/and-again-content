from lib_5658_5659_5662_5663 import write
chef=[(0,.27,.43,1),(0,.27,.43,1),(0,.26,.43,1),(0,.26,.44,1),(0,.25,.43,1),(0,.25,.43,1),(0,.25,.47,1),(0,.25,.45,1)]
cook=[(.45,.30,.96,.99),(.45,.30,.97,.99),(.45,.30,.98,.99),(.46,.30,.99,.99),(.44,.26,1,.99),(.46,.26,1,.99),(.48,.28,1,.99),(.58,.30,1,.99)]
write(5658,"B","blessing","male",[
 ("to lean against the counter","the chef in white","male",chef),
 ("to punch the air with joy","the cook in the apron","male",cook),
 ("to push the plate forward","the chef in white","male",chef)],
 2.2,[("wall tiles",.30,.24,"male"),("saucepans",.45,.36,"male"),("a plate",.50,.64,"male"),("an apron",.78,.75,"male")],
 "What is the cook in blue doing?",["He","is","punching","the","air","with","joy."],"male",
 "Two men: chef in white jacket (left, leans on counter, nudges the plate at 3.2-3.7) and cook in navy apron (right, fists up until 3.2, clasps hands at 3.7). 'to push the plate forward' is a small hand movement at 3.2-3.7 only. Boxes split at x~0.45-0.47 at 3.2 where the chef's hand reaches the plate.")
