---
layout: page
title: "Homework 7: Projections; Regression using Linear Algebra"
description: "Homework 7: Projections; Regression using Linear Algebra problems."
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

# Homework 7: Projections; Regression using Linear Algebra

**due** Thursday, June 4th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw07/hw07.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 6 Solutions Review](#problem-1-homework-6-solutions-review-10-pts)
- [Problem 2: Anonymous Feedback](#problem-2-anonymous-feedback-6-pts)
- [Problem 3: The Complete Solution](#problem-3-the-complete-solution-18-pts)
- [Problem 4: Orthogonalization](#problem-4-orthogonalization-27-pts)
- [Problem 5: Same, but Different](#problem-5-same-but-different-13-pts)
- [Problem 6: Putting it into Practice](#problem-6-putting-it-into-practice-8-pts)
- [Problem 7: Billy the Waiter](#problem-7-billy-the-waiter-14-pts)

---

Total Points: 10 + 6 + 18 + 27 + 13 + 8 + 14 = 96

---

## Problem 1: Homework 6 Solutions Review (10 pts)

Review the solutions to Homework 6. Pick **two problem parts** (for example, Problem 2a and Problem 5b) from Homework 6 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 6, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Anonymous Feedback (6 pts)

We'd like to get your feedback on how the course has been going so far, now that we're past the halfway point and Midterm 2 is fast approaching.

You can find the survey [at this link](https://docs.google.com/forms/d/e/1FAIpQLSctsQYk1gGq87DsRU1gwB8eFG4V6vSnb3qBjYaFypRg4qWlZQ/viewform?usp=publish-editor), which you should complete **after you've finished the rest of Homework 7**. Unlike the Homework 3 survey, **it is anonymous**, so feel free to provide candid feedback.

In order to earn the 6 points for Homework 7, Problem 2, include a screenshot of the confirmation message you see after submitting the form. (We consider it an honor code violation to include a screenshot if you didn't actually submit the form!)

Thank you for your feedback once again!

---

## Problem 3: The Complete Solution (18 pts)

Before beginning this problem, make sure you've read both [Chapter 6.3](https://notes.eecs245.org/linear-transformations-and-projections/projecting-onto-column-space/) and [Chapter 6.4](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Consider the matrix <span class="math-inline">\\(A\\)</span> and vector <span class="math-inline">\\(\vec b\\)</span> defined below.

<div class="math-display">
$$
A = \begin{bmatrix}
1 & 1 \\\\
0 & 1 \\\\
2 & -1 \\\\
1 & -1 \\\\
\end{bmatrix}, \quad \vec b = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\\\ 2 \end{bmatrix}
$$
</div>

Find the vector <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimizes <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span>. Show your work, but feel free to use `numpy` to compute some of the matrix operations; [here](https://youtu.be/HZtoekU9NcE?si=X6O8fJ19OdPIgpwq) is a video that walks through how to do this. (We're intentionally using different variables here than in the notes to have you think about the problem in general terms.)

For the remainder of the problem, we will use the same vector <span class="math-inline">\\(\vec b\\)</span>, but instead use the following matrix <span class="math-inline">\\(A\\)</span>.

<div class="math-display">
$$
A = \begin{bmatrix}
1 & 0 & 1 & -4 & 4 \\\\
0 & 2 & 1 & -5 & 3 \\\\
2 & -6 & -1 & 7 & -1 \\\\
1 & -4 & -1 & 6 & -2
\end{bmatrix}
$$
</div>

Note that this new matrix <span class="math-inline">\\(A\\)</span> has **a rank of 2**.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Now, find **one** vector <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimizes <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span> for this new matrix <span class="math-inline">\\(A\\)</span>. Again, show your work. If you've read [Chapter 6.4](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/) closely, this should not require much calculation.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. <em>Hint: Try and do so efficiently, since this is the type of problem we'll see on Midterm 2.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Show that if <span class="math-inline">\\(\vec x'\\)</span> satisfies the normal equation, <span class="math-inline">\\(A^TA \vec x' = A^T \vec b\\)</span>, and <span class="math-inline">\\(\vec x&#95;0 \in \text{nullsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x' + \vec x&#95;0\\)</span> also satisfies the normal equation. <em>Hint: This is two-line solution; we're mostly asking it so that you interalize <strong>what</strong> this means and why it's true.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Describe, using set notation, the complete set of vectors <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimize <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span>. Is this set a subspace?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) There are infinitely many vectors <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimize <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span>. If we try and use code to find a solution, it can't return all of them --- it'll pick a particular one.

In Python, use `np.linalg.lstsq` to find a vector <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimizes <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span>. Include a screenshot of your code and the vector <span class="math-inline">\\(\vec x^{\ast}\\)</span> it returns, and in your PDF, write out the coefficients of <span class="math-inline">\\(\vec x^{\ast}\\)</span> as a vector (in addition to the screenshot). Then, provide an educated guess of **why** you think it picked the <span class="math-inline">\\(\vec x^{\ast}\\)</span> that it did.

</div>
</div>

</div>

---

## Problem 4: Orthogonalization (27 pts)

**Before starting, refer to [Chapter 6.5](https://notes.eecs245.org/linear-transformations-and-projections/gram-schmidt-process/), written just for this problem.** It won't be possible to do this problem without referencing it.

In parts **a)** through **d)**, we'll refer to the vectors <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec v&#95;2 = \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec v&#95;3 = \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) By hand, apply the Gram-Schmidt process to the vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span> to find an orthonormal set of vectors <span class="math-inline">\\(\vec q&#95;1, \vec q&#95;2, \vec q&#95;3\\)</span>. Show your work; you cannot use `numpy` for this.

Then, create the matrix <span class="math-inline">\\(Q = \begin{bmatrix} | &amp; | &amp; | \\\\ \vec q&#95;1 &amp; \vec q&#95;2 &amp; \vec q&#95;3 \\\\ | &amp; | &amp; | \end{bmatrix}\\)</span> and confirm that <span class="math-inline">\\(Q^TQ = I\\)</span>, but that <span class="math-inline">\\(QQ^T \neq I\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Suppose <span class="math-inline">\\(\vec v&#95;4 = \begin{bmatrix} 2 \\\\ 2 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>. If you were to apply the Gram-Schmidt process to the vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3, \vec v&#95;4\\)</span>, what would the vector <span class="math-inline">\\(\vec Q&#95;4\\)</span> be? Why?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Consider <span class="math-inline">\\(\vec y = \begin{bmatrix} 3 \\\\ 1 \\\\ 2 \\\\ 4 \end{bmatrix}\\)</span>. <span class="math-inline">\\(\vec y\\)</span> **is** in <span class="math-inline">\\(\text{span}(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \rbrace) = \text{span}(\lbrace \vec q&#95;1, \vec q&#95;2, \vec q&#95;3 \rbrace)\\)</span>.

Find scalars <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(a\vec q&#95;1 + b\vec q&#95;2 + c\vec q&#95;3 = \vec y\\)</span>, **without** solving a system of 3 equations and 3 unknowns. Instead, use the fact that <span class="math-inline">\\(\vec q&#95;1, \vec q&#95;2, \vec q&#95;3\\)</span> are orthonormal. <em>Hint: There's a relevant problem from Lab 5.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Consider <span class="math-inline">\\(\vec y = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>. Unlike in **c)**, <span class="math-inline">\\(\vec y\\)</span> **is not** in <span class="math-inline">\\(\text{span}(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \rbrace)\\)</span>.

Find the vector in <span class="math-inline">\\(\text{span}(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \rbrace)\\)</span> that is closest to <span class="math-inline">\\(\vec y\\)</span>. **Do not** stack the <span class="math-inline">\\(\vec v&#95;i\\)</span>'s into a matrix <span class="math-inline">\\(X\\)</span> and then use <span class="math-inline">\\(X(X^TX)^{-1}X^T\vec y\\)</span>. Instead, use the fact that <span class="math-inline">\\(\vec q&#95;1, \vec q&#95;2, \vec q&#95;3\\)</span> are orthonormal and have the same span as <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span>. How does this simplify the problem?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Open the **the supplemental Jupyter Notebook** we've created for Homework 7, which can either be found [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw07/hw07.ipynb) in the course GitHub repository, or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw07%2Fhw07.ipynb&branch=main) on DataHub.

There, you're asked to implement the function `orthogonalize`, which takes in an <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(V\\)</span> whose columns are linearly independent, and returns a matrix <span class="math-inline">\\(Q\\)</span> whose columns are orthonormal and have the same span as <span class="math-inline">\\(V\\)</span>. This problem is **not autograded**. Rather, in your submission to this part, include a screenshot of your implementation and sample output in your PDF for Homework 7.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) A QR decomposition of a matrix <span class="math-inline">\\(A\\)</span> is a factorization of the form

<div class="math-display">
$$
A = QR
$$
</div>

where <span class="math-inline">\\(Q\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix with orthonormal columns and <span class="math-inline">\\(R\\)</span> is an <span class="math-inline">\\(d \times d\\)</span> **upper triangular** matrix (a matrix that has 0s below the diagonal).

For example, if <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 1 &amp; 1 \\\\ -1 &amp; 0 &amp; 1 \\\\ 1 &amp; 1 &amp; 2 \end{bmatrix}\\)</span>, a <span class="math-inline">\\(QR\\)</span> decomposition of <span class="math-inline">\\(A\\)</span> is

<div class="math-display">
$$
A = \begin{bmatrix} 1 & 1 & 1 \\\\ -1 & 0 & 1 \\\\ 1 & 1 & 2 \end{bmatrix} =
  \underbrace{\begin{bmatrix}
    1 / \sqrt{3} & 1 / \sqrt{6} & -1 / \sqrt{2} \\\\
    -1 / \sqrt{3} & 2 / \sqrt{6} & 0 \\\\
    1 / \sqrt{3} & 1 / \sqrt{6} & 1 / \sqrt{2}
  \end{bmatrix}}_{Q}
  \underbrace{\begin{bmatrix}
    \sqrt{3} & 2 \sqrt{3} / 3 & 2 \sqrt{3} / 3 \\\\
    0 & \sqrt{6} / 3 & 5 \sqrt{6} / 6 \\\\
    0 & 0 & 1 / \sqrt{2}
  \end{bmatrix}}_{R}
$$
</div>

Finding the <span class="math-inline">\\(Q\\)</span> in a <span class="math-inline">\\(QR\\)</span> decomposition is straightforward: apply Gram-Schmidt to the columns of <span class="math-inline">\\(A\\)</span>, assuming <span class="math-inline">\\(A\\)</span>'s columns are linearly independent. The question is how to find <span class="math-inline">\\(R\\)</span>.

1.  In the supplemental Jupyter Notebook, we've defined an arbitrary matrix <span class="math-inline">\\(A\\)</span> and call your `orthogonalize` function on it, and give you hints as to how to find <span class="math-inline">\\(R\\)</span>. Using the experimentation there, and what you know about <span class="math-inline">\\(Q\\)</span>, **explain how to find <span class="math-inline">\\(R\\)</span>.**

2.  Find a <span class="math-inline">\\(QR\\)</span> decomposition of <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 &amp; 0 \\\\ 1 &amp; 1 &amp; 0 \\\\ 0 &amp; 1 &amp; 1 \\\\ 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>. Note that the columns of <span class="math-inline">\\(A\\)</span> are made up of the same three vectors you worked with in parts **a)** through **d)** of this problem.

3.  Given **a** <span class="math-inline">\\(QR\\)</span> decomposition of <span class="math-inline">\\(A\\)</span>, explain how to find **another** <span class="math-inline">\\(QR\\)</span> decomposition of <span class="math-inline">\\(A\\)</span> with a (slightly) different <span class="math-inline">\\(Q\\)</span> and/or <span class="math-inline">\\(R\\)</span>.

</div>
</div>

</div>

---

## Problem 5: Same, but Different (13 pts)

In [Chapter 2.4](https://notes.eecs245.org/simple-linear-regression/correlation/#correlation-and-the-regression-line/), we were introduced to one of many formulas for the optimal slope, <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>, and optimal intercept, <span class="math-inline">\\(w&#95;0^{\ast}\\)</span>, for the simple linear regression model <span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i\\)</span> when using squared loss:

<div class="math-display">
$$
w_1^* = r \frac{\sigma_{y}}{\sigma_{x}} \qquad w_0^* = \bar y - w_1^* \bar x
$$
</div>

The end goal of Chapters 3 through 6 has been to give us the tools to revisit the simple linear regression model in terms of linear algebra, so that we can extend our model to allow for multiple input variables. As we see in [Chapter 7.1](https://notes.eecs245.org/regression-using-linear-algebra/regression-using-linear-algebra/), the solution is to define the <span class="math-inline">\\(n \times 2\\)</span> "**design matrix**" <span class="math-inline">\\(X\\)</span> and observation vector <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> as follows:

<div class="math-display">
$$
X = \begin{bmatrix} 1 & x_1 \\\\ 1 & x_2 \\\\ \vdots & \vdots \\\\ 1 & x_n \end{bmatrix}, \quad \vec y = \begin{bmatrix} y_1 \\\\ y_2 \\\\ \vdots \\\\ y_n \end{bmatrix}
$$
</div>

Then, the vector containing the optimal model parameters is

<div class="math-display">
$$
\vec w^* = (X^TX)^{-1}X^T \vec y = \begin{bmatrix} w_0^* \\\\ w_1^* \end{bmatrix}
$$
</div>

 **It's not immediately obvious why the components of <span class="math-inline">\\(\vec w^{\ast}\\)</span> should have anything to do with the correlation, means of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>, and standard deviations of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>.** In this problem, we will prove that both of these formulations are equivalent, for any dataset <span class="math-inline">\\((x&#95;1, y&#95;1)\\)</span>, <span class="math-inline">\\((x&#95;2, y&#95;2)\\)</span>, \..., <span class="math-inline">\\((x&#95;n, y&#95;n)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Express the matrix <span class="math-inline">\\((X^TX)^{-1}\\)</span> using constants and/or summations involving <span class="math-inline">\\(x&#95;i\\)</span> and/or <span class="math-inline">\\(y&#95;i\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Prove that

<div class="math-display">
$$
(X^TX)^{-1} = \frac{1}{n\sigma_x^2} \begin{bmatrix} \sigma_x^2 + \bar{x}^2 & -\bar{x} \\\\ -\bar{x} & 1 \end{bmatrix}
$$
</div>

<em>Hint: Start by proving <span class="math-inline">\\(\sum&#95;{i = 1}^n x&#95;i^2 = n \sigma&#95;x^2 + n \bar{x}^2\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Finally, prove that

<div class="math-display">
$$
(X^TX)^{-1}X^T \vec{y} = \begin{bmatrix} \bar{y} - r \frac{\sigma_y}{\sigma_x} \bar{x} \\\\ r \frac{\sigma_y}{\sigma_x}  \end{bmatrix}
$$
</div>

<em>Hint: Start by proving that <span class="math-inline">\\(\sum&#95;{i=1}^n x&#95;i y&#95;i = nr \sigma&#95;x \sigma&#95;y + n \bar{x}\bar{y}\\)</span>.</em>

Note that the second component of the vector above is <span class="math-inline">\\(w&#95;1^{\ast} =  r \frac{\sigma&#95;y}{\sigma&#95;x}\\)</span> and the first component of the vector above is <span class="math-inline">\\(w&#95;0^{\ast} = \bar{y} -  r \frac{\sigma&#95;y}{\sigma&#95;x} \bar{x} = \bar{y} - w&#95;1^{\ast} \bar{x}\\)</span>, as we first saw in Chapter 2.4! I think this is beautiful.

</div>
</div>

</div>

---

## Problem 6: Putting it into Practice (8 pts)

This problem asks you to apply the concepts in [Chapter 7.2](https://notes.eecs245.org/regression-using-linear-algebra/multiple-linear-regression/), and follows the last problem.

Suppose we'd like to fit a hypothesis function of the form <span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i^2\\)</span>. Notice the squared term; this is **not** a simple linear regression line.

To do so, we'll find the optimal parameter vector <span class="math-inline">\\(\vec w^{\ast}\\)</span> that satisfies the normal equations. The first 5 rows of our dataset are as follows, though note that our dataset has <span class="math-inline">\\(n\\)</span> rows in total.

<div class="math-display">
$$
\begin{array}{c|c}
x_i & y_i \\\\
\hline
2   & 4 \\\\
-1  & 2 \\\\
3   & 5 \\\\
-7  & 3 \\\\
3   & -7 \\\\
\vdots & \vdots
\end{array}
$$
</div>

Suppose <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> have a mean of <span class="math-inline">\\(\bar{x} = 5\\)</span> and a variance of <span class="math-inline">\\(\sigma&#95;x^2 = 8\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Write the first five rows of the design matrix, <span class="math-inline">\\(X\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Suppose that after solving the normal equations, we find <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 5 \\\\ -2 \end{bmatrix}\\)</span>. Find the augmented feature vector <span class="math-inline">\\(\text{Aug}(\vec x&#95;3)\\)</span> and squared loss for row 3 of the dataset.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(X&#95;\text{tri} = 3X\\)</span>, where <span class="math-inline">\\(X\\)</span> is the full design matrix for our dataset with <span class="math-inline">\\(n\\)</span> rows. Determine the bottom-left value in the matrix <span class="math-inline">\\(X&#95;\text{tri}^TX&#95;\text{tri}\\)</span>, i.e. the value in the second row and first column. Your answer should be an expression involving <span class="math-inline">\\(n\\)</span>. <em>Hint: You can use any of the hints or results from Problem 2 without needing to re-prove them.</em>

</div>
</div>

</div>

---

## Problem 7: Billy the Waiter (14 pts)

This problem involves writing code and submitting it to the Gradescope autograder. The goal of this problem is to give you a taste of how linear algebra can be used to implement linear regression in code, and show you how to build models that involve multiple features (including categorical variables).

Open the **the supplemental Jupyter Notebook** we've created for Homework 7, which can either be found [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw07/hw07.ipynb) in the course GitHub repository, or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw07%2Fhw07.ipynb&branch=main) on DataHub.

**This problem is entirely autograded; to receive credit for Problem 7 of this homework, you'll need to submit your completed notebook to the autograder on Gradescope.** Your submission time for Homework 7 is the **latter** of your PDF and code submission times.

{% endraw %}
