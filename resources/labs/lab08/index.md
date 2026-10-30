---
layout: page
title: "Lab 8: Linear Transformations, Inverses, and Projections"
description: "Lab 8: Linear Transformations, Inverses, and Projections activities."
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
</style>

# Lab 8: Linear Transformations, Inverses, and Projections

**due** by the end of your lab section on Wednesday, October 28th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab08/lab08.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab08/lab08-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete all activities and show your lab TA by the end of the lab section.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: PrairieLearn Practice Problems](#activity-1-prairielearn-practice-problems)
- [Activity 2: Symbolic Inverses](#activity-2-symbolic-inverses)
- [Activity 3: Can $A$ Be Invertible?](#activity-3-can-a-be-invertible)
- [Activity 4: Linear Transformations](#activity-4-linear-transformations)
- [Activity 5: Projecting onto the Column Space](#activity-5-projecting-onto-the-column-space)

---

## Recap: Linear Transformations ([Chapter 6.1](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/)) and Inverses ([Chapter 6.2](https://notes.eecs245.org/linear-transformations-and-projections/inverses/))

<ul class="assignment-list" markdown="1" data-item-count="4">
<li markdown="1">

A linear transformation is a function <span class="math-inline">\\(\mathbb{R}^d \to \mathbb{R}^n\\)</span> such that

<div class="math-display">
$$
f(\vec x + \vec y) = f(\vec x) + f(\vec y), \qquad f(c \vec x) = c f(\vec x)
$$
</div>

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

Every linear transformation has a corresponding <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(A\\)</span> where <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span>.

</li>
<li markdown="1">

If <span class="math-inline">\\(A\\)</span> is square, then <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span> is a function from <span class="math-inline">\\(\mathbb{R}^n\\)</span> to <span class="math-inline">\\(\mathbb{R}^n\\)</span>, and <span class="math-inline">\\(A\\)</span> is invertible if and only if the function <span class="math-inline">\\(f\\)</span> is invertible.

</li>
</ul>
</li>
<li markdown="1">

An <span class="math-inline">\\(n \times n\\)</span> square matrix <span class="math-inline">\\(A\\)</span> is **invertible** if and only if <span class="math-inline">\\(\text{rank}(A) = n\\)</span>, which also means that <span class="math-inline">\\(A\\)</span>'s columns are linearly independent (along with several other equivalent conditions).

</li>
<li markdown="1">

If <span class="math-inline">\\(A\\)</span> is invertible, then its **inverse** <span class="math-inline">\\(A^{-1}\\)</span> is the **unique** <span class="math-inline">\\(n \times n\\)</span> matrix such that <span class="math-inline">\\(AA^{-1}=I=A^{-1}A\\)</span>.

</li>
<li markdown="1">

The **determinant** of an <span class="math-inline">\\(n \times n\\)</span> square matrix <span class="math-inline">\\(A\\)</span>, denoted <span class="math-inline">\\(\text{det}(A)\\)</span>, is defined so that <span class="math-inline">\\(|\text{det}(A)|\\)</span> is the <span class="math-inline">\\(n\\)</span>-dimensional volume of the parallelepiped spanned by the columns of <span class="math-inline">\\(A\\)</span>.

<ul class="assignment-list" markdown="1" data-item-count="3">
<li markdown="1">

If <span class="math-inline">\\(\text{det}(A) = 0\\)</span>, then <span class="math-inline">\\(A\\)</span> is not invertible.

</li>
<li markdown="1">

If <span class="math-inline">\\(A = \begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span>, then <span class="math-inline">\\(\text{det}(A) = ad - bc\\)</span> and <span class="math-inline">\\(A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d &amp; -b \\\\ -c &amp; a \end{bmatrix}\\)</span>.

</li>
<li markdown="1">

The determinant satisfies several properties, including that <span class="math-inline">\\(\text{det}(AB) = \text{det}(A) \text{det}(B)\\)</span> and <span class="math-inline">\\(\text{det}(A^T) = \text{det}(A)\\)</span>.

</li>
</ul>
</li>
</ul>

---

## Activity 1: PrairieLearn Practice Problems

We're testing out a new website for practicing linear algebra problems: PrairieLearn.

On the course website, under Lab 8, click the "PrairieLearn" link to access the relevant problems for this activity. It consists of 6 problems, each worth 1 point. The numbers in the problems are randomized; everyone will receive slightly different problems.

You can also [**access the problems here**](https://us.prairielearn.com/pl/course_instance/236398/assessment/2742917) when reviewing.

To get credit for Activity 1, you must **eventually** correctly answer all 6 problems, earning a score of 6/6. If you answer a problem incorrectly, click "New Variant" to generate a new version and then try again. There is no penalty for answering a problem incorrectly, as long as you eventually get it correct.

To get checked off for Activity 1, show your lab TA that you have earned a score of 6/6 on PrairieLearn.

If you can't access PrairieLearn, post on Ed or email Suraj.

---

## Activity 2: Symbolic Inverses

Given that <span class="math-inline">\\(A\\)</span> is an invertible <span class="math-inline">\\(n \times n\\)</span> matrix that satisfies <span class="math-inline">\\(A^4 - 3A^2 + 2A - 4I = 0\\)</span>, find an expression for <span class="math-inline">\\(A^{-1}\\)</span> in terms of <span class="math-inline">\\(A\\)</span>.

<details markdown="1"><summary>Solution</summary>

The goal is to find another matrix <span class="math-inline">\\(B\\)</span> such that <span class="math-inline">\\(AB = BA = I\\)</span>. We can do this by isolating the identity matrix, <span class="math-inline">\\(I\\)</span>, and then trying to write the other side of the equation as <span class="math-inline">\\(A\\)</span> times some other matrix.

<div class="math-display">
$$
\begin{align*}
A^4 - 3A^2 + 2A - 4I &= 0 \\\\
A^4 - 3A^2 + 2A &= 4I \\\\
A(A^3 - 3A + 2I) &= 4I \\\\
A \left( \frac{1}{4}(A^3 - 3A + 2I) \right) &= I
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\boxed{A^{-1} = \frac{1}{4}(A^3 - 3A + 2I)}\\)</span>.
</details>

---

## Activity 3: Can <span class="math-inline">\\(A\\)</span> Be Invertible?

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3\times3\\)</span> matrix such that

<div class="math-display">
$$
A\begin{bmatrix}5\\\\-1\\\\2\end{bmatrix}
=A\begin{bmatrix}1\\\\3\\\\2\end{bmatrix}
$$
</div>

 Is <span class="math-inline">\\(A\\)</span> invertible? Why or why not?

<details markdown="1"><summary>Solution</summary>

No. If <span class="math-inline">\\(A\\)</span> were invertible, we could multiply both sides by <span class="math-inline">\\(A^{-1}\\)</span> to get

<div class="math-display">
$$
\begin{bmatrix}5\\\\-1\\\\2\end{bmatrix}=\begin{bmatrix}1\\\\3\\\\2\end{bmatrix}
$$
</div>

 But these vectors aren't equal, so <span class="math-inline">\\(A\\)</span> can't be invertible.

Equivalently, the distributive property of matrix multiplication tells us that

<div class="math-display">
$$
A\begin{bmatrix}5\\\\-1\\\\2\end{bmatrix}-A\begin{bmatrix}1\\\\3\\\\2\end{bmatrix}=\vec0
\quad\Longrightarrow\quad
A\begin{bmatrix}4\\\\-4\\\\0\end{bmatrix}=\vec0
$$
</div>

 This means that <span class="math-inline">\\(\begin{bmatrix}4\\\\-4\\\\0\end{bmatrix}\in\text{nullsp}(A)\\)</span>. Since this is a non-zero vector, <span class="math-inline">\\(A\\)</span> does not have linearly independent columns and is not invertible.
</details>

---

## Activity 4: Linear Transformations

[**Watch the TA walkthrough for Activity 4.**](https://youtu.be/r5N26V-WEaA)

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/r5N26V-WEaA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

Suppose <span class="math-inline">\\(f: \mathbb{R}^3 \to \mathbb{R}^3\\)</span> is a linear transformation represented by the matrix <span class="math-inline">\\(A\\)</span>.

Furthermore, suppose that <span class="math-inline">\\(f\left(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\right) = \begin{bmatrix} 0 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>, <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 10 \\\\ 0 \end{bmatrix}\right) = \begin{bmatrix} 0 \\\\ 4 \\\\ -3 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\right) = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(f\left(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\right)\\)</span>. **After that**, find the matrix <span class="math-inline">\\(A\\)</span> corresponding to <span class="math-inline">\\(f\\)</span>, i.e. where <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span>.

<details markdown="1"><summary>Solution</summary>

First, using just the properties of linear transformations, we can find <span class="math-inline">\\(f\left(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\right)\\)</span>. Recall that a linear transformation <span class="math-inline">\\(f:\mathbb R^3\to\mathbb R^3\\)</span> satisfies

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

<span class="math-inline">\\(f(\vec x + \vec y) = f(\vec x) + f(\vec y)\\)</span>, for all <span class="math-inline">\\(\vec x,\vec y\in\mathbb R^3\\)</span>.

</li>
<li markdown="1">

<span class="math-inline">\\(f(c \vec x) = c f(\vec x)\\)</span>, for all <span class="math-inline">\\(\vec x\in\mathbb R^3\\)</span> and <span class="math-inline">\\(c\in\mathbb R\\)</span>.

</li>
</ul>

In other words, <span class="math-inline">\\(f\\)</span> preserves linear combinations: <span class="math-inline">\\(f(a \vec x + b \vec y) = a f(\vec x) + b f(\vec y)\\)</span>.

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

<ul class="assignment-list" markdown="1" data-item-count="3">
<li markdown="1">

The first column of <span class="math-inline">\\(A\\)</span> is given by <span class="math-inline">\\(f\left(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\right)\\)</span>, which we're told is <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>.

</li>
<li markdown="1">

The second column of <span class="math-inline">\\(A\\)</span> is given by <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\right)\\)</span>, which we've computed above to be <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 4/10 \\\\ -3/10 \end{bmatrix}\\)</span>.

</li>
<li markdown="1">

The third column of <span class="math-inline">\\(A\\)</span> is given by <span class="math-inline">\\(f\left(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\right)\\)</span>, which we're told is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>.

</li>
</ul>

So,

<div class="math-display">
$$
A = \begin{bmatrix} 0 & 0 & 1 \\\\ 3 & 4 / 10 & 0 \\\\ 4 & -3 / 10 & 0 \end{bmatrix}
$$
</div>

You can verify that multiplying <span class="math-inline">\\(A\\)</span> by <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \\\\ 2 \end{bmatrix}\\)</span> gives us <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 6.4 \\\\ 7.7 \end{bmatrix}\\)</span>, and that multiplying <span class="math-inline">\\(A\\)</span> by the three vectors in the question give the outputs we're told. Remember that <span class="math-inline">\\(A \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> returns just the first column of <span class="math-inline">\\(A\\)</span>, and so on.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a **diagonal** matrix <span class="math-inline">\\(D\\)</span> and an **orthogonal** matrix <span class="math-inline">\\(Q\\)</span> such that <span class="math-inline">\\(A = QD\\)</span>. (Not every matrix can be written in this form, but this particular <span class="math-inline">\\(A\\)</span> can.) Then, describe **in English** how <span class="math-inline">\\(f\\)</span> transforms a vector <span class="math-inline">\\(\vec x\\)</span>.

<details markdown="1"><summary>Solution</summary>

Remember that

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

Diagonal matrices have 0s everywhere except on the diagonal, and have the effect of stretching/compressing each axis/dimension of the input vector independently.

</li>
<li markdown="1">

Orthogonal matrices have columns that are orthonormal, meaning their columns are unit vectors that are orthogonal to one another.

</li>
</ul>

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

<span class="math-inline">\\(f(\vec x) = QD \vec x\\)</span> transforms <span class="math-inline">\\(f\\)</span> by first scaling <span class="math-inline">\\(\vec x\\)</span>'s first component by 5, second component by 1/2, and leaving the third component as-is, and then applying the orthogonal matrix <span class="math-inline">\\(Q\\)</span>.

Orthogonal matrices preserve lengths and angles; they may include reflections. This particular <span class="math-inline">\\(Q\\)</span> reverses orientation. It's harder to describe rotations in <span class="math-inline">\\(\mathbb{R}^3\\)</span> and beyond, but the key property that describes the effect of an orthogonal matrix <span class="math-inline">\\(Q\\)</span> is that for any vector <span class="math-inline">\\(\vec x\\)</span>,

<div class="math-display">
$$
\lVert Q \vec x \rVert = \lVert \vec x \rVert
$$
</div>

as follows from <span class="math-inline">\\(Q^TQ=I\\)</span>, meaning that all an orthogonal matrix is doing is changing the angle of the vector, not its length.

So, <span class="math-inline">\\(f(\vec x)\\)</span> first scales <span class="math-inline">\\(\vec x\\)</span>'s components, and then applies <span class="math-inline">\\(Q\\)</span> to the resulting vector.
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

And, since <span class="math-inline">\\(Q\\)</span> is orthogonal, we know <span class="math-inline">\\(Q^TQ = I\\)</span>, meaning that <span class="math-inline">\\(Q^{-1} = Q^T\\)</span>, i.e. <span class="math-inline">\\(Q\\)</span>'s inverse is its transpose. This corresponds to "undoing" the orthogonal transformation of the vector.

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
Using the scaling factors from part **b)**, find <span class="math-inline">\\(|\text{det}(A)|\\)</span>. (You can verify your work using the formula in [Chapter 6.1](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#the-determinant).)

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(Q\\)</span> is orthogonal, <span class="math-inline">\\(Q^TQ=I\\)</span>. Taking determinants gives

<div class="math-display">
$$
\text{det}(Q^TQ)=\text{det}(I)=1
$$
</div>

 Using <span class="math-inline">\\(\text{det}(AB)=\text{det}(A)\text{det}(B)\\)</span> and <span class="math-inline">\\(\text{det}(Q^T)=\text{det}(Q)\\)</span>, we get

<div class="math-display">
$$
\text{det}(Q)^2=1\quad\Longrightarrow\quad |\text{det}(Q)|=1
$$
</div>

 So, since <span class="math-inline">\\(A=QD\\)</span>,

<div class="math-display">
$$
|\text{det}(A)|=|\text{det}(Q)|\,|\text{det}(D)|=1\cdot5\cdot\frac12=\boxed{\frac52}
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 5: Projecting onto the Column Space

The next big idea in the course is finding the projection of a vector <span class="math-inline">\\(\vec y\in\mathbb R^n\\)</span> onto the column space of an <span class="math-inline">\\(n\times d\\)</span> matrix <span class="math-inline">\\(X\\)</span>.

Let

<div class="math-display">
$$
X=\begin{bmatrix}2&1\\\\0&-3\\\\0&0\end{bmatrix},\qquad
\vec y=\begin{bmatrix}2\\\\3\\\\4\end{bmatrix}
$$
</div>

<img src="imgs/tikz-1d585341dbc8.png" alt="Figure from the assignment PDF" style="display: block; margin-left: auto; margin-right: auto; width: 60%; max-width: 100%;">

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blank: <span class="math-inline">\\(\text{colsp}(X)\\)</span> is a \_\_\_\_ in <span class="math-inline">\\(\mathbb R^3\\)</span>.

<details markdown="1"><summary>Solution</summary>

A **plane**. The columns are linearly independent and both have third component 0, so their span is the plane of vectors whose third component is 0. In other words, <span class="math-inline">\\(\text{colsp}(X)\\)</span> is the <span class="math-inline">\\(xy\\)</span>-plane in <span class="math-inline">\\(\mathbb R^3\\)</span>, which is the plane <span class="math-inline">\\(z=0\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Which vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span> is closest to <span class="math-inline">\\(\vec y\\)</span>? Normally, this would require more calculation, but it is possible to see the answer here without much work. Explain your thought process.

<details markdown="1"><summary>Solution</summary>

Every vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span> has third component 0. So, we can't match the third component of <span class="math-inline">\\(\vec y\\)</span>, but we can match its first two components exactly, because the two columns of <span class="math-inline">\\(X\\)</span> are linearly independent and span a plane (and the set of vectors with <span class="math-inline">\\(z=0\\)</span> is a plane). This gives

<div class="math-display">
$$
\boxed{\vec p=\begin{bmatrix}2\\\\3\\\\0\end{bmatrix}}
$$
</div>

 Changing either of the first two components would only move us farther from <span class="math-inline">\\(\vec y\\)</span>.
</details>

We'll call the vector you found <span class="math-inline">\\(\vec p\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find the error vector <span class="math-inline">\\(\vec e=\vec y-\vec p\\)</span>.

<details markdown="1"><summary>Solution</summary>

Subtracting gives

<div class="math-display">
$$
\vec e=\vec y-\vec p=\begin{bmatrix}2\\\\3\\\\4\end{bmatrix}-\begin{bmatrix}2\\\\3\\\\0\end{bmatrix}=\boxed{\begin{bmatrix}0\\\\0\\\\4\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Verify that <span class="math-inline">\\(\vec e\\)</span> is orthogonal to each column of <span class="math-inline">\\(X\\)</span>.

<details markdown="1"><summary>Solution</summary>

Taking the dot product with each column gives

<div class="math-display">
$$
\begin{bmatrix}0\\\\0\\\\4\end{bmatrix}\cdot\begin{bmatrix}2\\\\0\\\\0\end{bmatrix}=0,\qquad
\begin{bmatrix}0\\\\0\\\\4\end{bmatrix}\cdot\begin{bmatrix}1\\\\-3\\\\0\end{bmatrix}=0
$$
</div>

 Both dot products are 0, so <span class="math-inline">\\(\vec e\\)</span> is orthogonal to both columns.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec w^{\ast}\in\mathbb R^2\\)</span> such that <span class="math-inline">\\(X\vec w^{\ast}=\vec p\\)</span>.

<details markdown="1"><summary>Solution</summary>

Writing out <span class="math-inline">\\(X\vec w^{\ast}=\vec p\\)</span> gives

<div class="math-display">
$$
2w_1^*+w_2^*=2,\qquad -3w_2^*=3
$$
</div>

 The second equation gives <span class="math-inline">\\(w&#95;2^{\ast}=-1\\)</span>. Substituting into the first gives <span class="math-inline">\\(2w&#95;1^{\ast}-1=2\\)</span>, so

<div class="math-display">
$$
\boxed{\vec w^*=\begin{bmatrix}3/2\\\\-1\end{bmatrix}}
$$
</div>

</details>

We were able to find <span class="math-inline">\\(\vec p\\)</span> without much calculation because of the particular <span class="math-inline">\\(X\\)</span> and <span class="math-inline">\\(\vec y\\)</span> we chose. But we need a **more general-purpose solution**, one that works for any <span class="math-inline">\\(n\times d\\)</span> matrix <span class="math-inline">\\(X\\)</span> and any <span class="math-inline">\\(\vec y\in\mathbb R^n\\)</span>. We can't rely on being able to see the answer, especially when <span class="math-inline">\\(n&gt;3\\)</span>!

**Important: Every vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span> can be written as <span class="math-inline">\\(X\vec w\\)</span> for some <span class="math-inline">\\(\vec w\in\mathbb R^d\\)</span>.**

Our goal is to find <span class="math-inline">\\(\vec w\\)</span> so that the error <span class="math-inline">\\(\vec e=\vec y-X\vec w\\)</span> is orthogonal to every column of <span class="math-inline">\\(X\\)</span>. Let <span class="math-inline">\\(\vec x^{(1)},\ldots,\vec x^{(d)}\\)</span> be the columns of <span class="math-inline">\\(X\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blank: For <span class="math-inline">\\(\vec e\\)</span> to be orthogonal to every column of <span class="math-inline">\\(X\\)</span>, we need

<div class="math-display">
$$
\vec x^{(1)}\cdot\vec e=0,\quad\ldots,\quad\vec x^{(d)}\cdot\vec e=0,
$$
</div>

 which we can write as a single matrix-vector product:

<div class="math-display">
$$
\_\_\_\_\;\vec e=\vec0
$$
</div>

<details markdown="1"><summary>Solution</summary>

The blank is <span class="math-inline">\\(\boxed{X^T}\\)</span>. Each row of <span class="math-inline">\\(X^T\\)</span> is the transpose of a column of <span class="math-inline">\\(X\\)</span>, so the components of <span class="math-inline">\\(X^T\vec e\\)</span> are exactly the dot products listed above.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">g)</div>
<div class="assignment-part-content" markdown="1">
Substitute <span class="math-inline">\\(\vec e=\vec y-X\vec w\\)</span> into your equation and rearrange it to fill in the blanks below. This is called the **normal equation**.

<div class="math-display">
$$
\underbrace{\_\_\_\_}_{d\times d}\,\vec w
=\underbrace{\_\_\_\_}_{d\times1}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Starting with <span class="math-inline">\\(X^T\vec e=\vec0\\)</span>, substitute <span class="math-inline">\\(\vec e=\vec y-X\vec w\\)</span>:

<div class="math-display">
$$
\begin{align*}
X^T(\vec y-X\vec w)&=\vec0\\\\
X^T\vec y-X^TX\vec w&=\vec0\\\\
\boxed{X^TX}\,\vec w&=\boxed{X^T\vec y}
\end{align*}
$$
</div>

</details>

The normal equation describes the condition we want for any <span class="math-inline">\\(n\times d\\)</span> matrix <span class="math-inline">\\(X\\)</span>. To solve it using an inverse, we'll now assume that <span class="math-inline">\\(X\\)</span>'s columns are linearly independent.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">h)</div>
<div class="assignment-part-content" markdown="1">
Explain why <span class="math-inline">\\(X^TX\\)</span> is invertible under this assumption. <em>Hint: Recall that <span class="math-inline">\\(\text{rank}(X^TX)=\text{rank}(X)\\)</span>, as explained in <a href="https://www.youtube.com/watch?v=hOyaHqGmO1I">this video</a>.</em>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(X\\)</span> has <span class="math-inline">\\(d\\)</span> linearly independent columns, <span class="math-inline">\\(\text{rank}(X)=d\\)</span>. We also know that <span class="math-inline">\\(\text{rank}(X^TX)=\text{rank}(X)\\)</span>, so <span class="math-inline">\\(\text{rank}(X^TX)=d\\)</span>.

But <span class="math-inline">\\(X^TX\\)</span> is a <span class="math-inline">\\(d\times d\\)</span> square matrix. Its rank equals its number of columns, so it is invertible.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">i)</div>
<div class="assignment-part-content" markdown="1">
Solve the normal equation for <span class="math-inline">\\(\vec w\\)</span> by multiplying both sides by an appropriate inverse. Call your solution <span class="math-inline">\\(\vec w^{\ast}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Multiplying both sides on the left by <span class="math-inline">\\((X^TX)^{-1}\\)</span> gives

<div class="math-display">
$$
\begin{align*}
(X^TX)^{-1}X^TX\vec w&=(X^TX)^{-1}X^T\vec y\\\\
\vec w&=(X^TX)^{-1}X^T\vec y
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\boxed{\vec w^{\ast}=(X^TX)^{-1}X^T\vec y}\\)</span>.
</details>

The closest vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span> to <span class="math-inline">\\(\vec y\\)</span> is <span class="math-inline">\\(\vec p=X\vec w^{\ast}\\)</span>. We call <span class="math-inline">\\(\vec p\\)</span> the **projection** of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

Now, let's try our method with a different <span class="math-inline">\\(X\\)</span>:

<div class="math-display">
$$
X=\begin{bmatrix}1&1\\\\1&-1\\\\1&0\end{bmatrix},\qquad
\vec y=\begin{bmatrix}2\\\\3\\\\4\end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">j)</div>
<div class="assignment-part-content" markdown="1">
Use the normal equation to find <span class="math-inline">\\(\vec w^{\ast}\\)</span>.

<details markdown="1"><summary>Solution</summary>

First, compute the two sides of the normal equation:

<div class="math-display">
$$
X^TX=\begin{bmatrix}3&0\\\\0&2\end{bmatrix},\qquad
X^T\vec y=\begin{bmatrix}9\\\\-1\end{bmatrix}
$$
</div>

 So, we need to solve

<div class="math-display">
$$
\begin{bmatrix}3&0\\\\0&2\end{bmatrix}\vec w^*=\begin{bmatrix}9\\\\-1\end{bmatrix}
$$
</div>

 This gives <span class="math-inline">\\(3w&#95;1^{\ast}=9\\)</span> and <span class="math-inline">\\(2w&#95;2^{\ast}=-1\\)</span>, so

<div class="math-display">
$$
\boxed{\vec w^*=\begin{bmatrix}3\\\\-1/2\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">k)</div>
<div class="assignment-part-content" markdown="1">
Find the projection <span class="math-inline">\\(\vec p\\)</span> of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Multiplying by <span class="math-inline">\\(X\\)</span> gives

<div class="math-display">
$$
\vec p=X\vec w^*=\begin{bmatrix}1&1\\\\1&-1\\\\1&0\end{bmatrix}\begin{bmatrix}3\\\\-1/2\end{bmatrix}=\boxed{\begin{bmatrix}5/2\\\\7/2\\\\3\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">l)</div>
<div class="assignment-part-content" markdown="1">
Find the error vector <span class="math-inline">\\(\vec e=\vec y-\vec p\\)</span>.

<details markdown="1"><summary>Solution</summary>

Subtracting gives

<div class="math-display">
$$
\vec e=\vec y-\vec p=\begin{bmatrix}2\\\\3\\\\4\end{bmatrix}-\begin{bmatrix}5/2\\\\7/2\\\\3\end{bmatrix}=\boxed{\begin{bmatrix}-1/2\\\\-1/2\\\\1\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">m)</div>
<div class="assignment-part-content" markdown="1">
Why do the components of <span class="math-inline">\\(\vec e\\)</span> sum to 0 in this example, but not in the first example in this activity?

<details markdown="1"><summary>Solution</summary>

In both parts, <span class="math-inline">\\(X^T \vec e = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}\\)</span>, but only in this new example is the sum of the components in <span class="math-inline">\\(\vec e\\)</span> exactly 0 (in the first example, it's 4).

This has to do with the fact that in each case, <span class="math-inline">\\(\vec e\\)</span> is orthogonal to **any linear combination of the columns of <span class="math-inline">\\(X\\)</span>**. This is what it means for <span class="math-inline">\\(\vec e\\)</span> to be orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

In the second example, one of the columns of <span class="math-inline">\\(X\\)</span> is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>, meaning that <span class="math-inline">\\(\vec e \cdot \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix} = e&#95;1 + e&#95;2 + e&#95;3 = 0\\)</span>. However, no linear combination of the columns of <span class="math-inline">\\(X\\)</span> in the first example gives a vector of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>, so we can't use this logic to guarantee the error vector's components sum to 0 in the first example. (I say "guarantee" because while the error vector's components don't sum to 0 for <span class="math-inline">\\(\vec y = \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>, they still could for some other <span class="math-inline">\\(\vec y\\)</span> projected onto the column space of <span class="math-inline">\\(X\\)</span> in the first example.)

**Don't forget this fact**: the existence of a column of 1's in <span class="math-inline">\\(X\\)</span> (or in <span class="math-inline">\\(X\\)</span>'s column space) guarantees that the error vector <span class="math-inline">\\(\vec e\\)</span> when projecting <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> will have a sum of components equal to 0, no matter what the other columns of <span class="math-inline">\\(X\\)</span> are and no matter what <span class="math-inline">\\(\vec y\\)</span> is.
</details>
</div>
</div>

</div>

{% endraw %}
