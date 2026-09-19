Track C (Czech, 0 model calls). Dir: TO/phase1v/trackC. Build a Czech-specific reader (new module,
Slovak reader untouched — prove it: hash of the Slovak reader file before/after, and the Slovak control
gold validation identical before/after). Fix: (1) instrumental -em misread as 1sg; (2) `se` missing from
the reflexive regex; (3) `jestli` misread as an l-participle; (4) Czech aspect lexicon gap (15).
Re-run the 1T Czech gold validation (phase1t/taskB) UNCHANGED: agree / conservative / ERROR per guard,
before and after, Slovak control beside it. No Czech probe, no Czech test set, 0 model calls.
