# AIAYN — Day 1: First Pass & Architecture Mapping  
*Part of my “Attention Is All You Need” from-scratch replication project using JAX/Flax.*

---

**Date:** YYYY-MM-DD  
**Goal:** Read through the paper once, map out the architecture at the highest level, and prepare a reference diagram + notes for implementation.

---

## 1. Read-Through + Inline Diagramming (2–3 hrs total)

**Plan:**
- Read Abstract, Introduction, and Conclusion for problem statement and main contributions.
- Skim all section headings and figures/tables to understand paper structure.
- Glance at equations to identify where the math is concentrated:
  - §3.2 — Scaled Dot-Product Attention
  - §3.3 — Feedforward Networks
  - §3.5 — Positional Encoding
  - §5.3 — Optimizer
- As I go through model sections:
  - Keep `docs/architecture.md` open.
  - Update `docs/architecture.png` with each component as I encounter it.
  - For each block, note:
    - Role (plain English)
    - Inputs (types/shapes)
    - Outputs (types/shapes)
    - Paper section reference
  - Add shape annotations (`d_model`, head count, sequence length) and mark residuals/layer norms.

**Current Progress:**  
#### Transformer — Highest Level
![transformer_highest_level](../images/transformer_highest_level.png)

---

## 2. Reflection Questions (To Fill In)
1. Why did they remove recurrence/convolutions?  
2. What training-time benefits do they claim from self-attention?  
3. How do they handle sequence order without recur
