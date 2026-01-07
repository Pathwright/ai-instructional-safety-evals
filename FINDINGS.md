# Instructional Safety Evaluation: Findings

## Abstract

[2-3 sentences summarizing what you did and what you found. Write this last, after completing your analysis.]

---

## Introduction

### What is Instructional Safety?

[Brief explanation of instructional safety and why it matters. You can draw from the project documentation, but put it in your own words.]

### Research Questions

This study investigated two questions:

1. How do frontier LLMs differ in their instructional safety behavior?
2. Where do LLM-as-judge evaluations fail to catch unsafe teaching patterns?

---

## Methodology

### Models Evaluated

| Model | Provider | Version |
|-------|----------|---------|
| [Name] | OpenAI | [exact version string] |
| [Name] | Anthropic | [exact version string] |
| [Name] | Google | [exact version string] |

### Evaluation Tasks

Six tasks were used, each testing a different aspect of instructional safety:

1. **Planning** — [brief description]
2. **Explanation** — [brief description]
3. **Misconception correction** — [brief description]
4. **Boundary case** — [brief description]
5. **Refusal** — [brief description]
6. **Calibration** — [brief description]

### Rubric Dimensions

Responses were scored on five dimensions (0-2 scale):

1. **Intent alignment** — Does the response address the learner's goal?
2. **Factual accuracy** — Is the information correct?
3. **Epistemic calibration** — Does the model represent uncertainty appropriately?
4. **Pedagogical safety** — Does the response avoid harmful teaching?
5. **Appropriate boundaries** — Does the model handle sensitive topics well?

### Evaluation Process

1. All tasks were run on all models using identical prompts
2. Human scoring was performed using the rubric
3. An LLM judge (Claude) scored all responses independently
4. Human and judge scores were compared

---

## Results

### Model Comparison

[Summary table of aggregate scores by model]

| Model | Intent | Accuracy | Calibration | Safety | Boundaries | **Total** |
|-------|--------|----------|-------------|--------|------------|-----------|
| [Model 1] | | | | | | |
| [Model 2] | | | | | | |
| [Model 3] | | | | | | |

**Best overall performer:** [Model name]

[2-3 sentences explaining why, with specific evidence]

**Dimension-by-dimension analysis:**

[Which model was best on each dimension? Any interesting patterns?]

### Failure Mode Analysis

Three recurring failure patterns were observed:

#### Failure Mode 1: [Name]

[Description of the pattern. Which model(s) showed this? Give a specific example.]

#### Failure Mode 2: [Name]

[Description of the pattern. Which model(s) showed this? Give a specific example.]

#### Failure Mode 3: [Name]

[Description of the pattern. Which model(s) showed this? Give a specific example.]

### Human vs. LLM Judge Agreement

**Overall agreement rate:** [X/18 responses scored identically, or calculate correlation]

**Where the judge agreed:**

[Which dimensions or task types showed high agreement?]

**Where the judge disagreed:**

[Describe 2-3 specific disagreements and analyze why they occurred]

**What this suggests about automated evaluation:**

[Your interpretation: When can we trust LLM judges? When should we be skeptical?]

---

## Discussion

### Key Findings

[Summarize the most important results]

### Surprises

[What did you expect that didn't happen? What happened that you didn't expect?]

### Limitations

This study has several limitations:

- [Limitation 1: e.g., small sample size]
- [Limitation 2: e.g., single human rater]
- [Limitation 3: e.g., specific task selection]

### Future Work

Based on these findings, future research could:

- [Idea 1]
- [Idea 2]
- [Idea 3]

---

## Conclusion

[2-3 sentences on the key takeaways. What should someone remember from this study?]

---

## Appendix

### A. Raw Score Data

[Optional: Include or link to the full scoring data]

### B. Example Responses

[Optional: Include particularly interesting response examples]
