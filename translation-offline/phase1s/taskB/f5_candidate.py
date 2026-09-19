#!/usr/bin/env python3
"""Phase 1S / Task B1 - CANDIDATE only. NOT applied anywhere. 0 model calls.

The frozen F5 (phase1i/checker_1i.f5_adjunct_deletion) is NOT modified and NOT imported-and-patched
in place: this file re-implements only span_information() with an extra English stop set, and the
replay harness calls the frozen f5 with span_information swapped for the duration of the replay.

Design note: the stop set is applied INSIDE span_information (classification), never inside
optional_tokens/_subseq_positions (matching). Consequence: the candidate can only ever RELEASE an
item that the frozen F5 rejected; it can never create a new rejection, because the subsequence test
and the span segmentation are byte-identical to the frozen ones.
"""

# English renderings of the disputed Slovak particles. F5 never sees Slovak - it compares the
# learner's English answer with the English reference - so a "Slovak function-word stoplist" is
# impossible; the stoplist has to be on the English side.
STOP_A = {            # prave, aj   (owner has NOT disputed these: judge called them function words)
    'also', 'too', 'well',            # aj  -> also / too / as well
    'very', 'precisely', 'exactly',   # prave -> this very / precisely this / exactly this
}
STOP_B_EXTRA = {      # konecne, vtedy, az   (OPEN BOUNDARY - owner has not decided these)
    'finally',                        # konecne
    'then', 'back', 'time', 'moment', # vtedy -> back then / at the time / at that moment
    'only', 'until',                  # az    -> only when / not until
}
STOP_B = STOP_A | STOP_B_EXTRA


def make_span_information(C, stop):
    """Returns a span_information() that is the frozen one plus `stop` treated as non-informative."""
    def span_information(span, opt, postdash_start):
        eff = [t for _p, t in span if t not in opt and t not in stop]
        if not eff:
            return None
        if any(p >= postdash_start for p, _t in span):
            return 'clause after the dash dropped (%s)' % ' '.join(eff[:6])
        if all(t in C.NONINFO for t in eff):
            return None
        content = [t for t in eff if t not in C.FUNCTION]
        if content:
            return 'content word(s) %s' % ' '.join(content[:4])
        if eff[0] in C.PREP_HEADS and len(eff) > 1:
            return 'prepositional phrase %s' % ' '.join(eff[:5])
        if any(t in C.PARTICLES for t in eff):
            return 'verb particle / directional %s' % ' '.join(eff[:4])
        if any(t in C.INFO_FUNC for t in eff):
            return 'adjunct adverb %s' % ' '.join(eff[:4])
        return None
    return span_information
