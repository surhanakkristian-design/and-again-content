# Task: annotate one batch (Sonnet). Budget: 2 tool rounds — read everything in ONE parallel round, write ONE file.
Read in parallel: phase1b/FORMAT_SPEC.md, phase1b/selection/batches/b{N}.jsonl, phase1b/selection/batches/b{N}_lib.txt,
phase1b/synonyms/INDEX.txt. Then write phase1b/annotated/batch_b{N}.json: a JSON array, one compact object per line, one per
input sentence, in the §3 format (keys id,t,lv,v,lk,s,g,o,d,p,m,ng; omit empty keys). Per sentence:
- v[0] = `en` exactly. Add a variant only for a genuinely different construction/word order a learner would write for the
  `sk` sentence (≤3). Never a synonym/article/pronoun swap — use s/d/g/o/p for those.
- lk = `ans` located in each variant.
- s: for EVERY content word or phrase outside the lock that a learner could render differently from the `sk` sentence, map it
  to the best-fitting contextual group from INDEX.txt (same sense!). If none fits and the alternative is common, propose `ng`.
- g/o: only where `sk` does not fix gender (no pronoun, verb form not gendered) or "ju/ho" may be a thing.
- d: where `sk` has no demonstrative/possessive. p: meaning-neutral small words learners add or drop.
- m: 3–8 library items from b{N}_lib.txt that fit this sentence, with the concrete wrong text. ALSO map every Phase 1
  mistake in `p1m` ("text | verdict | kind") to a library item of that verdict (wrong text = the part that differs); if no
  replacement expresses it use [id,"=full wrong sentence"] with the first expansion of its {a|b} slots.
- Be terse; do not deliberate at length per sentence. Never output anything but the file.
