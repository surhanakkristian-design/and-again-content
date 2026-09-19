# FLOOR_CHECK_1T — judged-label floors before the run (0 model calls)

- items 900 · labelled 900 · unlabelled 0
- verdict: **FLOORS PASS**

## floors

| floor | required | got | ok |
| --- | ---: | ---: | --- |
| F1_agentdrop_any_wrong | 120 | 152 | yes |
| F2_agentdrop_embedded_wrong | 60 | 72 | yes |
| F3_timeframe_wrong | 100 | 120 | yes |
| F4_by_passive_correct | 60 | 80 | yes |
| F5_skp_correct | 40 | 80 | yes |

## judged-wrong types (T/W/M/S)

| scope | T | W | M | S | ? |
| --- | ---: | ---: | ---: | ---: | ---: |
| all | 120 | 52 | 228 | 100 | 0 |
| half:P1 | 60 | 26 | 114 | 50 | 0 |
| half:P2 | 60 | 26 | 114 | 50 | 0 |
| level:A1 | 30 | 13 | 57 | 25 | 0 |
| level:A2 | 30 | 13 | 57 | 25 | 0 |
| level:B1 | 30 | 13 | 57 | 25 | 0 |
| level:B2 | 30 | 13 | 57 | 25 | 0 |

## writer intent x judged

| scope | cell | n |
| --- | --- | ---: |
| all | C/correct | 400 |
| all | M/wrong:M | 228 |
| all | S/wrong:S | 100 |
| all | T/wrong:T | 120 |
| all | W/wrong:W | 52 |
| half:P1 | C/correct | 200 |
| half:P1 | M/wrong:M | 114 |
| half:P1 | S/wrong:S | 50 |
| half:P1 | T/wrong:T | 60 |
| half:P1 | W/wrong:W | 26 |
| half:P2 | C/correct | 200 |
| half:P2 | M/wrong:M | 114 |
| half:P2 | S/wrong:S | 50 |
| half:P2 | T/wrong:T | 60 |
| half:P2 | W/wrong:W | 26 |
| level:A1 | C/correct | 100 |
| level:A1 | M/wrong:M | 57 |
| level:A1 | S/wrong:S | 25 |
| level:A1 | T/wrong:T | 30 |
| level:A1 | W/wrong:W | 13 |
| level:A2 | C/correct | 100 |
| level:A2 | M/wrong:M | 57 |
| level:A2 | S/wrong:S | 25 |
| level:A2 | T/wrong:T | 30 |
| level:A2 | W/wrong:W | 13 |
| level:B1 | C/correct | 100 |
| level:B1 | M/wrong:M | 57 |
| level:B1 | S/wrong:S | 25 |
| level:B1 | T/wrong:T | 30 |
| level:B1 | W/wrong:W | 13 |
| level:B2 | C/correct | 100 |
| level:B2 | M/wrong:M | 57 |
| level:B2 | S/wrong:S | 25 |
| level:B2 | T/wrong:T | 30 |
| level:B2 | W/wrong:W | 13 |

## floors per scope

| scope | floor | n |
| --- | --- | ---: |
| all | F1_agentdrop_any_wrong | 152 |
| all | F2_agentdrop_embedded_wrong | 72 |
| all | F3_timeframe_wrong | 120 |
| all | F4_by_passive_correct | 80 |
| all | F5_skp_correct | 80 |
| half:P1 | F1_agentdrop_any_wrong | 76 |
| half:P1 | F2_agentdrop_embedded_wrong | 36 |
| half:P1 | F3_timeframe_wrong | 60 |
| half:P1 | F4_by_passive_correct | 40 |
| half:P1 | F5_skp_correct | 40 |
| half:P2 | F1_agentdrop_any_wrong | 76 |
| half:P2 | F2_agentdrop_embedded_wrong | 36 |
| half:P2 | F3_timeframe_wrong | 60 |
| half:P2 | F4_by_passive_correct | 40 |
| half:P2 | F5_skp_correct | 40 |
| level:A1 | F1_agentdrop_any_wrong | 38 |
| level:A1 | F2_agentdrop_embedded_wrong | 18 |
| level:A1 | F3_timeframe_wrong | 30 |
| level:A1 | F4_by_passive_correct | 20 |
| level:A1 | F5_skp_correct | 20 |
| level:A2 | F1_agentdrop_any_wrong | 38 |
| level:A2 | F2_agentdrop_embedded_wrong | 18 |
| level:A2 | F3_timeframe_wrong | 30 |
| level:A2 | F4_by_passive_correct | 20 |
| level:A2 | F5_skp_correct | 20 |
| level:B1 | F1_agentdrop_any_wrong | 38 |
| level:B1 | F2_agentdrop_embedded_wrong | 18 |
| level:B1 | F3_timeframe_wrong | 30 |
| level:B1 | F4_by_passive_correct | 20 |
| level:B1 | F5_skp_correct | 20 |
| level:B2 | F1_agentdrop_any_wrong | 38 |
| level:B2 | F2_agentdrop_embedded_wrong | 18 |
| level:B2 | F3_timeframe_wrong | 30 |
| level:B2 | F4_by_passive_correct | 20 |
| level:B2 | F5_skp_correct | 20 |
