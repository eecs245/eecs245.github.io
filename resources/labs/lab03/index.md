---
layout: page
title: "Lab 3: Introduction to Vectors"
description: "Lab 3: Introduction to Vectors activities."
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

# Lab 3: Introduction to Vectors

**due** by the end of your lab section on Wednesday, September 16th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete all activities and show your lab TA by the end of the lab section.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Transformed Data](#activity-1-transformed-data)
- [Activity 2: Triangle Inequality](#activity-2-triangle-inequality)
- [Activity 3: Linear Combinations](#activity-3-linear-combinations)
- [Activity 4: Arrays in NumPy](#activity-4-arrays-in-numpy)
- [Activity 5: The Dot Product](#activity-5-the-dot-product)
- [Activity 6: Angles and Orthogonality](#activity-6-angles-and-orthogonality)

---

In each category, select the option that best describes your (honest) thoughts towards this class so far.

**i. Difficulty**

<span class="mc-bubble" aria-hidden="true"></span> Way harder than I expected

<span class="mc-bubble" aria-hidden="true"></span> Harder than I expected

<span class="mc-bubble" aria-hidden="true"></span> About as hard as I expected

<span class="mc-bubble" aria-hidden="true"></span> Easier than I expected

<span class="mc-bubble" aria-hidden="true"></span> Way easier than I expected

**ii. Interest**

<span class="mc-bubble" aria-hidden="true"></span> Way more interesting than I expected

<span class="mc-bubble" aria-hidden="true"></span> More interesting than I expected

<span class="mc-bubble" aria-hidden="true"></span> About as interesting as I expected

<span class="mc-bubble" aria-hidden="true"></span> Less interesting than I expected

<span class="mc-bubble" aria-hidden="true"></span> Way less interesting than I expected

Any immediate action items we can take to make your experience better?

---

## Activity 1: Transformed Data

Let's begin by reviewing how transforming a dataset affects a fitted simple linear model.

Suppose we're given a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \dots, (x&#95;n, y&#95;n)\\)</span>, where <span class="math-inline">\\(\bar{x}\\)</span> is the mean of <span class="math-inline">\\(x&#95;1, x&#95;2, \dots, x&#95;n\\)</span> and <span class="math-inline">\\(\bar{y}\\)</span> is the mean of <span class="math-inline">\\(y&#95;1, y&#95;2, \dots, y&#95;n\\)</span>.

Using this dataset, we create a *transformed* dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1', y&#95;1'), (x&#95;2', y&#95;2'), \dots, (x&#95;n', y&#95;n')\\)</span>, where:

<div class="math-display">
$$
x_i' = 4x_i - 3 \qquad y_i' = y_i + 24
$$
</div>

So the transformed dataset is of the form

<div class="math-display">
$$
(4x_1-3, y_1+24), (4x_2-3, y_2+24), \dots, (4x_n-3, y_n+24)
$$
</div>

We decide to fit a simple linear model <span class="math-inline">\\(h(x&#95;i') = w&#95;0 + w&#95;1 x&#95;i'\\)</span> on the transformed dataset using squared loss. We find that <span class="math-inline">\\(w&#95;0^{\ast} = 7\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast} = 2\\)</span>, so <span class="math-inline">\\(h^{\ast}(x&#95;i') = 7 + 2x&#95;i'\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose we were to fit a simple linear model through the original dataset, again using squared loss. What would the optimal slope on the original dataset be?

<details markdown="1"><summary>Solution</summary>

8\.

Relative to the dataset with <span class="math-inline">\\(x'\\)</span>, the dataset with <span class="math-inline">\\(x\\)</span> is compressed by a factor of 4, so the slope increases by a factor of 4: <span class="math-inline">\\(2 \cdot 4 = 8\\)</span>.

Concretely, this can be shown by looking at the formula for the new slope:

<div class="math-display">
$$
\begin{align*}
2 &= r\frac{\sigma_{y'}}{\sigma_{x'}} \\\\
2 &= r\frac{\sigma_y}{4\sigma_x} \\\\
8 &= r\frac{\sigma_y}{\sigma_x}
\end{align*}
$$
</div>

so the original slope is <span class="math-inline">\\(8\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Recall, the model <span class="math-inline">\\(h^{\ast}(x&#95;i') = w&#95;0 + w&#95;1 x&#95;i'\\)</span> was fit on the transformed dataset, introduced above. <span class="math-inline">\\(h^{\ast}(x&#95;i')\\)</span> happens to pass through the point <span class="math-inline">\\((\bar{x}, \bar{y})\\)</span>. What is the value of <span class="math-inline">\\(\bar{x}\\)</span>? Give your answer as an integer with no variables. <em>Hint: What else does <span class="math-inline">\\(h^{\ast}(x&#95;i')\\)</span> pass through?</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(h^{\ast}(x&#95;i')\\)</span> is guaranteed to pass through <span class="math-inline">\\((\bar{x}', \bar{y}')\\)</span>, where <span class="math-inline">\\(\bar{x}'\\)</span> is the mean of the <span class="math-inline">\\(x'\\)</span> values and <span class="math-inline">\\(\bar{y}'\\)</span> is the mean of the <span class="math-inline">\\(y'\\)</span> values.

Let's see what that looks like as an equation:

<div class="math-display">
$$
\begin{align*}
w_0^* + w_1^*\bar{x}' &= h^*(\bar{x}') \\\\
7 + 2\bar{x}' &= h^*(\bar{x}') \\\\
7 + 2\bar{x}' &= \bar{y}'
\end{align*}
$$
</div>

Now write <span class="math-inline">\\(\bar{x}'\\)</span> and <span class="math-inline">\\(\bar{y}'\\)</span> in terms of <span class="math-inline">\\(\bar{x}\\)</span> and <span class="math-inline">\\(\bar{y}\\)</span>:

<div class="math-display">
$$
\bar{x}' = 4\bar{x} - 3
\qquad
\bar{y}' = \bar{y} + 24
$$
</div>

Substitute these into the equation above:

<div class="math-display">
$$
7 + 2(4\bar{x} - 3) = \bar{y} + 24
$$
</div>

The problem also tells us that <span class="math-inline">\\(h^{\ast}(x&#95;i')\\)</span> passes through <span class="math-inline">\\((\bar{x}, \bar{y})\\)</span>, so

<div class="math-display">
$$
2\bar{x} + 7 = \bar{y}
$$
</div>

Now subtract:

<div class="math-display">
$$
\begin{align*}
7 + 2(4\bar{x} - 3) - (2\bar{x} + 7) &= \bar{y} + 24 - \bar{y} \\\\
7 + 8\bar{x} - 6 - 2\bar{x} - 7 &= 24 \\\\
6\bar{x} &= 30 \\\\
\bar{x} &= 5
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Recap: Vectors

Now that we've reviewed simple linear regression, let's turn to vectors. The next three activities explore vector lengths, linear combinations, and their implementation in NumPy.

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

([Chapters 3.1](https://notes.eecs245.org/vectors/vectors-and-linear-combinations/) and [3.2](https://notes.eecs245.org/vectors/norms/)) The **norm** of a vector <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span> measures its length:

<div class="math-display">
$$
\lVert \vec v \rVert = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}
$$
</div>

 This is the default norm for vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>, but other norms exist.

</li>
<li markdown="1">

([3.1](https://notes.eecs245.org/vectors/vectors-and-linear-combinations/)) A **linear combination** of the vectors <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2, \dots,\vec v&#95;d\\)</span> is any vector that can be written as

<div class="math-display">
$$
a_1\vec v_1 + a_2\vec v_2+\dots+a_d\vec v_d
$$
</div>

 where <span class="math-inline">\\(a&#95;1, a&#95;2, \dots, a&#95;d\\)</span> are scalars. We can think of this as taking bits of each vector and adding them together. The <span class="math-inline">\\(a&#95;i\\)</span>'s are called the **coefficients** of the linear combination.

</li>
</ul>

---

## Activity 2: Triangle Inequality

We first use norms to compare the length of a sum with the lengths of the original vectors. The triangle inequality states that for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n:\\)</span>

<div class="math-display">
$$
\lVert \vec u + \vec v \rVert \leq \lVert \vec u \rVert + \lVert \vec v \rVert
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
**For the vectors <span class="math-inline">\\(\vec u = \begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span>**, verify that the triangle inequality holds. That is, show that the left-hand side is less than or equal to the right-hand side.

<details markdown="1"><summary>Solution</summary>

First, let's find <span class="math-inline">\\(\lVert \vec u + \vec v \rVert\\)</span>.

<div class="math-display">
$$
\begin{align*}
\lVert \vec u + \vec v \rVert
&= \left\lVert \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} \right\rVert \\\\
&= \left\lVert \begin{bmatrix} 4-1 \\\\ 3-3 \end{bmatrix} \right\rVert \\\\
&= \left\lVert \begin{bmatrix} 3 \\\\ 0 \end{bmatrix} \right\rVert \\\\
&= \sqrt{3^2 + 0^2} \\\\
&= \sqrt{9} \\\\
&= 3
\end{align*}
$$
</div>

Also, <span class="math-inline">\\(\lVert \vec u \rVert = \sqrt{4^2 + 3^2} = 5\\)</span>. What's <span class="math-inline">\\(\lVert \vec v \rVert\\)</span>?

<div class="math-display">
$$
\begin{align*}
\lVert \vec v \rVert
&= \left\lVert \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} \right\rVert \\\\
&= \sqrt{(-1)^2 + (-3)^2} \\\\
&= \sqrt{1 + 9} \\\\
&= \sqrt{10}
\end{align*}
$$
</div>

So, the triangle inequality claims that

<div class="math-display">
$$
\lVert \vec u + \vec v \rVert \leq \lVert \vec u \rVert + \lVert \vec v \rVert
$$
</div>

which, here, is

<div class="math-display">
$$
3 \leq 5 + \sqrt{10}
$$
</div>

This is true, since 5 alone is greater than 3, so <span class="math-inline">\\(5 + \sqrt{10}\\)</span> is surely also greater than (or equal to) 3.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find two **different** vectors <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^2\\)</span> such that the triangle inequality achieves **equality**, i.e. where

<div class="math-display">
$$
\lVert \vec x + \vec y \rVert = \lVert \vec x \rVert + \lVert \vec y \rVert
$$
</div>

What is the relationship between the <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> you found?

<details markdown="1"><summary>Solution</summary>

Example: let <span class="math-inline">\\(\vec x = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec y = \begin{bmatrix} 2 \\\\ 2 \end{bmatrix}\\)</span>. Then,

<div class="math-display">
$$
\left\lVert \vec x + \vec y \right\rVert = \left\lVert \begin{bmatrix} 3 \\\\ 3 \end{bmatrix} \right\rVert = \sqrt{3^2 + 3^2} = 3 \sqrt{2}
$$
</div>



<div class="math-display">
$$
\lVert \vec x \rVert + \lVert \vec y \rVert = \sqrt{1^2 + 1^2} + \sqrt{2^2 + 2^2} = \sqrt{2} + \sqrt{8} = \sqrt{2} + 2 \sqrt{2} = 3 \sqrt{2}
$$
</div>

So, in this case, the triangle inequality achieves equality. What you'll notice is that <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> point in the same direction, i.e. <span class="math-inline">\\(\vec y = 2 \vec x\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 3: Linear Combinations

Next, we'll look at which vectors we can form by scaling and adding other vectors.

Let <span class="math-inline">\\(\vec u = \begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec v = \begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec w = \begin{bmatrix} -6 \\\\ 9 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that <span class="math-inline">\\(a \vec u + b \vec v = \vec w\\)</span>. By finding <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>, you have written <span class="math-inline">\\(\vec w\\)</span> as a **linear combination** of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

<details markdown="1"><summary>Solution</summary>

We can pose this problem as solving a system of equations. By scalar multiplication, we have:

<div class="math-display">
$$
\begin{align*}
a \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} &= \begin{bmatrix} -6 \\\\ 9 \end{bmatrix} \\\\
\begin{bmatrix} 4a \\\\ 3a \end{bmatrix} + \begin{bmatrix} -b \\\\ -3b \end{bmatrix} &= \begin{bmatrix} -6 \\\\ 9 \end{bmatrix} \\\\
\begin{bmatrix} 4a - b \\\\ 3a - 3b \end{bmatrix} &= \begin{bmatrix} -6 \\\\ 9 \end{bmatrix}
\end{align*}
$$
</div>

The vector equation on the last line is equivalent to the system of equations:

<div class="math-display">
$$
\begin{cases}
  4a - b &= -6 \\\\
  3a - 3b &= 9
\end{cases}
$$
</div>

So, we just need to solve this system of equations to find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>.

To do so, we can multiply the first equation by 3 to get:

<div class="math-display">
$$
\begin{cases}
  12a - 3b &= -18 \\\\
  3a - 3b &= 9
\end{cases}
$$
</div>

Then, we can subtract the second equation from the first to get:

<div class="math-display">
$$
9a = -27 \implies a = -3
$$
</div>

Substituting <span class="math-inline">\\(a = -3\\)</span> back into the second equation, we get:

<div class="math-display">
$$
3(-3) - 3b = 9 \implies -9 - 3b = 9 \implies -3b = 18 \implies b = -6
$$
</div>

So, we have <span class="math-inline">\\(\boxed{a = -3}\\)</span> and <span class="math-inline">\\(\boxed{b = -6}\\)</span>.

To verify that this solution works, we can substitute <span class="math-inline">\\(a = -3\\)</span> and <span class="math-inline">\\(b = -6\\)</span> back into the original equation:

<div class="math-display">
$$
(-3)\begin{bmatrix}4\\\\3\end{bmatrix} + (-6)\begin{bmatrix}-1\\\\-3\end{bmatrix}
= \begin{bmatrix}-12\\\\-9\end{bmatrix} + \begin{bmatrix}6\\\\18\end{bmatrix}
= \begin{bmatrix}-6\\\\9\end{bmatrix}=\vec w
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now, try and write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span>. In other words, try and find values of <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that

<div class="math-display">
$$
a \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} + c \begin{bmatrix} 2 \\\\ 1 \end{bmatrix} = \vec w
$$
</div>

What happens? Why?

<details markdown="1"><summary>Solution</summary>

We can start by trying to solve the corresponding system of equations:

<div class="math-display">
$$
\begin{cases}
4a - b + 2c = -6\\\\
3a - 3b + c = 9
\end{cases}
$$
</div>

There are 2 equations and 3 unknowns, **which means thare are infinitely many solutions for <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span>**.

What's the linear algebra reason for this?

<ul class="assignment-list" markdown="1" data-item-count="4">
<li markdown="1">

With just <span class="math-inline">\\(\begin{bmatrix}4\\\\3\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-1\\\\-3\end{bmatrix}\\)</span>, you can already create any other vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>. That is, any vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span> can be written as a linear combination of <span class="math-inline">\\(\begin{bmatrix}4\\\\3\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-1\\\\-3\end{bmatrix}\\)</span>.

</li>
<li markdown="1">

That is, for **any** vector <span class="math-inline">\\(\vec w \in \mathbb{R}^2\\)</span> (not just the one in this question), there exist **unique values** of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that

<div class="math-display">
$$
a \begin{bmatrix}4\\\\3\end{bmatrix} + b \begin{bmatrix}-1\\\\-3\end{bmatrix} = \vec w
$$
</div>

</li>
<li markdown="1">

Since <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span> already can create any other vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>, adding <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> to the linear combination doesn't "unlock" any new vectors --- we can still create any other vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

</li>
<li markdown="1">

But, because <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> already can be created using <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span>, adding it to the linear combination makes it so that there are infinitely many solutions for <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> in

<div class="math-display">
$$
a \begin{bmatrix}4\\\\3\end{bmatrix} + b \begin{bmatrix}-1\\\\-3\end{bmatrix} + c \begin{bmatrix}2\\\\1\end{bmatrix} = \vec w
$$
</div>

</li>
</ul>

If there are infinitely many solutions, how do we find them? Let's treat <span class="math-inline">\\(c\\)</span> as a free variable, and solve for <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> in terms of <span class="math-inline">\\(c\\)</span>.

<div class="math-display">
$$
\begin{cases}
4a - b + 2c = -6\\\\
3a - 3b + c = 9
\end{cases}
$$
</div>

Multiplying the first equation by 3 gives us:

<div class="math-display">
$$
\begin{cases}
12a - 3b + 6c = -18\\\\
3a - 3b + c = 9
\end{cases}
$$
</div>

Subtracting the second equation from the (new) first gives us:

<div class="math-display">
$$
9a + 5c = -27 \implies a = -3 - \frac{5}{9}c
$$
</div>

Similarly, multiplying the first equation by 3 and the second equation by 4 gives us:

<div class="math-display">
$$
\begin{cases}
12a - 3b + 6c = -18\\\\
12a - 12b + 4c = 36
\end{cases}
$$
</div>

Subtracting the (new) second equation from the (new) first gives us:

<div class="math-display">
$$
9b + 2c = -54 \implies b = -6 - \frac{2}{9}c
$$
</div>

So, the values of <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> that satisfy

<div class="math-display">
$$
a \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} + c \begin{bmatrix} 2 \\\\ 1 \end{bmatrix} = \begin{bmatrix} -6 \\\\ 9 \end{bmatrix}
$$
</div>

are

<div class="math-display">
$$
\boxed{a = -3 - \frac{5}{9}c, \qquad b = -6 - \frac{2}{9}c, \qquad c = c, c \in \mathbb{R}}
$$
</div>

<span class="math-inline">\\(c\\)</span> can be anything, which is why there are infinitely many solutions. If we let <span class="math-inline">\\(c = 0\\)</span>, then we get back <span class="math-inline">\\(a = -3\\)</span> and <span class="math-inline">\\(b = -6\\)</span> from part **a)**. But, say, if we let <span class="math-inline">\\(c = -9\\)</span>, then we get <span class="math-inline">\\(a = 2\\)</span> and <span class="math-inline">\\(b = -4\\)</span>, which also works:

<div class="math-display">
$$
2 \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} - 4 \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} + (-9) \begin{bmatrix} 2 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 8 \\\\ 6 \end{bmatrix} - \begin{bmatrix} -4 \\\\ -12 \end{bmatrix} + \begin{bmatrix} -18 \\\\ -9 \end{bmatrix} = \begin{bmatrix} -6 \\\\ 9 \end{bmatrix} = \vec w
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Now, try and write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -4 \\\\ -2 \end{bmatrix}\\)</span>. What happens? Why?

<details markdown="1"><summary>Solution</summary>

Note <span class="math-inline">\\(\begin{bmatrix}-4\\\\-2\end{bmatrix}=-2\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, which means these vectors point in the same direction, or lie on the same line. (The formal term is that these vectors are **collinear**.)

Since <span class="math-inline">\\(\vec w=\begin{bmatrix}-6\\\\9\end{bmatrix}\\)</span> is not a scalar multiple of <span class="math-inline">\\(\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span> (ratios <span class="math-inline">\\(-6/2=-3\\)</span> vs. <span class="math-inline">\\(9/1=9\\)</span> disagree), **no solution exists**!

To conclude, because the two vectors <span class="math-inline">\\(\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-4\\\\-2\end{bmatrix}\\)</span> are collinear, it is impossible to write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of them. The only possible linear combinations are of the form <span class="math-inline">\\(c \begin{bmatrix}2\\\\1\end{bmatrix}\\)</span> for some <span class="math-inline">\\(c \in \mathbb{R}\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 4: Arrays in NumPy

Now, put vector operations into practice using NumPy arrays. Instead of writing code in a separate Jupyter Notebook for this lab, you will interact with the code cells that exist in the course notes.

In particular, go to [Chapter 3.2](https://notes.eecs245.org/vectors/norms/) of the course notes, scroll all the way to the bottom, and complete **Activity 5** there. To get checked off, show your lab TA that you've completed the activity --- there's no need to submit your code anywhere.

**Introduction: The Dot Product**

So far, we've measured vector lengths and formed linear combinations. The dot product gives us a way to compare the directions of two vectors. We will study this in tomorrow's lecture; use the definitions below to explore it in the next two activities.

<ul class="assignment-list" markdown="1" data-item-count="3">
<li markdown="1">

([3.3](https://notes.eecs245.org/vectors/dot-product/)) The **dot product** of two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> is defined as:

<div class="math-display">
$$
\vec u \cdot \vec v = \begin{bmatrix}u_1 \\\\ u_2 \\\\ \dots \\\\ u_n\end{bmatrix} \cdot \begin{bmatrix}v_1 \\\\ v_2 \\\\ \dots \\\\ v_n\end{bmatrix} = u_1v_1 + u_2v_2 + \dots + u_nv_n
$$
</div>

 The result is a **scalar**, not another vector.

</li>
<li markdown="1">

([3.3](https://notes.eecs245.org/vectors/dot-product/)) The dot product also has a geometric definition, involving the norms (lengths) of two nonzero vectors and the angle between them:

<div class="math-display">
$$
\vec u \cdot \vec v = ||\vec u|| ||\vec v|| \text{cos}\theta
$$
</div>

</li>
<li markdown="1">

([3.3](https://notes.eecs245.org/vectors/dot-product/)) The key takeaway from the dot product is that it tells us how similar the directions of two vectors are. When two vectors have a dot product of 0, they are **orthogonal**. For two nonzero vectors, this means that the angle between them is <span class="math-inline">\\(90^\circ\\)</span>.

</li>
</ul>

---

## Activity 5: The Dot Product

For each pair of vectors below, (1) draw them on the grid to the right and (2) compute their dot product using the component-wise definition.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot 1 + 6\cdot 0 = 8.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} -2 \\\\ 0 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot (-2) + 6\cdot 0 = -16.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 6 \\\\ 8 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot 6 + 6\cdot 8 = 48 + 48 = 96.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 8 \\\\ 6 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot 8 + 6\cdot 6 = 64 + 36 = 100.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} -3 \\\\ 4 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot (-3) + 6\cdot 4 = -24 + 24 = 0.
$$
</div>

Since the dot product is <span class="math-inline">\\(0\\)</span>, the vectors are **orthogonal**.
</details>

<img src="imgs/activity-2-blank-grid.png" alt="image" style="width: 100%; max-width: 100%;">

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="imgs/activity-3-solutions.png" alt="image" style="width: 80%; max-width: 100%;">
</div>
</details>

</div>
</div>

</div>

---

## Activity 6: Angles and Orthogonality

In the previous activity, we computed dot products using vector components. Now, we will connect those calculations to angles using the geometric definition of the dot product.

<div class="math-display">
$$
\vec u \cdot \vec v = \begin{bmatrix}u_1 \\\\ u_2 \\\\ \dots \\\\ u_n\end{bmatrix} \cdot \begin{bmatrix}v_1 \\\\ v_2 \\\\ \dots \\\\ v_n\end{bmatrix} = u_1v_1 + u_2v_2 + \dots + u_nv_n
$$
</div>



<div class="math-display">
$$
\vec u \cdot \vec v = ||\vec u|| ||\vec v|| \text{cos}\theta
$$
</div>

 Let <span class="math-inline">\\(\vec w=\begin{bmatrix}5\\\\0\\\\-4\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec x=\begin{bmatrix}9\\\\1\\\\2\\\\3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec w \cdot \vec x\\)</span>, <span class="math-inline">\\(\lVert \vec w \rVert\\)</span>, and <span class="math-inline">\\(\lVert \vec x \rVert\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\vec w \cdot \vec x = 5\cdot 9 + 0\cdot 1 + (-4)\cdot 2 + 1\cdot 3 = 45 + 0 - 8 + 3 = \boxed{40}.
$$
</div>



<div class="math-display">
$$
\lVert \vec w \rVert = \sqrt{5^2 + 0^2 + (-4)^2 + 1^2} = \sqrt{25 + 0 + 16 + 1} = \boxed{\sqrt{42}}.
$$
</div>



<div class="math-display">
$$
\lVert \vec x \rVert = \sqrt{9^2 + 1^2 + 2^2 + 3^2} = \sqrt{81 + 1 + 4 + 9} = \boxed{\sqrt{95}}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Using the results of part **a)**, find the angle between <span class="math-inline">\\(\vec w\\)</span> and <span class="math-inline">\\(\vec x\\)</span>. Leave your answer in the form <span class="math-inline">\\(\cos^{-1}(\cdot)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Using <span class="math-inline">\\(\vec w \cdot \vec x=\|\vec w\|\|\vec x\|\cos\theta\\)</span>,

<div class="math-display">
$$
\cos \theta = \frac{\vec w \cdot \vec x}{\|\vec w\|\,\|\vec x\|}
= \frac{40}{\sqrt{42}\,\sqrt{95}}.
$$
</div>

 Therefore

<div class="math-display">
$$
\boxed{\;\theta = \cos^{-1}\!\left(\frac{40}{\sqrt{42\cdot 95}}\right)\;}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
What is <span class="math-inline">\\(\cos(90^\circ)\\)</span>? What does this have to do with orthogonality?

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\cos(90^\circ)=0.
$$
</div>

 If the angle <span class="math-inline">\\(\theta\\)</span> between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(90^\circ\\)</span>, then

<div class="math-display">
$$
\vec u\cdot\vec v=\|\vec u\|\,\|\vec v\|\cos\theta=\|\vec u\|\,\|\vec v\| \cdot 0 = 0,
$$
</div>

 so the vectors are **orthogonal**. Conversely, if <span class="math-inline">\\(\vec u\cdot\vec v=0\\)</span> (and neither vector is the zero vector), then <span class="math-inline">\\(\cos\theta=0\\)</span> and <span class="math-inline">\\(\theta=90^\circ\\)</span>.
</details>
</div>
</div>

</div>

{% endraw %}
