# Day 1 — First Pass & Architecture Mapping

## 1. Quick Skim (15–20 min)
- Read the **Abstract**, **Introduction**, and **Conclusion** to get the problem statement and main contribution.
- Skim all **section headings** and **figures/tables** to see the paper’s overall “shape.”
- Glance at **equations** to locate where the math is concentrated:
  - Section 3.2 — Scaled Dot-Product Attention
  - Section 3.3 — Feedforward Networks
  - Section 3.5 — Positional Encoding
  - Section 5.3 — Optimizer

**Goal:** Identify all building blocks before diving deep.

---

## 2. Component Checklist (30–45 min)
- List the **major blocks** you identify:
  - Encoder
  - Decoder
  - Attention (scaled dot-product + multi-head)
  - Feedforward network (FFN)
  - Embeddings
  - Positional encoding
  - Output projection / Softmax
- For each block, jot:
  - **Role** (e.g., “maps input token sequence to contextual embeddings”)
  - **Inputs/Outputs** (types, shapes)
  - **Paper section reference** (for quick lookup later)
---

## 3. Architecture Diagram (45 min)
- On paper or digital tablet, draw:
  - **Encoder stack:** input embeddings → positional encoding → N × [MHA → FFN]
  - **Decoder stack:** masked MHA → encoder-decoder attention → FFN
  - **Residual connections** and **layer norms** shown as arrows/boxes.
- Include **shape annotations** (e.g., `d_model`, sequence length, head count).
- Save diagram as `docs/architecture.png`.

---

## 4. Big-Picture Questions (15 min)
In your notebook, answer:
1. Why did they remove recurrence/convolutions?  
2. What *training-time* benefits do they claim from self-attention?  
3. How do they handle sequence order without recurrence?

---

## 5. Coding Tasks
- Create `transformer/` folder in your repo.
- Add empty files:
  - `attention.py`
  - `feedforward.py`
  - `positional_encoding.py`
  - `encoder.py`
  - `decoder.py`
  - `transformer.py`
- Add placeholder class/function definitions (just `pass`).

---

## 6. Deliverables for Day 1
- [ ] `docs/components.md` with block list and descriptions.
- [ ] `docs/architecture.png` with labeled diagram.
- [ ] Initial `transformer/` folder with placeholder modules.
- [ ] Notebook answers to big-picture questions.
- [ ] Commit and push to GitHub.
