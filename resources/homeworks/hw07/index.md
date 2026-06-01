---
layout: page
title: "Homework 7: Linear Transformations and Projections"
description: "Homework 7: Linear Transformations and Projections problems."
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

# Homework 7: Linear Transformations and Projections

**due** Thursday, June 4th, 2026 at 11:59PM Ann Arbor Time

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 6 Solutions Review](#problem-1-homework-6-solutions-review-10-pts)
- [Problem 2: Projecting onto the Column Space](#problem-2-projecting-onto-the-column-space-35-pts)
- [Problem 3: Moving Things Around](#problem-3-moving-things-around-10-pts)
- [Problem 4: The Sum of Errors](#problem-4-the-sum-of-errors-8-pts)

---

Total Points: 10 + 35 + 10 + 8 = 63

---

## Problem 1: Homework 6 Solutions Review (10 pts)

Review the solutions to Homework 6. Pick **two problem parts** (for example, Problem 2a and Problem 5b) from Homework 6 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 6, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Projecting onto the Column Space (35 pts)

The big idea in [Chapter 6.3](https://notes.eecs245.org/linear-transformations-and-projections/projecting-onto-column-space/), which we will also revisit in Chapter 7.1, is that of projecting a vector <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> onto the column space of an <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(X\\)</span>. That is, unlike in previous homeworks, we **don't** assume <span class="math-inline">\\(\vec y\\)</span> is a linear combination of <span class="math-inline">\\(X\\)</span>'s columns, and instead aim to find the vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span> that is closest to <span class="math-inline">\\(\vec y\\)</span>.

As we will show in [Chapter 6.3](https://notes.eecs245.org/linear-transformations-and-projections/projecting-onto-column-space/), if <span class="math-inline">\\(X\\)</span>'s columns are the vectors <span class="math-inline">\\(\vec x^{(1)}, \vec x^{(2)}, \ldots, \vec x^{(d)}\\)</span>, then the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is the vector

<div class="math-display">
$$
\vec p = X\vec w^* = w_1^* \vec x^{(1)} + w_2^* \vec x^{(2)} + \cdots + w_d^* \vec x^{(d)}, \quad \text{where} \quad \underbrace{\vec w^* = (X^TX)^{-1}X^T\vec y}_{\text{if X^TX is invertible}}
$$
</div>

The vector <span class="math-inline">\\(\vec w^*\\)</span> minimizes the norm of the error vector, <span class="math-inline">\\(\vec e = \vec y - \vec p\\)</span>, and as we will see in coming problems and homeworks, it contains **optimal model parameters** for linear regression, when we fill our <span class="math-inline">\\(X\\)</span> (carefully) with our input variables and <span class="math-inline">\\(\vec y\\)</span> with our output variables.

Taking another look at the formula <span class="math-inline">\\(\vec p = X \vec w^*\\)</span>, we see that it's equivalent to

<div class="math-display">
$$
\vec p = X \vec w^* = X (X^TX)^{-1}X^T\vec y = P\vec y
$$
</div>

where <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span> is called the **projection matrix**. Multiplying <span class="math-inline">\\(P \vec y\\)</span> is equivalent to projecting <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. In this problem, you'll explore properties of <span class="math-inline">\\(P\\)</span> and <span class="math-inline">\\(\vec w^*\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) In this part only, suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times 1\\)</span> matrix, i.e. it is a vector. Then,

1.  What is the value of <span class="math-inline">\\(\vec w^*\\)</span>, and how does it relate to what we learned in [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-projections)?

2.  What is the value of the matrix <span class="math-inline">\\(P\\)</span>, and how does it relate to what we learned in [Homework 6, Problem 5](https://eecs245.org/resources/homeworks/hw06/)?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Show that <span class="math-inline">\\(P\\)</span> is both symmetric (meaning that <span class="math-inline">\\(P^T = P\\)</span>) and idempotent (meaning that <span class="math-inline">\\(P^2 = P\\)</span>). Then, explain in English how <span class="math-inline">\\(P\\)</span>'s idempotence relates to the linear transformation of projecting <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Recall that <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix (meaning it's not necessarily square), which makes <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span> an <span class="math-inline">\\(n \times n\\)</span> matrix.

Fill in the blanks: <span class="math-inline">\\(X^TX\\)</span> is invertible if and only if <span class="math-inline">\\(X\\)</span>'s columns are \_\_\_\_.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In the rare case that <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> square matrix, and <span class="math-inline">\\(\text{rank}(X) = n\\)</span>, what is <span class="math-inline">\\(P\\)</span>? What does this say about the relationship between <span class="math-inline">\\(\vec y\\)</span>, <span class="math-inline">\\(\vec p\\)</span>, and <span class="math-inline">\\(\text{colsp}(X)\\)</span>?

<em>Hint: Use the fact that <span class="math-inline">\\((AB)^{-1} = B^{-1}A^{-1}\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) In **(i)** and **(ii)**, find <span class="math-inline">\\(\vec w^*\\)</span>, <span class="math-inline">\\(\vec p\\)</span>, and <span class="math-inline">\\(\vec e = \vec y - \vec p\\)</span>, and verify that <span class="math-inline">\\(\vec e\\)</span> is orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span> by showing that it is orthogonal to each of <span class="math-inline">\\(X\\)</span>'s columns.

1.  <span class="math-inline">\\(X = \begin{bmatrix} 2 &amp; 1 \\\\ 0 &amp; -3 \\\\ 0 &amp; 0 \end{bmatrix}, \quad \vec y = \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>

2.  <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; 1 \\\\ 1 &amp; -1 \\\\ 1 &amp; 0 \end{bmatrix}, \quad \vec y = \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>

3.  In **only one** of the subparts above, it is true that the sum of the components of <span class="math-inline">\\(\vec e\\)</span> is 0. Which one, and why? This is a **hugely** important result, and one that will 100% appear on Midterm 2. <em>Hint: The answer is not that <span class="math-inline">\\(\vec y\\)</span> is in <span class="math-inline">\\(\text{colsp}(X)\\)</span>; in both parts, it is <strong>not</strong>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) What linear combination of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 2 \\\\ -1 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ -3 \end{bmatrix}\\)</span> is closest to <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 1 \\\\ 2 \\\\ 4 \end{bmatrix}\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">g)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find the point on the plane <span class="math-inline">\\(x - y - 2z = 0\\)</span> that is closest to the point <span class="math-inline">\\((5, 0, 3)\\)</span>.

<em>Hint: Start by thinking of this as a projection problem. What are <span class="math-inline">\\(X\\)</span> and <span class="math-inline">\\(\vec y\\)</span>?</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">h)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Consider the matrix

<div class="math-display">
$$
A = \begin{bmatrix} 3 & 6 & 6 \\\\ 4 & 8 & 8 \end{bmatrix}
$$
</div>

1.  How many vectors <span class="math-inline">\\(\vec w\\)</span> are there that minimize <span class="math-inline">\\(\lVert \vec y - A \vec w \rVert^2\\)</span>? 0, 1, finitely many, or infinitely many?

2.  Find the matrix <span class="math-inline">\\(P&#95;c\\)</span> that projects vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> onto the column space of <span class="math-inline">\\(A\\)</span>. <em>Hint: The formula for <span class="math-inline">\\(P\\)</span> will fail here, since <span class="math-inline">\\(A^TA\\)</span> will not be invertible. Start by explaining why <span class="math-inline">\\(A^TA\\)</span> is not invertible. Then, look at Homework 5 for inspiration.</em>

3.  Find the matrix <span class="math-inline">\\(P&#95;r\\)</span> that projects vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> onto the row space of <span class="math-inline">\\(A\\)</span>.

4.  Find the product <span class="math-inline">\\(P&#95;c A P&#95;r\\)</span> and explain the result.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">i)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose that <span class="math-inline">\\(Q\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix whose columns are orthonormal, meaning that its columns are orthogonal to each other and have length 1. Note that we are not assuming that <span class="math-inline">\\(Q\\)</span>'s rows are orthonormal too, meaning that <span class="math-inline">\\(Q\\)</span> is not necessarily an orthogonal matrix using the definition from Homework 5 or Chapter 6.1.

The fact that <span class="math-inline">\\(Q\\)</span>'s columns are orthonormal greatly simplifies the formulas involved in projecting <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(Q)\\)</span>.

1.  What is the value of <span class="math-inline">\\(\vec w^*\\)</span>?

2.  What is the value of <span class="math-inline">\\(\vec p\\)</span>?

3.  If <span class="math-inline">\\(Q\\)</span>'s rows were orthonormal too, how would the answers to **(i)** and **(ii)** simply further, and why?

</div>
</div>

</div>

---

## Problem 3: Moving Things Around (10 pts)

Let <span class="math-inline">\\(X\\)</span> be an <span class="math-inline">\\(n \times 4\\)</span> design matrix whose first column is all 1s, let <span class="math-inline">\\(\vec y\\)</span> be an observation vector, and let <span class="math-inline">\\(\vec w^* = (X^TX)^{-1}X^T \vec y\\)</span>, where <span class="math-inline">\\(\vec w^* = \begin{bmatrix} w&#95;0^* \\\\ w&#95;1^* \\\\ w&#95;2^* \\\\ w&#95;3^* \end{bmatrix}\\)</span>.

In this problem, you'll reason about modifications to the design matrix and see how they affect the components of <span class="math-inline">\\(\vec w^*\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(X&#95;a\\)</span> be the design matrix that results from **swapping the first two columns of <span class="math-inline">\\(X\\)</span>**. Let

<span class="math-inline">\\(\vec v^* = (X&#95;a^TX&#95;a)^{-1}X&#95;a^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^*\\)</span> in terms of <span class="math-inline">\\(w&#95;0^*, w&#95;1^*, w&#95;2^*, w&#95;3^*\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(X&#95;b\\)</span> be the design matrix that results from **adding 3 to each entry in the *first* column of <span class="math-inline">\\(X\\)</span>**. Let <span class="math-inline">\\(\vec v^* = (X&#95;b^TX&#95;b)^{-1}X&#95;b^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^*\\)</span> in terms of <span class="math-inline">\\(w&#95;0^*, w&#95;1^*, w&#95;2^*, w&#95;3^*\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(X&#95;c\\)</span> be the design matrix that results from **adding 3 to each entry in the *second* column of <span class="math-inline">\\(X\\)</span>**. Let <span class="math-inline">\\(\vec v^* = (X&#95;c^TX&#95;c)^{-1}X&#95;c^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^*\\)</span> in terms of <span class="math-inline">\\(w&#95;0^*, w&#95;1^*, w&#95;2^*, w&#95;3^*\\)</span>.

</div>
</div>

</div>

---

## Problem 4: The Sum of Errors (8 pts)

Consider a set of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((\vec x&#95;1, y&#95;1), (\vec x&#95;2, y&#95;2), ..., (\vec x&#95;n, y&#95;n)\\)</span>, where each <span class="math-inline">\\(\vec x&#95;i\\)</span> is a feature vector in <span class="math-inline">\\(\mathbb{R}^d\\)</span> and each <span class="math-inline">\\(y&#95;i\\)</span> is a scalar.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) To fit the model

<div class="math-display">
$$
h(\vec x_i) = w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)} + ... + w_d x_i^{(d)} = \vec w \cdot \text{Aug}(\vec x_i)
$$
</div>

we minimize mean squared error,

<div class="math-display">
$$
R(\vec w) = \frac{1}{n} \sum_{i=1}^n (y_i - \vec w \cdot \text{Aug}(\vec x_i))^2 = \frac{1}{n} \lVert \vec y - X \vec w \rVert^2
$$
</div>

meaning that <span class="math-inline">\\(\vec w^*\\)</span> is chosen to satisfy the normal equations. Explain why the components of the error vector,

<div class="math-display">
$$
\vec e = \vec y - X \vec w^*
$$
</div>

are **guaranteed** to sum to 0.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) If we decide instead to fit the model

<div class="math-display">
$$
h(\vec x_i) = w_1 x_i^{(1)} + w_2 x_i^{(2)} + ... + w_d x_i^{(d)} = \vec w \cdot \vec x_i
$$
</div>

which has no intercept term, are the components of the error vector <span class="math-inline">\\(\vec e = \vec y - X \vec w^*\\)</span> still guaranteed to sum to 0? If they are, explain why. If they are not, explain why not, but give at least one example dataset where they still do sum to 0.
</div>
</div>

</div>

{% endraw %}
