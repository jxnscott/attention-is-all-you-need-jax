# Scratchpad

This is my running scratchpad for the AIAYN replication project.  
Raw, unordered thoughts and notes go here first.  
Later, I’ll distill them into daily logs (`day_XX.md`).

---
- [Scratchpad](#scratchpad)
  - [2025-07-15](#2025-07-15)
  - [2025-08-12](#2025-08-12)
  - [2025-08-13](#2025-08-13)

---

## 2025-07-15
**Tasks Completed:**
- Got ROCm installed.
- Installed JAX for ROCm.
- Downloaded *Attention Is All You Need* paper and began reading.

**Key Learnings / Insights:**
- **Clarification: Sequence Transduction vs. Transductive Learning**
    - **Sequence Transduction:** Refers to transforming one sequence into another.  
      In NLP, this means ingesting a sequence and autoregressively decoding a new sequence using both the original input and the generated output so far.  
      Input/output lengths can differ.
    - **Transductive Learning:** Inference on specific known unlabeled instances during training (e.g., filling in missing labels in a known graph), as opposed to inductive learning which generalizes to unseen examples.

---

## 2025-08-12
- Took about a one-month break (vacation + computer crash/reset).  
  I did get to read through the entire paper.  
  I noted everything down that I did not understand.
- Back at it today.

---

## 2025-08-13
- Got through abstract, intro, and conclusion in a refresher.
- Started reading the paper again, but this time for thorough understanding rather than a first pass.
- Reached `3 Model Architecture` and diagrammed the Transformer on paper at the highest level.
- Uploaded the diagram.
- Observed how transduction played out with the dimensions changing from **N** in the input to **M** in the output (sequence length).
- Saw how the latent representations **Z** were used by the Decoder autoregressively.
