# AIAYN — Day 1: First Pass & Architecture Mapping  
*Part of my “Attention Is All You Need” from-scratch replication project using JAX/Flax.*

## Abstract Notes:

### Key BLEU Results

> *Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.*

---

#### Why this matters

#### 1 — The subtext of the numbers
- **28.4 BLEU on En→De**: +2 BLEU over the best existing systems (including ensembles).  
  → This is a *huge* leap for a hard language pair.
- **41.8 BLEU on En→Fr**: New single-model SOTA, trained in only 3.5 days.  
  → Demonstrates both accuracy *and* efficiency.

#### 2 — Why this implies better long-range modeling
- **English→German** is difficult because:
  - Verbs often move to the end in subordinate clauses.
  - Compound nouns and inflections require knowing far-apart context.
  - Agreement rules depend on long-distance grammatical cues.
- **RNNs**: Must carry information sequentially → long-distance info degrades.
- **Self-attention**: Can directly connect *any* word to *any other* → much easier to track long-range relationships.

#### 3 — Instant takeaways for a 2017 NLP researcher
1. Not just faster — more accurate than the best RNN+attention systems.
2. Beating ensembles with a single model means higher inherent expressiveness.
3. Parallelizable + faster training → easier scaling.
4. +2 BLEU on En→De = better handling of long-range dependencies.

## Read-Through + Diagramming


### Transformer — Highest Level
![transformer_highest_level](../images/transformer_highest_level.png)

---