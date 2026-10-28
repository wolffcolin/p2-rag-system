    # Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I chose the USGS Mineral Commodity Summaries corpus because it was one of the recommended options for the assignment. I wanted to avoid unnecessary complications with collecting and licensing documents. I was also interested in how retrieval systems would handle the similar reports covering different years of the summaries. I used 264 commodity chapters from the 2023 to 2025 editions, which created opportunities to test if a system could distinguish between publication years and reporting periods. 

Before I evaluated my own corpus, I expected rerank to outperform hybrid on MRR@10 because Claude could potentially be better at distinguishing between similar reports from different years. I recorded this prediction in PREREG.md before creating my relevance judgements, but I did not document a prediction about which system would perform worst. 

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

One design choice I made was to use chunk-level retrieval instead of embedding entire documents, as in Lab 12. I used 300 word chunks that overlapped by 50 words each, and I selected each document's highest scoring chunk. This enabled the retriever to identify relevant passages within longer documents rather than relying on a single embedding that represents the entire document. 

The alternative approach would have been simpler and would have required fewer embeddings, however it may have performed worse on longer documents that referred to several different topics. Chunking added complexity and increased the number of embeddings that had to be generated and searched. I did not directly compare the two approaches, so I cannot say which performed better. 

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

When implementing my ablation experiment, Claude recommended changing the RRF constant from K=60 to K=10. I initially accepted this suggestion and tested the implementation. Although it worked locally, GitHub actions failed the reproducibility check because the generated retrieval scores differed from a fresh run. I suspected that the reason for this was small floating-point precision or rounding differences between environments, which had a bigger effect with a smaller RRF constant.

Rather than keeping the ablation check that couldn't be reproduced, I instead chose K=120, which passed the checks and allowed me to complete the experiment. 

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

One number I don't fully trust is the rerank MRR@10 of 0.964 on my own corpus. Since this is very close to the maximum value of 1.000, my gold set may have contained too many easy queries. Additionally, 45 of the 60 queries in my gold set were generated with Claude, and my relevance judgements were based on a limited set of candidate documents rather than an exhaustive review of all 264.

I manually reviewed relevance judgements and performed the failure analysis, which identified a label that might have been wrong for query u46. Since I only ran rerank once on my corpus, I would need to evaluate harder queries that were indepedantly written, review the relevance labels thoroughly and repeat the experiment to have more confidence in this result.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

The main issue with my system was that the reranker implementation only received the first 600 characters of each candidate document. This is an issue for the USGS corpus, as the documents are relatively long, and important information was often much later in the document. For example, for query u22, the relevant information in mcs2023-zinc appeared after the first 600 characters, and rerank placed it second instead of first. 

To fix this, I would modify p2/retrievers/rerank.py to provide Claude with the highest scoring chunk from each candidate document. I would then compare MRR@10 and the rankings of the affected queries against the original reranker to determine whether this change improved performance. 