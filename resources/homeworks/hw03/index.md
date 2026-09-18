---
layout: page
title: "Homework 3: Vectors and the Dot Product"
description: "Homework 3: Vectors and the Dot Product problems."
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

# Homework 3: Vectors and the Dot Product

**due** Friday, September 25th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw03/hw03.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 2 Solutions Review](#problem-1-homework-2-solutions-review-10-pts)
- [Problem 2: Feedback](#problem-2-feedback-6-pts)
- [Problem 3: Drawing Linear Combinations](#problem-3-drawing-linear-combinations-6-pts)
- [Problem 4: Displacement and Distance](#problem-4-displacement-and-distance-7-pts)
- [Problem 5: Distributing the Dots](#problem-5-distributing-the-dots-13-pts)
- [Problem 6: Parallelogram Law](#problem-6-parallelogram-law-12-pts)
- [Problem 7: Linear Combinations](#problem-7-linear-combinations-10-pts)
- [Problem 8: Correlation](#problem-8-correlation-8-pts)
- [Problem 9: Projections](#problem-9-projections-9-pts)
- [Problem 10: Norms](#problem-10-norms-13-pts)
- [Problem 11: Neighbors](#problem-11-neighbors-10-pts)

---

Total Points: 10 + 6 + 6 + 7 + 13 + 12 + 10 + 8 + 9 + 13 + 10 = 104

---

## Problem 1: Homework 2 Solutions Review (10 pts)

Review the solutions to Homework 2. Pick **two problem parts** (for example, Problem 2a and Problem 4b) from Homework 2 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 2, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Feedback (6 pts)

We'd like to get your feedback on how the course has been going so far, now that we're a few weeks in.

You can find the survey [at this link](https://docs.google.com/forms/d/e/1FAIpQLSdvBEc75kpB1p-YZPtD0SctjfkbokDTlLh8wc1Y5D7m9fTaDw/viewform?usp=publish-editor). It is **not anonymous**, but it links to an anonymous feedback form if you'd like to provide some feedback anonymously.

When submitting to Pensive, it does not matter which page of your submission you assign to Problem 2; we will enter survey completion credit in manually.

Thank you for your feedback --- it's helping shape our relatively new course.

---

## Problem 3: Drawing Linear Combinations (6 pts)

In this problem, draw all vectors on the same set of axes, like the one below. Your final graph should contain five vectors. Draw each vector starting at the origin, and label it.

<ol class="assignment-list" markdown="1" data-item-count="5" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Draw <span class="math-inline">\\(\vec u=\begin{bmatrix}3\\\\4\end{bmatrix}\\)</span>.

</li>
<li markdown="1" value="2">

Draw <span class="math-inline">\\(\vec v=\begin{bmatrix}-1\\\\-4\end{bmatrix}\\)</span>.

</li>
<li markdown="1" value="3">

(2 pts) Draw <span class="math-inline">\\(\vec a=-\vec u-\vec v\\)</span>. Verify that your drawing is correct by finding <span class="math-inline">\\(\vec a\\)</span>'s components.

</li>
<li markdown="1" value="4">

(2 pts) Draw <span class="math-inline">\\(\vec b=2\vec u+\vec v\\)</span>. Verify that your drawing is correct by finding <span class="math-inline">\\(\vec b\\)</span>'s components.

</li>
<li markdown="1" value="5">

(2 pts) Draw <span class="math-inline">\\(\vec c=\frac12\vec u-\frac12\vec v\\)</span>. Verify that your drawing is correct by finding <span class="math-inline">\\(\vec c\\)</span>'s components.

</li>
</ol>

---

## Problem 4: Displacement and Distance (7 pts)

A drone begins at the point

<div class="math-display">
$$
P=(2,-1,4)
$$
</div>

 and flies in a straight line to the point

<div class="math-display">
$$
Q=(6,7,-4).
$$
</div>

 The coordinates here are in meters.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) Let <span class="math-inline">\\(\vec{d}\\)</span> be the vector that describes the displacement from <span class="math-inline">\\(P\\)</span> to <span class="math-inline">\\(Q\\)</span>. Find <span class="math-inline">\\(\vec{d}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find the exact distance traveled by the drone.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose the drone continues to travel another 10 meters in the same direction. What are its coordinates?

</div>
</div>

</div>

---

## Problem 5: Distributing the Dots (13 pts)

Let <span class="math-inline">\\(\vec{u},\vec{v}\in\mathbb{R}^n\\)</span> satisfy

<div class="math-display">
$$
\|\vec{u}\|=3,\qquad \|\vec{v}\|=2,\qquad
(3\vec{u}-4\vec{v})\cdot(\vec{u}+9\vec{v})=-71.
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(\vec{u}\cdot\vec{v}\\)</span>. Show your work.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\|-2\vec{u}\|\\)</span> and <span class="math-inline">\\(\|3\vec{v}\|\\)</span>. Explain why neither length is negative.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Recall, the cosine similarity of two nonzero vectors <span class="math-inline">\\(\vec u,\vec v\\)</span> is defined as

<div class="math-display">
$$
\cos\theta=\frac{\vec u\cdot\vec v}{\|\vec u\|\|\vec v\|},
$$
</div>

 where <span class="math-inline">\\(\theta\\)</span> is the angle between the vectors.

Find the cosine similarity of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. Then find the cosine similarity of <span class="math-inline">\\(-2\vec{u}\\)</span> and <span class="math-inline">\\(3\vec{v}\\)</span>. If the two cosine similarities are different, why are they different?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) Find <span class="math-inline">\\(\vec{u}\cdot\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\cdot\vec{v}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find <span class="math-inline">\\(\|\vec{u}+\vec{v}\|\\)</span>. Is it equal to <span class="math-inline">\\(\sqrt{\|\vec{u}\|^2+\|\vec{v}\|^2}\\)</span>? Explain what condition would make these quantities equal.

<em>Hint: Start by writing <span class="math-inline">\\(\lVert\vec{u}+\vec{v}\rVert^2\\)</span> as <span class="math-inline">\\((\vec{u}+\vec{v})\cdot(\vec{u}+\vec{v})\\)</span>.</em>

</div>
</div>

</div>

---

## Problem 6: Parallelogram Law (12 pts)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Let <span class="math-inline">\\(\vec{u} = \begin{bmatrix} 3 \\\\ -6 \\\\ 0 \\\\ 2 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec{v} = \begin{bmatrix} 2 \\\\ 1 \\\\ 4 \\\\ -2 \end{bmatrix}\\)</span>. Compute the following quantities:

<ol class="assignment-list" markdown="1" data-item-count="4" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

<span class="math-inline">\\(\lVert \vec{u} \rVert\\)</span>

</li>
<li markdown="1" value="2">

<span class="math-inline">\\(\lVert \vec{v} \rVert\\)</span>

</li>
<li markdown="1" value="3">

<span class="math-inline">\\(\lVert \vec{u} + \vec{v} \rVert\\)</span>

</li>
<li markdown="1" value="4">

<span class="math-inline">\\(\lVert \vec{u} - \vec{v} \rVert\\)</span>

</li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Using the same vectors as in part **a)**, compute the angle between <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. Leave your answer in terms of <span class="math-inline">\\(\cos^{-1}\\)</span>. We asked you to do something very similar in Problem 5c, but here we are asking for the angle itself, which is why your answer involves <span class="math-inline">\\(\cos^{-1}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Now, suppose <span class="math-inline">\\(\vec{u} = \begin{bmatrix} u&#95;1 \\\\ u&#95;2 \\\\ \vdots \\\\ u&#95;n \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec{v} = \begin{bmatrix} v&#95;1 \\\\ v&#95;2 \\\\ \vdots \\\\ v&#95;n \end{bmatrix}\\)</span> are any two vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. Prove that:

<div class="math-display">
$$
\lVert \vec{u} + \vec{v} \rVert^2 + \lVert \vec{u} - \vec{v} \rVert^2 = 2\lVert \vec{u} \rVert^2 + 2\lVert \vec{v} \rVert^2
$$
</div>

The statement above is called the **parallelogram law** of vectors.

<em>Hint: The point of part <strong>a)</strong> was to give you a feel for which quantities are involved in this statement. Your proof should not use these values in particular. Refer to the hint from Problem 5e.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Why is the equality from part **c)** called the parallelogram law? Let's explore.

Suppose points <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, <span class="math-inline">\\(C\\)</span>, and <span class="math-inline">\\(D\\)</span> in <span class="math-inline">\\(\mathbb{R}^n\\)</span> form a parallelogram: a polygon with four sides where opposite sides are parallel and equal in length.

<div style="text-align: center;">
<img src="imgs/parallelogram.png" alt="image" style="width: 60%; max-width: 100%;">
</div>

Using the results of the previous part of this problem, prove that the sum of the squares of the side lengths of the parallelogram is equal to the sum of the squares of the diagonals. In other words, prove that:

<div class="math-display">
$$
(AB)^2 + (BC)^2 + (CD)^2 + (DA)^2 = (AC)^2 + (BD)^2
$$
</div>

where <span class="math-inline">\\(AB\\)</span> represents the length of the segment from point <span class="math-inline">\\(A\\)</span> to point <span class="math-inline">\\(B\\)</span>, etc.

<em>Hint: Define two vectors, <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and explain why the result from the previous part of this problem implies the desired equality. This is mostly an English problem.</em>

</div>
</div>

</div>

---

## Problem 7: Linear Combinations (10 pts)

Much of our study of linear algebra involves understanding **the set of possible linear combinations** of a given set of vectors. As the notes detail, our multiple linear regression problem boils down to finding the best possible linear combination of the features, so it's important that we understand how linear combinations work.

Let

<div class="math-display">
$$
\vec v_1 = \begin{bmatrix} 2 \\\\ 3 \\\\ 0 \end{bmatrix},\quad \vec v_2 = \begin{bmatrix} -1 \\\\ 2 \\\\ -1 \end{bmatrix},\quad \vec v_3 = \begin{bmatrix} 0 \\\\ 5 \\\\ 2 \end{bmatrix},\quad \vec x = \begin{bmatrix} -6 \\\\ 1 \\\\ 4 \end{bmatrix}.
$$
</div>

You can find an interactive, three-dimensional visualization of these four vectors at this link:

<https://eecs245.org/resources/homeworks/hw03/hw03-problem-7.html>

We recommend you have this visual open while you work through this problem.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find constants <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that

<div class="math-display">
$$
a \vec v_1 + b \vec v_2 + c \vec v_3 = \vec x
$$
</div>

 In other words, write <span class="math-inline">\\(\vec x\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span>.

<em>Hint: Start by writing out the equation as a system of equations. Then, use your favorite method for solving systems of equations to find <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span>. We reviewed how to solve systems of equations in Lab 3.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Try and find constants <span class="math-inline">\\(d\\)</span> and <span class="math-inline">\\(e\\)</span> such that

<div class="math-display">
$$
d \vec v_1 + e \vec v_3 = \vec x
$$
</div>

 If you are able to find constants <span class="math-inline">\\(d\\)</span> and <span class="math-inline">\\(e\\)</span>, **explain why**, even though there are two unknowns but three equations for them. If you are unable to find constants <span class="math-inline">\\(d\\)</span> and <span class="math-inline">\\(e\\)</span>, **explain why** no solution exists.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Try and find constants <span class="math-inline">\\(p\\)</span> and <span class="math-inline">\\(q\\)</span> such that

<div class="math-display">
$$
p \vec v_1 + q \vec v_2 = \vec x
$$
</div>

 If you are able to find constants <span class="math-inline">\\(p\\)</span> and <span class="math-inline">\\(q\\)</span>, **explain why**, even though there are two unknowns but three equations for them. If you are unable to find constants <span class="math-inline">\\(p\\)</span> and <span class="math-inline">\\(q\\)</span>, **explain why** no solution exists.

</div>
</div>

</div>

---

## Problem 8: Correlation (8 pts)

In [Chapter 2.4](https://notes.eecs245.org/simple-linear-regression/correlation/), you were told that the correlation coefficient, <span class="math-inline">\\(r\\)</span>, ranges between <span class="math-inline">\\(-1\\)</span> and <span class="math-inline">\\(1\\)</span>, where <span class="math-inline">\\(-1\\)</span> implies a perfect negative linear association and <span class="math-inline">\\(1\\)</span> implies a perfect positive linear association. However, you were never given a proof of the fact that <span class="math-inline">\\(-1 \leq r \leq 1\\)</span>.

Here, you will prove this fact, given your newfound understanding of vectors, the dot product, and angles.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Let <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> be two vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. We define the "mean-centered" version of <span class="math-inline">\\(\vec x\\)</span> to be:

<div class="math-display">
$$
\vec{x}_{\text{c}} = \begin{bmatrix} x_1 - \bar{x} \\\\ x_2 - \bar{x} \\\\ \vdots \\\\ x_n - \bar{x} \end{bmatrix}
$$
</div>

 where <span class="math-inline">\\(\displaystyle \bar{x} = \frac{1}{n} \sum&#95;{i=1}^n x&#95;i\\)</span> is the mean of the components of <span class="math-inline">\\(\vec{x}\\)</span>. The mean-centered version of <span class="math-inline">\\(\vec y\\)</span>, named <span class="math-inline">\\(\vec{y}&#95;{\text{c}}\\)</span>, is defined similarly.

Express <span class="math-inline">\\(\vec{x}&#95;{\text{c}} \cdot \vec{y}&#95;{\text{c}}\\)</span> using summation notation.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Prove that:

<div class="math-display">
$$
r = \frac{\vec{x}_{\text{c}} \cdot \vec{y}_{\text{c}}}{\lVert \vec{x}_{\text{c}} \rVert \lVert \vec{y}_{\text{c}} \rVert}
$$
</div>

 Do so by starting with the right-hand side of the equation, expanding it, and simplifying it until you reach the definition of <span class="math-inline">\\(r\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In 1-2 English sentences, explain why the result from part **b)** implies that <span class="math-inline">\\(-1 \leq r \leq 1\\)</span>.

</div>
</div>

</div>

---

## Problem 9: Projections (9 pts)

In [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/), we study the concept of **projecting** one vector onto one or more other vectors. In this problem, you'll see how this concept can be thought of in terms of our friend from the first two weeks of the course: calculus.

Let <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> be two vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. Consider the function <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span>, defined as:

<div class="math-display">
$$
f(k) = \lVert \vec y - k \vec x \rVert^2
$$
</div>

 By <span class="math-inline">\\(\mathbb{R} \to \mathbb{R}\\)</span>, we mean that <span class="math-inline">\\(f\\)</span> takes in a single real number (i.e. a scalar, **not** a vector) and outputs a single real number. This means that we can find <span class="math-inline">\\(\frac{\text{d} f}{\text{d} k}\\)</span>, the derivative of <span class="math-inline">\\(f\\)</span> with respect to <span class="math-inline">\\(k\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Rewrite <span class="math-inline">\\(f(k)\\)</span> using the properties of the dot product from [Chapter 3.3](https://notes.eecs245.org/vectors/dot-product/#dot-product-and-the-vector-norm). Then, show that:

<div class="math-display">
$$
\frac{\text{d} f}{\text{d} k} = -2 \vec x \cdot \vec y + 2k \vec x \cdot \vec x
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(k^{\ast}\\)</span>, the value of <span class="math-inline">\\(k\\)</span> that minimizes <span class="math-inline">\\(f(k)\\)</span>. A second derivative test is not necessary.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Show that the vectors <span class="math-inline">\\(k^{\ast} \vec x\\)</span> and <span class="math-inline">\\(\vec y - k^{\ast} \vec x\\)</span> are orthogonal.

</div>
</div>

</div>

---

## Problem 10: Norms (13 pts)

In [the *Other Norms* section of Chapter 3.2](https://notes.eecs245.org/vectors/norms/#other-norms), we introduced the concept of vector norms *other than* the "default" Euclidean norm. Each of those norms describes a different way of measuring the length of a vector --- just like how different loss functions described different ways of measuring the error of a prediction.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) **In this part only**, let <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 \\\\ -6 \\\\ 0 \\\\ 2 \end{bmatrix}\\)</span>. Compute <span class="math-inline">\\(\lVert \vec v \rVert&#95;2\\)</span>, <span class="math-inline">\\(\lVert \vec v \rVert&#95;1\\)</span>, and <span class="math-inline">\\(\lVert \vec v \rVert&#95;\infty\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) In the Parallelogram Law problem, we introduced the following identity:

<div class="math-display">
$$
\lVert \vec{u} + \vec{v} \rVert^2 + \lVert \vec{u} - \vec{v} \rVert^2 = 2\lVert \vec{u} \rVert^2 + 2\lVert \vec{v} \rVert^2
$$
</div>

 In general, the parallelogram law only holds for the <span class="math-inline">\\(L&#95;2\\)</span> norm, not necessarily other norms.

Find a counterexample involving two vectors <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> such that the parallelogram law **does not hold** for the <span class="math-inline">\\(L&#95;1\\)</span> norm.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Prove that

<div class="math-display">
$$
\lVert \vec v \rVert_2 \leq \sqrt{n}\lVert \vec v \rVert_\infty
$$
</div>

 <em>Hint: Start by writing out the definition of the <span class="math-inline">\\(L&#95;2\\)</span> norm, and then square it to remove the square root. You will have a sum of <span class="math-inline">\\(n\\)</span> terms. Explain why each of those <span class="math-inline">\\(n\\)</span> terms is less than or equal to <span class="math-inline">\\(\lVert \vec v \rVert&#95;\infty^2\\)</span>. This is most of the way to the proof, but there's still some work you'll need to do after you get to that point.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Prove that

<div class="math-display">
$$
\lVert \vec v \rVert_2 \leq \lVert \vec v \rVert_1
$$
</div>

 <em>Hint: Start with the fact that </em>

<div class="math-display">
$$
\lVert \vec v \rVert_1^2 = \left( |v_1| + |v_2| + \cdots + |v_n| \right)^2
$$
</div>

</div>
</div>

</div>

---

## Problem 11: Neighbors (10 pts)

This problem involves writing code and submitting it to the Pensive autograder.

There are two ways to access the supplemental Jupyter Notebook:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

**Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/fa26-code/tree/main), and open `homeworks/hw03/hw03.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

</li>
<li markdown="1">

**Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https://github.com/eecs245/fa26-code&urlpath=tree/fa26-code/homeworks/hw03/hw03.ipynb&branch=main) to open `hw03.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

</li>
</ul>

To receive credit for the programming portion of the homework, you'll need to submit your completed notebook to the autograder on Pensive. Your submission time for Homework 3 is the **latter** of your PDF and code submission times.

{% endraw %}
