# Pre-registration (598E)

This file is for 598E students; it is the second half of the 598E rider, and 498E students can ignore it or delete it.

A pre-registration is a claim you write down, with the test that will judge it, before you can see the answer.
Its value is that the claim can be wrong in a way anyone can check, and that you cannot adjust it afterwards to fit the numbers.
A well-powered result that says "no effect as large as the one I cared about" scores as well as a confirmation, so you have no reason to bend the claim.

**Git history is how I will know the order.**
Commit this file, filled in through section 4, before the first commit that puts a judgment line into `eval/own/qrels.txt` (or any other file under `eval/own/`).
`uv run p2 check` reads `git log` to find the first commit in which sections 1 to 4 have no TODO marker left and some words of yours in each, and confirms that it comes before your first judgment; a copy that was filled in afterwards fails.
Right after that commit, `p2 check` names it and waits for your first judgment; it asks for section 5 separately, once you have scored your own corpus.
You may ingest your corpus and write queries first, but not the relevance judgments.
After that first commit, do not edit sections 1 to 4, because `p2 check` compares them with the commit where you filled them in.
If something must change, add a dated entry in section 6 and leave the original as it was.

You need your stage 1 scores for section 3, so score the shared corpus first.

---

## 1. Hypothesis

One sentence, about your own corpus, naming two of your systems and a direction.
For example: "On my corpus of Kubernetes documentation, `rerank` has a higher MRR@10 than `hybrid`, because the queries are paraphrases that a first-stage fusion ranks too low."
It should be something you could be wrong about.

On my 264 document corpus of USGS Mineral Commodity Summaries, rerank will have a higher MRR@10 than hybrid because there are highly similar commodity chapters from different publication years, and Claude reranking may be better at identifying which publication year the query is requesting. 

---

## 2. The smallest effect that matters

Name one metric, MRR@10 or nDCG@10, and choose it now so you cannot pick the better one afterwards.
Then say how large a difference between the two systems would matter to a person using the search, and why that size.
A difference of 0.02 is usually not worth a reranker's cost in time and tokens.
In this course, choose a Δ of at least 0.15 unless you argue for a larger one, because a smaller gap takes more queries than one project can judge.
Call your number Δ (delta).

My sole primary metric is MRR@10. My delta (Δ) value is 0.15. I chose 0.15 as my minimum meaningful improvement primarily because a smaller minimum meaningful improvement may not justify the latency and token costs of Claude reranking, and it is the course recommended delta. 

---

## 3. How many queries you need

The size of the gold set follows from three numbers: how large a difference you want to detect (Δ), how variable the per-query differences are (sd), and the usual choices of a 5% false-alarm rate and 80% power.

```
n = ((1.96 + 0.84) * sd / Δ)^2
```

Here sd is the standard deviation of the per-query differences between your two systems, which `results/results.json` holds for the shared practice queries.
Compute it from your stage 1 runs for the same two systems, or the nearest pair you have, and say which pair you used.
With only 20 practice queries the sd is itself noisy, so be generous and round up.

Some numbers to calibrate against.
At sd 0.3 and Δ 0.10 the formula gives about 71 queries, and with the t distribution's small-sample correction it is a few more, about 73.
At sd 0.3, a gold set of 30 queries can only detect a difference of about 0.15, which is why 30 queries cannot support a claim about a gap of 0.10.
The spreads you will measure on the shared practice queries are mostly larger than 0.3: from about 0.31 for `hybrid` against `bm25` to about 0.66 for `dense` against `bm25`.
For `rerank` against `hybrid` the sd is about 0.39, so a Δ of 0.10 needs about 120 queries, 0.15 about 55, and 0.20 about 31.
So the course's Δ of 0.15 means about 55 queries for that pair; at an sd of 0.66 it would mean about 150, so compare a pair whose spread you can afford.
Choose Δ and the size of your gold set together: the smallest effect that matters to a user, and a number of queries you can write and judge in the time you have.
If the two do not meet, say which one you gave ground on and why.

After you score the own corpus, the minimum detectable difference that `uv run p2 score` prints for your two systems is this same calculation run the other way.
It should come out at or below your Δ.
If it does not, your queries varied more than your stage 1 sd suggested, and you will say so in the outcome.

My SD was 0.3901. It came from the rerank versus hybrid pair, and it was evaluated on the 20 shared corpus practice queries in stage 1. The metric used was MRR@10. Given this SD and the 0.15 chosen delta, the calculation is n = ((1.96 + 0.84) * 0.3901 / 0.15)^2 = 53.025, meaning the minimum sample size rounds up to 54 queries. In order to provide a buffer for uncertainty, I will choose n = 60 queries as my planned sample size.

---

## 4. The test, and what each result will mean

The test is the paired 95% interval of the mean difference between your two systems on your own gold set, from the `own-pairs` table that `uv run p2 score` writes in `EVAL.md`.
Write the rule now.
This is the default rule, and you can tighten it, but do not loosen it after you see your numbers.

| The interval is | I will say |
|---|---|
| entirely above zero in the direction I predicted | supported: the difference is distinguishable from zero |
| entirely on the other side of zero | contradicted: the opposite of my hypothesis holds on this gold set |
| around zero, with both ends inside plus or minus Δ | well-powered null: a difference as large as Δ is ruled out |
| around zero, with an end beyond plus or minus Δ | inconclusive: the gold set could not settle it, and I say so |

I will use the 95% confidence interval reported by `uv run p2 score`, comparing rerank with hybrid on my own corpus. The difference between the two will be MRR@10(rerank) - MRR@10(hybrid). As the table above states, if the interval is entirely above zero in the direction of rerank, my hypothesis is supported by the outcome. If it is entirely on the other side of zero, my hypothesis is contradicted for the gold set. If the interval is around zero, with both ends inside plus or minus delta, this outcome is a well-powered null. If the interval is around zero, with an end beyond plus or minus delta, the outcome is inconclusive, the gold set could not settle this for me. 


---

## 5. Outcome (write this after the fact)

What was the interval?
Which row of the table in section 4 is it?
Did your gold set reach the size section 3 asked for, and what was the minimum detectable difference that `uv run p2 score` printed?
What would you do next, and what would you want a reader to take from this?

On my USGS Mineral Commodity Summaries gold set rerank had an MRR@10 of 0.964, whereas hybrid had an MRR@10 of 0.764, which is a +0.200 MRR@10 improvement. The paired 95% bootstrap confidence interval for this difference was [+0.119, +0.281].

The whole confidence interval falls above zero, which means this result falls under the supported category in my preregistered decision table in section 4. The result supports my hypothesis that reranking would outperform hybrid on my corpus.

I selected a minimum meaningful difference (delta) value of 0.15. The observed improvement of +0.200 exceeds this delta value. It is important to note that the lower bound of the computed confidence interval, +0.119, is below this threshold. Because of this, I cannot confidently conclude that the improvement was at least 0.15. 

I planned to evaluate 60 queries, providing a buffer above the minimum of 54 queries that I calculated in section 3. I completed all 60 queries. The minimum detectable difference p2 score reported was approximately 0.117, which is below the chosen delta of 0.15. This means my gold set achieved the planned sensitivity for detecting an improvement of my chosen meaningful size.

One limitation is that the rerank MRR@10 of 0.964 is very close to the maximum possible value 1.0. This could mean some of my queries were too easy, limiting my ability to distinguish between high performance retrieval systems and leaving little room to measure further improvements over rerank. Many of my queries explicitly identify a commodity and publication year. The results also are not able to establish that better differentiation between very similar publications from different years caused the improvement over hybrid.

The logical next step would be to pick more challenging queries for a future evaluation, especially queries that require distinguishing similar statistics across different publication years without explicitly naming the desired document. It would also be useful to evaluate the latency and token cost of reranking to determine whether the improvement is worth the costs.

The main conclusion is that Claude reranking substantially improved the ranking of relevant documents on this corpus and gold set. The evidence supports my original directional hypothesis, but the limited corpus scope and near-maximum performance should be considered when interpreting or generalizing the result.


---

## 6. Amendments

Dated entries only, one per change, each saying what changed and why.
Leave this section as it is if nothing changed.
