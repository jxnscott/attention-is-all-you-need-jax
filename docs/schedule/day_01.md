# Day 1 — First Pass & Architecture Mapping

## 1. Read-Through + Diagram (2–3 hrs total)
Today I’m just going to read through the paper once and map the architecture as I go.

- Start with the Abstract, Introduction, and Conclusion to get the problem statement and main contributions.
- Skim section headings and figures/tables to get a feel for the paper’s overall structure.
- Glance at the equations to see where the math is concentrated:
  - §3.2 — Scaled Dot-Product Attention
  - §3.3 — Feedforward Networks
  - §3.5 — Positional Encoding
  - §5.3 — Optimizer

As I go through the model sections, I’ll:
- Keep `docs/architecture.md` open.
- Draw the architecture in `docs/architecture.png` as I encounter each component.
- For each block, jot down:
  - Role (in plain English)
  - Inputs (types/shapes)
  - Outputs (types/shapes)
  - Paper section reference
- Add shape annotations (`d_model`, head count, sequence length) and mark residuals/layer norms.

Goal is to finish the pass with a diagram that I can use as a reference while coding.

#### Transformer: Highest Level
![transformer_highest_level](../images/transformer_highest_level.png)

---

## 2. Reflection Questions
Once I finish the pass, I’ll write quick answers to:
1. Why did they remove recurrence/convolutions?  
2. What training-time benefits do they claim from self-attention?  
3. How do they handle sequence order without recurrence?  

---

## 3. End-of-Day Checklist
- [ ] `docs/architecture.md` — diagram + table of components
- [ ] `docs/architecture.png` — labeled, with shapes and data flow
- [ ] Notebook answers to reflection questions
- [ ] Commit + push everything to GitHub


