"""Dense retrieval: embed every chunk once, embed the query, and rank chunks by cosine similarity.

It follows the 12 lab's dense_rankings (retrieve.py): the chunk vectors come from a cache, the query
is embedded the same way, and one matrix product gives every score. The embedder is bge-small-en-v1.5,
loaded and cached by the helpers in p2/embed.py. Vectors have length 1, so a dot product is the cosine.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False
MODEL = embed.BGE


class Dense(ChunkScorer):
    model = MODEL

    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.embedder = embed.load(MODEL)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> list[float]:
        if not self.chunks:
            return []
        query = self.embedder.encode([text])[0]
        return (self.vectors @ query).tolist()


def build(corpus, cfg):
    return Dense(corpus, cfg)
