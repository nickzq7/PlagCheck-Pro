```markdown
# 🔍 PlagCheck Pro (CHIMERA-Hash Ultra v5)

[![Built By](https://img.shields.io/badge/Built%20By-Manish%20Kumar%20Parihar-blue?style=for-the-badge)](https://youtube.com/@ProgramDr)
[![YouTube](https://img.shields.io/badge/YouTube-@ProgramDr-red?style=for-the-badge&logo=youtube)](https://youtube.com/@ProgramDr)
[![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Free-green?style=for-the-badge)](#)
[![Paper](https://img.shields.io/badge/DOI-10.5281/zenodo.18824917-purple?style=for-the-badge)](https://doi.org/10.5281/zenodo.18824917)

**PlagCheck Pro** is a revolutionary, 100% free, and fully local plagiarism detection engine. Powered by the proprietary **CHIMERA-Hash Ultra v5** algorithm, this tool completely abandons traditional TF-IDF corpus-dependent models in favor of chaos theory and logistic maps. 

Designed for students, researchers, and developers, it runs entirely on your local machine, requires **NO API keys**, and automatically scrapes search engines and massive academic databases to find exact source matches for your text.

---

## 🥊 How It Compares to the Industry Giants

Most commercial plagiarism checkers hide behind massive paywalls, store your private data, and use outdated algorithms. Here is how PlagCheck Pro completely changes the game:

| Feature | PlagCheck Pro (CHIMERA v5) | Turnitin | Grammarly Pro | Copyscape |
| :--- | :--- | :--- | :--- | :--- |
| **Cost** | **100% Free Forever** | Expensive Institutional License | Costly Monthly Subscription | Pay-Per-Search |
| **Data Privacy** | **Total (Runs Locally, No DB)** | Stores your text in their database | Processed on their servers | Processed on their servers |
| **Search Mechanism** | **Sentence-by-Sentence Exact Match** | Bulk document comparison | General web crawl | General web crawl |
| **Underlying Math** | **Chaos Theory / Logistic Maps** | String matching & TF-IDF | Proprietary ML | Fingerprinting |
| **API Keys Required**| **None (Native HTTP Requests)** | N/A | N/A | Premium API Key |
| **Academic Databases**| **Semantic Scholar (200M+ papers)** | Yes (Proprietary DB) | ProQuest | No |

---

## 🚀 The Core Features: Why It's Built Different

### 1. Zero-Cost, API-Free Architecture
Unlike commercial plagiarism checkers that charge per word or require expensive API subscriptions, PlagCheck Pro relies purely on native Python HTTP requests. It intelligently queries public search engines (DuckDuckGo, Bing) by mimicking real browser headers, bypassing the need for developer keys or paid scraping services.

### 2. Sentence-by-Sentence Forensic Search
Instead of searching a whole document at once (which often fails to find cobbled-together or heavily edited plagiarism), the engine:
* Splits your input text into individual sentences.
* Takes the first 12 significant words of each valid sentence.
* Wraps them in quotes `("example text...")` to force search engines to find **exact phrase matches**.
* Compiles a massive, deduplicated list of unique URLs from the internet where those exact phrases appear.

### 3. Full-Page Context Reading
Search snippets are often too short to accurately calculate plagiarism percentages. PlagCheck Pro physically visits every single discovered URL, strips away the HTML, CSS, and JavaScript, and extracts the raw article text. It then scans the *entire* target webpage against your input to find the highest-density match blocks using a sliding window technique.

### 4. Deep Academic Integration
Alongside standard web scraping, the engine automatically extracts core keywords from your text and queries:
* **Semantic Scholar:** Scans a database of over 200 million academic papers for abstract matches.
* **Wikipedia:** Pulls directly from the Wiki API for encyclopedic cross-referencing.

### 5. Beautiful Local Web UI
The Python script features an embedded, modern dark-mode HTML/CSS/JS frontend. It spins up a lightweight local server (`localhost:7477`) that provides:
* **Real-time Server Logging:** Watch the scraper fetch pages, bypass blocks, and score sources live.
* **Sentence-Level Heatmap:** Hover over your text to see exactly which sentences are flagged (Green = Original, Yellow = Tweaked, Red = Direct Copy).
* **Interactive Source Ranking:** Displays matched URLs, similarity percentages, and visual risk gauges.

---

## 🧠 Deep Dive: The CHIMERA-Hash Ultra v5 Algorithm

At the heart of PlagCheck Pro is **CHIMERA-Hash**, a completely novel approach to text similarity that operates independently of a trained machine-learning corpus. It calculates a multi-dimensional similarity score by combining several advanced metrics:

* **Chaotic Iteration Similarity (ci):** Uses a logistic map formula (r=3.9) to generate chaotic weightings for individual tokens. It distributes tokens across dynamic hash rings (R=[16, 32, 64, 128, 256]) to map structural similarity without relying on word frequencies.
* **Vocabulary Jaccard (vj):** Measures the pure intersection of significant words (length >= 4) between two texts.
* **Bigram Cosine (bc):** Analyzes the exact sequencing of characters by converting text into character-level bigrams and computing the cosine similarity between their frequency vectors.
* **Numeric Jaccard Cap:** Specifically isolates and compares numbers to prevent factual variation (e.g., changing "25%" to "35%") from being marked as a perfect match.
* **Longest Common Subsequence (lcs):** Finds the absolute longest unbroken chain of shared alpha-tokens to catch direct copy-pasting.
* **Short-Alpha-Unique Ratio (saur):** A custom penalty function designed to handle negations and subtle phrasing tricks (e.g., distinguishing "The system is active" from "The system is not active").

The final score is a highly-tuned weighted average of these components, dynamically penalized if certain thresholds are triggered (e.g., high bigram match but low semantic overlap).

---

## 🛠️ Installation & Usage

Because the entire engine, UI, and scraper are bundled into a single file, setup takes less than 10 seconds.

### Prerequisites
* Python 3.x installed on your system.
* **No external libraries are required!** You do NOT need to run `pip install`. The script strictly uses Python's standard library (`threading`, `json`, `urllib`, `http.server`, etc.).

### Run the Checker
1. Clone this repository or download the `plagcheck.py` file directly.
   ```bash
   git clone [https://github.com/nickzq7/chimera-hash-ultra.git](https://github.com/nickzq7/chimera-hash-ultra.git)
   cd chimera-hash-ultra

```

2. Open your terminal or command prompt.
3. Run the script:
```bash
python plagcheck.py

```


4. A browser window will automatically open to `http://localhost:7477`.
5. Paste your text (minimum 10 words) and click **Check for Plagiarism**.

*Note: A thorough check takes 30-60 seconds, as the engine respects server rate limits while forensically searching every single sentence online.*

---

## 📊 Understanding the Verdicts

The UI grades your text from **A** to **F** based on the highest matched source:

* 🟢 **Grade A (0-19%): APPEARS ORIGINAL** - No significant matches found.
* 🟢 **Grade B (20-44%): MINOR SIMILARITY** - Likely coincidental phrasing or common idioms.
* 🟡 **Grade C (45-64%): MODERATE OVERLAP** - Notable overlap. Review highlighted sentences carefully.
* 🟠 **Grade D (65-84%): LIKELY PLAGIARISM** - Strong similarity detected. Citation needed for all matched sources.
* 🔴 **Grade F (85-100%): HIGH PLAGIARISM** - Direct match found online. Must attribute the source.

---

## 🔬 Research & Documentation

The mathematical foundation and benchmark testing for CHIMERA-Hash are detailed in our official research publication.

* **Read the Paper:** [DOI: 10.5281/zenodo.18824917](https://doi.org/10.5281/zenodo.18824917)

## 👨‍💻 Connect with the Creator

This tool was designed and engineered by **Manish Kumar Parihar**.

If you are interested in the architecture behind this tool, Artificial General Intelligence (AGI), Python programming, algorithmic trading (LMPM), or highly optimized logic frameworks like SĀM̐KHYA and Hypervision, join the community!

* 📺 **YouTube:** [@ProgramDr](https://youtube.com/@ProgramDr)
* 🐙 **GitHub:** [nickzq7](https://www.google.com/search?q=https://github.com/nickzq7)

---

*Disclaimer: Web scraping functionality relies on the current DOM structure of public search engines. Excessive requests from a single IP address may result in temporary rate-limiting by the search providers.*

```

```
