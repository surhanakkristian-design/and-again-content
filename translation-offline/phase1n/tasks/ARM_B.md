# Arm B — the Slovak subject-pronoun convention (frozen since Phase 1j, used for every Phase 1k sentence)

## Definition, verbatim

`phase1k/CONTEXT_1K.md` lines 91-92:

> - **Arm B is frozen**: explicit subject pronoun wherever Slovak would drop it; no `g` chain when the
>   pronoun is stated. Every fresh sentence follows it (noun-subject sentences stay as they are).

`phase1k/fresh/make_fresh.py` lines 10-11 (the sentence writer's own statement):

> Arm-B convention: an explicit subject pronoun wherever Slovak would drop the subject; noun subjects
> stay as they are; no `g` chain anywhere (the pronoun states the gender).

`phase1k/HANDOFF_P.md` lines 8-9:

> sids **140001..140070** … arm-B form (explicit subject
> pronoun wherever Slovak would drop it; noun subjects untouched)

## What it inserts

A subject **personal pronoun** (ja / ty / on / ona / my / vy / oni) in front of a finite verb whose
subject Slovak would normally leave implicit in the verb ending:

- Ona každé ráno pije zelený čaj s medom.
- On práve teraz umýva staré tenisky v dreze.
- Ty teraz držíš môj dáždnik a ja mrznem.
- My chodíme do tej pekárne každú sobotu ráno.
- Oni už dve hodiny čakajú na autobus pred knižnicou.
- Ja rád varím cestoviny pre celú rodinu.
- Ty musíš odovzdať ten formulár ešte dnes popoludní.

## What it does NOT insert

- It does not touch a sentence that already has a **noun** subject — those stay exactly as they are:
  - Moja sestra nosí okuliare iba pri čítaní.
  - Tento vlak zastavuje v každej malej dedine.
  - Sused, ktorý býva nad nami, opravuje bicykle v garáži.
- It does not add a subject to a Slovak sentence that is genuinely impersonal or passive, and it does
  not turn such a sentence into a personal one: the Phase 1k set deliberately kept 6 impersonal and
  5 passive Slovak sentences in their own form.
- It changes nothing else: no word order beyond placing the pronoun, no added emphasis particles, no
  change of verb, aspect, tense or lexis.
