"""Hybrid retrieval: reciprocal rank fusion (RRF, k = 60) of the bm25 and dense rankings over chunks.

It follows the 13 lab's rrf() (pipeline.py): each chunk scores the sum of 1 / (60 + rank) over the two
rankings. The two systems come from p2.retrievers.build, so their indexes are built once per run and
their own search_chunks gives the rankings; nothing about their scoring is repeated here.
"""

from __future__ import annotations

from p2 import retrievers
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False
PARTS = ("bm25", "dense")
K = 60


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
