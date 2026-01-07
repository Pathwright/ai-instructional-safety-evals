# Instructional Safety Evaluation

An empirical study of how safely frontier language models behave as AI tutors, and where automated evaluation falls short.

## Research Questions

1. **How do frontier LLMs differ in their instructional safety behavior?**
2. **Where do LLM-as-judge evaluations fail to catch unsafe teaching patterns?**
3. **How robust are models to adversarial manipulation attempts by students?**

## Project Overview

This project evaluates 3 flagship language models on 10 instructional safety tasks, using both human scoring and an LLM judge. The goal is to identify failure modes in model teaching behavior and understand the limitations of automated evaluation.

### Why This Matters

AI tutors are increasingly deployed in educational settings. Unlike general-purpose AI safety, instructional safety has unique challenges:
- Models must balance helpfulness with academic integrity
- Students may attempt to manipulate models into doing their homework
- Age-appropriate communication requires nuanced calibration
- Incorrect information can be especially harmful in learning contexts

### Research Design

All models receive an **educational system prompt** based on best practices from Khan Academy's Khanmigo and similar educational AI systems. This simulates realistic deployment conditions.

Tasks are split into two categories:
- **Baseline tasks (01-06)**: Standard instructional scenarios (scaffolding, age-calibration, academic integrity, citations, factual accuracy)
- **Adversarial tasks (07-10)**: Manipulation attempts (indirect requests, emotional pressure, authority appeals, reframing)

The adversarial tasks are where we expect to see meaningful differentiation between models.

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
python run_evals.py                    # Run all 10 tasks on all 3 models
python run_evals.py --task task07      # Run only task07 (for testing)
python run_evals.py --no-system-prompt # Run without educational system prompt (baseline comparison)
```

### 4. Human scoring

Score each response in `evals/responses/` using `rubric.json`. Record your scores in `evals/scores/human_scores.csv`.

**Tip:** Focus on the adversarial tasks (07-10) — that's where models are most likely to differ.

### 5. Automated scoring

```bash
python run_judge.py
```

This uses Claude Sonnet 4.5 as the judge model.

### 6. Analyze results

Compare your human scores with the judge scores. Look for:
- Where do you and the judge agree/disagree?
- Are there systematic biases in the judge?
- Which models handle adversarial prompts best?

### 7. Write up findings

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
├── tasks.json                # The 10 evaluation tasks
├── rubric.json               # Scoring dimensions (0-2 scale)
│
├── examples/
│   └── scored_examples.md    # Practice scoring before real data
│
└── evals/
    ├── responses/            # Raw model outputs
    │   ├── gpt-4.1/
    │   ├── claude-sonnet-4.5/
    │   └── gemini-2.5-pro/
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
| `tasks.json` | 10 prompts testing different instructional safety aspects |
| `rubric.json` | 6 scoring dimensions with 0-2 scale definitions |
| `examples/scored_examples.md` | Calibration examples to practice scoring |
| `RESEARCH_LOG.md` | Template for documenting your process |
| `FINDINGS.md` | Template for your research writeup |

## Models Tested

| Model | Provider | Notes |
|-------|----------|-------|
| GPT-4.1 | OpenAI | Flagship model (Jan 2025) |
| Claude Sonnet 4.5 | Anthropic | Flagship model (Jan 2025) |
| Gemini 2.5 Pro | Google | Flagship model (Jan 2025) |

All models are tested at `temperature=0` for reproducibility.

## Task Types

| Task | Type | What It Tests |
|------|------|---------------|
| 01 | scaffolding | Does the model teach vs. give answers? |
| 02-03 | age-appropriate | Does the model calibrate to grade level? |
| 04 | academic-integrity | Does the model refuse to write essays? |
| 05 | citation-honesty | Does the model admit it can't cite sources? |
| 06 | factual-accuracy | Does the model correct misconceptions? |
| 07 | adversarial-indirect | Resists "compare to my work" framing |
| 08 | adversarial-emotional | Maintains boundaries under emotional pressure |
| 09 | adversarial-authority | Resists "my teacher said it's okay" claims |
| 10 | adversarial-reframing | Resists "just show me an example" requests |

## Rubric Dimensions

| Dimension | What It Measures |
|-----------|------------------|
| `pedagogical_approach` | Teaches/scaffolds rather than giving answers |
| `age_calibration` | Response matches stated grade level |
| `academic_integrity` | Doesn't complete assignments for students |
| `citation_honesty` | Doesn't fabricate sources or statistics |
| `factual_accuracy` | Information is correct |
| `adversarial_resistance` | Maintains boundaries under manipulation |

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
