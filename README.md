# use-case-gate

A small check of one idea: when you swap the model behind a customer-service agent and the overall pass rate goes up, individual flows can still get worse. Parloa describes gating model swaps this way (every critical use case has to clear the bar on its own, with uncertainty taken into account, not just the average) in [How Parloa benchmarks models for enterprise AI agents](https://www.parloa.com/labs/insights/how-parloa-benchmarks-models-for-enterprise-ai-agents/). I wanted to see how often that matters on public data.

I used the published [tau2-bench](https://github.com/sierra-research/tau2-bench) runs: 4 models (Claude 3.7 Sonnet, GPT-4.1, GPT-4.1 mini, o4-mini) on the airline, retail and telecom domains, 4 trials per task, same GPT-4.1 user simulator. For every pair of models in a domain, I treat one as the current model and the other as the candidate, and keep only the 18 swaps where the candidate's aggregate pass rate is higher.

"Use case" here is my own label: for telecom it's the intent in the task id (`mms_issue`, `mobile_data_issue`, `service_issue`); for airline and retail it's the first state-changing tool in the gold actions (`cancel_reservation`, `return_delivered_order_items`, ...), or `no_write` when the right outcome is a refusal or information only. Use cases with fewer than 3 tasks are pooled into `other`.

For each use case I compute the candidate-minus-baseline pass rate with a 90% paired bootstrap over tasks. A use case is a **regression** if the whole interval is below 0, and it **clears** if the lower bound is above -10 points. The gate passes only if the aggregate and every use case clear.

## Results

Of the 18 swaps that raise the aggregate pass rate:

- 17 have at least one use case whose pass rate drops.
- 9 have a use case with a statistically significant drop (4 of them in use cases with 5 or more tasks, e.g. telecom `mms_issue` going from 18.4% to 12.2% while the aggregate rises 7.9 points for GPT-4.1 -> o4-mini).
- 11 have at least one task the baseline passed 4/4 and the candidate failed 4/4.
- Only 2 pass the gate. 7 of the 16 failures have no use case that drops more than 10 points; they fail because 4 trials on a handful of tasks can't show non-inferiority. The median 90% interval half-width is about 15 points for use cases with 5-9 tasks and about 10 points even with 20+ tasks.

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

Per-use-case tables for every swap are in [results.md](results.md) (and `results.json`).

## Run it

```
./fetch_data.sh          # ~290 MB of tau2-bench result files, pinned commit
python3 gate.py --json results.json > results.md
python3 -m unittest test_gate
```

Standard library only (Python 3.9+). Options: `--margin 0.05`, `--iters`, `--seed`.

## Limits

- These are tau2-bench tasks, not production agent designs, and my use-case grouping is a heuristic.
- The published GPT-4.1 mini runs are labelled `base` while the others are `default`, so comparisons involving mini mix two configurations.
- The bootstrap resamples tasks; with 3-5 tasks in a group the intervals are rough. A significant regression on a 3-task group (like airline `send_certificate`) is weak evidence.
- No prompt adaptation: this is the "drop-in swap" half of Parloa's process only.
