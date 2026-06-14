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
.math-display,
mjx-container[jax="CHTML"][display="true"] {
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
}
.math-display {
  padding-bottom: 0.2rem;
}
.math-display mjx-container[jax="CHTML"][display="true"] {
  padding-bottom: 0.2rem;
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
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw06/hw06-solutions.pdf" target="_blank">Solutions PDF ✅</a>
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

Review [the solutions to Homework 5](https://eecs245.org/resources/homeworks/hw05/). Pick **two problem parts** (for example, Problem 2a and Problem 4b) from Homework 5 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 5, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

<details markdown="1"><summary>Solution</summary>

</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\text{False}}\\)</span>. <span class="math-inline">\\(\text{rank}(A) = \text{dim}(\text{colsp}(A))\\)</span> for any matrix <span class="math-inline">\\(A\\)</span> by definition.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(B\\)</span> with <span class="math-inline">\\(\text{rank}(B) = 3\\)</span> and <span class="math-inline">\\(\text{dim}(\text{nullsp}(B)) = 2\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\text{True}}\\)</span>. In fact, every <span class="math-inline">\\(4 \times 5\\)</span> matrix with <span class="math-inline">\\(\text{rank}(B) = 3\\)</span> must have <span class="math-inline">\\(\text{dim}(\text{nullsp}(B)) = 2\\)</span>.

This is because the rank-nullity theorem tells us that

<div class="math-display">
$$
\text{rank}(B) + \text{dim}(\text{nullsp}(B)) = \text{\# columns in } B = 5
$$
</div>

 so if <span class="math-inline">\\(\text{rank}(B) = 3\\)</span>, then <span class="math-inline">\\(\text{dim}(\text{nullsp}(B)) = 2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(C\\)</span> with <span class="math-inline">\\(\text{dim}(\text{nullsp}(C)) = 4\\)</span> and <span class="math-inline">\\(\text{dim}(\text{nullsp}(C^T)) = 1\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\boxed{\text{False}}\\)</span>.

Suppose <span class="math-inline">\\(C\\)</span> is a <span class="math-inline">\\(4 \times 5\\)</span> matrix with <span class="math-inline">\\(\text{dim}(\text{nullsp}(C)) = 4\\)</span>. Then, by the rank-nullity theorem,

<div class="math-display">
$$
\text{rank}(C) + \text{dim}(\text{nullsp}(C)) = 5 \implies \text{rank}(C) = 5 - 4 = 1
$$
</div>

But then, applying the rank-nullity theorem to <span class="math-inline">\\(C^T\\)</span> and using the fact that <span class="math-inline">\\(\text{rank}(C^T) = \text{rank}(C) = 1\\)</span>, we have

<div class="math-display">
$$
\text{rank}(C^T) + \text{dim}(\text{nullsp}(C^T)) = 4 \implies \text{dim}(\text{nullsp}(C^T)) = 4 - 1 = 3
$$
</div>

But, the question states that <span class="math-inline">\\(\text{dim}(\text{nullsp}(C^T)) = 1\\)</span>, so we have a contradiction. Therefore, no such matrix <span class="math-inline">\\(C\\)</span> exists.
</details>

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

<details markdown="1"><summary>Solution</summary>

Recall, <span class="math-inline">\\(\text{nullsp}(A)\\)</span> is the set of all vectors <span class="math-inline">\\(\vec x\\)</span> such that <span class="math-inline">\\(A\vec x = \vec 0\\)</span>. We have that:

**(i)** <span class="math-inline">\\(\text{nullsp}(A)\\)</span> is a 1-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^4\\)</span>.

**(ii)** <span class="math-inline">\\(A\\)</span> has 4 columns, because the null space is made up of vectors in <span class="math-inline">\\(\mathbb{R}^4\\)</span>; <span class="math-inline">\\(A\\)</span> must have 4 columns in order for <span class="math-inline">\\(A \begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span> to be a valid product.

**(iii)** The above two facts imply, from the rank-nullity theorem, that <span class="math-inline">\\(\text{rank}(A) + 1 = 4 \implies \text{rank}(A) = 3\\)</span>.

We know that <span class="math-inline">\\(A\\)</span> has 3 linearly independent columns, and 4 total columns. We don't know how many rows it has, but it must have at least 3 rows since <span class="math-inline">\\(\text{rank}(A) = 3\\)</span>.

The easiest solution is to make <span class="math-inline">\\(A\\)</span> a <span class="math-inline">\\(3 \times 4\\)</span> matrix. Let <span class="math-inline">\\(\vec a^{(1)}, \vec a^{(2)}, \vec a^{(3)}, \vec a^{(4)}\\)</span> be the columns of <span class="math-inline">\\(A\\)</span>. Then,

<div class="math-display">
$$
A\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix} = \begin{bmatrix} | & | & | & | \\\\ \vec a^{(1)} & \vec a^{(2)} & \vec a^{(3)} & \vec a^{(4)} \\\\ | & | & | & |\end{bmatrix} \begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix} = \vec 0
$$
</div>

 implies that <span class="math-inline">\\(A\\)</span>'s columns must satisfy

<div class="math-display">
$$
2 \vec a^{(1)} + \vec a^{(2)} + \vec a^{(4)} = \vec 0
$$
</div>

So, we just need to pick 4 vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> such that one of them is a linear combination of the others, and the above relationship is satisfied. The above relationship gives us a dependency relationship between <span class="math-inline">\\(\vec a^{(1)}\\)</span>, <span class="math-inline">\\(\vec a^{(2)}\\)</span>, and <span class="math-inline">\\(\vec a^{(4)}\\)</span>, so we can accomplish both goals at the same time.

Let's pick <span class="math-inline">\\(\vec a^{(1)} = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec a^{(2)} = \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec a^{(3)} = \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>. There's nothing special about these choices other than that the numbers are small and simple; you could have picked any three linearly independent vectors. Note that <span class="math-inline">\\(\vec a^{(3)}\\)</span> doesn't appear in the relationship above; <span class="math-inline">\\(\vec a^{(1)}\\)</span>, <span class="math-inline">\\(\vec a^{(2)}\\)</span>, and <span class="math-inline">\\(\vec a^{(4)}\\)</span> all do, so now we can find the required <span class="math-inline">\\(\vec a^{(4)}\\)</span> by solving the equation <span class="math-inline">\\(2 \vec a^{(1)} + \vec a^{(2)} + \vec a^{(4)} = \vec 0\\)</span>.

<div class="math-display">
$$
\vec a^{(4)} = -2 \vec a^{(1)} - \vec a^{(2)} = \begin{bmatrix} -2 \\\\ -1 \\\\ 0 \end{bmatrix}
$$
</div>

So, one possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\boxed{A = \begin{bmatrix} 1 &amp; 0 &amp; 0 &amp; -2 \\\\ 0 &amp; 1 &amp; 0 &amp; -1 \\\\ 0 &amp; 0 &amp; 1 &amp; 0 \end{bmatrix}}\\)</span>, which has <span class="math-inline">\\(\boxed{\text{rank}(A) = 3}\\)</span>.
</details>

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

<details markdown="1"><summary>Solution</summary>

Following the logic from the last subpart, <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) = 2\\)</span> and <span class="math-inline">\\(A\\)</span> must have 4 columns, so

<div class="math-display">
$$
\text{rank}(A) = 4 - 2 = 2
$$
</div>

So, the easiest example will involve a <span class="math-inline">\\(2 \times 4\\)</span> matrix <span class="math-inline">\\(A\\)</span>. If <span class="math-inline">\\(A = \begin{bmatrix} | &amp; | &amp; | &amp; | \\\\ \vec a^{(1)} &amp; \vec a^{(2)} &amp; \vec a^{(3)} &amp; \vec a^{(4)} \\\\ | &amp; | &amp; | &amp; |\end{bmatrix}\\)</span>, then it must be the case that

<span class="math-inline">\\(A \begin{bmatrix} 2 \\\\ 2 \\\\ 1 \\\\ 0 \end{bmatrix} = \vec 0\\)</span> and <span class="math-inline">\\(A \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix} = \vec 0\\)</span>. This gives us two conditions on <span class="math-inline">\\(\vec a^{(1)}, \vec a^{(2)}, \vec a^{(3)}, \vec a^{(4)}\\)</span>:

<div class="math-display">
$$
2 \vec a^{(1)} + 2 \vec a^{(2)} + \vec a^{(3)} = \vec 0
$$
</div>

<div class="math-display">
$$
3 \vec a^{(1)} + \vec a^{(2)} + \vec a^{(4)} = \vec 0
$$
</div>

<span class="math-inline">\\(\vec a^{(1)}\\)</span> and <span class="math-inline">\\(\vec a^{(2)}\\)</span> appear in both equations, so it might be easiest to make those the two linearly independent columns (remember that <span class="math-inline">\\(\text{rank}(A) = 2\\)</span>). So, let's make them <span class="math-inline">\\(\vec a^{(1)} = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec a^{(2)} = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span>. Now, we can solve for <span class="math-inline">\\(\vec a^{(3)}\\)</span> and <span class="math-inline">\\(\vec a^{(4)}\\)</span> by solving the two equations:

<div class="math-display">
$$
\vec a^{(3)} = -2 \vec a^{(1)} - 2 \vec a^{(2)} = \begin{bmatrix} -2 \\\\ -2 \end{bmatrix}
$$
</div>

<div class="math-display">
$$
\vec a^{(4)} = -3 \vec a^{(1)} - \vec a^{(2)} = \begin{bmatrix} -3 \\\\ -1 \end{bmatrix}
$$
</div>

So, one possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\boxed{A = \begin{bmatrix} 1 &amp; 0 &amp; -2 &amp; -3 \\\\ 0 &amp; 1 &amp; -2 &amp; -1 \end{bmatrix}}\\)</span>, which has <span class="math-inline">\\(\boxed{\text{rank}(A) = 2}\\)</span>.

Just to verify that we did this correctly, let's take a linear combination of <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 2 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span> and check that multiplying <span class="math-inline">\\(A\\)</span> by that linear combination gets us to <span class="math-inline">\\(\vec 0\\)</span>. How about

<div class="math-display">
$$
\vec v = 5 \begin{bmatrix} 2 \\\\ 2 \\\\ 1 \\\\ 0 \end{bmatrix} + 2 \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 16 \\\\ 12 \\\\ 5 \\\\ 2 \end{bmatrix}
$$
</div>

Indeed,

<div class="math-display">
$$
A \vec v = \begin{bmatrix} 1 & 0 & -2 & -3 \\\\ 0 & 1 & -2 & -1 \end{bmatrix} \begin{bmatrix} 16 \\\\ 12 \\\\ 5 \\\\ 2 \end{bmatrix} = \begin{bmatrix} 16 - 2 \cdot 5 - 3 \cdot 2 \\\\ 12 - 2 \cdot 5 - 1 \cdot 2 \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix} = \vec 0
$$
</div>

so it seems like we found a valid <span class="math-inline">\\(A\\)</span>.
</details>

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

<details markdown="1"><summary>Solution</summary>

We know that <span class="math-inline">\\(A\\)</span> has 3 rows, because <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 5 \end{bmatrix}\\)</span> is a linear combination of <span class="math-inline">\\(A\\)</span>'s columns, which must be in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. It also has 3 columns, because the null space is made up of vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span>; <span class="math-inline">\\(A\\)</span> must have 3 columns in order for <span class="math-inline">\\(A \begin{bmatrix} 1 \\\\ 1 \\\\ 2 \end{bmatrix}\\)</span> to be a valid product.

So, <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3 \times 3\\)</span> matrix.

There are two linearly independent columns in the column space of <span class="math-inline">\\(A\\)</span>, so <span class="math-inline">\\(A\\)</span> must have at least 2 linearly independent columns, meaning <span class="math-inline">\\(\text{rank}(A) \geq 2\\)</span>. However, the null space contains a non-zero vector, so <span class="math-inline">\\(A\\)</span> must have exactly 2 linearly independent columns and a null space of dimension 1, meaning <span class="math-inline">\\(\text{rank}(A) = 2\\)</span>.

The easiest path forward is to make <span class="math-inline">\\(A\\)</span> a <span class="math-inline">\\(3 \times 3\\)</span> matrix whose first column is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 5 \end{bmatrix}\\)</span> and whose second column is <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span>. Then, we can solve for the third column by solving the equation <span class="math-inline">\\(A \begin{bmatrix} 1 \\\\ 1 \\\\ 2 \end{bmatrix} = \vec 0\\)</span> (or <span class="math-inline">\\(A \begin{bmatrix} 2 \\\\ 2 \\\\ 4 \end{bmatrix} = \vec 0\\)</span>, or <span class="math-inline">\\(A (\text{any scalar multiple of } \begin{bmatrix} 1 \\\\ 1 \\\\ 2 \end{bmatrix}) = \vec 0\\)</span>).

If we let <span class="math-inline">\\(A = \begin{bmatrix}1 &amp; 0 &amp; c&#95;1 \\\\ 1 &amp; 3 &amp; c&#95;2 \\\\ 5 &amp; 1 &amp; c&#95;3 \end{bmatrix}\\)</span>, then we have the following system of equations:

<div class="math-display">
$$
\begin{align*}
A\begin{bmatrix} 1 \\\\ 1 \\\\ 2 \end{bmatrix} &= \vec{0} \\\\
\implies \begin{bmatrix} 1 & 0 & c_1 \\\\ 1 & 3 & c_2 \\\\ 5 & 1 & c_3 \end{bmatrix}
\begin{bmatrix} 1 \\\\ 1 \\\\ 2 \end{bmatrix} &=
\begin{bmatrix}
1 \cdot 1 + 0 \cdot 1 + c_1 \cdot 2 \\\\
1 \cdot 1 + 3 \cdot 1 + c_2 \cdot 2 \\\\
5 \cdot 1 + 1 \cdot 1 + c_3 \cdot 2 \\\\
\end{bmatrix}
=
\begin{bmatrix}
1 + 2c_1 \\\\
4 + 2c_2 \\\\
6 + 2c_3
\end{bmatrix}
= \vec{0}
\end{align*}
$$
</div>

This is satisfied by <span class="math-inline">\\(c&#95;1 = -\frac{1}{2}\\)</span>, <span class="math-inline">\\(c&#95;2 = -2\\)</span>, and <span class="math-inline">\\(c&#95;3 = -3\\)</span>, so one possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\boxed{A = \begin{bmatrix} 1 &amp; 0 &amp; -\frac{1}{2} \\\\ 1 &amp; 3 &amp; -2 \\\\ 5 &amp; 1 &amp; -3 \end{bmatrix}}\\)</span>, with <span class="math-inline">\\(\boxed{\text{rank}(A) = 2}\\)</span>.
</details>

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

<details markdown="1"><summary>Solution</summary>

The reason is that **every element of <span class="math-inline">\\(\text{colsp}(A)\\)</span> is orthogonal to every element of <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span>**. Sometimes, this is phrased as the column space and null space being <span class="math-inline">\\(\textbf{orthogonal complements}\\)</span>.

Why is this the case? Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix where <span class="math-inline">\\(\vec u \in \text{colsp}(A)\\)</span> and <span class="math-inline">\\(\vec v \in \text{nullsp}(A^T)\\)</span>. The definition of <span class="math-inline">\\(\vec u \in \text{colsp}(A)\\)</span> is that there exists some other vector <span class="math-inline">\\(\vec y\\)</span> such that

<div class="math-display">
$$
\vec u = A \vec y
$$
</div>

Here, <span class="math-inline">\\(\vec u \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(\vec y \in \mathbb{R}^d\\)</span>.

The definition of <span class="math-inline">\\(\vec v\\)</span> is that

<div class="math-display">
$$
A^T \vec v = \vec 0
$$
</div>

Likewise, <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>.

Then,

<div class="math-display">
$$
\vec u \cdot \vec v = (A \vec y) \cdot \vec v = (A \vec y)^T \vec v = \vec y^T A^T \vec v = \vec y^T \vec 0 = 0
$$
</div>

So, if <span class="math-inline">\\(\vec u \in \text{colsp}(A)\\)</span> and <span class="math-inline">\\(\vec v \in \text{nullsp}(A^T)\\)</span>, then <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> must be orthogonal.

This explains why there doesn't exist a matrix <span class="math-inline">\\(A\\)</span> where <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 4 \end{bmatrix} \in \text{colsp}(A)\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 8 \\\\ -2 \\\\ 3 \end{bmatrix} \in \text{nullsp}(A^T)\\)</span>, since these vectors aren't orthogonal, as their dot product is <span class="math-inline">\\(8 - 6 + 12 = 14 \neq 0\\)</span>.

A change to <span class="math-inline">\\(\vec v\\)</span> that would allow such an <span class="math-inline">\\(A\\)</span> to exist is to change its first component to <span class="math-inline">\\(-6\\)</span>; then,

<div class="math-display">
$$
\vec u \cdot \vec v = \begin{bmatrix} 1 \\\\ 3 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} -6 \\\\ -2 \\\\ 3 \end{bmatrix} = -6 + -6 + 12 = 0
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

**(i)** If there are either 0 or 1 solutions, we know that <span class="math-inline">\\(A\\)</span>'s columns must be linearly independent. This is because if a given set of vectors is linearly independent, then any linear combination of them can only be written in one way (a fact that we proved in Chapter 2.6). <span class="math-inline">\\(A\\)</span>'s columns must also **not** span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, since there are some <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span> with no solutions for <span class="math-inline">\\(\vec x\\)</span>, so <span class="math-inline">\\(A\\)</span> must have fewer columns than rows.

One possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 \\\\ 0 &amp; 2 \\\\ 0 &amp; 0 \end{bmatrix}\\)</span>. For example, <span class="math-inline">\\(\vec b = \begin{bmatrix} -3 \\\\ 4 \\\\ 0 \end{bmatrix}\\)</span> only has a single solution for <span class="math-inline">\\(\vec x\\)</span>, which is <span class="math-inline">\\(\vec x = \begin{bmatrix} -3 \\\\ 2 \end{bmatrix}\\)</span>, while <span class="math-inline">\\(\vec c = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}\\)</span> has no solution for <span class="math-inline">\\(\vec x\\)</span>.

**(ii)** The function <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span> is one-to-one, but not onto. It is one-to-one because of the fact that any linear combination of <span class="math-inline">\\(A\\)</span>'s columns can only be written in one way, so if <span class="math-inline">\\(\vec x \neq \vec y\\)</span>, then <span class="math-inline">\\(A \vec x\\)</span> and <span class="math-inline">\\(A \vec y\\)</span> must also be different. It is not onto, since there are vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> (like <span class="math-inline">\\(\vec c\\)</span> above) that aren't the output of <span class="math-inline">\\(f(\vec x)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\infty\\)</span>, no matter what <span class="math-inline">\\(\vec b\\)</span> is

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(A\vec x = \vec b\\)</span> to have an infinite number of solutions, for every possible <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>, we need <span class="math-inline">\\(A\\)</span>'s **columns to be linearly dependent and span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span>**. We need its columns to span <span class="math-inline">\\(\mathbb{R}^n\\)</span> so there's at least one solution for every <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>, and we need its columns to be linearly dependent so that there are infinitely many ways to write any given <span class="math-inline">\\(\vec b \in \text{colsp}(A)\\)</span> through a linear combination of <span class="math-inline">\\(A\\)</span>'s columns.

One possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\boxed{A=\begin{bmatrix}1 &amp; 0 &amp; 0 &amp; 1 \\\\ 0 &amp; 1 &amp; 0 &amp; 1 \\\\ 0 &amp; 0 &amp; 1 &amp; 1\end{bmatrix}}\\)</span>. Pick any <span class="math-inline">\\(\vec b \in \mathbb{R}^3\\)</span> and there will be infinitely many vectors <span class="math-inline">\\(\vec x\\)</span> where <span class="math-inline">\\(A \vec x = \vec b\\)</span>.

The function <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span>\...

-   **is onto**, because the columns of <span class="math-inline">\\(A\\)</span> span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, meaning that all vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> are possible outputs of <span class="math-inline">\\(f(\vec x)\\)</span>.

-   **is not one-to-one**, because it's possible for two different vectors <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^4\\)</span> to result in <span class="math-inline">\\(A \vec x = A \vec y\\)</span>. For example, <span class="math-inline">\\(A \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix} = A \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 2 \end{bmatrix} = \begin{bmatrix} 2 \\\\ 2 \\\\ 2 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(\infty\\)</span>, depending on what <span class="math-inline">\\(\vec b\\)</span> is

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(A\vec x = \vec b\\)</span> to have either <span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(\infty\\)</span> solutions depending on <span class="math-inline">\\(\vec b\\)</span>, <span class="math-inline">\\(A\\)</span>'s columns **must be linearly dependent but must *not* span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span>**. This ensures that for some <span class="math-inline">\\(\vec b\\)</span> there are no solutions (when <span class="math-inline">\\(\vec b\\)</span> is not in the column space of <span class="math-inline">\\(A\\)</span>), and for any <span class="math-inline">\\(\vec b\\)</span> in the column space, there are infinitely many solutions (since the columns are linearly dependent).

One possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\boxed{A = \begin{bmatrix} 1 &amp; 0 &amp; 1 \\\\ 0 &amp; 1 &amp; 1 \\\\ 0 &amp; 0 &amp; 0 \end{bmatrix}}\\)</span>. For example, for <span class="math-inline">\\(\vec b = \begin{bmatrix} 2 \\\\ 2 \\\\ 0 \end{bmatrix}\\)</span>, there are infinitely many solutions for <span class="math-inline">\\(\vec x\\)</span>; <span class="math-inline">\\(\vec x = \begin{bmatrix} 0 \\\\ 0 \\\\ 2 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec x = \begin{bmatrix} -6 \\\\ -6 \\\\ 8 \end{bmatrix}\\)</span> both do the job. But for <span class="math-inline">\\(\vec b = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}\\)</span>, there are no solutions for <span class="math-inline">\\(\vec x\\)</span> in <span class="math-inline">\\(A \vec x = \vec b\\)</span>, since no linear combination of <span class="math-inline">\\(A\\)</span>'s columns can have a non-zero third component.

The function <span class="math-inline">\\(f(\vec x) = A\vec x\\)</span>\...

-   **is not onto**, because the columns of <span class="math-inline">\\(A\\)</span> do not span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span> (e.g., we can't reach <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}\\)</span>).

-   **is not one-to-one**, because it's possible for two different vectors <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^3\\)</span> to result in <span class="math-inline">\\(A \vec x = A \vec y\\)</span> as we saw above with <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 0 \\\\ 2 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -6 \\\\ -6 \\\\ 8 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(1\\)</span>, no matter what <span class="math-inline">\\(\vec b\\)</span> is

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(A\vec x = \vec b\\)</span> to have exactly one solution for every <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>, <span class="math-inline">\\(A\\)</span>'s columns **must be linearly independent and must span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span>**. This guarantees that for any <span class="math-inline">\\(\vec b\\)</span>, there is a *unique* solution <span class="math-inline">\\(\vec x\\)</span>.

One possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\boxed{A = \begin{bmatrix} 1 &amp; 0 &amp; 0 \\\\ 0 &amp; 1 &amp; 0 \\\\ 0 &amp; 0 &amp; 1 \end{bmatrix}}\\)</span>. Given any <span class="math-inline">\\(\vec b \in \mathbb{R}^3\\)</span>, <span class="math-inline">\\(A\vec x = \vec b\\)</span> always has the unique solution <span class="math-inline">\\(\vec x = \vec b\\)</span>.

The function <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span>\...

-   **is onto**, because the columns of <span class="math-inline">\\(A\\)</span> span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, so every vector in <span class="math-inline">\\(\mathbb{R}^n\\)</span> can be written as <span class="math-inline">\\(A\vec x\\)</span> for some <span class="math-inline">\\(\vec x\\)</span>.

-   **is one-to-one**, because the columns are linearly independent; if <span class="math-inline">\\(A\vec x&#95;1 = A\vec x&#95;2\\)</span> then <span class="math-inline">\\(\vec x&#95;1 = \vec x&#95;2\\)</span>.

Therefore, <span class="math-inline">\\(A\\)</span> is invertible.
</details>

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

<details markdown="1"><summary>Solution</summary>

**(i)** <span class="math-inline">\\(\boxed{\text{rank}(P)=1}\\)</span>. Both columns are scalar multiples of <span class="math-inline">\\(\begin{bmatrix} v&#95;1 \\\\ v&#95;2 \end{bmatrix}\\)</span>. Another way of looking at it is that <span class="math-inline">\\(\text{column 2} = \frac{v&#95;2}{v&#95;1} (\text{column 1})\\)</span>.

**(ii)** A basis for <span class="math-inline">\\(\text{colsp}(P)\\)</span> is <span class="math-inline">\\(\boxed{\left\lbrace \begin{bmatrix} v&#95;1 \\\\ v&#95;2 \end{bmatrix} \right\rbrace}\\)</span>; any linear combination of <span class="math-inline">\\(P\\)</span>'s columns is a scalar multiple of <span class="math-inline">\\(\begin{bmatrix} v&#95;1 \\\\ v&#95;2 \end{bmatrix}\\)</span>.

**(iii)** Since <span class="math-inline">\\(P\\)</span> has <span class="math-inline">\\(2\\)</span> columns and <span class="math-inline">\\(\text{rank}(P) = 1\\)</span>, the null space of <span class="math-inline">\\(P\\)</span> has dimension <span class="math-inline">\\(2 - 1 = 1\\)</span>, so a basis for <span class="math-inline">\\(\text{nullsp}(P)\\)</span> will contain just a single vector, and <span class="math-inline">\\(\text{nullsp}(P)\\)</span> will be the set of scalar multiples of that vector.

Let <span class="math-inline">\\(\vec{x} = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span> be a vector in <span class="math-inline">\\(\text{nullsp}(P)\\)</span>. Then,

<div class="math-display">
$$
P \vec{x} = \begin{bmatrix} v_1^2 & v_1 v_2 \\\\ v_1 v_2 & v_2^2 \end{bmatrix} \begin{bmatrix} x_1 \\\\ x_2 \end{bmatrix}
      = \begin{bmatrix} v_1^2 x_1 + v_1 v_2 x_2 \\\\ v_1 v_2 x_1 + v_2^2 x_2 \end{bmatrix} = \vec{0}
$$
</div>

By inspection, one possible solution is <span class="math-inline">\\(\vec x = \begin{bmatrix} - v&#95;2 \\\\ v&#95;1 \end{bmatrix}\\)</span>. Plugging this into both components of <span class="math-inline">\\(P \vec x = \vec 0\\)</span> gives us:

<div class="math-display">
$$
v_1^2 (-v_2) + v_1 v_2 (v_1) = 0 \\\\ v_1v_2(-v_2) + v_2^2 (v_1) = 0
$$
</div>

which is satisfied, so <span class="math-inline">\\(\boxed{\left\lbrace \begin{bmatrix} - v&#95;2 \\\\ v&#95;1 \end{bmatrix} \right\rbrace}\\)</span> is a basis for <span class="math-inline">\\(\text{nullsp}(P)\\)</span>. Any scalar multiple of <span class="math-inline">\\(\begin{bmatrix} - v&#95;2 \\\\ v&#95;1 \end{bmatrix}\\)</span> will also work.

**(iv)** Note that <span class="math-inline">\\(P = P^T\\)</span>, i.e. <span class="math-inline">\\(P\\)</span> is symmetric, so a basis for <span class="math-inline">\\(\text{colsp}(P)\\)</span> is also a basis for <span class="math-inline">\\(\text{colsp}(P^T)\\)</span>. So, <span class="math-inline">\\(\boxed{\left\lbrace \begin{bmatrix} v&#95;1 \\\\ v&#95;2 \end{bmatrix} \right\rbrace}\\)</span> is a basis for <span class="math-inline">\\(\text{colsp}(P^T)\\)</span>.

A worthwhile observation is that <span class="math-inline">\\(P\\)</span> is the outer product of <span class="math-inline">\\(\vec v = \begin{bmatrix} v&#95;1 \\\\ v&#95;2 \end{bmatrix}\\)</span> with itself, i.e. <span class="math-inline">\\(P = \vec v \vec v^T\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Explain why <span class="math-inline">\\(P\\)</span> is not invertible, and then explain why the transformation <span class="math-inline">\\(f(\vec u) = P \vec u\\)</span> can't be reversed.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(P\\)</span> is not invertible because <span class="math-inline">\\(\text{rank}(P)\neq 2\\)</span>, and an <span class="math-inline">\\(n \times n\\)</span> matrix must have rank <span class="math-inline">\\(n\\)</span> to be invertible.

When you project <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>, you're "losing information" because you no longer know the direction of the original <span class="math-inline">\\(\vec u\\)</span>. Different vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> might end up with the same projection onto <span class="math-inline">\\(\vec v\\)</span>, despite being different vectors, meaning the transformation isn't one-to-one, and hence can't be undone.
</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(P\\)</span> must be the **identity matrix**, <span class="math-inline">\\(I\\)</span>.

<div class="math-display">
$$
\begin{align*}
P^2 &= P \\\\
PP &= P \\\\
PPP^{-1} &= PP^{-1} \\\\
P\underbrace{(PP^{-1})}_{I} &= \underbrace{PP^{-1}}_{I} \\\\
P &= I
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 6: Invertibility of <span class="math-inline">\\(XX^T\\)</span> (5 pts)

In [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-rank-of-x-tx), and in [this video](https://youtu.be/hOyaHqGmO1I), we proved that <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^TX)\\)</span>.

Here, we'll ask you to prove something similar involving <span class="math-inline">\\(XX^T\\)</span>. Note that <span class="math-inline">\\(X^TX\\)</span> is a matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s **columns**, while <span class="math-inline">\\(XX^T\\)</span> is a matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s **rows**. (This has fact had something to do with Homework 6, Problem 4!)

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix, and <span class="math-inline">\\(XX^T\\)</span> is invertible. Find and explain **all** inequalities that **must** be true between <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(d\\)</span>, and <span class="math-inline">\\(r = \text{rank}(X)\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(XX^T\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix. For it to be invertible, it must have a rank of <span class="math-inline">\\(n\\)</span>. But, since <span class="math-inline">\\(\text{rank}(X) = \text{rank}(XX^T)\\)</span>, <span class="math-inline">\\(X\\)</span> must also have a rank of <span class="math-inline">\\(n\\)</span>. So, one equality is <span class="math-inline">\\(\boxed{r = n}\\)</span>.

**Why is <span class="math-inline">\\(\text{rank}(X) = \text{rank}(XX^T)\\)</span>? For full credit, this needed to be proved.** There's an easy way and a hard way; we'll start with the hard way. Similar to what we did in the homework, we'll prove that the ranks are equal by looking at null spaces and using the rank-nullity theorem. But, <span class="math-inline">\\(X\\)</span>'s null space is made up of vectors in <span class="math-inline">\\(\mathbb{R}^d\\)</span>, while <span class="math-inline">\\(XX^T\\)</span>'s null space is made up of vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. So, we need to find a way to compare the two, since they involve different types of vectors.

The linking fact is that <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^T)\\)</span>, so we can instead argue that <span class="math-inline">\\(\text{rank}(X^T) = \text{rank}(XX^T)\\)</span>. And, to do this, we'll show that the null spaces of <span class="math-inline">\\(X^T\\)</span> and <span class="math-inline">\\(XX^T\\)</span> are the same, which will tell us (again, through the rank-nullity theorem) that the ranks are equal.

Our goal is to show that <span class="math-inline">\\(\text{nullsp}(X^T) = \text{nullsp}(XX^T)\\)</span>. Both sides of this equation are sets, so to show they're equal, we need to show that any element in one set is also in the other, and vice versa.

**(i)** **Prove <span class="math-inline">\\(\vec v \in \text{nullsp}(X^T) \implies \vec v \in \text{nullsp}(XX^T)\\)</span>**:

Let <span class="math-inline">\\(\vec v \in \text{nullsp}(X^T)\\)</span>. This means <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(X^T \vec v = \vec 0\\)</span>. Multiplying both sides by <span class="math-inline">\\(X\\)</span> on the left gives us <span class="math-inline">\\(XX^T \vec v = X \vec 0 = \vec 0\\)</span>. So, <span class="math-inline">\\(\vec v \in \text{nullsp}(XX^T)\\)</span>.

**(ii)** **Prove <span class="math-inline">\\(\vec v \in \text{nullsp}(XX^T) \implies \vec v \in \text{nullsp}(X^T)\\)</span>**:

Let <span class="math-inline">\\(\vec v \in \text{nullsp}(XX^T)\\)</span>. Again, this means that <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(XX^T \vec v = \vec 0\\)</span>. Let's multiply both sides by <span class="math-inline">\\(\vec v^T\\)</span> on the left:

<div class="math-display">
$$
\begin{align*}
XX^T \vec v &= \vec 0 \\\\
\vec v^T XX^T \vec v &= \vec v^T \vec 0 \\\\
(X^T \vec v)^T (X^T \vec v) &= 0 \\\\
(X^T \vec v) \cdot (X^T \vec v) &= 0 \\\\
\| X^T \vec v \|^2 &= 0 \\\\
X^T \vec v &= \vec 0
\end{align*}
$$
</div>

Since we've shown that any element in <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span> is also in <span class="math-inline">\\(\text{nullsp}(XX^T)\\)</span>, and vice versa, we have <span class="math-inline">\\(\text{nullsp}(X^T) = \text{nullsp}(XX^T)\\)</span>.

The easier way to prove this would be to start with the fact that

<div class="math-display">
$$
\text{rank}(X) = \text{rank}(X^TX)
$$
</div>

and replace every <span class="math-inline">\\(X\\)</span> with <span class="math-inline">\\(X^T\\)</span>:

<div class="math-display">
$$
\text{rank}(X^T) = \text{rank}((X^T)^T X^T) = \text{rank}(XX^T)
$$
</div>

But since <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^T)\\)</span>, we have <span class="math-inline">\\(\text{rank}(X) = \text{rank}(XX^T)\\)</span>.

Back to the main plot. Remember that <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix, and we now know that <span class="math-inline">\\(\text{rank}(X) = r = n\\)</span>. But, in general, <span class="math-inline">\\(\text{rank}(X) \leq n\\)</span> and <span class="math-inline">\\(\text{rank}(X) \leq d\\)</span>. So, <span class="math-inline">\\(\boxed{n \leq d}\\)</span>, meaning that <span class="math-inline">\\(X\\)</span> must have at least as many columns as rows (meaning it must be wide or square, not tall).

Just to make sense of this, imagine <span class="math-inline">\\(X\\)</span> had more rows than columns. Then, it might look something like

<div class="math-display">
$$
X = \begin{bmatrix} \cdot & \cdot & \cdot & \cdot \\\\ \cdot & \cdot & \cdot & \cdot \\\\ \cdot & \cdot & \cdot & \cdot \\\\ \cdot & \cdot & \cdot & \cdot \\\\ \cdot & \cdot & \cdot & \cdot \\\\ \cdot & \cdot & \cdot & \cdot \end{bmatrix}
$$
</div>

This matrix has up to 4 linearly independent columns, and so it has up to 4 linearly independent rows, meaning not all of its rows can be linearly independent. But, since <span class="math-inline">\\(\text{rank}(X) = n\\)</span>, we need all of its rows to be linearly independent. So, <span class="math-inline">\\(X\\)</span> can't be tall, and its number of columns must be greater than or equal to its number of rows.

So, to summarize:

-   <span class="math-inline">\\(r = n\\)</span>

-   <span class="math-inline">\\(n \leq d\\)</span>

-   (implied by the above two) <span class="math-inline">\\(r \leq d\\)</span>
</details>

---

## Problem 7: Trickster (5 pts)

Find a matrix <span class="math-inline">\\(A\\)</span> that is **not equal to the identity matrix**, but where <span class="math-inline">\\(A^6 = I\\)</span>.

Once you think of your answer, you should explain how you found it, and should use Python to verify that <span class="math-inline">\\(A^6 = I\\)</span> holds. Include a screenshot of your Python code.

<em>Hint: This problem has a trick to it, and to think of it, I'd suggest reading the <a href="https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#rotations-and-orthogonal-matrices">Rotations and Orthogonal Matrices section of Chapter 6.2</a>.</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(A\\)</span> could be the rotation matrix that corresponds to rotating by <span class="math-inline">\\(60^\circ\\)</span>, or <span class="math-inline">\\(\frac{\pi}{3}\\)</span> radians, since applying this transformation 6 times will bring us back to the vectors we started with.

As we saw in [Chapter 6.2](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#rotations-and-orthogonal-matrices),

<div class="math-display">
$$
R(\theta) = \begin{bmatrix} \cos \theta & -\sin \theta \\\\ \sin \theta & \cos \theta \end{bmatrix}
$$
</div>

so

<div class="math-display">
$$
\boxed{A = \begin{bmatrix} \cos \frac{\pi}{3} & -\sin \frac{\pi}{3} \\\\ \sin \frac{\pi}{3} & \cos \frac{\pi}{3} \end{bmatrix} = \begin{bmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\\\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{bmatrix}}
$$
</div>

A simpler answer might be <span class="math-inline">\\(\boxed{A = \begin{bmatrix} 0 &amp; 1 \\\\ 1 &amp; 0 \end{bmatrix}}\\)</span>, since <span class="math-inline">\\(A^2 = I\\)</span> and so <span class="math-inline">\\(A^6 = (A^2)^3 = I^3 = I\\)</span>.
</details>

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

<details markdown="1"><summary>Solution</summary>

As the hint suggests, let's multiply out <span class="math-inline">\\(B \vec u\\)</span> in the case where <span class="math-inline">\\(A = I\\)</span>.

<div class="math-display">
$$
\begin{align*}
B\vec u &= (I+\vec u\vec v^T)\vec u
\\\\&= I\vec u+\vec u\vec v^T\vec u
\\\\&= 1\vec u+(\vec v^T\vec u) \vec u
\\\\&= \vec u(1+\vec v^T\vec u) \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: (\vec v ^T \vec u \text{ is a scalar!)}
\end{align*}
$$
</div>

When <span class="math-inline">\\(1+\vec v^T\vec u=0\\)</span>, then <span class="math-inline">\\(B\vec u=\vec 0\\)</span>. This means that <span class="math-inline">\\(\vec u \in \text{nullsp}(B)\\)</span>. But, this means that <span class="math-inline">\\(B\\)</span>'s null space contains more than just the zero vector, so <span class="math-inline">\\(\text{dim}(\text{nullsp}(B)) &gt; 0\\)</span>, so <span class="math-inline">\\(\text{rank}(B) &lt; n\\)</span>, meaning <span class="math-inline">\\(B\\)</span> is not invertible.
</details>

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

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
(I + {\vec u \vec v^T}) \left( I - \frac{{\vec u \vec v^T}}{1 + {\vec v^T \vec u}} \right) &= I - \frac{{\vec u \vec v^T}}{1 + {\vec v^T \vec u}} + {\vec u \vec v^T} - \frac{{\vec u \vec v^T} {\vec u \vec v^T}}{1 + {\vec v^T \vec u}} \\\\
&= I - \frac{{\vec u \vec v^T}}{1 + {\vec v^T \vec u}} + {\vec u \vec v^T} - \frac{({\vec v^T \vec u}){\vec u \vec v^T}}{1 + {\vec v^T \vec u}} \hspace{3em} \text{(remember, } {\vec v^T \vec u} \text{ is a scalar)} \\\\
&= I + {\vec u \vec v^T}\left(-\frac{1}{1 + {\vec v^T \vec u}} + 1 - \frac{({\vec v^T \vec u})}{1 + {\vec v^T \vec u}}\right) \\\\
&= I + {\vec u \vec v^T}\left(-\frac{1}{1 + {\vec v^T \vec u}} + \frac{1 + {\vec v^T \vec u}}{1 + {\vec v^T \vec u}} - \frac{\vec v^T\vec u}{1 + {\vec v^T \vec u}}\right) \\\\
&= I + {\vec u \vec v^T}\left(\frac{1 + {\vec v^T \vec u}}{1 + {\vec v^T \vec u}} - \frac{1 + \vec v^T \vec u}{1 + {\vec v^T \vec u}}\right) \\\\
&= I + {\vec u \vec v^T}(0) \\\\
&= I
\end{align*}
$$
</div>

</details>

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

Open the **supplemental Jupyter Notebook** we've created for Homework 6, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw06%2Fhw06.ipynb&branch=main) on DataHub, or [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw06/hw06.ipynb) in the course GitHub repository; also watch [this video](https://youtu.be/HZtoekU9NcE) first with tips on using `numpy` for linear algebra.

There, you're asked to implement the Sherman-Morrison formula, and run some experiments to quantify how much quicker using the formula is than computing the inverse of <span class="math-inline">\\(B\\)</span> from scratch.

This problem is **not autograded**. Rather, in your submission to this part, include screenshots of your implementations of functions `generate_random_data`, `invert_B_directly`,

`invert_B_with_sherman_morrison`, `run_one_experiment`, and `many_experiments_mean_sd`, along with their outputs on the provided examples.

<details markdown="1"><summary>Solution</summary>

<img src="imgs/7c_generate.png" alt="image" style="width: 100%; max-width: 100%;"> <img src="imgs/7c_invert_direct.png" alt="image" style="width: 100%; max-width: 100%;"> <img src="imgs/7c_invert_sherman.png" alt="image" style="width: 100%; max-width: 100%;"> <img src="imgs/7c_run_one.png" alt="image" style="width: 100%; max-width: 100%;"> <img src="imgs/7c_run_many.png" alt="image" style="width: 100%; max-width: 100%;">
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Include screenshots of the code you used to call `many_experiments_mean_sd` for the values provided in the question, the outputs of the print statements you were asked to add, and the `plotly` line chart you were asked to create.

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="imgs/7d.png" alt="image" style="width: 100%; max-width: 100%;">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Answer the question posed at the end of the supplemental Jupyter Notebook. (This shouldn't be a screenshot; just write your answer in this PDF the same way you answered Problems 1-7.)

<details markdown="1"><summary>Solution</summary>

Once <span class="math-inline">\\(n\\)</span> increases past a point, the pre-computed inverse <span class="math-inline">\\(A^{-1}\\)</span> no longer fits in the computer's cache, and has to be stored in memory (RAM), which is slower to access than the cache. At that point, the cost of retrieving <span class="math-inline">\\(A^{-1}\\)</span> from memory to apply the Sherman-Morrison formula becomes larger than just computing the inverse directly.

This may seem unintuitive, but note that `numpy` has highly optimized linear algebra routines, written in C which solve systems and invert matrices very quickly. So, even though the Sherman-Morrison formula is more efficient than inverting <span class="math-inline">\\(B\\)</span> directly, the difference in execution time becomes negligible as <span class="math-inline">\\(n\\)</span> increases.
</details>

If you're curious, look into [Low-Rank Adaptions (LoRA)](https://www.ibm.com/think/topics/lora), a relatively recent development in large language model research! The general idea is the same as we've worked with here.
</div>
</div>

</div>

{% endraw %}
