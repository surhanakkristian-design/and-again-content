# STOP es (22 Sept 2026) - judge session s4 invalid after every allowed attempt

Judge packet s4 (245 items) came back with ONE jid missing three times: s4 dropped j68edd and j8f71a (and invented
j8f711), s4_r1 dropped j68edd, s4_r2 (the extra attempt added for pure jid-set misses) dropped j19029. Sessions s1-s3
are valid (s3 on its retry). No labels were built, the set was never frozen or opened, 0 Gemini calls for es.
The es set (partD/set/sentences.jsonl + answers.jsonl) is unopened and can be reused by a later run.
