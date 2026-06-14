---
layout: page
title: "Lab 10: Eigenvalues and Eigenvectors, Convexity"
description: "Lab 10: Eigenvalues and Eigenvectors, Convexity activities."
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

# Lab 10: Eigenvalues and Eigenvectors, Convexity

**due** for completion at 11:59PM Ann Arbor Time on Monday, June 15th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab10/lab10.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Introduction](#activity-1-introduction)
- [Activity 2: Rapid Fire](#activity-2-rapid-fire)
- [Activity 3: Quadratic Forms Return](#activity-3-quadratic-forms-return)
- [Activity 4: Understanding Complex Proofs](#activity-4-understanding-complex-proofs)

---

## Recap: Eigenvalues and Eigenvectors

Let <span class="math-inline">\\(A = \begin{bmatrix} 6 &amp; 3 \\\\ 3 &amp; -2 \end{bmatrix}\\)</span>.

-   An **eigenvector** of <span class="math-inline">\\(A\\)</span> is a non-zero vector <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(A \vec v = \lambda \vec v\\)</span> for some scalar <span class="math-inline">\\(\lambda\\)</span>. The scalar <span class="math-inline">\\(\lambda\\)</span> is called the **eigenvalue** corresponding to <span class="math-inline">\\(\vec v\\)</span>. For <span class="math-inline">\\(A\\)</span>'s eigenvectors, multiplying by <span class="math-inline">\\(A\\)</span> is equivalent to multiplying by a scalar.

-   The **characteristic polynomial** of <span class="math-inline">\\(A\\)</span> is given by <span class="math-inline">\\(p(\lambda) = \det(A - \lambda I)\\)</span>.

<div class="math-display">
$$
p(\lambda) = \det(A - \lambda I) = \begin{vmatrix} 6 - \lambda & 3 \\\\ 3 & -2 - \lambda \end{vmatrix} = (6 - \lambda)(-2 - \lambda) - 3 \cdot 3 = \lambda^2 - 4\lambda - 21 = (\lambda + 3)(\lambda - 7)
$$
</div>

-   The eigenvalues of <span class="math-inline">\\(A\\)</span> are the roots of the characteristic polynomial, so <span class="math-inline">\\(\lambda&#95;1 = -3\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 7\\)</span>.

-   The eigenvector <span class="math-inline">\\(\vec v&#95;1\\)</span> satisfies <span class="math-inline">\\(A \vec v&#95;1 = -3 \vec v&#95;1\\)</span>.

<div class="math-display">
$$
\begin{bmatrix} 6 & 3 \\\\ 3 & -2 \end{bmatrix} \begin{bmatrix} a \\\\ b \end{bmatrix} = -3 \begin{bmatrix} a \\\\ b \end{bmatrix}\implies b = -3a
$$
</div>

 So any vector of the form <span class="math-inline">\\(\begin{bmatrix} a \\\\ -3a \end{bmatrix}\\)</span> (<span class="math-inline">\\(a \neq 0\\)</span>) is an eigenvector of <span class="math-inline">\\(A\\)</span> corresponding to the eigenvalue <span class="math-inline">\\(-3\\)</span>. We could pick <span class="math-inline">\\(\boxed{\vec v&#95;1 = \begin{bmatrix} 2 \\\\ -6 \end{bmatrix}}\\)</span>.

-   The eigenvector <span class="math-inline">\\(\vec v&#95;2\\)</span> satisfies <span class="math-inline">\\(A \vec v&#95;2 = 7 \vec v&#95;2\\)</span>. Another way to find it is to solve for the null space of <span class="math-inline">\\(A - 7I = \begin{bmatrix} -1 &amp; 3 \\\\ 3 &amp; -9 \end{bmatrix}\\)</span>. One vector in <span class="math-inline">\\(\text{nullsp}(A - 7I)\\)</span> is <span class="math-inline">\\(\boxed{\vec v&#95;2 = \begin{bmatrix} 3 \\\\ 1 \end{bmatrix}}\\)</span>.

---

## Activity 1: Introduction

For each <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(A\\)</span> below:

1.  Find the characteristic polynomial of <span class="math-inline">\\(A\\)</span>, and use it to find the eigenvalues of <span class="math-inline">\\(A\\)</span>.

2.  Find one eigenvector for each eigenvalue of <span class="math-inline">\\(A\\)</span>. Verify that each eigenvector is indeed an eigenvector of <span class="math-inline">\\(A\\)</span> by multiplying it by <span class="math-inline">\\(A\\)</span>.

3.  **By hand (not using Python or Desmos)**, draw a picture (like the one in Chapter 9.1 titled [Visualizing the eigenvectors of <span class="math-inline">\\(A\\)</span>](https://notes.eecs245.org/eigenvalues-and-eigenvectors/eigenvalues-eigenvectors/#a-first-example)) with vectors <span class="math-inline">\\(\vec v&#95;1, A \vec v&#95;1, \vec v&#95;2, A \vec v&#95;2\\)</span> as arrows (where <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> are the eigenvectors you found above).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 0 \\\\ 0 &amp; 4 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 4 \\\\ 4 &amp; 3 \end{bmatrix}\\)</span>

</div>
</div>

</div>

---

## Activity 2: Rapid Fire

The goal of this activity is to practice spotting eigenvalues and characteristic polynomials quickly. Two quick facts:

-   The **sum** of the eigenvalues of a matrix is equal to the **trace** of the matrix (which is the sum of the diagonal entries).

-   The **product** of the eigenvalues of a matrix is equal to the **determinant** of the matrix.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
A <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(A\\)</span> has <span class="math-inline">\\(\text{trace}(A) = 5\\)</span> and <span class="math-inline">\\(\text{det}(A) = 6\\)</span>. What are the eigenvalues of <span class="math-inline">\\(A\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
A non-invertible <span class="math-inline">\\(2 \times 2\\)</span> matrix has an eigenvalue of 5. What is its characteristic polynomial?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
A <span class="math-inline">\\(3 \times 3\\)</span> matrix <span class="math-inline">\\(A\\)</span> has <span class="math-inline">\\(\text{det}(A) = 20\\)</span> and two unique **positive integer** eigenvalues, one of which is repeated twice. In other words, <span class="math-inline">\\(p(\lambda)\\)</span> has the form

<div class="math-display">
$$
p(\lambda) = (\lambda - \lambda_1)^2 (\lambda - \lambda_2)
$$
</div>

(<span class="math-inline">\\(\lambda&#95;1\\)</span> has an **algebraic multiplicity** of 2. This is a term we'll see more in tomorrow's lecture and [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/).)

What are all possible values of <span class="math-inline">\\(\lambda&#95;1\\)</span> and <span class="math-inline">\\(\lambda&#95;2\\)</span>?

</div>
</div>

</div>

---

## Activity 3: Quadratic Forms Return

Open Desmos in 3D mode at [desmos.com/3d](https://www.desmos.com/3d) and write <span class="math-inline">\\(z = x^{2}+2bxy+16y^{2}\\)</span>. This should show you a 3D surface along with a slider for <span class="math-inline">\\(b\\)</span>. Drag the slider to see how the shape of the surface changes for different <span class="math-inline">\\(b\\)</span>'s. You should notice that depending on the value of <span class="math-inline">\\(b\\)</span>, the surface may or may not have a global minimum. Let's explore!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(z\\)</span> is a quadratic form, <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span>, where <span class="math-inline">\\(\vec x = \begin{bmatrix} x \\\\ y \end{bmatrix}\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric matrix. Find <span class="math-inline">\\(A\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
For a vector-to-scalar function <span class="math-inline">\\(f: \mathbb{R}^n \to \mathbb{R}\\)</span>, the **Hessian** of <span class="math-inline">\\(f\\)</span>, denoted <span class="math-inline">\\(\nabla^2 f\\)</span>, is the <span class="math-inline">\\(n \times n\\)</span> matrix of second partial derivatives of <span class="math-inline">\\(f\\)</span>. Find <span class="math-inline">\\(\nabla^2 f\\)</span> for <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
A symmetric matrix <span class="math-inline">\\(A\\)</span> is **positive semidefinite** (PSD) if <span class="math-inline">\\(\vec v^T A \vec v \geq 0\\)</span> for all <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>. In English, this says that <span class="math-inline">\\(A\\)</span> is positive semidefinite if the quadratic form <span class="math-inline">\\(f(\vec v) = \vec v^T A \vec v\\)</span> is always non-negative for all <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>. Two relevant facts:

-   A differentiable vector-to-scalar function <span class="math-inline">\\(f\\)</span> is **convex** if its Hessian is PSD.

-   A symmetric matrix <span class="math-inline">\\(A\\)</span> is PSD if and only if all of its eigenvalues are non-negative.

Using the facts above, find the range of values <span class="math-inline">\\(b\\)</span> for which <span class="math-inline">\\(f\\)</span> is convex, and verify your answer by dragging the slider on Desmos.

</div>
</div>

</div>

---

## Activity 4: Understanding Complex Proofs

Let <span class="math-inline">\\(f: \mathbb{R}^n \to \mathbb{R}\\)</span> be a convex function. It turns out that the function <span class="math-inline">\\(g(\vec x)\\)</span>, defined by

<div class="math-display">
$$
g(\vec x) = f(A\vec x + \vec b)
$$
</div>

 for some <span class="math-inline">\\(n \times n\\)</span> matrix <span class="math-inline">\\(A\\)</span> and vector <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>, is also convex, no matter what <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(\vec b\\)</span> are. We're not going to ask you to prove this on your own: instead, we'll give you a proof and ask you questions to ensure you understand it.

<span class="answer-blank"></span>

Our **goal** is to show that <span class="math-inline">\\(g((1-t) \vec x + t \vec y) \leq (1-t) g(\vec x) + t g(\vec y)\\)</span>, for all <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(t \in [0, 1]\\)</span>. We'll start with the "left-hand side" of the definition, and try and leverage <span class="math-inline">\\(f\\)</span>'s convexity.

<div class="math-display">
$$
\begin{align}
g((1-t) \vec x + t \vec y) &= f\left(A\left((1-t) \vec x + t \vec y\right) + \vec b\right) \\\\
&= f\left((1-t)A \vec x + t A \vec y + \vec b\right) \\\\
&= f\left((1-t)(A \vec x + \vec b) + t(A \vec y + \vec b)\right) \\\\
&\leq (1-t)f(A \vec x + \vec b) + t f(A \vec y + \vec b) \\\\
&= \boxed{(1-t)g(\vec x) + t g(\vec y)}
\end{align}
$$
</div>

<span class="answer-blank"></span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
In which line did we use the fact that <span class="math-inline">\\(f\\)</span> is convex?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
How did we move from line (1) to line (2), i.e. <span class="math-inline">\\(f\left(A\left((1-t) \vec x + t \vec y\right) + \vec b\right) = f\left((1-t)A \vec x + t A \vec y + \vec b\right)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
How did we move from line (2) to line (3), i.e. <span class="math-inline">\\(f\left((1-t)A \vec x + t A \vec y + \vec b\right) = f\left((1-t)(A \vec x + \vec b) + t(A \vec y + \vec b)\right)\\)</span>?

Recall, <span class="math-inline">\\(g(\vec x) = f(A\vec x + \vec b)\\)</span>, where <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix and <span class="math-inline">\\(\vec x, \vec b \in \mathbb{R}^n\\)</span>. On the last page, we showed that if <span class="math-inline">\\(f\\)</span> is convex, then <span class="math-inline">\\(g\\)</span> is convex.

Now, let's explore what happens if <span class="math-inline">\\(f\\)</span> is **strictly** convex. Recall, this means that for all (non-equal) <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> in its domain, and for any <span class="math-inline">\\(t \in (0, 1)\\)</span>,

<div class="math-display">
$$
f((1-t) \vec x + t \vec y) < (1-t) f(\vec x) + t f(\vec y)
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\text{rank}(A) = n\\)</span>. Explain why it's impossible for <span class="math-inline">\\(A \vec x + \vec b = A \vec y + \vec b\\)</span> for two different vectors <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\text{rank}(A) &lt; n\\)</span>. Explain why it's possible for <span class="math-inline">\\(g(\vec x) = g(\vec y)\\)</span> for two different vectors <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>. <em>Hint: Think about <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
Using the above reasoning, explain why if <span class="math-inline">\\(f\\)</span> is strictly convex, then <span class="math-inline">\\(g\\)</span> is strictly convex if <span class="math-inline">\\(\text{rank}(A) = n\\)</span>, and is (not strictly) convex if <span class="math-inline">\\(\text{rank}(A) &lt; n\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">g)</div>
<div class="assignment-part-content" markdown="1">
What were your thoughts on this type of activity, where we give you a proof and ask you questions about it?

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Hated it</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Didn't like it</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Neutral</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Liked it</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Loved it</span></div>
</div>
</div>

</div>

{% endraw %}
