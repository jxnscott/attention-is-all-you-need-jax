# AIAYN From-Scratch — Notes & Roadmap

**Context:** Ongoing learning log and implementation notes for replicating *Attention Is All You Need* in JAX/Flax.

---

## Roadmap / Schedule (living checklist)
- [x] Day 1 — First pass & architecture mapping ([notes/day_01.md](./day_01.md))
- [ ] Day 2 — Attention math + typed shapes (Q/K/V, masking)
- [ ] Day 3 — Multi-head attention impl sketch
- [ ] Day 4 — FFN + residuals + LayerNorm decisions (pre- vs post-norm)
- [ ] Day 5 — Positional encodings (sinusoidal vs learned) experiments
- [ ] Day 6 — Training loop (loss, label smoothing, scheduling)
- [ ] Day 7 — Inference (greedy vs beam) + eval harness (BLEU)

> I’ll update links as I commit each day’s notes.

---

## Notes Index
- **Day 1:** [AIAYN BLEU results + top-level shapes](./day_01.md)
- **Scratchpad:** [Running raw notes](./scratchpad.md)

---

## Figures
- Transformer (highest level): `../images/transformer_highest_level.png`
