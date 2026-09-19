# Task A — movement of the 119 judged-correct type-M answers (Phase 1R)

One blind re-judge, 0 model calls in this scoring step. Packet: `phase1r/taskA/judge/verdicts.json`; key: `phase1r/taskA/_key.json`; buckets from `phase1q/taskA/triage.json`.

## Tally

- Items in the packet: 119 (116 M2 + 3 M1 hidden controls).
- Judge classes: content 118, function 1. Judge verdicts: wrong 118, correct 1. Borderline: 10.
- **Of the 116 M2: 116 move to WRONG, 0 stay CORRECT.**
- Borderline among the movers: 7.

## The 3 M1 hidden controls (owner's rule keeps them CORRECT)

| jid | iid | judge verdict | class | dropped | Slovak | answer |
| --- | --- | --- | --- | --- | --- | --- |
| J020 | W:170116:w4 | correct | function | Práve = this very (emphatic); aj = also/even | Práve táto poisťovňa pokrýva aj škody spôsobené vetrom. | This insurance company covers damage caused by wind. |
| J039 | W:170107:w4 | wrong | content | Až = only when; konečne = finally | Až keď technici vymenili server, stránka konečne prestala padať. | When the technicians replaced the server, the website stopped crashing. |
| J063 | W:170110:w4 | wrong | content | Vtedy = back then | Vtedy sme si my ani neuvedomili, ako veľmi nám tá zmena pomohla. | We did not even realise how much that change had helped us. |

**Control disagreement: the judge called 2 of the 3 M1 controls "wrong".** Reported plainly; these items are NOT moved in the primary score (owner's rule). They are moved only in sensitivity variant S1.

## M2 stayers (0)

| jid | iid | class | dropped | Slovak | answer | note |
| --- | --- | --- | --- | --- | --- | --- |

## 10 movers (first by jid, not cherry-picked)

| jid | Slovak | answer | dropped | borderline |
| --- | --- | --- | --- | --- |
| J001 | On beží každý deň okolo jazera. | He runs every day. | okolo jazera = around the lake | False |
| J002 | Búrka minulý týždeň poškodila strechu telocvične a vyvrátila dva stromy. | Last week the storm damaged the roof of the gym. | a vyvrátila dva stromy = and knocked down two trees | False |
| J003 | Môj otec opravuje starý nábytok vo svojej dielni. | Old furniture is repaired. | Môj otec = my father; vo svojej dielni = in his workshop | False |
| J004 | Hoci firma sľubuje rýchle dodanie, zákazníci čakajú na objednávky aj tri týždne. | Customers wait up to three weeks for their orders. | Hoci firma sľubuje rýchle dodanie = although the company promises fast delivery | False |
| J005 | Ak vláda schváli tú novelu, úrady zrušia poplatky za výpisy. | The authorities will abolish the fees for extracts. | Ak vláda schváli tú novelu = if the government approves that amendment | False |
| J006 | Otec mi povedal, že on zamkol garáž ešte pred obedom. | My father told me that he had locked the garage. | ešte pred obedom = before lunch | False |
| J007 | Keby si Lucia bola prečítala pokyny, nebola by pokazila celú tabuľku. | If Lucia had read the instructions, she would not have ruined the spreadsheet. | celú = whole | True |
| J008 | Sestra fotí kvety v záhrade. | My sister is photographing the flowers. | v záhrade = in the garden | False |
| J009 | Manažér priznal, že tím podcenil prípravu na tú prezentáciu. | The manager admitted that the team had underestimated the preparation. | na tú prezentáciu = for that presentation | False |
| J010 | Oni zavreli obchod o šiestej večer. | They closed the shop. | o šiestej večer = at six in the evening | False |

## Resulting label totals

| | before | after (primary) |
| --- | --- | --- |
| judged correct | 599 | 483 |
| judged wrong | 481 | 597 |
| of which wrong_type M | 10 | 126 |

Sensitivity variants used in Task B: **S1** = follow the blind judge on all 119 (M1 controls included, 118 flipped); **S2** = borderline movers stay correct (109 flipped).
