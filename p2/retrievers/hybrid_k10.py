"""Ablation of hybrid: the same reciprocal rank fusion (RRF) of the bm25 and dense rankings over chunks, with k = 10 instead of 60.

It is a copy of hybrid.py in which only the RRF constant K changes (60 to 10): each chunk scores the sum of
1 / (10 + rank) over the two rankings. The two systems come from p2.retrievers.build, so their indexes are built
once per run and their own search_chunks gives the rankings; nothing about their scoring is repeated here.
"""

from __future__ import annotations

from p2 import retrievers
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False
BASE = "hybrid"
PARTS = ("bm25", "dense")
K = 10


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
