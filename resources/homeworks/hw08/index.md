---
layout: page
title: "Homework 8: Multiple Linear Regression, Gradients"
description: "Homework 8: Multiple Linear Regression, Gradients problems."
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

# Homework 8: Multiple Linear Regression, Gradients

**due** Sunday, June 7th, 2026 at 11:59PM Ann Arbor Time <span style="color: red;">(no slip days allowed!)</span>

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw08/hw08.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw08/hw08-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 7 Solutions Review](#problem-1-homework-7-solutions-review-10-pts)
- [Problem 2: The Sum of Errors](#problem-2-the-sum-of-errors-8-pts)
- [Problem 3: Moving Things Around](#problem-3-moving-things-around-10-pts)
- [Problem 4: Gradient Descent Fundamentals](#problem-4-gradient-descent-fundamentals-8-pts)
- [Problem 5: Product and Chain Rules](#problem-5-product-and-chain-rules-13-pts)
- [Problem 6: Convexity](#problem-6-convexity-12-pts)

---

Total Points: 10 + 8 + 10 + 8 + 13 + 12 = 61

---

## Problem 1: Homework 7 Solutions Review (10 pts)

Review the solutions to Homework 7 and pick **two problem parts** (for example, Problem 3c and Problem 5b) from Homework 7 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 7, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

<details markdown="1"><summary>Solution</summary>

</details>

---

## Problem 2: The Sum of Errors (8 pts)

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

<details markdown="1"><summary>Solution</summary>

At the optimal parameters <span class="math-inline">\\(\vec w^{\ast}\\)</span>, the normal equations hold:

<div class="math-display">
$$
X^T(\vec y - X\vec w^*) = 0
$$
</div>

 This means the residual vector <span class="math-inline">\\(\vec e = \vec y - X\vec w^{\ast}\\)</span> is orthogonal to every column of <span class="math-inline">\\(X\\)</span>, **and any of their linear combinations**.

Because the first column of <span class="math-inline">\\(X\\)</span> consists of all 1s (from the intercept term), orthogonality with that column implies

<div class="math-display">
$$
\vec 1^T \vec e = 0 \quad \Longrightarrow \quad \sum_{i=1}^n e_i = 0
$$
</div>

Therefore, the residuals (errors) always sum to zero when an intercept is included in the model.

<div class="math-display">
$$
\boxed{\sum_{i=1}^n e_i = 0}
$$
</div>

</details>

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

which has no intercept term, are the components of the error vector <span class="math-inline">\\(\vec e = \vec y - X \vec w^{\ast}\\)</span> still guaranteed to sum to 0? If they are, explain why. If they are not, explain why not, but give at least one example dataset where they still do sum to 0.

<details markdown="1"><summary>Solution</summary>

Without an intercept term, the first column of <span class="math-inline">\\(X\\)</span> is no longer all 1s. The normal equations <span class="math-inline">\\(X^T\vec e = 0\\)</span> still ensure <span class="math-inline">\\(\vec e\\)</span> is orthogonal to each column of <span class="math-inline">\\(X\\)</span>, but *not* necessarily to the all-ones vector. Therefore, there is **no guarantee** that the components of <span class="math-inline">\\(\vec e\\)</span> sum to 0.

However, they still **can** sum to 0. For instance, if <span class="math-inline">\\(\vec 1\\)</span> lies in the column space of <span class="math-inline">\\(X\\)</span>, the errors will still sum to 0 --- in other words, if you can make a vector of all ones using linear combinations of the other columns of <span class="math-inline">\\(X\\)</span>, <span class="math-inline">\\(\vec e\\)</span> will be orthogonal to that vector, and therefore sum to 0.

Even if <span class="math-inline">\\(\vec 1\\)</span> isn't in the column space of <span class="math-inline">\\(X\\)</span>, if <span class="math-inline">\\(\vec y\\)</span> is in the column space of <span class="math-inline">\\(X\\)</span>, the errors will sum to 0 because they'll all be 0 exactly. For example, if

<div class="math-display">
$$
X = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 0 & 0 \end{bmatrix}, \quad \vec y = \begin{bmatrix} 5 \\\\ 6 \\\\ 0 \end{bmatrix}
$$
</div>

then since <span class="math-inline">\\(\vec y = X \begin{bmatrix} 5 \\\\ 6 \end{bmatrix}\\)</span> exactly, the error vector <span class="math-inline">\\(\vec e\\)</span> is just <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, and therefore sums to 0.
</details>

</div>
</div>

</div>

---

## Problem 3: Moving Things Around (10 pts)

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

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\vec v^* = \begin{bmatrix} v_0^* \\\\ v_1^* \\\\ v_2^* \\\\ v_3^* \end{bmatrix} = \begin{bmatrix} w_1^* \\\\ w_0^* \\\\ w_2^* \\\\ w_3^* \end{bmatrix}
$$
</div>

Suppose our original model was of the form:

<div class="math-display">
$$
h(x_i^{(1)}, x_i^{(2)}, x_i^{(3)}) =
w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)} + w_3 x_i^{(3)}
$$
</div>

Because the column space of the resulting design matrix has not changed, the optimal predictions themselves will not change, because the optimal predictions come from projecting <span class="math-inline">\\(\vec y\\)</span> onto the same <span class="math-inline">\\(\text{colsp}(X)\\)</span>. So, the problem boils down to figuring out how to choose the coefficients in <span class="math-inline">\\(\vec{v}^{\ast}\\)</span> so that the predictions of the resulting model are the same as those in the original model. **This logic holds for the other parts of the problem, too.**

Swapping the first two columns of <span class="math-inline">\\(X\\)</span> interchanges the constant (intercept) column and the <span class="math-inline">\\(x&#95;i^{(1)}\\)</span> column. The modified model is then

<div class="math-display">
$$
h(x_i^{(1)}, x_i^{(2)}, x_i^{(3)}) =
v_1 + v_0 x_i^{(1)} + v_2 x_i^{(2)} + v_3 x_i^{(3)}
$$
</div>

To produce the same predictions as before, the coefficients must switch positions accordingly:

<div class="math-display">
$$
v_0^* = w_1^* \quad v_1^* = w_0^* \quad v_2^* = w_2^* \quad v_3^* = w_3^*
$$
</div>

Intuitively, when we interchange two columns of our design matrix, all that does is interchange the terms in the model, which interchanges those weights in the parameter vector.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(X&#95;b\\)</span> be the design matrix that results from **adding 3 to each entry in the *first* column of <span class="math-inline">\\(X\\)</span>**. Let <span class="math-inline">\\(\vec v^{\ast} = (X&#95;b^TX&#95;b)^{-1}X&#95;b^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^{\ast}\\)</span> in terms of <span class="math-inline">\\(w&#95;0^{\ast}, w&#95;1^{\ast}, w&#95;2^{\ast}, w&#95;3^{\ast}\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\vec v^* = \begin{bmatrix} v_0^* \\\\ v_1^* \\\\ v_2^* \\\\ v_3^* \end{bmatrix} = \begin{bmatrix} w_0^* / 4 \\\\ w_1^* \\\\ w_2^* \\\\ w_3^* \end{bmatrix}
$$
</div>

Suppose our original model was of the form:

<div class="math-display">
$$
h(x_i^{(1)}, x_i^{(2)}, x_i^{(3)}) =
w_0(1) + w_1 x_i^{(1)} + w_2 x_i^{(2)} + w_3 x_i^{(3)}
$$
</div>

Adding <span class="math-inline">\\(3\\)</span> to each entry of the first column of <span class="math-inline">\\(X\\)</span> means the intercept column (previously all ones) becomes a column of all fours. The new model is therefore

<div class="math-display">
$$
h(x_i^{(1)}, x_i^{(2)}, x_i^{(3)}) =
v_0\cdot 4 + v_1 x_i^{(1)} + v_2 x_i^{(2)} + v_3 x_i^{(3)}
$$
</div>

In order to compensate for these changes to our coefficients, we need to "offset" any alterations made to our coefficients. To keep the model predictions identical to those produced by <span class="math-inline">\\(\vec w^{\ast}\\)</span>, the term multiplying the constant column must remain the same:

<div class="math-display">
$$
4v_0^* = w_0^*.
$$
</div>

 All other coefficients remain unchanged.

Thus,

<div class="math-display">
$$
v_0^* = \frac{w_0^*}{4} \quad v_1^* = w_1^* \quad v_2^* = w_2^* \quad v_3^* = w_3^*
$$
</div>

For example, imagine fitting a line to data in <span class="math-inline">\\(\mathbb{R}^2\\)</span> and finding that the best-fitting line is <span class="math-inline">\\(y = 12 + 3x\\)</span>. If we had to write this in the form <span class="math-inline">\\(y = v&#95;0 \cdot 4 + v&#95;1 x\\)</span>, then the best choice for <span class="math-inline">\\(v&#95;0\\)</span> would be <span class="math-inline">\\(3\\)</span>, since <span class="math-inline">\\(4v&#95;0 = 12\\)</span>, and the best choice for <span class="math-inline">\\(v&#95;1\\)</span> would be <span class="math-inline">\\(3\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(X&#95;c\\)</span> be the design matrix that results from **adding 3 to each entry in the *second* column of <span class="math-inline">\\(X\\)</span>**. Let <span class="math-inline">\\(\vec v^{\ast} = (X&#95;c^TX&#95;c)^{-1}X&#95;c^T \vec y\\)</span>. Express the components of <span class="math-inline">\\(\vec v^{\ast}\\)</span> in terms of <span class="math-inline">\\(w&#95;0^{\ast}, w&#95;1^{\ast}, w&#95;2^{\ast}, w&#95;3^{\ast}\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\vec v^* =
\begin{bmatrix}
w_0^* - 3w_1^* \\\\[4pt]
w_1^* \\\\[4pt]
w_2^* \\\\[4pt]
w_3^*
\end{bmatrix}
$$
</div>

Suppose our original model was of the form

<div class="math-display">
$$
h(x_i^{(1)}, x_i^{(2)}, x_i^{(3)}) =
w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)} + w_3 x_i^{(3)}
$$
</div>

Adding <span class="math-inline">\\(3\\)</span> to every entry in the second column means that the feature <span class="math-inline">\\(x&#95;i^{(1)}\\)</span> is replaced by <span class="math-inline">\\(x&#95;i^{(1)} + 3\\)</span>. The new model becomes

<div class="math-display">
$$
h(x_i^{(1)}, x_i^{(2)}, x_i^{(3)}) =
v_0 + v_1(x_i^{(1)} + 3) + v_2 x_i^{(2)} + v_3 x_i^{(3)}
$$
</div>

Expanding this gives:

<div class="math-display">
$$
h(x_i^{(1)}, x_i^{(2)}, x_i^{(3)}) =
(v_0 + 3v_1) + v_1 x_i^{(1)} + v_2 x_i^{(2)} + v_3 x_i^{(3)}
$$
</div>

In order to compensate for these changes to our coefficients, we need to "offset" any alterations made to our coefficients. For the model to produce identical predictions as before, each coefficient multiplying a feature must match its original:

<div class="math-display">
$$
v_1^* = w_1^* \quad v_2^* = w_2^* \quad v_3^* = w_3^*
$$
</div>

 To offset the constant <span class="math-inline">\\(+3v&#95;1\\)</span>, the intercept must decrease by <span class="math-inline">\\(3w&#95;1^{\ast}\\)</span>:

<div class="math-display">
$$
v_0^* + 3v_1^* = w_0^*
\quad \Rightarrow \quad
v_0^* = w_0^* - 3w_1^*
$$
</div>

One way to think about this is that if we shift the feature <span class="math-inline">\\(x&#95;i^{(1)}\\)</span> by a constant value, all predictions increase by that feature's coefficient times the constant (here <span class="math-inline">\\(3w&#95;1^{\ast}\\)</span>). To preserve the same overall outputs, the intercept term must decrease by that same amount.
</details>

</div>
</div>

</div>

---

## Problem 4: Gradient Descent Fundamentals (8 pts)

Let <span class="math-inline">\\(f(\vec x) = (x&#95;1 - 5)^2 + (x&#95;1^2 - x&#95;2)^2 + 1\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>, the gradient of <span class="math-inline">\\(f(\vec x)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let's start by computing the partial derivatives of <span class="math-inline">\\(f\\)</span> with respect to <span class="math-inline">\\(x&#95;1\\)</span> and <span class="math-inline">\\(x&#95;2\\)</span>.

<div class="math-display">
$$
f(\vec x) = f\left( \begin{bmatrix} x_1 \\\\ x_2 \end{bmatrix} \right) = (x_1 - 5)^2 + (x_1^2 - x_2)^2 + 1
$$
</div>

First, let's compute <span class="math-inline">\\(\frac{\partial f}{\partial x&#95;1}\\)</span>. Using the chain rule:

<div class="math-display">
$$
\frac{\partial f}{\partial x_1} = 2(x_1 - 5) + 2(x_1^2 - x_2) \cdot (2x_1) = 2(x_1 - 5) + 4x_1(x_1^2 - x_2)
$$
</div>

Next, let's compute <span class="math-inline">\\(\frac{\partial f}{\partial x&#95;2}\\)</span>. Only the term <span class="math-inline">\\((x&#95;1^2 - x&#95;2)^2\\)</span> depends on <span class="math-inline">\\(x&#95;2\\)</span>.

<div class="math-display">
$$
\frac{\partial f}{\partial x_2} = 2(x_1^2 - x_2)(-1) = -2(x_1^2 - x_2)
$$
</div>

So, the gradient is:

<div class="math-display">
$$
\boxed{\nabla f(\vec x) =
\begin{bmatrix}
2(x_1 - 5) + 4x_1(x_1^2 - x_2) \\\\
-2(x_1^2 - x_2)
\end{bmatrix}}
$$
</div>

This coould be further simplified, but there's no need.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) To minimize <span class="math-inline">\\(f(\vec x)\\)</span>, we'll use gradient descent. Perform one iteration of gradient descent by hand, using the initial guess <span class="math-inline">\\(\vec x^{(0)} = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span> and learning rate <span class="math-inline">\\(\alpha = \frac{1}{2}\\)</span>. What is <span class="math-inline">\\(\vec x^{(1)}\\)</span>?

<details markdown="1"><summary>Solution</summary>

The gradient descent update rule is:

<div class="math-display">
$$
\vec x^{(t+1)} = \vec x^{(t)} - \alpha \nabla f(\vec x^{(t)})
$$
</div>

We've already computed <span class="math-inline">\\(\nabla f(\vec x^{(0)}) = \nabla f(\begin{bmatrix} 0 \\\\ 1 \end{bmatrix}) = \begin{bmatrix} -10 \\\\ 2 \end{bmatrix}\\)</span> from the previous part, so we can plug in everything we know:

<div class="math-display">
$$
\begin{align*}
\vec x^{(1)} &= \vec x^{(0)} - \alpha \nabla f(\vec x^{(0)}) \\\\
&= \begin{bmatrix} 0 \\\\ 1 \end{bmatrix} - \frac{1}{2} \begin{bmatrix} -10 \\\\ 2 \end{bmatrix} \\\\
&= \begin{bmatrix} 0 + 5 \\\\ 1 - 1 \end{bmatrix} \\\\
&= \begin{bmatrix} 5 \\\\ 0 \end{bmatrix}
\end{align*}
$$
</div>

So,

<div class="math-display">
$$
\boxed{\vec x^{(1)} =
\begin{bmatrix}
5 \\\\
0
\end{bmatrix}}
$$
</div>

This means that after one gradient descent step with <span class="math-inline">\\(\alpha = \frac{1}{2}\\)</span>, the algorithm moves the guess for <span class="math-inline">\\(\vec x^{\ast}\\)</span> from <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span> to <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ 0 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 5: Product and Chain Rules (13 pts)

Our goal in this problem is to study the behavior of the function

<div class="math-display">
$$
f(\vec x) = \frac{\vec x^T A \vec x}{\vec x^T \vec x}
$$
</div>

where <span class="math-inline">\\(x \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix (meaning <span class="math-inline">\\(A = A^T\\)</span>). This function, called the **Rayleigh quotient**, will play an important role in Chapter 5 of the course, when we eventually study the **dimensionality reduction** problem first introduced in [Chapter 1.1](https://notes.eecs245.org/introduction-to-supervised-learning/what-is-machine-learning/#dimensionality-reduction).

But first, we have to get a handle on a few gradient rules.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) As described in the [Norm and Chain Rule in Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#example-norm-and-chain-rule), the chain rule for gradients says that if

-   <span class="math-inline">\\(g: \mathbb{R}^d \to \mathbb{R}\\)</span> is a **vector**-to-scalar function, and

-   <span class="math-inline">\\(h: \mathbb{R} \to \mathbb{R}\\)</span> is a **scalar**-to-scalar function,

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

1.  <span class="math-inline">\\(f&#95;1(\vec x) = \log(\vec x^T A \vec x)\\)</span>, where <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix

2.  <span class="math-inline">\\(f&#95;2(\vec x) = e^{-\sin(\vec a^T\vec x)}\\)</span>, where <span class="math-inline">\\(\vec x, \vec a \in \mathbb{R}^n\\)</span>

Here, <span class="math-inline">\\(\log(x)\\)</span> denotes the base-<span class="math-inline">\\(e\\)</span> logarithm, i.e. <span class="math-inline">\\(\ln(x)\\)</span>.

<em>Hint: You can use any of the <a href="https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#the-big-three-rules">three important gradient rules from Chapter 8.2</a> without proof.</em>

<details markdown="1"><summary>Solution</summary>

**(i)** For <span class="math-inline">\\(f&#95;1(\vec x) = \log(\vec x^T A \vec x)\\)</span>:

Let <span class="math-inline">\\(g(\vec x) = \vec x^T A \vec x\\)</span>. Then, using the known rule for quadratic forms,

<div class="math-display">
$$
\nabla g(\vec x) = 2A\vec x
$$
</div>

 since <span class="math-inline">\\(A\\)</span> is symmetric.

Since <span class="math-inline">\\(\frac{\text{d}}{\text{d}x} \log(x) = \frac{1}{x}\\)</span>, the chain rule says:

<div class="math-display">
$$
\nabla f_1(\vec x) = \frac{1}{\vec x^T A \vec x} \nabla g(\vec x) = \frac{1}{\vec x^T A \vec x} 2A \vec x = \boxed{ \frac{2A\vec x}{\vec x^T A \vec x}}
$$
</div>

**(ii)** For <span class="math-inline">\\(f&#95;2(\vec x) = e^{-\sin(\vec a^T \vec x)}\\)</span>:

Let <span class="math-inline">\\(g(\vec x) = -\sin(\vec a^T \vec x)\\)</span> and <span class="math-inline">\\(h(x) = e^x\\)</span>. Then <span class="math-inline">\\(f&#95;2(\vec x) = h(g(\vec x))\\)</span>.

By the chain rule,

<div class="math-display">
$$
\nabla f_2(\vec x) = \underbrace{\left(\frac{\text{d}h}{\text{d}x}(g(\vec x)) \right)}_{h'(g(\vec x))} \nabla g(\vec x)
$$
</div>

We know <span class="math-inline">\\(\frac{\text{d}h}{\text{d}x} = e^x\\)</span>, so <span class="math-inline">\\(\frac{\text{d}h}{\text{d}x}(g(\vec x)) = e^{g(\vec x)} = e^{-\sin(\vec a^T \vec x)}\\)</span>.

The gradient of <span class="math-inline">\\(g(\vec x)\\)</span> is

<div class="math-display">
$$
\nabla g(\vec x) = -\cos(\vec a^T \vec x)\vec a
$$
</div>

So, the full application of the chain rule gives us

<div class="math-display">
$$
\boxed{\nabla f_2(\vec x) = -e^{-\sin(\vec a^T \vec x)} \cos(\vec a^T \vec x)\vec a}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) The product rule for gradients is a natural extension of the product rule for derivatives. If <span class="math-inline">\\(f(\vec x) = g(\vec x) h(\vec x)\\)</span>, then

<div class="math-display">
$$
\nabla f(\vec x) = \nabla (g(\vec x) h(\vec x)) = g(\vec x) \nabla h(\vec x) + h(\vec x) \nabla g(\vec x)
$$
</div>

Find the gradients of each of the following functions.

1.  <span class="math-inline">\\(f&#95;3(\vec x) = (\vec a \cdot \vec x)(\vec b \cdot \vec x)\\)</span>, where <span class="math-inline">\\(\vec x, \vec a, \vec b \in \mathbb{R}^n\\)</span>

2.  <span class="math-inline">\\(f&#95;4(\vec x) = \vec a^T \vec x \vec x^T A \vec x\\)</span>, where <span class="math-inline">\\(\vec x, \vec a \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(A\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix

<details markdown="1"><summary>Solution</summary>

**(i)** For <span class="math-inline">\\(f&#95;3(\vec x) = (\vec a \cdot \vec x)(\vec b \cdot \vec x)\\)</span>:

Let <span class="math-inline">\\(g(\vec x) = \vec a \cdot \vec x\\)</span> and <span class="math-inline">\\(h(\vec x) = \vec b \cdot \vec x\\)</span>, then <span class="math-inline">\\(\nabla g(\vec x) = \vec a\\)</span> and <span class="math-inline">\\(\nabla h(\vec x) = \vec b\\)</span>.

Then, the product rule tells us

<div class="math-display">
$$
\begin{align*}
\nabla f_3(\vec x) &= g(\vec x)\nabla h(\vec x) + h(\vec x)\nabla g(\vec x) \\\\
&= \boxed{(\vec a \cdot \vec x)\vec b + (\vec b \cdot \vec x)\vec a}
\end{align*}
$$
</div>

**(ii)** For <span class="math-inline">\\(f&#95;4(\vec x) = \vec a^T \vec x  \vec x^T A \vec x\\)</span>:

Let <span class="math-inline">\\(g(\vec x) = \vec a^T \vec x\\)</span> and <span class="math-inline">\\(h(\vec x) = \vec x^T A \vec x\\)</span>, then <span class="math-inline">\\(\nabla g(\vec x) = \vec a\\)</span> and <span class="math-inline">\\(\nabla h(\vec x) = 2A\vec x\\)</span> (since <span class="math-inline">\\(A\\)</span> is symmetric).

Then,

<div class="math-display">
$$
\begin{align*}
\nabla f_4(\vec x)
&= g(\vec x)\nabla h(\vec x) + h(\vec x)\nabla g(\vec x) \\\\
&= (\vec a^T \vec x)(2A\vec x) + (\vec x^T A \vec x)\vec a \\\\
&= \boxed{2(\vec a^T \vec x)A\vec x + (\vec x^T A \vec x)\vec a}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Putting together the chain rule and product rule, show that if

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

<details markdown="1"><summary>Solution</summary>

Let

<div class="math-display">
$$
g(\vec x) = \vec x^T A \vec x \quad h(\vec x) = \frac{1}{\vec x^T \vec x}
$$
</div>

Then,

<div class="math-display">
$$
f(\vec x) = g(\vec x) h(\vec x)
$$
</div>

Notice that we **intentionally** didn't introduce a quotient rule! Instead, we gave you the tools to find <span class="math-inline">\\(\nabla h(\vec x)\\)</span>, which allows you to then use the product rule.

So first, since <span class="math-inline">\\(\frac{\text{d}}{\text{d}x} \left(\frac{1}{x}\right) = -\frac{1}{x^2}\\)</span>, we have

<div class="math-display">
$$
\nabla h(\vec x) = \nabla \left(\frac{1}{\vec x^T \vec x}\right) = -\frac{1}{(\vec x^T \vec x)^2} \nabla (\vec x^T \vec x) = -\frac{1}{(\vec x^T \vec x)^2} (2\vec x) = -\frac{2\vec x}{(\vec x^T \vec x)^2}
$$
</div>

Now, we're ready to use the product rule, with <span class="math-inline">\\(g(\vec x) = \vec x^T A \vec x\\)</span>, <span class="math-inline">\\(\nabla g(\vec x) = 2A\vec x\\)</span>, <span class="math-inline">\\(h(\vec x) = \frac{1}{\vec x^T \vec x}\\)</span>, and <span class="math-inline">\\(\nabla h(\vec x) = -\frac{2\vec x}{(\vec x^T \vec x)^2}\\)</span>.

<div class="math-display">
$$
\begin{align*}
\nabla f(\vec x) &= g(\vec x)\nabla h(\vec x) + h(\vec x)\nabla g(\vec x) \\\\
&= (\vec x^T A \vec x)\left(-\frac{2\vec x}{(\vec x^T \vec x)^2}\right) + \frac{1}{\vec x^T \vec x}(2A\vec x) \\\\
&= \frac{\vec x^TA\vec x}{\vec x^T \vec x}\left(\frac{-2 \vec x}{\vec x^T \vec x} \right) + \frac{2A\vec x}{\vec x^T \vec x} \\\\
&= f(\vec x)\left(\frac{-2 \vec x}{\vec x^T \vec x} \right) + \frac{2A\vec x}{\vec x^T \vec x} \\\\
&= \boxed{\frac{2}{\vec x^T \vec x} \left( A \vec x - f(\vec x) \vec x \right)}
\end{align*}
$$
</div>

There were several ways to simplify the expression, and any correct answer will receive full credit. But, by using the fact that <span class="math-inline">\\(f(\vec x) = \frac{\vec x^T A \vec x}{\vec x^T \vec x}\\)</span>, the expression simplifies rather nicely, **and we will see this specific gradient again in Chapter 10**, when studying PCA.
</details>

</div>
</div>

</div>

---

## Problem 6: Convexity (12 pts)

In [this video](https://www.loom.com/share/0b459d47827d4a2093d58a0632c9a97e), we introduce the formal definition of **convexity** for vector-to-scalar functions. Intuitively, a function <span class="math-inline">\\(f: \mathbb{R}^d \to \mathbb{R}\\)</span> is convex if its graph is a bowl-shaped surface. Formally, <span class="math-inline">\\(f\\)</span> is convex if for all <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^d\\)</span> and all <span class="math-inline">\\(t \in [0,1]\\)</span>,

<div class="math-display">
$$
f((1-t)\vec x + t \vec y) \le (1-t) f(\vec x) + t f(\vec y)
$$
</div>

This is a formal way of saying that when you connect any two points on the graph of <span class="math-inline">\\(f\\)</span> with a line segment, the line segment lies on or above the graph of <span class="math-inline">\\(f\\)</span>, never below.

The second derivative test for convexity is more convenient, but it doesn't apply to non-differentiable functions, e.g. <span class="math-inline">\\(f(x) = |x|\\)</span> is convex, but it isn't differentiable.

For each statement below, prove that the statement is true using the formal definition above, or give a counterexample.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) The sum of two convex functions must also be convex.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(f\\)</span> and <span class="math-inline">\\(g\\)</span> be convex functions. We want to show that their sum <span class="math-inline">\\(h(x) = f(x) + g(x)\\)</span> is also convex.

Let's start with the definition of convexity. For any <span class="math-inline">\\(x, y\\)</span> in <span class="math-inline">\\(f\\)</span>'s domain and <span class="math-inline">\\(t \in [0,1]\\)</span>, since <span class="math-inline">\\(f\\)</span> and <span class="math-inline">\\(g\\)</span> are convex, we have:

<div class="math-display">
$$
f((1-t)x + ty) \leq (1-t) f(x) + t f(y)
$$
</div>



<div class="math-display">
$$
g((1-t)x + ty) \leq (1-t) g(x) + t g(y)
$$
</div>

Note that the above two inequalities are individually true for any valid <span class="math-inline">\\(t\\)</span>, but to combine them we can pick the same <span class="math-inline">\\(t\\)</span>. Adding the two inequalities gives

<div class="math-display">
$$
f((1-t)x + ty) + g((1-t)x + ty) \leq (1-t)[f(x) + g(x)] + t[f(y) + g(y)]
$$
</div>

We can recognize that the left-hand side is <span class="math-inline">\\(h((1-t)x + ty)\\)</span>, and the right-hand side is <span class="math-inline">\\((1-t) h(x) + t h(y)\\)</span>.

<div class="math-display">
$$
h((1-t)x + ty) \leq (1-t) h(x) + t h(y)
$$
</div>

And we can conclude that <span class="math-inline">\\(h(x) = f(x) + g(x)\\)</span> satisfies the convexity definition.

<div class="math-display">
$$
\boxed{\text{Therefore, the sum of convex functions is convex.}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) The difference of two convex functions must also be convex.

<details markdown="1"><summary>Solution</summary>

This statement is **not true** in general. As a counterexample, let's consider <span class="math-inline">\\(f(x) = x^2\\)</span> and <span class="math-inline">\\(g(x) = 2x^2\\)</span>. Then both <span class="math-inline">\\(f\\)</span> and <span class="math-inline">\\(g\\)</span> are convex, but

<div class="math-display">
$$
h(x) = f(x) - g(x) = x^2 - 2x^2 = -x^2
$$
</div>

 which is concave, not convex (since its second derivative is negative).

<div class="math-display">
$$
\boxed{\text{The difference of two convex functions is not necessarily convex.}}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

We will show that this statement is **false** by constructing convex <span class="math-inline">\\(f\\)</span> and <span class="math-inline">\\(g\\)</span> for which <span class="math-inline">\\(h(x)\\)</span> is not convex:

Let

<div class="math-display">
$$
f(x) = x^2, \quad g(x) = (x - 2)^2, \quad \text{and } a = 1
$$
</div>

 Then:

<div class="math-display">
$$
f(1) = 1^2 = 1 \quad g(1) = (1 - 2)^2 = 1
$$
</div>

 so <span class="math-inline">\\(f(a) = g(a)\\)</span> as required.

<div class="math-display">
$$
h(x) =
\begin{cases}
x^2 & x \leq 1 \\\\
(x - 2)^2 & x > 1
\end{cases}
$$
</div>

<div style="text-align: center;">
<img src="imgs/p6c-counterexample.png" alt="image" style="width: 80%; max-width: 100%;">
</div>

<span class="math-inline">\\(h(x)\\)</span> is not convex: there are plenty of secant lines (line segments connecting two points on the curve) that partially lie below the curve.

<div class="math-display">
$$
\boxed{\text{The function } h(x) \text{ is not necessarily convex, even if } f \text{ and } g \text{ are.}}
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
