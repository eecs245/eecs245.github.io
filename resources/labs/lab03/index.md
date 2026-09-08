---
layout: page
title: "Lab 3: Vectors and the Dot Product"
description: "Lab 3: Vectors and the Dot Product activities."
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

# Lab 3: Vectors and the Dot Product

**due** by the end of your lab section on Wednesday, September 16th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete all activities and show your lab TA by the end of the lab section.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Linear Combinations](#activity-1-linear-combinations)
- [Activity 2: The Dot Product](#activity-2-the-dot-product)
- [Activity 3: Angles and Orthogonality](#activity-3-angles-and-orthogonality)
- [Activity 4: Sum--Difference Orthogonality](#activity-4-sum--difference-orthogonality)
- [Activity 5: Triangle Inequality](#activity-5-triangle-inequality)
- [Activity 6: Arrays in NumPy](#activity-6-arrays-in-numpy)
- [Activity 7: Transformed Data](#activity-7-transformed-data)

---

## Recap: Vectors and the Dot Product

-   ([Chapters 3.1](https://notes.eecs245.org/vectors/vectors-and-linear-combinations/) and [3.2](https://notes.eecs245.org/vectors/norms/)) The **norm** of a vector <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span> measures its length:

<div class="math-display">
$$
\lVert \vec v \rVert = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}
$$
</div>

 This is the default norm for vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>, but other norms exist.

-   ([3.1](https://notes.eecs245.org/vectors/vectors-and-linear-combinations/)) A **linear combination** of the vectors <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2, \dots,\vec v&#95;d\\)</span> is any vector that can be written as

<div class="math-display">
$$
a_1\vec v_1 + a_2\vec v_2+\dots+a_d\vec v_d
$$
</div>

 where <span class="math-inline">\\(a&#95;1, a&#95;2, \dots, a&#95;d\\)</span> are scalars. We can think of this as taking bits of each vector and adding them together. The <span class="math-inline">\\(a&#95;i\\)</span>'s are called the **coefficients** of the linear combination.

-   ([3.3](https://notes.eecs245.org/vectors/dot-product/)) The **dot product** of two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> is defined as:

<div class="math-display">
$$
\vec u \cdot \vec v = \begin{bmatrix}u_1 \\\\ u_2 \\\\ \dots \\\\ u_n\end{bmatrix} \cdot \begin{bmatrix}v_1 \\\\ v_2 \\\\ \dots \\\\ v_n\end{bmatrix} = u_1v_1 + u_2v_2 + \dots + u_nv_n
$$
</div>

 The result is a **scalar**, not another vector.

-   ([3.3](https://notes.eecs245.org/vectors/dot-product/)) The dot product also has a geometric definition, involving the norms (lengths) of the vectors and the angle between them:

<div class="math-display">
$$
\vec u \cdot \vec v = ||\vec u|| ||\vec v|| \text{cos}\theta
$$
</div>

-   ([3.3](https://notes.eecs245.org/vectors/dot-product/)) The key takeaway from the dot product is that it tells us how similar the directions of two vectors are. When two vectors have a dot product of 0, they are **orthogonal**, or have a 90 degree angle between them.

---

## Activity 1: Linear Combinations

Let <span class="math-inline">\\(\vec u = \begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec v = \begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec w = \begin{bmatrix} -6 \\\\ 9 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that <span class="math-inline">\\(a \vec u + b \vec v = \vec w\\)</span>. By finding <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>, you have written <span class="math-inline">\\(\vec w\\)</span> as a **linear combination** of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Now, try and write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -4 \\\\ -2 \end{bmatrix}\\)</span>. What happens? Why?

</div>
</div>

</div>

---

## Activity 2: The Dot Product

For each pair of vectors below (1) draw them on the grid at the bottom of the page and (2) compute their dot product.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} -5 \\\\ 0 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 6 \\\\ 8 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 8 \\\\ 6 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} -3 \\\\ 4 \end{bmatrix}\\)</span>

<img src="imgs/activity-2-blank-grid.png" alt="image" style="width: 100%; max-width: 100%;">

</div>
</div>

</div>

---

## Activity 3: Angles and Orthogonality

In this activity, we will investigate the relationship between the two definitions of the dot product and learn how to use this equivalence to measure the similarity between two vectors.

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Using the results of part **a)**, find the angle between <span class="math-inline">\\(\vec w\\)</span> and <span class="math-inline">\\(\vec x\\)</span>. Leave your answer in the form <span class="math-inline">\\(\cos^{-1}(\cdot)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
What is <span class="math-inline">\\(\cos(90^\circ)\\)</span>? What does this have to do with orthogonality?

</div>
</div>

</div>

---

## Activity 4: Sum--Difference Orthogonality

Let <span class="math-inline">\\(\vec u=\begin{bmatrix}2\\\\-1\\\\0\\\\5\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\2\\\\4\\\\-3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Show that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now suppose <span class="math-inline">\\(\vec u,\vec v\in\mathbb{R}^n\\)</span> are arbitrary vectors with the same number of components. Is it always true that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal?

-   If so, prove why.

-   If not, specify conditions under which it's guaranteed that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal.

<em>Hint: Use the distributive property of the dot product, which states that </em>

<div class="math-display">
$$
(\vec a + \vec b) \cdot (\vec c + \vec d) = \vec a \cdot \vec c + \vec a \cdot \vec d + \vec b \cdot \vec c + \vec b \cdot \vec d
$$
</div>

</div>
</div>

</div>

---

## Activity 5: Triangle Inequality

The triangle inequality states that for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n:\\)</span>

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find two **different** vectors in <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^2\\)</span> such that the triangle inequality achieves **equality**, i.e. where

<div class="math-display">
$$
\lVert \vec x + \vec y \rVert = \lVert \vec x \rVert + \lVert \vec y \rVert
$$
</div>

What is the relationship between the <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> you found?

</div>
</div>

</div>

---

## Activity 6: Arrays in NumPy

Instead of writing code in a separate Jupyter Notebook for this lab, you will interact with the code cells that exist in the course notes.

In particular, go to [Chapter 3.2](https://notes.eecs245.org/vectors/norms/) of the course notes, scroll all the way to the bottom, and complete **Activity 5** there. To get checked off, show your lab TA that you've completed the activity --- there's no need to submit your code anywhere.

---

## Activity 7: Transformed Data

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
Suppose we were to fit a simple linear model through the original dataset, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \dots, (x&#95;n, y&#95;n)\\)</span>, again using squared loss. What would the optimal slope on the original dataset be?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Recall, the model <span class="math-inline">\\(h^{\ast}(x&#95;i') = w&#95;0 + w&#95;1 x&#95;i'\\)</span> was fit on the transformed dataset, <span class="math-inline">\\((x&#95;1', y&#95;1'), (x&#95;2', y&#95;2'), \dots, (x&#95;n', y&#95;n')\\)</span>. <span class="math-inline">\\(h^{\ast}(x&#95;i')\\)</span> happens to pass through the point <span class="math-inline">\\((\bar{x}, \bar{y})\\)</span>. What is the value of <span class="math-inline">\\(\bar{x}\\)</span>? Give your answer as an integer with no variables. <em>Hint: What else does <span class="math-inline">\\(h^{\ast}(x&#95;i')\\)</span> pass through?</em>
</div>
</div>

</div>

{% endraw %}
