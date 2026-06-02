---
layout: page
title: "Lab 7: Inverses and Projections"
description: "Lab 7: Inverses and Projections activities."
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

# Lab 7: Inverses and Projections

**due** for completion at 11:59PM Ann Arbor Time on Monday, June 1st, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab07/lab07.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab07/lab07-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).
</div>

---

## Activities

- [Activity 1: PrairieLearn Practice Problems](#activity-1-prairielearn-practice-problems)
- [Activity 2: Linear Transformations](#activity-2-linear-transformations)
- [Activity 3: Projecting onto the Column Space](#activity-3-projecting-onto-the-column-space)

---

## Recap: Inverses ([Chapter 6.2](https://notes.eecs245.org/linear-transformations-and-projections/inverses/)) and Linear Transformations ([Chapter 6.1](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/))

(We provide a recap of projections and the normal equation in Activity 3.)

-   An <span class="math-inline">\\(n \times n\\)</span> square matrix <span class="math-inline">\\(A\\)</span> is **invertible** if and only if <span class="math-inline">\\(\text{rank}(A) = n\\)</span>, which also means that <span class="math-inline">\\(A\\)</span>'s columns are linearly independent (along with several other equivalent conditions).

-   If <span class="math-inline">\\(A\\)</span> is invertible, then its **inverse** <span class="math-inline">\\(A^{-1}\\)</span> is the **unique** <span class="math-inline">\\(n \times n\\)</span> matrix such that <span class="math-inline">\\(AA^{-1}=I=A^{-1}A\\)</span>.

-   The determinant of a square matrix <span class="math-inline">\\(A\\)</span> is the volume of the <span class="math-inline">\\(n\\)</span>-dimensional cube with side length 1 after it is transformed by <span class="math-inline">\\(A\\)</span>.

-   If <span class="math-inline">\\(\text{det}(A) = 0\\)</span>, then <span class="math-inline">\\(A\\)</span> is not invertible.

-   If <span class="math-inline">\\(A = \begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span>, then <span class="math-inline">\\(\text{det}(A) = ad - bc\\)</span> and <span class="math-inline">\\(A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d &amp; -b \\\\ -c &amp; a \end{bmatrix}\\)</span>.

-   The determinant satisfies several properties, including that <span class="math-inline">\\(\text{det}(AB) = \text{det}(A) \text{det}(B)\\)</span> and <span class="math-inline">\\(\text{det}(A^T) = \text{det}(A)\\)</span>.

-   A linear transformation is a function <span class="math-inline">\\(\mathbb{R}^d \to \mathbb{R}^n\\)</span> such that

<div class="math-display">
$$
f(\vec x + \vec y) = f(\vec x) + f(\vec y), \qquad f(c \vec x) = c f(\vec x)
$$
</div>

-   Every linear transformation has a corresponding <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(A\\)</span> where <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span>.

-   If <span class="math-inline">\\(A\\)</span> is square, then <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span> is a function from <span class="math-inline">\\(\mathbb{R}^n\\)</span> to <span class="math-inline">\\(\mathbb{R}^n\\)</span>, and <span class="math-inline">\\(A\\)</span> is invertible if and only if the function <span class="math-inline">\\(f\\)</span> is invertible.

---

## Activity 1: PrairieLearn Practice Problems

We're testing out a new website for practicing linear algebra problems: PrairieLearn.

Click [**this link**](https://us.prairielearn.com/pl/course_instance/217357) to access the relevant problems for this activity. It consists of 6 problems, each worth 1 point. The numbers in the problems are randomized; everyone will receive slightly different problems.

To get credit for Activity 1, you must **eventually** correctly answer all 6 problems, earning a score of 6/6. If you answer a problem incorrectly, click "New Variant" to generate a new version and then try again. There is no penalty for answering a problem incorrectly, as long as you eventually get it correct.

To be clear, you don't need to include anything in your PDF for Activity 1; we will manually verify that you've finished all 6 problems.

If you have trouble accessing PrairieLearn, message Suraj on Slack.

---

## Activity 2: Linear Transformations

Suppose <span class="math-inline">\\(f: \mathbb{R}^3 \to \mathbb{R}^3\\)</span> is a linear transformation represented by the matrix <span class="math-inline">\\(A\\)</span>.

Furthermore, suppose that <span class="math-inline">\\(f\left(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\right) = \begin{bmatrix} 0 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>, <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 10 \\\\ 0 \end{bmatrix}\right) = \begin{bmatrix} 0 \\\\ 4 \\\\ -3 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\right) = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(f\left(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\right)\\)</span>. **After that**, find the matrix <span class="math-inline">\\(A\\)</span> corresponding to <span class="math-inline">\\(f\\)</span>, i.e. where <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span>.

<details markdown="1"><summary>Solution</summary>

First, using just the properties of linear transformations, we can find <span class="math-inline">\\(f\left(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\right)\\)</span>. Recall that a linear transformation <span class="math-inline">\\(f\\)</span> satisfies

-   <span class="math-inline">\\(f(\vec x + \vec y) = f(\vec x) + f(\vec y)\\)</span>

-   <span class="math-inline">\\(f(c \vec x) = c f(\vec x)\\)</span>

In other words, <span class="math-inline">\\(f\\)</span> preserves linear combinations, i.e. <span class="math-inline">\\(f(a \vec x + b \vec y) = a f(\vec x) + b f(\vec y)\\)</span>.

Let's decompose <span class="math-inline">\\(f\left(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\right)\\)</span> into a linear combination of outputs we already know.

<div class="math-display">
$$
\begin{align*}
f\left(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\right)
&= f\left(2 \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix} + \frac{1}{10} \begin{bmatrix} 0 \\\\ 10 \\\\ 0 \end{bmatrix} + 2 \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\right) \\\\
&= \underbrace{2 f\left(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\right)
+ \frac{1}{10} f\left(\begin{bmatrix} 0 \\\\ 10 \\\\ 0 \end{bmatrix}\right)
+ 2 f\left(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\right)}_\text{property of linear transformations} \\\\
&= 2 \begin{bmatrix} 0 \\\\ 3 \\\\ 4 \end{bmatrix} + \frac{1}{10} \begin{bmatrix} 0 \\\\ 4 \\\\ -3 \end{bmatrix} + 2 \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix} \\\\
&= \begin{bmatrix} 0 \\\\ 6 \\\\ 8 \end{bmatrix} + \begin{bmatrix} 0 \\\\ 4 / 10 \\\\ -3 / 10 \end{bmatrix} + \begin{bmatrix} 2 \\\\ 0 \\\\ 0 \end{bmatrix} \\\\
&= \begin{bmatrix} 2 \\\\ 6.4 \\\\ 7.7 \end{bmatrix}
\end{align*}
$$
</div>

So, <span class="math-inline">\\(f\left(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\right) = \begin{bmatrix} 2 \\\\ 6.4 \\\\ 7.7 \end{bmatrix}\\)</span>.

Next, we need to find the matrix <span class="math-inline">\\(A\\)</span> corresponding to <span class="math-inline">\\(f\\)</span>, i.e. where <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span>. Since <span class="math-inline">\\(f\\)</span> is a linear transformation, we know that <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span> for some matrix <span class="math-inline">\\(A\\)</span>.

-   The first column of <span class="math-inline">\\(A\\)</span> is given by <span class="math-inline">\\(f\left(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\right)\\)</span>, which we're told is <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>.

-   The second column of <span class="math-inline">\\(A\\)</span> is given by <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\right)\\)</span>, which we've computed above to be <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 4/10 \\\\ -3/10 \end{bmatrix}\\)</span>.

-   The third column of <span class="math-inline">\\(A\\)</span> is given by <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\right)\\)</span>, which we're told is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>.

So,

<div class="math-display">
$$
A = \begin{bmatrix} 0 & 0 & 1 \\\\ 3 & 4 / 10 & 0 \\\\ 4 & -3 / 10 & 0 \end{bmatrix}
$$
</div>

If that seems too simple to be true, you can verify that multiplying <span class="math-inline">\\(A\\)</span> by <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\\)</span> gives us <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 6.4 \\\\ 7.7 \end{bmatrix}\\)</span>, and that multiplying <span class="math-inline">\\(A\\)</span> by the three vectors in the question give the outputs we're told. Remember that <span class="math-inline">\\(A \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> returns just the first column of <span class="math-inline">\\(A\\)</span>, and so on.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a **diagonal** matrix <span class="math-inline">\\(D\\)</span> and an **orthogonal** matrix <span class="math-inline">\\(Q\\)</span> such that <span class="math-inline">\\(A = QD\\)</span>. (Not every matrix can be written in this form, but this particular <span class="math-inline">\\(A\\)</span> can.) Then, describe **in English** how <span class="math-inline">\\(f\\)</span> transforms a vector <span class="math-inline">\\(\vec x\\)</span>.

<details markdown="1"><summary>Solution</summary>

Remember that

-   Diagonal matrices have 0s everywhere except on the diagonal, and have the effect of stretching/compressing each axis/dimension of the input vector independently.

-   Orthogonal matrices have columns that are orthonormal, meaning their columns are unit vectors that are orthogonal to one another.

In

<div class="math-display">
$$
A = \begin{bmatrix} 0 & 0 & 1 \\\\ 3 & 4 / 10 & 0 \\\\ 4 & -3 / 10 & 0 \end{bmatrix}
$$
</div>

You might notice that <span class="math-inline">\\(A\\)</span>'s first column is 5 times <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 3/5 \\\\ 4/5 \end{bmatrix}\\)</span>, which is a unit vector. You might also notice that <span class="math-inline">\\(A\\)</span>'s second column is <span class="math-inline">\\((1/2)\\)</span> times <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 4/5 \\\\ -3/5 \end{bmatrix}\\)</span>, which is another unit vector orthogonal to the first column. And finally, <span class="math-inline">\\(A\\)</span>'s third column is already a unit vector, and its orthogonal to the first two columns.

So, if we put these orthogonal unit vectors into the columns of <span class="math-inline">\\(Q\\)</span>, and the scaling factors of <span class="math-inline">\\(5\\)</span>, <span class="math-inline">\\(1/2\\)</span>, and <span class="math-inline">\\(1\\)</span> into the diagonal of <span class="math-inline">\\(D\\)</span>, we have

<div class="math-display">
$$
A = \begin{bmatrix} 0 & 0 & 1 \\\\ 3 & 4 / 10 & 0 \\\\ 4 & -3 / 10 & 0 \end{bmatrix} = \underbrace{\begin{bmatrix} 0 & 0 & 1 \\\\ 3/5 & 4/5 & 0 \\\\ 4/5 & -3/5 & 0 \end{bmatrix}}_Q \underbrace{\begin{bmatrix} 5 & 0 & 0 \\\\ 0 & 1 / 2 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}}_D
$$
</div>

So, <span class="math-inline">\\(Q = \begin{bmatrix} 0 &amp; 0 &amp; 1 \\\\ 3/5 &amp; 4/5 &amp; 0 \\\\ 4/5 &amp; -3/5 &amp; 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(D = \begin{bmatrix} 5 &amp; 0 &amp; 0 \\\\ 0 &amp; 1 / 2 &amp; 0 \\\\ 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

<span class="math-inline">\\(f(\vec x) = QD \vec x\\)</span> transforms <span class="math-inline">\\(f\\)</span> by first scaling <span class="math-inline">\\(\vec x\\)</span>'s first component by 5, second component by 1/2, and leaving the third component as-is, and then rotating it by the orthogonal matrix <span class="math-inline">\\(Q\\)</span>.

Orthogonal matrices rotate the vectors that they're multiplied by. In <span class="math-inline">\\(\mathbb{R}^2\\)</span>, this is a rotation by some angle <span class="math-inline">\\(\theta\\)</span>. It's harder to describe rotations in <span class="math-inline">\\(\mathbb{R}^3\\)</span> and beyond, but the key property that describes the effect of an orthogonal matrix <span class="math-inline">\\(Q\\)</span> is that for any vector <span class="math-inline">\\(\vec x\\)</span>,

<div class="math-display">
$$
\lVert Q \vec x \rVert = \lVert \vec x \rVert
$$
</div>

as you proved in Homework 6, meaning that all an orthogonal matrix is doing is changing the angle of the vector, not its length.

So, <span class="math-inline">\\(f(\vec x)\\)</span> first scales <span class="math-inline">\\(\vec x\\)</span>'s components, and then rotates the resulting vector.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Using your <span class="math-inline">\\(A = QD\\)</span> decomposition from part **b)**, find <span class="math-inline">\\(A^{-1}\\)</span>.

<em>Hint: Recall that for orthogonal matrices, <span class="math-inline">\\(QQ^T = Q^TQ = I\\)</span>. And, for any invertible matrices <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, <span class="math-inline">\\((AB)^{-1} = B^{-1}A^{-1}\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(A = QD\\)</span>, we have

<div class="math-display">
$$
A^{-1} = D^{-1}Q^{-1}
$$
</div>

Since <span class="math-inline">\\(D\\)</span> is diagonal, its inverse is just the diagonal matrix with the reciprocal of each diagonal entry. This corresponds to "unstretching" the vector in each dimension. So,

<div class="math-display">
$$
D^{-1} = \begin{bmatrix} 1 / 5 & 0 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}
$$
</div>

And, since <span class="math-inline">\\(Q\\)</span> is orthogonal, we know <span class="math-inline">\\(Q^TQ = I\\)</span>, meaning that <span class="math-inline">\\(Q^{-1} = Q^T\\)</span>, i.e. <span class="math-inline">\\(Q\\)</span>'s inverse is its transpose. This corresponds to "undoing" the rotation of the vector.

<div class="math-display">
$$
Q^{-1} = Q^T = \begin{bmatrix} 0 & 3/5 & 4/5 \\\\ 0 & 4/5 & -3/5 \\\\ 1 & 0 & 0 \end{bmatrix}
$$
</div>

Putting these building blocks together gives us

<div class="math-display">
$$
A^{-1} = D^{-1}Q^{-1} = D^{-1}Q^T = \begin{bmatrix} 1 / 5 & 0 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 3/5 & 4/5 \\\\ 0 & 4/5 & -3/5 \\\\ 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 3/25 & 4/25 \\\\ 0 & 8/5 & -6/5 \\\\ 1 & 0 & 0 \end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Given the English definition of <span class="math-inline">\\(f\\)</span> from part **b)** **alone**, find <span class="math-inline">\\(\text{det}(A)\\)</span>. (You can verify your work using the formula in [Chapter 6.1](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#the-determinant).)

<details markdown="1"><summary>Solution</summary>

Recall, <span class="math-inline">\\(f(\vec x)\\)</span> first scales <span class="math-inline">\\(\vec x\\)</span>'s first component by 5, second component by 1/2, and leaves the third component as-is, and then it rotates the resulting vector in a way that preserves its length.

Intuitively, <span class="math-inline">\\(\text{det}(A)\\)</span> should be the product of the scaling factors, i.e. <span class="math-inline">\\(5 \cdot 1/2 \cdot 1 = 5/2\\)</span>.

</details>

</div>
</div>

</div>

---

## Activity 3: Projecting onto the Column Space

Note: We've recorded a **[YouTube playlist](https://www.youtube.com/playlist?list=PLEFTQpsm47qQeWokuNgEIryDcVJ9iVQbx)** walking through the activities in this lab.

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix with columns <span class="math-inline">\\(\vec x^{(1)}, \vec x^{(2)}, \ldots, \vec x^{(d)}\\)</span> and <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span>. Then, the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is the vector

<div class="math-display">
$$
\vec p = X\vec w^* = w_1^* \vec x^{(1)} + w_2^* \vec x^{(2)} + \cdots + w_d^* \vec x^{(d)}
$$
</div>

 where <span class="math-inline">\\(\vec w^{\ast} \in \mathbb{R}^d\\)</span> is chosen to satisfy the **normal equation**,

<div class="math-display">
$$
X^TX \vec w = X^T \vec y
$$
</div>

 If <span class="math-inline">\\(X\\)</span>'s columns are linearly independent, <span class="math-inline">\\(\vec w^{\ast}\\)</span> is the unique vector

<div class="math-display">
$$
\vec w^* = (X^TX)^{-1}X^T \vec y
$$
</div>

Of all vectors in <span class="math-inline">\\(\text{colsp}(X)\\)</span>, <span class="math-inline">\\(X \vec w^{\ast}\\)</span> is the one that is closest to <span class="math-inline">\\(\vec y\\)</span>, meaning it minimizes

<div class="math-display">
$$
\lVert \vec y - X \vec w \rVert^2
$$
</div>

<div style="text-align: center;">
<img src="imgs/colsp-projection.png" alt="image" style="width: 45%; max-width: 100%;">
</div>

As we will see in Tuesday's lecture, <span class="math-inline">\\(\vec w^{\ast}\\)</span> contains the **optimal model parameters** for linear regression, when we fill our <span class="math-inline">\\(X\\)</span> (carefully) with our input variables and <span class="math-inline">\\(\vec y\\)</span> with our output variables.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(X = \begin{bmatrix} 2 &amp; 1 \\\\ 0 &amp; -3 \\\\ 0 &amp; 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec y = \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>. Find <span class="math-inline">\\(\vec w^{\ast}\\)</span>, <span class="math-inline">\\(\vec p\\)</span>, and <span class="math-inline">\\(\vec e = \vec y - \vec p\\)</span>, and verify that <span class="math-inline">\\(\vec e\\)</span> is orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span> by showing that it is orthogonal to each of <span class="math-inline">\\(X\\)</span>'s columns.

<details markdown="1"><summary>Solution</summary>

For

<div class="math-display">
$$
X =
\begin{bmatrix}
2 & 1 \\\\
0 & -3 \\\\
0 & 0
\end{bmatrix}
\qquad
\vec y =
\begin{bmatrix}
2 \\\\ 3 \\\\ 4
\end{bmatrix}
$$
</div>

 we begin by computing the normal equation components:

<div class="math-display">
$$
X^T X =
\begin{bmatrix}
2 & 0 & 0 \\\\
1 & -3 & 0
\end{bmatrix}
\begin{bmatrix}
2 & 1 \\\\
0 & -3 \\\\
0 & 0
\end{bmatrix}
=
\begin{bmatrix}
4 & 2 \\\\
2 & 10
\end{bmatrix}
$$
</div>

 The determinant of <span class="math-inline">\\(X^T X\\)</span> is <span class="math-inline">\\(36\\)</span>, so

<div class="math-display">
$$
(X^T X)^{-1}
= \frac{1}{36}
\begin{bmatrix}
10 & -2 \\\\
-2 & 4
\end{bmatrix}
=
\begin{bmatrix}
\frac{5}{18} & -\frac{1}{18} \\\\
-\frac{1}{18} & \frac{1}{9}
\end{bmatrix}
$$
</div>

Next, compute

<div class="math-display">
$$
X^T \vec y =
\begin{bmatrix}
2 & 0 & 0 \\\\
1 & -3 & 0
\end{bmatrix}
\begin{bmatrix}
2 \\\\ 3 \\\\ 4
\end{bmatrix}
=
\begin{bmatrix}
4 \\\\ -7
\end{bmatrix}
$$
</div>

 Therefore,

<div class="math-display">
$$
\vec w^* = (X^T X)^{-1} X^T \vec y
=
\begin{bmatrix}
\frac{5}{18} & -\frac{1}{18} \\\\
-\frac{1}{18} & \frac{1}{9}
\end{bmatrix}
\begin{bmatrix}
4 \\\\ -7
\end{bmatrix}
=
\begin{bmatrix}
\frac{27}{18} \\\\[4pt]
-1
\end{bmatrix}
=
\begin{bmatrix}
1.5 \\\\[4pt] -1
\end{bmatrix}
$$
</div>

Now compute the projection:

<div class="math-display">
$$
\vec p = X \vec w^*
=
\begin{bmatrix}
2 & 1 \\\\
0 & -3 \\\\
0 & 0
\end{bmatrix}
\begin{bmatrix}
1.5 \\\\[4pt]
-1
\end{bmatrix}
=
\begin{bmatrix}
2 \\\\ 3 \\\\ 0
\end{bmatrix}
$$
</div>

 The error vector is:

<div class="math-display">
$$
\vec e = \vec y - \vec p =
\begin{bmatrix}
2 \\\\ 3 \\\\ 4
\end{bmatrix}
-
\begin{bmatrix}
2 \\\\ 3 \\\\ 0
\end{bmatrix}
=
\begin{bmatrix}
0 \\\\ 0 \\\\ 4
\end{bmatrix}
$$
</div>

 To verify orthogonality:

<div class="math-display">
$$
X^T \vec e =
\begin{bmatrix}
2 & 0 & 0 \\\\
1 & -3 & 0
\end{bmatrix}
\begin{bmatrix}
0 \\\\ 0 \\\\ 4
\end{bmatrix}
=
\begin{bmatrix}
0 \\\\ 0
\end{bmatrix}
$$
</div>

 Thus, <span class="math-inline">\\(\vec e\\)</span> is orthogonal to both columns of <span class="math-inline">\\(X\\)</span> as required.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that <span class="math-inline">\\(a \begin{bmatrix} 2 \\\\ 0 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 1 \\\\ -3 \\\\ 0 \end{bmatrix}\\)</span> is as close as possible to <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 9 \\\\ 2 \end{bmatrix}\\)</span>. <em>Hint: You can reuse most of your work from part <strong>a)</strong>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Now, suppose <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; 1 \\\\ 1 &amp; -1 \\\\ 1 &amp; 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec y = \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>. We've already computed <span class="math-inline">\\(\vec w^{\ast}\\)</span>, <span class="math-inline">\\(\vec p\\)</span>, and <span class="math-inline">\\(\vec e\\)</span> here:

<div class="math-display">
$$
\vec w^* = \begin{bmatrix} 3 \\\\ -\frac{1}{2} \end{bmatrix}, \quad \vec p = \begin{bmatrix} 5/2 \\\\ 7/2 \\\\ 3 \end{bmatrix}, \quad \vec e = \vec y - \vec p = \begin{bmatrix} -1/2 \\\\ -1/2 \\\\ 1 \end{bmatrix}
$$
</div>

Notice that the components of this <span class="math-inline">\\(\vec e\\)</span> add up to 0, but this doesn't happen with your <span class="math-inline">\\(\vec e\\)</span> from part **a)**. **Why?** <em>Hint: The answer is not that <span class="math-inline">\\(\vec y\\)</span> is in <span class="math-inline">\\(\text{colsp}(X)\\)</span> --- it isn't in part <strong>a)</strong> and it isn't here either. Rather, it has something to do with the difference between the two <span class="math-inline">\\(X\\)</span>'s. This is a hugely important result, and one that will 100% appear on Midterm 2.</em>

<details markdown="1"><summary>Solution</summary>

In both parts, <span class="math-inline">\\(X^T \vec e = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}\\)</span>, but only in this new example is the sum of the components in <span class="math-inline">\\(\vec e\\)</span> exactly 0 (in part **a)**, it's 4).

This has to do with the fact that in each case, <span class="math-inline">\\(\vec e\\)</span> is orthogonal to **any linear combination of the columns of <span class="math-inline">\\(X\\)</span>**. This is what it means for <span class="math-inline">\\(\vec e\\)</span> to be orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

In subpart (ii), one of the columns of <span class="math-inline">\\(X\\)</span> is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>, meaning that <span class="math-inline">\\(\vec e \cdot \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix} = e&#95;1 + e&#95;2 + e&#95;3 = 0\\)</span>. However, no linear combination of the columns of <span class="math-inline">\\(X\\)</span> in subpart (i) gives a vector of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>, so we can't use this logic to guarantee the error vector's components sum to 0 in subpart (i). (I say "guarantee" because while the error vector's components don't sum to 0 for <span class="math-inline">\\(\vec y = \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>, they still could for some other <span class="math-inline">\\(\vec y\\)</span> projected onto the column space of <span class="math-inline">\\(X\\)</span> in subpart (i).)

**Don't forget this fact**: the existence of a column of 1's in <span class="math-inline">\\(X\\)</span> (or in <span class="math-inline">\\(X\\)</span>'s column space) guarantees that the error vector <span class="math-inline">\\(\vec e\\)</span> when projecting <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> will have a sum of components equal to 0, no matter what the other columns of <span class="math-inline">\\(X\\)</span> are and no matter what <span class="math-inline">\\(\vec y\\)</span> is.

</details>

Taking another look at the formula <span class="math-inline">\\(\vec p = X \vec w^{\ast}\\)</span>, we see that it's equivalent to

<div class="math-display">
$$
\vec p = X \vec w^* = X (X^TX)^{-1}X^T\vec y = P\vec y
$$
</div>

 where <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span> is called the **projection matrix**, discussed in [Chapter 6.4](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/#the-projection-matrix). Multiplying <span class="math-inline">\\(P \vec y\\)</span> is equivalent to projecting <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Recall that <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix (meaning it's not necessarily square), which makes <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span> an <span class="math-inline">\\(n \times n\\)</span> matrix.

Fill in the blanks: <span class="math-inline">\\(X^TX\\)</span> is invertible if and only if <span class="math-inline">\\(X\\)</span>'s columns are \_\_\_\_.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(X^TX\\)</span> is invertible if and only if <span class="math-inline">\\(X\\)</span>'s columns are **linearly independent**. This is because <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^TX)\\)</span>, as we proved in [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-rank-of-x-tx), and a matrix is invertible if and only if its rank is equal to its number of columns.

For <span class="math-inline">\\(\text{rank}(X^TX) = d\\)</span>, we need <span class="math-inline">\\(\text{rank}(X) = d\\)</span>, meaning <span class="math-inline">\\(X\\)</span>'s columns must be linearly independent.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
In this part only, suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times 1\\)</span> matrix, i.e. it is a vector. Then,

1.  What is the value of <span class="math-inline">\\(\vec w^{\ast}\\)</span>, and how does it relate to what we learned in [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-projections)? (What type of object is <span class="math-inline">\\((X^TX)^{-1}\\)</span> when <span class="math-inline">\\(X\\)</span> is a vector?)

2.  What is the value of the matrix <span class="math-inline">\\(P\\)</span>, and how does it relate to what we learned in [Homework 6, Problem 5](https://eecs245.org/resources/homeworks/hw06/#problem-5-projecting-onto-a-single-vector-12-pts)?

<details markdown="1"><summary>Solution</summary>

Suppose <span class="math-inline">\\(X\\)</span> is the vector <span class="math-inline">\\(\vec x\\)</span>. Remember that <span class="math-inline">\\(\vec x^T \vec x\\)</span> is a scalar; it's the dot product of <span class="math-inline">\\(\vec x\\)</span> with itself. So, <span class="math-inline">\\((X^TX)^{-1} = (\vec x^T \vec x)^{-1} = \frac{1}{\vec x^T \vec x}\\)</span>, since the inverse of a scalar is the reciprocal of that scalar.

1.  $$
\vec w^* = (X^TX)^{-1}X^T\vec y = (\vec x^T \vec x)^{-1} \vec x^T \vec y = \frac{\vec x^T \vec y}{\vec x^T \vec x} = \frac{\vec x \cdot \vec y}{\vec x \cdot \vec x}
$$

   This is the same formula for the optimal value of <span class="math-inline">\\(k\\)</span> from Chapter 3.4, where we approximated <span class="math-inline">\\(\vec y\\)</span> by a scalar multiple of <span class="math-inline">\\(\vec x\\)</span>, called <span class="math-inline">\\(k \vec x\\)</span>.

2.  $$
P = X (X^TX)^{-1}X^T = \vec x (\vec x^T \vec x)^{-1} \vec x^T = \frac{\vec x \vec x^T}{\vec x^T \vec x}
$$

   In [Homework 6, Problem 5](https://eecs245.org/resources/homeworks/hw06/#problem-5-projecting-onto-a-single-vector-12-pts), we found that the matrix <span class="math-inline">\\(P\\)</span> that projects <span class="math-inline">\\(\vec y\\)</span> onto the line spanned by the **unit vector** <span class="math-inline">\\(\vec x\\)</span> is given by

<div class="math-display">
$$
P = \begin{bmatrix} x_1^2 & x_1x_2 \\\\ x_1x_2 & x_2^2 \end{bmatrix} = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} x_1 & x_2 \end{bmatrix}^T = \vec x \vec x^T
$$
</div>

   Here, <span class="math-inline">\\(\vec x\\)</span> isn't a unit vector, hence the division by <span class="math-inline">\\(\vec x^T \vec x\\)</span>.

</details>

<div class="math-display">
$$
P = X (X^TX)^{-1}X^T
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
Show that <span class="math-inline">\\(P\\)</span> is both symmetric (meaning that <span class="math-inline">\\(P^T = P\\)</span>) and idempotent (meaning that <span class="math-inline">\\(P^2 = P\\)</span>). Then, explain in English how <span class="math-inline">\\(P\\)</span>'s idempotence relates to the linear transformation of projecting <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<details markdown="1"><summary>Solution</summary>

To show that <span class="math-inline">\\(P\\)</span> is **symmetric**, we need to show that <span class="math-inline">\\(P^T = P\\)</span>. Recall that <span class="math-inline">\\((AB)^T = B^TA^T\\)</span>, so

<div class="math-display">
$$
\begin{align*}
P^T &= \left( {X} ({X^T X})^{-1} {X^T} \right)^T \\\\ &= \left( {X^T} \right)^T \left( ({X^T X})^{-1} \right)^T {X^T} \\\\ &= {X} ({X^T X})^{-1} X^T \\\\ &= P
\end{align*}
$$
</div>

To go from line 2 to line 3, we used the fact that <span class="math-inline">\\(X^TX\\)</span> is symmetric, so <span class="math-inline">\\((X^TX)^{-1}\\)</span> is also symmetric. Remember that <span class="math-inline">\\(X^TX\\)</span> contains the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s columns.

To show that <span class="math-inline">\\(P\\)</span> is **idempotent**, we need to show that <span class="math-inline">\\(P^2 = P\\)</span>.

<div class="math-display">
$$
\begin{align*}
P^2
&= \left( {X} ({X^T X})^{-1} {X^T} \right) \left( {X} ({X^T X})^{-1} {X^T} \right) \\\\
&= {X} ({X^T X})^{-1} \left( {X^T} {X} \right) ({X^T X})^{-1} {X^T} \\\\
&= {X} ({X^T X})^{-1} {I} {X^T} \\\\
&= {X} ({X^T X})^{-1} {X^T}  \\\\
&= P
\end{align*}
$$
</div>

The fact that <span class="math-inline">\\(P\\)</span> is idempotent means that applying <span class="math-inline">\\(P\\)</span> twice (or three times, or four times, etc.) to a vector is the same as applying it once. Once we've already projected <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, we don't need to project it again, since the projection <span class="math-inline">\\(\vec p = P \vec y\\)</span> is already in <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">g)</div>
<div class="assignment-part-content" markdown="1">
In the rare case that <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> square matrix, and <span class="math-inline">\\(\text{rank}(X) = n\\)</span>, what is <span class="math-inline">\\(P\\)</span>? What does this say about the relationship between <span class="math-inline">\\(\vec y\\)</span>, <span class="math-inline">\\(\vec p\\)</span>, and <span class="math-inline">\\(\text{colsp}(X)\\)</span>? <em>Hint: Use the fact that <span class="math-inline">\\((AB)^{-1} = B^{-1}A^{-1}\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> square matrix, and <span class="math-inline">\\(\text{rank}(X) = n\\)</span>, then <span class="math-inline">\\(X\\)</span> is invertible, and so is <span class="math-inline">\\(X^T\\)</span> (since if <span class="math-inline">\\(X\\)</span> has <span class="math-inline">\\(n\\)</span> linearly independent columns, it must have <span class="math-inline">\\(n\\)</span> linearly independent rows).

<span class="math-inline">\\((X^TX)^{-1} = X^{-1}(X^T)^{-1}\\)</span> because <span class="math-inline">\\((AB)^{-1} = B^{-1}A^{-1}\\)</span>.

Then,

<div class="math-display">
$$
P = X (X^TX)^{-1}X^T = \underbrace{X X^{-1}}_I \underbrace{(X^T)^{-1}X^T}_I = I
$$
</div>

So, if <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> square matrix with <span class="math-inline">\\(\text{rank}(X) = n\\)</span>, then <span class="math-inline">\\(P = I\\)</span>. What this says is that <span class="math-inline">\\(\text{colsp}(X) = \mathbb{R}^n\\)</span>, meaning that any vector <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> can be represented as a linear combination of <span class="math-inline">\\(X\\)</span>'s columns, so the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is just <span class="math-inline">\\(\vec y\\)</span> itself, i.e. <span class="math-inline">\\(\vec p = P \vec y = \vec y\\)</span>.

</details>
</div>
</div>

</div>

{% endraw %}
