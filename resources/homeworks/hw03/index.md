---
layout: page
title: "Homework 3: Vectors and the Dot Product"
description: "Homework 3: Vectors and the Dot Product problems."
nav_exclude: true
hide_footer_hr: true
---

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

# Homework 3: Vectors and the Dot Product

**due** Sunday, May 17th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw03/hw03.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 2 Solutions Review](#problem-1-homework-2-solutions-review-10-pts)
- [Problem 2: Parallelogram Law](#problem-2-parallelogram-law-14-pts)
- [Problem 3: Linear Combinations](#problem-3-linear-combinations-9-pts)
- [Problem 4: Correlation](#problem-4-correlation-7-pts)
- [Problem 5: Projections](#problem-5-projections-15-pts)
- [Problem 6: Norms](#problem-6-norms-12-pts)
- [Problem 7: Neighbors](#problem-7-neighbors-10-pts)
- [Problem 8: Feedback](#problem-8-feedback-6-pts)

---

Total Points: 10 + 14 + 9 + 7 + 15 + 12 + 10 + 6 = 83

---

## Problem 1: Homework 2 Solutions Review (10 pts)

Review the solutions to Homework 2. Pick **two problem parts** (for example, Problem 2a and Problem 4b) from Homework 2 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 2, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: Parallelogram Law (14 pts)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(\vec{u} = \begin{bmatrix} 3 \\\\ -6 \\\\ 0 \\\\ 2 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec{v} = \begin{bmatrix} 2 \\\\ 1 \\\\ 4 \\\\ -2 \end{bmatrix}\\)</span>. Compute the following quantities:

1.  <span class="math-inline">\\(\lVert \vec{u} \rVert\\)</span>

2.  <span class="math-inline">\\(\lVert \vec{v} \rVert\\)</span>

3.  <span class="math-inline">\\(\lVert \vec{u} + \vec{v} \rVert\\)</span>

4.  <span class="math-inline">\\(\lVert \vec{u} - \vec{v} \rVert\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Using the same vectors as in part **a)**, compute the angle between <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. Leave your answer in terms of <span class="math-inline">\\(\cos^{-1}\\)</span>.

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

<em>Hint: The point of part <strong>a)</strong> was to give you a feel for which quantities are involved in this statement. Your proof should not use these values in particular. Instead, <strong>start with the left-hand side</strong> of the equation and use the properties of the dot product introduced in <a href="https://notes.eecs245.org/vectors/dot-product/#properties-of-the-dot-product">Chapter 3.3</a>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Why is the equality from part **c)** called the parallelogram law? Let's explore.

Suppose points <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, <span class="math-inline">\\(C\\)</span>, and <span class="math-inline">\\(D\\)</span> in <span class="math-inline">\\(\mathbb{R}^n\\)</span> form a parallelogram: a polygon with four sides where opposite sides are parallel and equal in length.

![image](imgs/parallelogram.png)

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

## Problem 3: Linear Combinations (9 pts)

As we saw in [Chapter 3.1](https://notes.eecs245.org/vectors/vectors-and-linear-combinations/#linear-combinations), a **linear combination** of vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d \in \mathbb{R}^n\\)</span> is a vector of the form

<div class="math-display">
$$
a_1 \vec v_1 + a_2 \vec v_2 + \cdots + a_d \vec v_d
$$
</div>

where <span class="math-inline">\\(a&#95;1, a&#95;2, \ldots, a&#95;d\\)</span> are scalars.

Much of our study of linear algebra involves understanding **the set of possible linear combinations** of a given set of vectors. As the notes detail, our multiple linear regression problem boils down to finding the best possible linear combination of the features, so it's important that we understand how linear combinations work.

Let <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix} 2 \\\\ 3 \\\\ 0 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec v&#95;2 = \begin{bmatrix} -1 \\\\ 2 \\\\ -1 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec v&#95;3 = \begin{bmatrix} 0 \\\\ 5 \\\\ 2 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec x = \begin{bmatrix} -6 \\\\ 1 \\\\ 4 \end{bmatrix}\\)</span>.

You can find an interactive, three-dimensional visualization of these four vectors at this link:

<https://eecs245.org/resources/homeworks/hw03/hw03-problem-2.html>

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
(2 pts) Try and find constants <span class="math-inline">\\(d\\)</span> and <span class="math-inline">\\(e\\)</span> such that

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

## Problem 4: Correlation (7 pts)

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
(3 pts) Prove that:

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

## Problem 5: Projections (15 pts)

In [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/), we study the concept of **projecting** one vector onto one or more other vectors. In this problem, you'll see how this concept can be thought of in terms of our friend from the first two weeks of the course: calculus.

Let <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> be two vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. Consider the function <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span>, defined as: 

<div class="math-display">
$$
f(k) = \lVert \vec y - k \vec x \rVert^2
$$
</div>

 By <span class="math-inline">\\(\mathbb{R} \to \mathbb{R}\\)</span>, we mean that <span class="math-inline">\\(f\\)</span> takes in a single real number (i.e. a scalar, **not** a vector) and outputs a single real number. This means that we can find <span class="math-inline">\\(\frac{\text{d} f}{\text{d} k}\\)</span>, the derivative of <span class="math-inline">\\(f\\)</span> with respect to <span class="math-inline">\\(k\\)</span>.

Note that <span class="math-inline">\\(k \vec x\\)</span> is a vector that points in the same direction (or the opposite direction) as <span class="math-inline">\\(\vec x\\)</span>.

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
(2 pts) Find <span class="math-inline">\\(k^&#42;\\)</span>, the value of <span class="math-inline">\\(k\\)</span> that minimizes <span class="math-inline">\\(f(k)\\)</span>. A second derivative test is not necessary.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Show that the vectors <span class="math-inline">\\(k^&#42; \vec x\\)</span> and <span class="math-inline">\\(\vec y - k^&#42; \vec x\\)</span> are orthogonal.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Now, let's study a seemingly unrelated problem. Suppose we're given a dataset

<span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span> and we'd like to find the optimal model parameter, <span class="math-inline">\\(w\\)</span>, for a simple linear model **with no intercept term**, 

<div class="math-display">
$$
h(x_i) = w x_i
$$
</div>

 Find the value of <span class="math-inline">\\(w\\)</span> that minimizes the average loss (i.e. empirical risk) when using squared loss. A second derivative test is not necessary. (To be clear, the solution to this problem does not involve linear algebra.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ \vdots \\\\ x&#95;n \end{bmatrix}\\)</span> is a vector of all the <span class="math-inline">\\(x&#95;i\\)</span> values in the dataset and <span class="math-inline">\\(\vec y = \begin{bmatrix} y&#95;1 \\\\ y&#95;2 \\\\ \vdots \\\\ y&#95;n \end{bmatrix}\\)</span> is a vector of all the <span class="math-inline">\\(y&#95;i\\)</span> values in the dataset.

Then, notice that <span class="math-inline">\\(w^&#42;\\)</span> (the optimal slope) from part **d)** is the same formula as <span class="math-inline">\\(k^&#42;\\)</span> (the optimal stretching factor) from part **b)**! This is not a coincidence: the problem in part **d)** is equivalent to the problem stated at the start of this question, it's just stated differently! This may be a bit confusing, since:

-   The problem at the start involves two vectors, <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>, which live in <span class="math-inline">\\(\mathbb{R}^n\\)</span>, and <span class="math-inline">\\(n\\)</span> may be very large (could be 100-dimensional space!).

-   The problem in part **d)** involves a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, but the points themselves along with the line <span class="math-inline">\\(h(x&#95;i) = w x&#95;i\\)</span> are drawn in <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

In the vector view, we're finding the best scalar multiple of a vector in <span class="math-inline">\\(\mathbb{R}^n\\)</span> to make it as close as possible to another vector in <span class="math-inline">\\(\mathbb{R}^n\\)</span>. In the regression view, we're fitting a line (through the origin) to points in <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

Let's make the connection between the two viewpoints more explicit. In part **d)**, once we pick a value of <span class="math-inline">\\(w\\)</span>, the predictions for each <span class="math-inline">\\(x&#95;i\\)</span> are of the form <span class="math-inline">\\(w x&#95;i\\)</span>. A vector of predictions, <span class="math-inline">\\(\vec p\\)</span>, might look like:

<div class="math-display">
$$
\vec p = \begin{bmatrix} h(x_1) \\\\ h(x_2) \\\\ \vdots \\\\ h(x_n) \end{bmatrix} = \begin{bmatrix} w x_1 \\\\ w x_2 \\\\ \vdots \\\\ w x_n \end{bmatrix} = w \begin{bmatrix} x_1 \\\\ x_2 \\\\ \vdots \\\\ x_n \end{bmatrix} = w \vec x
$$
</div>

Given this, in 1-2 English sentences, explain why finding the <span class="math-inline">\\(w\\)</span> that minimizes

<span class="math-inline">\\(\displaystyle R&#95;\text{sq}(w) = \frac{1}{n}\sum&#95;{i=1}^n \big(y&#95;i - w x&#95;i\big)^2\\)</span> is equivalent to finding the scalar <span class="math-inline">\\(k\\)</span> that minimizes

<span class="math-inline">\\(\displaystyle f(k) = \lVert \vec y - k \vec x \rVert^2\\)</span>.

</div>
</div>

</div>

---

## Problem 6: Norms (12 pts)

In [the last section of Chapter 3.2](https://notes.eecs245.org/vectors/norms/#other-norms), we introduced the concept of vector norms *other than* the "default" Euclidean norm. Each of those norms describes a different way of measuring the length of a vector --- just like how different loss functions described different ways of measuring the error of a prediction.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) **In this part only**, let <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 \\\\ -6 \\\\ 0 \\\\ 2 \end{bmatrix}\\)</span>. Compute <span class="math-inline">\\(\lVert \vec v \rVert&#95;2\\)</span>, <span class="math-inline">\\(\lVert \vec v \rVert&#95;1\\)</span>, and <span class="math-inline">\\(\lVert \vec v \rVert&#95;\infty\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) In Problem 1, we introduced the parallelogram law, which states that

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

## Problem 7: Neighbors (10 pts)

This problem involves writing code and submitting it to the Gradescope autograder.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open `homeworks/hw03/hw03.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https://github.com/eecs245/sp26-code&urlpath=tree/sp26-code/homeworks/hw03/hw03.ipynb&branch=main) to open `hw03.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

To receive credit for the programming portion of the homework, you'll need to submit your completed notebook to the autograder on Gradescope. Your submission time for Homework 3 is the **latter** of your PDF and code submission times.

---

## Problem 8: Feedback (6 pts)

We'd like to get your feedback on how the course has been going so far, now that we're a few weeks in.

You can find the survey [at this link](https://docs.google.com/forms/d/e/1FAIpQLScjtXiAZMekz3ezBMt6Eshjxfze-QMcZM7hCQu_h-oLXv1xfg/viewform?usp=publish-editor). It is **not anonymous**, but it links to an anonymous feedback form if you'd like to provide some feedback anonymously.

Thank you for your feedback --- it's helping shape our brand-new course.
