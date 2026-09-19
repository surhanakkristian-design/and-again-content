# Phase 1M — TIP switch decision (label `freeze`)

Taken by the main session BEFORE the new Phase 1M set was opened, on DEV plus the zero-call
readout of `TIP_READOUT.md`; stack F8v2 + F9 off. 0 model calls were made for this decision.

## Readout (zero-call, closed sets)

* `fresh1l` : TIP-reject coverage 194/217 = 89.40 %, FA 12/383 = 3.13 %, type-T 3/130 |
  TIP-accept coverage 203/217 = 93.55 %, FA 30/383 = 7.83 %, type-T 12/130 = 9.23 %
* `dev`     : TIP-reject 182/189, FA 11/301 = 3.65 % | TIP-accept 184/189, FA 28/301 = 9.30 %
* `replay1j`: TIP-reject 182/196, FA 17/294 = 5.78 % | TIP-accept 187/196, FA 35/294 = 11.90 %

## DECISION (verbatim)

DECISION: TIP-as-rejection stays ON (tip_reject = true). Reasoning: the brief's premise was that
after fixing F8 the FA would sit near 1.8 %, leaving room to trade. The readout says otherwise:
accepting TIP buys +9 / +2 / +5 correct answers but lets in +18 / +17 / +18 wrong ones; FA would
be 7.8 % - 11.9 % on all three sides and type-T 9.2 % on fresh1l, i.e. both FA targets would be
lost on the point, not merely on the interval, to gain 4 pp of coverage on one side. With n about
650 wrong answers an FA interval below 5 % needs a point near 3.4 % or lower; only TIP-reject is
compatible with that. Consequence accepted with open eyes: under TIP-reject the closed-set
coverage is 89.4 %, so the coverage target may well be missed again, now decisively. The readout
is a zero-call readout on a closed set, not a measurement.

## F9 OFF — reason on the record

F9 is retired from the frozen stack: the code is kept and its readout is reported, but it does
not decide. With the model present it is redundant (on the 1L fresh side it caught 2 items and
uniquely 0) and it costs coverage (3 correct answers).

## F8 module

`f8v2` alone (not the union `f8u`) — see `F8_UNION_DECISION.md`: the pre-registered adoption rule
failed on (a) union gold ERRORs 20/210 = 9.52 % (bar <= 4/210) and (c) selftest 49/50.
