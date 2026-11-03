## airline: claude-3-7-sonnet-20250219 -> gpt-4.1-2025-04-14 (50 tasks x 4 trials)

Aggregate pass rate  50.0% ->  56.0% (diff   6.0 pts, 90% CI [ -3.5,  15.5])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 0; the reverse: 3

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| no_write | 20 |  55.0% |  75.0% |  20.0 [  6.2,  35.0] | clears |
| update_reservation_flights | 12 |  43.8% |  52.1% |   8.3 [-12.5,  29.2] | not shown within -10 pts |
| cancel_reservation | 8 |  37.5% |  28.1% |  -9.4 [-31.2,  12.5] | not shown within -10 pts |
| book_reservation | 5 |  60.0% |  45.0% | -15.0 [-30.0,   0.0] | not shown within -10 pts |
| send_certificate | 3 |  58.3% |  25.0% | -33.3 [-58.3,  -8.3] | REGRESSION |
| other | 2 |  50.0% |  75.0% |  25.0 [  0.0,  50.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## airline: claude-3-7-sonnet-20250219 -> gpt-4.1-mini-2025-04-14 (50 tasks x 4 trials)

Aggregate pass rate  50.0% ->  50.5% (diff   0.5 pts, 90% CI [ -9.0,  10.0])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 1

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| no_write | 20 |  55.0% |  62.5% |   7.5 [ -5.0,  21.2] | clears |
| update_reservation_flights | 12 |  43.8% |  33.3% | -10.4 [-35.4,  16.7] | not shown within -10 pts |
| cancel_reservation | 8 |  37.5% |  28.1% |  -9.4 [-28.1,   9.4] | not shown within -10 pts |
| book_reservation | 5 |  60.0% |  45.0% | -15.0 [-25.0,  -5.0] | REGRESSION |
| send_certificate | 3 |  58.3% |  83.3% |  25.0 [  8.3,  41.7] | clears |
| other | 2 |  50.0% |  87.5% |  37.5 [  0.0,  75.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## airline: claude-3-7-sonnet-20250219 -> o4-mini-2025-04-16 (50 tasks x 4 trials)

Aggregate pass rate  50.0% ->  59.0% (diff   9.0 pts, 90% CI [ -1.0,  19.5])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 4

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| no_write | 20 |  55.0% |  87.5% |  32.5 [ 18.8,  47.5] | clears |
| update_reservation_flights | 12 |  43.8% |  45.8% |   2.1 [-18.8,  25.0] | not shown within -10 pts |
| cancel_reservation | 8 |  37.5% |  21.9% | -15.6 [-37.5,   3.1] | not shown within -10 pts |
| book_reservation | 5 |  60.0% |  45.0% | -15.0 [-30.0,   0.0] | not shown within -10 pts |
| send_certificate | 3 |  58.3% |  33.3% | -25.0 [-41.7,  -8.3] | REGRESSION |
| other | 2 |  50.0% |  75.0% |  25.0 [  0.0,  50.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## airline: gpt-4.1-2025-04-14 -> o4-mini-2025-04-16 (50 tasks x 4 trials)

Aggregate pass rate  56.0% ->  59.0% (diff   3.0 pts, 90% CI [ -5.5,  11.5])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 0; the reverse: 0

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| no_write | 20 |  75.0% |  87.5% |  12.5 [  0.0,  25.0] | clears |
| update_reservation_flights | 12 |  52.1% |  45.8% |  -6.2 [-25.0,  14.6] | not shown within -10 pts |
| cancel_reservation | 8 |  28.1% |  21.9% |  -6.2 [-21.9,   9.4] | not shown within -10 pts |
| book_reservation | 5 |  45.0% |  45.0% |   0.0 [-25.0,  25.0] | not shown within -10 pts |
| send_certificate | 3 |  25.0% |  33.3% |   8.3 [-25.0,  41.7] | not shown within -10 pts |
| other | 2 |  75.0% |  75.0% |   0.0 [  0.0,   0.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## airline: gpt-4.1-mini-2025-04-14 -> gpt-4.1-2025-04-14 (50 tasks x 4 trials)

Aggregate pass rate  50.5% ->  56.0% (diff   5.5 pts, 90% CI [ -3.5,  15.0])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 1

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| no_write | 20 |  62.5% |  75.0% |  12.5 [ -3.8,  27.5] | clears |
| update_reservation_flights | 12 |  33.3% |  52.1% |  18.8 [  4.2,  35.4] | clears |
| cancel_reservation | 8 |  28.1% |  28.1% |   0.0 [-18.8,  18.8] | not shown within -10 pts |
| book_reservation | 5 |  45.0% |  45.0% |   0.0 [-15.0,  15.0] | not shown within -10 pts |
| send_certificate | 3 |  83.3% |  25.0% | -58.3 [-66.7, -50.0] | REGRESSION |
| other | 2 |  87.5% |  75.0% | -12.5 [-25.0,   0.0] | not shown within -10 pts |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## airline: gpt-4.1-mini-2025-04-14 -> o4-mini-2025-04-16 (50 tasks x 4 trials)

Aggregate pass rate  50.5% ->  59.0% (diff   8.5 pts, 90% CI [ -1.0,  18.5])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 0; the reverse: 3

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| no_write | 20 |  62.5% |  87.5% |  25.0 [  7.5,  42.5] | clears |
| update_reservation_flights | 12 |  33.3% |  45.8% |  12.5 [ -4.2,  29.2] | clears |
| cancel_reservation | 8 |  28.1% |  21.9% |  -6.2 [-15.6,   3.1] | not shown within -10 pts |
| book_reservation | 5 |  45.0% |  45.0% |   0.0 [-10.0,  10.0] | not shown within -10 pts |
| send_certificate | 3 |  83.3% |  33.3% | -50.0 [-75.0, -25.0] | REGRESSION |
| other | 2 |  87.5% |  75.0% | -12.5 [-25.0,   0.0] | not shown within -10 pts |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## retail: gpt-4.1-2025-04-14 -> claude-3-7-sonnet-20250219 (114 tasks x 4 trials)

Aggregate pass rate  74.1% ->  78.7% (diff   4.6 pts, 90% CI [ -0.7,   9.9])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 2; the reverse: 1

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| exchange_delivered_order_items | 27 |  73.1% |  80.6% |   7.4 [ -5.6,  19.4] | clears |
| return_delivered_order_items | 26 |  77.9% |  82.7% |   4.8 [ -4.8,  15.4] | clears |
| modify_pending_order_items | 18 |  56.9% |  73.6% |  16.7 [  2.8,  30.6] | clears |
| cancel_pending_order | 15 |  85.0% |  78.3% |  -6.7 [-16.7,   3.3] | not shown within -10 pts |
| modify_pending_order_address | 14 |  64.3% |  73.2% |   8.9 [ -7.1,  25.0] | clears |
| no_write | 9 |  91.7% |  83.3% |  -8.3 [-19.4,   0.0] | not shown within -10 pts |
| modify_user_address | 4 |  81.2% |  68.8% | -12.5 [-62.5,  31.2] | not shown within -10 pts |
| other | 1 | 100.0% | 100.0% |   0.0 [  0.0,   0.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## retail: gpt-4.1-mini-2025-04-14 -> claude-3-7-sonnet-20250219 (114 tasks x 4 trials)

Aggregate pass rate  66.0% ->  78.7% (diff  12.7 pts, 90% CI [  7.2,  18.2])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 3

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| exchange_delivered_order_items | 27 |  68.5% |  80.6% |  12.0 [  0.0,  23.1] | clears |
| return_delivered_order_items | 26 |  69.2% |  82.7% |  13.5 [  1.9,  26.0] | clears |
| modify_pending_order_items | 18 |  43.1% |  73.6% |  30.6 [ 16.7,  44.4] | clears |
| cancel_pending_order | 15 |  76.7% |  78.3% |   1.7 [-13.3,  16.7] | not shown within -10 pts |
| modify_pending_order_address | 14 |  51.8% |  73.2% |  21.4 [ 10.7,  32.1] | clears |
| no_write | 9 |  94.4% |  83.3% | -11.1 [-22.2,  -2.8] | REGRESSION |
| modify_user_address | 4 |  68.8% |  68.8% |   0.0 [-37.5,  37.5] | not shown within -10 pts |
| other | 1 | 100.0% | 100.0% |   0.0 [  0.0,   0.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## retail: gpt-4.1-mini-2025-04-14 -> gpt-4.1-2025-04-14 (114 tasks x 4 trials)

Aggregate pass rate  66.0% ->  74.1% (diff   8.1 pts, 90% CI [  3.9,  12.5])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 0; the reverse: 0

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| exchange_delivered_order_items | 27 |  68.5% |  73.1% |   4.6 [ -3.7,  12.0] | clears |
| return_delivered_order_items | 26 |  69.2% |  77.9% |   8.7 [ -1.0,  18.3] | clears |
| modify_pending_order_items | 18 |  43.1% |  56.9% |  13.9 [  4.2,  23.6] | clears |
| cancel_pending_order | 15 |  76.7% |  85.0% |   8.3 [ -5.0,  21.7] | clears |
| modify_pending_order_address | 14 |  51.8% |  64.3% |  12.5 [ -1.8,  26.8] | clears |
| no_write | 9 |  94.4% |  91.7% |  -2.8 [-11.1,   5.6] | not shown within -10 pts |
| modify_user_address | 4 |  68.8% |  81.2% |  12.5 [-12.5,  37.5] | not shown within -10 pts |
| other | 1 | 100.0% | 100.0% |   0.0 [  0.0,   0.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## retail: gpt-4.1-mini-2025-04-14 -> o4-mini-2025-04-16 (114 tasks x 4 trials)

Aggregate pass rate  66.0% ->  71.5% (diff   5.5 pts, 90% CI [  0.0,  11.2])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 0; the reverse: 4

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| exchange_delivered_order_items | 27 |  68.5% |  70.4% |   1.9 [ -8.3,  13.0] | clears |
| return_delivered_order_items | 26 |  69.2% |  83.7% |  14.4 [  4.8,  24.0] | clears |
| modify_pending_order_items | 18 |  43.1% |  68.1% |  25.0 [  6.9,  43.1] | clears |
| cancel_pending_order | 15 |  76.7% |  68.3% |  -8.3 [-21.7,   6.7] | not shown within -10 pts |
| modify_pending_order_address | 14 |  51.8% |  58.9% |   7.1 [ -3.6,  17.9] | clears |
| no_write | 9 |  94.4% |  88.9% |  -5.6 [-22.2,  11.1] | not shown within -10 pts |
| modify_user_address | 4 |  68.8% |  25.0% | -43.8 [-62.5, -25.0] | REGRESSION |
| other | 1 | 100.0% | 100.0% |   0.0 [  0.0,   0.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## retail: o4-mini-2025-04-16 -> claude-3-7-sonnet-20250219 (114 tasks x 4 trials)

Aggregate pass rate  71.5% ->  78.7% (diff   7.2 pts, 90% CI [  1.5,  12.9])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 2

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| exchange_delivered_order_items | 27 |  70.4% |  80.6% |  10.2 [ -1.9,  21.3] | clears |
| return_delivered_order_items | 26 |  83.7% |  82.7% |  -1.0 [-12.5,  10.6] | not shown within -10 pts |
| modify_pending_order_items | 18 |  68.1% |  73.6% |   5.6 [ -9.7,  20.8] | clears |
| cancel_pending_order | 15 |  68.3% |  78.3% |  10.0 [ -5.0,  23.3] | clears |
| modify_pending_order_address | 14 |  58.9% |  73.2% |  14.3 [  1.8,  26.8] | clears |
| no_write | 9 |  88.9% |  83.3% |  -5.6 [-22.2,  13.9] | not shown within -10 pts |
| modify_user_address | 4 |  25.0% |  68.8% |  43.8 [  0.0,  81.2] | clears |
| other | 1 | 100.0% | 100.0% |   0.0 [  0.0,   0.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## retail: o4-mini-2025-04-16 -> gpt-4.1-2025-04-14 (114 tasks x 4 trials)

Aggregate pass rate  71.5% ->  74.1% (diff   2.6 pts, 90% CI [ -3.5,   8.6])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 3; the reverse: 2

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| exchange_delivered_order_items | 27 |  70.4% |  73.1% |   2.8 [-11.1,  16.7] | not shown within -10 pts |
| return_delivered_order_items | 26 |  83.7% |  77.9% |  -5.8 [-17.3,   5.8] | not shown within -10 pts |
| modify_pending_order_items | 18 |  68.1% |  56.9% | -11.1 [-27.8,   5.6] | not shown within -10 pts |
| cancel_pending_order | 15 |  68.3% |  85.0% |  16.7 [  5.0,  28.3] | clears |
| modify_pending_order_address | 14 |  58.9% |  64.3% |   5.4 [ -8.9,  19.6] | clears |
| no_write | 9 |  88.9% |  91.7% |   2.8 [-11.1,  19.4] | not shown within -10 pts |
| modify_user_address | 4 |  25.0% |  81.2% |  56.2 [ 37.5,  81.2] | clears |
| other | 1 | 100.0% | 100.0% |   0.0 [  0.0,   0.0] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## telecom: gpt-4.1-2025-04-14 -> claude-3-7-sonnet-20250219 (114 tasks x 4 trials)

Aggregate pass rate  34.2% ->  49.3% (diff  15.1 pts, 90% CI [  9.6,  20.8])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 0; the reverse: 4

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| mms_issue | 49 |  18.4% |  18.4% |   0.0 [ -5.1,   5.1] | clears |
| mobile_data_issue | 36 |  29.9% |  69.4% |  39.6 [ 29.2,  49.3] | clears |
| service_issue | 29 |  66.4% |  76.7% |  10.3 [  0.0,  20.7] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): PASS

## telecom: gpt-4.1-2025-04-14 -> gpt-4.1-mini-2025-04-14 (114 tasks x 4 trials)

Aggregate pass rate  34.2% ->  43.9% (diff   9.6 pts, 90% CI [  4.8,  14.5])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 1

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| mms_issue | 49 |  18.4% |  16.3% |  -2.0 [ -7.7,   3.1] | clears |
| mobile_data_issue | 36 |  29.9% |  53.5% |  23.6 [ 14.6,  32.6] | clears |
| service_issue | 29 |  66.4% |  78.4% |  12.1 [  0.9,  23.3] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): PASS

## telecom: gpt-4.1-2025-04-14 -> o4-mini-2025-04-16 (114 tasks x 4 trials)

Aggregate pass rate  34.2% ->  42.1% (diff   7.9 pts, 90% CI [  2.4,  13.6])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 4

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| mms_issue | 49 |  18.4% |  12.2% |  -6.1 [-11.7,  -1.0] | REGRESSION |
| mobile_data_issue | 36 |  29.9% |  47.9% |  18.1 [  9.0,  27.8] | clears |
| service_issue | 29 |  66.4% |  85.3% |  19.0 [  5.2,  32.8] | clears |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## telecom: gpt-4.1-mini-2025-04-14 -> claude-3-7-sonnet-20250219 (114 tasks x 4 trials)

Aggregate pass rate  43.9% ->  49.3% (diff   5.5 pts, 90% CI [  1.1,  10.1])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 0

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| mms_issue | 49 |  16.3% |  18.4% |   2.0 [ -3.1,   7.7] | clears |
| mobile_data_issue | 36 |  53.5% |  69.4% |  16.0 [  9.0,  23.6] | clears |
| service_issue | 29 |  78.4% |  76.7% |  -1.7 [-12.9,   9.5] | not shown within -10 pts |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## telecom: o4-mini-2025-04-16 -> claude-3-7-sonnet-20250219 (114 tasks x 4 trials)

Aggregate pass rate  42.1% ->  49.3% (diff   7.2 pts, 90% CI [  2.6,  12.1])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 1; the reverse: 2

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| mms_issue | 49 |  12.2% |  18.4% |   6.1 [  1.0,  11.7] | clears |
| mobile_data_issue | 36 |  47.9% |  69.4% |  21.5 [ 12.5,  31.2] | clears |
| service_issue | 29 |  85.3% |  76.7% |  -8.6 [-17.2,  -0.9] | REGRESSION |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## telecom: o4-mini-2025-04-16 -> gpt-4.1-mini-2025-04-14 (114 tasks x 4 trials)

Aggregate pass rate  42.1% ->  43.9% (diff   1.8 pts, 90% CI [ -2.9,   6.1])
Tasks the baseline passed 4/4 and the candidate failed 4/4: 0; the reverse: 0

| use case | tasks | baseline | candidate | diff (90% CI) | verdict |
|---|---:|---:|---:|---|---|
| mms_issue | 49 |  12.2% |  16.3% |   4.1 [ -1.0,   9.2] | clears |
| mobile_data_issue | 36 |  47.9% |  53.5% |   5.6 [ -4.2,  15.3] | clears |
| service_issue | 29 |  85.3% |  78.4% |  -6.9 [-16.4,   2.6] | not shown within -10 pts |

Gate (aggregate and every use case non-inferior within 10 pts): FAIL

## Summary: swaps that raise the aggregate pass rate

| domain | baseline -> candidate | aggregate diff | use cases that drop | significant regressions | tasks 4/4 -> 0/4 | gate |
|---|---|---:|---|---|---:|---|
| airline | claude-3-7-sonnet-20250219 -> gpt-4.1-2025-04-14 | +6.0 | 3/6 cancel_reservation, book_reservation, send_certificate | send_certificate | 0 | FAIL |
| airline | claude-3-7-sonnet-20250219 -> gpt-4.1-mini-2025-04-14 | +0.5 | 3/6 update_reservation_flights, cancel_reservation, book_reservation | book_reservation | 1 | FAIL |
| airline | claude-3-7-sonnet-20250219 -> o4-mini-2025-04-16 | +9.0 | 3/6 cancel_reservation, book_reservation, send_certificate | send_certificate | 1 | FAIL |
| airline | gpt-4.1-2025-04-14 -> o4-mini-2025-04-16 | +3.0 | 2/6 update_reservation_flights, cancel_reservation | none | 0 | FAIL |
| airline | gpt-4.1-mini-2025-04-14 -> gpt-4.1-2025-04-14 | +5.5 | 2/6 send_certificate, other | send_certificate | 1 | FAIL |
| airline | gpt-4.1-mini-2025-04-14 -> o4-mini-2025-04-16 | +8.5 | 3/6 cancel_reservation, send_certificate, other | send_certificate | 0 | FAIL |
| retail | gpt-4.1-2025-04-14 -> claude-3-7-sonnet-20250219 | +4.6 | 3/8 cancel_pending_order, no_write, modify_user_address | none | 2 | FAIL |
| retail | gpt-4.1-mini-2025-04-14 -> claude-3-7-sonnet-20250219 | +12.7 | 1/8 no_write | no_write | 1 | FAIL |
| retail | gpt-4.1-mini-2025-04-14 -> gpt-4.1-2025-04-14 | +8.1 | 1/8 no_write | none | 0 | FAIL |
| retail | gpt-4.1-mini-2025-04-14 -> o4-mini-2025-04-16 | +5.5 | 3/8 cancel_pending_order, no_write, modify_user_address | modify_user_address | 0 | FAIL |
| retail | o4-mini-2025-04-16 -> claude-3-7-sonnet-20250219 | +7.2 | 2/8 return_delivered_order_items, no_write | none | 1 | FAIL |
| retail | o4-mini-2025-04-16 -> gpt-4.1-2025-04-14 | +2.6 | 2/8 return_delivered_order_items, modify_pending_order_items | none | 3 | FAIL |
| telecom | gpt-4.1-2025-04-14 -> claude-3-7-sonnet-20250219 | +15.1 | 0/3  | none | 0 | PASS |
| telecom | gpt-4.1-2025-04-14 -> gpt-4.1-mini-2025-04-14 | +9.6 | 1/3 mms_issue | none | 1 | PASS |
| telecom | gpt-4.1-2025-04-14 -> o4-mini-2025-04-16 | +7.9 | 1/3 mms_issue | mms_issue | 1 | FAIL |
| telecom | gpt-4.1-mini-2025-04-14 -> claude-3-7-sonnet-20250219 | +5.5 | 1/3 service_issue | none | 1 | FAIL |
| telecom | o4-mini-2025-04-16 -> claude-3-7-sonnet-20250219 | +7.2 | 1/3 service_issue | service_issue | 1 | FAIL |
| telecom | o4-mini-2025-04-16 -> gpt-4.1-mini-2025-04-14 | +1.8 | 1/3 service_issue | none | 0 | FAIL |
