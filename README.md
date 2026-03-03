# 🔍 PlagCheck Pro — Powered by CHIMERA-Hash v5

**Sentence-Level Web Source Tracing & Deterministic Hybrid Similarity Engine**

PlagCheck Pro is a fully local plagiarism detection system that performs exact sentence-by-sentence web search, downloads full source pages, and scores similarity using the research-grade **CHIMERA-Hash v5 hybrid model**.

It is not a shallow cosine checker.  
It is a deterministic multi-signal source tracing engine.

---

# 🧠 Core Philosophy

Most plagiarism tools:

- Use embeddings or TF-IDF
- Depend on private corpora
- Operate as black-box SaaS systems
- Do not reveal scoring logic

PlagCheck Pro instead:

- Searches each sentence independently as an exact quoted phrase
- Fetches full webpage content (not just snippets)
- Applies deterministic hybrid similarity scoring
- Runs 100% locally
- Produces interpretable structural signals

---

# 🏗 System Architecture

## 1️⃣ Sentence Intelligence Engine

- Text split into sentences
- Sentences ≥ 8 words searched as exact quoted phrase
- Uses DuckDuckGo HTML + Bing fallback
- Deduplicates URLs

This allows original source tracing instead of approximate semantic guessing.

---

## 2️⃣ Full Page Extraction Engine

For every discovered URL:

- Fetch full HTML
- Remove scripts, styles, nav, footer
- Extract main article body
- Normalize and clean text

Prevents snippet bias and improves scoring precision.

---

## 3️⃣ CHIMERA-Hash v5 Similarity Core

Hybrid deterministic similarity model:

| Component | Weight | Function |
|------------|--------|----------|
| Vector Jaccard | 0.35 | Token overlap (≥4 chars) |
| Chaos Index | 0.37 | Non-linear logistic map hashing |
| Bigram Cosine | 0.18 | Character-level similarity |
| Numeric Jaccard | 0.10 | Factual consistency validation |

### Logistic Map

xₙ₊₁ = 3.9x(1 − x)

Used for chaos-weighted token mapping.

---

## Advanced Safeguards

- LCS structural dampening
- SAUR (Short-Alpha-Unique Ratio) negation detection
- Numeric mismatch penalty
- Code pattern suppression
- Sliding window best-match extraction

Scores normalized to range [0, 1].

---

# 📊 Score Interpretation

| Score | Verdict |
|--------|----------|
| ≥ 0.85 | High Plagiarism |
| 0.65–0.84 | Likely Plagiarism |
| 0.45–0.64 | Moderate Overlap |
| 0.20–0.44 | Minor Similarity |
| < 0.20 | Appears Original |

Includes:
- Sentence heatmap
- High-risk sentence count
- Ranked source list

---

# 🔬 Comparison With Other Tools

| Feature | PlagCheck Pro | Turnitin | Grammarly | Copyscape | Embedding Models |
|----------|---------------|----------|------------|------------|------------------|
| Local Execution | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No |
| Sentence Exact Search | ✅ Yes | Partial | No | Limited | No |
| Full Page Fetch | ✅ Yes | Unknown | No | No | No |
| Transparent Scoring | ✅ Yes | ❌ Black box | ❌ Black box | ❌ Black box | ❌ Black box |
| Corpus Required | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| Numeric Variation Handling | ✅ Yes | Unknown | No | No | Weak |
| Negation Detection | ✅ Yes | Unknown | No | No | No |

PlagCheck Pro focuses on **traceable origin detection**, not only semantic similarity approximation.

---

# ⚙️ Run

```bash
python plagcheck.py
```

Open:
```
http://localhost:7477
```

---

# 📈 Computational Model

If:
S = sentences  
E = engines  
F = fetched pages  

Complexity ≈ O(S × E + F × L)

Where L is processed page length.

---

# 📚 Research Foundation

Powered by:

**CHIMERA-Hash v5 — Hybrid Chaos-Weighted Similarity Model**

DOI:
https://doi.org/10.5281/zenodo.18824917  
https://doi.org/10.5281/zenodo.18823652  

Author: Manish Kumar Parihar  
ORCID: https://orcid.org/0009-0002-1900-8945  
YouTube: https://www.youtube.com/@ProgramDr  
GitHub: https://github.com/nickzq7  

---

# 🔐 Security

- 100% Localhost execution
- No telemetry
- No cloud storage
- No external dependency

---

# 📜 License

MIT License

---

PlagCheck Pro is a deterministic sentence-level source tracing engine powered by CHIMERA-Hash v5 — designed for researchers, educators, and developers who require mathematical transparency and reproducible similarity scoring.
