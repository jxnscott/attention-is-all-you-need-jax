# Attention Is All You Need — Implementation Tracker

This is a day-by-day checklist for replicating AIAYN in JAX/`flax.nnx`.
Tick each box when complete.

---

## Week 1 — Reading + First Modules

**Day 1**
- [ ] Read AIAYN overview and skim all sections.
- [ ] List core components in `docs/components.md`:
  - Encoder
  - Decoder
  - Scaled dot-product attention
  - Multi-head attention
  - Feedforward network
  - Embeddings
  - Positional encoding
  - Output projection/softmax

**Day 2**
- [ ] Read Sections 1–2 in detail.
- [ ] Draw encoder–decoder architecture diagram, save as `docs/architecture.png`.
- [ ] Create `transformer/` folder with empty module stubs:
  - [ ] `attention.py`
  - [ ] `feedforward.py`
  - [ ] `positional_encoding.py`
  - [ ] `encoder.py`
  - [ ] `decoder.py`
  - [ ] `transformer.py`

**Day 3**
- [ ] Read Section 3.2 (Scaled Dot-Product Attention).
- [ ] Implement `scaled_dot_product_attention(q, k, v, mask)` in `attention.py`.
- [ ] Write test `tests/test_attention.py::test_scaled_dot_product_attention`.

**Day 4**
- [ ] Re-read Section 3.2 for Multi-Head Attention.
- [ ] Implement `MultiHeadAttention` in `attention.py`.
- [ ] Write test `tests/test_attention.py::test_multihead_shapes`.

**Day 5**
- [ ] Read Section 3.3 (Feedforward Networks).
- [ ] Implement `FeedForward` in `feedforward.py`.
- [ ] Write test `tests/test_feedforward.py`.

**Day 6**
- [ ] Read Section 3.5 (Positional Encoding).
- [ ] Implement sinusoidal positional encoding in `positional_encoding.py`.
- [ ] Visualize with `notebooks/positional_encoding.ipynb`.

**Day 7**
- [ ] Re-read Sections 3.1–3.4.
- [ ] Refactor code for clarity and match diagram.
- [ ] Commit progress to GitHub.

---

## Week 2 — Assembly + Training

**Day 8**
- [ ] Implement `EncoderLayer` in `encoder.py` (MHA + FFN + residual + layer norm).
- [ ] Stack into `Encoder` module.

**Day 9**
- [ ] Implement `DecoderLayer` in `decoder.py` (masked MHA + cross-attn + FFN).
- [ ] Stack into `Decoder` module.

**Day 10**
- [ ] Assemble `Transformer` in `transformer.py`.
- [ ] Test forward pass on random tensors.

**Day 11**
- [ ] Read Section 5 (Training).
- [ ] Implement loss (cross-entropy w/ label smoothing) in `loss.py`.

**Day 12**
- [ ] Add dataset loader in `data.py` for IWSLT’14 En→De subset.
- [ ] Test batching in `tests/test_data.py`.

**Day 13**
- [ ] Run short training loop in `train.py` (few thousand steps).
- [ ] Check learning curve logs.

**Day 14**
- [ ] Save trained model to `checkpoints/`.
- [ ] Sample translations in `inference.py`.
- [ ] Write project `README.md` mapping components to paper sections.
