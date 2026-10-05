# Pre-check 8039 "a way" (phone photo, golden hour), still stills/8039.png
Still inventory: no logos or lettering. Text-like patterns: the woman's Nordic sweater behind the window, small picture frames on the cabin wall, and a pale-blue rectangle at the man's waist. Eyelines in the source: the woman glares sideways towards camera-left; the couple laugh and look out at her. Backups are in precheck_backup/.

## way out (prompts/8039_way_out.txt)
- Predicted failures: (1) The top-left sky survives, so it reads as a trench with a wall, not a tunnel. (2) Turning her head re-renders her face and identity. (3) The window survives. R1 is fine because the cabin, the frames and the sweater are all removed.
- Changed: the whole top of the frame is a snow ceiling and the only sky is through the exit; her body, pose and face stay the same and only her head turns.
- Remaining risk: MEDIUM (a big scene change; the exit must read as the goal; her face may drift).

## to block the way (prompts/8039_to_block_the_way.txt)
- Predicted failures: (1) The geometry contradicted itself: the moose was "between her and the camera, filling the whole trench width" yet "she stays on the right of the moose". The model would either hide her or put the moose beside her, so the path would not be blocked (R7). (2) The husky was in the left of the trench, exactly where the moose goes, so it would be duplicated or lost (R10). (3) The sweater pattern and the picture frames behind the window could turn into lettering (R1/R9). (4) Two moose, or a moose that is too small.
- Changed: there is ONE moose, standing across the trench a few steps ahead of her shovel, from snow wall to snow wall, in the lower half, at least a third of the frame. She stays behind it on the right, with her head and upper body visible above its back. The camera step-back is bounded ("no more than needed"). The same single husky peeks from behind her legs. The sweater and the frames are named as plain.
- Remaining risk: MEDIUM (the occlusion and scale need to land; the couple are small and may warp).

## to lose your way (prompts/8039_to_lose_your_way.txt)
- Predicted failures: (1) "Looking around in a blizzard" reads as "cold" or "snowstorm", not as "lost" (a weak cue, R7). (2) A full background swap drifts her face. (3) Trench remnants read as clearing the way.
- Changed: added a strong lost cue: behind her, her own line of footprints wanders in a loop and crosses itself (walking in circles). The Must NOT list now says "a path, a road, a signpost, vehicle tracks" so it no longer contradicts her own footprints. "Only the surroundings and light change" was added to the keep line.
- Remaining risk: MEDIUM (the footprints may be hidden by the blizzard; the abstract concept relies on her expression).
