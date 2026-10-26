"""Ablation of hybrid: reciprocal rank fusion (RRF) of the bm25 and dense rankings over chunks, with k = 120 instead of 60.

Experiment: change one thing, the RRF constant, and keep everything else the same as hybrid.py. Each chunk scores
the sum of 1 / (120 + rank) over the two rankings. A larger constant flattens the weights, so a chunk ranked first
counts for less against one ranked tenth than it does at k = 60, and the highly ranked candidates of either system
have a smaller relative influence on the fused order.

Hypothesis (written before the run, also in EVAL.md section 5): this slightly decreases MRR@10 on the own corpus.

This file is a copy of hybrid.py in which only K (60 to 120) and the BASE line differ. The two systems come from
p2.retrievers.build, so their indexes are built once per run and their own search_chunks gives the rankings;
nothing about their scoring is repeated here. BASE names the system it varies, for the own-ablation tables.
"""

from __future__ import annotations

from p2 import retrievers
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False
BASE = "hybrid"
PARTS = ("bm25", "dense")
K = 120


class Hybrid(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.parts = [retrievers.build(name, corpus, cfg) for name in PARTS]

    def score_chunks(self, text: str) -> list[float]:
        fused = {c.id: 0.0 for c in self.chunks}
        for part in self.parts:
            ranking = part.search_chunks(text, len(self.chunks))  # every chunk, best first
            for rank, (chunk_id, _) in enumerate(ranking, 1):
                fused[chunk_id] += 1 / (K + rank)
        return [fused[c.id] for c in self.chunks]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
