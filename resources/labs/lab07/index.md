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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a **diagonal** matrix <span class="math-inline">\\(D\\)</span> and an **orthogonal** matrix <span class="math-inline">\\(Q\\)</span> such that <span class="math-inline">\\(A = QD\\)</span>. (Not every matrix can be written in this form, but this particular <span class="math-inline">\\(A\\)</span> can.) Then, describe **in English** how <span class="math-inline">\\(f\\)</span> transforms a vector <span class="math-inline">\\(\vec x\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Using your <span class="math-inline">\\(A = QD\\)</span> decomposition from part **b)**, find <span class="math-inline">\\(A^{-1}\\)</span>.

<em>Hint: Recall that for orthogonal matrices, <span class="math-inline">\\(QQ^T = Q^TQ = I\\)</span>. And, for any invertible matrices <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, <span class="math-inline">\\((AB)^{-1} = B^{-1}A^{-1}\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Given the English definition of <span class="math-inline">\\(f\\)</span> from part **b)** **alone**, find <span class="math-inline">\\(\text{det}(A)\\)</span>. (You can verify your work using the formula in [Chapter 6.1](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#the-determinant).)

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
In this part only, suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times 1\\)</span> matrix, i.e. it is a vector. Then,

1.  What is the value of <span class="math-inline">\\(\vec w^{\ast}\\)</span>, and how does it relate to what we learned in [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-projections)? (What type of object is <span class="math-inline">\\((X^TX)^{-1}\\)</span> when <span class="math-inline">\\(X\\)</span> is a vector?)

2.  What is the value of the matrix <span class="math-inline">\\(P\\)</span>, and how does it relate to what we learned in [Homework 6, Problem 5](https://eecs245.org/resources/homeworks/hw06/#problem-5-projecting-onto-a-single-vector-12-pts)?

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">g)</div>
<div class="assignment-part-content" markdown="1">
In the rare case that <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> square matrix, and <span class="math-inline">\\(\text{rank}(X) = n\\)</span>, what is <span class="math-inline">\\(P\\)</span>? What does this say about the relationship between <span class="math-inline">\\(\vec y\\)</span>, <span class="math-inline">\\(\vec p\\)</span>, and <span class="math-inline">\\(\text{colsp}(X)\\)</span>? <em>Hint: Use the fact that <span class="math-inline">\\((AB)^{-1} = B^{-1}A^{-1}\\)</span>.</em>
</div>
</div>

</div>

{% endraw %}
