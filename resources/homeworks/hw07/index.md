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
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw07/hw07-solutions.pdf" target="_blank">Solutions PDF ✅</a>
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

<details markdown="1"><summary>Solution</summary>

</details>

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

<details markdown="1"><summary>Solution</summary>

Given

<div class="math-display">
$$
A =
\begin{bmatrix}
1 & 1 \\\\
0 & 1 \\\\
2 & -1 \\\\
1 & -1
\end{bmatrix}
\qquad
\vec{b} =
\begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\\\ 2 \end{bmatrix}
$$
</div>

 and <span class="math-inline">\\(\vec{x} \in \mathbb{R}^2\\)</span>, we want the vector <span class="math-inline">\\(\vec{x}^{\ast}\\)</span> that makes the squared error <span class="math-inline">\\(\lVert \vec{b} - A\vec{x} \rVert^2\\)</span> as small as possible.

Because <span class="math-inline">\\(A\\)</span> has two linearly independent columns, its columns form a 2D subspace of <span class="math-inline">\\(\mathbb{R}^4\\)</span>, and there is a *unique* least-squares solution. The standard way to get it is to use the normal equations

<div class="math-display">
$$
A^T A \vec{x}^* = A^T \vec{b}
$$
</div>

First let's find <span class="math-inline">\\(A^T A\\)</span>:

<div class="math-display">
$$
A^T =
\begin{bmatrix}
1 & 0 & 2 & 1 \\\\
1 & 1 & -1 & -1
\end{bmatrix}
\qquad
A^T A =
\begin{bmatrix}
1 & 0 & 2 & 1 \\\\
1 & 1 & -1 & -1
\end{bmatrix}
\begin{bmatrix}
1 & 1 \\\\
0 & 1 \\\\
2 & -1 \\\\
1 & -1
\end{bmatrix}
=
\begin{bmatrix}
6 & -2 \\\\
-2 & 4
\end{bmatrix}
$$
</div>

 Now we'll find the right-hand side <span class="math-inline">\\(A^T \vec{b}\\)</span>:

<div class="math-display">
$$
A^T \vec{b}
=
\begin{bmatrix}
1 & 0 & 2 & 1 \\\\
1 & 1 & -1 & -1
\end{bmatrix}
\begin{bmatrix}
1 \\\\ 2 \\\\ 3 \\\\ 2
\end{bmatrix}
=
\begin{bmatrix}
9 \\\\ -2
\end{bmatrix}
$$
</div>

So the normal equation becomes

<div class="math-display">
$$
\begin{bmatrix}
6 & -2 \\\\
-2 & 4
\end{bmatrix}
\begin{bmatrix}
x_1^* \\\\[2pt] x_2^*
\end{bmatrix}
=
\begin{bmatrix}
9 \\\\[2pt] -2
\end{bmatrix}
$$
</div>

To solve, we invert <span class="math-inline">\\(A^T A\\)</span>. The determinant is <span class="math-inline">\\(6 \cdot 4 - (-2)(-2) = 20\\)</span>, so

<div class="math-display">
$$
(A^T A)^{-1} = \frac{1}{20}
\begin{bmatrix}
4 & 2 \\\\
2 & 6
\end{bmatrix}
$$
</div>

Then:

<div class="math-display">
$$
\vec{x}^* = (A^T A)^{-1} A^T \vec{b}
= \frac{1}{20}
\begin{bmatrix}
4 & 2 \\\\
2 & 6
\end{bmatrix}
\begin{bmatrix}
9 \\\\ -2
\end{bmatrix}
= \frac{1}{20}
\begin{bmatrix}
36 - 4 \\\\
18 - 12
\end{bmatrix}
= \frac{1}{20}
\begin{bmatrix}
32 \\\\ 6
\end{bmatrix}
=
\begin{bmatrix}
\frac{8}{5} \\\\[4pt]
\frac{3}{10}
\end{bmatrix}
$$
</div>

So the least-squares minimizer is

<div class="math-display">
$$
\boxed{
\vec{x}^* =
\begin{bmatrix}
\frac{8}{5} \\\\[4pt]
\frac{3}{10}
\end{bmatrix}
}
$$
</div>

Geometrically, <span class="math-inline">\\(A\vec{x}^{\ast}\\)</span> is the projection of <span class="math-inline">\\(\vec{b}\\)</span> onto the column space of <span class="math-inline">\\(A\\)</span>, and <span class="math-inline">\\(\vec{x}^{\ast}\\)</span> are the coordinates of that projection in the basis given by the two columns of <span class="math-inline">\\(A\\)</span>.

</details>

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

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(A\\)</span> has rank 2 but 5 columns, the normal equation

<div class="math-display">
$$
A^T A \vec{x} = A^T \vec{b}
$$
</div>

 do not have a unique solution, and there are infinitely many vectors <span class="math-inline">\\(\vec{x}^{\ast}\\)</span> that minimize <span class="math-inline">\\(\lVert \vec{b} - A\vec{x}\rVert^2\\)</span>.

To find one such vector, we can keep only two linearly independent columns of <span class="math-inline">\\(A\\)</span> --- here, we use columns 3 and 1, in that order --- since removing dependent columns does not change <span class="math-inline">\\(\text{colsp}(A)\\)</span>.

<div class="math-display">
$$
A' =
\begin{bmatrix}
1 & 1 \\\\[3pt]
1 & 0 \\\\[3pt]
-1 & 2 \\\\[3pt]
-1 & 1
\end{bmatrix}
\qquad
\vec{b} =
\begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\\\ 2 \end{bmatrix}
$$
</div>

This matrix has the same two columns as in part **a)**, but in the opposite order, so the least-squares coefficients are also swapped relative to part **a)**. Therefore,

<div class="math-display">
$$
\vec{x}' =
\begin{bmatrix}
\frac{3}{10} \\\\[3pt]
\frac{8}{5}
\end{bmatrix}
$$
</div>

To extend back to the full 5-dimensional <span class="math-inline">\\(\vec{x}\\)</span>, we place these coefficients in entries 3 and 1, respectively, and set the others to <span class="math-inline">\\(0\\)</span>:

<div class="math-display">
$$
\boxed{
\vec{x}^* =
\begin{bmatrix}
\frac{3}{10} \\\\[3pt]
0 \\\\[3pt]
\frac{8}{5} \\\\[3pt]
0 \\\\[3pt]
0
\end{bmatrix}
}
$$
</div>

This <span class="math-inline">\\(\vec{x}^{\ast}\\)</span> satisfies the normal equation <span class="math-inline">\\(A^T A \vec{x} = A^T \vec{b}\\)</span> and therefore minimizes <span class="math-inline">\\(\lVert \vec{b} - A\vec{x}\rVert^2\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. <em>Hint: Try and do so efficiently, since this is the type of problem we'll see on Midterm 2.</em>

<details markdown="1"><summary>Solution</summary>

To find a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, we look for all vectors <span class="math-inline">\\(\vec{x}\\)</span> that satisfy

<div class="math-display">
$$
A\vec{x} = \vec{0}
\quad \text{where }
A =
\begin{bmatrix}
1 & 0 & 1 & -4 & 4 \\\\
0 & 2 & 1 & -5 & 3 \\\\
2 & -6 & -1 & 7 & -1 \\\\
1 & -4 & -1 & 6 & -2
\end{bmatrix}
$$
</div>

Since <span class="math-inline">\\(\text{rank}(A) = 2\\)</span> and <span class="math-inline">\\(A\\)</span> has 5 columns, the rank-nullity theorem says

<div class="math-display">
$$
\dim(\text{nullsp}(A)) = 5 - 2 = 3
$$
</div>

So, a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span> will have 3 vectors. The easy way to find those three vectors is to determine how to write <span class="math-inline">\\(A\\)</span>'s linearly dependent columns as linear combinations of its linearly independent columns. Columns 1 and 3 are linearly independent (they are the same two columns as in part **a)**). By inspection --- that is, by guessing and checking --- we can find that:

-   <span class="math-inline">\\(\text{column 2} = -2 (\text{column 1}) + 2 (\text{column 3})\\)</span>, so



<div class="math-display">
$$
A \begin{bmatrix} -2 \\\\ -1 \\\\ 2 \\\\ 0 \\\\ 0 \end{bmatrix} = \vec 0
$$
</div>

-   <span class="math-inline">\\(\text{column 4} = 1 (\text{column 1}) - 5 (\text{column 3})\\)</span>, so



<div class="math-display">
$$
A \begin{bmatrix} 1 \\\\ 0 \\\\ -5 \\\\ -1 \\\\ 0 \end{bmatrix} = \vec 0
$$
</div>

-   <span class="math-inline">\\(\text{column 5} = 1 (\text{column 1}) + 3 (\text{column 3})\\)</span>, so



<div class="math-display">
$$
A \begin{bmatrix} 1 \\\\ 0 \\\\ 3 \\\\ 0 \\\\ -1 \end{bmatrix} = \vec 0
$$
</div>

So, a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span> is given by

<div class="math-display">
$$
\boxed{\left\{\begin{bmatrix} -2 \\\\ -1 \\\\ 2 \\\\ 0 \\\\ 0 \end{bmatrix},
\begin{bmatrix} 1 \\\\ 0 \\\\ -5 \\\\ -1 \\\\ 0 \end{bmatrix},
\begin{bmatrix} 1 \\\\ 0 \\\\ 3 \\\\ 0 \\\\ -1 \end{bmatrix}
\right\}}
$$
</div>

Any linear combination of these vectors, when multiplied by <span class="math-inline">\\(A\\)</span>, will result in the zero vector.

This also means that

<div class="math-display">
$$
\text{nullsp}(A) = \text{span}\left( \left\{
\begin{bmatrix} -2 \\\\ -1 \\\\ 2 \\\\ 0 \\\\ 0 \end{bmatrix},
\begin{bmatrix} 1 \\\\ 0 \\\\ -5 \\\\ -1 \\\\ 0 \end{bmatrix},
\begin{bmatrix} 1 \\\\ 0 \\\\ 3 \\\\ 0 \\\\ -1 \end{bmatrix}
\right\} \right)
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Show that if <span class="math-inline">\\(\vec x'\\)</span> satisfies the normal equation, <span class="math-inline">\\(A^TA \vec x' = A^T \vec b\\)</span>, and <span class="math-inline">\\(\vec x&#95;0 \in \text{nullsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x' + \vec x&#95;0\\)</span> also satisfies the normal equation. <em>Hint: This is two-line solution; we're mostly asking it so that you interalize <strong>what</strong> this means and why it's true.</em>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\vec x'\\)</span> satisfies the normal equation, then

<div class="math-display">
$$
A^T A \vec x' = A^T \vec b
$$
</div>

 By the definition of the null space, if <span class="math-inline">\\(\vec x&#95;0 \in \text{nullsp}(A)\\)</span>, then <span class="math-inline">\\(A\vec x&#95;0 = \vec 0\\)</span>. Then:

<div class="math-display">
$$
A^T A (\vec x' + \vec x_0)
= A^T (A\vec x' + A\vec x_0)
= A^T A\vec x' + A^T \vec 0
= A^T A\vec x' + \vec 0
= A^T \vec b.
$$
</div>

 Thus, <span class="math-inline">\\(\vec x' + \vec x&#95;0\\)</span> also satisfies the normal equation. This means adding any vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span> to a solution <span class="math-inline">\\(\vec x'\\)</span> of the normal equation gives another valid solution.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Describe, using set notation, the complete set of vectors <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimize <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span>. Is this set a subspace?

<details markdown="1"><summary>Solution</summary>

The complete set of vectors that minimize <span class="math-inline">\\(\lVert \vec{b} - A\vec{x} \rVert^2\\)</span> is all vectors that result from starting with a particular solution <span class="math-inline">\\(\vec x'\\)</span> and adding any vector in the null space of <span class="math-inline">\\(A\\)</span>.

<div class="math-display">
$$
\boxed{
\{\;\vec{x}^* + \vec{x}_0 \mid \vec{x}_0 \in \text{nullsp}(A)\;\}
}
$$
</div>

This set is *not* a subspace, because it does not necessarily pass through the origin (for instance, <span class="math-inline">\\(\vec{x}^{\ast}\\)</span> itself may not be <span class="math-inline">\\(\vec{0}\\)</span>).

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) There are infinitely many vectors <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimize <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span>. If we try and use code to find a solution, it can't return all of them --- it'll pick a particular one.

In Python, use `np.linalg.lstsq` to find a vector <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimizes <span class="math-inline">\\(\lVert \vec b - A \vec x \rVert^2\\)</span>. Include a screenshot of your code and the vector <span class="math-inline">\\(\vec x^{\ast}\\)</span> it returns, and in your PDF, write out the coefficients of <span class="math-inline">\\(\vec x^{\ast}\\)</span> as a vector (in addition to the screenshot). Then, provide an educated guess of **why** you think it picked the <span class="math-inline">\\(\vec x^{\ast}\\)</span> that it did.

<details markdown="1"><summary>Solution</summary>

When fitting a linear model, the goal of `np.linalg.lstsq` is to find a weight vector <span class="math-inline">\\(\vec{w}^{\ast}\\)</span> that minimizes

<div class="math-display">
$$
\lVert \vec{b} - A\vec{w} \rVert^2
$$
</div>

 If <span class="math-inline">\\(A^TA\\)</span> is invertible (that is, if the columns of <span class="math-inline">\\(A\\)</span> are linearly independent), there is exactly one solution:

<div class="math-display">
$$
\vec{w}^* = (A^TA)^{-1}A^T\vec{b}
$$
</div>

However, if <span class="math-inline">\\(A\\)</span> does not have full rank, then <span class="math-inline">\\(A^TA\\)</span> cannot be inverted, and there are infinitely many <span class="math-inline">\\(\vec{w}\\)</span> that give the same minimum error.

In this case, `np.linalg.lstsq` uses the **singular value decomposition (SVD)** of <span class="math-inline">\\(A\\)</span> to find a stable and well-defined <span class="math-inline">\\(\vec{w}^{\ast}\\)</span>. Without getting into the details, know that among all possible minimizers, this particular <span class="math-inline">\\(\vec{w}^{\ast}\\)</span> also has the smallest possible length <span class="math-inline">\\(\lVert \vec{w} \rVert\\)</span>. In other words, it fits the data as well as possible while keeping the parameter vector as small as possible. It is called the "min-norm" solution.

</details>

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

<details markdown="1"><summary>Solution</summary>

-   **Iteration 1**: Set <span class="math-inline">\\(\vec Q&#95;1 = \vec v&#95;1 = \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>.

-   **Iteration 2**: Set <span class="math-inline">\\(\vec Q&#95;2 = \vec v&#95;2 - \text{proj}&#95;{\vec Q&#95;1}(\vec v&#95;2) = \vec v&#95;2 - \frac{\vec v&#95;2 \cdot \vec Q&#95;1}{\vec Q&#95;1 \cdot \vec Q&#95;1} \vec Q&#95;1 = \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} - \frac{1}{2} \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix} = \begin{bmatrix} -1/2 \\\\ 1/2 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>.

-   **Iteration 3**: Set <span class="math-inline">\\(\vec Q&#95;3 = \vec v&#95;3 - \text{proj}&#95;{\vec Q&#95;1}(\vec v&#95;3) - \text{proj}&#95;{\vec Q&#95;2}(\vec v&#95;3)\\)</span>:



<div class="math-display">
$$
\begin{align*}
    \vec Q_3 &= \vec v_3 - \text{proj}_{\vec Q_1}(\vec v_3)- \text{proj}_{\vec Q_2}(\vec v_3) \\\\
    &= \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix} - \underbrace{\frac{\vec v_3 \cdot \vec Q_1}{\vec Q_1 \cdot \vec Q_1} \vec Q_1}_{\vec v_3 \cdot \vec Q_1 = 0} - \frac{\vec v_3 \cdot \vec Q_2}{\vec Q_2 \cdot \vec Q_2} \vec Q_2 \\\\
    &= \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix} - \frac{\vec v_3 \cdot \vec Q_2}{\vec Q_2 \cdot \vec Q_2} \vec Q_2 \\\\
    &= \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix} - \frac{\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix} \cdot \begin{bmatrix} -1/2 \\\\ 1/2 \\\\ 1 \\\\ 0 \end{bmatrix}}{\begin{bmatrix} -1/2 \\\\ 1/2 \\\\ 1 \\\\ 0 \end{bmatrix} \cdot \begin{bmatrix} -1/2 \\\\ 1/2 \\\\ 1 \\\\ 0 \end{bmatrix}} \begin{bmatrix} -1/2 \\\\ 1/2 \\\\ 1 \\\\ 0 \end{bmatrix} \\\\
    &= \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix} - \frac{2}{3} \begin{bmatrix} -1/2 \\\\ 1/2 \\\\ 1 \\\\ 0 \end{bmatrix} = \begin{bmatrix} 1/3 \\\\ -1/3 \\\\ 1/3 \\\\ 1 \end{bmatrix}
    \end{align*}
$$
</div>

So,

<div class="math-display">
$$
\vec Q_1 = \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix}, \quad \vec Q_2 = \begin{bmatrix} -1/2 \\\\ 1/2 \\\\ 1 \\\\ 0 \end{bmatrix}, \quad \vec Q_3 = \begin{bmatrix} 1/3 \\\\ -1/3 \\\\ 1/3 \\\\ 1 \end{bmatrix}
$$
</div>

Finally, we need to normalize the vectors to have length 1. Doing so gives

<div class="math-display">
$$
\boxed{\vec q_1 = \frac{\vec Q_1}{\lVert \vec Q_1 \rVert} = \begin{bmatrix} 1 /\sqrt{2} \\\\ 1 /\sqrt{2} \\\\ 0 \\\\ 0 \end{bmatrix}, \quad \vec q_2 = \frac{\vec Q_2}{\lVert \vec Q_2 \rVert} = \begin{bmatrix} -1 /\sqrt{6} \\\\ 1 /\sqrt{6} \\\\ 2 /\sqrt{6} \\\\ 0 \end{bmatrix}, \quad \vec q_3 = \frac{\vec Q_3}{\lVert \vec Q_3 \rVert} = \begin{bmatrix} \sqrt{3}/6 \\\\ -\sqrt{3}/6 \\\\ \sqrt{3}/6 \\\\ \sqrt{3}/2 \end{bmatrix}}
$$
</div>

(Tip: Instead of converting <span class="math-inline">\\(\vec Q&#95;3 = \begin{bmatrix} 1/3 \\\\ -1/3 \\\\ 1/3 \\\\ 1 \end{bmatrix}\\)</span> to a unit vector, it's easier to instead convert <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \\\\ 1 \\\\ 3 \end{bmatrix}\\)</span>, which points in the same direction as <span class="math-inline">\\(\vec Q&#95;3\\)</span>, to a unit vector. The result will be the same in both cases, but by multiplying through by 3 you get to avoid messier fractions.)

Finally, we need to construct <span class="math-inline">\\(Q = \begin{bmatrix} 1/\sqrt{2} &amp; -1/\sqrt{6} &amp; \sqrt{3}/6 \\\\ 1/\sqrt{2} &amp; 1/\sqrt{6} &amp; -\sqrt{3}/6 \\\\ 0 &amp; 2/\sqrt{6} &amp; \sqrt{3}/6 \\\\ 0 &amp; 0 &amp; \sqrt{3}/2 \end{bmatrix}\\)</span>. Indeed, <span class="math-inline">\\(Q^TQ = I\\)</span> because all pairs of columns are orthogonal and have length 1. However, <span class="math-inline">\\(QQ^T \neq I\\)</span> because, for instance, row 3 and row 4 are not orthogonal, so <span class="math-inline">\\((QQ^T)&#95;{3, 4} = 3/12 = 1/4 \neq 0\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Suppose <span class="math-inline">\\(\vec v&#95;4 = \begin{bmatrix} 2 \\\\ 2 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>. If you were to apply the Gram-Schmidt process to the vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3, \vec v&#95;4\\)</span>, what would the vector <span class="math-inline">\\(\vec Q&#95;4\\)</span> be? Why?

<details markdown="1"><summary>Solution</summary>

Note that <span class="math-inline">\\(\vec v&#95;4 = \begin{bmatrix} 2 \\\\ 2 \\\\ 3 \\\\ 3 \end{bmatrix} = 2 \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix} + 3 \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix} = 2 \vec v&#95;1 + 3 \vec v&#95;3\\)</span>, meaning <span class="math-inline">\\(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3, \vec v&#95;4 \rbrace\\)</span> are linearly dependent.

In the previous part, we already applied Gram-Schmidt to the vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span>, giving us the orthonormal vectors <span class="math-inline">\\(\vec q&#95;1, \vec q&#95;2, \vec q&#95;3\\)</span>. If we were to continue the Gram-Schmidt process for a fourth iteration, we'd have

<div class="math-display">
$$
\vec Q_4 = \vec v_4 - \text{proj}_{\vec Q_1}(\vec v_4) - \text{proj}_{\vec Q_2}(\vec v_4) - \text{proj}_{\vec Q_3}(\vec v_4)
$$
</div>

Gram-Schmidt already gave us <span class="math-inline">\\(Q = \begin{bmatrix} 1/\sqrt{2} &amp; -1/\sqrt{6} &amp; \sqrt{3}/6 \\\\ 1/\sqrt{2} &amp; 1/\sqrt{6} &amp; -\sqrt{3}/6 \\\\ 0 &amp; 2/\sqrt{6} &amp; \sqrt{3}/6 \\\\ 0 &amp; 0 &amp; \sqrt{3}/2 \end{bmatrix}\\)</span>, which has a column space that is equal to the span of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Consider <span class="math-inline">\\(\vec y = \begin{bmatrix} 3 \\\\ 1 \\\\ 2 \\\\ 4 \end{bmatrix}\\)</span>. <span class="math-inline">\\(\vec y\\)</span> **is** in <span class="math-inline">\\(\text{span}(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \rbrace) = \text{span}(\lbrace \vec q&#95;1, \vec q&#95;2, \vec q&#95;3 \rbrace)\\)</span>.

Find scalars <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(a\vec q&#95;1 + b\vec q&#95;2 + c\vec q&#95;3 = \vec y\\)</span>, **without** solving a system of 3 equations and 3 unknowns. Instead, use the fact that <span class="math-inline">\\(\vec q&#95;1, \vec q&#95;2, \vec q&#95;3\\)</span> are orthonormal. <em>Hint: There's a relevant problem from Lab 5.</em>

<details markdown="1"><summary>Solution</summary>

The main idea here is that to write <span class="math-inline">\\(\vec y\\)</span> as a linear combination of <span class="math-inline">\\(\vec q&#95;1\\)</span>, <span class="math-inline">\\(\vec q&#95;2\\)</span>, and <span class="math-inline">\\(\vec q&#95;3\\)</span>, we can project <span class="math-inline">\\(\vec y\\)</span> onto each of these vectors **individually** and then use the corresponding coefficients to write <span class="math-inline">\\(\vec y\\)</span> as a linear combination of all three.

Remember, <span class="math-inline">\\(\text{proj}&#95;{\vec q&#95;i}(\vec y) = \frac{\vec y \cdot \vec q&#95;i}{\vec q&#95;i \cdot \vec q&#95;i} \vec q&#95;i\\)</span>, but since each <span class="math-inline">\\(\vec q&#95;i\\)</span> is a unit vector, we have <span class="math-inline">\\(\text{proj}&#95;{\vec q&#95;i}(\vec y) = (\vec y \cdot \vec q&#95;i) \vec q&#95;i\\)</span>. So,

<div class="math-display">
$$
\vec y = \text{proj}_{\vec q_1}(\vec y) + \text{proj}_{\vec q_2}(\vec y) + \text{proj}_{\vec q_3}(\vec y)
$$
</div>

<div class="math-display">
$$
= \underbrace{(\vec y \cdot \vec q_1)}_a \vec q_1 + \underbrace{(\vec y \cdot \vec q_2)}_b \vec q_2 + \underbrace{(\vec y \cdot \vec q_3)}_c \vec q_3 = a \vec q_1 + b \vec q_2 + c \vec q_3
$$
</div>

If this idea seems like it's coming out of nowhere, review the relevant projection activity from Lab 4.

So,

<div class="math-display">
$$
\begin{align*}
a &= \vec y \cdot \vec q_1 = \begin{bmatrix} 3 \\\\ 1 \\\\ 2 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} 1/\sqrt{2} \\\\ 1/\sqrt{2} \\\\ 0 \\\\ 0 \end{bmatrix} = 4/\sqrt{2} = \boxed{2\sqrt{2}} \\\\
b &= \vec y \cdot \vec q_2 = \begin{bmatrix} 3 \\\\ 1 \\\\ 2 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} -1/\sqrt{6} \\\\ 1/\sqrt{6} \\\\ 2/\sqrt{6} \\\\ 0 \end{bmatrix} = \boxed{2/\sqrt{6}} \\\\
c &= \vec y \cdot \vec q_3 = \begin{bmatrix} 3 \\\\ 1 \\\\ 2 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} \sqrt{3}/6 \\\\ -\sqrt{3}/6 \\\\ \sqrt{3}/6 \\\\ \sqrt{3}/2 \end{bmatrix} = \boxed{8\sqrt{3}/3}
\end{align*}
$$
</div>

**Notice that <span class="math-inline">\\(Q^T \vec y\\)</span> is a vector containing <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span>, since <span class="math-inline">\\(Q^T \vec y\\)</span> contains the dot product of each of <span class="math-inline">\\(Q^T\\)</span>'s rows (which are <span class="math-inline">\\(Q\\)</span>'s columns) with <span class="math-inline">\\(\vec y\\)</span>.**

Let's test out our logic in Python.

<div style="text-align: center;">
<img src="imgs/q4-ss1.png" alt="image" style="width: 80%; max-width: 100%;">
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Consider <span class="math-inline">\\(\vec y = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span>. Unlike in **c)**, <span class="math-inline">\\(\vec y\\)</span> **is not** in <span class="math-inline">\\(\text{span}(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \rbrace)\\)</span>.

Find the vector in <span class="math-inline">\\(\text{span}(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \rbrace)\\)</span> that is closest to <span class="math-inline">\\(\vec y\\)</span>. **Do not** stack the <span class="math-inline">\\(\vec v&#95;i\\)</span>'s into a matrix <span class="math-inline">\\(X\\)</span> and then use <span class="math-inline">\\(X(X^TX)^{-1}X^T\vec y\\)</span>. Instead, use the fact that <span class="math-inline">\\(\vec q&#95;1, \vec q&#95;2, \vec q&#95;3\\)</span> are orthonormal and have the same span as <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span>. How does this simplify the problem?

<details markdown="1"><summary>Solution</summary>

Recall, the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{span}(\lbrace \vec q&#95;1, \vec q&#95;2, \vec q&#95;3 \rbrace)\\)</span> is given by

<div class="math-display">
$$
\vec p = \underbrace{Q(Q^TQ)^{-1}Q^T}_P\vec y
$$
</div>

 Since <span class="math-inline">\\(Q^TQ = I\\)</span>, we have that

<div class="math-display">
$$
\vec p = QQ^T \vec y
$$
</div>

If <span class="math-inline">\\(Q\\)</span>'s rows were orthonormal, then <span class="math-inline">\\(QQ^T = I\\)</span>, but that's not the case here. Instead, <span class="math-inline">\\(\vec p = QQ^T \vec y\\)</span>.

<div class="math-display">
$$
QQ^T = \begin{bmatrix} 3/4 & 1/4 & -1/4 & 1/4 \\\\ 1/4 & 3/4 & 1/4 & -1/4 \\\\ -1/4 & 1/4 & 3/4 & 1/4 \\\\ 1/4 & -1/4 & 1/4 & 3/4 \end{bmatrix}
$$
</div>

<div class="math-display">
$$
\implies \vec p = QQ^T \vec y =  \begin{bmatrix} 3/4 & 1/4 & -1/4 & 1/4 \\\\ 1/4 & 3/4 & 1/4 & -1/4 \\\\ -1/4 & 1/4 & 3/4 & 1/4 \\\\ 1/4 & -1/4 & 1/4 & 3/4 \end{bmatrix} \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\\\ 4 \end{bmatrix} = \begin{bmatrix} 3/2 \\\\ 3/2 \\\\ 7/2 \\\\ 7/2 \end{bmatrix}
$$
</div>

So, the vector in <span class="math-inline">\\(\text{span}(\lbrace \vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \rbrace)\\)</span> that is closest to <span class="math-inline">\\(\vec y\\)</span> is <span class="math-inline">\\(\boxed{\begin{bmatrix} 3/2 \\\\ 3/2 \\\\ 7/2 \\\\ 7/2 \end{bmatrix}}\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Open the **the supplemental Jupyter Notebook** we've created for Homework 7, which can either be found [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw07/hw07.ipynb) in the course GitHub repository, or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw07%2Fhw07.ipynb&branch=main) on DataHub.

There, you're asked to implement the function `orthogonalize`, which takes in an <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(V\\)</span> whose columns are linearly independent, and returns a matrix <span class="math-inline">\\(Q\\)</span> whose columns are orthonormal and have the same span as <span class="math-inline">\\(V\\)</span>. This problem is **not autograded**. Rather, in your submission to this part, include a screenshot of your implementation and sample output in your PDF for Homework 7.

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="imgs/q4-ss2.png" alt="image" style="width: 80%; max-width: 100%;">
</div>

<div style="text-align: center;">
<img src="imgs/q4-ss3.png" alt="image" style="width: 80%; max-width: 100%;">
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

1.  The big idea is that if <span class="math-inline">\\(Q\\)</span> is a matrix with orthonormal columns, then <span class="math-inline">\\(Q^TQ = I\\)</span>. So, if we're trying to find an <span class="math-inline">\\(R\\)</span> such that <span class="math-inline">\\(A = QR\\)</span>, then multiplying both sides by <span class="math-inline">\\(Q^T\\)</span> on the left gives us



<div class="math-display">
$$
A = QR \implies Q^TA = Q^TQR \implies Q^TA = R
$$
</div>

   meaning that <span class="math-inline">\\(R = Q^TA\\)</span>.

   All that's left to explain is **why <span class="math-inline">\\(R\\)</span> is upper triangular**. The product <span class="math-inline">\\(Q^TA\\)</span> contains the dot products of the rows of <span class="math-inline">\\(Q^T\\)</span> with the columns of <span class="math-inline">\\(A\\)</span>. But, the rows of <span class="math-inline">\\(Q^T\\)</span> are the columns of <span class="math-inline">\\(Q\\)</span>, so <span class="math-inline">\\(R = Q^TA\\)</span> contains the dot products of columns of <span class="math-inline">\\(Q\\)</span> with columns of <span class="math-inline">\\(A\\)</span>. Specifically,



<div class="math-display">
$$
R_{i, j} = \vec q_i \cdot \vec v_j
$$
</div>

   where <span class="math-inline">\\(\vec q&#95;i\\)</span> is the <span class="math-inline">\\(i\\)</span>-th column of <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(\vec v&#95;j\\)</span> is the <span class="math-inline">\\(j\\)</span>-th column of <span class="math-inline">\\(A\\)</span>.

   Remember, we constructed each <span class="math-inline">\\(\vec q&#95;i\\)</span> to be orthogonal to all previously constructed <span class="math-inline">\\(\vec q&#95;j\\)</span>'s for <span class="math-inline">\\(j &lt; i\\)</span>. Put in English, <span class="math-inline">\\(\vec q&#95;2\\)</span> is orthogonal to <span class="math-inline">\\(\vec q&#95;1\\)</span>, <span class="math-inline">\\(\vec q&#95;3\\)</span> is orthogonal to <span class="math-inline">\\(\vec q&#95;1\\)</span> and <span class="math-inline">\\(\vec q&#95;2\\)</span>, and so on.

   Each <span class="math-inline">\\(\vec q&#95;i\\)</span> was found by taking <span class="math-inline">\\(\vec v&#95;i\\)</span> and subtracting off **a linear combination of** <span class="math-inline">\\(\vec q&#95;{i - 1}, \vec q&#95;{i - 2}, \ldots, \vec q&#95;1\\)</span>. (More precisely, we built the <span class="math-inline">\\(\vec Q&#95;i\\)</span>'s this way and then normalized them to get the <span class="math-inline">\\(\vec q&#95;i\\)</span>'s, but the directions of the <span class="math-inline">\\(\vec Q&#95;i\\)</span>'s are the same as the directions of the <span class="math-inline">\\(\vec q&#95;i\\)</span>'s, so this reasoning still holds.) As an example, consider how we would construct <span class="math-inline">\\(\vec q&#95;4\\)</span> if we were to apply Gram-Schmidt to the vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3, \vec v&#95;4\\)</span>:



<div class="math-display">
$$
\begin{align*}
    \vec q_4 &= \vec v_4 - \text{proj}_{\vec q_1}(\vec v_4) - \text{proj}_{\vec q_2}(\vec v_4) - \text{proj}_{\vec q_3}(\vec v_4) \\\\
    \vec q_4 &= \vec v_4
- \frac{\vec v_4 \cdot \vec q_1}{\vec q_1 \cdot \vec q_1} \vec q_1
- \frac{\vec v_4 \cdot \vec q_2}{\vec q_2 \cdot \vec q_2} \vec q_2
- \frac{\vec v_4 \cdot \vec q_3}{\vec q_3 \cdot \vec q_3} \vec q_3 \\\\
    \vec q_4 &= \vec v_4 - a \vec q_1 - b \vec q_2 - c \vec q_3 \\\\
    \implies a \vec q_1 + b \vec q_2 + c \vec q_3 + \vec q_4 &= \vec v_4
    \end{align*}
$$
</div>

   But, since all the <span class="math-inline">\\(\vec q&#95;i\\)</span>'s are orthogonal to each other, if we were to take the dot product of both sides of the equation with <span class="math-inline">\\(\vec q&#95;5\\)</span>, or <span class="math-inline">\\(\vec q&#95;6\\)</span>, or any other <span class="math-inline">\\(\vec q&#95;i\\)</span> for <span class="math-inline">\\(i &gt; 4\\)</span>, we would get 0.

   This illustrates that <span class="math-inline">\\(\vec q&#95;i \cdot \vec v&#95;j = 0\\)</span> when <span class="math-inline">\\(i &gt; j\\)</span>. But, a matrix with 0's where <span class="math-inline">\\(i &gt; j\\)</span> is a matrix with 0's everywhere below the diagonal of <span class="math-inline">\\(i = j\\)</span>, which is precisely an upper triangular matrix.



<div class="math-display">
$$
\underbrace{\begin{bmatrix} \cdot & \cdot & \cdot & \cdot \\\\ 0 & \cdot & \cdot & \cdot \\\\ 0 & 0 & \cdot & \cdot \\\\ 0 & 0 & 0 & \cdot \end{bmatrix}}_{\text{in all the 0's, the row index (i) is greater than the column index (j)}}
$$
</div>

   So, since <span class="math-inline">\\(\vec q&#95;i \cdot \vec v&#95;j = 0\\)</span> when <span class="math-inline">\\(i &gt; j\\)</span>, <span class="math-inline">\\(R = Q^TA\\)</span> --- which is made up of these dot products --- is upper triangular.

2.  We have already found the <span class="math-inline">\\(Q\\)</span> in a <span class="math-inline">\\(QR\\)</span> decomposition of <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 &amp; 0 \\\\ 1 &amp; 1 &amp; 0 \\\\ 0 &amp; 1 &amp; 1 \\\\ 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>: these are the vectors we found in part **a)** of the problem.



<div class="math-display">
$$
Q = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{6} & \sqrt{3}/6 \\\\ 1/\sqrt{2} & 1/\sqrt{6} & -\sqrt{3}/6 \\\\ 0 & 2/\sqrt{6} & \sqrt{3}/6 \\\\ 0 & 0 & \sqrt{3}/2 \end{bmatrix}
$$
</div>

   Then, <span class="math-inline">\\(R = Q^TA\\)</span> is



<div class="math-display">
$$
R = Q^TA = \underbrace{\begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 & 0 \\\\ -1/\sqrt{6} & 1/\sqrt{6} & 2/\sqrt{6} & 0 \\\\ \sqrt{3}/6 & -\sqrt{3}/6 & \sqrt{3}/6 & 3\sqrt{3}/6 \end{bmatrix}}_{Q^T} \begin{bmatrix} 1 & 0 & 0 \\\\ 1 & 1 & 0 \\\\ 0 & 1 & 1 \\\\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} \sqrt{2} & 1/\sqrt{2} & 0 \\\\ 0 & 3/\sqrt{6} & 2/\sqrt{6} \\\\ 0 & 0 & 2\sqrt{3}/3 \end{bmatrix}
$$
</div>

3.  An easy solution is to negate one or more of the columns of <span class="math-inline">\\(Q\\)</span>; the resulting columns of <span class="math-inline">\\(Q\\)</span> will still be orthonormal with the same column space. This will lead to a slightly different <span class="math-inline">\\(R\\)</span>. (There are other ways of finding a <span class="math-inline">\\(QR\\)</span> decomposition as well.)

</details>

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

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
X^TX &= \begin{bmatrix} 1 & 1 & \ldots & 1 \\\\ x_1 & x_2 & \ldots & x_n \end{bmatrix} \begin{bmatrix} 1 & x_1 \\\\ 1 & x_2 \\\\ \vdots & \vdots \\\\ 1 & x_n \end{bmatrix} = \begin{bmatrix}n & \sum_{i=1}^nx_i \\\\ \sum_{i=1}^nx_i & \sum_{i=1}^nx_i^2\end{bmatrix} \\\\
(X^TX)^{-1} &= \frac{1}{n\sum_{i=1}^nx_i^2 - (\sum_{i=1}^nx_i)^2}\begin{bmatrix}\sum_{i=1}^nx_i^2 & -\sum_{i=1}^nx_i \\\\ -\sum_{i=1}^nx_i & n\end{bmatrix}
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

From the previous part, we have that

<div class="math-display">
$$
(X^TX)^{-1} = \frac{1}{n\sum_{i=1}^nx_i^2 - (\sum_{i=1}^nx_i)^2}\begin{bmatrix}\sum_{i=1}^nx_i^2 & -\sum_{i=1}^nx_i \\\\ -\sum_{i=1}^nx_i & n\end{bmatrix}
$$
</div>

To simplify, we'll start by proving the statement in the hint, that <span class="math-inline">\\(\sum&#95;{i = 1}^n x&#95;i^2 = n \sigma&#95;x^2 + n \bar{x}^2\\)</span>. The key "trick" is writing <span class="math-inline">\\(x&#95;i^2\\)</span> as <span class="math-inline">\\((x&#95;i - \bar{x} + \bar{x})^2\\)</span>, and then expand by grouping <span class="math-inline">\\(((x&#95;i - \bar{x}) + \bar{x})^2\\)</span>.

We'll use the fact that <span class="math-inline">\\(\sum&#95;{i = 1}^n (x&#95;i - \bar{x}) = 0\\)</span>; see [Chapter 0.1](https://notes.eecs245.org/prelim/summation/#mean-and-standard-deviation).

<div class="math-display">
$$
\begin{align*}
\sum_{i = 1}^n x_i^2 &= \sum_{i = 1}^n (x_i - \bar{x} + \bar{x})^2 \\\\
&= \sum_{i = 1}^n ((x_i - \bar{x}) + \bar{x})^2 \\\\
&= \sum_{i = 1}^n \left( (x_i - \bar{x})^2 + 2(x_i - \bar{x})\bar{x} + \bar{x}^2 \right) \\\\
&= \sum_{i = 1}^n (x_i - \bar{x})^2 + 2\bar{x}\underbrace{\sum_{i = 1}^n (x_i - \bar{x})}_{0} + n\bar{x}^2 \\\\
&= \sum_{i = 1}^n (x_i - \bar{x})^2 + n\bar{x}^2 \\\\
&= n\sigma_x^2 + n\bar{x}^2
\end{align*}
$$
</div>

How does this help us? Looking back at

<div class="math-display">
$$
(X^TX)^{-1} = \frac{1}{n\sum_{i=1}^nx_i^2 - (\sum_{i=1}^nx_i)^2}\begin{bmatrix}\sum_{i=1}^nx_i^2 & -\sum_{i=1}^nx_i \\\\ -\sum_{i=1}^nx_i & n\end{bmatrix}
$$
</div>

We can make the following substitutions:

-   <span class="math-inline">\\(n \sum&#95;{i=1}^nx&#95;i^2 = n(n\sigma&#95;x^2 + n\bar{x}^2) = n^2 \sigma&#95;x^2 + n^2 \bar{x}^2\\)</span>

-   <span class="math-inline">\\((\sum&#95;{i=1}^nx&#95;i)^2 = (n\bar{x})^2 = n^2 \bar{x}^2\\)</span>

-   <span class="math-inline">\\(\sum&#95;{i=1}^nx&#95;i^2 = n\sigma&#95;x^2 + n\bar{x}^2\\)</span>

-   <span class="math-inline">\\(-\sum&#95;{i=1}^nx&#95;i = -n\bar{x}\\)</span>

So,

<div class="math-display">
$$
\begin{align*}
(X^TX)^{-1} &= \frac{1}{n\sum_{i=1}^n x_i^2 - \left( \sum_{i=1}^n x_i \right)^2}
\begin{bmatrix}
\sum_{i=1}^n x_i^2 & -\sum_{i=1}^n x_i \\\\
-\sum_{i=1}^n x_i & n
\end{bmatrix} \\\\
&= \frac{1}{n^2 \sigma_x^2 + n^2 \bar{x}^2 - n^2 \bar{x}^2}
\begin{bmatrix}
n\sigma_x^2 + n\bar{x}^2 & -n\bar{x} \\\\
-n\bar{x} & n
\end{bmatrix} \\\\
&= \underbrace{\frac{1}{n^2 \sigma_x^2} \begin{bmatrix}
n\sigma_x^2 + n\bar{x}^2 & -n\bar{x} \\\\
-n\bar{x} & n
\end{bmatrix}}_{\text{divide matrix by } n} \\\\
&= \frac{1}{n\sigma_x^2} \begin{bmatrix}
\sigma_x^2 + \bar{x}^2 & -\bar{x} \\\\
-\bar{x} & 1
\end{bmatrix}
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

We already have a simplified form for <span class="math-inline">\\((X^TX)^{-1}\\)</span> from the previous part. Let's look at <span class="math-inline">\\(X^T \vec y\\)</span>.

<div class="math-display">
$$
\begin{align*}
X^T \vec y &= \begin{bmatrix} 1 & 1 & \ldots & 1 \\\\ x_1 & x_2 & \ldots & x_n \end{bmatrix} \begin{bmatrix} y_1 \\\\ y_2 \\\\ \vdots \\\\ y_n \end{bmatrix} = \begin{bmatrix} \sum_{i=1}^ny_i \\\\ \sum_{i=1}^nx_iy_i \end{bmatrix}
\end{align*}
$$
</div>

This is where the hint comes in. Let's show that <span class="math-inline">\\(\sum&#95;{i=1}^n x&#95;i y&#95;i = nr \sigma&#95;x \sigma&#95;y + n \bar{x}\bar{y}\\)</span>. It's not immediately clear how to approach this, since starting with just <span class="math-inline">\\(\sum&#95;{i=1}^n x&#95;i y&#95;i\\)</span> doesn't seem to help us. Instead, let's start by expanding the definition of <span class="math-inline">\\(r\\)</span>.

<div class="math-display">
$$
\begin{align*}
r &= \frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right) \\\\
nr\sigma_x \sigma_y &= \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \\\\
nr \sigma_x \sigma_y &= \sum_{i=1}^n \left( x_iy_i - x_i \bar{y} - y_i \bar{x} + \bar{x}\bar{y} \right) \\\\
nr \sigma_x \sigma_y &= \sum_{i=1}^n x_iy_i - \bar{y} \sum_{i=1}^n x_i  - \bar{x}\sum_{i=1}^n y_i  + \sum_{i=1}^n \bar{x}\bar{y} \\\\
nr \sigma_x \sigma_y &= \sum_{i=1}^n x_iy_i - n\bar{y}\bar{x} - n\bar{x}\bar{y} + n\bar{x}\bar{y} \\\\
nr \sigma_x \sigma_y &= \sum_{i=1}^n x_iy_i - n\bar{x}\bar{y} \\\\
\sum_{i=1}^n x_iy_i &= nr \sigma_x \sigma_y + n \bar{x}\bar{y}
\end{align*}
$$
</div>

So, that gives us

<div class="math-display">
$$
X^T \vec y = \begin{bmatrix} \sum_{i=1}^ny_i \\\\ \sum_{i=1}^nx_iy_i \end{bmatrix} = \begin{bmatrix} n\bar{y} \\\\ n(r\sigma_x\sigma_y + \bar{x}\bar{y}) \end{bmatrix}
$$
</div>

Finally, we're ready to evaluate <span class="math-inline">\\(\vec w^{\ast} = (X^TX)^{-1}X^T \vec y\\)</span>.

<div class="math-display">
$$
\begin{align*}
(X^TX)^{-1}X^T \vec y
&= \frac{1}{n\sigma_x^2}
\begin{bmatrix}
\bar{x}^2+\sigma_x^2 & -\bar{x} \\\\
-\bar{x} & 1
\end{bmatrix}
\begin{bmatrix}
n\bar{y} \\\\
n(r\sigma_x\sigma_y + \bar{x}\bar{y})
\end{bmatrix}
\\\\
&= \frac{1}{\sigma_x^2}
\begin{bmatrix}
\bar{x}^2+\sigma_x^2 & -\bar{x} \\\\
-\bar{x} & 1
\end{bmatrix}
\begin{bmatrix}
\bar{y} \\\\
r\sigma_x\sigma_y + \bar{x}\bar{y}
\end{bmatrix}
\\\\
&= \frac{1}{\sigma_x^2}
\begin{bmatrix}
(\bar{x}^2+\sigma_x^2)\bar{y} - \bar{x}(r\sigma_x\sigma_y + \bar{x}\bar{y}) \\\\
-\bar{x}\bar{y} + r\sigma_x\sigma_y + \bar{x}\bar{y}
\end{bmatrix}
\\\\
&= \frac{1}{\sigma_x^2}
\begin{bmatrix}
\bar{x}^2\bar{y} + \sigma_x^2\bar{y} - \bar{x}r\sigma_x\sigma_y - \bar{x}^2\bar{y} \\\\
r\sigma_x\sigma_y
\end{bmatrix}
\\\\
&= \frac{1}{\sigma_x^2}
\begin{bmatrix}
\sigma_x^2\bar{y} - \bar{x}r\sigma_x\sigma_y \\\\
r\sigma_x\sigma_y
\end{bmatrix}
\\\\
&= \begin{bmatrix}
\bar{y} - r \frac{\sigma_y}{\sigma_x}\bar{x} \\\\
r \frac{\sigma_y}{\sigma_x}
\end{bmatrix}
\end{align*}
$$
</div>

Finally!

</details>

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

<details markdown="1"><summary>Solution</summary>

Since our hypothesis function is <span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i^2\\)</span>, the design matrix must include a column of ones (for the intercept term) and a column containing <span class="math-inline">\\(x&#95;i^2\\)</span> for each <span class="math-inline">\\(x&#95;i\\)</span> value.

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & x_1^2 \\\\
1 & x_2^2 \\\\
1 & x_3^2 \\\\
1 & x_4^2 \\\\
1 & x_5^2
\end{bmatrix}
=
\begin{bmatrix}
1 & 4 \\\\
1 & 1 \\\\
1 & 9 \\\\
1 & 49 \\\\
1 & 9
\end{bmatrix}
$$
</div>

Here, each entry in the second column corresponds to <span class="math-inline">\\(x&#95;i^2\\)</span> for the given <span class="math-inline">\\(x&#95;i\\)</span> values in the dataset.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Suppose that after solving the normal equations, we find <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 5 \\\\ -2 \end{bmatrix}\\)</span>. Find the augmented feature vector <span class="math-inline">\\(\text{Aug}(\vec x&#95;3)\\)</span> and squared loss for row 3 of the dataset.

<details markdown="1"><summary>Solution</summary>

The augmented feature vector adds a constant <span class="math-inline">\\(1\\)</span> for the intercept and the squared value of <span class="math-inline">\\(x&#95;3\\)</span>:

<div class="math-display">
$$
\text{Aug}(\vec x_3) =
\begin{bmatrix}
1 \\\\ x_3^2
\end{bmatrix}
=
\begin{bmatrix}
1 \\\\ 9
\end{bmatrix}
$$
</div>

The hypothesis function is

<div class="math-display">
$$
h(x_i) = w_0 + w_1 x_i^2
$$
</div>

 Plugging in <span class="math-inline">\\(x&#95;3 = 3\\)</span> and <span class="math-inline">\\(\vec w^{\ast} = [5, -2]^T\\)</span>:

<div class="math-display">
$$
h(x_3) = 5 + (-2)(9) = -13
$$
</div>

From the dataset, <span class="math-inline">\\(y&#95;3 = 5\\)</span>. The error for this data point is:

<div class="math-display">
$$
e_3 = y_3 - h(x_3) = 5 - (-13) = 18
$$
</div>

The squared loss is

<div class="math-display">
$$
L_{\text{sq}}(y_3, h(x_3)) = (y_3 - h(x_3))^2 = (18)^2 = 324
$$
</div>

<div class="math-display">
$$
\boxed{
\text{Aug}(\vec x_3) =
\begin{bmatrix} 1 \\\\ 9 \end{bmatrix} \quad
L_{\text{sq}}(y_3, h(x_3)) = 324
}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(X&#95;\text{tri} = 3X\\)</span>, where <span class="math-inline">\\(X\\)</span> is the full design matrix for our dataset with <span class="math-inline">\\(n\\)</span> rows. Determine the bottom-left value in the matrix <span class="math-inline">\\(X&#95;\text{tri}^TX&#95;\text{tri}\\)</span>, i.e. the value in the second row and first column. Your answer should be an expression involving <span class="math-inline">\\(n\\)</span>. <em>Hint: You can use any of the hints or results from Problem 2 without needing to re-prove them.</em>

<details markdown="1"><summary>Solution</summary>

Starting with the design matrix

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & x_1^2 \\\\
1 & x_2^2 \\\\
\vdots & \vdots \\\\
1 & x_n^2
\end{bmatrix}
\qquad
X_\text{tri} = 3X =
\begin{bmatrix}
3 & 3x_1^2 \\\\
3 & 3x_2^2 \\\\
\vdots & \vdots \\\\
3 & 3x_n^2
\end{bmatrix}
$$
</div>

The matrix product is

<div class="math-display">
$$
X_\text{tri}^T X_\text{tri} =
\begin{bmatrix}
3 & 3 & \cdots & 3 \\\\
3x_1^2 & 3x_2^2 & \cdots & 3x_n^2
\end{bmatrix}
\begin{bmatrix}
3 & 3x_1^2 \\\\
3 & 3x_2^2 \\\\
\vdots & \vdots \\\\
3 & 3x_n^2
\end{bmatrix}
$$
</div>

The bottom-left entry (row 2, column 1) is

<div class="math-display">
$$
\sum_{i=1}^n (3x_i^2)(3) = \sum_{i=1}^n 9x_i^2 = 9 \sum_{i=1}^n x_i^2.
$$
</div>

Using the identity <span class="math-inline">\\(\sum&#95;{i=1}^n x&#95;i^2 = n\sigma&#95;x^2 + n\bar{x}^2\\)</span>,

<div class="math-display">
$$
\sum_{i=1}^n x_i^2 = n\sigma_x^2 + n\bar{x}^2
$$
</div>

 we substitute to obtain

<div class="math-display">
$$
\text{Bottom-left entry} = 9n(\sigma_x^2 + \bar{x}^2)
$$
</div>

and finally, substituting <span class="math-inline">\\(\sigma&#95;x^2 = 8\\)</span> and <span class="math-inline">\\(\bar{x} = 5\\)</span>:

<div class="math-display">
$$
9n(8 + 5^2) = 9n(8 + 25) = 9n(33) = \boxed{297n}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 7: Billy the Waiter (14 pts)

This problem involves writing code and submitting it to the Gradescope autograder. The goal of this problem is to give you a taste of how linear algebra can be used to implement linear regression in code, and show you how to build models that involve multiple features (including categorical variables).

Open the **the supplemental Jupyter Notebook** we've created for Homework 7, which can either be found [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw07/hw07.ipynb) in the course GitHub repository, or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw07%2Fhw07.ipynb&branch=main) on DataHub.

**This problem is entirely autograded; to receive credit for Problem 7 of this homework, you'll need to submit your completed notebook to the autograder on Gradescope.** Your submission time for Homework 7 is the **latter** of your PDF and code submission times.

{% endraw %}
