---
layout: page
title: "Lab 8: Multiple Linear Regression; The Gradient Vector"
description: "Lab 8: Multiple Linear Regression; The Gradient Vector activities."
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

# Lab 8: Multiple Linear Regression; The Gradient Vector

**due** for completion at 11:59PM Ann Arbor Time on Wednesday, June 3rd, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab08/lab08.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).
</div>

---

## Activities

- [Activity 1: Multiple Linear Regression](#activity-1-multiple-linear-regression)
- [Activity 2: Chicken, Beef, or Fish?](#activity-2-chicken-beef-or-fish)
- [Activity 3: Gradients and Partial Derivatives](#activity-3-gradients-and-partial-derivatives)
- [Activity 4: The Big Three](#activity-4-the-big-three)
- [Activity 5: Quadratic Forms and Symmetry](#activity-5-quadratic-forms-and-symmetry)

---

## Recap: Multiple Linear Regression ([Chapter 7.2](https://notes.eecs245.org/regression-using-linear-algebra/multiple-linear-regression/))

Suppose we have <span class="math-inline">\\(n\\)</span> data points, <span class="math-inline">\\((\vec x&#95;1, y&#95;1), (\vec x&#95;2, y&#95;2), \dots (\vec x&#95;n, y&#95;n)\\)</span>, where each <span class="math-inline">\\(\vec x&#95;i\\)</span> is a feature vector of <span class="math-inline">\\(d\\)</span> features:

<div class="math-display">
$$
\vec x_i = \begin{bmatrix}
x_i^{(1)} \\\\
x_i^{(2)} \\\\
\vdots \\\\
x_i^{(d)}
\end{bmatrix} \qquad \qquad \text{for example}, \vec x_i = \begin{bmatrix} \text{height}_i \\\\ \text{weight}_i \\\\ \text{shoe size}_i \\\\ \text{height}_i^2 \\\\ \cos\left( \text{height}_i \cdot \text{weight}_i \right) \end{bmatrix}
$$
</div>

This data is stored in the <span class="math-inline">\\(n \times (d+1)\\)</span> matrix <span class="math-inline">\\(X\\)</span>, called the **design matrix**, and observation vector <span class="math-inline">\\(\vec y\\)</span>.

<div class="math-display">
$$
X = \begin{bmatrix}
1 && x_1^{(1)} && x_1^{(2)} && \dots && x_1^{(d)} \\\\
1 && x_2^{(1)} && x_2^{(2)} && \dots && x_2^{(d)} \\\\
\vdots && \vdots && \vdots && \vdots && \vdots \\\\
1 && x_n^{(1)} && x_n^{(2)} && \dots && x_n^{(d)} \\\\
\end{bmatrix}
= \begin{bmatrix}
\text{Aug}(\vec x_1)^T \\\\
\text{Aug}(\vec x_2)^T \\\\
\vdots \\\\
\text{Aug}(\vec x_n)^T \\\\
\end{bmatrix}, \quad
\vec y = \begin{bmatrix}
y_1 \\\\
y_2 \\\\
\vdots \\\\
y_n
\end{bmatrix}
$$
</div>

Our goal is to find the optimal parameter vector, <span class="math-inline">\\(\vec w^{*}\\)</span>, which minimizes the mean squared error of our model's predictions on the training data.

<div class="math-display">
$$
\text{mean squared error} = \displaystyle R_\text{sq}(\vec w)=\frac{1}{n}||\vec y - X\vec w||^2
$$
</div>

The optimal <span class="math-inline">\\(\vec w^*\\)</span> satisfies the normal equation, <span class="math-inline">\\(X^TX \vec w = X^T \vec y\\)</span>. To make predictions:

-   <span class="math-inline">\\(\vec p = X\vec w^*\\)</span> is a vector containing the prediction for all <span class="math-inline">\\(n\\)</span> observations.

-   <span class="math-inline">\\(h(\vec x&#95;i)=\vec w^* \cdot \text{Aug}(\vec x&#95;i)\\)</span> is the prediction for any one observation <span class="math-inline">\\(\vec x&#95;i\\)</span>.

---

## Activity 1: Multiple Linear Regression

Let <span class="math-inline">\\(X\\)</span> be a **full rank** <span class="math-inline">\\(n \times 3\\)</span> design matrix and <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> be an observation vector. Suppose we have already fit a multiple linear regression model of the form

<div class="math-display">
$$
h(\vec x_i)=w_0+w_1x_i^{(1)}+w_2 x_i^{(2)}
$$
</div>

 Now, suppose we add the feature <span class="math-inline">\\((x&#95;i^{(1)}+x&#95;i^{(2)})\\)</span> to our design matrix and train a new model.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Which of the following are true about the new <span class="math-inline">\\(n \times 4\\)</span> design matrix <span class="math-inline">\\(X&#95;\text{new}\\)</span> with our added feature? Select all that apply.

<span class="mc-square" aria-hidden="true"></span> The columns of <span class="math-inline">\\(X&#95;\text{new}\\)</span> are linearly independent

<span class="mc-square" aria-hidden="true"></span> The columns of <span class="math-inline">\\(X&#95;\text{new}\\)</span> are linearly dependent

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\vec y\\)</span> is orthogonal to all the columns of <span class="math-inline">\\(X&#95;\text{new}\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\vec y\\)</span> is orthogonal to all the columns of the original design matrix <span class="math-inline">\\(X\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\text{colsp}(X)=\text{colsp}(X&#95;\text{new})\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(X&#95;\text{new}^TX&#95;\text{new}\\)</span> is invertible

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(X&#95;\text{new}^TX&#95;\text{new}\\)</span> is not invertible

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{nullsp}(X&#95;\text{new})\\)</span>. (This should be quick!)

</div>
</div>

</div>

---

## Activity 2: Chicken, Beef, or Fish?

Every week, Lauren goes to her local grocery store and buys exactly one pound of meat (either beef, fish, or chicken) but varying amounts of vegetables. We've collected a dataset containing the pounds of vegetables bought, the type of meat bought, and the total bill. Below we display the first few rows of the dataset and two plots generated using the entire (training) dataset.

<div style="text-align: center;">
<img src="imgs/lab08_act2.png" alt="image" style="width: 80%; max-width: 100%;">
</div>

In each part below, we provide you with a model that predicts `total` (her total grocery bill), fit to the dataset by minimizing mean squared error. For each model, determine whether **each optimal parameter <span class="math-inline">\\(w^*\\)</span> is positive, negative or exactly 0**. For example, in part (iv), you'll need to provide 3 answers: one for <span class="math-inline">\\(w&#95;0^*\\)</span>, one for <span class="math-inline">\\(w&#95;1^*\\)</span>, and one for <span class="math-inline">\\(w&#95;2^*\\)</span>.

1.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0\\)</span>

2.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{veg}&#95;i\\)</span>

3.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=chicken}&#95;i\\)</span> (one hot encoded feature for chicken)

4.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=beef}&#95;i+ w&#95;2 \cdot \text{meat=chicken}&#95;i\\)</span>

5.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=beef}&#95;i+ w&#95;2 \cdot \text{meat=chicken}&#95;i + w&#95;3 \cdot \text{meat=fish}&#95;i\\)</span>

---

## Activity 3: Gradients and Partial Derivatives

Suppose <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span>. Let <span class="math-inline">\\(g(\vec x)=(x&#95;1^2+x&#95;2-3)^2+(x&#95;1+x&#95;2^2-4)^2 + x&#95;3^2\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\nabla g(\vec x)\\)</span>. <em>Hint: Start by finding the partial derivatives of <span class="math-inline">\\(g\\)</span> with respect to <span class="math-inline">\\(x&#95;1\\)</span>, <span class="math-inline">\\(x&#95;2\\)</span>, and <span class="math-inline">\\(x&#95;3\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Evaluate <span class="math-inline">\\(\nabla g\left( \begin{bmatrix} 2 \\\\ 1 \\\\ 0 \end{bmatrix} \right)\\)</span>. The result is a vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. What does it mean?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Why is it guaranteed that <span class="math-inline">\\(g(\vec x)\\)</span> **has** a global minimum?

</div>
</div>

</div>

---

## Activity 4: The Big Three

In [Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/), we introduced three key gradient rules for vector-to-scalar functions.

-   **Dot product**: If <span class="math-inline">\\(f(\vec x) = \vec a \cdot \vec x\\)</span>, then <span class="math-inline">\\(\nabla f(\vec x) = \vec a\\)</span>.

-   **Squared norm**: If <span class="math-inline">\\(f(\vec x) = \lVert \vec x \rVert^2\\)</span>, then <span class="math-inline">\\(\nabla f(\vec x) = 2 \vec x\\)</span>.

-   **Quadratic form**: If <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span>, then <span class="math-inline">\\(\nabla f(\vec x) = (A + A^T) \vec x\\)</span>.

In each part below, assume <span class="math-inline">\\(\vec x, \vec a, \vec b \in \mathbb{R}^n\\)</span>, <span class="math-inline">\\(A \in \mathbb{R}^{n \times n}\\)</span>, and <span class="math-inline">\\(c \in \mathbb{R}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x + \vec b^T \vec x + c\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = \sum&#95;{i=1}^n x&#95;i\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = \lVert A \vec x \rVert^2\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>. <em>Hint: Use the fact that <span class="math-inline">\\(\lVert \vec v \rVert^2 = \vec v^T \vec v\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = \lVert \vec x \rVert\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = (\vec a \cdot \vec x)^2\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>.

<em>Hint: Expand <span class="math-inline">\\(f(\vec x)\\)</span> so that you can use one of the "big three" rules.</em>

</div>
</div>

</div>

---

## Activity 5: Quadratic Forms and Symmetry

Suppose <span class="math-inline">\\(f(\vec x) = \vec x^T \begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix} \vec x\\)</span>, where <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span>. (If you'd like, as an example, let <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 3 \\\\ 7 &amp; -8 \end{bmatrix}\\)</span>.)

1.  Expand <span class="math-inline">\\(f(\vec x)\\)</span> so that it doesn't involve matrices or vectors.

2.  Find <span class="math-inline">\\(\frac{\partial f}{\partial x&#95;1}\\)</span>, <span class="math-inline">\\(\frac{\partial f}{\partial x&#95;2}\\)</span>, and show that <span class="math-inline">\\(\nabla f(\vec x) = \begin{bmatrix} \frac{\partial f}{\partial x&#95;1} \\\\ \frac{\partial f}{\partial x&#95;2} \end{bmatrix}\\)</span> satisfies the quadratic form gradient rule.

3.  Discuss: Why do we typically assume that <span class="math-inline">\\(A\\)</span> is symmetric when defining a quadratic form?

{% endraw %}
