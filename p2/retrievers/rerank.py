"""Reranking: ask Claude to reorder the top 20 of the hybrid system, one claude -p call per query.

It follows the 13 lab's rerank_one() (pipeline.py): the passages are numbered, a schema forces the reply
into {"order": [...]}, and a reply that is not each number once keeps the first-stage order. The documents
below the top 20 keep their order underneath. Every call goes through p2.claude.call, which caches the
reply and adds its tokens to the open retrieval span, so the committed trace shows what it cost.
"""

from __future__ import annotations

from p2 import claude, retrievers

NEEDS_CLAUDE = True
FIRST_STAGE = "hybrid"
CANDIDATES = 20
PASSAGE_CHARS = 600  # the first characters of each passage that Claude sees (lab 13)
PROMPT = """Below are {n} passages from a document collection, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n: int) -> dict:
    """The reply shape: an order of exactly n passage numbers, each between 1 and n."""
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": {"type": "integer", "minimum": 1, "maximum": n}, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


def problem(output, n: int) -> str | None:
    """Why a reply cannot be used, or None when it is each of 1 to n once."""
    order = output.get("order") if isinstance(output, dict) else None
    if not isinstance(order, list) or not all(type(i) is int for i in order) or sorted(order) != list(range(1, n + 1)):
        return f"the reply was not each of 1 to {n} once: {order}"
    return None


class Rerank:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.model = cfg.model  # recorded in the trace
        self.first = retrievers.build(FIRST_STAGE, corpus, cfg)
        self.doc_text = {docid: doc.text for docid, doc in corpus.docs.items()}
        self.chunk_text = {c.id: c.text for c in self.first.chunks}

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search(text, len(self.corpus.docs))
        return self._rerank(text, ranked, self.doc_text)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search_chunks(text, len(self.chunk_text))
        return self._rerank(text, ranked, self.chunk_text)[:k]

    def _rerank(self, text: str, ranked: list[tuple[str, float]], texts: dict[str, str]) -> list[tuple[str, float]]:
        """The whole ranking, best first: the top 20 in Claude's order, then the rest as the first stage had them."""
        top = ranked[:CANDIDATES]
        picks = self._order(text, [texts[i] for i, _ in top])
        reordered = [top[i] for i in picks] + ranked[CANDIDATES:]
        return [(i, 1 / rank) for rank, (i, _) in enumerate(reordered, 1)]  # 1 / rank keeps the order and has no ties

    def _order(self, text: str, passages: list[str]) -> list[int]:
        """The 0-based order Claude picks for the passages; the first-stage order when the reply is unusable."""
        n = len(passages)
        if not n:
            return []
        numbered = "\n\n".join(f"[{i}] {p[:PASSAGE_CHARS]}" for i, p in enumerate(passages, 1))
        prompt = PROMPT.format(n=n, query=text, passages=numbered)
        reply = claude.call(prompt, schema(n), model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg))
        reason = reply.error or problem(reply.output, n)
        if reason:
            print(f"  rerank kept the first-stage order: {reason}", flush=True)
            return list(range(n))
        return [i - 1 for i in reply.output["order"]]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
