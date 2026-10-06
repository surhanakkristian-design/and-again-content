# verify tr (b002, de)

Texts checked: 1307 (100 videos: phrases, nouns, question, answer, recall). Checker: `tr_check57.py b002 de tr` ok, 100 ids.

## Fixes (7 changes, 10 cells)
- 596 answer: "Sarılı kadın koşucu yarışı kazanıyor." -> "Sarı giyen kadın koşucu yarışı kazanıyor." (why: "sarılı" reads as "wrapped/hugged", ambiguous)
- 278 phrases[0] + recall[0]: "ağaçların tepesinin üzerinden doğmak" -> "ağaç tepelerinin üzerinden doğmak" (why: Baumkronen plural, natural compound)
- 5712 phrases[1] + recall[1]: "bir kâğıt yaprağını düşürmek" -> "bir kâğıt yaprağı düşürmek" (why: indefinite object takes no accusative)
- 4156 nouns[0]: "çalı çit" -> "çalı çiti" (why: noun compound needs -i)
- 6820 phrases[1] + recall[1]: "paytak paytak yürümek" -> "tıpış tıpış yürümek" (why: hertrotten = small quick steps, paytak = waddling)
- 7813 nouns[0]: "şemsiyeler" -> "güneş şemsiyeleri" (why: Sonnenschirme = sun umbrellas)
- 4920 nouns[3]: "yükseltilmiş bahçe yatağı" -> "yükseltilmiş tarh" (why: "bahçe yatağı" is a calque; tarh is the Turkish term)

## Doubts left unchanged
- 5499 "sokak boyunca koşmak" for "durch die Straße joggen": "sokakta koşu yapmak" would be closer to jogging; current is acceptable.
- 4125 "taç yapraklarına dağılmak" for "in Blütenblätter zerfallen": understandable, slightly stiff.
- 376 "hızlı akıntılar" for Stromschnellen: technical term is "ivinti", kept the plainer wording for learners.
- 7962/7849 "ışık zinciri" for Lichterkette: calque but in common commercial use.
- "Beyazlı/Mavili" (5149, 7932, 7845): colloquial but natural; kept.
