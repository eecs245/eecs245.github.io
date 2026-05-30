---
layout: page
title: "Homework 5: Matrices"
description: "Homework 5: Matrices problems."
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

# Homework 5: Matrices

**due** Thursday, May 28th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw05/hw05.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw05/hw05-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Midterm 1 Solutions Review](#problem-1-midterm-1-solutions-review-10-pts)
- [Problem 2: Getting Started](#problem-2-getting-started-15-pts)
- [Problem 3: Correlation, Revisited](#problem-3-correlation-revisited-11-pts)
- [Problem 4: Projections, Revisited](#problem-4-projections-revisited-14-pts)
- [Problem 5: Orthogonal Matrices](#problem-5-orthogonal-matrices-15-pts)
- [Problem 6: CR Decomposition](#problem-6-cr-decomposition-9-pts)

---

Total Points: 10 + 15 + 11 + 14 + 15 + 9 = 74

---

**Note**: In some of the problems in this homework, we'll explicitly mention that you can use Python and `numpy` to perform some of the relevant calculations. For a reference on how to do so, consult [Chapter 5.1](https://notes.eecs245.org/matrices/matrix-operations/#computation) or [this video](https://youtu.be/HZtoekU9NcE). In other problems, we'll explicitly state that you must execute all calculations by hand.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/HZtoekU9NcE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

---

## Problem 1: Midterm 1 Solutions Review (10 pts)

Review the solutions to Midterm 1. Pick **two problem parts** (for example, Problem 3b and Problem 7a) from Midterm 1 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Midterm 1, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

<details markdown="1"><summary>Solution</summary>

</details>

---

## Problem 2: Getting Started (15 pts)

Let

<div class="math-display">
$$
A = \begin{bmatrix} 3 & 0 & 4 \\\\ 0 & 1 & 0 \\\\ 2 & -1 & -3 \\\\ 5 & 0 & -1 \\\\ 3 & 2 & 0 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) In each subpart, state whether the resulting object is a matrix, vector, or scalar. If the result is a matrix or vector, state its dimensions. If the result is not defined, state why. **You don't need to actually compute the resulting objects.**

1.  <span class="math-inline">\\(A^T\\)</span>

2.  <span class="math-inline">\\(A^TA\\)</span>

3.  <span class="math-inline">\\(AA^T\\)</span>

4.  <span class="math-inline">\\(A^TA + AA^T\\)</span>

5.  <span class="math-inline">\\(A^T \vec x\\)</span>, where <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span>

6.  <span class="math-inline">\\(A^T \vec x\\)</span>, where <span class="math-inline">\\(\vec x \in \mathbb{R}^5\\)</span>

7.  <span class="math-inline">\\(\vec x^T A^T A \vec x\\)</span>, where <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span>

<details markdown="1"><summary>Solution</summary>

1.  <span class="math-inline">\\(A^T\\)</span> is a matrix in <span class="math-inline">\\(\mathbb{R}^{3 \times 5}\\)</span>, since we replace the rows with the columns, and <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(\mathbb{R}^{5 \times 3}\\)</span> matrix.

2.  <span class="math-inline">\\(A^TA\\)</span> is a matrix in <span class="math-inline">\\(\mathbb{R}^{3 \times 3}\\)</span>. We can multiply <span class="math-inline">\\(A^T\\)</span> with <span class="math-inline">\\(A\\)</span> because their inner dimensions match (<span class="math-inline">\\(\mathbb{R}^{(3 \times 5)} \times \mathbb{R}^{(5 \times 3)}\\)</span>).

3.  <span class="math-inline">\\(AA^T\\)</span> is a matrix in <span class="math-inline">\\(\mathbb{R}^{5 \times 5}\\)</span> because the inner dimensions match (<span class="math-inline">\\(\mathbb{R}^{(5 \times 3)} \times \mathbb{R}^{(3 \times 5)}\\)</span>).

4.  Undefined. <span class="math-inline">\\(A^TA\\)</span> and <span class="math-inline">\\(AA^T\\)</span> have different shapes, so we can't add them together.

5.  Undefined, because the inner dimensions of the product don't match (<span class="math-inline">\\(\mathbb{R}^{(3 \times 5)} \times \mathbb{R}^{(3 \times 1)}\\)</span>).

6.  <span class="math-inline">\\(A^T \vec x\\)</span> is a vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

7.  <span class="math-inline">\\(\vec x^T A^T A \vec x\\)</span> is a scalar. The steps for this are below:

<div class="math-display">
$$
\begin{align*}
\vec x^T A^T A \vec x &= \vec x^T (A^T A) \vec x \:\:\:\: \text{using associative property} \\\\
&=\vec x^T (\mathbb{R}^{3 \times 3}) \vec x \:\:\:\: \text{substituting from part (ii)} \\\\
&=\mathbb{R}^{1 \times 3} (\mathbb{R}^{3 \times 3}) \vec x \:\:\:\: \text{transpose } \vec x \\\\
&=\mathbb{R}^{1 \times 3} \vec x \:\:\:\: \text{resolve the left product} \\\\
&=\mathbb{R}^{1 \times 1} \\\\
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Evaluate <span class="math-inline">\\(A\begin{bmatrix} 3 \\\\ 0 \\\\ -2 \end{bmatrix}\\)</span>.

There are two interpretations of the resulting vector, based on what we've seen in [Chapter 5.1](https://notes.eecs245.org/matrices/matrix-operations/) --- what are they?

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\begin{bmatrix} 3 & 0 & 4 \\\\ 0 & 1 & 0 \\\\ 2 & -1 & -3 \\\\ 5 & 0 & -1 \\\\ 3 & 2 & 0 \end{bmatrix} \begin{bmatrix} {3} \\\\ {0} \\\\ {-2} \end{bmatrix} &= \begin{bmatrix} 3 \cdot {3} & + & 0 \cdot {0} & + & 4 \cdot {(-2)} \\\\ 0 \cdot {3} & + & 1 \cdot {0} & + & 0 \cdot {(-2)} \\\\ 2 \cdot {3} & + & (-1) \cdot {0} & + & (-3) \cdot {(-2)}  \\\\ 5 \cdot {3} & + & 0 \cdot {0} & + & (-1) \cdot {(-2)} \\\\ 3 \cdot {3} & + & 2 \cdot {0} & + & 0 \cdot {(-2)}\end{bmatrix} \\\\
&= \begin{bmatrix} 9 & + & 0 & + & (-8) \\\\ 0 & + & 0 & + & 0 \\\\ 6 & + & 0 & + & 6  \\\\ 15 & + & 0 & + & 2 \\\\ 9 & + & 0 & + & 0\end{bmatrix} \\\\
&=\begin{bmatrix} 1 \\\\ 0 \\\\ 12  \\\\ 17 \\\\ 9\end{bmatrix}
\end{align*}
$$
</div>

The two key interpretations of matrix-vector multiplication from [Chapter 5.1](https://notes.eecs245.org/matrices/matrix-operations/) are:

1.  **Dot product with the rows of <span class="math-inline">\\(A\\)</span>**: <span class="math-inline">\\(A \vec x\\)</span> represents the dot product of the rows of <span class="math-inline">\\(A\\)</span> with the vector <span class="math-inline">\\(\vec x\\)</span>.

2.  **Linear combination of the columns of <span class="math-inline">\\(A\\)</span>**: <span class="math-inline">\\(A \vec x\\)</span> represents the linear combination of the columns of <span class="math-inline">\\(A\\)</span> with coefficients given by the components of <span class="math-inline">\\(\vec x\\)</span>. This is equivalent to thinking of <span class="math-inline">\\(A \vec x\\)</span> as a transformation of <span class="math-inline">\\(\vec x\\)</span> by the matrix <span class="math-inline">\\(A\\)</span>, sending it from <span class="math-inline">\\(\mathbb{R}^3\\)</span> to <span class="math-inline">\\(\mathbb{R}^5\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) In both subparts, try and find a vector <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span> such that <span class="math-inline">\\(A \vec x = \vec b\\)</span>. If it's not possible to do so, explain why.

1.  <span class="math-inline">\\(\vec b = \begin{bmatrix} 0 \\\\ 5 \\\\ 3 \\\\ -1 \\\\ 4 \end{bmatrix}\\)</span>

2.  <span class="math-inline">\\(\vec b = \begin{bmatrix} 10 \\\\ 1 \\\\ -17 \\\\ -14 \\\\ -4 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

1.  $$
\begin{align*}
    A \vec x &= \vec b \\\\
    \begin{bmatrix} 3 & 0 & 4 \\\\ 0 & 1 & 0 \\\\ 2 & -1 & -3 \\\\ 5 & 0 & -1 \\\\ 3 & 2 & 0 \end{bmatrix} \begin{bmatrix}x_1 \\\\ x_2 \\\\ x_3 \end{bmatrix} &= \begin{bmatrix} 0 \\\\ 5 \\\\ 3 \\\\ -1 \\\\ 4 \end{bmatrix} \\\\
    x_1\begin{bmatrix}3 \\\\ 0 \\\\ 2 \\\\ 5 \\\\ 3\end{bmatrix} + x_2\begin{bmatrix}0 \\\\ 1 \\\\ -1 \\\\ 0 \\\\ 2\end{bmatrix} + x_3\begin{bmatrix}4 \\\\ 0 \\\\ -3 \\\\ -1 \\\\ 0\end{bmatrix} &=\begin{bmatrix} 0 \\\\ 5 \\\\ 3 \\\\ -1 \\\\ 4 \end{bmatrix}
    \end{align*}
$$

   Now, we try to see if we can make <span class="math-inline">\\(\vec b\\)</span> as a linear combination of the columns of <span class="math-inline">\\(A\\)</span>:



<div class="math-display">
$$
\begin{align*}
    3x_1 + 4x_3 &= 0 \\\\
    x_2 &= 5 \\\\
    2x_1 -x_2 -3x_3 &= 3 \\\\
    5x_1 - x_3 &= -1 \\\\
    3x_1 + 2x_2 &= 4 \\\\
    \end{align*}
$$
</div>

   The second equation tells us that <span class="math-inline">\\(x&#95;2=5\\)</span>, so we can plug that into the last one to solve for <span class="math-inline">\\(x&#95;1\\)</span>:



<div class="math-display">
$$
\begin{align*}
    3x_1 + 2(5) &=4 \\\\
    3x_1 &=-6 \\\\
    x_1 &=-2
    \end{align*}
$$
</div>

   Using <span class="math-inline">\\(x&#95;1\\)</span>, we can see if there's a contradiction in the first and fourth equations:



<div class="math-display">
$$
\begin{align*}
    3(-2)+4x_3 &=0 \\\\
    5(-2)-x_3&=-1
    \end{align*}
$$
</div>

   In order for the equations to be true, <span class="math-inline">\\(x&#95;3\\)</span> must both be negative and positive, so we don't have to continue. So, there is no possible <span class="math-inline">\\(\vec x\\)</span>, since <span class="math-inline">\\(\vec b\\)</span> is not in the the column space of <span class="math-inline">\\(A\\)</span>.

2.  We can do a similar process for this part, even down to the steps of solving the system of linear equations (since we'll always know <span class="math-inline">\\(x&#95;2\\)</span>, plug into the last equation to solve for <span class="math-inline">\\(x&#95;1\\)</span>, and so on):



<div class="math-display">
$$
\begin{align*}
    \begin{bmatrix} 3 & 0 & 4 \\\\ 0 & 1 & 0 \\\\ 2 & -1 & -3 \\\\ 5 & 0 & -1 \\\\ 3 & 2 & 0 \end{bmatrix} \begin{bmatrix}x_1 \\\\ x_2 \\\\ x_3 \end{bmatrix} &= \begin{bmatrix} 10 \\\\ 1 \\\\ -17 \\\\ -14 \\\\ -4 \end{bmatrix} \\\\
    x_1\begin{bmatrix}3 \\\\ 0 \\\\ 2 \\\\ 5 \\\\ 3\end{bmatrix} + x_2\begin{bmatrix}0 \\\\ 1 \\\\ -1 \\\\ 0 \\\\ 2\end{bmatrix} + x_3\begin{bmatrix}4 \\\\ 0 \\\\ -3 \\\\ -1 \\\\ 0\end{bmatrix} &= \begin{bmatrix} 10 \\\\ 1 \\\\ -17 \\\\ -14 \\\\ -4 \end{bmatrix} \\\\
    \\\\
    3x_1 + 4x_3 &= 10 \\\\
    x_2 &= 1 \\\\
    2x_1 -x_2 -3x_3 &= -17 \\\\
    5x_1 - x_3 &= -14 \\\\
    3x_1 + 2x_2 &= -4 \\\\
    \\\\
    3x_1+2(1) &= -4 \\\\
    3x_1 &= -6 \\\\
    x_1 &= -2 \\\\
    \end{align*}
$$
</div>

   Now we solve for <span class="math-inline">\\(x&#95;3\\)</span>, starting with the first equation:



<div class="math-display">
$$
\begin{align*}
    3(-2)+4x_3 &= 10 \\\\
    -6 + 4x_3 &= 10 \\\\
    4x_3 &= 16 \\\\
    x_3 &= 4 \\\\
    \end{align*}
$$
</div>

   Plugging that value of <span class="math-inline">\\(x&#95;3\\)</span> into the fourth equation results in a valid equation, so all that's left is to check the third equation:



<div class="math-display">
$$
\begin{align*}
    2(-2) - 1 - 3(4) &= -17 \\\\
    -4 -1 - 12 &= -17
    \end{align*}
$$
</div>

   All the equations hold, so the vector <span class="math-inline">\\(\vec x = \begin{bmatrix}-2 \\\\ 1 \\\\ 4\end{bmatrix}\\)</span> satisfies <span class="math-inline">\\(A \vec x = \vec b\\)</span>

   Since we were able to find an <span class="math-inline">\\(\vec x\\)</span> that satisfies <span class="math-inline">\\(A \vec x = \vec b\\)</span>, <span class="math-inline">\\(\vec b\\)</span> is in the column space of <span class="math-inline">\\(A\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Explain why it's the case that --- for this particular matrix <span class="math-inline">\\(A\\)</span> --- if <span class="math-inline">\\(A \vec x&#95;1 = \vec b\\)</span> and <span class="math-inline">\\(A \vec x&#95;2 = \vec b\\)</span>, then <span class="math-inline">\\(\vec x&#95;1 = \vec x&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

The reason has to do with the fact that the column vectors of <span class="math-inline">\\(A\\)</span> are linearly independent. Recall,

<div class="math-display">
$$
A = \begin{bmatrix}
3 & 0 & 4 \\\\
0 & 1 & 0 \\\\
2 & -1 & -3 \\\\
5 & 0 & -1 \\\\
3 & 2 & 0 \end{bmatrix}
$$
</div>

We won't show here that the columns are linearly independent; this is something you should verify on your own.

Let the columns of <span class="math-inline">\\(A\\)</span> be <span class="math-inline">\\(\vec v^{(1)}\\)</span>, <span class="math-inline">\\(\vec v^{(2)}\\)</span>, and <span class="math-inline">\\(\vec v^{(3)}\\)</span>. Since they are linearly independent, the only solution to

<div class="math-display">
$$
a_1\vec v^{(1)} + a_2\vec v^{(2)} + a_3\vec v^{(3)} = \vec 0
$$
</div>

 is <span class="math-inline">\\(a&#95;1 = a&#95;2 = a&#95;3 = 0\\)</span>.

We'll now show that if <span class="math-inline">\\(A \vec x&#95;1 = \vec b\\)</span> and <span class="math-inline">\\(A \vec x&#95;2 = \vec b\\)</span>, then <span class="math-inline">\\(\vec x&#95;1 = \vec x&#95;2\\)</span>. Let <span class="math-inline">\\(\vec x&#95;1 = \begin{bmatrix} x&#95;{11} \\\\ x&#95;{12} \\\\ x&#95;{13} \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec x&#95;2 = \begin{bmatrix} x&#95;{21} \\\\ x&#95;{22} \\\\ x&#95;{23} \end{bmatrix}\\)</span>.

Given that <span class="math-inline">\\(A \vec x&#95;1 = \vec b\\)</span>, we have

<div class="math-display">
$$
A \vec x_1 = \vec b \implies x_{11}\vec v^{(1)} + x_{12}\vec v^{(2)} + x_{13}\vec v^{(3)} = \vec b
$$
</div>

Similarly, given that <span class="math-inline">\\(A \vec x&#95;2 = \vec b\\)</span>, we have

<div class="math-display">
$$
A \vec x_2 = \vec b \implies x_{21}\vec v^{(1)} + x_{22}\vec v^{(2)} + x_{23}\vec v^{(3)} = \vec b
$$
</div>

Subtracting the two equations, we get

<div class="math-display">
$$
(x_{11} - x_{21})\vec v^{(1)} + (x_{12} - x_{22})\vec v^{(2)} + (x_{13} - x_{23})\vec v^{(3)} = \vec 0
$$
</div>

 Since the columns are linearly independent, we know the three coefficients must all be zero. Therefore,

<div class="math-display">
$$
x_{11} - x_{21} = 0, x_{12} - x_{22} = 0, x_{13} - x_{23} = 0
$$
</div>

Therefore, <span class="math-inline">\\(\vec x&#95;1 = \vec x&#95;2\\)</span>. The more intuitive phrasing of this result is that if a set of vectors are linearly independent, then any vector that can be written as a linear combination of them can only be written in one way, or "linear combinations of linearly independent vectors are unique."

</details>

</div>
</div>

</div>

---

## Problem 3: Correlation, Revisited (11 pts)

In this problem, we'll see how the correlation coefficient between two variables, <span class="math-inline">\\(r\\)</span>, can be expressed as a matrix multiplication.

Consider a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, and let

<div class="math-display">
$$
D = \begin{bmatrix}
x_1 - \bar{x} & y_1 - \bar{y} \\\\
x_2 - \bar{x} & y_2 - \bar{y} \\\\
\vdots & \vdots \\\\
x_n - \bar{x} & y_n - \bar{y}
\end{bmatrix}
$$
</div>

where <span class="math-inline">\\(\bar{x}\\)</span> and <span class="math-inline">\\(\bar{y}\\)</span> are the means of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>, respectively. Note that <span class="math-inline">\\(D\\)</span> is an <span class="math-inline">\\(n \times 2\\)</span> matrix, and it is mean-centered, meaning that the mean of each column is 0.

Define the matrix <span class="math-inline">\\(\Sigma\\)</span> as follows.

<div class="math-display">
$$
\Sigma = \frac{1}{n} D^TD
$$
</div>

<span class="math-inline">\\(\Sigma\\)</span> is a <span class="math-inline">\\(2 \times 2\\)</span> matrix. Its name is pronounced "sigma", just like in summation notation and standard deviation. Don't confuse it with summation notation; <span class="math-inline">\\(\Sigma\\)</span> is just a single matrix.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) For this particular matrix <span class="math-inline">\\(D\\)</span>, find <span class="math-inline">\\(\Sigma\\)</span>. All four components of <span class="math-inline">\\(\Sigma\\)</span> should be expressions involving the points <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span> and/or <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>. Feel free to use summation notation in your answers.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\Sigma &= \frac{1}{n} D^TD \\\\
&=\frac{1}{n} \underbrace{\begin{bmatrix} x_1 - \bar{x} & x_2 - \bar{x} & \cdots & x_n - \bar{x} \\\\ y_1 - \bar{y} & y_2 - \bar{y} & \cdots & y_n - \bar{y} \end{bmatrix}}_{D^T, \: \text{shape } 2 \times n} \underbrace{\begin{bmatrix} x_1 - \bar{x} & y_1 - \bar{y} \\\\ x_2 - \bar{x} & y_2 - \bar{y} \\\\ \cdots & \cdots \\\\ x_n - \bar{x} & y_n - \bar{y} \end{bmatrix}}_{D, \: \text{shape } n \times 2} \\\\
&= \frac{1}{n} \begin{bmatrix}
(x_1 - \bar{x})^2 + \cdots + (x_n - \bar{x})^2 & (x_1 - \bar{x})(y_1 - \bar{y}) + \cdots + (x_n - \bar{x})(y_n - \bar{y}) \\\\
(x_1 - \bar{x})(y_1 - \bar{y}) + \cdots + (x_n - \bar{x})(y_n - \bar{y}) & (y_1 - \bar{y})^2 + \cdots + (y_n - \bar{y})^2 \end{bmatrix} \\\\
&= \frac{1}{n} \begin{bmatrix}
\sum_{i=1}^n (x_i - \bar{x})^2 &  \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \\\\
\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) & \sum_{i=1}^n (y_i - \bar{y})^2
\end{bmatrix}
\end{align*}
$$
</div>

If we'd like, we can distribute the <span class="math-inline">\\(\frac{1}{n}\\)</span> to get

<div class="math-display">
$$
\Sigma = \begin{bmatrix}
\displaystyle\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 & \displaystyle\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \\\\
\displaystyle\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) & \displaystyle\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In English, what do the two elements on the diagonal (top-left and bottom-right) of <span class="math-inline">\\(\Sigma\\)</span> represent?

<details markdown="1"><summary>Solution</summary>

The top-left element represents the variance of <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(\sigma&#95;x^2\\)</span>, and the bottom-right element represents the variance of <span class="math-inline">\\(y\\)</span>, <span class="math-inline">\\(\sigma&#95;y^2\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) You should notice that <span class="math-inline">\\(\Sigma\\)</span> is a *symmetric* matrix, meaning <span class="math-inline">\\(\Sigma^T = \Sigma\\)</span>. (See [Chapter 5.2](https://notes.eecs245.org/matrices/special-matrices/#symmetric-matrices) for more on symmetric matrices.) The elements off the diagonal (top-right and bottom-left) are both equal, and are called the **covariance** of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>. For that reason, <span class="math-inline">\\(\Sigma\\)</span> is often called the **covariance matrix**.

Find an expression for the off-diagonal elements of <span class="math-inline">\\(\Sigma\\)</span> in terms of the correlation coefficient, <span class="math-inline">\\(r\\)</span>, <span class="math-inline">\\(\sigma&#95;x\\)</span>, and <span class="math-inline">\\(\sigma&#95;y\\)</span>, but with no summation notation or other variables.

<em>Hint: This only requires 1-2 lines of work. Remember the definition of <span class="math-inline">\\(r\\)</span> from <a href="https://notes.eecs245.org/simple-linear-regression/correlation/">Chapter 2.4</a>.</em>

<details markdown="1"><summary>Solution</summary>

The off-diagonal elements, both of which are equal to

<div class="math-display">
$$
\text{covariance} = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$
</div>

are equal to

<div class="math-display">
$$
\text{covariance} = r \sigma_x \sigma_y
$$
</div>

This comes from the definition of <span class="math-inline">\\(r\\)</span>.

<div class="math-display">
$$
r = \frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right)
$$
</div>

Multiplying both sides in the definition of <span class="math-inline">\\(r\\)</span> by <span class="math-inline">\\(\sigma&#95;x \sigma&#95;y\\)</span> gives us the desired result.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In general, suppose <span class="math-inline">\\(X \in \mathbb{R}^{n \times d}\\)</span> is a matrix containing <span class="math-inline">\\(n\\)</span> observations for each of <span class="math-inline">\\(d\\)</span> variables/features. The covariance matrix of <span class="math-inline">\\(X\\)</span> is defined similarly.

<div class="math-display">
$$
\Sigma = \frac{1}{n} X^TX
$$
</div>

In English, explain what the element in row 3 and column 5 of this <span class="math-inline">\\(\Sigma\\)</span> represents.

<details markdown="1"><summary>Solution</summary>

This is the covariance between feature 3 and feature 5, which is the same as their correlation, multiplied by the standard deviation of feature 3 and the standard deviation of feature 5.

</details>

</div>
</div>

</div>

---

## Problem 4: Projections, Revisited (14 pts)

As we first saw in [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/), the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> is the vector

<div class="math-display">
$$
\vec p = \left( \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \right) \vec v
$$
</div>

If we assume that <span class="math-inline">\\(\vec v\\)</span> is a unit vector, meaning <span class="math-inline">\\(\lVert \vec v \rVert = 1\\)</span>, then the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> has a simpler form,

<div class="math-display">
$$
\vec p = (\vec u \cdot \vec v) \vec v
$$
</div>

 For simplicity, assume that <span class="math-inline">\\(\vec u = \begin{bmatrix} u&#95;1 \\\\ u&#95;2 \end{bmatrix}\\)</span> is some arbitrary (not-necessarily unit) vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>, and <span class="math-inline">\\(\vec v = \begin{bmatrix} v&#95;1 \\\\ v&#95;2 \end{bmatrix}\\)</span> is **a unit vector** in <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Find a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(P\\)</span>, called a **projection matrix**, such that

<div class="math-display">
$$
P \vec u = \vec p = (\vec u \cdot \vec v) \vec v
$$
</div>

Think of <span class="math-inline">\\(P\\)</span> as a matrix that transforms <span class="math-inline">\\(\vec u\\)</span> into an approximation of it, in the direction of <span class="math-inline">\\(\vec v\\)</span> (or "projects" <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>).

<em>Hint: Start by writing <span class="math-inline">\\(P = \begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> and solve for <span class="math-inline">\\(a, b, c, d\\)</span> in terms of <span class="math-inline">\\(v&#95;1\\)</span> and <span class="math-inline">\\(v&#95;2\\)</span>; <span class="math-inline">\\(P\\)</span> should not involve <span class="math-inline">\\(u&#95;1\\)</span> or <span class="math-inline">\\(u&#95;2\\)</span>. Don't forget that <span class="math-inline">\\(\vec v\\)</span> is a unit vector, and both <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^2\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
P\vec u &= (\vec u \cdot \vec v)\vec v \\\\
\begin{bmatrix} a & b \\\\ c & d \end{bmatrix}\begin{bmatrix} u_1 \\\\ u_2 \end{bmatrix} &= \begin{bmatrix}(u_1v_1+u_2v_2)v_1 \\\\ (u_1v_1+u_2v_2)v_2\end{bmatrix} \\\\
&= \begin{bmatrix}u_1v_1^2+u_2v_1v_2 \\\\ u_1v_1v_2+u_2v_2^2\end{bmatrix} \\\\
\\\\
u_1a+u_2b &= u_1v_1^2+u_2v_1v_2 \\\\
u_1c+u_2d &= u_1v_1v_2+u_2v_2^2
\end{align*}
$$
</div>

<div class="math-display">
$$
a=v_1^2, \: b=v_1v_2 \: c=v_1v_2, \: d=v_2^2
$$
</div>



<div class="math-display">
$$
P = \begin{bmatrix} v_1^2 & v_1v_2 \\\\ v_1v_2 & v_2^2 \end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the projection of <span class="math-inline">\\(\vec u = \begin{bmatrix} 9 \\\\ -3 \end{bmatrix}\\)</span> onto the unit vector <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 / 5 \\\\ 4 / 5 \end{bmatrix}\\)</span> using:

1.  The formula for the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>

2.  The projection matrix <span class="math-inline">\\(P\\)</span> you found in part **a)**

<em>Feel free to use Python and `numpy` to compute the relevant products as we do in <a href="https://notes.eecs245.org/matrices/special-matrices/#symmetric-matrices">Chapter 5.2</a> and <a href="https://youtu.be/HZtoekU9NcE">this video</a>, but if you do so, include screenshots of your code and results, and also write out the final result by hand. If you just write the final result with no work shown, you will not receive any credit.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\vec p &= (\vec u \cdot \vec v)\vec v \\\\
&=(9 \cdot \frac{3}{5} + (-3) \cdot \frac{4}{5})\vec v \\\\
&=(\frac{27}{5}-\frac{12}{5})\vec v \\\\
&=3\vec v \\\\
&=\begin{bmatrix}
9/5 \\\\ 12/5
\end{bmatrix}
\end{align*}
$$
</div>

<div class="math-display">
$$
\begin{align*}
P &= \begin{bmatrix} v_1^2 & v_1v_2 \\\\ v_1v_2 & v_2^2 \end{bmatrix} \\\\
&= \begin{bmatrix}
(9/25) & (12/25) \\\\
(12/25) & (16/25)
\end{bmatrix} \\\\
\\\\
P\vec u &= \begin{bmatrix}
(9/25) & (12/25) \\\\
(12/25) & (16/25)
\end{bmatrix}
\begin{bmatrix}
9 \\\\ -3
\end{bmatrix} \\\\
&= \begin{bmatrix}
9(9/25) + (-3)(12/25) \\\\
9(12/25) + (-3)(16/25)
\end{bmatrix} \\\\
&= \begin{bmatrix}
81/25 -36/25 \\\\
108/25 -48/25
\end{bmatrix} \\\\
&= \begin{bmatrix}
45/25 \\\\
60/25
\end{bmatrix} \\\\
&= \begin{bmatrix}
9/5 \\\\
12/5
\end{bmatrix}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Show that <span class="math-inline">\\(P\\)</span> satisfies the following property:

<div class="math-display">
$$
P^2 = P
$$
</div>

This means that <span class="math-inline">\\(P\\)</span> is an **idempotent** matrix, meaning that applying <span class="math-inline">\\(P\\)</span> twice (or three times, or four times, etc.) to a vector is the same as applying it once.

<em>Hint: You'll likely end up with terms of the form <span class="math-inline">\\(v&#95;1^4\\)</span>. Remember that <span class="math-inline">\\(\vec v\\)</span> is a unit vector; use this to help you simplify.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
PP &= \begin{bmatrix} v_1^2 & v_1v_2 \\\\ v_1v_2 & v_2^2 \end{bmatrix}\begin{bmatrix} v_1^2 & v_1v_2 \\\\ v_1v_2 & v_2^2 \end{bmatrix} \\\\
&=\begin{bmatrix}
v_1^4+v_1^2v_2^2 & v_1^3v_2+v_1v_2^3 \\\\
v_1^3v_2+v_1v_2^3 & v_1^2v_2^2+v_2^4
\end{bmatrix} \\\\
&=\begin{bmatrix}
v_1^2(v_1^2+v_2^2) & v_1v_2(v_1^2+v_2^2) \\\\
v_1v_2(v_1^2+v_2^2) & v_2^2(v_1^2+v_2^2)
\end{bmatrix} \\\\
\\\\
v_1^2+v_2^2&=\vec v \cdot \vec v \\\\
&= ||\vec v||^2 = 1 \: \text{because } \vec v \text{ is a unit vector} \\\\
\\\\
PP&=\begin{bmatrix}
v_1^2 & v_1v_2 \\\\
v_1v_2 & v_2^2
\end{bmatrix} = P\\\\
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 5: Orthogonal Matrices (15 pts)

Read [Orthogonal Matrices section of Chapter 5.2](https://notes.eecs245.org/matrices/special-matrices/#orthogonal-matrices) before starting this problem.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) For each of the following matrices, compute <span class="math-inline">\\(A^TA\\)</span> and <span class="math-inline">\\(AA^T\\)</span>; <span class="math-inline">\\(B^TB\\)</span> and <span class="math-inline">\\(BB^T\\)</span>; \... and use that to determine whether it is orthogonal. If a matrix is not orthogonal, explain which of the conditions for being orthogonal it does and does not satisfy.

<div class="math-display">
$$
A = \begin{bmatrix} 3 & 0 \\\\ 0 & 2 \\\\ 4 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 3/5 & -4/5 \\\\ 4/5 & 3/5 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & 0 & 1 \\\\ 3/5 & 4/5 & 0 \\\\ 4/5 & -3/5 & 0 \end{bmatrix}, \quad D = \begin{bmatrix} 3/5 & 0 & 1/\sqrt{2} \\\\ 4/5 & 0 & 1/\sqrt{2} \\\\ 0 & 1 & 0 \end{bmatrix}
$$
</div>

<em>Note: Feel free to use Python and `numpy` to compute the relevant products as we do in <a href="https://notes.eecs245.org/matrices/special-matrices/#symmetric-matrices">Chapter 5.2</a> and <a href="https://youtu.be/HZtoekU9NcE">this video</a>, but if you do so, include screenshots of your code and results, and also write out the final result by hand. If you just write the final result with no work shown, you will not receive any credit.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
A^TA&=\begin{bmatrix} 3 & 0 & 4  \\\\ 0 & 2 & 0\end{bmatrix} \begin{bmatrix} 3 & 0 \\\\ 0 & 2 \\\\ 4 & 0 \end{bmatrix}
\\\\&=\begin{bmatrix}25 & 0 \\\\ 0 & 4 \end{bmatrix} \neq I
\\\\
\\\\AA^T&=\begin{bmatrix} 3 & 0 \\\\ 0 & 2 \\\\ 4 & 0 \end{bmatrix}\begin{bmatrix} 3 & 0 & 4  \\\\ 0 & 2 & 0\end{bmatrix}
\\\\&=\begin{bmatrix}9 & 0 & 12 \\\\ 0 & 4 & 0 \\\\ 12 & 0 & 16\end{bmatrix} \neq I
\end{align*}
$$
</div>

<span class="math-inline">\\(A\\)</span>'s columns are orthogonal to one another, but they're not unit vectors. Also, since <span class="math-inline">\\(A^TA\\)</span> and <span class="math-inline">\\(AA^T\\)</span> have different shapes, they can't possibly be equal, which gives us another implicit condition: only square matrices can be orthogonal.

<div class="math-display">
$$
\begin{align*}
B^TB&=\begin{bmatrix} 3/5 & 4/5 \\\\ -4/5 & 3/5 \end{bmatrix}\begin{bmatrix} 3/5 & -4/5 \\\\ 4/5 & 3/5 \end{bmatrix}
\\\\&=\begin{bmatrix}9/25+16/25 & -12/25+12/25 \\\\ -12/25+12/25 & 16/25+9/25\end{bmatrix}
\\\\&=\begin{bmatrix}1 & 0 \\\\ 0 & 1\end{bmatrix}=I
\\\\
\\\\BB^T&=\begin{bmatrix} 3/5 & -4/5 \\\\ 4/5 & 3/5 \end{bmatrix}\begin{bmatrix} 3/5 & 4/5 \\\\ -4/5 & 3/5 \end{bmatrix}
\\\\&=\begin{bmatrix}9/25 +16/25 & 12/25-12/25 \\\\ 12/25-12/25 & 16/25+9/25\end{bmatrix}
\\\\&=\begin{bmatrix}1 & 0 \\\\ 0 & 1\end{bmatrix}=I
\end{align*}
$$
</div>

<span class="math-inline">\\(B\\)</span> satisfies both conditions, so it is orthogonal!

<div class="math-display">
$$
\begin{align*}
C^TC&=\begin{bmatrix} 0 & 3/5 & 4/5 \\\\ 0 & 4/5 & -3/5 \\\\ 1 & 0 & 0 \end{bmatrix}\begin{bmatrix} 0 & 0 & 1 \\\\ 3/5 & 4/5 & 0 \\\\ 4/5 & -3/5 & 0 \end{bmatrix}
\\\\&=\begin{bmatrix}9/25+16/25 & 12/25-12/25 & 0 \\\\ 12/25-12/25 & 16/25+9/25&0 \\\\ 0 & 0 & 1\end{bmatrix}
\\\\&=\begin{bmatrix}1 & 0 & 0 \\\\ 0 & 1&0 \\\\ 0 & 0 & 1\end{bmatrix}=I
\\\\
\\\\CC^T&=\begin{bmatrix} 0 & 0 & 1 \\\\ 3/5 & 4/5 & 0 \\\\ 4/5 & -3/5 & 0 \end{bmatrix}\begin{bmatrix} 0 & 3/5 & 4/5 \\\\ 0 & 4/5 & -3/5 \\\\ 1 & 0 & 0 \end{bmatrix}
\\\\&=\begin{bmatrix}1 & 0 & 0 \\\\ 0 & 9/25+16/25 & 0 \\\\ 0 & 12/25-12/25 & 16/25+9/25\end{bmatrix}
\\\\&=\begin{bmatrix}1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1\end{bmatrix}=I
\end{align*}
$$
</div>

<span class="math-inline">\\(C\\)</span> satisfies both conditions, so it is orthogonal!

<div class="math-display">
$$
\begin{align*}
D^TD&=\begin{bmatrix} 3/5 & 4/5 & 0 \\\\ 0 & 0 & 1 \\\\ 1/\sqrt{2} & 1/\sqrt{2} & 0\end{bmatrix} \begin{bmatrix} 3/5 & 0 & 1/\sqrt{2} \\\\ 4/5 & 0 & 1/\sqrt{2} \\\\ 0 & 1 & 0 \end{bmatrix}
\\\\&=\begin{bmatrix}9/25 + 16/25 & 0 & 3/5\sqrt{2}+4/5\sqrt{2} \\\\ 0 & 1 & 0 \\\\ 3/5\sqrt{2}+4/5\sqrt{2} & 0 & 1/2+1/2 \end{bmatrix}
\\\\&=\begin{bmatrix}1 & 0 & 7/5\sqrt{2} \\\\ 0 & 1 & 0 \\\\ 7/5\sqrt{2} & 0 & 1 \end{bmatrix} \neq I
\\\\
\\\\DD^T&=\begin{bmatrix} 3/5 & 0 & 1/\sqrt{2} \\\\ 4/5 & 0 & 1/\sqrt{2} \\\\ 0 & 1 & 0 \end{bmatrix}\begin{bmatrix} 3/5 & 4/5 & 0 \\\\ 0 & 0 & 1 \\\\ 1/\sqrt{2} & 1/\sqrt{2} & 0\end{bmatrix}
\\\\&=\begin{bmatrix}9/25+1/2 & 12/25 + 1/2 & 0 \\\\ 12/25 + 1/2 & 16/25 + 1/2  & 0 \\\\ 0 & 0 & 1 \end{bmatrix}
\\\\&=\begin{bmatrix}43/50 & 49/50 & 0 \\\\ 49/50 & 57/50  & 0 \\\\ 0 & 0 & 1 \end{bmatrix} \neq I
\end{align*}
$$
</div>

<span class="math-inline">\\(D\\)</span>'s columns are unit vectors, but they aren't orthogonal to one another, as evidenced by the non-diagonal elements being non-zero in <span class="math-inline">\\(D^TD\\)</span>. So, <span class="math-inline">\\(D\\)</span> is not orthogonal.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Explain why the following statement is true: If <span class="math-inline">\\(Q\\)</span> is an orthogonal matrix, then the **rows** of <span class="math-inline">\\(Q\\)</span> form an orthonormal set, in addition to the columns.

<em>Hint: Think about what <span class="math-inline">\\(Q^TQ\\)</span> and <span class="math-inline">\\(QQ^T\\)</span> each are.</em>

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(Q\\)</span> to be an orthogonal matrix, <span class="math-inline">\\(Q^TQ=QQ^T=I\\)</span> must be true. <span class="math-inline">\\(Q^TQ\\)</span> is a matrix containing dot products of the columns, while <span class="math-inline">\\(QQ^T\\)</span> has dot products of the rows.

Recall that for any vector <span class="math-inline">\\(\vec v\\)</span>, <span class="math-inline">\\(\vec v \cdot \vec v = ||\vec v||^2\\)</span>. For a matrix <span class="math-inline">\\(Q^TQ\\)</span>, each diagonal value is the dot product of a column with itself, and for <span class="math-inline">\\(QQ^T\\)</span> the diagonal has the dot products of rows with themselves. If the diagonal values are 1, then the length of the rows and columns must be 1.

Using similar logic, the off diagonal values of <span class="math-inline">\\(Q^TQ\\)</span> and <span class="math-inline">\\(QQ^T\\)</span> are 0, meaning the rows and columns have to be orthogonal to each other.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Orthogonal matrices have many useful properties. One is that they **preserve the norm** of vectors. In other words, if <span class="math-inline">\\(Q \in \mathbb{R}^{n \times n}\\)</span> is orthogonal and <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span>, then:

<div class="math-display">
$$
\lVert Q \vec x \rVert = \lVert \vec x \rVert
$$
</div>

Prove the statement above.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\lVert Q\vec x \rVert^2 &= (Q\vec x)^T(Q\vec x)
\\\\&=\vec x ^TQ^TQ\vec x
\\\\&=\vec x^TI\vec x
\\\\&=\vec x^T\vec x
\\\\&=\lVert \vec x \rVert^2
\end{align*}
$$
</div>

Since <span class="math-inline">\\(\lVert Q\vec x \rVert^2 = \lVert \vec x \rVert^2\\)</span>, we can take the square root of both sides to get <span class="math-inline">\\(\lVert Q\vec x \rVert = \lVert \vec x \rVert\\)</span>. (This is legal since <span class="math-inline">\\(\lVert Q\vec x \rVert\\)</span> and <span class="math-inline">\\(\lVert \vec x \rVert\\)</span> are both non-negative.)

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) At the end of [Chapter 5.2](https://notes.eecs245.org/matrices/special-matrices/#symmetric-matrices), we presented the matrix

<div class="math-display">
$$
A = \begin{bmatrix} \frac{\sqrt{3}}{2} & -\frac{1}{2} \\\\ \frac{1}{2} & \frac{\sqrt{3}}{2} \end{bmatrix}
$$
</div>

and visualized three vectors, <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec w\\)</span>, and the result of multiplying each one by <span class="math-inline">\\(A\\)</span>. We defined <span class="math-inline">\\(A\\)</span> as a rotation matrix; specifically, one that rotates vectors by <span class="math-inline">\\(\theta = 30^\circ\\)</span> counterclockwise. (Go and look at the picture there for context; we're intentionally not providing it here so that you have to look at the notes!)

In general, the <span class="math-inline">\\(2 \times 2\\)</span> rotation matrix by an angle <span class="math-inline">\\(\theta\\)</span> is given by

<div class="math-display">
$$
R = \begin{bmatrix} \cos(\theta) & -\sin(\theta) \\\\ \sin(\theta) & \cos(\theta) \end{bmatrix}
$$
</div>

Prove that the matrix <span class="math-inline">\\(R\\)</span> is orthogonal.

<em>Hint: There's an identity on <a href="https://mathcs.clarku.edu/~djoyce/trig/identities.html">this page</a> that you'll need.</em>

<details markdown="1"><summary>Solution</summary>

The key identity that helps us unlock the proof is

<div class="math-display">
$$
\cos^2(\theta) + \sin^2(\theta) = 1
$$
</div>

So, given that, we have

<div class="math-display">
$$
\begin{align*}
R^TR&=\begin{bmatrix} \cos(\theta) & \sin(\theta) \\\\ -\sin(\theta) & \cos(\theta) \end{bmatrix}\begin{bmatrix} \cos(\theta) & -\sin(\theta) \\\\ \sin(\theta) & \cos(\theta) \end{bmatrix}
\\\\&= \begin{bmatrix}\cos^2(\theta)+ \sin^2(\theta) & -\cos(\theta)\sin(\theta) + \sin(\theta)\cos(\theta)\\\\ -\sin(\theta)\cos(\theta)+\cos(\theta)\sin(\theta)& \sin^2(\theta)+\cos^2(\theta)\end{bmatrix}\\\\
\\\\&=\begin{bmatrix}1 & 0 \\\\ 0 & 1\end{bmatrix}=I
\\\\
\\\\RR^T&=\begin{bmatrix} \cos(\theta) & -\sin(\theta) \\\\ \sin(\theta) & \cos(\theta) \end{bmatrix}\begin{bmatrix} \cos(\theta) & \sin(\theta) \\\\ -\sin(\theta) & \cos(\theta) \end{bmatrix}
\\\\&=\begin{bmatrix}\cos^2(\theta)+\sin^2(\theta) & \cos(\theta)\sin(\theta)-\sin(\theta)\cos(\theta) \\\\ \sin(\theta)\cos(\theta) - \cos(\theta)\sin(\theta) & \sin^2(\theta)+\cos^2(\theta) \end{bmatrix}
\\\\&=\begin{bmatrix}1 & 0 \\\\ 0 & 1 \end{bmatrix}=I
\end{align*}
$$
</div>

<span class="math-inline">\\(R\\)</span> satisfies both conditions, so it is an orthogonal matrix.

</details>

</div>
</div>

</div>

---

## Problem 6: CR Decomposition (9 pts)

Read the [CR Decomposition section of Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#cr-decomposition) before starting this problem. There, we introduce the concept of a CR decomposition. As another example, let <span class="math-inline">\\(A\\)</span> be the matrix from [Homework 4, Problem 5](https://eecs245.org/resources/homeworks/hw04/#problem-5-rows-and-columns-12-pts).

<div class="math-display">
$$
A = \begin{bmatrix}
5 & 3 & 5 & 2 \\\\
3 & 0 & -6 & 4 \\\\
-2 & 0 & 4 & 3 \\\\
8 & 2 & -6 & -8 \\\\
1 & 1 & 3 & 0
\end{bmatrix}
$$
</div>

Its CR decomposition is:

<div class="math-display">
$$
A = \underbrace{\begin{bmatrix}
5 & 3 & 2 \\\\ 3 & 0 & 4 \\\\ -2 & 0 & 3 \\\\ 8 & 2 & -8 \\\\ 1 & 1 & 0
\end{bmatrix}}_{C} \underbrace{\begin{bmatrix} 1 & 0 & -2 & 0 \\\\ 0 & 1 & 5 & 0 \\\\ 0 & 0 & 0 & 1 \end{bmatrix}}_{R}
$$
</div>

To understand where the numbers in <span class="math-inline">\\(R\\)</span> came from, read the solutions to Homework 4, linked above.

**By hand**, find a CR decomposition of the matrices below, by placing the linearly independent columns (reading from left to right) in <span class="math-inline">\\(C\\)</span> and the values needed to "mix" the linearly independent columns in <span class="math-inline">\\(C\\)</span> to get back the original matrix in <span class="math-inline">\\(R\\)</span>.

<em>Hint: Most of these can be done quickly by eyeballing the relationships between columns.</em>

1.  <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 2 &amp; 3 \\\\ 4 &amp; 5 &amp; 6 \\\\ 7 &amp; 8 &amp; 9 \end{bmatrix}\\)</span>

2.  <span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 5 \\\\ 1 &amp; 1 \\\\ 2 &amp; -4 \\\\ 30 &amp; 0 \end{bmatrix}\\)</span>

3.  <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; -2 &amp; 3 &amp; -1 \\\\ -2 &amp; 4 &amp; 1 &amp; -5 \\\\ 3 &amp; -6 &amp; 4 &amp; 2 \\\\ 0 &amp; 0 &amp; 5 &amp; -5 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

While we *could* use the full algorithm from Homework 4 or [Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/#algorithm-for-finding-linearly-independent-subsets-with-the-same-span), the three matrices provided are all small enough that we can eyeball their relationships.

1.  $$
A = \begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \end{bmatrix}
$$

 The first two columns of <span class="math-inline">\\(A\\)</span> are linearly independent. You might notice that the middle column is the average of the first and third columns, i.e.

<div class="math-display">
$$
\frac{\text{column 1} + \text{column 3}}{2} = \text{column 2}
$$
</div>

 meaning that

<div class="math-display">
$$
\text{column 3} = -\text{column 1} + 2 \cdot \text{column 2}
$$
</div>

 So, <span class="math-inline">\\(C\\)</span> only needs to contain the first two columns, and <span class="math-inline">\\(R\\)</span> should start with the <span class="math-inline">\\(2 \times 2\\)</span> identity matrix and have a third column of <span class="math-inline">\\(-1\\)</span> and <span class="math-inline">\\(2\\)</span>.

<div class="math-display">
$$
A = \begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \end{bmatrix} = \underbrace{\begin{bmatrix} 1 & 2 \\\\ 4 & 5 \\\\ 7 & 8 \end{bmatrix}}_{C} \underbrace{\begin{bmatrix} 1 & 0 & -1 \\\\ 0 & 1 & 2 \end{bmatrix}}_{R}
$$
</div>

2.  $$
A = \begin{bmatrix} 3 & 5 \\\\ 1 & 1 \\\\ 2 & -4 \\\\ 30 & 0 \end{bmatrix}
$$

 The two columns of <span class="math-inline">\\(A\\)</span> are linearly independent, so all we have to do is make <span class="math-inline">\\(R\\)</span> the <span class="math-inline">\\(2 \times 2\\)</span> identity matrix.

<div class="math-display">
$$
A = \begin{bmatrix} 3 & 5 \\\\ 1 & 1 \\\\ 2 & -4 \\\\ 30 & 0 \end{bmatrix} = \underbrace{\begin{bmatrix} 3 & 5 \\\\ 1 & 1 \\\\ 2 & -4 \\\\ 30 & 0 \end{bmatrix}}_{C} \underbrace{\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix}}_{R}
$$
</div>

3.  $$
A = \begin{bmatrix} 1 & -2 & 3 & -1 \\\\ -2 & 4 & 1 & -5 \\\\ 3 & -6 & 4 & 2 \\\\ 0 & 0 & 5 & -5 \end{bmatrix}
$$

 <span class="math-inline">\\(A\\)</span>'s second column is just <span class="math-inline">\\(-2\\)</span> times the first column, so we shouldn't include it in <span class="math-inline">\\(C\\)</span>. <span class="math-inline">\\(A\\)</span>'s third column is not a scalar multiple of <span class="math-inline">\\(A\\)</span>'s first column, so we should include it in <span class="math-inline">\\(C\\)</span>.

   The question, then, is what to do with the fourth column, since it's not immediately obvious whether it's a linear combination of columns 1 and 3. If you notice that the last component of column 4 is <span class="math-inline">\\(-5\\)</span> and the last component of column 3 is 5, it exposes the fact that if column 4 were a linear combination of columns 1 and 3, the coefficient on column 3 would have to be <span class="math-inline">\\(-1\\)</span>, since column 1's last component is 0. A quick guess and check confirms that



<div class="math-display">
$$
2 \cdot \text{column 1} - \text{column 3} = \text{column 4}
$$
</div>

   This gives us one CR decomposition:



<div class="math-display">
$$
A = \begin{bmatrix} 1 & -2 & 3 & -1 \\\\ -2 & 4 & 1 & -5 \\\\ 3 & -6 & 4 & 2 \\\\ 0 & 0 & 5 & -5 \end{bmatrix} = \underbrace{\begin{bmatrix} 1 & 3 \\\\ -2 & 1 \\\\ 3 & 4 \\\\ 0 & 5 \end{bmatrix}}_{C} \underbrace{\begin{bmatrix} 1 & -2 & 0 & 2 \\\\ 0 & 0 & 1 & -1 \end{bmatrix}}_{R}
$$
</div>

   Another possible CR decomposition is to use <span class="math-inline">\\(A\\)</span>'s 2nd and 3rd columns, rather than its 1st and 3rd columns. This gives us the following CR decomposition:



<div class="math-display">
$$
A = \begin{bmatrix} 1 & -2 & 3 & -1 \\\\ -2 & 4 & 1 & -5 \\\\ 3 & -6 & 4 & 2 \\\\ 0 & 0 & 5 & -5 \end{bmatrix} = \underbrace{\begin{bmatrix} -2 & 3 \\\\ 4 & 1 \\\\ -6 & 4 \\\\ 0 & 5 \end{bmatrix}}_{C} \underbrace{\begin{bmatrix} -\frac{1}{2} & 1 & 0 & -1 \\\\ 0 & 0 & 1 & -1 \end{bmatrix}}_{R}
$$
</div>

   These are not the only two possible CR decompositions of <span class="math-inline">\\(A\\)</span>! We could also, for instance, use <span class="math-inline">\\(A\\)</span>'s 1st and 4th columns, or 2nd and 4th.

</details>

{% endraw %}
