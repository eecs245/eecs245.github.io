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

**Note**: In some of the problems in this homework, we'll explicitly mention that you can use Python and `numpy` to perform some of the relevant calculations. For a reference on how to do so, consult [Chapter 5.1](https://notes.eecs245.org/matrices/matrix-operations/#computation). In other problems, we'll explicitly state that you must execute all calculations by hand.

---

## Problem 1: Midterm 1 Solutions Review (10 pts)

Review the solutions to Midterm 1. Pick **two problem parts** (for example, Problem 3b and Problem 7a) from Midterm 1 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Midterm 1, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Evaluate <span class="math-inline">\\(A\begin{bmatrix} 3 \\\\ 0 \\\\ -2 \end{bmatrix}\\)</span>.

There are two interpretations of the resulting vector, based on what we've seen in [Chapter 5.1](https://notes.eecs245.org/matrices/matrix-operations/) --- what are they?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) In both subparts, try and find a vector <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span> such that <span class="math-inline">\\(A \vec x = \vec b\\)</span>. If it's not possible to do so, explain why.

1.  <span class="math-inline">\\(\vec b = \begin{bmatrix} 0 \\\\ 5 \\\\ 3 \\\\ -1 \\\\ 4 \end{bmatrix}\\)</span>

2.  <span class="math-inline">\\(\vec b = \begin{bmatrix} 10 \\\\ 1 \\\\ -17 \\\\ -14 \\\\ -4 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Explain why it's the case that --- for this particular matrix <span class="math-inline">\\(A\\)</span> --- if <span class="math-inline">\\(A \vec x&#95;1 = \vec b\\)</span> and <span class="math-inline">\\(A \vec x&#95;2 = \vec b\\)</span>, then <span class="math-inline">\\(\vec x&#95;1 = \vec x&#95;2\\)</span>.

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In English, what do the two elements on the diagonal (top-left and bottom-right) of <span class="math-inline">\\(\Sigma\\)</span> represent?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) You should notice that <span class="math-inline">\\(\Sigma\\)</span> is a *symmetric* matrix, meaning <span class="math-inline">\\(\Sigma^T = \Sigma\\)</span>. (See [Chapter 5.2](https://notes.eecs245.org/matrices/special-matrices/#symmetric-matrices) for more on symmetric matrices.) The elements off the diagonal (top-right and bottom-left) are both equal, and are called the **covariance** of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>. For that reason, <span class="math-inline">\\(\Sigma\\)</span> is often called the **covariance matrix**.

Find an expression for the off-diagonal elements of <span class="math-inline">\\(\Sigma\\)</span> in terms of the correlation coefficient, <span class="math-inline">\\(r\\)</span>, <span class="math-inline">\\(\sigma&#95;x\\)</span>, and <span class="math-inline">\\(\sigma&#95;y\\)</span>, but with no summation notation or other variables.

<em>Hint: This only requires 1-2 lines of work. Remember the definition of <span class="math-inline">\\(r\\)</span> from <a href="https://notes.eecs245.org/simple-linear-regression/correlation/">Chapter 2.4</a>.</em>

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the projection of <span class="math-inline">\\(\vec u = \begin{bmatrix} 9 \\\\ -3 \end{bmatrix}\\)</span> onto the unit vector <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 / 5 \\\\ 4 / 5 \end{bmatrix}\\)</span> using:

1.  The formula for the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>

2.  The projection matrix <span class="math-inline">\\(P\\)</span> you found in part **a)**

<em>Feel free to use Python and `numpy` to compute the relevant products as we do in <a href="https://notes.eecs245.org/matrices/special-matrices/#symmetric-matrices">Chapter 5.2</a>, but if you do so, include screenshots of your code and results, and also write out the final result by hand. If you just write the final result with no work shown, you will not receive any credit.</em>

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

<em>Note: Feel free to use Python and `numpy` to compute the relevant products as we do in <a href="https://notes.eecs245.org/matrices/special-matrices/#symmetric-matrices">Chapter 5.2</a>, but if you do so, include screenshots of your code and results, and also write out the final result by hand. If you just write the final result with no work shown, you will not receive any credit.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Explain why the following statement is true: If <span class="math-inline">\\(Q\\)</span> is an orthogonal matrix, then the **rows** of <span class="math-inline">\\(Q\\)</span> form an orthonormal set, in addition to the columns.

<em>Hint: Think about what <span class="math-inline">\\(Q^TQ\\)</span> and <span class="math-inline">\\(QQ^T\\)</span> each are.</em>

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

{% endraw %}
