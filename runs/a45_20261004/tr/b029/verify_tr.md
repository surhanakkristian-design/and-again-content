# b029 tr verify

Texts checked: 899 (100 videos: 300 phrases, 399 nouns, 100 questions, 100 answers). Fixes: 13. tr_check.py: ok 100 videos.

## Fixes
- 7772 phrases[2]: "iki eliyle el kol hareketi yapmak" -> "iki eliyle işaret etmek" (redundant "eliyle el kol", unnatural)
- 7774 phrases[0]: "bir kavanoz bozuk parayı boşaltmak" -> "bozuk para dolu bir kavanozu boşaltmak" (the jar is emptied, not "a jar of coins" as object)
- 7774 answer: "Bir kavanoz bozuk parayı boşaltıyor." -> "Bozuk para dolu bir kavanozu boşaltıyor." (same fix, consistency with phrase)
- 7777 phrases[1]: "bir donut almak" -> "eline bir donut almak" ("almak" alone reads as "buy"; pick up)
- 7781 answer: "Tilki çadıra çok yakın." -> "Tilki çadıra yakın." ("çok" added meaning not in English)
- 7804 phrases[1]: "kollarını havaya fırlatmak" -> "kollarını havaya kaldırmak" ("fırlatmak" = throw an object; unnatural for arms)
- 7821 nouns[3]: "balıkçı şapka" -> "balıkçı şapkası" (compound noun needs the -sı suffix)
- 7834 answer: "Gözleri kapalı bir şekilde ..." -> "Gözleri kapalı halde ..." (clumsy calque "bir şekilde")
- 7863 phrases[0]: "bariyerin üstünden tırmanmak" -> "bariyerin üstünden tırmanıp geçmek" (climb over = cross it)
- 7865 phrases[2]: "parlak bir şekilde yanmak" -> "parlak alevlerle yanmak" (calque of "brightly")
- 7872 phrases[0]: "üstüne uymayan bir takım elbise giymek" -> "üstüne oturmayan bir takım elbise giymek" (ill-fitting = "üstüne oturmayan")
- 7872 answer: "Üstüne uymayan ..." -> "Üstüne oturmayan ..." (same, consistency)
- 7874 phrases[1]: "elinin arkasında kıkırdamak" -> "eliyle ağzını kapatıp kıkırdamak" (literal calque of "behind her hand" is not Turkish)

## Doubts left unchanged
- 7779 phrases[1] "suyu tencereyle tutmak" (catch water in a saucepan): acceptable; "suyu tencereye toplamak" is an alternative.
- 7831 phrases[2] "eliyle yüzünü kapatıp utançtan büzülmek": slightly expanded rendering of "cringe behind her hand", kept as natural Turkish.
- 7874 phrases[0] "duvar resmine yaslanmak" (press against the mural): "yaslanmak" leans toward "lean"; answer uses "Elini duvar resmine bastırıyor" which matches the clip.
- 7856 phrases[1] "dudaklarını yalamak" for a dog, phrases[2] "yüzünü gömmek" without a location, mirrors the English.
- 7798 nouns "ip ışıklar" for string lights; "ışık zinciri" also used.
