# Pre-check 8055 "a balloon" (pen-and-ink hatched drawing on white), still stills/8055.png
Still inventory: no lettering, signature or watermark. The man's face is a blank oval with no features. Backups are in precheck_backup/.
Shared risk: the template line "every figure stands or sits with visible contact" contradicts a man hanging from a string. Adding facial features breaks R8.

## water balloon (prompts/8055_water_balloon.txt)
- Predicted failures: (1) Drops "from the knot (top) onto his shoes" are physically wrong and confuse the model. (2) Head-tilt eyeline invites a drawn face (R8). (3) In ink it may read as a plain balloon or a sack.
- Changed: drops run down its skin and drip from the bottom; the face stays a blank oval. The wavy water line, the sagging teardrop shape and the puddle are kept.
- Remaining risk: MEDIUM (water is hard to show in line art).

## balloon animal (prompts/8055_balloon_animal.txt)
- Predicted failures: (1) The template contact line contradicts the hanging man. (2) A real or furry dog. (3) The hot-air balloon is kept and a dog is added (two balloons). (4) A face is drawn.
- Changed: the man is exempt from the contact line because he hangs as in the source; the dog is "clearly a toy of twisted balloons, never a real or furry dog, only one"; the face stays blank.
- Remaining risk: LOW-MEDIUM.

## to blow up a balloon (prompts/8055_to_blow_up_a_balloon.txt)
- Predicted failures: (1) "Eyes squeezed shut" contradicts the keep line ("blank face oval") and adds features (R8). (2) The man stands on nothing (R10 floating). (3) A half-inflated balloon with any shine may read as a water balloon (sibling).
- Changed: the puffed cheek is shown only through the profile outline and the face stays featureless; there is a hatched ground line; the balloon is "plain, clearly empty of water". The R4 change (bigger, knees-up) was already bounded.
- Remaining risk: MEDIUM (contact between the hands, the mouth and the balloon neck on a blank-faced figure).

## to pop a balloon (prompts/8055_to_pop_a_balloon.txt)
- Predicted failures: (1) A sparrow sitting on a scrap of a bursting balloon is physically incoherent; the model often draws an intact balloon with a bird (no burst, so the cue fails). (2) "Free arm over his head" left no agent. (3) Onomatopoeia lettering in the burst (R9). (4) An intact outline survives.
- Changed: the bird is replaced by the man's own other hand holding a long sewing pin at the tear (a clear agent for "to pop"), and "a bird" was added to Must NOT. He flinches, leaning back, with a blank face. "No round intact outline remains" was added. The ban on "POP"/lettering is kept.
- Remaining risk: MEDIUM (the pin is small, but the burst star carries the cue; a stray mark can be retouched).
