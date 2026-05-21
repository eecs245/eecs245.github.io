---
layout: page
title: "Homework 4: Projections, Span, and Linear Independence"
description: "Homework 4: Projections, Span, and Linear Independence problems."
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

# Homework 4: Projections, Span, and Linear Independence

**due** Wednesday, May 20th, 2026 at 11:59PM Ann Arbor Time <span style="color: red;">(no slip days allowed!)</span>

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw04/hw04.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw04/hw04-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 3 Solutions Review](#problem-1-homework-3-solutions-review-10-pts)
- [Problem 2: Warmup](#problem-2-warmup-6-pts)
- [Problem 3: Projections](#problem-3-projections-7-pts)
- [Problem 4: Lines and Planes](#problem-4-lines-and-planes-11-pts)
- [Problem 5: Rows and Columns](#problem-5-rows-and-columns-12-pts)
- [Problem 6: Linear Independence of New Vectors](#problem-6-linear-independence-of-new-vectors-8-pts)
- [Problem 7: Intersections of Subspaces](#problem-7-intersections-of-subspaces-6-pts)

---

Total Points: 10 + 6 + 7 + 11 + 12 + 8 + 6 = 60

---

## Problem 1: Homework 3 Solutions Review (10 pts)

Review the solutions to Homework 3. Pick **two problem parts** (for example, Problem 2a and Problem 5b) from Homework 3 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 3, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

<details markdown="1"><summary>Solution</summary>

</details>

---

## Problem 2: Warmup (6 pts)

Let <span class="math-inline">\\(\vec u = \begin{bmatrix} k \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} 2 \\\\ -1 \end{bmatrix}\\)</span>, where <span class="math-inline">\\(k \in \mathbb{R}\\)</span> is some constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) Find all values of <span class="math-inline">\\(k\\)</span> such that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal.

<details markdown="1"><summary>Solution</summary>

In order for <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> to be orthogonal, their dot product must be 0.

<div class="math-display">
$$
\begin{align*}
\vec{u} \cdot \vec{v} &= 0 \\\\
k \cdot 2 + 3 \cdot (-1) &= 0 \\\\
2k-3&=0 \\\\
k &= \boxed{\frac{3}{2}}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find all values of <span class="math-inline">\\(k\\)</span> such that <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace) = \mathbb{R}^2\\)</span>.

<details markdown="1"><summary>Solution</summary>

As long as <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> aren't collinear --- that is, as long as <span class="math-inline">\\(\vec u \neq c \vec v\\)</span> for some <span class="math-inline">\\(c \in \mathbb{R}\\)</span> --- then <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace) = \mathbb{R}^2\\)</span>. Since we have 2 vectors, we can solve for the <span class="math-inline">\\(c\\)</span> that makes <span class="math-inline">\\(\vec{u}\\)</span> a scalar multiple of <span class="math-inline">\\(\vec{v}\\)</span>.

<div class="math-display">
$$
\begin{align*}
\vec{u}&= c\vec{v} \\\\
\begin{bmatrix} k \\\\ 3 \end{bmatrix} &= c \begin{bmatrix} 2 \\\\ -1 \end{bmatrix} \\\\
k &= 2c \\\\
3 &= -c \\\\
\end{align*}
$$
</div>

The above equations imply that <span class="math-inline">\\(c = -3\\)</span> and <span class="math-inline">\\(k = 2c = -6\\)</span>.

So, in order for <span class="math-inline">\\(\vec{u} \neq c\vec{v}\\)</span> to be true, <span class="math-inline">\\(\boxed{k \neq -6}\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find all values of <span class="math-inline">\\(k\\)</span> such that <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span> is a line in <span class="math-inline">\\(\mathbb{R}^2\\)</span>. Then, write the equation of that line, in both slope-intercept form (<span class="math-inline">\\(y = mx + b\\)</span>) and parametric form. (The parametric form of a line is introduced in [Chapter 4.4](https://notes.eecs245.org/linear-independence/lines-planes-hyperplanes/#lines-in-parametric-form). There are infinitely many possible answers; give just one.)

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span> to be a line, they must be collinear. So <span class="math-inline">\\(\vec{u}=c\vec{v}\\)</span> for some <span class="math-inline">\\(c \in \mathbb{R}\\)</span> must be true. We know from our solution in part **b)** that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are collinear when <span class="math-inline">\\(\boxed{k = -6}\\)</span>.

In parametric form, the line spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is the same as the line spanned by <span class="math-inline">\\(\vec v\\)</span> (since they point in the same direction), which is

<div class="math-display">
$$
\boxed{L = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix} + t \begin{bmatrix} 2 \\\\ -1 \end{bmatrix}, \quad t \in \mathbb{R}}
$$
</div>

There are infinitely many ways to write a particular line in parametric form, so as long as the point lies on the line and the slope is some <span class="math-inline">\\(c\vec{u}\\)</span> or <span class="math-inline">\\(c\vec{v}\\)</span> where <span class="math-inline">\\(c \in \mathbb{R}\\)</span>, we've correctly described the line in question. So, we could have used <span class="math-inline">\\(L = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix} + t\begin{bmatrix} -40 \\\\ 20\end{bmatrix}, \quad t \in \mathbb{R}\\)</span> if we wanted.

Next, we'll need to find the line in slope-intercept form. Scaling <span class="math-inline">\\(\vec{v}\\)</span> by <span class="math-inline">\\(\frac{1}{2}\\)</span> gives us <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -\frac{1}{2} \end{bmatrix}\\)</span>, a vector which tells us how much <span class="math-inline">\\(y\\)</span> changes for each change in <span class="math-inline">\\(x\\)</span>, so our slope is <span class="math-inline">\\(-\frac{1}{2}\\)</span>. Lastly, the line must go through the origin because it's a span of vectors, telling us the intercept is 0. So, in slope-intercept form, our line is <span class="math-inline">\\(\boxed{y = -\frac{1}{2}x}\\)</span>.

</details>

</div>
</div>

</div>

---

## Problem 3: Projections (7 pts)

Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>. Let <span class="math-inline">\\(\vec p\\)</span> be the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>, and let <span class="math-inline">\\(\vec e = \vec u - \vec p\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Which of the following vectors is <span class="math-inline">\\(\vec e\\)</span> orthogonal to, and why? Select all that apply.

<div class="math-display">
$$
\vec u, \quad \vec v, \quad \vec p
$$
</div>

 (You don't need to rederive any results from [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-projections), but we do want to hear your reasoning.)

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\vec e\\)</span> is orthogonal to <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec p\\)</span>. The error vector <span class="math-inline">\\(\vec{e}\\)</span> is the vector with the shortest distance from <span class="math-inline">\\(\vec{v}\\)</span> to <span class="math-inline">\\(\vec{u}\\)</span>, so it must be orthogonal to <span class="math-inline">\\(\vec{v}\\)</span>. <span class="math-inline">\\(\vec{p} = \frac{\vec{u} \cdot \vec{v}}{\vec v \cdot \vec v}\vec{v}\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec{v}\\)</span>, so <span class="math-inline">\\(\vec{e}\\)</span> is orthogonal to it as well.

Refer to a picture of the situation [here](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-projections) (scroll down to the second picture in the "Orthogonal Projections" section).

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts)
<span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span> is the set of all possible linear combinations of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. Similarly, <span class="math-inline">\\(\text{span}(\lbrace\vec e, \vec v\rbrace)\\)</span> is the set of all possible linear combinations of <span class="math-inline">\\(\vec e\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

Let's prove that <span class="math-inline">\\(\text{span}(\lbrace\vec e, \vec v\rbrace) = \text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, meaning that every vector you can create with <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> can also be created with <span class="math-inline">\\(\vec e\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and vice versa.

Remember that the span of a set of vectors is a **set** too. To show that two sets <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are equal, we need to show that every element of <span class="math-inline">\\(A\\)</span> is in <span class="math-inline">\\(B\\)</span>, and every element of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(A\\)</span>.

Here, we'll show that

1.  if <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, then <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec e, \vec v\rbrace)\\)</span>,

2.  if <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec e, \vec v\rbrace)\\)</span>, then <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>.

We'll do **(i)** for you. If <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, then

<div class="math-display">
$$
\vec x = a \vec u + b \vec v
$$
</div>

 for some scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>. But, we know that <span class="math-inline">\\(\vec e = \vec u - \vec p\\)</span>, meaning that <span class="math-inline">\\(\vec u = \vec e + \vec p\\)</span>. This gives

<div class="math-display">
$$
\vec x = a (\vec e + \vec p) + b \vec v = a \vec e + a \vec p + b \vec v
$$
</div>

But, <span class="math-inline">\\(\vec p\\)</span> --- the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> --- is a vector in the direction of <span class="math-inline">\\(\vec v\\)</span>, meaning that <span class="math-inline">\\(\vec p = c \vec v\\)</span> for some scalar <span class="math-inline">\\(c\\)</span>. ([Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-decomposition) has the optimal value of <span class="math-inline">\\(c\\)</span> but it's not important in this proof.) Substituting <span class="math-inline">\\(\vec p = c \vec v\\)</span> gives us

<div class="math-display">
$$
\vec x = a \vec e + a \vec p + b \vec v = a \vec e + a (c \vec v) + b \vec v = a \vec e + (ac + b) \vec v
$$
</div>

This last expression, <span class="math-inline">\\(a \vec e + (ac + b) \vec v\\)</span>, is a linear combination of <span class="math-inline">\\(\vec e\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, meaning that <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec e, \vec v\rbrace)\\)</span>, as required.

Your turn: complete **(ii)** by showing that if <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec e, \vec v\rbrace)\\)</span>, then <span class="math-inline">\\(\vec x \in \text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>.

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\vec{x} \in \text{span}(\lbrace\vec{e}, \vec{v}\rbrace)\\)</span>, then

<div class="math-display">
$$
\begin{align*}
\vec{x} &= a\vec{e} + b\vec{v} \\\\
&=a(\vec{u}-\vec{p}) + b\vec{v} \\\\
&=a(\vec{u}-c\vec{v}) + b\vec{v} \\\\
&= a\vec{u} - ac\vec{v} + b\vec{v} \\\\
&= a\vec{u} + (b - ac)\vec{v}
\end{align*}
$$
</div>

<span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b-ac\\)</span> are both scalars, so <span class="math-inline">\\(\vec{x}\in \text{span}(\lbrace\vec e, \vec v\rbrace)\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) To recap, the point of the previous part was to show that any vector that can be created with <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> can also be created with <span class="math-inline">\\(\vec e\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

Using what you learned in [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-decomposition) (and Lab 4), explain why we'd rather write some new vector <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec e\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, rather than <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

<details markdown="1"><summary>Solution</summary>

We prefer using <span class="math-inline">\\(\vec{e}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> because they are orthogonal, so writing <span class="math-inline">\\(\vec{b}\\)</span> as a linear combination of them doesn't involve solving a system of equations --- instead, we can find the scalars on <span class="math-inline">\\(\vec e\\)</span> and <span class="math-inline">\\(\vec v\\)</span> through orthogonal projections, which is simpler.

For example, to find scalars <span class="math-inline">\\(a&#95;1\\)</span> and <span class="math-inline">\\(a&#95;2\\)</span> such that

<div class="math-display">
$$
a_1 \vec e + a_2 \vec v = \vec b
$$
</div>

we know that <span class="math-inline">\\(a&#95;1 = \frac{\vec b \cdot \vec e}{\vec e \cdot \vec e}\\)</span> and <span class="math-inline">\\(a&#95;2 = \frac{\vec b \cdot \vec v}{\vec v \cdot \vec v}\\)</span>.

To review why this is the case, see the end of [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-decomposition). But in short, we could start with

<div class="math-display">
$$
a_1 \vec e + a_2 \vec v = \vec b
$$
</div>

and take the dot product of both sides with <span class="math-inline">\\(\vec e\\)</span>, which gives us

<div class="math-display">
$$
a_1 \vec e \cdot \vec e + a_2 \vec v \cdot \vec e = \vec b \cdot \vec e
$$
</div>

Since <span class="math-inline">\\(\vec e \cdot \vec = 0\\)</span>, this says

<div class="math-display">
$$
a_1 \vec e \cdot \vec e = \vec b \cdot \vec e \implies a_1 = \frac{\vec b \cdot \vec e}{\vec e \cdot \vec e}
$$
</div>

which is precisely the coefficient we'd find when projecting <span class="math-inline">\\(\vec b\\)</span> onto <span class="math-inline">\\(\vec e\\)</span>.

</details>

</div>
</div>

</div>

---

## Problem 4: Lines and Planes (11 pts)

As we saw in [Chapter 4.1](https://notes.eecs245.org/linear-independence/span/#span-of-two-vectors), the span of two linearly independent vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> is a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, which we call a plane when working with vectors from <span class="math-inline">\\(\mathbb{R}^3\\)</span>. In this problem, we will build your understanding of lines and planes in <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

To help you visualize lines and planes, consult:

-   (Primary) **The supplemental Jupyter Notebook** we've created for Homework 4, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw04%2Fhw04.ipynb&branch=main) on DataHub, or [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw04/hw04.ipynb) in the course GitHub repository.

-   [Chapter 4.4](https://notes.eecs245.org/linear-independence/span/#overview) of the course notes, which focuses on this idea (and is a detour in the main storyline of the notes).

-   **The Lab 4 solutions**, once they are released.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Consider the plane <span class="math-inline">\\(7x - 3y + 4z = 0\\)</span>. This is a plane written in standard form,

<div class="math-display">
$$
ax + by + cz + d = 0
$$
</div>

Find two vectors that lie in this plane, and use those vectors to write the plane in parametric form. (There are infinitely many possible answers, since the parametric form of a line, or plane, or subspace in general is not unique.)

<details markdown="1"><summary>Solution</summary>

Let's use <span class="math-inline">\\(\vec{u}=\begin{bmatrix} 1 \\\\ 1 \\\\ -1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec{v}=\begin{bmatrix} 6 \\\\ 10 \\\\ -3 \end{bmatrix}\\)</span> as our vectors that lie in the plane. There is nothing special about the numbers we've put in <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>; they just happen to satisfy <span class="math-inline">\\(7x - 3y + 4z = 0\\)</span>, as we'll verify below.

<div class="math-display">
$$
\begin{align*}
\text{using } &\vec{u}, \:\: 7(1) -3(1) +4(-1) \\\\
&=7-3-4=0\\\\
\\\\
\text{using } &\vec{v}, \:\: 7(6) -3(10) +4(-3) \\\\
&=42-30-12=0
\end{align*}
$$
</div>

The standard form of the plane tells us that <span class="math-inline">\\(d=0\\)</span>, meaning the plane contains the origin. So, we can write our plane's parametric form as:

<div class="math-display">
$$
\begin{align*}
&\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix} + s\vec{u} + t\vec{v} \\\\
&=\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix} + s\begin{bmatrix} 1 \\\\ 1 \\\\ -1 \end{bmatrix} + t\begin{bmatrix} 6 \\\\ 10 \\\\ -3 \end{bmatrix}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(8 pts) Consider the linearly independent vectors

<div class="math-display">
$$
\vec v_1 = \begin{bmatrix} 7 \\\\ -1 \\\\ 2 \end{bmatrix}, \quad \vec v_2 = \begin{bmatrix} 2 \\\\ 1 \\\\ 1 \end{bmatrix}, \quad \vec v_3 = \begin{bmatrix} 3 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

1.  In standard form, find the equation of the plane spanned by <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span>.

    <em>Hint: Use the cross product from <a href="https://notes.eecs245.org/linear-independence/lines-planes-hyperplanes/">Chapter 4.4</a> to find the values of <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> in <span class="math-inline">\\(ax + by + cz + d = 0\\)</span>, and you know what <span class="math-inline">\\(d\\)</span> must be by the definition of the span of a set of vectors.</em>

2.  In standard form, find the equation of the plane spanned by <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;3\\)</span>.

    Your answer should be a different plane than the one you found in subpart **(i)**. (This is an important point: since <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span> are linearly independent, any pair of them span a plane, but all three pairs of them span different planes.)

3.  The planes you find in subparts **(i)** and **(ii)** intersect at a **line**. Solve for the equation of this line of intersection in parametric form. What do you notice about the equation of the line?

   To help you visualize this line of intersection, use the supplemental Jupyter Notebook.

4.  In standard form, find the equation of the plane spanned by <span class="math-inline">\\(\vec v&#95;2\\)</span> and <span class="math-inline">\\(\vec v&#95;3\\)</span>. Now, find the intersection of this plane with the object from subpart **(iii)**. What type of geometric object is this new intersection?

   Once again, use the supplemental Jupyter Notebook to visualize this intersection.

<details markdown="1"><summary>Solution</summary>

To find the standard form of a plane for parts <span class="math-inline">\\(\textbf{(i)}\\)</span> and <span class="math-inline">\\(\textbf{(ii)}\\)</span>, we take the cross product of the two vectors used to span the plane. The resulting vector's components are the coefficients of the equation. For these planes, <span class="math-inline">\\(d=0\\)</span> by definition of a span of a set of vectors

<span class="math-inline">\\(\textbf{(i)}\\)</span>

<div class="math-display">
$$
\begin{align*}
\vec{v}_1 \times \vec{v}_2 &= \begin{bmatrix} (-1) \cdot 1 - 2 \cdot 1 \\\\ 2 \cdot 2 - 7 \cdot 1 \\\\ 7 \cdot 1 - (-1) \cdot 2 \end{bmatrix} \\\\
&= \begin{bmatrix} -1 -2 \\\\ 4-7 \\\\ 7+2 \end{bmatrix} \\\\
&= \begin{bmatrix} -3 \\\\ -3 \\\\ 9 \end{bmatrix}
\end{align*}
$$
</div>

So, the plane spanned by <span class="math-inline">\\(\vec{v}&#95;1\\)</span> and <span class="math-inline">\\(\vec{v}&#95;2\\)</span> is:

<div class="math-display">
$$
\begin{align*}
-3x - 3y + 9z = 0
\end{align*}
$$
</div>

You can verify that <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> both satisfy this equation by plugging them in.

<span class="math-inline">\\(\textbf{(ii)}\\)</span>

<div class="math-display">
$$
\begin{align*}
\vec{v}_1 \times \vec{v}_3 &= \begin{bmatrix} (-1) \cdot 1 - 2 \cdot 1 \\\\ 2 \cdot 3 - 7 \cdot 1 \\\\ 7 \cdot 1 - (-1) \cdot 3 \end{bmatrix} \\\\
&= \begin{bmatrix} -1-2 \\\\ 6-7 \\\\ 7+3 \end{bmatrix} \\\\
&= \begin{bmatrix} -3 \\\\ -1 \\\\ 10 \end{bmatrix} \\\\
\end{align*}
$$
</div>

So, the plane spanned by <span class="math-inline">\\(\vec{v}&#95;1\\)</span> and <span class="math-inline">\\(\vec{v}&#95;3\\)</span> is:

<div class="math-display">
$$
\begin{align*}
-3x - y + 10z = 0
\end{align*}
$$
</div>

<span class="math-inline">\\(\textbf{(iii)}\\)</span>

The intersection of the two planes is a line that passes through <span class="math-inline">\\((0, 0, 0)\\)</span>, since both planes pass through the origin. We know that lines that pass through the origin can be written as the span of a single vector. We also know that the vector <span class="math-inline">\\(\vec v&#95;1\\)</span>, by definition, is on that line, since it's on both the plane from part <span class="math-inline">\\(\textbf{(i)}\\)</span> and the plane from part <span class="math-inline">\\(\textbf{(ii)}\\)</span>. So, the line of intersection is the span of <span class="math-inline">\\(\vec v&#95;1\\)</span>. In parametric form, this is:

<div class="math-display">
$$
L = t\begin{bmatrix} 7 \\\\ -1 \\\\ 2 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

You might not have noticed this immediately, which is fine: there's an algebraic solution too. Let's look at the two equations for the planes from parts <span class="math-inline">\\(\textbf{(i)}\\)</span> and <span class="math-inline">\\(\textbf{(ii)}\\)</span>:

<div class="math-display">
$$
\begin{align*}
-3x - 3y + 9z &= 0 \\\\
-3x - y + 10z &= 0
\end{align*}
$$
</div>

This is a system of 2 equations with 3 unknowns, which means that we won't be able to find a single unique solution. But, we can find a parametric solution by solving for one variable in terms of the other two. Let's pick <span class="math-inline">\\(y\\)</span> as the parameter; call it <span class="math-inline">\\(t\\)</span>. Now, let's solve for <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(z\\)</span> in terms of <span class="math-inline">\\(t\\)</span>.

<div class="math-display">
$$
\begin{align*}
-3x - 3t + 9z &= 0 \\\\
-3x - t + 10z &= 0
\end{align*}
$$
</div>

Subtracting the second equation from the first, we get:

<div class="math-display">
$$
\begin{align*}
-2t - z &= 0 \\\\
z &= -2t
\end{align*}
$$
</div>

Substituting <span class="math-inline">\\(z = -2t\\)</span> back into the first equation gives

<div class="math-display">
$$
-3x - 3t + 9(-2t) = 0 \implies -3x - 3t - 18t = 0 \implies -3x - 21t = 0 \implies x = -7t
$$
</div>

So, the parametric solution is:

<div class="math-display">
$$
x = -7t, \quad y = t, \quad z = -2t, \quad t \in \mathbb{R}
$$
</div>

or, equivalently,

<div class="math-display">
$$
t\begin{bmatrix} -7 \\\\ 1 \\\\ -2 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

Which is the same as the form we found earlier!

**(iv)**

<div class="math-display">
$$
\begin{align*}
\vec{v}_2 \times \vec{v}_3 &= \begin{bmatrix} 1 \cdot 1 - 1 \cdot 1 \\\\ 1 \cdot 3 - 2 \cdot 1 \\\\ 2 \cdot 1 - 1 \cdot 3 \end{bmatrix} \\\\
&= \begin{bmatrix} 1 - 1 \\\\ 3 - 2 \\\\ 2 - 3 \end{bmatrix} \\\\
&= \begin{bmatrix} 0 \\\\ 1 \\\\ -1 \end{bmatrix}
\end{align*}
$$
</div>

So, the plane spanned by <span class="math-inline">\\(\vec{v}&#95;2\\)</span> and <span class="math-inline">\\(\vec{v}&#95;3\\)</span> is:

<div class="math-display">
$$
\begin{align*}
y-z = 0
\end{align*}
$$
</div>

The intersection between this new plane and the line from part <span class="math-inline">\\(\textbf{(iii)}\\)</span> is the point <span class="math-inline">\\((0, 0, 0)\\)</span>. All three planes we've found in this problem pass through the origin, and all three planes have different slopes, so their intersection is the single point <span class="math-inline">\\((0, 0, 0)\\)</span>.

</details>

</div>
</div>

</div>

---

## Problem 5: Rows and Columns (12 pts)

Soon, we will start to learn about matrices. In this problem, we'll start to connect what we've learned about vectors and spans to matrices. In this question, we'll consider the matrix <span class="math-inline">\\(A\\)</span>:

<div class="math-display">
$$
A = \begin{bmatrix}
5 & 3 & 5 & 2 \\\\
3 & 0 & -6 & 4 \\\\
-2 & 0 & 4 & 3 \\\\
8 & 2 & -6 & -8 \\\\
1 & 1 & 3 & 0
\end{bmatrix}
$$
</div>

<span class="math-inline">\\(A\\)</span> has 5 rows and 4 columns. There are two ways of looking at <span class="math-inline">\\(A\\)</span>:

1.  As a collection of **4 "column" vectors**, each in <span class="math-inline">\\(\mathbb{R}^5\\)</span>, stacked side-by-side.

2.  As a collection of **5 "row" vectors**, each in <span class="math-inline">\\(\mathbb{R}^4\\)</span>, stacked on top of each other.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Using the algorithm in [Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/#finding-linearly-independent-subsets-with-the-same-span), find a linearly independent set of vectors in <span class="math-inline">\\(\mathbb{R}^5\\)</span> with the same span as the column vectors of <span class="math-inline">\\(A\\)</span>. How many vectors are in this set?

<details markdown="1"><summary>Solution</summary>

Our goal is to find the set of linearly independent column vectors for the matrix <span class="math-inline">\\(A\\)</span>, as is outlined in the notes.

Let

<div class="math-display">
$$
\begin{align*}
\vec{v_1}=\begin{bmatrix} 5 \\\\ 3 \\\\ -2 \\\\ 8 \\\\ 1 \end{bmatrix} \qquad \vec{v_2}= \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \\\\ 2 \\\\ 1 \end{bmatrix} \qquad \vec{v_3} = \begin{bmatrix} 5 \\\\ -6 \\\\ 4 \\\\ -6 \\\\ 3 \end{bmatrix} \qquad \vec{v_4} = \begin{bmatrix} 2 \\\\ 4 \\\\ 3 \\\\ -8 \\\\ 0 \end{bmatrix}
\end{align*}
$$
</div>

<span class="math-inline">\\(i=2,S=\lbrace\vec{v&#95;1}\rbrace: \vec{v&#95;2} \notin \text{span}(S)\\)</span>. There's no way to make <span class="math-inline">\\(\vec{v&#95;2}\\)</span> as a linear combination of <span class="math-inline">\\(v&#95;1\\)</span> because of the 0's in <span class="math-inline">\\(\vec{v&#95;2}\\)</span>. So, we add <span class="math-inline">\\(\vec{v&#95;2}\\)</span> to the set.

<span class="math-inline">\\(i=3,S=\lbrace\vec{v&#95;1}, \vec{v&#95;2}\rbrace:\\)</span> Let's try to write <span class="math-inline">\\(\vec{v&#95;3}\\)</span> as a linear combination of <span class="math-inline">\\(\vec{v&#95;1}\\)</span> and <span class="math-inline">\\(\vec{v&#95;2}\\)</span>, i.e. solve the system of equations we get from <span class="math-inline">\\(a\vec{v&#95;1} + b\vec{v&#95;2} = \vec{v&#95;3}\\)</span>:

<div class="math-display">
$$
\begin{align}
5a + 3b &= 5 \\\\
3a &= -6 \\\\
-2a &= 4 \\\\
8a + 2b &= -6 \\\\
a + b &= 3
\end{align}
$$
</div>

Equations (2) and (3) tell us <span class="math-inline">\\(a = -2\\)</span>. Plugging this into equations (1), (4), and (5) each tell us that <span class="math-inline">\\(b = 5\\)</span>. So, <span class="math-inline">\\(a = -2, b = 5\\)</span> satisfy all 5 equations, meaning that <span class="math-inline">\\(\vec{v&#95;3}\\)</span> is a linear combination of <span class="math-inline">\\(\vec{v&#95;1}\\)</span> and <span class="math-inline">\\(\vec{v&#95;2}\\)</span>. (If we found that some equations implied <span class="math-inline">\\(b = -5\\)</span> and some implied <span class="math-inline">\\(b\\)</span> was something else, the equations would be inconsistent, meaning that <span class="math-inline">\\(\vec{v&#95;3}\\)</span> is not a linear combination of <span class="math-inline">\\(\vec{v&#95;1}\\)</span> and <span class="math-inline">\\(\vec{v&#95;2}\\)</span>.)

Since <span class="math-inline">\\(\vec{v&#95;3} \in \text{span}(S)\\)</span>, we don't add it to <span class="math-inline">\\(S\\)</span>.

<span class="math-inline">\\(i=4,S=\lbrace\vec{v&#95;1}, \vec{v&#95;2}\rbrace:\\)</span> Let's try to write <span class="math-inline">\\(\vec{v&#95;4}\\)</span> as a linear combination of the vectors in <span class="math-inline">\\(S\\)</span>, i.e. solve the system of equations we get from <span class="math-inline">\\(a\vec{v&#95;1}+b\vec{v&#95;2}=\vec{v&#95;4}\\)</span>:

<div class="math-display">
$$
\begin{align}
5a + 3b &= 2 \tag{1} \\\\
3a &= 4 \tag{2} \\\\
-2a &= 3 \tag{3} \\\\
8a + 2b &= -9 \tag{4} \\\\
a + b &= 0 \tag{5}
\end{align}
$$
</div>

In equations (2) and (3), simplifying for <span class="math-inline">\\(a\\)</span> gives us <span class="math-inline">\\(a=\frac{4}{3}\\)</span> and <span class="math-inline">\\(a=-\frac{3}{2}\\)</span>. This is a contradiction, so <span class="math-inline">\\(\vec{v&#95;4} \notin \text{span}(S)\\)</span>, so we should add it to the set.

Therefore, our set of linearly independent vectors in <span class="math-inline">\\(\mathbb{R}^5\\)</span> is <span class="math-inline">\\(\boxed{S=\lbrace\vec{v&#95;1}, \vec{v&#95;2}, \vec{v&#95;4}\rbrace}\\)</span>, a set of 3 vectors.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a linearly independent set of vectors in <span class="math-inline">\\(\mathbb{R}^4\\)</span> with the same span as the row vectors of <span class="math-inline">\\(A\\)</span>. How many vectors are in this set?

<details markdown="1"><summary>Solution</summary>

We can use a similar process as we did in the previous part, but on the rows of <span class="math-inline">\\(A\\)</span> rather than the columns.

Let

<div class="math-display">
$$
\begin{align*}
\vec{v_1}=\begin{bmatrix} 5 \\\\ 3 \\\\ 5 \\\\ 2 \end{bmatrix} \qquad \vec{v_2}= \begin{bmatrix} 3 \\\\ 0 \\\\ -6 \\\\ 4\end{bmatrix} \qquad \vec{v_3} = \begin{bmatrix} -2 \\\\ 0 \\\\ 4 \\\\ 3 \end{bmatrix} \qquad \vec{v_4} = \begin{bmatrix} 8 \\\\ 2 \\\\ -6 \\\\ -8 \end{bmatrix} \qquad \vec{v_5}=\begin{bmatrix}1 \\\\ 1\\\\ 3 \\\\0\end{bmatrix}
\end{align*}
$$
</div>

<span class="math-inline">\\(i=2,S=\lbrace\vec{v&#95;1}\rbrace: \vec{v&#95;2} \notin \text{span}(S)\\)</span>. There's no way to make <span class="math-inline">\\(\vec{v&#95;2}\\)</span> as a linear combination of <span class="math-inline">\\(v&#95;1\\)</span> because of the 0 in <span class="math-inline">\\(\vec{v&#95;2}\\)</span>. So, we add <span class="math-inline">\\(\vec{v&#95;2}\\)</span> to the set.

<span class="math-inline">\\(i=3,S=\lbrace\vec{v&#95;1}, \vec{v&#95;2}\rbrace:\\)</span> Let's try to write <span class="math-inline">\\(\vec v&#95;3\\)</span> as a linear combination of <span class="math-inline">\\(\vec{v&#95;1}\\)</span> and <span class="math-inline">\\(\vec{v&#95;2}\\)</span>, i.e. solve the system of equations we get from <span class="math-inline">\\(a\vec{v&#95;1} + b\vec{v&#95;2} = \vec{v&#95;3}\\)</span>:

<div class="math-display">
$$
\begin{align}
5a+3b&=-2 \tag{1} \\\\
3a &= 0 \tag{2} \\\\
5a-6b &= 4 \tag{3} \\\\
2a - 4b &= 3 \tag{4}
\end{align}
$$
</div>

In equation (2), we see that <span class="math-inline">\\(a=0\\)</span>. Plugging this into equations (1), (3), and (4) gives us:

<div class="math-display">
$$
\begin{align*}
3b &= -2 \\\\
5b &= 4 \\\\
-4b &= 3
\end{align*}
$$
</div>

These give us contradictions, so <span class="math-inline">\\(\vec{v&#95;3} \notin \text{span}(S)\\)</span>, so we should add it to the set.

<span class="math-inline">\\(i=4,S=\lbrace\vec{v&#95;1}, \vec{v&#95;2}, \vec{v&#95;3}\rbrace:\\)</span> Let's try to write <span class="math-inline">\\(\vec{v&#95;4}\\)</span> as a linear combination of the vectors in <span class="math-inline">\\(S\\)</span>, i.e. solve the system of equations we get from <span class="math-inline">\\(a\vec{v&#95;1}+b\vec{v&#95;2}+c\vec{v&#95;3}=\vec{v&#95;4}\\)</span>:

<div class="math-display">
$$
\begin{align}
5a+3b -2c&=8 \tag{1} \\\\
3a &= 2 \tag{2} \\\\
5a-6b +4c&= -6 \tag{3} \\\\
2a - 4b +3c&= -8 \tag{4}
\end{align}
$$
</div>

In equation (2), we see that <span class="math-inline">\\(a=\frac{2}{3}\\)</span>. Plugging this into equations (1), (3), and (4) gives us:

<div class="math-display">
$$
\begin{align*}
\frac{10}{3} + 3b -2c &= 8 \implies 3b -2c = \frac{14}{3} \\\\
\frac{10}{3} -6b +4c &= -6 \implies -6b +4c = -\frac{28}{3} \\\\
\frac{4}{3} -4b +3c &= -8 \implies -4b +3c = -\frac{28}{3}
\end{align*}
$$
</div>

Notice that the new first and second equations are the same; the second is just the first multiplied by -2. Since the second and third equations don't look like parallel lines, they will intersect somewhere, and so there does exist a solution for <span class="math-inline">\\(a, b, c\\)</span>. We don't even need to bother looking for it, though you can verify yourself that <span class="math-inline">\\(a = \frac{2}{3}, b = -\frac{14}{3}, c = -\frac{28}{3}\\)</span> satisfy all four original equations.

So, <span class="math-inline">\\(\vec{v&#95;4} \in \text{span}(S)\\)</span>, so we don't add it to the set.

<span class="math-inline">\\(i = 5, S = \lbrace\vec{v&#95;1}, \vec{v&#95;2}, \vec{v&#95;3}\rbrace:\\)</span> Let's try to write <span class="math-inline">\\(\vec{v&#95;5}\\)</span> as a linear combination of the vectors in <span class="math-inline">\\(S\\)</span>, i.e. solve the system of equations we get from <span class="math-inline">\\(a\vec{v&#95;1}+b\vec{v&#95;2}+c\vec{v&#95;3}=\vec{v&#95;5}\\)</span>:

<div class="math-display">
$$
\begin{align}
5a+3b -2c&=1 \tag{1} \\\\
3a &= 1 \tag{2} \\\\
5a-6b +4c&= 3 \tag{3} \\\\
2a - 4b +3c&= 0 \tag{4}
\end{align}
$$
</div>

You can verify yourself that <span class="math-inline">\\(a = \frac{1}{3}, b = -\frac{10}{3}, c = -\frac{14}{3}\\)</span> satisfy all four equations. So, <span class="math-inline">\\(\vec{v&#95;5} \in \text{span}(S)\\)</span>, so we don't add it to the set.

Therefore, our set of linearly independent vectors in <span class="math-inline">\\(\mathbb{R}^4\\)</span> is <span class="math-inline">\\(\boxed{S=\lbrace\vec{v&#95;1}, \vec{v&#95;2}, \vec{v&#95;3}\rbrace}\\)</span>, a set of 3 vectors.

</details>

You should have found that the number of vectors you found in both parts is the same. This is not a coincidence, it is true for any matrix --- the number of linearly independent columns is the same as the number of linearly independent rows. This number is called the **rank** of the matrix.

If you were to run the following Python code, the number you'd see back is the number of linearly independent vectors you found in both parts.

    import numpy as np

    A = np.array([[5, 3, 5, 2],
                  [3, 0, -6, 4],
                  [-2, 0, 4, 3],
                  [8, 2, -6, -8],
                  [1, 1, 3, 0]])

    np.linalg.matrix_rank(A)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Open the **the supplemental Jupyter Notebook** we've created for Homework 4, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw04%2Fhw04.ipynb&branch=main) on DataHub, or [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw04/hw04.ipynb) in the course GitHub repository.

Complete the three tasks within orange lines, related to the introduction we've provided above. Include screenshots of your code and its output as part of your PDF.

<details markdown="1"><summary>Solution</summary>

![image](imgs/hw04-prob4c-sol1.png) ![image](imgs/hw04-prob4c-sol2.png) ![image](imgs/hw04-prob4c-sol3.png)

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Using what you observed in the notebook, **by hand** (that is, without using Python), compute the result of the following matrix-vector multiplication:

<div class="math-display">
$$
\begin{bmatrix} 2 & 4 & 5 \\\\ 3 & 9 & 8 \\\\ 4 & 0 & 1 \end{bmatrix} \begin{bmatrix} 4 \\\\ 1 \\\\ 3 \end{bmatrix}
$$
</div>

<details markdown="1"><summary>Solution</summary>

As we saw, the product will contain the dot product of the rows of the matrix with the vector. So, we can compute each dot product manually:

<div class="math-display">
$$
\begin{align*}
\text{first row of output:} \quad 2 \cdot 4 + 4 \cdot 1 + 5 \cdot 3 &= 8 + 4 + 15 = 27 \\\\
\text{second row of output:} \quad 3 \cdot 4 + 9 \cdot 1 + 8 \cdot 3 &= 12 + 9 + 24 = 45 \\\\
\text{third row of output:} \quad 4 \cdot 4 + 0 \cdot 1 + 1 \cdot 3 &= 16 + 0 + 3 = 19
\end{align*}
$$
</div>

Therefore, the product is <span class="math-inline">\\(\boxed{\begin{bmatrix} 27 \\\\ 45 \\\\ 19 \end{bmatrix}}\\)</span>.

</details>

</div>
</div>

</div>

---

## Problem 6: Linear Independence of New Vectors (8 pts)

Suppose <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3 \in \mathbb{R}^n\\)</span> **are linearly independent**. In both parts below, determine if the new set of vectors is linearly independent. If they are, prove that they are by showing that the only solution to the equation

<div class="math-display">
$$
a \vec u_1 + b \vec u_2 + c \vec u_3 = \vec 0
$$
</div>

is <span class="math-inline">\\(a = b = c = 0\\)</span>. If they are not, show that there exist scalars <span class="math-inline">\\(a, b, c\\)</span> such that <span class="math-inline">\\(a \vec u&#95;1 + b \vec u&#95;2 + c \vec u&#95;3 = \vec 0\\)</span> where at least one of <span class="math-inline">\\(a, b, c\\)</span> is non-zero.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\vec u&#95;1 = \vec v&#95;2 - \vec v&#95;3\\)</span>, <span class="math-inline">\\(\vec u&#95;2 = \vec v&#95;1 - \vec v&#95;3\\)</span>, and <span class="math-inline">\\(\vec u&#95;3 = \vec v&#95;1 - \vec v&#95;2\\)</span>

<details markdown="1"><summary>Solution</summary>

These vectors are **linearly dependent**.

Let's start by writing

<div class="math-display">
$$
a\vec{u_1} + b\vec{u_2} + c\vec{u_3} = \vec{0}
$$
</div>

We need to try and find all solutions for <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> in the equation above.

Plugging in <span class="math-inline">\\(\vec{u&#95;1}, \vec{u&#95;2}, \vec{u&#95;3}\\)</span> gives us

<div class="math-display">
$$
\begin{align*}
a(\vec{v_2} - \vec{v_3}) + b(\vec{v_1} - \vec{v_3}) + c(\vec{v_1} - \vec{v_2}) &= \vec{0} \\\\
a\vec{v_2} - a\vec{v_3} + b\vec{v_1} - b\vec{v_3} + c\vec{v_1} - c\vec{v_2} &= \vec{0}
\end{align*}
$$
</div>

From here, let's collect like terms:

<div class="math-display">
$$
\begin{align*}
(b + c)\vec v_1 + (a - c) \vec v_2 + (-a - b)\vec v_3 = \vec{0}
\end{align*}
$$
</div>

But, since <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span> are linearly independent, the only solution to this equation is that all three of <span class="math-inline">\\(b + c\\)</span>, <span class="math-inline">\\(a - c\\)</span>, and <span class="math-inline">\\(-a - b\\)</span> are 0.

<div class="math-display">
$$
\begin{align*}
b + c &= 0 \\\\
a - c &= 0 \\\\
-a - b &= 0
\end{align*}
$$
</div>

The above tells us that <span class="math-inline">\\(a = c\\)</span> and <span class="math-inline">\\(b = -c\\)</span>, meaning that any solution of the form <span class="math-inline">\\((c, -c, c)\\)</span> is a non-zero solution to the equation <span class="math-inline">\\(a\vec{u&#95;1} + b\vec{u&#95;2} + c\vec{u&#95;3} = \vec{0}\\)</span>. For example, if we set <span class="math-inline">\\(c = 5\\)</span>, then

<div class="math-display">
$$
5\vec{u_1} - 5\vec{u_2} + 5\vec{u_3} = \vec 0
$$
</div>

So, there exists a non-zero solution to the equation <span class="math-inline">\\(a\vec{u&#95;1} + b\vec{u&#95;2} + c\vec{u&#95;3} = \vec{0}\\)</span>, meaning that the vectors <span class="math-inline">\\(\vec{u&#95;1}, \vec{u&#95;2}, \vec{u&#95;3}\\)</span> are linearly dependent.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\vec u&#95;1 = \vec v&#95;2 + \vec v&#95;3\\)</span>, <span class="math-inline">\\(\vec u&#95;2 = \vec v&#95;1 + \vec v&#95;3\\)</span>, and <span class="math-inline">\\(\vec u&#95;3 = \vec v&#95;1 + \vec v&#95;2\\)</span>

<details markdown="1"><summary>Solution</summary>

These vectors are **linearly independent**.

Let's start by writing

<div class="math-display">
$$
a\vec{u_1} + b\vec{u_2} + c\vec{u_3} = \vec{0}
$$
</div>

We need to try and find all solutions for <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> in the equation above. Plugging in <span class="math-inline">\\(\vec{u&#95;1}, \vec{u&#95;2}, \vec{u&#95;3}\\)</span> gives us

<div class="math-display">
$$
\begin{align*}
a(\vec{v_2} + \vec{v_3}) + b(\vec{v_1} + \vec{v_3}) + c(\vec{v_1} + \vec{v_2}) &= \vec{0} \\\\
a\vec{v_2} + a\vec{v_3} + b\vec{v_1} + b\vec{v_3} + c\vec{v_1} + c\vec{v_2} &= \vec{0} \\\\ (b + c) \vec v_1 + (a + c) \vec v_2 + (a + b) \vec v_3 &= 0
\end{align*}
$$
</div>

Again, since <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span> are linearly independent, the only solution to this equation is that <span class="math-inline">\\(b + c\\)</span>, <span class="math-inline">\\(a + c\\)</span>, and <span class="math-inline">\\(a + b\\)</span> are all 0.

<div class="math-display">
$$
\begin{align*}
b + c &= 0 \\\\
a + c &= 0 \\\\
a + b &= 0
\end{align*}
$$
</div>

The only solution to the system above is <span class="math-inline">\\(a = b = c = 0\\)</span>, meaning that the only solution to the equation <span class="math-inline">\\(a\vec{u&#95;1} + b\vec{u&#95;2} + c\vec{u&#95;3} = \vec{0}\\)</span> is the trivial solution. Therefore, the vectors <span class="math-inline">\\(\vec{u&#95;1}, \vec{u&#95;2}, \vec{u&#95;3}\\)</span> are linearly independent.

</details>

</div>
</div>

</div>

---

## Problem 7: Intersections of Subspaces (6 pts)

Let:

-   <span class="math-inline">\\(M\\)</span> be the subspace of <span class="math-inline">\\(\mathbb{R}^4\\)</span> spanned by <span class="math-inline">\\(\begin{bmatrix}1 \\\\ 1 \\\\ 1 \\\\ 0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}0 \\\\ -4 \\\\ 1 \\\\ 5\end{bmatrix}\\)</span>.

-   <span class="math-inline">\\(N\\)</span> be the subspace of <span class="math-inline">\\(\mathbb{R}^4\\)</span> spanned by <span class="math-inline">\\(\begin{bmatrix}0 \\\\ -2 \\\\ 1 \\\\ 2\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}1 \\\\ -1 \\\\ 1 \\\\ 3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find a vector that belongs to both <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(N\\)</span>. In other words, find a vector <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(\vec v \in M\\)</span> and <span class="math-inline">\\(\vec v \in N\\)</span>. There are infinitely many answers; state the answer with a first component of 1.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -3 \\\\ 2 \\\\ 5 \end{bmatrix}\\)</span> is a vector in both <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(N\\)</span>; it's the sum of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ -4 \\\\ 1 \\\\ 5 \end{bmatrix}\\)</span>, and it's also the sum of <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ -2 \\\\ 1 \\\\ 2 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \\\\ 1 \\\\ 3 \end{bmatrix}\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find the dimension of the set of all vectors that belong to both <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(N\\)</span>. Explain your reasoning.

<details markdown="1"><summary>Solution</summary>

Any vector in <span class="math-inline">\\(M\\)</span> is of the form

<div class="math-display">
$$
a \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\\\ -4 \\\\ 1 \\\\ 5 \end{bmatrix} = \begin{bmatrix} a \\\\ a - 4b \\\\ a + b \\\\ 5b \end{bmatrix}.
$$
</div>

Any vector in <span class="math-inline">\\(N\\)</span> is of the form

<div class="math-display">
$$
c \begin{bmatrix} 0 \\\\ -2 \\\\ 1 \\\\ 2 \end{bmatrix} + d \begin{bmatrix} 1 \\\\ -1 \\\\ 1 \\\\ 3 \end{bmatrix} = \begin{bmatrix} d \\\\ -2c - d \\\\ c + d \\\\ 2c + 3d \end{bmatrix}.
$$
</div>

For a vector to belong to both <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(N\\)</span>, we need

<div class="math-display">
$$
\begin{align*}
a &= d \\\\
a - 4b &= -2c - d \\\\
a + b &= c + d \\\\
5b &= 2c + 3d.
\end{align*}
$$
</div>

From the first equation, <span class="math-inline">\\(a = d\\)</span>. From the third equation, this means <span class="math-inline">\\(b = c\\)</span>. Plugging these into the second equation gives <span class="math-inline">\\(a - 4b = -2b - a\\)</span>, so <span class="math-inline">\\(a = b\\)</span>. Therefore <span class="math-inline">\\(a = b = c = d\\)</span>, and the fourth equation is automatically satisfied.

So, the set of all vectors in both <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(N\\)</span> is

<div class="math-display">
$$
\left\{t\begin{bmatrix} 1 \\\\ -3 \\\\ 2 \\\\ 5 \end{bmatrix} \mid t \in \mathbb{R}\right\}.
$$
</div>

This is a line through the origin, so its dimension is <span class="math-inline">\\(\boxed{1}\\)</span>.

</details>
</div>
</div>

</div>

{% endraw %}
