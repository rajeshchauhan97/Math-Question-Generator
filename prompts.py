PROMPT = r"""
You are an exam content author. Given the BASE questions below, generate TWO NEW multiple-choice math questions
similar in format and difficulty. MUST preserve any LaTeX in questions or solutions.

BASE QUESTIONS:
1) Each student at Central Middle School wears a uniform consisting of 1 shirt and 1 pair of pants. The table shows the colors available for each item of clothing. How many different uniforms are possible?

| Shirt Color | Pants Color |
| :---: | :---: |
| Tan | Black |
| Red | Khaki |
| White | Navy |
| Yellow |  |

2) The top view of a rectangular package of 6 tightly packed balls is shown. If each ball has a radius of 2 centimeters, which of the following are closest to the dimensions, in centimeters, of the rectangular package?
(A) $2 \times 3 \times 6$
(B) $4 \times 6 \times 6$
(C) $2 \times 4 \times 6$
(D) $4 \times 8 \times 12$
(E) $6 \times 8 \times 12$

INSTRUCTIONS:
- Output **only valid JSON** (no extra text). JSON must be an array of two objects.
- Each object must contain these keys:
  title, description, question, instruction, difficulty, Order,
  options (array of strings), correct (exact option string that is correct),
  explanation, subject, unit, topic, plusmarks (integer),
  image_description (a short text prompt used to generate an image illustrating the question).
- Preserve LaTeX (e.g., $...$) where needed in question or explanation.
- Keep text concise (each question around 2-6 lines). Provide simple image descriptions.
- Example JSON structure:
[ { "title": "...", ... }, { ... second question ... } ]
"""