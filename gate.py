"""Per-use-case model swap gate on tau2-bench results.

Compares a baseline and a candidate model on the same tasks and checks two
things: does the aggregate pass rate go up, and does every use case clear a
non-inferiority bar on its own (paired bootstrap over tasks, 90% interval).
Only uses the Python standard library.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import random
from collections import defaultdict

READ_PREFIXES = ("get_", "find_", "search_", "list_", "calculate", "think", "transfer")
MIN_GROUP = 3  # use cases with fewer tasks are pooled into "other"


def use_case(domain: str, task: dict) -> str:
    """Name the customer flow a task exercises.

    telecom task ids start with the intent, e.g. "[mms_issue]...".
    airline/retail: the first state-changing tool in the gold actions
    (cancel_reservation, return_delivered_order_items, ...), or "no_write"
    for tasks where the right outcome is a refusal or information only.
    """
    if domain == "telecom":
        return task["id"].split("]")[0].lstrip("[")
    actions = task["evaluation_criteria"].get("actions") or []
    writes = [a["name"] for a in actions if not a["name"].startswith(READ_PREFIXES)]
    return writes[0] if writes else "no_write"


def load(path: str) -> tuple[dict[str, list[float]], dict[str, dict]]:
    with open(path) as f:
        data = json.load(f)
    rewards: dict[str, list[float]] = defaultdict(list)
    for sim in data["simulations"]:
        reward = (sim.get("reward_info") or {}).get("reward") or 0.0
        rewards[sim["task_id"]].append(1.0 if reward >= 1.0 else 0.0)
    tasks = {t["id"]: t for t in data["tasks"]}
    return dict(rewards), tasks


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def task_rate(trials):
    return mean(trials)


def bootstrap_diff(task_ids, a, b, iters, rng):
    """90% paired bootstrap interval for mean(candidate - baseline) over tasks."""
    diffs = [task_rate(b[t]) - task_rate(a[t]) for t in task_ids]
    n = len(diffs)
    stats = []
    for _ in range(iters):
        stats.append(mean([diffs[rng.randrange(n)] for _ in range(n)]))
    stats.sort()
    return mean(diffs), stats[int(0.05 * iters)], stats[int(0.95 * iters) - 1]


def compare(domain, base_path, cand_path, margin, iters, seed):
    a, tasks = load(base_path)
    b, _ = load(cand_path)
    common = sorted(set(a) & set(b) & set(tasks))
    groups: dict[str, list[str]] = defaultdict(list)
    for t in common:
        groups[use_case(domain, tasks[t])].append(t)
    pooled: dict[str, list[str]] = defaultdict(list)
    for name, ids in groups.items():
        pooled[name if len(ids) >= MIN_GROUP else "other"].extend(ids)

    rng = random.Random(seed)
    overall = bootstrap_diff(common, a, b, iters, rng)
    rows = []
    for name, ids in sorted(pooled.items(), key=lambda kv: -len(kv[1])):
        d, lo, hi = bootstrap_diff(ids, a, b, iters, rng)
        rows.append({
            "use_case": name,
            "tasks": len(ids),
            "baseline": mean([task_rate(a[t]) for t in ids]),
            "candidate": mean([task_rate(b[t]) for t in ids]),
            "diff": d, "lo": lo, "hi": hi,
            "regression": hi < 0,            # worse, and the interval excludes 0
            "clears": lo > -margin,          # non-inferior within the margin
        })
    flips = {
        "broke": sum(1 for t in common if min(a[t]) == 1 and max(b[t]) == 0),
        "fixed": sum(1 for t in common if min(b[t]) == 1 and max(a[t]) == 0),
    }
    return {
        "domain": domain,
        "baseline": model_name(base_path),
        "candidate": model_name(cand_path),
        "tasks": len(common),
        "trials": len(next(iter(a.values()))),
        "overall": {"baseline": mean([task_rate(a[t]) for t in common]),
                    "candidate": mean([task_rate(b[t]) for t in common]),
                    "diff": overall[0], "lo": overall[1], "hi": overall[2]},
        "use_cases": rows,
        "flips": flips,
        "gate_passed": overall[1] > -margin and all(r["clears"] for r in rows),
    }


def model_name(path):
    return os.path.basename(path).split("_")[0]


def pct(x):
    return f"{100 * x:5.1f}"


def report(res, margin):
    o = res["overall"]
    lines = [
        f"## {res['domain']}: {res['baseline']} -> {res['candidate']} "
        f"({res['tasks']} tasks x {res['trials']} trials)",
        "",
        f"Aggregate pass rate {pct(o['baseline'])}% -> {pct(o['candidate'])}% "
        f"(diff {pct(o['diff'])} pts, 90% CI [{pct(o['lo'])}, {pct(o['hi'])}])",
        f"Tasks the baseline passed 4/4 and the candidate failed 4/4: {res['flips']['broke']}; "
        f"the reverse: {res['flips']['fixed']}",
        "",
        "| use case | tasks | baseline | candidate | diff (90% CI) | verdict |",
        "|---|---:|---:|---:|---|---|",
    ]
    for r in res["use_cases"]:
        verdict = ("REGRESSION" if r["regression"]
                   else "clears" if r["clears"] else f"not shown within -{margin*100:.0f} pts")
        lines.append(
            f"| {r['use_case']} | {r['tasks']} | {pct(r['baseline'])}% | {pct(r['candidate'])}% | "
            f"{pct(r['diff'])} [{pct(r['lo'])}, {pct(r['hi'])}] | {verdict} |")
    lines += ["", f"Gate (aggregate and every use case non-inferior within {margin*100:.0f} pts): "
              + ("PASS" if res["gate_passed"] else "FAIL"), ""]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data", default="data", help="folder with tau2-bench *_4trials.json results")
    p.add_argument("--margin", type=float, default=0.10, help="non-inferiority margin (0.10 = 10 pts)")
    p.add_argument("--iters", type=int, default=5000)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--json", help="also write all comparisons to this file")
    args = p.parse_args()

    out, summary = [], []
    for domain in ("airline", "retail", "telecom"):
        files = sorted(glob.glob(os.path.join(args.data, f"*_{domain}_*_4trials.json")))
        files = [f for f in files if f"_{domain}_default_" in f or f"_{domain}_base_" in f]
        for base in files:
            for cand in files:
                if base == cand:
                    continue
                res = compare(domain, base, cand, args.margin, args.iters, args.seed)
                if res["overall"]["diff"] <= 0:
                    continue  # only look at swaps that improve the aggregate
                out.append(res)
                print(report(res, args.margin))
                regressed = [r["use_case"] for r in res["use_cases"] if r["regression"]]
                dropped = [r["use_case"] for r in res["use_cases"] if r["diff"] < 0]
                summary.append((domain, res["baseline"], res["candidate"], res["overall"]["diff"],
                                len(res["use_cases"]), dropped, regressed, res["flips"]["broke"],
                                res["gate_passed"]))
    print("## Summary: swaps that raise the aggregate pass rate\n")
    print("| domain | baseline -> candidate | aggregate diff | use cases that drop | significant regressions | tasks 4/4 -> 0/4 | gate |")
    print("|---|---|---:|---|---|---:|---|")
    for d, b, c, diff, n, dropped, reg, broke, ok in summary:
        print(f"| {d} | {b} -> {c} | +{pct(diff).strip()} | {len(dropped)}/{n} {', '.join(dropped)} | "
              f"{', '.join(reg) or 'none'} | {broke} | {'PASS' if ok else 'FAIL'} |")
    if args.json:
        with open(args.json, "w") as f:
            json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
