from gen_6950_6951_6953_6954_lib import write
M=[(0.14,0.30,0.53,0.62),(0.10,0.29,0.55,0.63),(0.10,0.27,0.54,0.69),(0.08,0.27,0.56,0.73)]
D=[(0.75,0.64,0.24,0.15),(0.74,0.63,0.24,0.15),(0.72,0.61,0.24,0.15),(0.68,0.62,0.26,0.15)]
write(6953,"B","clear out","male",[
 ("to carry a mounted moose head","the man in front","male",M),
 ("to rest on a rolled-up rug","the beagle","male",D),
 ("to stride out of the barn","the man in front","male",M)],
 0.2,[("antlers",0.45,0.33,"male"),("a farmhouse",0.86,0.41,"male"),("a beagle",0.87,0.715,"male"),("a chair",0.68,0.80,"male")],
 "What is the man in front doing?","He is clearing out the old barn.","male",
 "Man's box includes the moose head on his shoulder. Background workers are small and not used as targets. Beagle lies on/against the rolled rug.")
