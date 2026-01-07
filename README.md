# Instructional Safety Evaluation

An empirical study of how safely frontier language models teach, and where automated evaluation falls short.

## Research Questions

1. **How do frontier LLMs differ in their instructional safety behavior?**
2. **Where do LLM-as-judge evaluations fail to catch unsafe teaching patterns?**

## Project Overview

This project evaluates 3 language models on 6 instructional safety tasks, using both human scoring and an LLM judge. The goal is to identify failure modes in model teaching behavior and understand the limitations of automated evaluation.

**Key outputs:**
- `RESEARCH_LOG.md` — Research process documentation
- `FINDINGS.md` — Paper-style writeup of results
- `evals/` — Raw data (responses and scores)

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up API keys

```bash
cp .env.example .env
```

Edit `.env` with your keys:

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AI...
```

### 3. Run data collection

```bash
python run_evals.py
```

### 4. Human scoring

Score each response in `evals/responses/` using `rubric.json`. Record in `evals/scores/human_scores.csv`.

### 5. Automated scoring

```bash
python run_judge.py
```

### 6. Write up findings

Complete `FINDINGS.md` with your analysis.

---

## Repository Structure

```
├── README.md                 # This file
├── RESEARCH_LOG.md           # Document your research process here
├── FINDINGS.md               # Your research writeup (paper-style)
│
├── run_evals.py              # Collect responses from all models
├── run_judge.py              # Run LLM-as-judge scoring
├── tasks.json                # The 6 evaluation tasks
├── rubric.json               # Scoring dimensions (0-2 scale)
│
├── examples/
│   └── scored_examples.md    # Practice scoring before real data
│
└── evals/
    ├── responses/            # Raw model outputs
    │   ├── gpt-4o/
    │   ├── claude-sonnet/
    │   └── gemini-pro/
    └── scores/
        ├── human_scores.csv  # Your scores
        └── judge_scores.csv  # Automated scores
```

---

## Commit Guide

Your commit history should document your research process:

```
Initial project setup
Add initial hypotheses to research log
Complete data collection: 18 responses from 3 models
Complete human scoring for GPT-4o
Complete human scoring for all models
Complete automated evaluation with LLM judge
Draft findings writeup
Finalize findings and analysis
```

---

## Files Reference

| File | Purpose |
|------|---------|
| `tasks.json` | 6 prompts testing different instructional safety aspects |
| `rubric.json` | 5 scoring dimensions with 0-2 scale definitions |
| `examples/scored_examples.md` | Calibration examples to practice scoring |
| `RESEARCH_LOG.md` | Template for documenting your process |
| `FINDINGS.md` | Template for your research writeup |

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"

```bash
pip install -r requirements.txt
```

### "AuthenticationError" or "Invalid API key"

Check `.env` — no spaces around `=`, correct keys, sufficient quota.

### "Rate limit exceeded"

Wait a minute and retry. The script runs sequentially to minimize this.

### Using different models

Edit the `models` list in `run_evals.py`.

---

## License

MIT License — see [LICENSE](LICENSE) for details.

## Credits

Work by **Tram Le** in collaboration with **Professor Mark Johnson**.
