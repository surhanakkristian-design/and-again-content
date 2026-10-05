# Pre-check 62 "a bag" (2D TV cartoon), still stills/62.png
Still inventory: no logo/lettering. One visible round placket button on the purple polo reads like the letter "o" (named as a plain button now). The man's face is out of frame above the top edge; only his chin, his shirt and a hand holding the bottle are visible. Backups are in precheck_backup/.

## shopping bag (prompts/62_shopping_bag.txt)
- Predicted failures: (1) "two buttons" does not match the still (only one is visible), so a button could be added or redrawn as a letter. (2) "the man looks down" invites the model to show his face, which changes the framing (R4/R5). (3) A shop logo on the kraft bag (R1/R9).
- Changed: the button is now one plain round button "not a letter"; the eyeline is kept but the face stays out of frame as in the source.
- Remaining risk: LOW (print on the paper bag can be fixed with a free retouch).

## tea bag (prompts/62_tea_bag.txt)
- Predicted failures: (1) The tea bag was "half dipped" in a huge mug, so the mug rim would hide the cue and it reads as "a mug of tea" (R7). (2) Face-in-frame drift as above. (3) Print on the tag or mug. (4) A teapot or a second tea bag being added.
- Changed: the tea bag is lifted just above the rim and fully visible, as big as the mug opening, touching the tea only at one corner, with drops. The face stays out of frame. The button is fixed. Added "a teapot, a second tea bag" to the Must NOT list.
- Remaining risk: MEDIUM (big change: the bag and bottle are removed and a mug is added; the tag may get print, which a retouch can fix).

## to drop a bag (prompts/62_to_drop_a_bag.txt)
- Predicted failures: (1) The keep line ("main object stays large in the lower two thirds") contradicted a bag in mid-air, so the model glues it to the blanket and it reads as "a tipped bag". (2) The "short gap" is too small to see in a close-up. (3) The model keeps the hand holding the bag (reads as packing). (4) A bouncing apple plus a bounce arc adds a second mid-air object and clutter. (5) Face drift.
- Changed: the keep line now allows the bag to be lifted (about half the frame height); there is an explicit visible band of blanket under the bag (a hand's width); the apple now lies on the blanket and the bounce arc is gone; added "a hand holding the bag, a bag resting on the blanket" to Must NOT; the face stays out of frame.
- Remaining risk: MEDIUM-HIGH (mid-air states are a known weak spot; motion lines and the shadow carry it). Not drop-risk.
