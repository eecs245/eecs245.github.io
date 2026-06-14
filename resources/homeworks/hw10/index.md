---
layout: page
title: "Homework 10: Eigenvalues and Eigenvectors"
description: "Homework 10: Eigenvalues and Eigenvectors problems."
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

# Homework 10: Eigenvalues and Eigenvectors

**due** Thursday, June 18th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw10/hw10.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 9 Solutions Review](#problem-1-homework-9-solutions-review-10-pts)
- [Problem 2: Rank One Projection Matrices](#problem-2-rank-one-projection-matrices-10-pts)
- [Problem 3: Algebraic and Geometric Multiplicities](#problem-3-algebraic-and-geometric-multiplicities-20-pts)
- [Problem 4: Diagonalization](#problem-4-diagonalization-14-pts)
- [Problem 5: Adjacency Matrices](#problem-5-adjacency-matrices-16-pts)
- [Problem 6: Regularization](#problem-6-regularization-24-pts)
- [Problem 7: PageRank](#problem-7-pagerank-12-pts)

---

Total Points: 10 + 10 + 20 + 14 + 16 + 24 + 12 = 106

---

**Note**: Repeatedly, you'll be asked to find eigenvalues and eigenvectors. As usual, you're expected to show all of your work. But, you're encouraged to verify your answers by using `np.linalg.eig` in Python, as is demonstrated in [Chapter 9.1](https://notes.eecs245.org/eigenvalues-and-eigenvectors/eigenvalues-eigenvectors/#finding-eigenvalues-using-numpy). (Resist the urge to use ChatGPT\...)

---

## Problem 1: Homework 9 Solutions Review (10 pts)

Review [the solutions to Homework 9](https://eecs245.org/resources/homeworks/hw09/). Pick **two problem parts** (for example, Problem 2a and Problem 5c) from Homework 9 in which your solutions have the most room for improvement, i.e. where they have unsound reasoning, could be significantly more efficient or clearer, etc. Include a screenshot of your solution to each problem part, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 9, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Rank One Projection Matrices (10 pts)

Consider the unit vector <span class="math-inline">\\(\vec u = \begin{bmatrix} 1/6 \\\\ 1/6 \\\\ 3/6 \\\\ 5/6 \end{bmatrix}\\)</span>, and the corresponding rank one projection matrix <span class="math-inline">\\(P = \vec u \vec u^T\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Show that <span class="math-inline">\\(\vec u\\)</span> is an eigenvector of <span class="math-inline">\\(P\\)</span>. What is its corresponding eigenvalue?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Show that if <span class="math-inline">\\(\vec v\\)</span> is orthogonal to <span class="math-inline">\\(\vec u\\)</span>, then <span class="math-inline">\\(\vec v\\)</span> is an eigenvector of <span class="math-inline">\\(P\\)</span>. What is its corresponding eigenvalue?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find three different **linearly independent** eigenvectors of <span class="math-inline">\\(P\\)</span>, all corresponding to the eigenvalue 0.

(In the terminology of Problem 4 and Chapter 5.2, these eigenvectors form a basis of the eigenspace of <span class="math-inline">\\(P\\)</span> corresponding to eigenvalue 0.)

</div>
</div>

</div>

---

## Problem 3: Algebraic and Geometric Multiplicities (20 pts)

For each matrix below:

1.  Find its characteristic polynomial in factored form.

2.  State all eigenvalues along with their algebraic multiplicities.

3.  For each eigenvalue, find a basis for the eigenspace corresponding to that eigenvalue, and state its geometric multiplicity.

Some advice:

-   There are multiple examples of what you're asked to do in [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/#algebraic-and-geometric-multiplicity).

-   Recall the trace and determinant tricks from [Chapter 9.2](https://notes.eecs245.org/eigenvalues-and-eigenvectors/characteristic-polynomial/#trace-and-determinant), and the fact that the determinant of an upper triangular matrix is the product of the diagonal entries.

-   Work efficiently: this problem is quicker than it seems.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 0 &amp; 0 \\\\ 0 &amp; 4 &amp; 0 \\\\ 0 &amp; 0 &amp; 4 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 1 \\\\ 0 &amp; 3 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 0 &amp; 1 \\\\ 0 &amp; 2 &amp; 1 \\\\ 0 &amp; 0 &amp; 3 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 5 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 3 &amp; 1 &amp; 0 \\\\ 0 &amp; 0 &amp; 3 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 5 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 1 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>

</div>
</div>

</div>

---

## Problem 4: Diagonalization (14 pts)

Before proceeding, it's wise to read [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) In each statement, fill in the blanks and provide a brief justification. Each answer is more than just one word or number.

1.  <span class="math-inline">\\(A\\)</span> is diagonalizable if and only if it has \_\_\_\_ eigenvectors.

2.  <span class="math-inline">\\(A\\)</span> is diagonalizable if and only if the geometric multiplicity of each eigenvalue is \_\_\_\_.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(10 pts) For each matrix <span class="math-inline">\\(A\\)</span> in **Problem 3**:

-   **if** it is diagonalizable, find matrices <span class="math-inline">\\(V\\)</span> and <span class="math-inline">\\(\Lambda\\)</span> such that <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>. (As we saw in [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/), this matrix is constructed by placing the eigenvectors of <span class="math-inline">\\(A\\)</span> as the columns of <span class="math-inline">\\(V\\)</span> and the eigenvalues of <span class="math-inline">\\(A\\)</span> as the diagonal entries of <span class="math-inline">\\(\Lambda\\)</span>. **You should have already done most of the work for this**; this problem is just a matter of organizing your work.)

-   **if not**, explain why it is not diagonalizable.

</div>
</div>

</div>

---

## Problem 5: Adjacency Matrices (16 pts)

Consider the matrix

<div class="math-display">
$$
A = \begin{bmatrix} 0.6 & 0.2 & 0.4 \\\\ 0.3 & 0.7 & 0.2 \\\\ 0.1 & 0.1 & 0.4 \end{bmatrix}
$$
</div>

 <span class="math-inline">\\(A\\)</span> represents the adjacency matrix of a Markov chain with three states; see [Chapter 9.3](https://notes.eecs245.org/eigenvalues-and-eigenvectors/markov-chains-adjacency-matrices/) for details.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Draw the corresponding state diagram for <span class="math-inline">\\(A\\)</span>. Label the states 1, 2, and 3.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Diagonalize <span class="math-inline">\\(A\\)</span> by finding matrices <span class="math-inline">\\(V\\)</span> and <span class="math-inline">\\(\Lambda\\)</span> such that <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>. Do this by hand, but then include a screenshot of `numpy` code that verifies that you found the correct <span class="math-inline">\\(V\\)</span> and <span class="math-inline">\\(\Lambda\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Compute <span class="math-inline">\\(A^{10}\\)</span> using the diagonalization you found in part **b)**. <em>Hint: You should <strong>not</strong> have to multiply ten matrices by hand: only three. State what the three matrices are, and then you can use `numpy` to actually multiply them. Include a screenshot of any code you write and its output.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(\vec x&#95;0 = \begin{bmatrix} 0.6 \\\\ 0.3 \\\\ 0.1 \end{bmatrix}\\)</span> be an initial state vector. Using `numpy`, compute <span class="math-inline">\\(A^{10} \vec x&#95;0\\)</span>. Include a screenshot of any code you write and its output.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) As <span class="math-inline">\\(k \to \infty\\)</span>, what does <span class="math-inline">\\(A^k \vec x&#95;0\\)</span> converge to, and why? Make sure your answer references the diagonalization you found in part **b)**.

</div>
</div>

</div>

---

## Problem 6: Regularization (24 pts)

Suppose we'd like to perform multiple linear regression using the <span class="math-inline">\\(n \times (d+1)\\)</span> design matrix <span class="math-inline">\\(X\\)</span>, observation vector <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span>, and parameter vector <span class="math-inline">\\(\vec w \in \mathbb{R}^{d+1}\\)</span>.

Instead of minimizing mean squared error to find <span class="math-inline">\\(\vec w^{\ast}\\)</span>, suppose we'd like to minimize the following **regularized objective function**:

<div class="math-display">
$$
R_\text{ridge}(\vec w) = \lVert \vec y - X \vec w \rVert^2 + \lambda \lVert \vec w \rVert^2
$$
</div>

where <span class="math-inline">\\(\lambda \geq 0\\)</span> is a constant. The <span class="math-inline">\\(+ \lambda \lVert \vec w \rVert^2\\)</span> term is called the **regularization term**.

The vector <span class="math-inline">\\(\vec w&#95;\text{ridge}^{\ast}\\)</span> that minimizes <span class="math-inline">\\(R&#95;\text{ridge}(\vec w)\\)</span> will be, in general, different than the vector <span class="math-inline">\\(\vec w^{\ast}\\)</span> that minimizes mean squared error without the added <span class="math-inline">\\(+ \lambda \lVert \vec w \rVert^2\\)</span> term, and will thus have a higher mean squared error on the training data.

But, it turns out that <span class="math-inline">\\(\vec w&#95;\text{ridge}^{\ast}\\)</span> **may** make better predictions on unseen test data, if we choose <span class="math-inline">\\(\lambda\\)</span> carefully, by forcing the model to be simpler and less overfit to the training data. Let's explore this idea in more depth.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Find <span class="math-inline">\\(\nabla R&#95;\text{ridge}(\vec w)\\)</span>, the gradient of <span class="math-inline">\\(R&#95;\text{ridge}(\vec w)\\)</span>.

<em>Hint: Most of the steps involved were done in <a href="https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#minimizing-mean-squared-error">Chapter 8.2</a>, but you'll need to redo the work yourself and extend it slightly.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(\vec w&#95;\text{ridge}^{\ast}\\)</span>, the vector that minimizes <span class="math-inline">\\(R&#95;\text{ridge}(\vec w)\\)</span>.

<em>Hint: Your answer should be such that if <span class="math-inline">\\(\lambda = 0\\)</span>, then <span class="math-inline">\\(\vec w&#95;\text{ridge}^{\ast}\\)</span> is the same as the vector <span class="math-inline">\\(\vec w^{\ast}\\)</span> that minimizes mean squared error without the added <span class="math-inline">\\(+ \lambda \lVert \vec w \rVert^2\\)</span> term.</em>

One of the side benefits of adding this regularization term is that a unique solution for <span class="math-inline">\\(\vec w&#95;\text{ridge}^{\ast}\\)</span> exists for all <span class="math-inline">\\(\lambda &gt; 0\\)</span>, **even if <span class="math-inline">\\(X\\)</span> is not full rank**. That's a bold claim: let's prove it.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Prove that all of the eigenvalues of <span class="math-inline">\\(X^TX\\)</span> are non-negative. (This means that <span class="math-inline">\\(X^TX\\)</span> is **positive semidefinite**.)

<em>Hint: Suppose <span class="math-inline">\\(\vec v&#95;i\\)</span> is an eigenvector of <span class="math-inline">\\(X^TX\\)</span> with eigenvalue <span class="math-inline">\\(\lambda&#95;i\\)</span>. From there, if you get stuck, take a look at <a href="https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-rank-of-x-tx">this seemingly unrelated proof from Chapter 5.4</a> for inspiration.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Suppose <span class="math-inline">\\(\vec v&#95;i\\)</span> is an eigenvector of <span class="math-inline">\\(X^TX\\)</span> with eigenvalue <span class="math-inline">\\(\lambda&#95;i\\)</span>. Show that <span class="math-inline">\\(\vec v&#95;i\\)</span> is also an eigenvector of <span class="math-inline">\\(X^TX + \lambda I\\)</span>. What is its corresponding eigenvalue?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Putting parts **c)** and **d)** together, why is it guaranteed that <span class="math-inline">\\(X^TX+ \lambda I\\)</span> is invertible for all <span class="math-inline">\\(\lambda &gt; 0\\)</span>, even if <span class="math-inline">\\(X\\)</span> is not full rank? (<span class="math-inline">\\(X^TX + \lambda I\\)</span> is said to be **positive definite** for all <span class="math-inline">\\(\lambda &gt; 0\\)</span>.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Now, let's explore how adding the regularization term <span class="math-inline">\\(\lambda \lVert \vec w \rVert^2\\)</span> to the objective function affects the shape of the loss surface.

Open the **the supplemental Jupyter Notebook** we've created for Homework 10, which can either be found [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw10/hw10.ipynb) in the course GitHub repository or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw10%2Fhw10.ipynb&branch=main) on DataHub.

This problem is **not** autograded. Instead,

1.  Read through the entire walkthrough, all the way through the end of Problem 6f).

2.  In this PDF, include a **screenshot of the diagram with a slider**, showing that you've moved it **all the way to the right, at <span class="math-inline">\\(\lambda = 100000\\)</span>.**

3.  In this PDF, include answers to both of the following questions:

-   Why is it called ridge regression?

-   How does the inclusion of the <span class="math-inline">\\(\lambda \lVert \vec w \rVert^2\\)</span> term change the **convexity** of the loss surface?

If you'd like to read more about regularization, and **how we actually choose the value of <span class="math-inline">\\(\lambda\\)</span> in practice**, read more from [EECS 398 here](https://practicaldsc.org/resources/lectures/lec19/lec19-filled.html).

</div>
</div>

</div>

---

## Problem 7: PageRank (12 pts)

This problem involves writing code and submitting it to the Gradescope autograder. The goal of this problem is to allow you to implement Google's PageRank algorithm in code and think through some of its pitfalls and variants.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open `homeworks/hw10/hw10.ipynb`. For instructions on how to do this, see the [Tech Support](https://eecs245.org/env-setup/#option-1-local-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw10%2Fhw10.ipynb&branch=main) to open `hw10.ipynb` on DataHub. Before doing so, read the instructions on the [Tech Support](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

**This problem is entirely autograded; to receive credit for Problem 7 of this homework, you'll need to submit your completed notebook to the autograder on Gradescope.** Your submission time for Homework 10 is the **latter** of your PDF and code submission times.

{% endraw %}
