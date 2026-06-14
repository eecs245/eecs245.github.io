---
layout: page
title: "Lab 13: Singular Value Decomposition"
description: "Lab 13: Singular Value Decomposition activities."
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

# Lab 13: Singular Value Decomposition

**due** for completion at the end of your lab section

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: SVD Fundamentals](#activity-1-svd-fundamentals)
- [Activity 2: Outer Products](#activity-2-outer-products)
- [Activity 3: Rotating and Stretching](#activity-3-rotating-and-stretching)
- [Activity 4](#activity-4)

---

**Recap: Singular Value Decomposition** ([Chapters 10.1](https://notes.eecs245.org/singular-value-decomposition/computing-svd/) and [10.2](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation/))

-   Suppose <span class="math-inline">\\(X\\)</span> is any <span class="math-inline">\\(n \times d\\)</span> matrix. Then, there exists a **singular value decomposition (SVD)** of <span class="math-inline">\\(X\\)</span> of the form

<div class="math-display">
$$
X = U \Sigma V^T
$$
</div>

 where:

    | **Matrix** | **Shape** | **Values Come From** | **Properties** |
    |:---|:--:|:---|:---|
    | <span class="math-inline">\\(U\\)</span> | <span class="math-inline">\\(n \times n\\)</span> | Columns are eigenvectors of <span class="math-inline">\\(XX^T\\)</span>, called the **left singular vectors** of <span class="math-inline">\\(X\\)</span> | Orthogonal

<div class="math-display">
$$
U^TU = UU^T = I_{n \times n}
$$
</div>

 |
    | <span class="math-inline">\\(\Sigma\\)</span> | <span class="math-inline">\\(n \times d\\)</span> | Each **singular value** <span class="math-inline">\\(\sigma&#95;i\\)</span> is the square root of the <span class="math-inline">\\(i\\)</span>-th largest eigenvalue of <span class="math-inline">\\(X^TX\\)</span> (or <span class="math-inline">\\(XX^T\\)</span>) | Diagonal, with value in position <span class="math-inline">\\((i, i)\\)</span> equal to <span class="math-inline">\\(\sigma&#95;i\\)</span> for <span class="math-inline">\\(i=1,2,\dots,r = \text{rank}(X)\\)</span> |
    | <span class="math-inline">\\(V\\)</span> | <span class="math-inline">\\(d \times d\\)</span> | Columns are eigenvectors of <span class="math-inline">\\(X^TX\\)</span>, called the **right singular vectors** of <span class="math-inline">\\(X\\)</span> | Orthogonal

<div class="math-display">
$$
V^TV = VV^T = I_{d \times d}
$$
</div>

 |

-   If <span class="math-inline">\\(\vec u&#95;i\\)</span> and <span class="math-inline">\\(\vec v&#95;i\\)</span> are the <span class="math-inline">\\(i\\)</span>-th left and right singular vectors of <span class="math-inline">\\(X\\)</span>, respectively, then <span class="math-inline">\\(X\vec v&#95;i = \sigma&#95;i \vec u&#95;i\\)</span>.

---

## Activity 1: SVD Fundamentals

Suppose the matrix <span class="math-inline">\\(X\\)</span> has the singular value decomposition <span class="math-inline">\\(X=U\Sigma V^T\\)</span> where

<div class="math-display">
$$
U = \begin{bmatrix}0 & 1 \\\\ 1 & 0\end{bmatrix}, \quad \Sigma = \begin{bmatrix}\sigma_1 & 0 & 0 \\\\ 0 & 2 & 0 \end{bmatrix}, \quad V = \begin{bmatrix}1/\sqrt{2} & | & 0 \\\\ 0 & \vec v_2 & 1 \\\\ 1/\sqrt{2} & | & 0 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
How many rows and columns does <span class="math-inline">\\(X\\)</span> have? What is <span class="math-inline">\\(\text{rank}(X)\\)</span>?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(2 \times 3\\)</span> matrix, matching the dimensions of <span class="math-inline">\\(\Sigma\\)</span>. <span class="math-inline">\\(\text{rank}(X)\\)</span> is 2, since there are 2 non-zero singular values.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec v&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\vec v&#95;2\\)</span> is the eigenvector of <span class="math-inline">\\(X^TX\\)</span> corresponding to the eigenvalue 2. It's also a unit vector, meaning we need to find a unit vector that's orthogonal to the other two columns, so <span class="math-inline">\\(\vec v&#95;2 = \begin{bmatrix}\sqrt{2} / 2 \\\\ 0 \\\\ -\sqrt{2} / 2 \end{bmatrix}\\)</span>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Given that the first column of <span class="math-inline">\\(X\\)</span> and third column of <span class="math-inline">\\(X\\)</span> sum to <span class="math-inline">\\(\begin{bmatrix}0 \\\\ 5\end{bmatrix}\\)</span>, find <span class="math-inline">\\(\sigma&#95;1\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
X\vec v_1 &= \sigma_1 \vec u_1
\\\\X\begin{bmatrix}1/\sqrt{2} \\\\ 0 \\\\ 1/\sqrt{2}\end{bmatrix} &= \sigma_1 \begin{bmatrix}0 \\\\ 1\end{bmatrix}
\end{align*}
$$
</div>

The left side of the equation is the sum of <span class="math-inline">\\(X\\)</span>'s first and third columns, scaled by <span class="math-inline">\\(1 / \sqrt{2}\\)</span>, so we can use the fact given in the problem here:

<div class="math-display">
$$
\begin{align*}
\frac{1}{\sqrt{2}}\begin{bmatrix}0 \\\\ 5\end{bmatrix} &= \sigma_1\begin{bmatrix}0 \\\\ 1\end{bmatrix}
\\\\ \begin{bmatrix}0 \\\\ 5/\sqrt{2}\end{bmatrix} &= \begin{bmatrix}0 \\\\ \sigma_1\end{bmatrix}
\\\\ \sigma_1 &= \frac{5\sqrt{2}}{2}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 2: Outer Products

Consider the rank-<span class="math-inline">\\(2\\)</span> matrix <span class="math-inline">\\(X=\begin{bmatrix}1 &amp; 2 &amp; 2 \\\\ 1 &amp; 3 &amp; 3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Write <span class="math-inline">\\(X\\)</span> as a sum of two rank-1 outer products, e.g. <span class="math-inline">\\(X=\vec x&#95;1 \vec y&#95;1^T + \vec x&#95;2 \vec y&#95;2^T\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(X\\)</span> has a unique first column, while the second and third columns are the same. So, we can use a similar idea to the CR decomposition:

<div class="math-display">
$$
X = \begin{bmatrix}1 \\\\ 1\end{bmatrix}\begin{bmatrix}1 & 0 & 0\end{bmatrix} + \begin{bmatrix}2 \\\\ 3\end{bmatrix}\begin{bmatrix}0 & 1 & 1\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(XX^T\\)</span> and <span class="math-inline">\\(X^TX\\)</span>, and the trace and determinant of each. Feel free to use `numpy`.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
XX^T &= \begin{bmatrix}1 & 2 & 2 \\\\ 1 & 3 & 3\end{bmatrix} \begin{bmatrix} 1 & 1 \\\\ 2 & 3 \\\\ 2 & 3\end{bmatrix}
\\\\&=\begin{bmatrix}1 + 4 + 4 & 1 + 6 + 6 \\\\ 1 + 6 + 6 & 1 + 9 + 9\end{bmatrix}
\\\\&=\begin{bmatrix}9 & 13 \\\\ 13 & 19\end{bmatrix}
\\\\\text{det}(XX^T)&=9\cdot 19 - 13 \cdot 13 = 2
\\\\\text{trace}(XX^T)&=9 + 19 = 28
\end{align*}
$$
</div>

<div class="math-display">
$$
\begin{align*}
X^TX &= \begin{bmatrix} 1 & 1 \\\\ 2 & 3 \\\\ 2 & 3\end{bmatrix}\begin{bmatrix}1 & 2 & 2 \\\\ 1 & 3 & 3\end{bmatrix}
\\\\&=\begin{bmatrix}1 + 1 & 2 + 3 & 2 + 3 \\\\ 2 + 3 & 4 + 9 & 4 + 9 \\\\ 2 + 3 & 4 + 9 & 4 + 9\end{bmatrix}
\\\\&=\begin{bmatrix}2 & 5 & 5 \\\\ 5 & 13 & 13 \\\\ 5 & 13 & 13\end{bmatrix}
\\\\\text{det}(X^TX)&=0 \text{, } X^TX \text{ is not invertible}
\\\\\text{trace}(X^TX)&=2 + 13 + 13 = 28
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
If <span class="math-inline">\\(X\\)</span> is any <span class="math-inline">\\(n \times d\\)</span> matrix, which of the following are guaranteed to be true, and why? <em>Hint: How does the trace of a matrix relate to its eigenvalues? How are the eigenvalues of <span class="math-inline">\\(XX^T\\)</span> and <span class="math-inline">\\(X^TX\\)</span> related?</em>

<div class="math-display">
$$
\begin{align*}
\text{trace}(XX^T)&=\text{trace}(X^TX)
\\\\\text{det}(XX^T)&=\text{det}(X^TX)
\end{align*}
$$
</div>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(XX^T\\)</span> and <span class="math-inline">\\(X^TX\\)</span> share the same **non-zero** values. Since the trace is equivalent to the sum of the eigenvalues, the non-zero eigenvalues being the same results in the same sum, as the zero eigenvalues don't affect it.

However, the same is not true for the determinant. In the case where <span class="math-inline">\\(n \neq d\\)</span>, one of <span class="math-inline">\\(XX^T\\)</span> or <span class="math-inline">\\(X^TX\\)</span> will be larger. The larger matrix **must** have a zero eigenvalue because <span class="math-inline">\\(\text{rank}(XX^T) = \text{rank}(X^TX)\\)</span>, so its determinant will be 0. We can't guarantee that <span class="math-inline">\\(X^TX\\)</span> won't be full rank, so its possible for the determinant to not be 0.
</details>

</div>
</div>

</div>

---

## Activity 3: Rotating and Stretching

Suppose <span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(5 \times 2\\)</span> matrix with singular value decomposition <span class="math-inline">\\(X=U \Sigma V^T\\)</span>, and that <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> are the first and second columns of <span class="math-inline">\\(V\\)</span>, respectively. Furthermore, suppose <span class="math-inline">\\(\vec w \in \mathbb{R}^2\\)</span> is a vector such that

<div class="math-display">
$$
\vec w = 3\vec v_1 - \vec v_2
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(V^T\vec w\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
V^T\vec w &= V^T(3\vec v_1 - \vec v_2)
\\\\&= 3V^T\vec v_1 - V^T\vec v_2
\\\\&= 3\begin{bmatrix}\vec v_1 \cdot \vec v_1  \\\\ \vec v_2 \cdot \vec v_1\end{bmatrix} - \begin{bmatrix}\vec v_1 \cdot \vec v_2  \\\\ \vec v_2 \cdot \vec v_2\end{bmatrix}
\end{align*}
$$
</div>

We can simplify this further thanks to <span class="math-inline">\\(V\\)</span> being an orthogonal matrix. <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> are orthogonal, and their norms are both 1.

<div class="math-display">
$$
\begin{align*}
V^T\vec w3 &= \begin{bmatrix}||\vec v_1||^2  \\\\ 0\end{bmatrix} - \begin{bmatrix}0 \\\\ ||\vec v_2||^2 \end{bmatrix}
\\\\&=3\begin{bmatrix}1  \\\\ 0\end{bmatrix} - \begin{bmatrix}0 \\\\ 1 \end{bmatrix}
\\\\&=\begin{bmatrix}3  \\\\ -1\end{bmatrix}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(X\\)</span>'s two singular values are <span class="math-inline">\\(\sigma&#95;1 = 10\\)</span> and <span class="math-inline">\\(\sigma&#95;2 = 3\\)</span>. Find <span class="math-inline">\\(\Sigma V^T\vec w\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\Sigma V^T\vec w &= \Sigma \begin{bmatrix}3  \\\\ -1\end{bmatrix}
\\\\&= \begin{bmatrix}10 & 0 \\\\ 0 & 3 \\\\ 0 & 0 \\\\ 0 & 0 \\\\ 0 & 0 \end{bmatrix} \begin{bmatrix}3  \\\\ -1\end{bmatrix}
\\\\&= \begin{bmatrix}30 \\\\ -3 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(\vec z = \Sigma V^T\vec w\\)</span>. In English, what does <span class="math-inline">\\(\vec z\\)</span> represent, relative to <span class="math-inline">\\(\vec w\\)</span>?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(V^T\vec w\\)</span> rotates <span class="math-inline">\\(\vec w\\)</span> using the right singular vectors as the basis. Since <span class="math-inline">\\(\vec w\\)</span> is already composed of those vectors, it returns the coefficients back in a vector. <span class="math-inline">\\(\Sigma\\)</span> then shifts the resulting vector by scaling each component using the singular values.
</details>

**Recap: Principal Component Analysis** ([Chapters 10.3](https://notes.eecs245.org/singular-value-decomposition/best-direction/) and [10.4](https://notes.eecs245.org/singular-value-decomposition/principal-components-analysis/))

-   The goal of **principal component analysis (PCA)** is reducing the dimensionality of a dataset by constructing new features --- called **principal components**.

-   These new features are linear combinations of the existing features in the data, and are constructed to **minimize the mean squared orthogonal error** of the data when projected onto the new features.

-   As we see in Chapter 10.3, this is equivalent to finding the **directions along which the data is most spread out**.

    <img src="imgs/pca_notes_plot2.png" alt="image" style="width: 100%; max-width: 100%;">

   The plot on the left shows the direction vectors <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> which define the first and second principal components, respectively. <span class="math-inline">\\(\vec v&#95;1\\)</span> is the direction that captures the most variability, followed by <span class="math-inline">\\(\vec v&#95;2\\)</span>. Note that <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> are **orthogonal**, which results in the principal components (new features) being **uncorrelated**, as we see in the plot on the right.

-   The "PCA recipe" is as follows:

    1.  Starting with an <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(X\\)</span> of <span class="math-inline">\\(n\\)</span> data points in <span class="math-inline">\\(d\\)</span> dimensions and **mean-center** the data by subtracting the mean of each column from itself. The new matrix is <span class="math-inline">\\(\tilde X\\)</span>.

    2.  Compute the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>: <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span>.

    3.  **The columns of <span class="math-inline">\\(V\\)</span> (rows of <span class="math-inline">\\(V^T\\)</span>) describe the directions of maximal variance in the data!** For instance, the single "best direction" is the eigenvector of <span class="math-inline">\\(\tilde X \tilde X^T\\)</span> with the largest eigenvalue, i.e. <span class="math-inline">\\(\vec v&#95;1\\)</span> in <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span>.

       4.  Principal component (new feature) <span class="math-inline">\\(j\\)</span> comes from multiplying <span class="math-inline">\\(\tilde X\\)</span> by the <span class="math-inline">\\(j\\)</span>-th column of <span class="math-inline">\\(V\\)</span>.

<div class="math-display">
$$
\text{PC}_j = \tilde X \vec v_j = \sigma_j \vec u_j
$$
</div>

       5.  The variance of <span class="math-inline">\\(\text{PC}&#95;j\\)</span> is <span class="math-inline">\\(\frac{\sigma&#95;j^2}{n}\\)</span>. The proportion of total variance in <span class="math-inline">\\(\tilde X\\)</span> that is explained by <span class="math-inline">\\(\text{PC}&#95;j\\)</span> is

<div class="math-display">
$$
\text{proportion of variance explained by PC } j = \frac{\sigma_j^2}{\sum_{k=1}^r \sigma_k^2}
$$
</div>

</div>
</div>

</div>

---

## Activity 4

Suppose <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are each <span class="math-inline">\\(100 \times 2\\)</span> matrices, representing <span class="math-inline">\\(n=100\\)</span> points in <span class="math-inline">\\(\mathbb{R}^2\\)</span>. The three datasets are shown in the scatter plots below. (Matrix <span class="math-inline">\\(A\\)</span> is in Plot A, matrix <span class="math-inline">\\(B\\)</span> is in Plot B, and matrix <span class="math-inline">\\(C\\)</span> is in Plot C.)

<div style="text-align: center;">
<img src="imgs/pc-3-plots.png" alt="image" style="width: 100%; max-width: 100%;">
</div>

Assume that <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are each already mean-centered.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
If we applied PCA to each of the above datasets, and created just one principal component in each case, for which dataset would the first principal component have the smallest mean squared orthogonal error --- <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, or <span class="math-inline">\\(C\\)</span>?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(B\\)</span> has a strong negative correlation, with little spread in the perpendicular direction, while <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(C\\)</span>'s dominant directions aren't as clear.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\tilde{X}=U \Sigma V^T\\)</span> is the singular value decomposition of <span class="math-inline">\\(\tilde{X}\\)</span>, and that

<div class="math-display">
$$
\Sigma = \begin{bmatrix}16 & 0 \\\\ 0 & 4 \\\\ 0 & 0 \\\\ \vdots & \vdots \\\\ 0 & 0 \end{bmatrix}, \quad \underbrace{V = \begin{bmatrix} 2/\sqrt{5} & 1/\sqrt{5} \\\\ -1/\sqrt{5} & 2/\sqrt{5}\end{bmatrix}}_{\textbf{not } V^T}
$$
</div>

Which dataset is most likely to be <span class="math-inline">\\(\tilde{X}\\)</span> --- <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, or <span class="math-inline">\\(C\\)</span>?

<details markdown="1"><summary>Solution</summary>

The singular values tell us that one direction is being scaled by 16, while the other is scaled by 4, meaning most of the variance is captured in the <span class="math-inline">\\(\vec v&#95;1\\)</span> direction. <span class="math-inline">\\(\vec v&#95;1\\)</span> has a positive <span class="math-inline">\\(x\\)</span> component and a negative <span class="math-inline">\\(y\\)</span> component, which matches the slope of plot <span class="math-inline">\\(B\\)</span>'s dominant direction, since <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>'s dominant directions are more positive.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Again, suppose <span class="math-inline">\\(\tilde{X}=U \Sigma V^T\\)</span> is the singular value decomposition of <span class="math-inline">\\(\tilde{X}\\)</span>, and that

<div class="math-display">
$$
\Sigma = \begin{bmatrix}16 & 0 \\\\ 0 & 4 \\\\ 0 & 0 \\\\ \vdots & \vdots \\\\ 0 & 0 \end{bmatrix}, \quad \underbrace{V = \begin{bmatrix} 2/\sqrt{5} & 1/\sqrt{5} \\\\ -1/\sqrt{5} & 2/\sqrt{5}\end{bmatrix}}_{\textbf{not } V^T}
$$
</div>

What is the proportion of the total variance in <span class="math-inline">\\(\tilde{X}\\)</span> that is accounted for by the first principal component?

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\displaystyle \frac{\sigma_1^2}{\sigma_1^2 + \sigma_2^2} = \frac{16^2}{16^2 + 4^2} = \frac{256}{272}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Suppose that in the graph of principal component 2 vs. principal component 1 (i.e. with PC 1 on the <span class="math-inline">\\(x\\)</span>-axis and PC 2 on the <span class="math-inline">\\(y\\)</span>-axis), a particular data point is plotted at <span class="math-inline">\\((4, 2)\\)</span>. What is the corresponding point in the original (mean-centered) dataset? Your answer should be a tuple of two numbers, <span class="math-inline">\\((x, y)\\)</span> (or equivalently, a vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>). <em>Hint: Start by understanding the plot on Page 4.</em>

<details markdown="1"><summary>Solution</summary>

There are two ways to approach this problem:

**Option 1: Dot Products and Transformation**

In the PC2 vs PC1 plot in the recap, you may have noticed the coordinates of <span class="math-inline">\\(\vec x&#95;{12}\\)</span> were <span class="math-inline">\\((\vec x&#95;{12} \cdot \vec v&#95;1, \vec x&#95;{12} \cdot \vec v&#95;2)\\)</span>. This comes from multiplying <span class="math-inline">\\(V^T\vec x&#95;{12}\\)</span>:

<div class="math-display">
$$
\begin{align*}
V^T\vec x_{12} &= \begin{bmatrix} — & \vec v_1 & — \\\\ — & \vec v_2 & —\end{bmatrix}\vec x_{12}
\\\\&= \begin{bmatrix}  \vec v_1 \cdot \vec x_{12} \\\\ \vec v_2 \cdot \vec x_{12} \end{bmatrix}
\end{align*}
$$
</div>

If this looks familiar, that's because it's similar to 3c! In 3c, <span class="math-inline">\\(V^T\vec w\\)</span> rotated <span class="math-inline">\\(\vec w\\)</span> by translating it into a space with {<span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2\\)</span>} as its basis. So, if we know a point's coordinates in <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2\\)</span> space, we can work backwards to solve for the point's coordinates in <span class="math-inline">\\(x,y\\)</span> space:

<div class="math-display">
$$
\begin{align*}
\begin{bmatrix}4 \\\\ 2\end{bmatrix} &= \begin{bmatrix}\vec v_1 \cdot \vec w \\\\ \vec v_2 \cdot \vec w\end{bmatrix}
\\\\
\\\\ 4 &= \vec v_1 \cdot \vec w = \frac{2}{\sqrt{5}}w_1 + \frac{-1}{\sqrt{5}}w_2
\\\\ 2 &= \vec v_2 \cdot \vec w = \frac{1}{\sqrt{5}}w_1 + \frac{2}{\sqrt{5}}w_2
\end{align*}
$$
</div>

Now we have a system of equations to solve for the coordinate of <span class="math-inline">\\(\vec w\\)</span>:

<div class="math-display">
$$
\begin{align*}
4 &= \frac{2}{\sqrt{5}}w_1 + \frac{-1}{\sqrt{5}}w_2
\\\\2 &=\frac{1}{\sqrt{5}}w_1 + \frac{2}{\sqrt{5}}w_2
\\\\
\\\\8 &= \frac{4}{\sqrt{5}}w_1 + \frac{-2}{\sqrt{5}}w_2
\\\\8+2 &= \frac{4}{\sqrt{5}}w_1 + \frac{1}{\sqrt{5}}w_1 + \frac{-2}{\sqrt{5}}w_2 + \frac{2}{\sqrt{5}}w_2
\\\\10 &= \frac{5}{\sqrt{5}}w_1
\\\\w_1 &= \frac{10\sqrt{5}}{5} = 2\sqrt{5}
\\\\
\\\\4 &= \frac{2}{\sqrt{5}}(2\sqrt{5}) + \frac{-1}{\sqrt{5}}w_2
\\\\4 &= 4 + \frac{-1}{\sqrt{5}}w_2
\\\\w_2&=0
\\\\
\\\\ 2 &= \frac{1}{\sqrt{5}}(2\sqrt{5}) + \frac{2}{\sqrt{5}}w_2
\\\\ 2 &= 2 + \frac{2}{\sqrt{5}}w_2
\\\\ w_2 &= 0 \quad \checkmark
\\\\ \vec w &= \begin{bmatrix}2\sqrt{5} \\\\ 0\end{bmatrix}
\end{align*}
$$
</div>

**Option 2: Thinking in Terms of Linear Combinations**

<span class="math-inline">\\((4, 2)\\)</span> are coefficients in the basis <span class="math-inline">\\(\lbrace \vec v&#95;1, \vec v&#95;2\rbrace\\)</span>. Since we know <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span>'s directions in <span class="math-inline">\\(x,y\\)</span> space, getting the point's coordinates in <span class="math-inline">\\(x,y\\)</span> space just involves computing the linear combination, using the coordinates in <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2\\)</span> space as coefficients:

<div class="math-display">
$$
\begin{align*}
4 \vec v_1 + 2\vec v_2 &= 4\begin{bmatrix} 2/\sqrt{5} \\\\ -1/\sqrt{5} \end{bmatrix} + 2\begin{bmatrix} 1/\sqrt{5} \\\\ 2/\sqrt{5}\end{bmatrix}
\\\\&= \begin{bmatrix} 8/\sqrt{5} \\\\ -4/\sqrt{5} \end{bmatrix} + \begin{bmatrix} 2/\sqrt{5} \\\\ 4/\sqrt{5}\end{bmatrix}
\\\\&= \begin{bmatrix} 10/\sqrt{5} \\\\ 0 \end{bmatrix} = \begin{bmatrix} 2\sqrt{5} \\\\ 0 \end{bmatrix}
\end{align*}
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
