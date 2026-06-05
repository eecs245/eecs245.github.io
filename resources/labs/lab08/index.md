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
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab08/lab08-solutions.pdf" target="_blank">Solutions PDF ✅</a>
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

Our goal is to find the optimal parameter vector, <span class="math-inline">\\(\vec w^{\ast}\\)</span>, which minimizes the mean squared error of our model's predictions on the training data.

<div class="math-display">
$$
\text{mean squared error} = \displaystyle R_\text{sq}(\vec w)=\frac{1}{n}||\vec y - X\vec w||^2
$$
</div>

The optimal <span class="math-inline">\\(\vec w^{\ast}\\)</span> satisfies the normal equation, <span class="math-inline">\\(X^TX \vec w = X^T \vec y\\)</span>. To make predictions:

-   <span class="math-inline">\\(\vec p = X\vec w^{\ast}\\)</span> is a vector containing the prediction for all <span class="math-inline">\\(n\\)</span> observations.

-   <span class="math-inline">\\(h(\vec x&#95;i)=\vec w^{\ast} \cdot \text{Aug}(\vec x&#95;i)\\)</span> is the prediction for any one observation <span class="math-inline">\\(\vec x&#95;i\\)</span>.

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

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(X&#95;\text{new}^TX&#95;\text{new}\\)</span> is not invertible

Let's look at the correct options:

-   The columns of <span class="math-inline">\\(X&#95;\text{new}\\)</span> are linearly dependent because the new added column, consisting of values of the form <span class="math-inline">\\(x&#95;i^{(1)}+x&#95;i^{(2)}\\)</span>, is a linear combination of columns 1 and 2 of <span class="math-inline">\\(X\\)</span>. By definition, this means the columns of <span class="math-inline">\\(X&#95;\text{new}\\)</span> are linearly dependent.

-   The new added column does not change the set of possible linear combinations of the columns of <span class="math-inline">\\(X\\)</span>, since this added column was already in <span class="math-inline">\\(\text{colsp}(X)\\)</span>. Therefore, <span class="math-inline">\\(\text{colsp}(X)=\text{colsp}(X&#95;\text{new})\\)</span>.

-   <span class="math-inline">\\(X&#95;\text{new}^TX&#95;\text{new}\\)</span> is not a full rank matrix because <span class="math-inline">\\(X&#95;\text{new}\\)</span>'s columns aren't linearly independent, meaning <span class="math-inline">\\(\text{rank}(X&#95;\text{new}) &lt; 4\\)</span>, and <span class="math-inline">\\(\text{rank}(X&#95;\text{new}^TX&#95;\text{new}) = \text{rank}(X&#95;\text{new})\\)</span>, so <span class="math-inline">\\(\text{rank}(X&#95;\text{new}^TX&#95;\text{new}) &lt; 4\\)</span>, meaning <span class="math-inline">\\(X&#95;\text{new}^TX&#95;\text{new}\\)</span> is not invertible.

Note that <span class="math-inline">\\(\vec y\\)</span> has no orthogonality relationship to the columns of <span class="math-inline">\\(X\\)</span> or <span class="math-inline">\\(X&#95;\text{new}\\)</span>. Instead, it's the case that the error vector, <span class="math-inline">\\(\vec e = \vec y - X \vec w^{\ast}\\)</span>, is orthogonal to the columns of both <span class="math-inline">\\(X\\)</span> and <span class="math-inline">\\(X&#95;\text{new}\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{nullsp}(X&#95;\text{new})\\)</span>. (This should be quick!)

<details markdown="1"><summary>Solution</summary>

Let's look at <span class="math-inline">\\(X&#95;\text{new}\\)</span>:

<div class="math-display">
$$
X_\text{new} = \begin{bmatrix} | & | & | & | \\\\ \vec{1} & \vec x^{(1)} & \vec x^{(2)} & \vec x^{(1)} + \vec x^{(2)} \\\\ | & | & | & | \end{bmatrix}
$$
</div>

 By construction, the fourth column of <span class="math-inline">\\(X&#95;\text{new}\\)</span> is the sum of <span class="math-inline">\\(\vec x^{(1)}\\)</span> and <span class="math-inline">\\(\vec x^{(2)}\\)</span>. So, multiplying <span class="math-inline">\\(X&#95;\text{new}\\)</span> by <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ -1 \end{bmatrix}\\)</span> --- or any scalar multiple of it --- will give the zero vector!

<div class="math-display">
$$
X_\text{new} \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ -1 \end{bmatrix} = \begin{bmatrix} | & | & | & | \\\\ \vec{1} & \vec x^{(1)} & \vec x^{(2)} & \vec x^{(1)} + \vec x^{(2)} \\\\ | & | & | & | \end{bmatrix} \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ -1 \end{bmatrix} = \vec x^{(1)} + \vec x^{(2)} - (\vec x^{(1)} + \vec x^{(2)}) = \vec 0
$$
</div>

 Since <span class="math-inline">\\(\text{rank}(X) = 3\\)</span> (because we were told the original design matrix <span class="math-inline">\\(X\\)</span> was full rank), <span class="math-inline">\\(\text{rank}(X&#95;\text{new}) = 3\\)</span> also, meaning <span class="math-inline">\\(\text{nullsp}(X&#95;\text{new})\\)</span> is 1-dimensional (from the rank-nullity theorem). So, this vector we've found is a basis for <span class="math-inline">\\(\text{nullsp}(X&#95;\text{new})\\)</span>.

<div class="math-display">
$$
\boxed{\text{nullsp}(X_\text{new}) = \text{span}\left(\left\{\begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ -1 \end{bmatrix}\right\}\right)}
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 2: Chicken, Beef, or Fish?

Every week, Lauren goes to her local grocery store and buys exactly one pound of meat (either beef, fish, or chicken) but varying amounts of vegetables. We've collected a dataset containing the pounds of vegetables bought, the type of meat bought, and the total bill. Below we display the first few rows of the dataset and two plots generated using the entire (training) dataset.

<div style="text-align: center;">
<img src="imgs/lab08_act2.png" alt="image" style="width: 80%; max-width: 100%;">
</div>

In each part below, we provide you with a model that predicts `total` (her total grocery bill), fit to the dataset by minimizing mean squared error. For each model, determine whether **each optimal parameter <span class="math-inline">\\(w^{\ast}\\)</span> is positive, negative or exactly 0**. For example, in part (iv), you'll need to provide 3 answers: one for <span class="math-inline">\\(w&#95;0^{\ast}\\)</span>, one for <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>, and one for <span class="math-inline">\\(w&#95;2^{\ast}\\)</span>.

1.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0\\)</span>

2.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{veg}&#95;i\\)</span>

3.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=chicken}&#95;i\\)</span> (one hot encoded feature for chicken)

4.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=beef}&#95;i+ w&#95;2 \cdot \text{meat=chicken}&#95;i\\)</span>

5.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=beef}&#95;i+ w&#95;2 \cdot \text{meat=chicken}&#95;i + w&#95;3 \cdot \text{meat=fish}&#95;i\\)</span>

<details markdown="1"><summary>Solution</summary>

1.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0\\)</span>

   This is the constant model. Since we're minimizing mean squared error, <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> is the mean of all total bills in the dataset, which we can tell from the scatter plot is positive.

   <span class="math-inline">\\(w&#95;0^{\ast}=\boxed{\text{positive}}\\)</span>

2.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{veg}&#95;i\\)</span>

   <span class="math-inline">\\(w&#95;0\\)</span> is the intercept and <span class="math-inline">\\(w&#95;1\\)</span> corresponds to pounds of vegetables. As vegetable purchases increase, the total bill increases, so <span class="math-inline">\\(w&#95;1&gt;0\\)</span>. The intercept looks positive as well, though this is a little less clear, admittedly.

   <span class="math-inline">\\(w&#95;0^{\ast}=\boxed{\text{positive}}\\)</span>, <span class="math-inline">\\(w&#95;1^{\ast}=\boxed{\text{positive}}\\)</span>

3.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=chicken}&#95;i\\)</span>

   Let's think in terms of two cases: Lauren buys chicken, and Lauren doesn't buy chicken.

-   Lauren buys chicken: <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1\\)</span>

-   Lauren doesn't buy chicken: <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0\\)</span>

   Since we're picking <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> so that they minimize mean squared error, <span class="math-inline">\\(w&#95;0^{\ast} + w&#95;1^{\ast}\\)</span> should be the average total bill for purchases involving chicken, and <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> should be the average total bill for purchases not involving chicken. Meaning,



<div class="math-display">
$$
w_1^* = \text{mean(chicken)} - \text{mean(no chicken)}
$$
</div>

   Both averages are positive, so <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> is positive. But, purchases involving chicken tend to be cheaper than purchases not involving chicken (as is evident in the third box plot), so <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> is negative.

   <span class="math-inline">\\(w&#95;0^{\ast}=\boxed{\text{positive}}\\)</span>, <span class="math-inline">\\(w&#95;1^{\ast}=\boxed{\text{negative}}\\)</span>

4.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=beef}&#95;i+ w&#95;2 \cdot \text{meat=chicken}&#95;i\\)</span>

   Following similar logic to the previous part, <span class="math-inline">\\(w&#95;0\\)</span> is the mean total for the reference group (fish), <span class="math-inline">\\(w&#95;1\\)</span> is the difference between the mean of beef and the mean of fish, <span class="math-inline">\\(w&#95;2\\)</span> is the difference between the mean of chicken and the mean of fish.

   <span class="math-inline">\\(w&#95;0^{\ast}=\boxed{\text{positive}}\\)</span>

   <span class="math-inline">\\(w&#95;1^{\ast}=\boxed{\text{negative}}\\)</span> (beef purchases tend to be less expensive than fish purchases)

   <span class="math-inline">\\(w&#95;2^{\ast}=\boxed{\text{negative}}\\)</span> (chicken purchases tend to be less expensive than fish purchases)

5.  <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1 \cdot \text{meat=beef}&#95;i+ w&#95;2 \cdot \text{meat=chicken}&#95;i + w&#95;3 \cdot \text{meat=fish}&#95;i\\)</span>

   This model has a parameter for each meat and an intercept, but since the sum of one hot encoded features for meat is always one, the design matrix is not full rank. Therefore, the optimal solution is not unique, and there are infinitely many optimal parameter vectors <span class="math-inline">\\(\vec w^{\ast}\\)</span> that minimize mean squared error.

   <span class="math-inline">\\(w&#95;0^{\ast}=\boxed{\text{N/A}}\\)</span> <span class="math-inline">\\(w&#95;1^{\ast}=\boxed{\text{N/A}}\\)</span> <span class="math-inline">\\(w&#95;2^{\ast}=\boxed{\text{N/A}}\\)</span> <span class="math-inline">\\(w&#95;3^{\ast}=\boxed{\text{N/A}}\\)</span>

   For example, <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 2 \\\\ 1 \\\\ 2 \\\\ 3 \end{bmatrix}\\)</span> both yield the same predictions. (Don't believe me? Write out all three cases for both <span class="math-inline">\\(\vec w^{\ast}\\)</span> vectors and see for yourself.)

</details>

---

## Activity 3: Gradients and Partial Derivatives

Suppose <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span>. Let <span class="math-inline">\\(g(\vec x)=(x&#95;1^2+x&#95;2-3)^2+(x&#95;1+x&#95;2^2-4)^2 + x&#95;3^2\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\nabla g(\vec x)\\)</span>. <em>Hint: Start by finding the partial derivatives of <span class="math-inline">\\(g\\)</span> with respect to <span class="math-inline">\\(x&#95;1\\)</span>, <span class="math-inline">\\(x&#95;2\\)</span>, and <span class="math-inline">\\(x&#95;3\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

Let's start by finding the partial derivatives of <span class="math-inline">\\(g\\)</span> with respect to <span class="math-inline">\\(x&#95;1\\)</span>, <span class="math-inline">\\(x&#95;2\\)</span>, and <span class="math-inline">\\(x&#95;3\\)</span>. We'll need to make heavy use of the (regular, scalar-to-scalar) chain rule.

<div class="math-display">
$$
\frac{\partial g}{\partial x_1} = 2(x_1^2+x_2-3)(2x_1) + 2(x_1+x_2^2-4)(1) = 4x_1 (x_1^2+x_2-3) + 2(x_1+x_2^2-4)
$$
</div>



<div class="math-display">
$$
\frac{\partial g}{\partial x_2} = 2(x_1^2+x_2-3) + 4x_2(x_1+x_2^2-4) \: \text{(notice the symmetry with the first case)}
$$
</div>



<div class="math-display">
$$
\frac{\partial g}{\partial x_3} = 2x_3
$$
</div>

So,

<div class="math-display">
$$
\boxed{\nabla g(\vec x) = \begin{bmatrix} 4x_1 (x_1^2+x_2-3) + 2(x_1+x_2^2-4) \\\\ 2(x_1^2+x_2-3) + 4x_2(x_1+x_2^2-4) \\\\ 2x_3 \end{bmatrix}}
$$
</div>

No need to simplify the expression any further --- doing so won't make it any easier to evaluate at a specific point.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Evaluate <span class="math-inline">\\(\nabla g\left( \begin{bmatrix} 2 \\\\ 1 \\\\ 0 \end{bmatrix} \right)\\)</span>. The result is a vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. What does it mean?

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\nabla g(\vec x) = \begin{bmatrix} 4x_1 (x_1^2+x_2-3) + 2(x_1+x_2^2-4) \\\\ 2(x_1^2+x_2-3) + 4x_2(x_1+x_2^2-4) \\\\ 2x_3 \end{bmatrix}
$$
</div>

Notice the shared terms of <span class="math-inline">\\(x&#95;1^2 + x&#95;2 - 3\\)</span> and <span class="math-inline">\\(x&#95;1 + x&#95;2^2 - 4\\)</span> in the first and second components. To make the computation of the gradient at <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> easier, let's compute these values first.

<div class="math-display">
$$
x_1^2 + x_2 - 3 = 2^2 + 1 - 3 = 2, \quad x_1 + x_2^2 - 4 = 2 + 1^2 - 4 = -1
$$
</div>

Then,

<div class="math-display">
$$
\boxed{\nabla g\left( \begin{bmatrix} 2 \\\\ 1 \\\\ 0 \end{bmatrix} \right) = \begin{bmatrix} 4x_1(x_1^2+x_2-3) + 2(x_1+x_2^2-4) \\\\ 2(x_1^2+x_2-3) + 4x_2(x_1+x_2^2-4) \\\\ 2x_3 \end{bmatrix} = \begin{bmatrix} 4(2)(2) + 2(-1) \\\\ 2(2) + 4(1)(-1) \\\\ 0 \end{bmatrix} = \begin{bmatrix} 14 \\\\ 0 \\\\ 0 \end{bmatrix}}
$$
</div>

The vector <span class="math-inline">\\(\begin{bmatrix} 14 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> describes the direction of steepest ascent at the point <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Why is it guaranteed that <span class="math-inline">\\(g(\vec x)\\)</span> **has** a global minimum?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(g(\vec x) = (x&#95;1^2 + x&#95;2 - 3)^2 + (x&#95;1 + x&#95;2^2 - 4)^2 + x&#95;3^2\\)</span> is a sum of three squares, each of which is <span class="math-inline">\\(\geq 0\\)</span>. So, knowing nothing else about what is being squared, we know that <span class="math-inline">\\(g(\vec x) \geq 0\\)</span> for all <span class="math-inline">\\(\vec x\\)</span>, and so <span class="math-inline">\\(g(\vec x)\\)</span> has a global minimum of **something**, whether it's 0 or some positive number.

</details>

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

<details markdown="1"><summary>Solution</summary>

The key idea is that the gradient of a sum is a sum of the gradients of the terms, just like with standard derivatives.

<div class="math-display">
$$
\nabla f(\vec x) = \nabla (\vec x^T A \vec x + \vec b^T \vec x + c) = \nabla (\vec x^T A \vec x) + \nabla (\vec b^T \vec x) + \nabla (c) = (A + A^T) \vec x + \vec b
$$
</div>

Therefore,

<div class="math-display">
$$
\boxed{\nabla f(\vec x) = (A + A^T) \vec x + \vec b}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = \sum&#95;{i=1}^n x&#95;i\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Remember that the sum of a vector's components is the same as the dot product of that vector with the vector of all 1's:

<div class="math-display">
$$
f(\vec x) = \sum_{i=1}^n x_i = \vec x \cdot \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix}
$$
</div>

So,

<div class="math-display">
$$
\boxed{\nabla f(\vec x) = \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = \lVert A \vec x \rVert^2\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>. <em>Hint: Use the fact that <span class="math-inline">\\(\lVert \vec v \rVert^2 = \vec v^T \vec v\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

Let's start by expanding <span class="math-inline">\\(\lVert A \vec x \rVert^2\\)</span>:

<div class="math-display">
$$
\begin{align*}
f(\vec x) &= \lVert A \vec x \rVert^2 \\\\
&= (A \vec x)^T (A \vec x) \\\\
&= \vec x^T A^T A \vec x \\\\
&= \vec x^T (A^TA) \vec x
\end{align*}
$$
</div>

<span class="math-inline">\\(f(\vec x)\\)</span> is a quadratic form, with the matrix <span class="math-inline">\\(A^TA\\)</span>. So,

<div class="math-display">
$$
\boxed{\nabla f(\vec x) = (A^TA + (A^TA)^T) \vec x = 2A^TA \vec x}
$$
</div>

Note that <span class="math-inline">\\(A^TA\\)</span> is symmetric, since <span class="math-inline">\\((A^TA)^T = A^TA\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = \lVert \vec x \rVert\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\boxed{\nabla f(\vec x) = \frac{\vec x}{\lVert \vec x \rVert}}
$$
</div>

For the derivation, see the [Norm and Chain Rule example in Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#example-norm-and-chain-rule).

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Given <span class="math-inline">\\(f(\vec x) = (\vec a \cdot \vec x)^2\\)</span>, find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>.

<em>Hint: Expand <span class="math-inline">\\(f(\vec x)\\)</span> so that you can use one of the "big three" rules.</em>

<details markdown="1"><summary>Solution</summary>

Let's follow the hint.

<div class="math-display">
$$
\begin{align*}
f(\vec x) &= (\vec a \cdot \vec x)^2
\\\\ &= (\vec a^T \vec x)^2
\\\\ &= (\vec x^T \vec a)(\vec a^T \vec x)
\\\\ &= \vec x^T (\vec a \vec a^T) \vec x
\end{align*}
$$
</div>

<span class="math-inline">\\(f(\vec x)\\)</span> is a quadratic form too, with the matrix <span class="math-inline">\\(\vec a \vec a^T\\)</span>. This is a symmetric matrix (<span class="math-inline">\\(\vec a \vec a^T = (\vec a \vec a^T)^T\\)</span>). So,

<div class="math-display">
$$
\boxed{\nabla f(\vec x) = 2(\vec a \vec a^T) \vec x = 2 \vec a (\vec a^T \vec x) = 2 (\vec a \cdot \vec x) \vec a}
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 5: Quadratic Forms and Symmetry

Suppose <span class="math-inline">\\(f(\vec x) = \vec x^T \begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix} \vec x\\)</span>, where <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span>. (If you'd like, as an example, let <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 3 \\\\ 7 &amp; -8 \end{bmatrix}\\)</span>.)

1.  Expand <span class="math-inline">\\(f(\vec x)\\)</span> so that it doesn't involve matrices or vectors.

2.  Find <span class="math-inline">\\(\frac{\partial f}{\partial x&#95;1}\\)</span>, <span class="math-inline">\\(\frac{\partial f}{\partial x&#95;2}\\)</span>, and show that <span class="math-inline">\\(\nabla f(\vec x) = \begin{bmatrix} \frac{\partial f}{\partial x&#95;1} \\\\ \frac{\partial f}{\partial x&#95;2} \end{bmatrix}\\)</span> satisfies the quadratic form gradient rule.

3.  Discuss: Why do we typically assume that <span class="math-inline">\\(A\\)</span> is symmetric when defining a quadratic form?

<details markdown="1"><summary>Solution</summary>

This problem is the same as the [Quadratic Forms example in Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#example-quadratic-forms).

</details>

{% endraw %}
