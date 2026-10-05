from gen_7328_7329_7332_7334_lib import write
S=[0.67,0.68,0.69,0.73,0.70,0.71,0.72,0.75]
L=[0.25,0.26,0.26,0.22,0.20,0.20,0.18,0.15]
TOP=[0.37,0.38,0.29,0.31,0.26,0.21,0.28,0.23]
BOT=[0.91,0.93,0.96,0.97,0.84,0.83,0.86,0.89]
DY=[(0.60,0.77),(0.62,0.78),(0.60,0.77),(0.56,0.70),(0.51,0.66),(0.48,0.62),(0.47,0.64),(0.44,0.62)]
woman=[(l,t,round(s-l,2),round(b-t,2)) for l,t,b,s in zip(L,TOP,BOT,S)]
dog=[(s,y0,0.19,round(y1-y0,2)) for s,(y0,y1) in zip(S,DY)]
write(7334,"B","maple","female",[
 ("to catch a skateboard deck","the woman","female",woman),
 ("to stroke the smooth deck","the woman","female",woman),
 ("to doze under the workbench","the dog","female",dog)],
 0.2,[("maple",0.57,0.12,"female"),("a mug",0.84,0.45,"female"),("a dog",0.72,0.69,"female"),("sawdust",0.50,0.90,"female")],
 "What is the woman doing?","She is stroking the maple deck.","female",
 "Only two targets: woman x2, dog x1. Dog lies right next to her knee / the deck she holds, so boxes are split at a vertical line; the dog's left part falls in the woman's box at 1.2-3.7 s. 'maple' pill sits on the falling deck at 0.2 s (that the wood is maple comes from the description, not provable from the picture). The answer is true from about 2.2 s on.")
