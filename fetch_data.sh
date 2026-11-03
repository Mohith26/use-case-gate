#!/usr/bin/env bash
# Downloads the public tau2-bench result files used here (about 290 MB) into ./data.
# Pinned to a tau2-bench commit so the numbers in the README are reproducible.
set -euo pipefail
SHA=19f13ea3f5fba8b4c4d272d1353590f29dc53062
BASE="https://raw.githubusercontent.com/sierra-research/tau2-bench/${SHA}/data/tau2/results/final"
mkdir -p data
for domain in airline retail telecom; do
  for model in claude-3-7-sonnet-20250219 gpt-4.1-2025-04-14 o4-mini-2025-04-16; do
    f="${model}_${domain}_default_gpt-4.1-2025-04-14_4trials.json"
    [[ -f "data/$f" ]] || curl -fsSL -o "data/$f" "$BASE/$f"
  done
  f="gpt-4.1-mini-2025-04-14_${domain}_base_gpt-4.1-2025-04-14_4trials.json"
  [[ -f "data/$f" ]] || curl -fsSL -o "data/$f" "$BASE/$f"
done
ls -1 data | wc -l
