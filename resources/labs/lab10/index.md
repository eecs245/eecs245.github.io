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
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab10/lab10-solutions.pdf" target="_blank">Solutions PDF ✅</a>
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

<details markdown="1"><summary>Solution</summary>

**(i)** The characteristic polynomial of <span class="math-inline">\\(A\\)</span> is

<div class="math-display">
$$
\begin{align*}
\det(A - \lambda I) &= \begin{vmatrix} 3 - \lambda & 0 \\\\ 0 & 4 - \lambda \end{vmatrix} \\\\
&= (3 - \lambda)(4 - \lambda)
\end{align*}
$$
</div>

So, the eigenvalues of <span class="math-inline">\\(A\\)</span> are <span class="math-inline">\\(\lambda&#95;1 = 3\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 4\\)</span>. <span class="math-inline">\\(A\\)</span> is a diagonal matrix, which means its eigenvalues are its diagonal entries.

**(ii)** Matching examples we've seen in class (in particular, [this example](https://notes.eecs245.org/eigenvalues-and-eigenvectors/characteristic-polynomial/#example-diagonal-matrices) from Chapter 9.2), an eigenvector for <span class="math-inline">\\(\lambda&#95;1 = 3\\)</span> is <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span> and an eigenvector for <span class="math-inline">\\(\lambda&#95;2 = 4\\)</span> is <span class="math-inline">\\(\vec v&#95;2 = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span>; indeed, <span class="math-inline">\\(A \vec v&#95;1 = 3 \vec v&#95;1\\)</span> and <span class="math-inline">\\(A \vec v&#95;2 = 4 \vec v&#95;2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 4 \\\\ 4 &amp; 3 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

**(i)** The characteristic polynomial of <span class="math-inline">\\(A\\)</span> is

<div class="math-display">
$$
\begin{align*}
\det(A - \lambda I) &= \begin{vmatrix} 3 - \lambda & 4 \\\\ 4 & 3 - \lambda \end{vmatrix} \\\\
&= (3 - \lambda)^2 - 16 \\\\
&= \lambda^2 - 6\lambda + 9 - 16 \\\\
&= \lambda^2 - 6\lambda - 7 \\\\
&= (\lambda + 1)(\lambda - 7)
\end{align*}
$$
</div>

So, the eigenvalues of <span class="math-inline">\\(A\\)</span> are <span class="math-inline">\\(\lambda&#95;1 = -1\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 7\\)</span>.

**(ii)** -   The eigenvector <span class="math-inline">\\(\vec v&#95;1\\)</span> corresponding to <span class="math-inline">\\(\lambda&#95;1 = -1\\)</span> satisfies <span class="math-inline">\\(A \vec v&#95;1 = -1 \vec v&#95;1\\)</span>.



<div class="math-display">
$$
\begin{align*}
    \begin{bmatrix} 3 & 4 \\\\ 4 & 3 \end{bmatrix} \begin{bmatrix} a \\\\ b \end{bmatrix} = -1 \begin{bmatrix} a \\\\ b \end{bmatrix}
    \end{align*}
$$
</div>

The first component implies <span class="math-inline">\\(3a + 4b = -a \implies 4a + 4b = 0 \implies a = -b\\)</span>. So, an eigenvector <span class="math-inline">\\(\vec v&#95;1\\)</span> is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \end{bmatrix}\\)</span> (though there are infinitely many other choices; any scalar multiple of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \end{bmatrix}\\)</span> is also an eigenvector for eigenvalue -1). Note that using the second component would give us the same relationship. To verify that we correctly found the eigenvector-eigenvalue pair, multiplying <span class="math-inline">\\(A\\)</span> by <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \end{bmatrix}\\)</span> gives

<div class="math-display">
$$
A \begin{bmatrix} 1 \\\\ -1 \end{bmatrix} = \begin{bmatrix} 3 - 4 \\\\ 4 - 3 \end{bmatrix} = \begin{bmatrix}-1 \\\\ 1 \end{bmatrix} = -1 \begin{bmatrix} 1 \\\\ -1 \end{bmatrix}
$$
</div>

 (We will omit this step moving forward.)

-   The eigenvector <span class="math-inline">\\(\vec v&#95;2\\)</span> corresponding to <span class="math-inline">\\(\lambda&#95;2 = 7\\)</span> satisfies <span class="math-inline">\\(A \vec v&#95;2 = 7 \vec v&#95;2\\)</span>.



<div class="math-display">
$$
\begin{align*}
    \begin{bmatrix} 3 & 4 \\\\ 4 & 3 \end{bmatrix} \begin{bmatrix} c \\\\ d \end{bmatrix} = 7 \begin{bmatrix} c \\\\ d \end{bmatrix}
    \end{align*}
$$
</div>

The first component implies <span class="math-inline">\\(3c + 4d = 7c \implies 4c - 4d = 0 \implies c = d\\)</span>. So, an eigenvector <span class="math-inline">\\(\vec v&#95;2\\)</span> is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \end{bmatrix}\\)</span>.

To conclude,

<div class="math-display">
$$
\boxed{\lambda_1 = -1, \vec v_1 = \begin{bmatrix} 1 \\\\ -1 \end{bmatrix}, \qquad \lambda_2 = 7, \vec v_2 = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lambda&#95;1 = 2, \lambda&#95;2 = 3\\)</span>.

The eigenvalues of <span class="math-inline">\\(A\\)</span> must sum to 5 and multiply to 6. The only possible solution is <span class="math-inline">\\(\lambda&#95;1 = 2\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 3\\)</span>, which indeed satisfy both conditions. There are infinitely many **matrices** that satisfy these conditions, but the eigenvalues in all of them are <span class="math-inline">\\(2\\)</span> and <span class="math-inline">\\(3\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
A non-invertible <span class="math-inline">\\(2 \times 2\\)</span> matrix has an eigenvalue of 5. What is its characteristic polynomial?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(p(\lambda) = \lambda^2 - 5\lambda\\)</span>.

Let <span class="math-inline">\\(A\\)</span> be the matrix in question. Since <span class="math-inline">\\(A\\)</span> is not invertible, 0 is one of its eigenvalues. Since it's a <span class="math-inline">\\(2 \times 2\\)</span> matrix, it can only have two eigenvalues, so its two eigenvalues are 0 and 5. So, its characteristic polynomial is a polynomial with roots 0 and 5, i.e.

<div class="math-display">
$$
p(\lambda) = (\lambda - 0)(\lambda - 5) = \lambda^2 - 5\lambda
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lambda&#95;1 = 2, \lambda&#95;2 = 5\\)</span> or <span class="math-inline">\\(\lambda&#95;1 = 1, \lambda&#95;2 = 20\\)</span>.

The product of <span class="math-inline">\\(A\\)</span>'s eigenvalues --- including arithmetic multiplicities --- is equal to the determinant of <span class="math-inline">\\(A\\)</span>. Since <span class="math-inline">\\(\lambda&#95;1\\)</span> has <span class="math-inline">\\(\text{AM}(\lambda&#95;1) = 2\\)</span>, it must appear twice in the product of the eigenvalues. So,

<div class="math-display">
$$
\lambda_1^2 \lambda_2 = 20
$$
</div>

We're told that <span class="math-inline">\\(\lambda&#95;1\\)</span> and <span class="math-inline">\\(\lambda&#95;2\\)</span> are integers. Note that <span class="math-inline">\\(20 = 2 \cdot 10 = 2 \cdot 2 \cdot 5\\)</span>. The only possible solutions are <span class="math-inline">\\(\lambda&#95;1 = 2\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 5\\)</span> (which means <span class="math-inline">\\(\lambda&#95;1^2 \lambda&#95;2 = (2)^2 \cdot 5 = 20\\)</span>) or <span class="math-inline">\\(\lambda&#95;1 = 1\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 20\\)</span> (which means <span class="math-inline">\\(\lambda&#95;1^2 \lambda&#95;2 = (1)^2 \cdot 20 = 20\\)</span>).
</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; b \\\\ b &amp; 16 \end{bmatrix}\\)</span>.

To see where this comes from, let's expand <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span>:

<div class="math-display">
$$
\begin{align*}
f(\vec x) &= \vec x^T A \vec x \\\\
&= \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} 1 & b \\\\ b & 16 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} \\\\
&= \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} x + by \\\\ bx + 16y \end{bmatrix} \\\\
&= x(x + by) + y(bx + 16y) \\\\
&= x^2 + bxy + bxy + 16y^2 \\\\
&= x^2 + 2bxy + 16y^2
\end{align*}
$$
</div>

So, <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; b \\\\ b &amp; 16 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
For a vector-to-scalar function <span class="math-inline">\\(f: \mathbb{R}^n \to \mathbb{R}\\)</span>, the **Hessian** of <span class="math-inline">\\(f\\)</span>, denoted <span class="math-inline">\\(\nabla^2 f\\)</span>, is the <span class="math-inline">\\(n \times n\\)</span> matrix of second partial derivatives of <span class="math-inline">\\(f\\)</span>. Find <span class="math-inline">\\(\nabla^2 f\\)</span> for <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\nabla^2 f = \begin{bmatrix} 2b &amp; 2b \\\\ 2b &amp; 32 \end{bmatrix}\\)</span>.

To find the second partial derivatives of <span class="math-inline">\\(f\\)</span>, we first find the first partial derivatives:

<div class="math-display">
$$
\begin{align*}
f(\vec x) = \vec x^T A \vec x &= x^2 + 2bxy + 16y^2 \\\\
\frac{\partial f}{\partial x} &= 2x + 2by \\\\
\frac{\partial f}{\partial y} &= 2bx + 32y
\end{align*}
$$
</div>

Since there are two first partial derivatives, there are <span class="math-inline">\\(2 \times 2 = 4\\)</span> second partial derivatives. We can find them all by taking the partial derivatives of the first partial derivatives:

<div class="math-display">
$$
\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= \frac{\partial}{\partial x} \left( 2x + 2by \right) = 2 \\\\
\frac{\partial^2 f}{\partial x \partial y} &= \frac{\partial}{\partial y} \left( 2x + 2by \right) = 2b \\\\
\frac{\partial^2 f}{\partial y \partial x} &= \frac{\partial}{\partial x} \left( 2bx + 32y \right) = 2b \\\\
\frac{\partial^2 f}{\partial y^2} &= \frac{\partial}{\partial y} \left( 2bx + 32y \right) = 32
\end{align*}
$$
</div>

Note that <span class="math-inline">\\(\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}\\)</span>, which is a general property of second partial derivatives --- it doesn't matter which order we take the derivatives in. So, the Hessian is

<div class="math-display">
$$
\nabla^2 f = \begin{bmatrix} 2 & 2b \\\\ 2b & 32 \end{bmatrix}
$$
</div>

Notice that this is just <span class="math-inline">\\(2A\\)</span>!
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
A symmetric matrix <span class="math-inline">\\(A\\)</span> is **positive semidefinite** (PSD) if <span class="math-inline">\\(\vec v^T A \vec v \geq 0\\)</span> for all <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>. In English, this says that <span class="math-inline">\\(A\\)</span> is positive semidefinite if the quadratic form <span class="math-inline">\\(f(\vec v) = \vec v^T A \vec v\\)</span> is always non-negative for all <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>. Two relevant facts:

-   A differentiable vector-to-scalar function <span class="math-inline">\\(f\\)</span> is **convex** if its Hessian is PSD.

-   A symmetric matrix <span class="math-inline">\\(A\\)</span> is PSD if and only if all of its eigenvalues are non-negative.

Using the facts above, find the range of values <span class="math-inline">\\(b\\)</span> for which <span class="math-inline">\\(f\\)</span> is convex, and verify your answer by dragging the slider on Desmos.

<details markdown="1"><summary>Solution</summary>

As long as <span class="math-inline">\\(-4 \leq b \leq 4\\)</span>, the Hessian is PSD, and <span class="math-inline">\\(f\\)</span> is convex.

Recall from the previous part that the Hessian is

<div class="math-display">
$$
\nabla^2 f = \begin{bmatrix} 2 & 2b \\\\ 2b & 32 \end{bmatrix} = 2A
$$
</div>

<span class="math-inline">\\(f\\)</span> is convex if and only if <span class="math-inline">\\(2A\\)</span> is PSD, which means that both of <span class="math-inline">\\(2A\\)</span>'s eigenvalues are non-negative. Let <span class="math-inline">\\(\lambda&#95;1\\)</span> and <span class="math-inline">\\(\lambda&#95;2\\)</span> be <span class="math-inline">\\(2A\\)</span>'s eigenvalues. Then, we need <span class="math-inline">\\(\lambda&#95;1 \geq 0\\)</span> and <span class="math-inline">\\(\lambda&#95;2 \geq 0\\)</span>. How do we ensure this?

Let's recall the facts about the trace and determinant introduced at the start of Activity 2:

-   The sum of <span class="math-inline">\\(2A\\)</span>'s eigenvalues, <span class="math-inline">\\(\lambda&#95;1 + \lambda&#95;2\\)</span>, is equal to the trace of <span class="math-inline">\\(2A\\)</span>, <span class="math-inline">\\(\text{trace}(2A)\\)</span>, which is the sum of the diagonal entries of <span class="math-inline">\\(2A\\)</span>. Here, this is <span class="math-inline">\\(2 + 32 = 34\\)</span>.

-   The product of <span class="math-inline">\\(2A\\)</span>'s eigenvalues, <span class="math-inline">\\(\lambda&#95;1 \lambda&#95;2\\)</span>, is equal to the determinant of <span class="math-inline">\\(2A\\)</span>, <span class="math-inline">\\(\det(2A)\\)</span>, which is <span class="math-inline">\\(2 \cdot 32 - (2b)^2 = 64 - 4b^2\\)</span>.

The fact that <span class="math-inline">\\(\lambda&#95;1 + \lambda&#95;2 = 34\\)</span> means that no matter what <span class="math-inline">\\(b\\)</span> is, at least one of the eigenvalues is non-negative, since you can't add two negative numbers and get a positive sum.

So, let's focus our attention on the product of the eigenvalues, <span class="math-inline">\\(\lambda&#95;1 \lambda&#95;2 = 64 - 4b^2\\)</span>. We need this to be <span class="math-inline">\\(\geq 0\\)</span>, because if it were negative, then one of the eigenvalues would be negative (since multiplying a positive number by a negative number gives a negative number).

Using this reasoning, we need <span class="math-inline">\\(64 - 4b^2 \geq 0\\)</span>, which simplifies to <span class="math-inline">\\(4b^2 \leq 64\\)</span>, which simplifies to <span class="math-inline">\\(b^2 \leq 16\\)</span>, which simplifies to <span class="math-inline">\\(-4 \leq b \leq 4\\)</span>. If <span class="math-inline">\\(|b| &gt; 4\\)</span>, then one of the eigenvalues would be negative, <span class="math-inline">\\(2A\\)</span> would not be PSD, and <span class="math-inline">\\(f\\)</span> would not be convex.

Notice that in this case, the "test" for convexity ended up simplifying to checking whether the determinant of <span class="math-inline">\\(A\\)</span> is non-negative. That is true, in general, for quadratic forms <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span> where <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(2 \times 2\\)</span>symmetric matrix. But if <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(3 \times 3\\)</span> or larger, the determinant test alone isn't sufficient; it's possible to have a positive determinant and trace but a negative eigenvalue in a <span class="math-inline">\\(3 \times 3\\)</span> matrix. What **is** true in general is that if <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix, then <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span> is convex if and only if all of <span class="math-inline">\\(A\\)</span>'s eigenvalues are non-negative.
</details>

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

<details markdown="1"><summary>Solution</summary>

Line 4. We simplified the original expression to the form of the formal definition's left side in line 3, and line 4 is where we connect it back to the right side.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
How did we move from line (1) to line (2), i.e. <span class="math-inline">\\(f\left(A\left((1-t) \vec x + t \vec y\right) + \vec b\right) = f\left((1-t)A \vec x + t A \vec y + \vec b\right)\\)</span>?

<details markdown="1"><summary>Solution</summary>

Distributing <span class="math-inline">\\(A\\)</span> by left multiplying it to the terms in the parentheses.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
How did we move from line (2) to line (3), i.e. <span class="math-inline">\\(f\left((1-t)A \vec x + t A \vec y + \vec b\right) = f\left((1-t)(A \vec x + \vec b) + t(A \vec y + \vec b)\right)\\)</span>?

<details markdown="1"><summary>Solution</summary>

Add <span class="math-inline">\\(t\vec b - t\vec b\\)</span> to the input expression, that way we can increase the number of terms without changing the value of the expression.
</details>

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

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\text{rank}(A) = n\\)</span>, then the columns of <span class="math-inline">\\(A\\)</span> are linearly independent, so <span class="math-inline">\\(A\vec x\\)</span> and <span class="math-inline">\\(A\vec y\\)</span> must be different for any <span class="math-inline">\\(\vec x \neq \vec y\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\text{rank}(A) &lt; n\\)</span>. Explain why it's possible for <span class="math-inline">\\(g(\vec x) = g(\vec y)\\)</span> for two different vectors <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>. <em>Hint: Think about <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\text{rank}(A) &lt; n\\)</span>, then <span class="math-inline">\\(A\\)</span>'s columns are linearly dependent, so <span class="math-inline">\\(A\vec x\\)</span> and <span class="math-inline">\\(A\vec y\\)</span> can be the same vector. In that case, <span class="math-inline">\\(f(A\vec x + \vec b)=f(A\vec y + \vec b) \rightarrow g(\vec x)=g(\vec y)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
Using the above reasoning, explain why if <span class="math-inline">\\(f\\)</span> is strictly convex, then <span class="math-inline">\\(g\\)</span> is strictly convex if <span class="math-inline">\\(\text{rank}(A) = n\\)</span>, and is (not strictly) convex if <span class="math-inline">\\(\text{rank}(A) &lt; n\\)</span>.

<details markdown="1"><summary>Solution</summary>

We can show this with a proof by cases. In both cases, we'll start from line 4 of the proof on the previous page, but with <span class="math-inline">\\(f\\)</span> being strictly convex.

Case 1: <span class="math-inline">\\(\text{rank}(A) = n\\)</span>

<div class="math-display">
$$
\begin{align*}
g((1-t) \vec x + t \vec y)&< (1-t)f(A \vec x + \vec b) + t f(A \vec y + \vec b)
\\\\&<(1-t)g(\vec x)+tg(\vec y)
\end{align*}
$$
</div>

Case 2: <span class="math-inline">\\(\text{rank}(A) &lt; n\\)</span>

We know from part **e)** that it's possible for <span class="math-inline">\\(g(\vec x)=g(\vec y)\\)</span>. Using proof by contradiction, assume that <span class="math-inline">\\(g\\)</span> is strictly convex.

<div class="math-display">
$$
\begin{align*}
g((1-t) \vec x + t \vec y)&< (1-t)f(A \vec x + \vec b) + t f(A \vec y + \vec b)
\\\\&<(1-t)g(\vec x)+tg(\vec y)
\\\\&<(1-t)g(\vec x)+tg(\vec x)
\\\\&<g(\vec x)
\end{align*}
$$
</div>

This is a contradiction, because if <span class="math-inline">\\(t=0\\)</span>, then the left side of the inequality is <span class="math-inline">\\(g(\vec x)\\)</span>, leaving us with <span class="math-inline">\\(g(\vec x)&lt;g(\vec x)\\)</span>.
</details>

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
