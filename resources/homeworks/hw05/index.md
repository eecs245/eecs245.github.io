---
layout: page
title: "Homework 5: Linear Independence and Subspaces"
description: "Homework 5: Linear Independence and Subspaces problems."
nav_exclude: true
hide_footer_hr: true
---

<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
}
.assignment-actions {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin: 0 0 1rem;
}
.answer-blank {
  border-bottom: 1px solid currentColor;
  display: inline-block;
  min-width: 8rem;
  height: 1em;
  vertical-align: baseline;
}
.assignment-parts {
  margin: 1rem 0;
}
.assignment-part {
  column-gap: 0.55rem;
  display: grid;
  grid-template-columns: 1.4rem minmax(0, 1fr);
  margin-bottom: 1.05rem;
}
.assignment-part-label {
  font-weight: 600;
  text-align: right;
}
.assignment-part-content > :first-child {
  margin-top: 0;
}
.mc-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem 1.6rem;
  margin: 0.9rem 0 1.1rem;
}
.mc-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
}
.mc-bubble,
.mc-square {
  display: inline-block;
  flex: 0 0 auto;
  height: 0.95em;
  width: 0.95em;
  vertical-align: -0.12em;
}
.mc-bubble {
  border: 1.5px solid currentColor;
  border-radius: 50%;
}
.mc-square {
  border: 1.5px solid currentColor;
}
.mc-correct {
  background: currentColor;
}
.main-content table {
  font-size: 0.9rem;
  width: auto;
  max-width: 100%;
}
.main-content table th,
.main-content table td {
  padding: 0.35rem 0.5rem;
  white-space: nowrap;
}
</style>

# Homework 5: Linear Independence and Subspaces

**due** Thursday, May 28th, 2026 at 11:59PM Ann Arbor Time

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 4 Solutions Review](#problem-1-homework-4-solutions-review-10-pts)
- [Problem 2: Linear Independence of New Vectors](#problem-2-linear-independence-of-new-vectors-8-pts)
- [Problem 3: Thinking in Higher Dimensions](#problem-3-thinking-in-higher-dimensions-8-pts)
- [Problem 4: Intersections of Subspaces](#problem-4-intersections-of-subspaces-6-pts)

---

Total Points: 10 + 8 + 8 + 6 = 32

---

## Problem 1: Homework 4 Solutions Review (10 pts)

Review the solutions to Homework 4. Pick **two problem parts** (for example, Problem 2a and Problem 4b) from Homework 4 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 4, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Linear Independence of New Vectors (8 pts)

Suppose <span class="math-inline">\\(\vec v_1, \vec v_2, \vec v_3 \in \mathbb{R}^n\\)</span> **are linearly independent**. In both parts below, determine if the new set of vectors is linearly independent. If they are, prove that they are by showing that the only solution to the equation

<div class="math-display">
$$
a \vec u_1 + b \vec u_2 + c \vec u_3 = \vec 0
$$
</div>

is <span class="math-inline">\\(a = b = c = 0\\)</span>. If they are not, show that there exist scalars <span class="math-inline">\\(a, b, c\\)</span> such that <span class="math-inline">\\(a \vec u_1 + b \vec u_2 + c \vec u_3 = \vec 0\\)</span> where at least one of <span class="math-inline">\\(a, b, c\\)</span> is non-zero.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\vec u_1 = \vec v_2 - \vec v_3\\)</span>, <span class="math-inline">\\(\vec u_2 = \vec v_1 - \vec v_3\\)</span>, and <span class="math-inline">\\(\vec u_3 = \vec v_1 - \vec v_2\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\vec u_1 = \vec v_2 + \vec v_3\\)</span>, <span class="math-inline">\\(\vec u_2 = \vec v_1 + \vec v_3\\)</span>, and <span class="math-inline">\\(\vec u_3 = \vec v_1 + \vec v_2\\)</span>

</div>
</div>

</div>

---

## Problem 3: Thinking in Higher Dimensions (8 pts)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Suppose <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_8\\)</span> are 8 vectors in <span class="math-inline">\\(\mathbb{R}^5\\)</span>. Fill in each blank below with one of the provided options, and explain your reasoning.

1.  These vectors \_\_\_\_\_\_\_\_ span all of <span class="math-inline">\\(\mathbb{R}^5\\)</span>.

    (options: do, do not, might)

2.  These vectors \_\_\_\_\_\_\_\_ linearly independent.

    (options: are, are not, might be)

3.  Any 5 of these vectors \_\_\_\_\_\_\_\_ span all of <span class="math-inline">\\(\mathbb{R}^5\\)</span>.

    (options: do, do not, might)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose <span class="math-inline">\\(\vec u_1, \vec u_2, \ldots, \vec u_{10}\\)</span> are 10 non-zero vectors in <span class="math-inline">\\(\mathbb{R}^{11}\\)</span>.

Furthermore, suppose that <span class="math-inline">\\(\text{span}(\lbrace\vec u_1, \vec u_2, \ldots, \vec u_{10}\rbrace)\\)</span> is a 6-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^{11}\\)</span>. This means that there exists a subset of 6 of these vectors that is linearly independent and spans the same 6-dimensional subspace as the original 10 vectors; we just don't know which 6.

1.  Let <span class="math-inline">\\(k\\)</span> be the dimension of the subspace spanned by a subset of 4 of these vectors. What are all possible values of <span class="math-inline">\\(k\\)</span>?

2.  Let <span class="math-inline">\\(m\\)</span> be the dimension of the subspace spanned by a subset of 7 of these vectors. What are all possible values of <span class="math-inline">\\(m\\)</span>?

</div>
</div>

</div>

---

## Problem 4: Intersections of Subspaces (6 pts)

Let:

-   <span class="math-inline">\\(M\\)</span> be the subspace of <span class="math-inline">\\(\mathbb{R}^4\\)</span> spanned by <span class="math-inline">\\(\begin{bmatrix}1 \\\\ 1 \\\\ 1 \\\\ 0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}0 \\\\ -4 \\\\ 1 \\\\ 5\end{bmatrix}\\)</span>

-   <span class="math-inline">\\(N\\)</span> be the subspace of <span class="math-inline">\\(\mathbb{R}^4\\)</span> spanned by <span class="math-inline">\\(\begin{bmatrix}0 \\\\ -2 \\\\ 1 \\\\ 2\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}1 \\\\ -1 \\\\ 1 \\\\ 3\end{bmatrix}\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find a vector that belongs to both <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(N\\)</span>. (In other words, find a vector <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(\vec v \in M\\)</span> and <span class="math-inline">\\(\vec v \in N\\)</span>.) There are infinitely many answers; state the answer with a first component of 1.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Fill in the blank and explain your reasoning: the set of all vectors that belong to both <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(N\\)</span> is a subspace of <span class="math-inline">\\(\mathbb{R}^4\\)</span> with dimension .
</div>
</div>

</div>
