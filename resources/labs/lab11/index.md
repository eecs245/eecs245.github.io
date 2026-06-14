---
layout: page
title: "Lab 11: Adjacency Matrices and Diagonalization"
description: "Lab 11: Adjacency Matrices and Diagonalization activities."
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

# Lab 11: Adjacency Matrices and Diagonalization

**due** for completion at 11:59PM Ann Arbor Time on Wednesday, June 17th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab11/lab11.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Rapid Fire](#activity-1-rapid-fire)
- [Activity 2: Fundamentals](#activity-2-fundamentals)
- [Activity 3: Adjacency Matrices](#activity-3-adjacency-matrices)
- [Activity 4: Symmetric Matrices](#activity-4-symmetric-matrices)
- [Activity 5: More Practice (Optional)](#activity-5-more-practice-optional)

---

**Recap: Diagonalization** ([Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/))

-   Since <span class="math-inline">\\(A\\)</span> has two linearly independent eigenvectors, it is **diagonalizable**, meaning we can write

<div class="math-display">
$$
A = V \Lambda V^{-1} = \underbrace{\begin{bmatrix} 2 & 3 \\\\ -6 & 1 \end{bmatrix}}_{V} \underbrace{\begin{bmatrix} -3 & 0 \\\\ 0 & 7 \end{bmatrix}}_{\Lambda} \underbrace{\begin{bmatrix} 0.05 & -0.15 \\\\ 0.3 & 0.1 \end{bmatrix}}_{V^{-1}}
$$
</div>

 where <span class="math-inline">\\(V\\)</span> is an invertible matrix whose columns are the eigenvectors of <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(\Lambda\\)</span> is a diagonal matrix with the eigenvalues of <span class="math-inline">\\(A\\)</span> on the diagonal.

-   The **algebraic multiplicity** of an eigenvalue, <span class="math-inline">\\(\text{AM}(\lambda&#95;i)\\)</span>, is the number of times it appears as a root of the characteristic polynomial.

<div class="math-display">
$$
p(\lambda) = (\lambda - \lambda_1)^{\text{AM}(\lambda_1)} (\lambda - \lambda_2)^{\text{AM}(\lambda_2)} \cdots (\lambda - \lambda_k)^{\text{AM}(\lambda_k)}
$$
</div>

-   The **geometric multiplicity** of an eigenvalue, <span class="math-inline">\\(\text{GM}(\lambda&#95;i)\\)</span>, is the dimension of the eigenspace corresponding to <span class="math-inline">\\(\lambda&#95;i\\)</span>.

<div class="math-display">
$$
\text{GM}(\lambda_i) = \text{dim}(\text{nullsp}(A - \lambda_i I)) = \text{number of linearly independent eigenvectors corresponding to } \lambda_i
$$
</div>

-   For any <span class="math-inline">\\(\lambda&#95;i\\)</span>, <span class="math-inline">\\(1 \leq \text{GM}(\lambda&#95;i) \leq \text{AM}(\lambda&#95;i)\\)</span>.

-   <span class="math-inline">\\(A\\)</span> is diagonalizable if and only if <span class="math-inline">\\(\text{AM}(\lambda&#95;i) = \text{GM}(\lambda&#95;i)\\)</span> for all eigenvalues <span class="math-inline">\\(\lambda&#95;i\\)</span>. This ensures that <span class="math-inline">\\(A\\)</span>'s eigenvectors form a basis of <span class="math-inline">\\(\mathbb{R}^n\\)</span>.

-   <span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; -1 \\\\ 1 &amp; 1 \end{bmatrix}\\)</span> has characteristic polynomial <span class="math-inline">\\(p(\lambda) = (2 - \lambda)^2\\)</span>. The eigenvalue <span class="math-inline">\\(\lambda = 2\\)</span> has algebraic multiplicity 2, but the corresponding eigenspace is only 1-dimensional:

<div class="math-display">
$$
\text{nullsp}(A - 2I) = \text{nullsp}\left(\begin{bmatrix} 1 & -1 \\\\ 1 & -1 \end{bmatrix}\right) = \text{span}\left(\begin{bmatrix} 1 \\\\ 1 \end{bmatrix}\right)
$$
</div>

 so, <span class="math-inline">\\(\lambda = 2\\)</span> has geometric multiplicity 1. Since <span class="math-inline">\\(\text{AM}(2) \neq \text{GM}(2)\\)</span>, <span class="math-inline">\\(A\\)</span> is **not diagonalizable**.

-   <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 &amp; 0 \\\\ -1 &amp; 2 &amp; 1 \\\\ -1 &amp; 1 &amp; 2 \end{bmatrix}\\)</span> has characteristic polynomial <span class="math-inline">\\(p(\lambda) = (1 - \lambda)^2(3 - \lambda)\\)</span>, so <span class="math-inline">\\(\lambda&#95;1 = 1\\)</span> has <span class="math-inline">\\(\text{AM}(\lambda&#95;1) = 2\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 3\\)</span> has <span class="math-inline">\\(\text{AM}(\lambda&#95;2) = 1\\)</span>. The eigenspace for <span class="math-inline">\\(\lambda&#95;1 = 1\\)</span> is 2-dimensional,

<div class="math-display">
$$
\text{nullsp}(A - 1 I) = \text{nullsp}\left(\begin{bmatrix} 0 & 0 & 0 \\\\ -1 & 1 & 1 \\\\ -1 & 1 & 1 \end{bmatrix}\right) = \text{span}\left(\begin{bmatrix} 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \end{bmatrix}\right)
$$
</div>

 so <span class="math-inline">\\(\text{GM}(\lambda&#95;1) = 2\\)</span>. Since <span class="math-inline">\\(\text{AM}(\lambda&#95;i) = \text{GM}(\lambda&#95;i)\\)</span> for all eigenvalues <span class="math-inline">\\(\lambda&#95;i\\)</span>, <span class="math-inline">\\(A\\)</span> is **diagonalizable**.

<div class="math-display">
$$
A = V \Lambda V^{-1} = \underbrace{\begin{bmatrix} 1 & 1 & 0 \\\\ 1 & 0 & 1 \\\\ 0 & 1 & 1 \end{bmatrix}}_{V} \underbrace{\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 3 \end{bmatrix}}_{\Lambda} \underbrace{\begin{bmatrix} 0.5 & 0.5 & -0.5 \\\\ 0.5 & -0.5 & 0.5 \\\\ -0.5 & 0.5 & 0.5 \end{bmatrix}}_{V^{-1}}
$$
</div>

-   Diagonalizability is not the same as invertibility!

---

## Activity 1: Rapid Fire

The goal here is to answer the problems **quickly** without working out the details.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 2 &amp; 3 \\\\ 0 &amp; 4 &amp; 5 \\\\ 0 &amp; 0 &amp; 6 \end{bmatrix}\\)</span>. What are the eigenvalues of <span class="math-inline">\\(A\\)</span>? Is <span class="math-inline">\\(A\\)</span> diagonalizable?

<em>Hint: Use the fact that <span class="math-inline">\\(A\\)</span> is an upper triangular matrix. What is <span class="math-inline">\\(\det(A - \lambda I)\\)</span>?</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
A <span class="math-inline">\\(5 \times 5\\)</span> matrix has an eigenvalue of 0 with geometric multiplicity 2. What is its rank?

</div>
</div>

</div>

---

## Activity 2: Fundamentals

Let <span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 2 &amp; 0 \\\\ 2 &amp; 3 &amp; 0 \\\\ 0 &amp; 0 &amp; 5 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find the characteristic polynomial of <span class="math-inline">\\(A\\)</span>, and use it to find the eigenvalues of <span class="math-inline">\\(A\\)</span> and their algebraic multiplicities.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for the eigenspace corresponding to each eigenvalue.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
This particular <span class="math-inline">\\(A\\)</span> is diagonalizable. Diagonalize <span class="math-inline">\\(A\\)</span> by finding a matrix <span class="math-inline">\\(V\\)</span> and a diagonal matrix <span class="math-inline">\\(\Lambda\\)</span> such that <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>.

</div>
</div>

</div>

---

## Activity 3: Adjacency Matrices

Suppose that each night, a Wolverine moves between three classic Ann Arbor spots: the Diag, Zingerman's, and the Big House.

-   From the Diag, <span class="math-inline">\\(\frac{2}{3}\\)</span> of the time it stays at the Diag, <span class="math-inline">\\(\frac{1}{6}\\)</span> of the time it walks to Zingerman's, and <span class="math-inline">\\(\frac{1}{6}\\)</span> of the time it walks to the Big House.

-   From the Big House, it **always** walks to Zingerman's.

-   From Zingerman's, it is **equally likely** to walk to the Diag or the Big House.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Draw a state diagram for this Markov chain. Make sure to clearly label the edges with their transition probabilities. (For help, see [Chapter 9.3](https://notes.eecs245.org/eigenvalues-and-eigenvectors/markov-chains-adjacency-matrices/).)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find the adjacency matrix, <span class="math-inline">\\(A\\)</span>, of this Markov chain.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Show that the long-run distribution of the Wolverine's locations is <span class="math-inline">\\(\begin{bmatrix} p(\text{Diag}) \\\\ p(\text{Big House}) \\\\ p(\text{Zingerman's}) \end{bmatrix} = \begin{bmatrix} 6/13 \\\\ 3/13 \\\\ 4/13 \end{bmatrix}\\)</span>. <em>Hint: Do this by finding the eigenvector of <span class="math-inline">\\(A\\)</span> corresponding to the eigenvalue 1. Since there are infinitely many such eigenvectors, find the one that satisfies the constraint that the components sum to 1.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Open a new Jupyter Notebook or interactive Python session in the Terminal. In it, run:

```python
import numpy as np
A = np.array(...) # Replace with the adjacency matrix you found in b)
eigvals, eigvecs = np.linalg.eig(A)
```
Now, if you run `eigvals`, you should see

```python
array([ 1.        ,  0.36037961, -0.69371294])
```
If you run `eigvecs[:, 0]` to access the eigenvector corresponding to the first eigenvalue in the array above, you should see

```python
array([0.76822128, 0.38411064, 0.51214752])
```
This is **not** the eigenvector you found in the previous part. Why not? What did it return, and what expression can you run in code to find the exact answer you found in the previous part?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Run both of the following commands:

```python
np.linalg.matrix_power(A, 20) @ np.array([[1/3], [1/3], [1/3]])
np.linalg.matrix_power(A, 21) @ np.array([[1/3], [1/3], [1/3]])
```
What do you see? Why?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
Now, consider the adjacency matrix

<div class="math-display">
$$
B = \begin{bmatrix} 0 & 0 & 1/2 \\\\ 0 & 0 & 1/2 \\\\ 1 & 1 & 0 \end{bmatrix}
$$
</div>

Using `numpy`, find the eigenvalues of <span class="math-inline">\\(B\\)</span>. Then, run all of the following commands:

```python
np.linalg.matrix_power(B, 20) @ np.array([[1/3], [1/3], [1/3]])
np.linalg.matrix_power(B, 21) @ np.array([[1/3], [1/3], [1/3]])
np.linalg.matrix_power(B, 22) @ np.array([[1/3], [1/3], [1/3]])
np.linalg.matrix_power(B, 23) @ np.array([[1/3], [1/3], [1/3]])
```
This Markov chain appears not to converge. **Why not?** Relate your answer to the discussion of "the dominant eigenvalue" in [Chapter 9.3](https://notes.eecs245.org/eigenvalues-and-eigenvectors/markov-chains-adjacency-matrices/).

</div>
</div>

</div>

---

## Activity 4: Symmetric Matrices

Suppose <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix, meaning <span class="math-inline">\\(A = A^T\\)</span>. Symmetric matrices have a special property, described by the spectral theorem: **the eigenvectors corresponding to different eigenvalues are orthogonal**. Below, we provide a proof of this fact.

`1.` Let <span class="math-inline">\\(\vec v&#95;i\\)</span> be an eigenvector of <span class="math-inline">\\(A\\)</span> with eigenvalue <span class="math-inline">\\(\lambda&#95;i\\)</span>, so <span class="math-inline">\\(A \vec v&#95;i = \lambda&#95;i \vec v&#95;i\\)</span>.

`2.` Let <span class="math-inline">\\(\vec v&#95;j\\)</span> be an eigenvector of <span class="math-inline">\\(A\\)</span> with eigenvalue <span class="math-inline">\\(\lambda&#95;j\\)</span>, where <span class="math-inline">\\(\lambda&#95;i \neq \lambda&#95;j\\)</span>, so <span class="math-inline">\\(A \vec v&#95;j = \lambda&#95;j \vec v&#95;j\\)</span>.

`3.` The dot product of <span class="math-inline">\\(\vec v&#95;i\\)</span> and <span class="math-inline">\\(A \vec v&#95;j\\)</span> is <span class="math-inline">\\(\vec v&#95;i \cdot (A \vec v&#95;j) = \vec v&#95;i \cdot (\lambda&#95;j \vec v&#95;j) = \lambda&#95;j (\vec v&#95;i \cdot \vec v&#95;j)\\)</span>.

`4.` But also, <span class="math-inline">\\(\vec v&#95;i \cdot (A \vec v&#95;j) = \vec v&#95;i^T A \vec v&#95;j = \vec v&#95;i^T A^T \vec v&#95;j = (A \vec v&#95;i)^T \vec v&#95;j = \lambda&#95;i \vec v&#95;i^T \vec v&#95;j = \lambda&#95;i (\vec v&#95;i \cdot \vec v&#95;j)\\)</span>.

`5.` The final expressions in both cases are equal, so <span class="math-inline">\\(\lambda&#95;j (\vec v&#95;i \cdot \vec v&#95;j) = \lambda&#95;i (\vec v&#95;i \cdot \vec v&#95;j)\\)</span>.

`6.` Equivalently, <span class="math-inline">\\((\lambda&#95;j - \lambda&#95;i) (\vec v&#95;i \cdot \vec v&#95;j) = 0\\)</span>. But since <span class="math-inline">\\(\lambda&#95;i \neq \lambda&#95;j\\)</span>, we must have <span class="math-inline">\\(\vec v&#95;i \cdot \vec v&#95;j = 0\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
In which line did we use the fact that <span class="math-inline">\\(A\\)</span> is symmetric? Select the line below, and then in that line, circle the specific part of the equation that uses the fact that <span class="math-inline">\\(A = A^T\\)</span>.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
The **spectral theorem** states that any symmetric <span class="math-inline">\\(n \times n\\)</span> matrix <span class="math-inline">\\(A\\)</span> can be diagonalized by an orthogonal matrix <span class="math-inline">\\(Q\\)</span> through

<div class="math-display">
$$
A = Q \Lambda Q^T
$$
</div>

Explain how this relates to the "regular" diagonalization <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>. Why does the equation above contain <span class="math-inline">\\(Q^T\\)</span> instead of <span class="math-inline">\\(Q^{-1}\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Symmetric matrices play a big role in solving optimization problems in machine learning. You'll get a taste of this in Homework 10, Problem 6, which discusses *ridge regression* and *regularization*, ideas that we use to make sure that our models are not overfitting to training data.

Here, we'll prove a related fact: **if <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> symmetric matrix and all of its eigenvalues are non-negative, then <span class="math-inline">\\(A\\)</span> is positive semidefinite.** A symmetric matrix <span class="math-inline">\\(A\\)</span> is positive semidefinite if and only if <span class="math-inline">\\(\boxed{\vec v^T A \vec v \geq 0}\\)</span> for all <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>. One interpretation: this means the quadratic form <span class="math-inline">\\(f(\vec v) = \vec v^T A \vec v\\)</span> is always greater than or equal to 0, no matter what <span class="math-inline">\\(\vec v\\)</span> is.

Let's work through the proof step-by-step: we will do some of it for you, and you'll complete the rest. (To be precise, we're only proving one direction of the "if and only if" statement; the other direction is in Homework 10!) First, since <span class="math-inline">\\(A\\)</span> is symmetric, the **spectral theorem** tells us that <span class="math-inline">\\(A\\)</span> can be written as

<div class="math-display">
$$
A = Q \Lambda Q^T
$$
</div>

 where <span class="math-inline">\\(Q\\)</span> is an orthogonal matrix and <span class="math-inline">\\(\Lambda\\)</span> is a diagonal matrix with the eigenvalues of <span class="math-inline">\\(A\\)</span> on the diagonal. This is the eigenvector decomposition of <span class="math-inline">\\(A\\)</span>.

On top of that, suppose that all of <span class="math-inline">\\(A\\)</span>'s eigenvalues, <span class="math-inline">\\(\lambda&#95;1, \lambda&#95;2, \ldots, \lambda&#95;n\\)</span>, are non-negative.

Now, let <span class="math-inline">\\(\vec v\\)</span> be some arbitrary vector (not necessarily an eigenvector of <span class="math-inline">\\(A\\)</span>) in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. Then, eventually we need to show that <span class="math-inline">\\(\vec v^T A \vec v \geq 0\\)</span>, regardless of what <span class="math-inline">\\(\vec v\\)</span> is. Let's start by expanding <span class="math-inline">\\(\vec v^T A \vec v\\)</span> using the fact that <span class="math-inline">\\(A = Q \Lambda Q^T\\)</span>.

<div class="math-display">
$$
\vec v^T A \vec v = \vec v^T (Q \Lambda Q^T) \vec v = (\vec v^T Q) \Lambda (Q^T \vec v)
$$
</div>

Suppose that <span class="math-inline">\\(\vec y = Q^T \vec v\\)</span>. Then, <span class="math-inline">\\(\vec y^T = (Q^T \vec v)^T = \vec v^T Q\\)</span>. This seems like an arbitrary maneuver, but it will be useful in a moment.

<div class="math-display">
$$
\begin{align*}
\vec v^T A \vec v &= \vec y^T \Lambda \vec y =\begin{bmatrix} y_1 & y_2 & \ldots & y_n \end{bmatrix}
\begin{bmatrix}
\lambda_1 & 0 & \ldots & 0 \\\\
0 & \lambda_2 & \ldots & 0 \\\\
\vdots & \vdots & \ddots & \vdots \\\\
0 & 0 & \ldots & \lambda_n
\end{bmatrix}
\begin{bmatrix}
y_1 \\\\ y_2 \\\\ \vdots \\\\ y_n
\end{bmatrix}
\end{align*}
$$
</div>

**Your job** is to complete the rest of the proof. Show that if <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> symmetric matrix and all of its eigenvalues are non-negative, then <span class="math-inline">\\(\vec v^T A \vec v \geq 0\\)</span> for all <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>.

</div>
</div>

</div>

---

## Activity 5: More Practice (Optional)

Let <span class="math-inline">\\(A\\)</span> be a <span class="math-inline">\\(3 \times 3\\)</span> with:

-   eigenvalue <span class="math-inline">\\(\lambda&#95;1 = 3\\)</span> with eigenvector <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix} 2 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>.

-   eigenvalue <span class="math-inline">\\(\lambda&#95;2 = -2\\)</span> with the 2-dimensional eigenspace: <span class="math-inline">\\(\text{span}\left(\begin{bmatrix} 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 1 \\\\ 2 \end{bmatrix}\right)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(A\\)</span>. Feel free to use `numpy` to find an inverse for you and verify your answer.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(V\\)</span> be the matrix whose columns are the eigenvectors of <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(\Lambda\\)</span> be the diagonal matrix with the eigenvalues of <span class="math-inline">\\(A\\)</span> on the diagonal. In terms of <span class="math-inline">\\(V\\)</span> and <span class="math-inline">\\(\Lambda\\)</span>, what is <span class="math-inline">\\(A^{8}\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span> is some vector. As <span class="math-inline">\\(k \to \infty\\)</span>, what does <span class="math-inline">\\(A^k \vec x\\)</span> approach? Explain your answer in English.
</div>
</div>

</div>

{% endraw %}
