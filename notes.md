# notes

## 07-15-25
- **Tasks Completed:**
    - Got ROCm installed.
    - Installed JAX for ROCm.
    - Downloaded "Attention Is All You Need" paper and began reading.
- **Key Learnings/Insights:**
    - **Clarification: Sequence Transduction vs. Transductive Learning**
        - **Sequence Transduction:** Refers to transforming one form of energy into another, as applied to sequences. Literally, seq2seq, and transformers are sequence transducers because they ingest a sequence and then autoregressively decode the new sequence via transduction using the original sequence and the newly generated tokens, as they are generated.
        - **Transductive Learning:** Refers to labeling specific, known, unlabeled instances during training, like completing node labels in a graph that has unknown node labels. This is contrast to **inductive learning** where the learner forms a general rule and then using an inductive bias applies that general rule to new, previously unknown samples.