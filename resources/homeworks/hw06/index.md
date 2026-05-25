---
layout: page
title: "Homework 6: Rank and Inverses"
description: "Homework 6: Rank and Inverses problems."
nav_exclude: true
hide_footer_hr: true
---

{% raw %}

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

# Homework 6: Rank and Inverses

**due** Sunday, May 31st, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw06/hw06.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 5 Solutions Review](#problem-1-homework-5-solutions-review-10-pts)
- [Problem 2: Rank-Nullity Practice](#problem-2-rank-nullity-practice-9-pts)
- [Problem 3: Spaces](#problem-3-spaces-16-pts)
- [Problem 4: Numbers of Solutions](#problem-4-numbers-of-solutions-12-pts)
- [Problem 5: Projecting onto a Single Vector](#problem-5-projecting-onto-a-single-vector-12-pts)
- [Problem 6: Invertibility of $XX^T$](#problem-6-invertibility-of-xxt-5-pts)
- [Problem 7: Trickster](#problem-7-trickster-5-pts)
- [Problem 8: Sherman-Morrison Inverse](#problem-8-sherman-morrison-inverse-22-pts)

---

Total Points: 10 + 9 + 16 + 12 + 12 + 5 + 5 + 22 = 91

---

## Problem 1: Homework 5 Solutions Review (10 pts)

Review the solutions to Homework 5. Pick **two problem parts** (for example, Problem 2a and Problem 4b) from Homework 5 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 5, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Rank-Nullity Practice (9 pts)

Recall from [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#rank-nullity-theorem) that the rank-nullity theorem states that for any <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(A\\)</span>,

<div class="math-display">
$$
\text{rank}(A) + \text{dim}(\text{nullsp}(A)) = \underbrace{\text{number of columns in } A}_{d}
$$
</div>

In each part, identify whether the statement is true or false, and explain why.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(A\\)</span> with <span class="math-inline">\\(\text{rank}(A) = 4\\)</span> and <span class="math-inline">\\(\text{dim}(\text{colsp}(A)) = 3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(B\\)</span> with <span class="math-inline">\\(\text{rank}(B) = 3\\)</span> and <span class="math-inline">\\(\text{dim}(\text{nullsp}(B)) = 2\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(C\\)</span> with <span class="math-inline">\\(\text{dim}(\text{nullsp}(C)) = 4\\)</span> and <span class="math-inline">\\(\text{dim}(\text{nullsp}(C^T)) = 1\\)</span>.

</div>
</div>

</div>

---

## Problem 3: Spaces (16 pts)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\text{nullsp}(A) = \text{span}\left(\left\{\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix}\right\}\right)
$$
</div>

What is <span class="math-inline">\\(\text{rank}(A)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\text{nullsp}(A) = \text{span}\left(\left\{\begin{bmatrix} 2 \\\\ 2 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix}\right\}\right)
$$
</div>

What is <span class="math-inline">\\(\text{rank}(A)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 1 \\\\ 5 \end{bmatrix} \in \text{colsp}(A), \quad \begin{bmatrix} 0 \\\\ 3 \\\\ 1 \end{bmatrix} \in \text{colsp}(A), \quad \begin{bmatrix} 1 \\\\ 1 \\\\ 2 \end{bmatrix} \in \text{nullsp}(A)
$$
</div>

What is <span class="math-inline">\\(\text{rank}(A)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} 8 \\\\ -2 \\\\ 3 \end{bmatrix}\\)</span>. Explain why there **does not** exist a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\vec u \in \text{colsp}(A), \quad \vec v \in \text{nullsp}(A^T)
$$
</div>

and propose one change we could make to <span class="math-inline">\\(\vec v\\)</span> that would allow such an <span class="math-inline">\\(A\\)</span> to exist.

<em>Hint: In the <a href="https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements">Orthogonal Complements example in Chapter 5.4</a>, and in <a href="https://youtu.be/dcqA-6-vYA4">this video</a>, we discuss a fact related to this question. If you want to make a claim about the required relationship between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, you need to re-prove it here. This shouldn't take too many lines of work.</em>

</div>
</div>

</div>

---

## Problem 4: Numbers of Solutions (12 pts)

Recall that if <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix, <span class="math-inline">\\(\vec x \in \mathbb{R}^d\\)</span>, and <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>, then

<div class="math-display">
$$
A \vec x = \vec b
$$
</div>

 is a system of <span class="math-inline">\\(n\\)</span> equations in <span class="math-inline">\\(d\\)</span> unknowns, where the unknowns are the components of <span class="math-inline">\\(\vec x\\)</span>, i.e. <span class="math-inline">\\(x&#95;1\\)</span>, <span class="math-inline">\\(x&#95;2\\)</span>, <span class="math-inline">\\(\ldots\\)</span>, <span class="math-inline">\\(x&#95;d\\)</span>. Solving this system is equivalent to writing <span class="math-inline">\\(\vec b\\)</span> as a **linear combination of the columns of <span class="math-inline">\\(A\\)</span>**.

In each part, do two things:

1.  Construct a matrix <span class="math-inline">\\(A\\)</span> for which the number of solutions (that is, number of valid <span class="math-inline">\\(\vec x\\)</span>'s) to the system <span class="math-inline">\\(A \vec x = \vec b\\)</span> is the number provided.

2.  Determine whether the function <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span> is one-to-one, onto, both, or neither. (See [Chapter 6.2](https://notes.eecs245.org/linear-transformations-and-projections/inverses/#inverting-a-transformation) for a refresher on the definitions.)

The first part has been done for you as an example.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(1\\)</span>, depending on <span class="math-inline">\\(\vec b\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\infty\\)</span>, no matter what <span class="math-inline">\\(\vec b\\)</span> is

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(\infty\\)</span>, depending on what <span class="math-inline">\\(\vec b\\)</span> is

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(1\\)</span>, no matter what <span class="math-inline">\\(\vec b\\)</span> is

</div>
</div>

</div>

---

## Problem 5: Projecting onto a Single Vector (12 pts)

In Homework 6, Problem 3, you found that the <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(P\\)</span> that projects <span class="math-inline">\\(\vec u \in \mathbb{R}^2\\)</span> onto the unit vector <span class="math-inline">\\(\vec v \in \mathbb{R}^2\\)</span> was

<div class="math-display">
$$
P = \begin{bmatrix} v_1^2 & v_1v_2 \\\\ v_1v_2 & v_2^2 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Find:

1.  <span class="math-inline">\\(\text{rank}(P)\\)</span>

2.  A basis for <span class="math-inline">\\(\text{colsp}(P)\\)</span>

3.  A basis for <span class="math-inline">\\(\text{nullsp}(P)\\)</span>

4.  A basis for <span class="math-inline">\\(\text{colsp}(P^T)\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Explain why <span class="math-inline">\\(P\\)</span> is not invertible, and then explain why the transformation <span class="math-inline">\\(f(\vec u) = P \vec u\\)</span> can't be reversed.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) As mentioned in Homework 6, Problem 3, <span class="math-inline">\\(P\\)</span> is an idempotent matrix, meaning that

<div class="math-display">
$$
P^2 = P
$$
</div>

In general, if <span class="math-inline">\\(P^2 = P\\)</span> and <span class="math-inline">\\(P\\)</span> is invertible, what must <span class="math-inline">\\(P\\)</span> be?

<em>Hint: Multiply both sides of <span class="math-inline">\\(P^2 = P\\)</span> by <span class="math-inline">\\(P^{-1}\\)</span>.</em>

</div>
</div>

</div>

---

## Problem 6: Invertibility of <span class="math-inline">\\(XX^T\\)</span> (5 pts)

In [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-rank-of-x-tx), and in [this video](https://youtu.be/hOyaHqGmO1I), we proved that <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^TX)\\)</span>.

Here, we'll ask you to prove something similar involving <span class="math-inline">\\(XX^T\\)</span>. Note that <span class="math-inline">\\(X^TX\\)</span> is a matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s **columns**, while <span class="math-inline">\\(XX^T\\)</span> is a matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s **rows**. (This has fact had something to do with Homework 6, Problem 4!)

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix, and <span class="math-inline">\\(XX^T\\)</span> is invertible. Find and explain **all** inequalities that **must** be true between <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(d\\)</span>, and <span class="math-inline">\\(r = \text{rank}(X)\\)</span>.

---

## Problem 7: Trickster (5 pts)

Find a matrix <span class="math-inline">\\(A\\)</span> that is **not equal to the identity matrix**, but where <span class="math-inline">\\(A^6 = I\\)</span>.

Once you think of your answer, you should explain how you found it, and should use Python to verify that <span class="math-inline">\\(A^6 = I\\)</span> holds. Include a screenshot of your Python code.

<em>Hint: This problem has a trick to it, and to think of it, I'd suggest reading the <a href="https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#rotations-and-orthogonal-matrices">Rotations and Orthogonal Matrices section of Chapter 6.2</a>.</em>

---

## Problem 8: Sherman-Morrison Inverse (22 pts)

In EECS 280 or EECS 281, you may have learned about **memoization**, which involves storing results of an earlier calculation to help speed up future calculations. This problem involves something similar.

Suppose we have an <span class="math-inline">\\(n \times n\\)</span> matrix <span class="math-inline">\\(A\\)</span> whose inverse, <span class="math-inline">\\(A^{-1}\\)</span>, we already know. Remember that finding inverses in general is a difficult task, so once we've found one, we'd like to avoid having to invert again.

And, suppose that we need to know the inverse of

<div class="math-display">
$$
B = A + \vec u \vec v^T
$$
</div>

which is the sum of <span class="math-inline">\\(A\\)</span> and a rank 1 matrix created by taking the "outer product" of <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> (as discussed in [Chapter 5.3](https://notes.eecs245.org/matrices/rank-and-column-space/#example-vector-outer-product)). Think of <span class="math-inline">\\(B\\)</span> as a small update to <span class="math-inline">\\(A\\)</span>.

The Sherman-Morrison formula states that

<div class="math-display">
$$
B^{-1} = (A + \vec u \vec v^T)^{-1} = A^{-1} - \frac{A^{-1} \vec u \vec v^T A^{-1}}{1 + \vec v^T A^{-1} \vec u}
$$
</div>

The formula allows us to find the inverse of <span class="math-inline">\\(A + \vec u \vec v^T\\)</span> just by knowing <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(A^{-1}\\)</span>, meaning we don't need to recompute the inverse!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) To start, we'll consider a simpler case of the Sherman-Morrison formula, where <span class="math-inline">\\(A = I\\)</span>, the identity matrix. Then, since <span class="math-inline">\\(I = I^{-1}\\)</span>, the matrix we're inverting is

<div class="math-display">
$$
B = A + \vec u \vec v^T
$$
</div>

and its inverse is

<div class="math-display">
$$
B^{-1} = (I + \vec u \vec v^T)^{-1} = I - \frac{\vec u \vec v^T}{1 + \vec v^T \vec u}
$$
</div>

<span class="math-inline">\\(B\\)</span> is invertible, **except when** the denominator of the fraction above is 0, i.e. <span class="math-inline">\\(1 + \vec v^T \vec u = 0\\)</span>.

When <span class="math-inline">\\(1 + \vec v^T \vec u = 0\\)</span>, what is true about <span class="math-inline">\\(B\\)</span>?

<em>Hint: Evaluate <span class="math-inline">\\(B \vec u\\)</span>. What does the result tell you about <span class="math-inline">\\(\text{nullsp}(B)\\)</span>?</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Prove that as long as <span class="math-inline">\\(1 + \vec v^T \vec u \neq 0\\)</span>, that

<div class="math-display">
$$
(I + \vec u \vec v^T) \left( I - \frac{\vec u \vec v^T}{1 + \vec v^T \vec u} \right) = I
$$
</div>

(Yes, this involves a fair bit of algebra.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Now, let's return to the full-fledged Sherman-Morrison formula, where

<div class="math-display">
$$
B = A + \vec u \vec v^T, \qquad B^{-1} = (A + \vec u \vec v^T)^{-1} = A^{-1} - \frac{A^{-1} \vec u \vec v^T A^{-1}}{1 + \vec v^T A^{-1} \vec u}
$$
</div>

Open the **supplemental Jupyter Notebook** we've created for Homework 6, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw06%2Fhw06.ipynb&branch=main) on DataHub, or [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw06/hw06.ipynb) in the course GitHub repository.

There, you're asked to implement the Sherman-Morrison formula, and run some experiments to quantify how much quicker using the formula is than computing the inverse of <span class="math-inline">\\(B\\)</span> from scratch.

This problem is **not autograded**. Rather, in your submission to this part, include screenshots of your implementations of functions `generate_random_data`, `invert_B_directly`,

`invert_B_with_sherman_morrison`, `run_one_experiment`, and `many_experiments_mean_sd`, along with their outputs on the provided examples.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Include screenshots of the code you used to call `many_experiments_mean_sd` for the values provided in the question, the outputs of the print statements you were asked to add, and the `plotly` line chart you were asked to create.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Answer the question posed at the end of the supplemental Jupyter Notebook. (This shouldn't be a screenshot; just write your answer in this PDF the same way you answered Problems 1-7.)

If you're curious, look into [Low-Rank Adaptions (LoRA)](https://www.ibm.com/think/topics/lora), a relatively recent development in large language model research! The general idea is the same as we've worked with here.
</div>
</div>

</div>

{% endraw %}
