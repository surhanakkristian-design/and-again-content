# Phase 1S / Task B1 - F5 and the M1 rule (sizing only, NOT applied)

0 model calls. Frozen F5 untouched; candidate in `f5_candidate.py`.

## Replay fidelity
Replay of the frozen F5 over all 1,080 1P items fires on 72; the 67 recorded F5-layer rejections are reproduced exactly (0 missed) and the 5 extra are precisely the 5 items F3 preempts. Labels = 1Q judged with the 116 M2 movers set to wrong.

## Mechanism
F5 never sees Slovak. It compares the learner's ENGLISH answer against the English reference/variants; there is no Slovak stoplist, so `prave/aj/konecne/vtedy/az` are never classified at all - their ENGLISH renderings are. `span_information()` classifies a dropped span: articles+item-optional tokens are stripped, an all-NONINFO span is free, then any token outside FUNCTION = 'content word(s)'; FUNCTION contains ADVERBS+PARTICLES but not `also`; and the last branch fires on any INFO_FUNC token ('adjunct adverb'), and INFO_FUNC contains every ADVERB (finally, already, just, even, only...), so a pure function-word drop still fires.

### The two F5-rejected M1 items

- `W:170116:w4` (Prave tato poistovna pokryva aj skody...): dropped span `that also` vs variant 1 -> `content word(s) also`. `also` is in neither FUNCTION nor NONINFO nor INFO_FUNC, so F5 calls it a CONTENT word.

- `W:170110:w4` (Vtedy sme si my ani neuvedomili...): dropped span `at time` vs variant 1 ('At the time we did not...') -> `content word(s) time`. `the` is an article and free, `at` is FUNCTION, but the noun `time` is content, so the deictic adverb `vtedy` is rejected as a dropped noun.

- `W:170107:w4` was NOT rejected by F5 (the answer is not a subsequence of either variant: `stopped crashing` vs `did ... finally stop crashing`). It reached L3 and the stored row says only `model: DIFF`, main_verdict wrong - no textual model reason is stored, so the cause cannot be read from the data.


## Sizing (all 67 F5 rejections replayed)

| variant | stop set (English) | released of 67 | released labelled CORRECT (gain) | released labelled WRONG (cost) | new fires created |
|---|---|---|---|---|---|
| a_prave_aj | also exactly precisely too very well | 1 | 1 | 0 | 0 |
| b_plus_konecne_vtedy_az | also back exactly finally moment only precisely then time too until very well | 1 | 1 | 0 | 0 |

### Per-token
| token | releases | of which correct | of which wrong |
|---|---|---|---|
| also | 1 | 1 | 0 |
| back | 0 | 0 | 0 |
| exactly | 0 | 0 | 0 |
| finally | 0 | 0 | 0 |
| moment | 0 | 0 | 0 |
| only | 0 | 0 | 0 |
| precisely | 0 | 0 | 0 |
| then | 0 | 0 | 0 |
| time | 0 | 0 | 0 |
| too | 0 | 0 | 0 |
| until | 0 | 0 | 0 |
| very | 0 | 0 | 0 |
| well | 0 | 0 | 0 |

### Released items

- a_prave_aj [W:170116:w4] label_1R=correct deleted=`that also` frozen_why=`content word(s) also` answer=This insurance company covers damage caused by wind.
- b_plus_konecne_vtedy_az [W:170116:w4] label_1R=correct deleted=`that also` frozen_why=`content word(s) also` answer=This insurance company covers damage caused by wind.

Items F5 releases do NOT become accepted: they fall through to L3, whose verdict for them was never stored (F5 short-circuits before the model call). That number is stated below and no call is made on it.
