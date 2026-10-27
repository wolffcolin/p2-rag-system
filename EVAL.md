# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

TODO: describe your three systems.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.633 | 0.528 | 0.495 |
| rerank | 0.733 | 0.800 | 0.735 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.571 | 0.452 | 0.917 |
| hybrid | MRR@10 | 0.520 | 0.228 | 0.889 |
| hybrid | nDCG@10 | 0.429 | 0.254 | 0.852 |
| rerank | Recall@10 | 0.714 | 0.595 | 0.917 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.684 | 0.626 | 0.922 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.008 | [-0.217, +0.233] | 0.328 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.021 | [-0.148, +0.193] | 0.249 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.024 | [-0.199, +0.146] | 0.250 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.075 | [-0.100, +0.250] | 0.255 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.034 | [-0.254, +0.170] | 0.309 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.015 | [-0.152, +0.170] | 0.235 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.108 | [-0.125, +0.333] | 0.336 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.217 | [-0.015, +0.441] | 0.330 | not distinguishable |
| rerank minus dense | Recall@10 | +0.175 | [+0.033, +0.333] | 0.221 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.255 | [+0.116, +0.414] | 0.219 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.100 | [+0.017, +0.200] | 0.133 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.272 | [+0.111, +0.447] | 0.244 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.241 | [+0.122, +0.365] | 0.177 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

TODO: write what the practice-query intervals let you claim.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 7 of 8 (88%) | [0.529, 0.978] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 9 of 10 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

TODO: write your answer choices and your three-answer audit.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

TODO: describe your corpus and its license basis.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

TODO: describe your gold set and your relevance rule.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.983 | 0.785 | 0.831 |
| dense | 0.967 | 0.744 | 0.799 |
| hybrid | 1.000 | 0.764 | 0.825 |
| rerank | 1.000 | 0.964 | 0.969 |
| ablation/hybrid_k120 | 1.000 | 0.764 | 0.825 |

60 judged queries; nDCG uses binary labels; a random ranking of the 264 documents would get recall@10 near 0.038.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | mixed (n=20) | paraphrase (n=20) | identifier (n=20) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.950 | 1.000 |
| bm25 | MRR@10 | 0.783 | 0.606 | 0.967 |
| bm25 | nDCG@10 | 0.836 | 0.682 | 0.975 |
| dense | Recall@10 | 0.950 | 1.000 | 0.950 |
| dense | MRR@10 | 0.738 | 0.817 | 0.679 |
| dense | nDCG@10 | 0.790 | 0.860 | 0.748 |
| hybrid | Recall@10 | 1.000 | 1.000 | 1.000 |
| hybrid | MRR@10 | 0.725 | 0.767 | 0.800 |
| hybrid | nDCG@10 | 0.796 | 0.826 | 0.852 |
| rerank | Recall@10 | 1.000 | 1.000 | 1.000 |
| rerank | MRR@10 | 1.000 | 0.975 | 0.917 |
| rerank | nDCG@10 | 0.992 | 0.978 | 0.938 |
| ablation/hybrid_k120 | Recall@10 | 1.000 | 1.000 | 1.000 |
| ablation/hybrid_k120 | MRR@10 | 0.725 | 0.767 | 0.800 |
| ablation/hybrid_k120 | nDCG@10 | 0.796 | 0.826 | 0.852 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=15) | claude (n=45) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.933 | 1.000 | -0.067 | [-0.200, +0.000] | not distinguishable |
| bm25 | MRR@10 | 0.867 | 0.758 | +0.108 | [-0.079, +0.268] | not distinguishable |
| bm25 | nDCG@10 | 0.884 | 0.813 | +0.071 | [-0.101, +0.205] | not distinguishable |
| dense | Recall@10 | 0.867 | 1.000 | -0.133 | [-0.333, +0.000] | not distinguishable |
| dense | MRR@10 | 0.578 | 0.800 | -0.222 | [-0.411, -0.030] | claude higher |
| dense | nDCG@10 | 0.652 | 0.848 | -0.196 | [-0.374, -0.030] | claude higher |
| hybrid | Recall@10 | 1.000 | 1.000 | +0.000 | [+0.000, +0.000] | not distinguishable |
| hybrid | MRR@10 | 0.678 | 0.793 | -0.115 | [-0.274, +0.044] | not distinguishable |
| hybrid | nDCG@10 | 0.760 | 0.847 | -0.086 | [-0.207, +0.032] | not distinguishable |
| rerank | Recall@10 | 1.000 | 1.000 | +0.000 | [+0.000, +0.000] | not distinguishable |
| rerank | MRR@10 | 1.000 | 0.952 | +0.048 | [+0.011, +0.096] | hand higher |
| rerank | nDCG@10 | 1.000 | 0.959 | +0.041 | [+0.011, +0.078] | hand higher |
| ablation/hybrid_k120 | Recall@10 | 1.000 | 1.000 | +0.000 | [+0.000, +0.000] | not distinguishable |
| ablation/hybrid_k120 | MRR@10 | 0.678 | 0.793 | -0.115 | [-0.274, +0.044] | not distinguishable |
| ablation/hybrid_k120 | nDCG@10 | 0.760 | 0.847 | -0.086 | [-0.207, +0.032] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.000 | +0.067 | -0.067 | [-0.267, +0.133] | not distinguishable |
| MRR@10 | -0.042 | +0.289 | -0.331 | [-0.551, -0.104] | bm25 gains more on hand queries |
| nDCG@10 | -0.035 | +0.232 | -0.267 | [-0.473, -0.060] | bm25 gains more on hand queries |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.74 (15 queries), claude 0.78 (45 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 15 hand and 45 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.017 | [-0.067, +0.033] | 0.081 | not distinguishable |
| dense minus bm25 | MRR@10 | -0.041 | [-0.147, +0.069] | 0.154 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.032 | [-0.117, +0.057] | 0.125 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.017 | [+0.000, +0.050] | 0.047 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.022 | [-0.102, +0.062] | 0.118 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.006 | [-0.068, +0.058] | 0.091 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [+0.000, +0.083] | 0.065 | not distinguishable |
| hybrid minus dense | MRR@10 | +0.019 | [-0.043, +0.079] | 0.088 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.026 | [-0.022, +0.074] | 0.069 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.017 | [+0.000, +0.050] | 0.047 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.178 | [+0.090, +0.270] | 0.128 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.138 | [+0.070, +0.208] | 0.099 | rerank higher |
| rerank minus dense | Recall@10 | +0.033 | [+0.000, +0.083] | 0.065 | not distinguishable |
| rerank minus dense | MRR@10 | +0.219 | [+0.131, +0.308] | 0.129 | rerank higher |
| rerank minus dense | nDCG@10 | +0.170 | [+0.099, +0.242] | 0.104 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| rerank minus hybrid | MRR@10 | +0.200 | [+0.119, +0.281] | 0.117 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.144 | [+0.084, +0.203] | 0.085 | rerank higher |
| ablation/hybrid_k120 minus bm25 | Recall@10 | +0.017 | [+0.000, +0.050] | 0.047 | not distinguishable |
| ablation/hybrid_k120 minus bm25 | MRR@10 | -0.022 | [-0.102, +0.062] | 0.118 | not distinguishable |
| ablation/hybrid_k120 minus bm25 | nDCG@10 | -0.006 | [-0.068, +0.058] | 0.091 | not distinguishable |
| ablation/hybrid_k120 minus dense | Recall@10 | +0.033 | [+0.000, +0.083] | 0.065 | not distinguishable |
| ablation/hybrid_k120 minus dense | MRR@10 | +0.019 | [-0.043, +0.079] | 0.088 | not distinguishable |
| ablation/hybrid_k120 minus dense | nDCG@10 | +0.026 | [-0.022, +0.074] | 0.069 | not distinguishable |
| ablation/hybrid_k120 minus hybrid | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus hybrid | MRR@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus hybrid | nDCG@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus rerank | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus rerank | MRR@10 | -0.200 | [-0.281, -0.119] | 0.117 | rerank higher |
| ablation/hybrid_k120 minus rerank | nDCG@10 | -0.144 | [-0.203, -0.084] | 0.085 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

TODO: write what your own-corpus intervals let you claim.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

**Hypothesis (recorded 2026-10-26, before the K=120 run):** Increasing the RRF constant from K=60 to K=120 reduces the relative influence of highly ranked candidates. I hypothesize that this will slightly decrease MRR@10 on the own corpus.

**Earlier attempt, K=10 (disclosed):** The first ablation I tried was `hybrid_k10`, the same fusion with K=10 instead of 60. It was run and scored on this corpus (MRR@10 minus hybrid: +0.017, 95% interval [+0.000, +0.042], not distinguishable) and it passed `uv run p2 check` locally. It then failed the GitHub Actions reproducibility check: `FAIL runs/own/ablation/hybrid_k10.trec matches a fresh run: for u27 it gives mcs2025-gold (rank 6) the score 0.108824 where a fresh run gives it 0.106443`. The cause is not confirmed; we suspect that the lower constant amplifies small cross-environment differences in the retrieval rankings. I retired K=10 (its file and run were removed) and replaced it with K=120. A working-tree draft that rounded the dense scores to 4 decimals before ranking was never committed and went with it. The K=10 numbers are recorded here for transparency and are not used for the claim below.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/hybrid_k120 minus bm25 | Recall@10 | +0.017 | [+0.000, +0.050] | 0.047 | not distinguishable |
| ablation/hybrid_k120 minus bm25 | MRR@10 | -0.022 | [-0.102, +0.062] | 0.118 | not distinguishable |
| ablation/hybrid_k120 minus bm25 | nDCG@10 | -0.006 | [-0.068, +0.058] | 0.091 | not distinguishable |
| ablation/hybrid_k120 minus dense | Recall@10 | +0.033 | [+0.000, +0.083] | 0.065 | not distinguishable |
| ablation/hybrid_k120 minus dense | MRR@10 | +0.019 | [-0.043, +0.079] | 0.088 | not distinguishable |
| ablation/hybrid_k120 minus dense | nDCG@10 | +0.026 | [-0.022, +0.074] | 0.069 | not distinguishable |
| ablation/hybrid_k120 minus hybrid | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus hybrid | MRR@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus hybrid | nDCG@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus rerank | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/hybrid_k120 minus rerank | MRR@10 | -0.200 | [-0.281, -0.119] | 0.117 | rerank higher |
| ablation/hybrid_k120 minus rerank | nDCG@10 | -0.144 | [-0.203, -0.084] | 0.085 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/hybrid_k120 against hybrid (BASE = "hybrid" in p2/retrievers/hybrid_k120.py): it helped 0 queries, hurt 0 and left 60 unchanged.

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

TODO: write the ablation: the one change, the hypothesis, the result and the claim.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|

TODO: add one row for each failure you analyzed, and write two or three sentences on the pattern you see across them.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 236,855 | 9,994 | 156.0 | 19,738 | 833 | 13.0 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 204,319 | 8,667 | 132.0 | 17,027 | 722 | 11.0 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 197,127 | 8,203 | 125.0 | 16,427 | 684 | 10.4 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 202,538 | 8,829 | 133.6 | 16,878 | 736 | 11.1 |
| traces/own-own-rerank.jsonl | rerank | 60 | 60 | 0 | 966,457 | 20,152 | 361.6 | 16,108 | 336 | 6.0 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 302,879 | 6,972 | 123.2 | 15,144 | 349 | 6.2 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 295,498 | 5,500 | 102.1 | 14,775 | 275 | 5.1 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 281,415 | 4,051 | 90.1 | 14,071 | 203 | 4.5 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 281,747 | 5,397 | 101.6 | 14,087 | 270 | 5.1 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 607,657 | 16,202 | 271.9 | 15,191 | 405 | 6.8 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 15,144 | 6.2 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 15,144 | 6.2 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.272 | [-0.447, -0.111] | 15,144 | 6.2 | rerank higher |
| own: bm25 minus rerank | 60 | -0.178 | [-0.270, -0.090] | 16,108 | 6.0 | rerank higher |
| own: dense minus rerank | 60 | -0.219 | [-0.308, -0.131] | 16,108 | 6.0 | rerank higher |
| own: hybrid minus rerank | 60 | -0.200 | [-0.281, -0.119] | 16,108 | 6.0 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-hybrid.jsonl | hybrid | 60 | 0.63 | 10.4 |
| traces/retrieval/own-own-ablation-hybrid_k120.jsonl | hybrid_k120 | 60 | 0.48 | 8.0 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 60 | 0.04 | 0.7 |
| traces/retrieval/own-own-dense.jsonl | dense | 60 | 0.61 | 10.2 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 60 | 0.90 | 15.0 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.06 | 3.0 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 1.00 | 50.1 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.88 | 44.0 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.12 | 3.0 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 2.21 | 55.1 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 1.80 | 45.0 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.708 | 0.800 | 0.715 |
| rerank.r2 | 0.708 | 0.800 | 0.726 |
| rerank.r3 | 0.708 | 0.800 | 0.726 |
| range (max minus min) | 0.000 | 0.000 | 0.011 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.075 | [+0.000, +0.167] | not distinguishable |
| rerank.r2 minus hybrid | Recall@10 | +0.075 | [+0.000, +0.167] | not distinguishable |
| rerank.r3 minus hybrid | Recall@10 | +0.075 | [+0.000, +0.167] | not distinguishable |
| rerank.r1 minus hybrid | MRR@10 | +0.272 | [+0.111, +0.447] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.272 | [+0.111, +0.447] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.272 | [+0.111, +0.447] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.221 | [+0.101, +0.349] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.232 | [+0.112, +0.360] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.232 | [+0.112, +0.360] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
