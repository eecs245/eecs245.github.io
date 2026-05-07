---
layout: page
title: "Homework 11: Singular Value Decomposition"
description: "Homework 11: Singular Value Decomposition problems."
nav_exclude: true
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
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
</style>

# Homework 11: Singular Value Decomposition

**due** Wednesday, June 17th, 2026 at 11:59PM Ann Arbor Time

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 10 Solutions Review](#problem-1-homework-10-solutions-review-10-pts)
- [Problem 2: SVD Fundamentals](#problem-2-svd-fundamentals-18-pts)
- [Problem 3: Frobenius Norm and Low-Rank Approximation](#problem-3-frobenius-norm-and-low-rank-approximation-22-pts)
- [Problem 4: Principal Components Analysis](#problem-4-principal-components-analysis-15-pts)

---

Total Points: 10 + 18 + 22 + 15 = 65

---

## Problem 1: Homework 10 Solutions Review (10 pts)

Review the solutions to Homework 10. Pick **two problem parts** (for example, Problem 6b and Problem 7c) from Homework 10 in which your solutions have the most room for improvement, i.e. where they have unsound reasoning, could be significantly more efficient or clearer, etc. Include a screenshot of your solution to each problem part, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 10, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: SVD Fundamentals (18 pts)

Before getting started, make sure to refer to [Chapter 10.1](https://notes.eecs245.org/singular-value-decomposition/computing-svd/). These problems aren't as computationally intensive as they look; think about ways to be efficient.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(A\\)</span> be a <span class="math-inline">\\(2 \times 2\\)</span> matrix with singular value decomposition <span class="math-inline">\\(A = U \Sigma V^T\\)</span> where:

-   The first column of <span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(\vec u_1 = \begin{bmatrix} 2/\sqrt{5} \\\\ 1/\sqrt{5} \end{bmatrix}\\)</span>.

-   <span class="math-inline">\\(A \vec v_1 = 3 \vec u_1\\)</span>, where <span class="math-inline">\\(\vec v_1 = \begin{bmatrix} 1/\sqrt{2} \\\\ 1/\sqrt{2} \end{bmatrix}\\)</span> is the first column of <span class="math-inline">\\(V\\)</span>.

-   The second singular value of <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\sigma_2 = 1\\)</span>.

Given this information, find <span class="math-inline">\\(U\\)</span>, <span class="math-inline">\\(\Sigma\\)</span>, and <span class="math-inline">\\(V^T\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Let <span class="math-inline">\\(X = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 2 & -1 \\\\ 2 & 2 \end{bmatrix}\\)</span>.

1.  Compute the singular value decomposition (that is, find <span class="math-inline">\\(U\\)</span>, <span class="math-inline">\\(\Sigma\\)</span>, and <span class="math-inline">\\(V^T\\)</span>) for <span class="math-inline">\\(X\\)</span>. Do this by hand, but use `np.linalg.svd` in Python to verify your work.

2.  Now, compute the singular value decomposition for <span class="math-inline">\\(X^T = \begin{bmatrix} 1 & 0 & 2 & 2 \\\\ 0 & 1 & -1 & 2 \end{bmatrix}\\)</span>. How can you reuse your work in finding the SVD of <span class="math-inline">\\(X\\)</span> to compute the SVD of <span class="math-inline">\\(X^T\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Compute the singular value decomposition for the diagonal matrix <span class="math-inline">\\(X = \begin{bmatrix} 3 & 0 & 0 \\\\ 0 & -2 & 0 \\\\ 0 & 0 & -2 \end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Compute the singular value decomposition for the rank-one matrix <span class="math-inline">\\(X = \begin{bmatrix} 0 & 0 \\\\ 3 & 4 \\\\ 6 & 8 \end{bmatrix}\\)</span>.

<em>Hint: Can you write <span class="math-inline">\\(X\\)</span> as an outer product of two vectors? If you can, how do those vectors relate to the singular values and singular vectors of <span class="math-inline">\\(X\\)</span>?</em>

</div>
</div>

</div>
---

## Problem 3: Frobenius Norm and Low-Rank Approximation (22 pts)

As we first saw in Chapter 2.1, the norm of a vector is a measure of its size. The "default" norm is the Euclidean, or <span class="math-inline">\\(L_2\\)</span> norm, <span class="math-inline">\\(\lVert \vec v \rVert_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}\\)</span>.

Similarly, the norm of a matrix is a measure of its size. The most common matrix norm is the **Frobenius norm**, defined as 

<div class="math-display">
$$
\lVert X \rVert_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^d x_{ij}^2}
$$
</div>

 That is, <span class="math-inline">\\(\lVert X \rVert_F\\)</span> is the square root of the sum of the squares of the elements of <span class="math-inline">\\(X\\)</span>; it treats <span class="math-inline">\\(X\\)</span> as a vector and computes its <span class="math-inline">\\(L_2\\)</span> norm.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Verify that <span class="math-inline">\\(\lVert X \rVert_F = \sqrt{15}\\)</span> for <span class="math-inline">\\(X = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 2 & -1 \\\\ 2 & 2 \end{bmatrix}\\)</span>.

*Notice that <span class="math-inline">\\(\sqrt{15} = \sqrt{10 + 5}\\)</span>, and in Problem 2a), you found that <span class="math-inline">\\(X\\)</span>'s singular values were <span class="math-inline">\\(\sigma_1 = \sqrt{10}\\)</span> and <span class="math-inline">\\(\sigma_2 = \sqrt{5}\\)</span>. We build on this idea in part **c)**.*

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Another equivalent formula for the Frobenius norm is

<div class="math-display">
$$
\lVert X \rVert_F^2 = \text{trace}(X^T X)
$$
</div>

 where <span class="math-inline">\\(\text{trace}(X^T X)\\)</span> is the sum of the diagonal entries of <span class="math-inline">\\(X^TX\\)</span>. (Notice the square on the left-hand side!) **Explain why** this is equivalent to the first definition of the Frobenius norm.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Another equivalent formula for the Frobenius norm is

<div class="math-display">
$$
\lVert X \rVert_F^2 = \sum_{i=1}^r \sigma_i^2
$$
</div>

 where <span class="math-inline">\\(\sigma_1, \sigma_2, \ldots, \sigma_r\\)</span> are the singular values of <span class="math-inline">\\(X\\)</span> and <span class="math-inline">\\(r = \text{rank}(X)\\)</span>. **Explain why** this is equivalent to the definition of the Frobenius norm from part **b)**. *Hint: What is the relationship between the singular values of <span class="math-inline">\\(X\\)</span> and the eigenvalues of some other matrix?*

The Frobenius norm allows us to make more precise the idea of a rank-<span class="math-inline">\\(k\\)</span> approximation of a matrix, first introduced in [Chapter 10.2](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation/).

Suppose <span class="math-inline">\\(X = U \Sigma V^T\\)</span> is the singular value decomposition of the <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(X\\)</span>, where the columns of <span class="math-inline">\\(U\\)</span> are <span class="math-inline">\\(\vec u_1, \vec u_2, \ldots, \vec u_n \in \mathbb{R}^n\\)</span>, the singular values of <span class="math-inline">\\(X\\)</span> are <span class="math-inline">\\(\sigma_1, \sigma_2, \ldots, \sigma_r > 0\\)</span>, the rows of <span class="math-inline">\\(V^T\\)</span> are <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_d \in \mathbb{R}^d\\)</span>, and <span class="math-inline">\\(r = \text{rank}(X)\\)</span>.

The Eckart--Young--Mirsky theorem states that, for any integer <span class="math-inline">\\(k\\)</span> between 1 and <span class="math-inline">\\(r\\)</span>, the <span class="math-inline">\\(n \times d\\)</span> matrix

<div class="math-display">
$$
X_k = \sum_{i=1}^k \sigma_i \vec u_i \vec v_i^T
$$
</div>

 is the closest rank-<span class="math-inline">\\(k\\)</span> matrix to <span class="math-inline">\\(X\\)</span>, in terms of Frobenius norm. That is, if <span class="math-inline">\\(Y\\)</span> is any other <span class="math-inline">\\(n \times d\\)</span> matrix of rank <span class="math-inline">\\(k\\)</span>, then <span class="math-inline">\\(\lVert X - X_k \rVert_F \leq \lVert X - Y \rVert_F\\)</span>. More intuitively, this says that <span class="math-inline">\\(X_k\\)</span> is the matrix with the smallest mean squared error from <span class="math-inline">\\(X\\)</span>, among all <span class="math-inline">\\(n \times d\\)</span> matrices of rank <span class="math-inline">\\(k\\)</span>. We will not prove this theorem in class.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Let's illustrate the above with an example. Consider the <span class="math-inline">\\(3 \times 4\\)</span> matrix <span class="math-inline">\\(X\\)</span>, whose singular value decomposition is given by

<div class="math-display">
$$
\underbrace{\begin{bmatrix} 24 & 0 & 0 & 24 \\\\ 7 & 25 & 25 & 7 \\\\ 1 & -1 & 1 & -1 \end{bmatrix}}_{X} = \underbrace{\begin{bmatrix} 0.6 & 0.8 & 0 \\\\ 0.8 & -0.6 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}}_{U} \underbrace{\begin{bmatrix} 40 & 0 & 0 & 0 \\\\ 0 & 30 & 0 & 0 \\\\ 0 & 0 & 2 & 0 \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} 1/2 & 1/2 & 1/2 & 1/2 \\\\ 1/2 & -1/2 & -1/2 & 1/2 \\\\ 1/2 & -1/2 & 1/2 & -1/2 \\\\ -1/2 & -1/2 & 1/2 & 1/2 \end{bmatrix}}_{V^T}
$$
</div>

For <span class="math-inline">\\(k = 1, 2, 3\\)</span>, compute the rank-<span class="math-inline">\\(k\\)</span> approximation <span class="math-inline">\\(X_k = \sum_{i=1}^k \sigma_i \vec u_i \vec v_i^T\\)</span> and the Frobenius norm of the approximation error, <span class="math-inline">\\(\lVert X - X_k \rVert_F\\)</span>.

Feel free to do the computations by hand or using `numpy`. If you use `numpy`, make sure to include screenshots of any code you write and its outputs, and **don't** use `np.linalg.svd`; instead, enter the SVD we provided you with and use `np.outer` to compute the outer product of two vectors.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Open the **the supplemental Jupyter Notebook** we've created for Homework 11, which can either be found [here](https://github.com/eecs245/wn26-code/blob/main/homeworks/hw11/hw11.ipynb) in the course GitHub repository, or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fwn26-code&urlpath=tree%2Fwn26-code%2Fhomeworks%2Fhw11%2Fhw11.ipynb&branch=main) on DataHub.

There, you're asked to implement the rank-<span class="math-inline">\\(k\\)</span> approximation of an image of your choosing, similar to the [Image Compression example in Chapter 10.2](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation/#example-image-compression).

More instructions are provided in the notebook. This problem is **not autograded**. Rather, in your submission to this part, include screenshots of all of your code and outputs here.

</div>
</div>

</div>
---

## Problem 4: Principal Components Analysis (15 pts)

**Make sure you've completed Problem 3 before attempting this problem.**

This problem involves a practical exploration of principal components analysis (PCA), perhaps the most interesting application of the singular value decomposition.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open `homeworks/hw11/hw11.ipynb`. For instructions on how to do this, see the [Tech Support](https://eecs245.org/env-setup/#option-1-local-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fwn26-code&urlpath=tree%2Fwn26-code%2Fhomeworks%2Fhw11%2Fhw11.ipynb&branch=main) to open `hw11.ipynb` on DataHub. Before doing so, read the instructions on the [Tech Support](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

**This problem is NOT autograded**. Instead, complete the five tasks mentioned in Problem 4, and include screenshots of all of your code and outputs here, along with your written answers to Tasks 3 and 5.
