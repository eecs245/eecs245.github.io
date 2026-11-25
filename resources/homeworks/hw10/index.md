---
layout: page
title: "Homework 10: Diagonalization"
description: "Homework 10: Diagonalization problems."
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
.main-content img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.main-content p {
  margin-bottom: 1.15em;
}
.main-content .assignment-list > li {
  display: list-item;
}
.main-content .assignment-list > li::before {
  content: none;
}
.main-content ul.assignment-list {
  list-style-type: disc;
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
/* Answer-choice matrices should size to their labels, not theme column minima. */
.main-content table.answer-choice-table th,
.main-content table.answer-choice-table td {
  min-width: 0;
  padding: 0.35rem 0.4rem;
}
.crossnumber-grid {
  display: grid;
  grid-template-columns: repeat(3, 2.4rem);
  grid-template-rows: repeat(3, 2.4rem);
  margin: 1rem auto;
  width: max-content;
}
.crossnumber-cell {
  align-items: center;
  border: 1.5px solid currentColor;
  display: flex;
  font-size: 1.1rem;
  justify-content: center;
  position: relative;
}
.crossnumber-label {
  font-size: 0.55rem;
  left: 0.15rem;
  line-height: 1;
  position: absolute;
  top: 0.15rem;
}
.crossnumber-missing {
  border: 0;
}
</style>

# Homework 10: Diagonalization

**due** Sunday, December 6th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw10/hw10.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Other than the video link for Problem 1 and the notebook for Problem 8, write your solutions by hand, on paper or on a tablet, and submit them as one PDF. Include your Problem 7f screenshot in that PDF. Submit your Problem 1 video link and your Problem 8 notebook separately on Pensive. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 9 Concept Video](#problem-1-homework-9-concept-video-8-pts)
- [Problem 2: Rank One Projection Matrices](#problem-2-rank-one-projection-matrices-8-pts)
- [Problem 3: Recovering Eigenvector Components](#problem-3-recovering-eigenvector-components-8-pts)
- [Problem 4: Algebraic and Geometric Multiplicities](#problem-4-algebraic-and-geometric-multiplicities-15-pts)
- [Problem 5: Diagonalization](#problem-5-diagonalization-12-pts)
- [Problem 6: Adjacency Matrices](#problem-6-adjacency-matrices-15-pts)
- [Problem 7: Regularization](#problem-7-regularization-22-pts)
- [Problem 8: PageRank](#problem-8-pagerank-12-pts)

---

Total Points: <span class="math-inline">\\(8 + 8 + 8 + 15 + 12 + 15 + 22 + 12 = 100\\)</span>

---

## Problem 1: Homework 9 Concept Video (8 pts)

Record a **2- to 5-minute video** answering **one** of the prompts below. These prompts are related to the ideas in [Homework 9](https://eecs245.org/resources/homeworks/hw09/).

<ol class="assignment-list" markdown="1" data-item-count="3" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

You fit two polynomial regression models to the same training data, one of degree 2 and one of degree 20. Explain why the higher-degree model can have lower training mean squared error and higher test mean squared error at the same time.

</li>
<li markdown="1" value="2">

Suppose you one-hot encode a categorical feature and fit a linear regression model with an intercept. What happens to the design matrix if you keep every one-hot-encoded column? Explain why dropping one of those columns can fix that dependence without changing the predictions the model can represent.

</li>
<li markdown="1" value="3">

Suppose a real matrix has an eigenvector with eigenvalue <span class="math-inline">\\(-2\\)</span>. Explain what multiplying by the matrix does to that vector and to any nonzero scalar multiple of it. What happens to the original eigenvector when you multiply by the matrix twice?

</li>
</ol>

The video should be **just you speaking into the camera**. Your face must be visible while you are talking for the entire video. Do not include slides, a screen recording, written work, or any other visuals.

Submit your video link to the separate assignment on Pensive called **Homework 10, Problem 1 Video Link**. You can upload your video to YouTube as unlisted, share a Zoom recording link, or share a Google Drive link; whatever works. Make sure the course staff can view the video using that link.

Your submission time for Homework 10 is the latest of your three submission times: your Problem 1 video link, your PDF, and your Problem 8 notebook.

**This problem is graded on completion.** Record a video of the required length and make an honest effort to explain the question, and you will receive full credit. Your explanation does not need to be polished or perfect.

---

{: .yellow }
> **Note**: Repeatedly, you'll be asked to find eigenvalues and eigenvectors. As usual, you're expected to show all of your work. But, you're encouraged to verify your answers by using `np.linalg.eig` in Python, as is demonstrated in [Chapter 9.1](https://notes.eecs245.org/eigenvalues-and-eigenvectors/eigenvalues-eigenvectors/#finding-eigenvalues-using-numpy). (Resist the urge to use ChatGPT\...)

---

## Problem 2: Rank One Projection Matrices (8 pts)

Consider the unit vector <span class="math-inline">\\(\vec u = \begin{bmatrix} 1/6 \\\\ 1/6 \\\\ 3/6 \\\\ 5/6 \end{bmatrix}\\)</span>, and the corresponding rank one projection matrix <span class="math-inline">\\(P = \vec u \vec u^T\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Show that <span class="math-inline">\\(\vec u\\)</span> is an eigenvector of <span class="math-inline">\\(P\\)</span>. What is its corresponding eigenvalue?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Show that if <span class="math-inline">\\(\vec v\\)</span> is orthogonal to <span class="math-inline">\\(\vec u\\)</span>, then <span class="math-inline">\\(\vec v\\)</span> is an eigenvector of <span class="math-inline">\\(P\\)</span>. What is its corresponding eigenvalue?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find three different **linearly independent** eigenvectors of <span class="math-inline">\\(P\\)</span>, all corresponding to the eigenvalue 0.

These three eigenvectors form a basis of the **eigenspace** of <span class="math-inline">\\(P\\)</span> corresponding to eigenvalue 0.

</div>
</div>

</div>

---

## Problem 3: Recovering Eigenvector Components (8 pts)

Suppose <span class="math-inline">\\(S\\)</span> is a <span class="math-inline">\\(2 \times 2\\)</span> **symmetric** matrix whose eigenvalues are <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(3\\)</span>. You are given a vector <span class="math-inline">\\(\vec x\\)</span> and the result of multiplying it by <span class="math-inline">\\(S\\)</span>:

<div class="math-display">
$$
\vec x=\begin{bmatrix}2\\\\4\end{bmatrix}
\qquad
S\vec x=\begin{bmatrix}6\\\\4\end{bmatrix}
$$
</div>

 Write <span class="math-inline">\\(\vec x=\vec v_1+\vec v_2\\)</span>, where <span class="math-inline">\\(\vec v_1\\)</span> is an eigenvector corresponding to <span class="math-inline">\\(\lambda=1\\)</span> and <span class="math-inline">\\(\vec v_2\\)</span> is an eigenvector corresponding to <span class="math-inline">\\(\lambda=3\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Express <span class="math-inline">\\(S\vec x\\)</span> as a linear combination of <span class="math-inline">\\(\vec v_1\\)</span> and <span class="math-inline">\\(\vec v_2\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Use the two given vectors to find <span class="math-inline">\\(\vec v_1\\)</span> and <span class="math-inline">\\(\vec v_2\\)</span>. Verify that <span class="math-inline">\\(\vec v_1\\)</span> and <span class="math-inline">\\(\vec v_2\\)</span> are orthogonal, as the Spectral Theorem in [Chapter 9.5](https://notes.eecs245.org/eigenvalues-and-eigenvectors/symmetric-matrices-spectral-theorem/) guarantees.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(S^4\vec x\\)</span> using your vectors from part b).
</div>
</div>

</div>

{% endraw %}


---

## Problem 4: Algebraic and Geometric Multiplicities (15 pts)

For each matrix below:

<ol class="assignment-list" markdown="1" data-item-count="3" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Find its characteristic polynomial in factored form.

</li>
<li markdown="1" value="2">

State all eigenvalues along with their algebraic multiplicities.

</li>
<li markdown="1" value="3">

For each eigenvalue, find a basis for the eigenspace corresponding to that eigenvalue, and state its geometric multiplicity.

</li>
</ol>

Some advice:

<ul class="assignment-list" markdown="1" data-item-count="3">
<li markdown="1">

There are multiple examples of what you're asked to do in [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/#algebraic-and-geometric-multiplicity).

</li>
<li markdown="1">

Recall the trace and determinant tricks from [Chapter 9.2](https://notes.eecs245.org/eigenvalues-and-eigenvectors/characteristic-polynomial/#trace-and-determinant), and the fact that the determinant of an upper triangular matrix is the product of the diagonal entries.

</li>
<li markdown="1">

Work efficiently: this problem is quicker than it seems.

</li>
</ul>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 0 &amp; 0 \\\\ 0 &amp; 4 &amp; 0 \\\\ 0 &amp; 0 &amp; 4 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 1 \\\\ 0 &amp; 3 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 0 &amp; 1 \\\\ 0 &amp; 2 &amp; 1 \\\\ 0 &amp; 0 &amp; 3 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 5 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 3 &amp; 1 &amp; 0 \\\\ 0 &amp; 0 &amp; 3 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 5 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 1 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>

</div>
</div>

</div>

---

## Problem 5: Diagonalization (12 pts)

Before proceeding, it's wise to read [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) In each statement, fill in the blanks and provide a brief justification. Each answer is more than just one word or number.

<ol class="assignment-list" markdown="1" data-item-count="2" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

<span class="math-inline">\\(A\\)</span> is diagonalizable if and only if it has \_\_\_\_ eigenvectors.

</li>
<li markdown="1" value="2">

<span class="math-inline">\\(A\\)</span> is diagonalizable if and only if the geometric multiplicity of each eigenvalue is \_\_\_\_.

</li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(9 pts) For each matrix <span class="math-inline">\\(A\\)</span> in **Problem 4**:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

**if** it is diagonalizable, find matrices <span class="math-inline">\\(V\\)</span> and <span class="math-inline">\\(\Lambda\\)</span> such that <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>. (As we saw in [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/), this matrix is constructed by placing the eigenvectors of <span class="math-inline">\\(A\\)</span> as the columns of <span class="math-inline">\\(V\\)</span> and the eigenvalues of <span class="math-inline">\\(A\\)</span> as the diagonal entries of <span class="math-inline">\\(\Lambda\\)</span>. **You should have already done most of the work for this**; this problem is just a matter of organizing your work.)

</li>
<li markdown="1">

**if not**, explain why it is not diagonalizable.

</li>
</ul>

</div>
</div>

</div>

---

## Problem 6: Adjacency Matrices (15 pts)

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
(3 pts) Diagonalize <span class="math-inline">\\(A\\)</span> by finding matrices <span class="math-inline">\\(V\\)</span> and <span class="math-inline">\\(\Lambda\\)</span> such that <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>. Do this by hand, but then include a screenshot of `numpy` code that verifies that you found the correct <span class="math-inline">\\(V\\)</span> and <span class="math-inline">\\(\Lambda\\)</span>.

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

## Problem 7: Regularization (22 pts)

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
(5 pts) Find <span class="math-inline">\\(\nabla R&#95;\text{ridge}(\vec w)\\)</span>, the gradient of <span class="math-inline">\\(R&#95;\text{ridge}(\vec w)\\)</span>.

<em>Hint: Most of the steps involved were done in <a href="https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#minimizing-mean-squared-error">Chapter 8.2</a>, but you'll need to redo the work yourself and extend it slightly.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(\vec w&#95;\text{ridge}^{\ast}\\)</span>, the vector that minimizes <span class="math-inline">\\(R&#95;\text{ridge}(\vec w)\\)</span>.

<em>Hint: Your answer should be such that if <span class="math-inline">\\(\lambda = 0\\)</span> and <span class="math-inline">\\(X\\)</span> has full column rank, then <span class="math-inline">\\(\vec w&#95;\text{ridge}^{\ast}\\)</span> is the same as the vector <span class="math-inline">\\(\vec w^{\ast}\\)</span> that minimizes mean squared error without the added <span class="math-inline">\\(+ \lambda \lVert \vec w \rVert^2\\)</span> term.</em>

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
(4 pts) Now, let's explore how adding the regularization term <span class="math-inline">\\(\lambda \lVert \vec w \rVert^2\\)</span> to the objective function affects the shape of the loss surface.

Open the **supplemental Jupyter Notebook** we've created for Homework 10, which can either be found [here](https://github.com/eecs245/fa26-code/blob/main/homeworks/hw10/hw10.ipynb) in the course GitHub repository or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw10%2Fhw10.ipynb&branch=main) on DataHub.

This problem is **not** autograded. Instead,

<ol class="assignment-list" markdown="1" data-item-count="3" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Read through the entire walkthrough, all the way through the end of Problem 7f).

</li>
<li markdown="1" value="2">

In this PDF, include a **screenshot of the diagram with a slider**, showing that you've moved it **all the way to the right, at <span class="math-inline">\\(\lambda = 100000\\)</span>.**

</li>
<li markdown="1" value="3">

In this PDF, include answers to both of the following questions:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

Why is it called ridge regression?

</li>
<li markdown="1">

How does the inclusion of the <span class="math-inline">\\(\lambda \lVert \vec w \rVert^2\\)</span> term change the **convexity** of the loss surface?

</li>
</ul>
</li>
</ol>

If you'd like to read more about regularization, and **how we actually choose the value of <span class="math-inline">\\(\lambda\\)</span> in practice**, read more from [EECS 398 here](https://practicaldsc.org/resources/lectures/lec19/lec19-filled.html).

</div>
</div>

</div>

---

## Problem 8: PageRank (12 pts)

This problem involves writing code and submitting it to the Pensive autograder. The goal of this problem is to allow you to implement Google's PageRank algorithm in code and think through some of its pitfalls and variants.

There are two ways to access the supplemental Jupyter Notebook:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

**Option 1**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open [`homeworks/hw10/hw10.ipynb`](https://github.com/eecs245/fa26-code/blob/main/homeworks/hw10/hw10.ipynb). For instructions on how to do this, see the [Tech Support](https://eecs245.org/env-setup/#option-1-local-setup) page of the course website.

</li>
<li markdown="1">

**Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw10%2Fhw10.ipynb&branch=main) to open `hw10.ipynb` on DataHub. Before doing so, read the instructions on the [Tech Support](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

</li>
</ul>

{: .yellow }
> This problem is entirely autograded. Submit your completed notebook to **Homework 10, Problem 8 Code** on Pensive.
