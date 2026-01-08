# Research Log

This log documents my research process, observations, and thinking throughout the project.

---

## Phase 1: Setup & Planning

### [01/07/2026]: Initial Hypotheses

**Before looking at any data, my predictions:**

- Claude-Sonnet-4.5 handles pedagogical edge cases well, particularly in situtations involving emtional pressure, indirect attempts to bypass the academic integrity, or ambiguous requests.
- Gemini 2.5 pro might be a reliable pedagogical edge cases that require strict rule adherence and consistency. 
- GPT-4.1 might give instant answer and provide more help than appropriate.

**Which model will perform best overall?**

Overall, I think GPT-4.1 has the best overall performance. Based on my personal experience, the GPT-4.1 model exhibits comprehensive reasoning, providing helpful responses. Specifically, it functions as a reliable "teacher" when it comes to delivering clear and structured instructions for any purpose. With a strong reinforcement learning from human feedback and self-evaluation, GPT-4.1 has demonstrated a remarkable ability to follow detailed instructions while maintaining coherence in complicated tasks. While GPT-4.0  already handled a significant amount of tokens without limitation, GPT-4.1 presents a more substantial improvement, especially in its impressive management of large amounts of text, code, images, or complex structured data.

**Which tasks will be hardest for models?**

Academic integrity and Emotional pressure will be the most concerning because the models autonomously resolve complex issues if not restricted. In most cases, the models will balance between guiding and refusing unethical assistance. However, when humans express vulnerability, they eventually exploit empathy-aligned training, which creates tensions with refusal policies. Overall, the AI assistance needs to be helpful, honest, and harmless at the same time which makes it harder.

**Where will the LLM judge struggle?**

The LLM judges tend to exhibit a significant self-preference bias, rating their own generated text more favorably than content produced by humans or other models. With a self-recognition capability, LLM can distinguish its own outputs, leading to a self-preference. The LLM judge also struggles to evaluate because of the verbosity bias. It systematically prefers longer answers over shorter ones, regardless of the quality of extra length. Lastly, with the lack of reasoning and limited expertise, LLM may overlook subtle logical or factual errors if the text is well-written and coherent. As the context windows increase, its reasoning accuracy degrades, particularly for tasks more complex than simple information retrieval.

---

## Phase 2: Data Collection

### [01/07/2026]: Data Collection Notes

**Issues encountered:**

Everything runs smoothly.

**Initial impressions from skimming responses:**

- Without the system prompt, Claude-Sonnet-4.5 appears to satisfy most of the evaluation criteria, followed by Gemini-2.5, with GPT-4.1 performing the weakest. In the first task, despite adopting slightly different approaches, three models all gave the answers without encouraging the users to attempt the problems by themselves. The thing that surprises me the most is that GPT-4.1 fails most of the tasks related to adversarial resistance and academic integrity (Tasks 7,8,9, and 10). 

- With the system prompt, Claude-Sonnet-4.5 continues to perform as the best model. Although GPT-4.1 shows an improvement in its response, it still does not meet the requirement when compared to Gemini-2.5.

---

## Phase 3: Human Evaluation

### [07/01/2026]: Scoring Observations

**Hardest responses to score:**

[Which ones? Why were they difficult?]

**Surprising results:**

[Anything that contradicted your hypotheses?]

**Patterns emerging:**

[Any failure modes becoming apparent?]

---

## Phase 4: Automated Evaluation

### [DATE]: Judge Comparison

**Where the judge agreed with me:**

[Examples and observations]

**Where the judge disagreed:**

[Examples and analysis of why]

**Patterns in disagreements:**

[Any systematic biases in the judge?]

---

## Phase 5: Analysis & Reflection

### [DATE]: Final Reflections

**What I learned:**

[Key takeaways from this project]

**What surprised me most:**

[Unexpected findings]

**Ideas for future research:**

[Questions this project raised]

---

## Notes & Ideas

[Space for additional observations, ideas, or notes that don't fit above]
