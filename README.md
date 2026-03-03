# 🔥 CHIMERA‑Hash Ultra

> Sentence‑by‑Sentence Web Intelligence Plagiarism Engine
> Fully Local • No API Keys • Full‑Page Source Extraction • Hybrid Similarity Scoring

---

## 🚀 Official Project Name

# **CHIMERA‑Hash Ultra: Deterministic Hybrid Similarity & Source Tracing Engine**

A locally running plagiarism detection system that:

* Splits text into individual sentences
* Searches each sentence as an exact quoted phrase
* Collects web search results from multiple engines
* Downloads full page content from discovered sources
* Scores similarity using a custom hybrid hashing model
* Generates a visual sentence‑level heatmap

No paid APIs. No external SaaS dependency. 100% executable from a single Python file.

---

# 🧠 Architecture Overview

CHIMERA‑Hash Ultra consists of three primary layers:

## 1️⃣ Frontend Engine (Embedded HTML UI)

* Fully embedded inside `plagcheck.py`
* Real‑time progress logs
* Sentence‑level heatmap
* Source ranking dashboard
* Risk classification system

## 2️⃣ Web Intelligence Layer

* DuckDuckGo HTML scraping
* Bing HTML scraping (fallback)
* Wikipedia API search
* Semantic Scholar API search
* Full‑page content extraction
* DOM cleaning and noise removal

## 3️⃣ CHIMERA‑Hash v5 Similarity Core

Hybrid deterministic scoring using:

| Component        | Weight | Purpose                         |
| ---------------- | ------ | ------------------------------- |
| Vector Jaccard   | 0.35   | Token overlap similarity        |
| Chaos Index      | 0.37   | Non‑linear hashed token mapping |
| Bigram Cosine    | 0.18   | Character‑level similarity      |
| Numeric Matching | 0.10   | Number consistency validation   |

Additional Safeguards:

* Longest Common Subsequence dampening
* Short‑word asymmetry detection
* Code‑pattern false positive suppression
* Sliding window best‑match detection

All scores normalized to range `[0, 1]`.

---

# ⚙️ How It Works (Technical Flow)

1. User pastes text.
2. Text is split into sentences.
3. Each sentence ≥ 8 words is searched as an exact quoted phrase.
4. Search engines return candidate URLs.
5. Unique URLs are deduplicated.
6. Full HTML page is fetched.
7. Scripts, nav, footer, ads are removed.
8. Main article content extracted.
9. CHIMERA‑Hash similarity score computed.
10. Top sources ranked and displayed.

Time complexity roughly:

O(S × E × F)

Where:

* S = number of sentences
* E = search engines queried
* F = fetched pages

---

# 📊 Similarity Interpretation Model

| Score     | Classification    | Meaning              |
| --------- | ----------------- | -------------------- |
| 0.85+     | High Plagiarism   | Direct match online  |
| 0.65–0.84 | Likely Plagiarism | Strong similarity    |
| 0.45–0.64 | Moderate Overlap  | Partial reuse        |
| 0.20–0.44 | Minor Similarity  | Possible coincidence |
| <0.20     | Appears Original  | No significant match |

Sentence heatmap colors:

* 🔴 Very High (75%+)
* 🟠 High (55–74%)
* 🟡 Moderate (35–54%)
* 🟢 Low
* ⚪ Clean

---

# 🛠 Installation

## Requirements

* Python 3.9+
* No external libraries required

## Run

```bash
python plagcheck.py
```

Then open:

```
http://localhost:7477
```

The browser auto‑opens by default.

---

# 📂 Project Structure

```
plagcheck.py
└── Embedded UI (HTML + CSS + JS)
└── Search Engine Layer
    ├── DuckDuckGo HTML parser
    ├── Bing HTML parser
    ├── Wikipedia API
    └── Semantic Scholar API
└── Full Page Extraction Engine
└── CHIMERA‑Hash v5 Similarity Core
└── Local HTTP Server
```

Single file deployment.

---

# 🔬 Why CHIMERA‑Hash Is Different

Unlike basic cosine similarity plagiarism tools, this system:

✔ Searches sentence‑by‑sentence
✔ Uses exact quoted phrase detection
✔ Downloads full source content
✔ Uses multi‑layer deterministic similarity
✔ Penalizes false positives
✔ Handles numeric consistency
✔ Detects structural similarity
✔ Avoids shallow keyword overlap bias

This significantly reduces both:

* Type I errors (false positives)
* Type II errors (missed plagiarism)

---

# 🧩 Core Mathematical Components

## Vector Jaccard

J(A,B) = |A ∩ B| / |A ∪ B|

Applied to tokens length ≥ 4.

## Chaos Index

Uses logistic map transformation:

xₙ₊₁ = 3.9x(1 − x)

Token hash buckets aggregated across multiple radii.

## Bigram Cosine

Character‑level similarity using cosine distance.

## LCS Normalization

Used to dampen artificially high overlaps.

---

# 🌍 Ethical & Legal Notes

* Designed for academic analysis and content originality validation.
* Uses public search engines.
* No API keys required.
* Respects crawl pacing via delay throttling.

---

# 🔐 Security Characteristics

* No remote server dependency
* No database storage
* No data retention
* Localhost only
* No telemetry

All analysis happens on the user machine.

---

# 📈 Future Enhancements (Optional Roadmap)

* Parallel sentence search
* TF‑IDF adaptive weighting
* Academic DOI resolution
* PDF source extraction
* Distributed crawling mode
* API wrapper version

---

# 👨‍💻 Author

**Manish Kumar Parihar**
YouTube: @ProgramDr
Research: CHIMERA‑Hash Similarity Model

---

# 🏁 Final Statement

CHIMERA‑Hash Ultra is not a simple plagiarism checker.

It is a deterministic hybrid similarity engine designed to identify exact origin sources using structural, lexical, numerical, and chaotic hash analysis.

If you want a fully local, research‑grade plagiarism tracing engine — this is it.

---

# ⭐ License

MIT License (recommended)
You may modify, distribute, and improve with attribution.
