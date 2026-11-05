---
layout: page
title: "Homework 8: Multiple Linear Regression; Gradients"
description: "Homework 8: Multiple Linear Regression; Gradients problems."
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
.assignment-description-box { border: 1px solid currentColor; padding: 1rem 1.25rem; margin: 1.25rem 0; border-radius: 0; }
.assignment-description-box > :last-child { margin-bottom: 0; }
</style>

# Homework 8: Multiple Linear Regression; Gradients

**due** Sunday, November 15th, 2026 at 11:59PM Ann Arbor Time <span style="color: red;">(no slip days allowed!)</span>

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw08/hw08.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Except for the video link in Problem 1, write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 7 Concept Video](#problem-1-homework-7-concept-video-10-pts)
- [Problem 2: Reading Regression Expressions](#problem-2-reading-regression-expressions-12-pts)
- [Problem 3: The Sum of Errors](#problem-3-the-sum-of-errors-10-pts)
- [Problem 4: Moving Things Around](#problem-4-moving-things-around-10-pts)
- [Problem 5: Gradient Descent Fundamentals](#problem-5-gradient-descent-fundamentals-8-pts)
- [Problem 6: Product and Chain Rules](#problem-6-product-and-chain-rules-18-pts)
- [Problem 7: Convexity](#problem-7-convexity-12-pts)

---

Total Points: <span class="math-inline">\\(10 + 12 + 10 + 10 + 8 + 18 + 12 = 80\\)</span>

---

## Problem 1: Homework 7 Concept Video (10 pts)

Record a **2- to 5-minute video** answering **one** of the prompts below. These prompts are related to the ideas in [Homework 7](https://eecs245.org/resources/homeworks/hw07/).

<ol class="assignment-list" markdown="1" data-item-count="3" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

When finding the optimal parameter <span class="math-inline">\\(\vec w^{\ast}\\)</span> in multiple linear regression, depending on the dataset, there may be infinitely many optimal <span class="math-inline">\\(\vec w^{\ast}\\)</span>s that all equally minimize mean squared error, but there is always only one optimal prediction vector. Explain how both of these facts are true simultaneously.

</li>
<li markdown="1" value="2">

Suppose you project a vector onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and then project the resulting vector onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> again. What happens and why? What property of a projection matrix <span class="math-inline">\\(P\\)</span> does this relate to?

</li>
<li markdown="1" value="3">

Suppose we add a feature that is a linear combination of the existing columns of the design matrix. What impact will this have on the (training) mean squared error of the resulting model?

</li>
</ol>

The video should be **just you speaking into the camera**. Your face must be visible while you are talking for the entire video. Do not include slides, a screen recording, written work, or any other visuals.

Submit your video link to the separate assignment on Pensive called **Homework 8, Problem 1 Video Link**. You can upload your video to YouTube as unlisted, share a Zoom recording link, or share a Google Drive link; whatever works. Make sure the course staff can view the video using that link.

Your submission time for Homework 8 is the latest of your two submission times: your Problem 1 video link and your PDF.

**This problem is graded on completion.** Record a video of the required length and make an honest effort to explain the question, and you will receive full credit. Your explanation does not need to be polished or perfect.

---

## Problem 2: Reading Regression Expressions (12 pts)

Suppose we'd like to fit a multiple linear regression model with an intercept and two features. The model is fit by minimizing mean squared error on <span class="math-inline">\\(n &gt; 3\\)</span> training points.

Let <span class="math-inline">\\(X\\)</span> be the <span class="math-inline">\\(n \times 3\\)</span> design matrix, whose first column is all 1s, and assume its columns are linearly independent. Let <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> be the observation vector and <span class="math-inline">\\(\vec w^{\ast} \in \mathbb{R}^3\\)</span> be the optimal parameter vector. Let <span class="math-inline">\\(\vec 1 \in \mathbb{R}^n\\)</span> be the vector of all 1s.

For each expression below, state its type – either scalar, vector, or matrix – and shape (for non-scalars), and choose the most appropriate English description from among the options provided. No justification is required. The first item has been completed for you.

<ol class="assignment-list" markdown="1" data-item-count="8" start="1" style="list-style-type: lower-roman;">
<li markdown="1" value="1">

<span class="math-inline">\\((X^TX)^{-1}X^T\vec y\\)</span>

**Solution:** Optimal parameter vector; vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

</li>
<li markdown="1" value="2">

(2 pts) <span class="math-inline">\\(X(X^TX)^{-1}X^T\\)</span>

</li>
<li markdown="1" value="3">

(2 pts) <span class="math-inline">\\(X(X^TX)^{-1}X^T\vec y\\)</span>

</li>
<li markdown="1" value="4">

(2 pts) <span class="math-inline">\\(\vec y - X\vec w^{\ast}\\)</span>

</li>
<li markdown="1" value="5">

(2 pts) <span class="math-inline">\\(X^TX\vec w^{\ast} - X^T\vec y\\)</span>

</li>
<li markdown="1" value="6">

(2 pts) <span class="math-inline">\\(\vec 1^T(\vec y - X\vec w^{\ast})\\)</span>

</li>
<li markdown="1" value="7">

(1 pt) <span class="math-inline">\\(\lVert \vec y - X\vec w^{\ast} \rVert^2\\)</span>

</li>
<li markdown="1" value="8">

(1 pt) <span class="math-inline">\\(\displaystyle\frac{1}{n}\lVert \vec y - X\vec w^{\ast} \rVert^2\\)</span>

</li>
</ol>

<div class="assignment-description-box" markdown="1">

**Possible descriptions**

<ul class="assignment-list" markdown="1" data-item-count="9">
<li markdown="1">

Training mean squared error

</li>
<li markdown="1">

Optimal parameter vector

</li>
<li markdown="1">

Projection matrix

</li>
<li markdown="1">

Zero vector

</li>
<li markdown="1">

Residual vector

</li>
<li markdown="1">

Sum of squared training errors

</li>
<li markdown="1">

Vector of predictions on the training points

</li>
<li markdown="1">

The scalar zero

</li>
<li markdown="1">

Reflection matrix

</li>
</ul>

</div>

---

## Problem 3: The Sum of Errors (10 pts)

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

meaning that <span class="math-inline">\\(\vec w^{\ast}\\)</span> is chosen to satisfy the normal equations. Explain why the components of the error vector,

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
(6 pts) If we decide instead to fit the model

<div class="math-display">
$$
h(\vec x_i) = w_1 x_i^{(1)} + w_2 x_i^{(2)} + ... + w_d x_i^{(d)} = \vec w \cdot \vec x_i
$$
</div>

which has no intercept term, are the components of the error vector <span class="math-inline">\\(\vec e = \vec y - X \vec w^{\ast}\\)</span> still guaranteed to sum to 0? If they are, explain why. If they are not, explain why not, but give at least one example dataset where they still do sum to 0.

</div>
</div>

</div>

---

## Problem 4: Moving Things Around (10 pts)

Let <span class="math-inline">\\(X\\)</span> be an <span class="math-inline">\\(n \times 4\\)</span> design matrix whose first column is all 1s, let <span class="math-inline">\\(\vec y\\)</span> be an observation vector, and let <span class="math-inline">\\(\vec w^{\ast} = (X^TX)^{-1}X^T \vec y\\)</span>.

<div class="math-display">
$$
\vec w^* = \begin{bmatrix} w_0^* \\\\ w_1^* \\\\ w_2^* \\\\ w_3^* \end{bmatrix}
$$
</div>

In this problem, you'll reason about modifications to the design matrix and see how they affect the components of <span class="math-inline">\\(\vec w^{\ast}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(X&#95;a\\)</span> be the design matrix that results from **swapping the first two columns of <span class="math-inline">\\(X\\)</span>**. Let

<span class="math-inline">\\(\vec v^{\ast} = (X&#95;a^TX&#95;a)^{-1}X&#95;a^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^{\ast}\\)</span> in terms of <span class="math-inline">\\(w&#95;0^{\ast}, w&#95;1^{\ast}, w&#95;2^{\ast}, w&#95;3^{\ast}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(X&#95;b\\)</span> be the design matrix that results from **adding 3 to each entry in the *first* column of <span class="math-inline">\\(X\\)</span>**. Let <span class="math-inline">\\(\vec v^{\ast} = (X&#95;b^TX&#95;b)^{-1}X&#95;b^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^{\ast}\\)</span> in terms of <span class="math-inline">\\(w&#95;0^{\ast}, w&#95;1^{\ast}, w&#95;2^{\ast}, w&#95;3^{\ast}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(X&#95;c\\)</span> be the design matrix that results from **adding 3 to each entry in the *second* column of <span class="math-inline">\\(X\\)</span>**. Let <span class="math-inline">\\(\vec v^{\ast} = (X&#95;c^TX&#95;c)^{-1}X&#95;c^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^{\ast}\\)</span> in terms of <span class="math-inline">\\(w&#95;0^{\ast}, w&#95;1^{\ast}, w&#95;2^{\ast}, w&#95;3^{\ast}\\)</span>.

</div>
</div>

</div>

---

## Problem 5: Gradient Descent Fundamentals (8 pts)

Let <span class="math-inline">\\(f(\vec x) = (x&#95;1 - 5)^2 + (x&#95;1^2 - x&#95;2)^2 + 1\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>, the gradient of <span class="math-inline">\\(f(\vec x)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) To minimize <span class="math-inline">\\(f(\vec x)\\)</span>, we'll use gradient descent. Perform one iteration of gradient descent by hand, using the initial guess <span class="math-inline">\\(\vec x^{(0)} = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span> and learning rate <span class="math-inline">\\(\alpha = \frac{1}{2}\\)</span>. What is <span class="math-inline">\\(\vec x^{(1)}\\)</span>?

</div>
</div>

</div>

---

## Problem 6: Product and Chain Rules (18 pts)

Our goal in this problem is to study the behavior of the function

<div class="math-display">
$$
f(\vec x) = \frac{\vec x^T A \vec x}{\vec x^T \vec x}
$$
</div>

where <span class="math-inline">\\(x \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix (meaning <span class="math-inline">\\(A = A^T\\)</span>). This function, called the **Rayleigh quotient**, will play an important role in [Chapter 10](https://notes.eecs245.org/singular-value-decomposition/computing-svd/) of the course, when we eventually study the **dimensionality reduction** problem first introduced in [Chapter 1.1](https://notes.eecs245.org/introduction-to-supervised-learning/what-is-machine-learning/#dimensionality-reduction).

But first, we have to get a handle on a few gradient rules.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) As described in the [Norm and Chain Rule in Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#example-norm-and-chain-rule), the chain rule for gradients says that if

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

<span class="math-inline">\\(g: \mathbb{R}^d \to \mathbb{R}\\)</span> is a **vector**-to-scalar function, and

</li>
<li markdown="1">

<span class="math-inline">\\(h: \mathbb{R} \to \mathbb{R}\\)</span> is a **scalar**-to-scalar function,

</li>
</ul>

then the gradient of the **vector**-to-scalar function <span class="math-inline">\\(f(\vec x) = h(g(\vec x))\\)</span> is given by

<div class="math-display">
$$
\nabla f(\vec x) = \left( \frac{\text{d}h}{\text{d}x} (g(\vec x)) \right) \nabla g(\vec x)
$$
</div>

 or, perhaps more intuitively,

<div class="math-display">
$$
\nabla f(\vec x) = h'(g(\vec x)) \nabla g(\vec x)
$$
</div>

Note that we need to pay close attention to the types of functions we're working with. <span class="math-inline">\\(h(g(\vec x))\\)</span> is well-defined, but <span class="math-inline">\\(g(h(\vec x))\\)</span> is not, since <span class="math-inline">\\(h\\)</span> doesn't take in vectors (it takes in scalars).

Find the gradients of each of the following functions.

<ol class="assignment-list" markdown="1" data-item-count="2" start="1" style="list-style-type: lower-roman;">
<li markdown="1" value="1">

(3 pts) <span class="math-inline">\\(f&#95;1(\vec x) = \log(\vec x^T A \vec x)\\)</span>, where <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix

</li>
<li markdown="1" value="2">

(3 pts) <span class="math-inline">\\(f&#95;2(\vec x) = e^{-\sin(\vec a^T\vec x)}\\)</span>, where <span class="math-inline">\\(\vec x, \vec a \in \mathbb{R}^n\\)</span>

</li>
</ol>

Here, <span class="math-inline">\\(\log(x)\\)</span> denotes the base-<span class="math-inline">\\(e\\)</span> logarithm, i.e. <span class="math-inline">\\(\ln(x)\\)</span>.

<em>Hint: You can use any of the <a href="https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#the-big-three-rules">three important gradient rules from Chapter 8.2</a> without proof.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) The product rule for gradients is a natural extension of the product rule for derivatives. If <span class="math-inline">\\(f(\vec x) = g(\vec x) h(\vec x)\\)</span>, then

<div class="math-display">
$$
\nabla f(\vec x) = \nabla (g(\vec x) h(\vec x)) = g(\vec x) \nabla h(\vec x) + h(\vec x) \nabla g(\vec x)
$$
</div>

Find the gradients of each of the following functions.

<ol class="assignment-list" markdown="1" data-item-count="2" start="1" style="list-style-type: lower-roman;">
<li markdown="1" value="1">

(2 pts) <span class="math-inline">\\(f&#95;3(\vec x) = (\vec a \cdot \vec x)(\vec b \cdot \vec x)\\)</span>, where <span class="math-inline">\\(\vec x, \vec a, \vec b \in \mathbb{R}^n\\)</span>

</li>
<li markdown="1" value="2">

(4 pts) <span class="math-inline">\\(f&#95;4(\vec x) = \vec a^T \vec x \vec x^T A \vec x\\)</span>, where <span class="math-inline">\\(\vec x, \vec a \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix

</li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Putting together the chain rule and product rule, show that if

<div class="math-display">
$$
f(\vec x) = \frac{\vec x^T A \vec x}{\vec x^T \vec x}
$$
</div>

where <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix, then

<div class="math-display">
$$
\nabla f(\vec x) = \frac{2}{\vec x^T \vec x} \left( A \vec x - f(\vec x) \vec x \right)
$$
</div>

</div>
</div>

</div>

---

## Problem 7: Convexity (12 pts)

In [Chapter 8.5](https://notes.eecs245.org/gradients/convexity/), we introduce the formal definition of **convexity** for vector-to-scalar functions. Formally, the function <span class="math-inline">\\(f: \mathbb{R}^d \to \mathbb{R}\\)</span> is convex if for all <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^d\\)</span> and all <span class="math-inline">\\(t \in [0,1]\\)</span>,

<div class="math-display">
$$
f((1-t)\vec x + t \vec y) \le (1-t) f(\vec x) + t f(\vec y)
$$
</div>

This is a formal way of saying that when you connect any two points on the graph of <span class="math-inline">\\(f\\)</span> with a line segment, the line segment lies on or above the graph of <span class="math-inline">\\(f\\)</span>, never below.

For each statement below, prove that the statement is true using the formal definition above, or give a counterexample. You don't need to prove that a counterexample does not satisfy the formal definition; visual counterexamples are sufficient.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) The sum of two convex functions must also be convex.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) The difference of two convex functions must also be convex.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose <span class="math-inline">\\(f(x)\\)</span> and <span class="math-inline">\\(g(x)\\)</span> are both scalar-to-scalar convex functions and that, for some scalar <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(f(a) = g(a)\\)</span>. Then, <span class="math-inline">\\(h(x)\\)</span> is also convex, where

<div class="math-display">
$$
h(x) = \begin{cases} f(x) & x \leq a \\\\ g(x) & x > a \end{cases}
$$
</div>

<em>Hint: The statement is false, so focus your energy on finding a counterexample.</em>
</div>
</div>

</div>

{% endraw %}
