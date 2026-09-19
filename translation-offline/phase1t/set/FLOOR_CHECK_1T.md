# FLOOR_CHECK_1T — judged-label floors before the run (0 model calls)

- items 900 · labelled 900 · unlabelled 0
- verdict: **FLOORS PASS**

## floors

| floor | required | got | ok |
| --- | ---: | ---: | --- |
| F1_agentdrop_any_wrong | 120 | 161 | yes |
| F2_agentdrop_embedded_wrong | 60 | 96 | yes |
| F3_timeframe_wrong | 100 | 119 | yes |
| F4_by_passive_correct | 60 | 80 | yes |
| F4_bypassive_correct | 60 | 80 | yes |
| F5_skp_correct | 40 | 81 | yes |

## judged-wrong types (T/W/M/S)

| scope | T | W | M | S | ? |
| --- | ---: | ---: | ---: | ---: | ---: |
| all | 119 | 72 | 209 | 79 | 0 |
| half:P1 | 60 | 38 | 102 | 40 | 0 |
| half:P2 | 59 | 34 | 107 | 39 | 0 |
| level:A1 | 30 | 33 | 38 | 21 | 0 |
| level:A2 | 30 | 21 | 49 | 20 | 0 |
| level:B1 | 30 | 9 | 61 | 18 | 0 |
| level:B2 | 29 | 9 | 61 | 20 | 0 |

## writer intent x judged

| scope | cell | n |
| --- | --- | ---: |
| all | C/correct | 399 |
| all | C/wrong:S | 1 |
| all | M/wrong:M | 209 |
| all | S/correct | 21 |
| all | S/wrong:S | 78 |
| all | S/wrong:W | 1 |
| all | T/correct | 1 |
| all | T/wrong:T | 119 |
| all | W/wrong:W | 71 |
| half:P1 | C/correct | 199 |
| half:P1 | C/wrong:S | 1 |
| half:P1 | M/wrong:M | 102 |
| half:P1 | S/correct | 11 |
| half:P1 | S/wrong:S | 39 |
| half:P1 | T/wrong:T | 60 |
| half:P1 | W/wrong:W | 38 |
| half:P2 | C/correct | 200 |
| half:P2 | M/wrong:M | 107 |
| half:P2 | S/correct | 10 |
| half:P2 | S/wrong:S | 39 |
| half:P2 | S/wrong:W | 1 |
| half:P2 | T/correct | 1 |
| half:P2 | T/wrong:T | 59 |
| half:P2 | W/wrong:W | 33 |
| level:A1 | C/correct | 100 |
| level:A1 | M/wrong:M | 38 |
| level:A1 | S/correct | 3 |
| level:A1 | S/wrong:S | 21 |
| level:A1 | S/wrong:W | 1 |
| level:A1 | T/wrong:T | 30 |
| level:A1 | W/wrong:W | 32 |
| level:A2 | C/correct | 100 |
| level:A2 | M/wrong:M | 49 |
| level:A2 | S/correct | 5 |
| level:A2 | S/wrong:S | 20 |
| level:A2 | T/wrong:T | 30 |
| level:A2 | W/wrong:W | 21 |
| level:B1 | C/correct | 100 |
| level:B1 | M/wrong:M | 61 |
| level:B1 | S/correct | 7 |
| level:B1 | S/wrong:S | 18 |
| level:B1 | T/wrong:T | 30 |
| level:B1 | W/wrong:W | 9 |
| level:B2 | C/correct | 99 |
| level:B2 | C/wrong:S | 1 |
| level:B2 | M/wrong:M | 61 |
| level:B2 | S/correct | 6 |
| level:B2 | S/wrong:S | 19 |
| level:B2 | T/correct | 1 |
| level:B2 | T/wrong:T | 29 |
| level:B2 | W/wrong:W | 9 |

## floors per scope

| scope | floor | n |
| --- | --- | ---: |
| all | F1_agentdrop_any_wrong | 161 |
| all | F2_agentdrop_embedded_wrong | 96 |
| all | F3_timeframe_wrong | 119 |
| all | F4_by_passive_correct | 80 |
| all | F5_skp_correct | 81 |
| half:P1 | F1_agentdrop_any_wrong | 78 |
| half:P1 | F2_agentdrop_embedded_wrong | 46 |
| half:P1 | F3_timeframe_wrong | 60 |
| half:P1 | F4_by_passive_correct | 40 |
| half:P1 | F5_skp_correct | 40 |
| half:P2 | F1_agentdrop_any_wrong | 83 |
| half:P2 | F2_agentdrop_embedded_wrong | 50 |
| half:P2 | F3_timeframe_wrong | 59 |
| half:P2 | F4_by_passive_correct | 40 |
| half:P2 | F5_skp_correct | 41 |
| level:A1 | F1_agentdrop_any_wrong | 23 |
| level:A1 | F2_agentdrop_embedded_wrong | 3 |
| level:A1 | F3_timeframe_wrong | 30 |
| level:A1 | F4_by_passive_correct | 20 |
| level:A1 | F5_skp_correct | 21 |
| level:A2 | F1_agentdrop_any_wrong | 34 |
| level:A2 | F2_agentdrop_embedded_wrong | 18 |
| level:A2 | F3_timeframe_wrong | 30 |
| level:A2 | F4_by_passive_correct | 20 |
| level:A2 | F5_skp_correct | 20 |
| level:B1 | F1_agentdrop_any_wrong | 52 |
| level:B1 | F2_agentdrop_embedded_wrong | 38 |
| level:B1 | F3_timeframe_wrong | 30 |
| level:B1 | F4_by_passive_correct | 20 |
| level:B1 | F5_skp_correct | 20 |
| level:B2 | F1_agentdrop_any_wrong | 52 |
| level:B2 | F2_agentdrop_embedded_wrong | 37 |
| level:B2 | F3_timeframe_wrong | 29 |
| level:B2 | F4_by_passive_correct | 20 |
| level:B2 | F5_skp_correct | 20 |
