# A56 blind caption test
You see picture cards of one or more words. For each word folder you are given, open card_1.jpg, card_2.jpg, card_3.jpg
(Read them) and assign each of the word's three captions to exactly one card (a one-to-one match), the way a learner would
at first glance. Do NOT open any *_key.json file or any other folder. Write `blind/<round>_answer.json`:
{"<word id>": {"card_1": "<caption>", "card_2": "<caption>", "card_3": "<caption>", "confidence": {"card_1": "high|medium|low", ...}}, ...}
Reply with one line per word: id and the three assignments. Nothing else.
