# Phase 1M - F8v2 (agent demotion) vs F8v1, offline replay

Label `f8v2-build`. 0 model calls, 0 network, 0 DB. Judge labels are the stored ones
(`dev` / `holdout1j` / `fresh`); `intent` is writer intent, never truth.

F8v2 rule: a Slovak clause with a nominative agent must keep that agent as the subject
of the aligned English clause. Reject on (1) passive clause, (2) it-/wh-cleft,
(3) perspective recast, (4) generic/expletive subject. Everything else abstains.

| side | items | labeled | judged wrong | v1 fired/wrong | v2 fired/wrong | v1 fired/wrong intent V | v2 fired/wrong intent V | v1 COST | v2 COST |
|---|---|---|---|---|---|---|---|---|---|
| dev | 490 | 490 | 301 | 1 | 25 | 0/0 | 0/0 | 0 | 0 |
| replay1j | 490 | 490 | 294 | 0 | 20 | 0/0 | 0/0 | 1 | 0 |
| fresh1l | 600 | 600 | 383 | 23 | 46 | 23/43 | 29/43 | 0 | 0 |
| **total** | | | | 24 | 91 | 23 | 29 | **1** | **0** |

## Cost: guards firing on judged-CORRECT items

* **replay1j C:10107:3602000965** (v1=reject, v2=accept)
  * SK: `Terminál bol prázdny; aj tak ona mala pocit, že ju niekto sleduje.`
  * EN: `The terminal was deserted; nevertheless, she had the feeling someone was watching her.`
  * reason: SK agent "ona" (pron/she) is still the English subject

## The 8 Phase 1L voice false acceptances

| sid | item | intent | type | v1 | v2 | answer |
|---|---|---|---|---|---|---|
| 140006 | 3299777528 | T | T | accept | accept | She is never sending emails after ten in the evening. |
| 140006 | 3100171170 | W | W | accept | accept | She never sends letters after ten in the evening. |
| 140006 | 2667012976 | M | M | accept | accept | She never sends emails in the evening. |
| 140006 | 2996102833 | S | S | accept | reject | They never send emails after ten in the evening. |
| 140006 | 98216243 | V | V | accept | reject | Emails are never sent by her after ten in the evening. |
| 140006 | 2278841645 | TF | T | accept | accept | She never sent emails after ten in the evening. |
| 140014 | 877747763 | T | T | accept | accept | She is working on that thesis for three months. |
| 140014 | 2067027689 | W | W | accept | accept | She has been working on that article for three months. |
| 140014 | 2630403857 | M | M | accept | accept | She has been working on that thesis. |
| 140014 | 2761801588 | S | S | accept | reject | They have been working on that thesis for three months. |
| 140014 | 1487151881 | V | V | accept | reject | That thesis has been worked on by her for three months. |
| 140014 | 3677295634 | TF | T | accept | accept | She worked on that thesis for three months. |
| 140024 | 3157801818 | T | T | accept | accept | He has been fixing that lawnmower all afternoon and finally gave up. |
| 140024 | 3893964095 | W | W | accept | accept | He was fixing that chainsaw all afternoon and in the end he gave up. |
| 140024 | 2714018426 | M | M | accept | abstain | He was fixing that lawnmower all afternoon. |
| 140024 | 831956955 | S | S | accept | reject | They were fixing that lawnmower all afternoon and in the end they gave up. |
| 140024 | 670820885 | V | V | accept | reject | That lawnmower was being repaired by him all afternoon, and in the end he gave up. |
| 140024 | 424977132 | TF | T | accept | accept | He is fixing that lawnmower all afternoon and in the end he gives up. |
| 140037 | 1271826976 | W | W | accept | abstain | We put that carpet together in two hours. |
| 140037 | 4048879004 | M | M | accept | abstain | We put that furniture together. |
| 140037 | 2603321074 | S | S | accept | abstain | They put that furniture together in two hours. |
| 140037 | 1538470541 | V | V | accept | reject | That furniture was assembled by us in two hours. |
| 140037 | 689179285 | TF | T | accept | accept | We will put that furniture together in two hours. |
| 140041 | 661386254 | T | T | accept | accept | We have signed that contract without any changes. |
| 140041 | 1292587313 | W | W | accept | accept | We will sign that contract without any delays. |
| 140041 | 140591788 | M | M | accept | accept | We will sign that contract. |
| 140041 | 271742839 | S | S | accept | reject | They will sign that contract without any changes. |
| 140041 | 1273097874 | V | V | accept | reject | That contract will be signed by us without any changes. |
| 140041 | 2229379120 | TF | T | accept | accept | We signed that contract without any changes. |
| 140058 | 1001426149 | T | T | accept | accept | If we leave earlier, we will not miss that flight. |
| 140058 | 133020611 | W | W | accept | accept | If we had left earlier, we would not have missed that train. |
| 140058 | 845145025 | M | M | accept | accept | If we had left, we would not have missed that flight. |
| 140058 | 1313963202 | S | S | accept | accept | If they had left earlier, they would not have missed that flight. |
| 140058 | 4156271032 | V | V | accept | reject | If we had left earlier, that flight would not have been missed. |
| 140058 | 4124720339 | TF | T | accept | accept | If we left earlier, we would not miss that flight. |
| 140060 | 1056254805 | T | T | accept | accept | He will have solved that problem in a single afternoon. |
| 140060 | 3177856491 | W | W | accept | accept | He would solve that problem in a single morning. |
| 140060 | 4108835030 | M | M | accept | accept | He would solve that problem in an afternoon. |
| 140060 | 2913393374 | S | S | accept | reject | They would solve that problem in a single afternoon. |
| 140060 | 2368276709 | V | V | accept | reject | That problem would be solved by him in a single afternoon. |
| 140060 | 510574810 | TF | T | accept | accept | He solved that problem in a single afternoon. |
| 140064 | 309266963 | T | T | accept | accept | She has moved that wardrobe closer to the window. |
| 140064 | 3355888801 | W | W | accept | accept | She would move that wardrobe closer to the door. |
| 140064 | 1045155915 | M | M | accept | accept | She would move that wardrobe. |
| 140064 | 121245013 | S | S | accept | accept | He would move that wardrobe closer to the window. |
| 140064 | 225979015 | V | V | accept | reject | That wardrobe would be moved closer to the window by her. |
| 140064 | 3626910025 | TF | T | accept | accept | She moved that wardrobe closer to the window. |

Newly caught (v2 rejects, v1 did not): **8 / 8** sids.

## Slovak clause readout on the 8 sids (`sk_clauses`)

* **140006** `Ona nikdy neposiela e-maily po desiatej večer.`
  * [0/main] agent=she - explicit nominative pronoun "ona"
* **140014** `Ona pracuje na tej diplomovke už tri mesiace.`
  * [0/main] agent=she - explicit nominative pronoun "ona"
* **140024** `On opravoval tú kosačku celé popoludnie a nakoniec to vzdal.`
  * [0/main] agent=he - explicit nominative pronoun "on"
  * [1/main] agent=None - no finite verb signal -> abstain
* **140037** `My sme ten nábytok zložili za dve hodiny.`
  * [0/main] agent=we - explicit nominative pronoun "my"
* **140041** `My tú zmluvu podpíšeme bez akýchkoľvek zmien.`
  * [0/main] agent=we - explicit nominative pronoun "my"
* **140058** `Keby sme boli odišli skôr, neboli by sme zmeškali ten let.`
  * [0/sub] agent=None - noun + copula, no agent asserted -> abstain
  * [1/main] agent=we - pro-drop agent from "neboli" (1pl)
* **140060** `On by ten problém vyriešil za jediné popoludnie.`
  * [0/main] agent=he - explicit nominative pronoun "on"
* **140064** `Ona by tú skriňu presunula bližšie k oknu.`
  * [0/main] agent=she - explicit nominative pronoun "ona"

selftest: PASS (43 cases)

