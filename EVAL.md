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

Dense: My dense retriever uses the BAAI/bge-small-en-v1.5 embedding model through FastEmbed. This retriever divides documents into 300-word chunks with 50 words of overlap. It uses cosine similarity between normalized query and chunk embeddings for retrieval. Each document is represented by its highest-    scoring chunk, and the top 10 documents are returned. While the lab 12 implementation embeds entire documents, my implementation embeds individual chunks. 

Hybrid: My hybrid retriever combines BM25 and dense retrieval using reciprocal rank fusion (RRF) with K=60. This retriever combines the full chunk-level rankings from both systems, adding their reciprocal rank scores for each chunk, and selects each document's highest-scoring chunk. This differs from the lab 13 implementation, which performs fusion at the document level. 

Rerank: My rerank retriever takes the top 20 documents from the hybrid retriever and passes the first 600 characters of each document to Claude Sonnet 5. Claude then orders the documents according to their usefulness for answering the query, and the system returns the top 10 in that order. If the ranking returned by Claude is invalid, the system falls back to the original hybrid ordering. This is similar to the Lab 13 reranker, but my implementation uses the chunk-based hybrid system as its first stage. 

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

On the 20 shared practice queries, rerank had the highest performance across all three metrics, with a Recall@10 of 0.733, MRR@10 of 0.800, and nDCG@10 of 0.735. Its MRR@10 improvement over hybrid was +0.272, with a paired 95% confidence interval of [+0.111, +0.447]. Since this interval is entirely above zero, rerank performed distinguishably better than hybrid on this gold set. Rerank also had a distinguishable MRR@10 improvement over BM25 and dense. 

The differences between BM25, dense, and hybrid were not distinguishable from zero on any of the three metrics. Hybrid improved MRR@10 over BM25 by only +0.021, with a confidence interval of [-0.148, +0.193]. Because this interval includes zero, the results do not establish that hybrid was better than BM25 on these queries. 

The results for the different classes of queries show different strengths between lexical and semantic retrieval. BM25 performed well on identifier queries, with an MRR@10 of 0.810, but an MRR@10 of 0.000 on paraphrase queries. Dense was comparatively much better on paraphrase queries, with an MRR@10 of 0.714, although it was worse on identifer queries. These observations make sense given that dense retrieval handles vocabulary mismatches better than BM25. However, given the small number of queries in each class, I cannot make strong conclusions.

Minimum detectable difference varies with systems and metrics. For example, the MDD for hybrid versus BM25 on MRR@10 was 0.249, which means this 20-query gold set was not sensitive enough to detect a small improvement between these systems. The MDD for rerank versus hybrid was 0.244. Therefore, differences smaller than the MDD for that pair should not be interpreted as evidence that the systems perform equally. 

Overall, my results support the effectiveness of reranking and demonstrate different strengths of lexical and semantic retrieval, but they do not establish hybrid fusion is substantially better compared to its component systems. 

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

I used rerank to generate answers for the 12 shared questions because it had the highest performance on all three metrics for the shared practice queries. Answer generation works by reranking the top 20 chunks returned by hybrid retrieval, and then passes the top 5 chunks to Claude for the final answer generation. The answer includes claims with chunk identifiers and quotes from the retrieved text.

I did not modify the actual instructions in prompts/answer.txt from Lab 13. The prompt in that version tells Claude to answer only from the provided chunks, cite each claim it makes, and decline any questions that aren't answerable using the retrieved text. Because I did not modify this prompt, I do not have a before-and-after comparison that could show whether changing this prompt could affect either rate.

The answer run verified 7 out of 8 questions that were in the corpus, which is 87.5%. The confidence interval for this result was [0.529, 0.978]. It correctly declined all 4 of the questions that were not answerable with the corpus, with an interval of [0.510, 1.000]. The answers contained 10 citations, and 9 of these passed automated verification. The one that did not pass verification was question a07, where claude used the citation identifier cfr57.9300#0 instead of cfr30-57.9300#0. The factual answer, which was about berm and guardrail height, was supported by the source, but since Claude incorrectly formatted the identifier, verification failed.

I manually examined three of the in-corpus answers that passed automated verification:

- **a01**: The answer provided states that an operator must notify MSHA immediately and within 15 minutes after a fatal accident. I looked at cfr30-50.10#0, which agreed with the answer, it specifies notification within 15 minutes and includes a death at the mine as one of the events triggering this required notification. The two quoted passages support this answer.

- **a05**: The answer states new underground miners must receive a minimum of 40 hours of training before being assigned to work duties. The quoted passage, cfr30-48.5#0, explicitly states that new miners must receive no less than 40 hours of training before being assigned to work duties. The quoted passage supports the number of hours required, however the "underground miner" aspect of the query is not explicitly stated in this passage, but the surrounding context of the passage does support this. 

- **a08**: The answer states that refuge-alternative breathable air must sustain each person for 96 hours. The cited chunk, cfr30-7.506#0, explicitly states that such a refuge must support each person for 96 hours. This chunk supports the answer provided. 

All three of these verified answers were supported by the cited chunk or chunks. However, the automated verifier only establishes whether quotations appear in the cited chunks, and whether the chunk identifiers were cited correctly, not whether the information cited actually logically supports the claims made in the answer. This manual audit is important to evaluate whether the answers are factually supported by the chunk.

The confidence intervals were fairly wide because the experiment only included 8 answerable and 4 unanswerable questions. The results are encouraging, especially the fact that all 4 out-of-corpus questions were refused, but they do not establish that a larger set of questions would achieve the same rates.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

I chose the USGS Mineral Commodity Summaries as my own corpus. This was one of the course-recommended corpus options in the assignment. This collection contains reports about the production, consumption, prices and other economic information associated with different mineral commodities. I selected the 2023, 2024, and 2025 editions, with 88 commodity chapters from each year, giving a total of 264 documents. The resulting text corpus had a size of about 2.2 MB.

The source documents came from the USGS website. The format of the documents was individual PDF chapters. I used a download script Claude generated to collect the PDFs, with intentional delays in downloads. I used the project's ingestion tool to convert these PDF files into Markdown documents. Each document's source URL was recorded in corpora/own/manifest.tsv.

This corpus falls under the allowed category of US federal government works. In the manifest, each document is labeled us-gov-public-domain. I used the `uv run p2 license` tool to check the corpus. The report generated by this tool (LICENSES.md) showed that all 264 documents passed, there were no failures, and none of the documents were flagged.

One consideration in terms of licensing with the USGS documents is that these works can contain third party copyrighted material, especially photographs. These third party material may not be public domain. However, my corpus contains the extracted text of commodity chapters, and did not include any images. The licensing scan did not return any problematic notices in these chapters, but this automated check cannot guarantee that every piece of material is public domain and free of copyright restrictions.

I had small concerns with some of the documents in the ingested corpus. `mcs2023-arsenic.md` had a faulty ingestion, with the author line of the document being incorrectly extracted as the title, rather than the commodity name. I decided to retain this document anyway, since the rest of the text was not poorly extracted, and the filename identifies the commodity being discussed.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

I had 60 queries in my gold set. I hand-wrote 15 of them, and drafted the remaining 45 using Claude. I chose an even divide of query classes, with 20 queries for each of paraphrase, identifier, and mixed queries. I chose these three classes to evaluate how the retrieval system performs with different types of queries that reflect real world use, with some containing specific identifiers and terminology, some with paraphrased text that matches the meaning of a passage but with different wording, and some that combine these characteristics. 

My relevance judgements were binary, with a 1 indicating the document is relevant to the query. I considered a document relevant if it contained sufficient information to answer the query, including any applicable commodity or publication year requirements. The Mineral Commodity Summaries sometimes report data from the preceding year, so I distinguished between the publication year of a document and the year of the information requested. Because of this, I considered documents from other years relevant if they explicitly contained the historical information needed for the query.

For the 45 queries generated by Claude, I first used Claude to identify candidate documents from the corpus that could be relevant. Claude provided documents it was fairly certain were relevant, and for some queries additional documents that it thought could be relevant but was less certain about. I then manually reviewed all 45 queries, and checked the higher confidence candidate documents to determine whether they were actually relevant and could answer the query. I only added documents to `qrels.txt` if I thought they were relevant. 

I performed a second pass over the candidates that Claude provided to evaluate the less certain candidates. Most of these less certain candidates were for the same commodity as the more certain ones, but from different publication years. I only added relevance judgements if the documents could accurately answer the query with the correct referenced year, either for publication or reporting years. This process resulted in 66 positive relevance judgements for 60 queries, with some queries having multiple relevant documents. 

A more exhaustive way to produce relevance judgements for each query would be to read every document in the corpus for every query, ensuring nothing relevant is missed. My approach was to review candidate documents most likely to be relevant, identified by Claude. One limitation of this approach is that Claude may have missed some documents that were relevant to a query. Although my manual review helped ensure that the positive relevance judgement was accurate for that query, it doesn't guarantee that the gold set includes every relevant document for one query. 

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

Rerank performed the best overall, with an MRR@10 of 0.964, and an nDCG@10 of 0.969. This represents an improvement over hybrid by +0.200 MRR@10, with a paired 95% confidence interval of [+0.119, +0.281]. The MDD for rerank versus hybrid was 0.117, which means this query set was sufficiently sensitive to detect observed improvement. This improvement is statistically distinguishable from zero, as the confidence interval is entirely above zero. Rerank's nDCG@10 improvement over hybrid was +0.144, with a 95% confidence interval of [+0.084, +0.203]. The differences between BM25, dense, and hybrid were not statistically distinguishable from zero on these metrics. Both rerank and hybrid achieved perfect Recall@10, but rerank placed relevant documents much higher.

In terms of performance across queries, BM25 performed best on identifier queries, with an MRR@10 of 0.967, compared to 0.917 for rerank and 0.679 for dense. Since BM25 relies on lexical matching, this makes sense, as identifier queries contain specific terminology from the documents. Dense performed much better than BM25 on paraphrase queries, with an MRR@10 of 0.817 compared to 0.606. This makes sense given that dense is better at finding semantically similar information even if the wording is different in the document. Rerank performed best on paraphrase and mixed queries, with an MRR@10 of 0.975 and 1.000 respectively. However, the results for individual query classes do not have confidence intervals, so these observations are more descriptive than statistically distinguishable differences.

There were some interesting differences between the hand-written and Claude-written queries. Dense performed better on the Claude written queries, with an MRR@10 of 0.800 compared to 0.578 on the hand-written queries. The confidence interval for the difference between hand-written and Claude-written queries was [-0.411, -0.030], which indicates a statistically distinguishable difference. Rerank was slightly better on hand-written queries, with an MRR@10 of 1.000 compared to 0.952 on Claude-written queries. This difference was also distinguishable from zero, with a confidence interval of [+0.011, +0.096]. The difference between hand-written and Claude-written queries for BM25 and hybrid were not distinguishable from zero.

Given that Claude-written queries are generated from the source documents, they are more likely to contain specific keywords, which might favor a keyword-based retrieval like BM25. My results did not support this. BM25 had an MRR@10 improvement of +0.289 over dense on my hand-written queries, but it performed slightly worse on Claude-written queries, with a difference of -0.042. The difference between BM25's relative advantage on Claude and hand-written queries was -0.331, with a 95% confidence interval of [-0.551, -0.104]. This implies that BM25 had a statisically distinguishably larger advantage over dense on the hand-written queries than on Claude-written queries. It is important to note that the two groups of queries generally contained different questions about different commodities, so this cannot establish whether the method of query generation caused these differences. 

My preregistered prediction in PREREG.md was that rerank would perform better than hybrid on MRR@10 for my own corpus. This prediction is supported by my results, with the observed improvement of +0.200 with a 95% confidence interval of [+0.119, +0.281]. Since this interval is entirely above zero, my prediction is supported. This observed improvement also exceeds the minimum meaningful difference I chose of 0.15. The MDD of 0.117 is also below this threshold. However, since the lower bound of this confidence interval, +0.119, is below 0.15, I cannot conclude that the actual improvement was at least that large. Another thing to note is that rerank's MRR@10 of 0.964 is close to the maximum possible value of 1.000, which means further measurable improvement on this gold set is limited.

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

I increased the reciprocal rank fusion (RRF) constant in the hybrid retriever from K=60 to K=120, keeping the BM25 and dense retrievers and all other settings constant. Increasing this K value reduces how much relative influence the highly ranked results have compared to the lower ranked results. My hypothesis was that this would slightly decrease MRR@10 on my own corpus.

The results did not support this hypothesis. Both the K=60 and K=120 versions of the hybrid retriever had an identical Recall@10 value of 1.000, MRR@10 value of 0.764 and nDCG@10 of 0.825. The paired 95% confidence interval for all three metrics was [+0.000, +0.000] because the differences per-query metric were all zero. MDD was not reported because of the lack of any variation in these differences. 

The own-ablation-queries table reported that the change didn't help or hurt any queries. All 60 were left unchanged. However, the top 10 rankings differed for 47 of the queries. The changes occured at ranks 4-10, while the position for judged relevant documents did not change. As an example, on query u16, two irrelevant documents switched positions at ranks 4 and 5, while the helium document judged relevant stayed at rank 1. This explains why the retrieval metrics were not different between versiosn of retriever despite some difference in rankings.

These results show that increasing K from 60 to 120 did not affect the retrieval performance on my gold set that I measured. They do not, however, establish that the two versions of this retriever would be the same on other queries or corpora. A useful next step would be to run an experiment that tests a wider range of K values while still keeping other settings fixed to see if relevant documents change positions or if evaluation metrics improve. 

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

Since rerank achieved a Recall@10 of 1.000 on my gold set, none of the judged relevant documents were missing from the top 10. Because of this, I analyzed cases where relevant documents were ranked lower than expected, and one possible relevance label error.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
|u22|Ranked mcs2023-lead first and mcs2023-zinc second|mcs2023-zinc|Relevant information appears after the first 600 characters shown to Claude. The lead document mentions zinc mines in Alaska, which could have influenced the ranking.|Provide the most relevant passage from each document rather than its first 600 characters.|
|u25|Ranked mcs2025-nickel, mcs2024-nickel second, and mcs2023-nickel third.|mcs2023-nickel contains the $115 million Bipartisan Infrastructure Law project.|The relevant sentence is also after the first 600 characters, and the nickel documents from other years were ranked higher.|Increase the excerpt length or select passages that best match.|
|u44|Ranked mcs2023-molybdenum first and mcs2024-molybdenum second.|mcs2024-molybdenum reports the import sources for 2019-2022|The different year editions are almost duplicates, but the 2023 version covered 2018-2021 instead. The relevant reporting period was outside Claude's excerpt. |Include publication year and relevant import source passages for reranking|
|u30|Ranked mcs2023-rare-earths first, placed mcs2023-yttrium sixth, below documents from several years.|Both mcs2023-rare-earths and mcs2023-yttrium contain China's 2022 mining quota for rare earths.|The relevant quota information in the yttrium document was beyond the excerpt Claude saw.|Provide passages containing the quota figure and explicitly identify desired reporting years.|
|u46|Ranked mcs2025-niobium first, and mcs2024-niobium second.|mcs2024-niobium was labeled relevant but mcs2025-niobium was what contained the figures wanted.|This is likely a relevance label error, as the 2025 document reports the 2024 figure that was requested, while the labeled document contained different figures|Review relevance judgements against source text and correct it if confirmed. |

The biggest issue across these was that a lot of the relevant information appeared beyond the first 600 characters provided to the reranker. Another issue was that documents for the same commodity across different reporting years were very similar, which made it difficult to distinguish the correct reporting period. One fix for this could be to provide query-relevant passages and more clear year information. I could test this by checking whether the judged relevant documents move higher without reducing performance for other queries. 


---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

The best performing system was the same for both corpora. Rerank achieved the highest MRR@10 and nDCG@10 on both the shared and own corpora. The following results are copied from the generated tables in sections 1 and 4. 

| System | Shared MRR@10 | Own MRR@10 |
|---|---|---|
|BM25|0.507|0.785|
|Dense|0.562|0.744|
|Hybrid|0.528|0.764|
|Rerank|0.800|0.964|

On the shared corpus, rerank improved MRR@10 over hybrid by +0.272. The paired 95% confidence interval for this value was [+0.111, +0.447], and it had an MDD of 0.244. On my corpus, the improvement was +0.200, with an interval of [+0.119, +0.281] and an MDD of 0.117. Both of these improvements are statistically distinguishable from zero. The differences between BM25, dense and hybrid were not distinguishable from zero on either corpus.

The two corpora were quite different. The shared corpus consisted of 2,484 documents that were relatively short, with a median length of 68 words, while my corpus contained 264 mineral commodity chapters that had a median length of about 1,062 words. The reranker only examined the first 600 characters of each document, which was the entire document for about 60% of the shared corpus and none of my USGS corpus. My failure analysis confirmed several cases where relevant information was not in the 600 character excerpt handed to the reranker. The queries for the shared corpus contained regulation and standard identifiers, whereas my queries used commodity names, publication years and numerical information. My corpus also contained similar chapters from three publication years, which sometimes led to the reranker ranking the wrong year's document higher than it should have. 

The shared evaluation consisted of only 20 queries, whereas my corpus had 60. Because of this, the shared corpus had less sensitivity to smaller differences, which can be seen in the larger MDD for rerank versus hybrid. Since the corpora use different documents, relevance judgements and queries, the higher score on my own corpus do not mean the systems perform better on USGS documents generally. Additionally, I cannot conclude that the difference between rerank's improvement on the two corpora was statistically significantor caused by any corpus characteristic.

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

rider

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

Across the three experiments on the reranker, Recall@10 and MRR@10 didn't change. Both had a range of 0.000, while nDCG@10 had a range of 0.011. Rerank's MRR@10 improvement over hybrid remained +0.272 in all three repeats. The paired 95% confidence interval was [+0.111, +0.447], which means the improvment was distinguishable from zero across all three repeats.

All three answer-generation repeats verified 8 out of 8 in-corpus answers, and the Wilson 95% interval was [0.676, 1.000]. All three correctly declined 4 out of 4 out-of-corpus questions, with an interval of [0.510, 1.000]. These intervals are relatively wide, and they show that the small number of questions limits what can be concluded about the actual verification and refusal rates. Since these repeats used the same queries, they aren't indepedant trials and shouldn't be pooled. 

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

I followed the plan I laid out in PREREG.md, which I commited before my relevance judgements. I planned to evaluate all 60 of the queries in my gold set, and completed all 60 using the planned paired confidence interval test. My hypothesis was that rerank would outperform the hybrid on MRR@10, with a minimum meaningful difference of 0.15.

The observed improvement was +0.200 MRR@10, with a paired 95% confidence interval of [+0.119, +0.281], and an MDD of 0.117. Since this interval is entirely above zero, my directional hypothesis was supported by this outcome. However, the lower bound of this range is below 0.15, my minimum meaningful difference. Additionally, rerank's MRR@10 of 0.964 is close to the maximum possible value. This limits how much further improvement this gold set could measure. 
