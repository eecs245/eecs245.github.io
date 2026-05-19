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

# Homework 3: Vectors and the Dot Product

**due** Sunday, May 17th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw03/hw03.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw03/hw03-solutions.pdf" target="_blank">Solutions PDF ✅</a>
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

<details markdown="1"><summary>Solution</summary>

</details>

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

<details markdown="1"><summary>Solution</summary>

1.  <span class="math-inline">\\(\lVert \vec{u} \rVert = \sqrt{3^2 + (-6)^2 + 0^2 + 2^2} = \sqrt{9 + 36 + 0 + 4} = \sqrt{49} = 7\\)</span>

2.  <span class="math-inline">\\(\lVert \vec{v} \rVert = \sqrt{2^2 + 1^2 + 4^2 + (-2)^2} = \sqrt{4 + 1 + 16 + 4} = \sqrt{25} = 5\\)</span>

3.  $$
\begin{align*}
    \lVert \vec{u} + \vec{v} \rVert &= \sqrt{(3+2)^2 + (-6+1)^2 + (0+4)^2 + (2-2)^2} \\\\
    &= \sqrt{25 + 25 + 16 + 0} \\\\ &= \sqrt{66}
    \end{align*}
$$

4.  $$
\begin{align*}
    \lVert \vec{u} - \vec{v} \rVert &= \sqrt{(3-2)^2 + (-6-1)^2 + (0-4)^2 + (2 - (-2))^2} \\\\
    &= \sqrt{1 + 49 + 16 + 16} \\\\ &= \sqrt{82}
    \end{align*}
$$

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Using the same vectors as in part **a)**, compute the angle between <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span>. Leave your answer in terms of <span class="math-inline">\\(\cos^{-1}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\vec{u} \cdot \vec{v} = \lVert \vec{u} \rVert \lVert \vec{v} \rVert \cos \theta\\)</span>, we have:

<div class="math-display">
$$
\begin{align*}
\vec u \cdot \vec v &= 3\cdot 2 + (-6)\cdot 1 + 0\cdot 4 + 2\cdot (-2) = 6 - 6 + 0 - 4 = -4,\\\\
\|\vec u\| &= \sqrt{3^2 + (-6)^2 + 0^2 + 2^2} = \sqrt{49} = 7,\\\\
\|\vec v\| &= \sqrt{2^2 + 1^2 + 4^2 + (-2)^2} = \sqrt{25} = 5,\\\\
\cos\theta &= \frac{\vec u \cdot \vec v}{\|\vec u\|\;\|\vec v\|} = \frac{-4}{7\cdot 5} = -\frac{4}{35}.\\\\
\theta &= \cos^{-1}\!\left(-\dfrac{4}{35}\right)
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\|\vec u\|^2 = \vec u \cdot \vec u\\)</span>, we can expand both <span class="math-inline">\\(\|\vec u+\vec v\|^2\\)</span> and <span class="math-inline">\\(\|\vec u-\vec v\|^2\\)</span> using the distributive property of the dot product, as mentioned in the hint. Below, we color <span class="math-inline">\\(\textcolor{orange}{\vec u\cdot\vec u}\\)</span> in <span style="color: orange">orange</span>, <span class="math-inline">\\(\textcolor{blue}{\vec v\cdot\vec v}\\)</span> in <span style="color: #3D81F6">blue</span>, and <span class="math-inline">\\(\textcolor{magenta}{\vec u\cdot\vec v}\\)</span> in <span style="color: #D81B60">magenta</span>.

<div class="math-display">
$$
\begin{align*}
\|\vec u+\vec v\|^2
&= (\vec u+\vec v)\cdot(\vec u+\vec v) \\\\
&= \textcolor{orange}{\vec u\cdot\vec u}
+ \textcolor{magenta}{\vec u\cdot\vec v}
+ \textcolor{magenta}{\vec v\cdot\vec u}
+ \textcolor{blue}{\vec v\cdot\vec v} \\\\
&= \textcolor{orange}{\vec u\cdot\vec u}
+ \textcolor{blue}{\vec v\cdot\vec v}
+ \textcolor{magenta}{2\,\vec u\cdot\vec v}.
\end{align*}
$$
</div>

<div class="math-display">
$$
\begin{align*}
\|\vec u-\vec v\|^2
&= (\vec u-\vec v)\cdot(\vec u-\vec v) \\\\
&= \textcolor{orange}{\vec u\cdot\vec u}
- \textcolor{magenta}{\vec u\cdot\vec v}
- \textcolor{magenta}{\vec v\cdot\vec u}
+ \textcolor{blue}{\vec v\cdot\vec v} \\\\
&= \textcolor{orange}{\vec u\cdot\vec u}
+ \textcolor{blue}{\vec v\cdot\vec v}
- \textcolor{magenta}{2\,\vec u\cdot\vec v}.
\end{align*}
$$
</div>

Note that the <span class="math-inline">\\(\textcolor{magenta}{+2\vec u\cdot\vec v}\\)</span> from the first expansion and the <span class="math-inline">\\(\textcolor{magenta}{-2\vec u\cdot\vec v}\\)</span> from the second cancel when we add them. Thus,

<div class="math-display">
$$
\begin{align*}
\|\vec u+\vec v\|^2 + \|\vec u-\vec v\|^2
&= \left(\textcolor{orange}{\vec u\cdot\vec u} + \textcolor{blue}{\vec v\cdot\vec v} + \textcolor{magenta}{2\,\vec u\cdot\vec v}\right) \\\\
&\quad + \left(\textcolor{orange}{\vec u\cdot\vec u} + \textcolor{blue}{\vec v\cdot\vec v} - \textcolor{magenta}{2\,\vec u\cdot\vec v}\right) \\\\
&= 2\,\textcolor{orange}{\vec u\cdot\vec u} + 2\,\textcolor{blue}{\vec v\cdot\vec v} \\\\
&= 2\|\vec u\|^2 + 2\|\vec v\|^2.
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec u\\)</span> be the vector along <span class="math-inline">\\(\overrightarrow{AB}\\)</span> (purple arrow in the figure) and <span class="math-inline">\\(\vec v\\)</span> be the vector along <span class="math-inline">\\(\overrightarrow{BC}\\)</span> (green arrow).

![image](imgs/parallelogram_sol_1d.png)

Opposite sides of a parallelogram are equal and parallel, so the remaining sides point as

<div class="math-display">
$$
\overrightarrow{CD}=-\,{\color{Violet}\vec u},\qquad
\overrightarrow{DA}=-\,{\color{ForestGreen}\vec v}.
$$
</div>

Next, read each diagonal as a head--to--tail sum of side vectors.

<div class="math-display">
$$
\overrightarrow{AC}=\overrightarrow{AB}+\overrightarrow{BC}
= {\color{Violet}\vec u}+{\color{ForestGreen}\vec v},\qquad
\overrightarrow{BD}=\overrightarrow{BC}+\overrightarrow{CD}
= {\color{ForestGreen}\vec v}-{\color{Violet}\vec u}.
$$
</div>

Now translate side lengths into norms of the corresponding vectors.

<div class="math-display">
$$
\begin{align*}
(AB) &= \|{\color{Violet}\vec u}\|, &
(BC) &= \|{\color{ForestGreen}\vec v}\|, &
(CD) &= \|{-\,{\color{Violet}\vec u}}\|=\|{\color{Violet}\vec u}\|, &
(DA) &= \|{-\,{\color{ForestGreen}\vec v}}\|=\|{\color{ForestGreen}\vec v}\|.
\end{align*}
$$
</div>

Squaring and summing the four sides gives

<div class="math-display">
$$
\begin{align*}
\big(\textcolor{blue}{AB}\big)^2+\big(\textcolor{blue}{BC}\big)^2
+\big(\textcolor{blue}{CD}\big)^2+\big(\textcolor{blue}{DA}\big)^2
&= \|{\color{Violet}\vec u}\|^2+\|{\color{ForestGreen}\vec v}\|^2
+\|{\color{Violet}\vec u}\|^2+\|{\color{ForestGreen}\vec v}\|^2 \\\\
&= 2\|{\color{Violet}\vec u}\|^2 + 2\|{\color{ForestGreen}\vec v}\|^2.
\end{align*}
$$
</div>

Do the same for the diagonals, using the vector expressions above.

<div class="math-display">
$$
\begin{align*}
(AC) &= \|\,{\color{Violet}\vec u}+{\color{ForestGreen}\vec v}\,\|, &
(BD) &= \|\,{\color{ForestGreen}\vec v}-{\color{Violet}\vec u}\,\|.
\end{align*}
$$
</div>

Squaring and adding the diagonals yields

<div class="math-display">
$$
\begin{align*}
\big(\textcolor{orange}{AC}\big)^2+\big(\textcolor{orange}{BD}\big)^2
&= \|\,{\color{Violet}\vec u}+{\color{ForestGreen}\vec v}\,\|^2
+ \|\,{\color{Violet}\vec u}-{\color{ForestGreen}\vec v}\,\|^2.
\end{align*}
$$
</div>

By the parallelogram law proven in part **(c)**,

<div class="math-display">
$$
\|\,{\color{Violet}\vec u}+{\color{ForestGreen}\vec v}\,\|^2
+\|\,{\color{Violet}\vec u}-{\color{ForestGreen}\vec v}\,\|^2
= 2\|{\color{Violet}\vec u}\|^2 + 2\|{\color{ForestGreen}\vec v}\|^2.
$$
</div>

Combining with the side-length sum computed above,

<div class="math-display">
$$
\boxed{\;
\big(\textcolor{blue}{AB}\big)^2+\big(\textcolor{blue}{BC}\big)^2
+\big(\textcolor{blue}{CD}\big)^2+\big(\textcolor{blue}{DA}\big)^2
\;=\;
\big(\textcolor{orange}{AC}\big)^2+\big(\textcolor{orange}{BD}\big)^2
\;}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(a=-3, b=0, c=2\\)</span>

We can express the equation above as a system of three equations in the three unknowns <span class="math-inline">\\(a,b,c\\)</span>.

<div class="math-display">
$$
\begin{align*}
a\vec v_1 + b\vec v_2 + c\vec v_3 &= \vec x \\\\
a\begin{bmatrix}2\\\\3\\\\0\end{bmatrix}
+ b\begin{bmatrix}-1\\\\2\\\\-1\end{bmatrix}
+ c\begin{bmatrix}0\\\\5\\\\2\end{bmatrix}
&= \begin{bmatrix}-6\\\\1\\\\4\end{bmatrix}
\end{align*}
$$
</div>

Equating components gives the system

<div class="math-display">
$$
\begin{align*}
2a - b &= -6 \tag{1}\\\\
3a + 2b + 5c &= 1 \tag{2}\\\\
-b + 2c &= 4 \tag{3}
\end{align*}
$$
</div>

In <span class="math-inline">\\((1)\\)</span>, isolate <span class="math-inline">\\(b\\)</span>:

<div class="math-display">
$$
\begin{align*}
b &= 6 + 2a \tag{4}
\end{align*}
$$
</div>

Substitute this expression for <span class="math-inline">\\(b\\)</span> into <span class="math-inline">\\((3)\\)</span>:

<div class="math-display">
$$
\begin{align*}
-(6+2a) + 2c &= 4 \\\\
2c &= 10 + 2a \\\\
c &= 5 + a \tag{5}
\end{align*}
$$
</div>

Now substitute <span class="math-inline">\\((4)\\)</span> and <span class="math-inline">\\((5)\\)</span> into <span class="math-inline">\\((2)\\)</span>:

<div class="math-display">
$$
\begin{align*}
3a + 2(6+2a) + 5(5+a) &= 1 \\\\
3a + 12 + 4a + 25 + 5a &= 1 \\\\
12a + 37 &= 1 \\\\
12a &= -36 \\\\
a &= -3 \tag{6}
\end{align*}
$$
</div>

Back-substitute to get <span class="math-inline">\\(b\\)</span> and <span class="math-inline">\\(c\\)</span>:

<div class="math-display">
$$
\begin{align*}
b &= 6 + 2(-3) = 0 \\\\
c &= 5 + (-3) = 2
\end{align*}
$$
</div>

**So:** to verify that these values are correct, compute the linear combination:

<div class="math-display">
$$
\begin{align*}
a\vec v_1 + b\vec v_2 + c\vec v_3
&= (-3)\begin{bmatrix}2\\\\3\\\\0\end{bmatrix}
+ 0\begin{bmatrix}-1\\\\2\\\\-1\end{bmatrix}
+ 2\begin{bmatrix}0\\\\5\\\\2\end{bmatrix} \\\\
&= \begin{bmatrix}-6\\\\-9\\\\0\end{bmatrix}
+ \begin{bmatrix}0\\\\0\\\\0\end{bmatrix}
+ \begin{bmatrix}0\\\\10\\\\4\end{bmatrix} \\\\
&= \begin{bmatrix}-6\\\\1\\\\4\end{bmatrix}
= \vec x
\end{align*}
$$
</div>

<div class="math-display">
$$
\boxed{\,a=-3,\; b=0,\; c=2\,}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(d=-3, e=2\\)</span>

This is a system of three equations and two unknowns, since there are only two vectors in the linear combination. We'll start by solving it the same way we did in part **(a)**.

<div class="math-display">
$$
\begin{align*}
d\vec v_1 + e\vec v_3
&= \vec x \\\\
d\begin{bmatrix}2\\\\3\\\\0\end{bmatrix}
+ e\begin{bmatrix}0\\\\5\\\\2\end{bmatrix}
&= \begin{bmatrix}-6\\\\1\\\\4\end{bmatrix}
\end{align*}
$$
</div>

Equating components gives

<div class="math-display">
$$
\begin{align*}
2d &= -6 \tag{1}\\\\
3d + 5e &= 1 \tag{2}\\\\
2e &= 4 \tag{3}
\end{align*}
$$
</div>

We can solve directly from <span class="math-inline">\\((1)\\)</span> and <span class="math-inline">\\((3)\\)</span>:

<div class="math-display">
$$
\begin{align*}
d &= -3 \tag{4}\\\\
e &= 2 \tag{5}
\end{align*}
$$
</div>

Now check equation <span class="math-inline">\\((2)\\)</span> with these values:

<div class="math-display">
$$
\begin{align*}
3(-3) + 5(2) &= -9 + 10 = 1
\end{align*}
$$
</div>

so <span class="math-inline">\\((2)\\)</span> holds as well. Notice we did not need <span class="math-inline">\\((2)\\)</span> to *find* <span class="math-inline">\\(d\\)</span> and <span class="math-inline">\\(e\\)</span>; it served as a consistency check, which it passes, so a solution exists.

You could also have seen this without re-solving: in part **(a)**, the coefficient on <span class="math-inline">\\(\vec v&#95;2\\)</span> was <span class="math-inline">\\(b=0\\)</span>. Since <span class="math-inline">\\(\vec v&#95;2\\)</span> does not appear in the combination here, the same coefficients on <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;3\\)</span> work, namely <span class="math-inline">\\(d=a=-3\\)</span> and <span class="math-inline">\\(e=c=2\\)</span>.

<div class="math-display">
$$
\boxed{\,d=-3,\; e=2\,}
$$
</div>

Geometrically, <span class="math-inline">\\(\vec x\\)</span> lies in the plane spanned by <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;3\\)</span> (the set <span class="math-inline">\\(\mathrm{span}\lbrace\vec v&#95;1,\vec v&#95;3\rbrace\\)</span>), so we did not need <span class="math-inline">\\(\vec v&#95;2\\)</span> to reach <span class="math-inline">\\(\vec x\\)</span>. (See next page)

![image](imgs/solving_systems_2b_sol.png)

**Visual note**: In the view above, the arrows for <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;3\\)</span>, and <span class="math-inline">\\(\vec x\\)</span> look almost colinear only because of the camera angle. What matters is that they are *coplanar*: <span class="math-inline">\\(\vec x \in \mathrm{span}\lbrace\vec v&#95;1,\vec v&#95;3\rbrace\\)</span>. The arrow for <span class="math-inline">\\(\vec v&#95;2\\)</span> is not in that plane, which is why we did not need it in the combination. To see this clearly, open the interactive viewer and rotate the scene:

<https://eecs245.org/resources/homeworks/hw03/hw03-problem-2.html>

</details>

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

<details markdown="1"><summary>Solution</summary>

No solution.

This is a system of three equations in two unknowns, because the linear combination uses only two vectors. We'll attempt to solve it the same way as in part **(a)**.

<div class="math-display">
$$
\begin{align*}
p\vec v_1 + q\vec v_2
&= \vec x \\\\
p\begin{bmatrix}2\\\\3\\\\0\end{bmatrix}
+ q\begin{bmatrix}-1\\\\2\\\\-1\end{bmatrix}
&= \begin{bmatrix}-6\\\\1\\\\4\end{bmatrix}
\end{align*}
$$
</div>

Equating components gives the system

<div class="math-display">
$$
\begin{align*}
2p - q &= -6 \tag{1}\\\\
3p + 2q &= 1 \tag{2}\\\\
-q &= 4 \tag{3}
\end{align*}
$$
</div>

From <span class="math-inline">\\((3)\\)</span> we get <span class="math-inline">\\(q=-4\\)</span>. Use <span class="math-inline">\\((1)\\)</span> with <span class="math-inline">\\(q=-4\\)</span>:

<div class="math-display">
$$
\begin{align*}
2p - (-4) &= -6 \\\\
2p + 4 &= -6 \\\\
2p &= -10 \\\\
p &= -5
\end{align*}
$$
</div>

Now check <span class="math-inline">\\((2)\\)</span> with <span class="math-inline">\\(p=-5,\ q=-4\\)</span>:

<div class="math-display">
$$
\begin{align*}
3(-5) + 2(-4) &= -15 - 8 = -23 \neq 1
\end{align*}
$$
</div>

Since <span class="math-inline">\\((2)\\)</span> is violated, the system is inconsistent and there are no constants <span class="math-inline">\\(p,q\\)</span> satisfying all three equations.

![image](imgs/solving_systems_2c_sol.png)

**Why this also makes sense visually.** From the 3D visualization, <span class="math-inline">\\(\vec x\\)</span> lies in the plane generated by linear combinations of <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;3\\)</span> <span class="math-inline">\\(\big(\mathrm{span}\lbrace\vec v&#95;1,\vec v&#95;3\rbrace\big)\\)</span>. Trying to use only <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> keeps you in the different plane <span class="math-inline">\\(\mathrm{span}\lbrace\vec v&#95;1,\vec v&#95;2\rbrace\\)</span>, which does not contain <span class="math-inline">\\(\vec x\\)</span>. Hence no solution with <span class="math-inline">\\(p\vec v&#95;1+q\vec v&#95;2=\vec x\\)</span>.

<div class="math-display">
$$
\boxed{\text{No solution}}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\vec{x}_{\text{c}} \cdot \vec{y}_{\text{c}}
&=
\begin{bmatrix}
x_1-\bar{x} \\\\[2pt]
x_2-\bar{x} \\\\[2pt]
\vdots \\\\[2pt]
x_n-\bar{x}
\end{bmatrix}
\cdot
\begin{bmatrix}
y_1-\bar{y} \\\\[2pt]
y_2-\bar{y} \\\\[2pt]
\vdots \\\\[2pt]
y_n-\bar{y}
\end{bmatrix} \\\\[6pt]
&=
(x_1-\bar{x})(y_1-\bar{y})
+ (x_2-\bar{x})(y_2-\bar{y})
+ \cdots
+ (x_n-\bar{x})(y_n-\bar{y}) \\\\[6pt]
&= \sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

From part **(a)**, the dot product of the mean--centered vectors is

<div class="math-display">
$$
\vec{x}_{\mathrm c}\cdot \vec{y}_{\mathrm c} \;=\; \sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)
$$
</div>

 and the norms are

<div class="math-display">
$$
\|\vec{x}_{\mathrm c}\| \;=\; \sqrt{\sum_{i=1}^n (x_i-\bar x)^2},
\qquad
\|\vec{y}_{\mathrm c}\| \;=\; \sqrt{\sum_{i=1}^n (y_i-\bar y)^2}
$$
</div>

Start from the right-hand side and substitute these definitions:

<div class="math-display">
$$
\begin{align*}
\frac{\vec{x}_{\mathrm c}\cdot \vec{y}_{\mathrm c}}{\|\vec{x}_{\mathrm c}\|\,\|\vec{y}_{\mathrm c}\|}
&= \frac{\sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)}
{\sqrt{\sum_{i=1}^n (x_i-\bar x)^2}\;\sqrt{\sum_{i=1}^n (y_i-\bar y)^2}}
\end{align*}
$$
</div>

Now rewrite each square root as <span class="math-inline">\\(\sqrt{n}\\)</span> times the square root of the average (this is just <span class="math-inline">\\(\sqrt{\sum}=\sqrt{n}\sqrt{\text{average}}\\)</span>):

<div class="math-display">
$$
\begin{align*}
&= \frac{\sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)}
{\,\big(\sqrt{n}\,\sqrt{\tfrac{1}{n}\sum_{i=1}^n (x_i-\bar x)^2}\big)\;
\big(\sqrt{n}\,\sqrt{\tfrac{1}{n}\sum_{i=1}^n (y_i-\bar y)^2}\big)}
\end{align*}
$$
</div>

Let

<div class="math-display">
$$
\sigma_x \;=\; \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i-\bar x)^2},
\qquad
\sigma_y \;=\; \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i-\bar y)^2}
$$
</div>

 so each denominator factor is <span class="math-inline">\\(\sqrt{n}\sigma&#95;x\\)</span> and <span class="math-inline">\\(\sqrt{n}\sigma&#95;y\\)</span>. This gives

<div class="math-display">
$$
\begin{align*}
&= \frac{\sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)}{\,n\,\sigma_x\,\sigma_y}
\end{align*}
$$
</div>

Finally, pull out the <span class="math-inline">\\(1/n\\)</span> and group terms to match the correlation definition (average of standardized products):

<div class="math-display">
$$
\begin{align*}
\frac{\vec{x}_{\mathrm c}\cdot \vec{y}_{\mathrm c}}{\|\vec{x}_{\mathrm c}\|\,\|\vec{y}_{\mathrm c}\|}&= \frac{1}{n}\sum_{i=1}^n
\left(\frac{x_i-\bar x}{\sigma_x}\right)
\left(\frac{y_i-\bar y}{\sigma_y}\right)
\;=\; r
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) In 1-2 English sentences, explain why the result from part **b)** implies that <span class="math-inline">\\(-1 \leq r \leq 1\\)</span>.

<details markdown="1"><summary>Solution</summary>

The result from part **b)** implies that <span class="math-inline">\\(-1 \leq r \leq 1\\)</span> because the right-hand side of the equation is the cosine of the angle between the mean-centered vectors, and the cosine of an angle is bounded between <span class="math-inline">\\(-1\\)</span> and <span class="math-inline">\\(1\\)</span>.

</details>

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

<details markdown="1"><summary>Solution</summary>

Start by rewriting the squared norm as a dot product and expanding. We color the dot--product pieces to track them: <span class="math-inline">\\(\textcolor{orange}{\vec y\cdot\vec y}\\)</span> (orange), <span class="math-inline">\\(\textcolor{blue}{\vec x\cdot\vec x}\\)</span> (blue), and <span class="math-inline">\\(\textcolor{magenta}{\vec x\cdot\vec y}\\)</span> (magenta).

<div class="math-display">
$$
\begin{align*}
f(k)
&= \|\vec y - k\vec x\|^2 \\\\
&= (\vec y - k\vec x)\!\cdot\!(\vec y - k\vec x) \\\\
&= \textcolor{orange}{\vec y\!\cdot\!\vec y}
\;-\; k\,\textcolor{magenta}{(\vec y\!\cdot\!\vec x)}
\;-\; k\,\textcolor{magenta}{(\vec x\!\cdot\!\vec y)}
\;+\; k^2\,\textcolor{blue}{(\vec x\!\cdot\!\vec x)} \\\\
&= \textcolor{orange}{\|\vec y\|^2}
\;-\; 2k\,\textcolor{magenta}{(\vec x\!\cdot\!\vec y)}
\;+\; k^2\,\textcolor{blue}{(\vec x\!\cdot\!\vec x)}
\qquad\text{(since }\vec x\!\cdot\!\vec y=\vec y\!\cdot\!\vec x\text{).}
\end{align*}
$$
</div>

Now differentiate term--by--term with respect to <span class="math-inline">\\(k\\)</span> (the dot products are constants with respect to <span class="math-inline">\\(k\\)</span>):

<div class="math-display">
$$
\frac{\text{d}f}{\text{d}k}
= 0 \;-\; 2\,\textcolor{magenta}{(\vec x\!\cdot\!\vec y)}
\;+\; 2k\,\textcolor{blue}{(\vec x\!\cdot\!\vec x)}.
$$
</div>

<div class="math-display">
$$
\boxed{\;\displaystyle \frac{\text{d}f}{\text{d}k} \;=\; -2\,\vec x\!\cdot\!\vec y \;+\; 2k\,(\vec x\!\cdot\!\vec x)\;}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(k^*\\)</span>, the value of <span class="math-inline">\\(k\\)</span> that minimizes <span class="math-inline">\\(f(k)\\)</span>. A second derivative test is not necessary.

<details markdown="1"><summary>Solution</summary>

From part **a)**, we know that <span class="math-inline">\\(\dfrac{\text{d}f}{\text{d}k} = -2\vec x\cdot\vec y + 2k(\vec x\cdot\vec x)\\)</span>. Let's set this derivative to <span class="math-inline">\\(0\\)</span> and solve for <span class="math-inline">\\(k\\)</span>.

<div class="math-display">
$$
\begin{align*}
-2\,\vec x\!\cdot\!\vec y + 2k\,(\vec x\!\cdot\!\vec x) &= 0 \\\\
2k\,(\vec x\!\cdot\!\vec x) &= 2\,\vec x\!\cdot\!\vec y \\\\
k^* &= \frac{\vec x\!\cdot\!\vec y}{\vec x\!\cdot\!\vec x}
\end{align*}
$$
</div>

This gives the minimizer when <span class="math-inline">\\(\vec x\cdot\vec x&gt;0\\)</span>. If <span class="math-inline">\\(\vec x\cdot\vec x=0\\)</span>, the only possibility is <span class="math-inline">\\(\vec x=\vec 0=\begin{bmatrix}0\\\\0\\\\ \vdots\\\\ 0\end{bmatrix}\\)</span>. In that case,

<div class="math-display">
$$
f(k)=\|\vec y - k\vec 0\|^2=\|\vec y\|^2
$$
</div>

 which does not depend on <span class="math-inline">\\(k\\)</span>. Thus every value of <span class="math-inline">\\(k\\)</span> yields the same objective value, and any <span class="math-inline">\\(k\\)</span> minimizes <span class="math-inline">\\(f\\)</span>.

<div class="math-display">
$$
\boxed{\,k^*=\dfrac{\vec x\!\cdot\!\vec y}{\vec x\!\cdot\!\vec x}\ \text{ when }\ \vec x\neq \vec 0\,}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Show that the vectors <span class="math-inline">\\(k^* \vec x\\)</span> and <span class="math-inline">\\(\vec y - k^* \vec x\\)</span> are orthogonal.

<details markdown="1"><summary>Solution</summary>

From part **b)**, <span class="math-inline">\\(k^*=\dfrac{\vec x\cdot\vec y}{\vec x\cdot\vec x}\\)</span> when <span class="math-inline">\\(\vec x\neq \vec 0\\)</span>. To check whether two vectors are orthogonal, we compute their dot product; they are orthogonal if and only if the dot product equals <span class="math-inline">\\(0\\)</span>.

<div class="math-display">
$$
\begin{align*}
(k^* \vec x)\cdot(\vec y - k^* \vec x)
&= (k^*\vec x)\cdot \vec y \;-\; (k^*\vec x)\cdot(k^*\vec x) \\\\
&= k^*\,(\vec x\cdot \vec y) \;-\; (k^*)^2\,(\vec x\cdot \vec x) \\\\
&= \frac{\vec x\cdot \vec y}{\vec x\cdot \vec x}\,(\vec x\cdot \vec y)
\;-\; \left(\frac{\vec x\cdot \vec y}{\vec x\cdot \vec x}\right)^2 (\vec x\cdot \vec x) \\\\
&= \frac{(\vec x\cdot \vec y)^2}{\vec x\cdot \vec x}
\;-\; \frac{(\vec x\cdot \vec y)^2}{\vec x\cdot \vec x} \\\\
&= 0
\end{align*}
$$
</div>

Since the dot product is <span class="math-inline">\\(0\\)</span>, the vectors <span class="math-inline">\\(k^*\vec x\\)</span> and <span class="math-inline">\\(\vec y - k^*\vec x\\)</span> are orthogonal.

</details>

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

<details markdown="1"><summary>Solution</summary>

First, let's start by writing down an expression for mean squared error, <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span>.

<div class="math-display">
$$
\begin{align*}
R_\text{sq}(w) &= \frac{1}{n}\sum_{i=1}^n \big(y_i - w x_i\big)^2
\end{align*}
$$
</div>

Now, let's find <span class="math-inline">\\(\dfrac{\text{d}R&#95;\text{sq}}{\text{d}w}\\)</span>. Differentiate term by term; for each <span class="math-inline">\\(i\\)</span>,

<div class="math-display">
$$
\dfrac{\text{d}}{\text{d}w}\big(y_i - w x_i\big)^2 = 2\big(y_i - w x_i\big)(-x_i)
$$
</div>

Then,

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}R}{\text{d}w}
&= \frac{1}{n}\sum_{i=1}^n 2\big(y_i - w x_i\big)(-x_i) \\\\
&= -\frac{2}{n}\sum_{i=1}^n x_i y_i \;+\; \frac{2}{n} w \sum_{i=1}^n x_i^2
\end{align*}
$$
</div>

Next, we'll set <span class="math-inline">\\(\dfrac{\text{d}R&#95;\text{sq}}{\text{d}w}=0\\)</span> and solve for the corresponding value of <span class="math-inline">\\(w\\)</span>, called <span class="math-inline">\\(w^*\\)</span>.

<div class="math-display">
$$
\begin{align*}
-\sum_{i=1}^n x_i y_i \;+\; w^* \sum_{i=1}^n x_i^2 &= 0 \\\\
w^* \sum_{i=1}^n x_i^2 &= \sum_{i=1}^n x_i y_i \\\\
w^* &= \dfrac{\sum_{i=1}^n x_i y_i}{\sum_{i=1}^n x_i^2}
\end{align*}
$$
</div>

<div class="math-display">
$$
\boxed{\,w^* = \dfrac{\sum_{i=1}^n x_i y_i}{\sum_{i=1}^n x_i^2}\,}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ \vdots \\\\ x&#95;n \end{bmatrix}\\)</span> is a vector of all the <span class="math-inline">\\(x&#95;i\\)</span> values in the dataset and <span class="math-inline">\\(\vec y = \begin{bmatrix} y&#95;1 \\\\ y&#95;2 \\\\ \vdots \\\\ y&#95;n \end{bmatrix}\\)</span> is a vector of all the <span class="math-inline">\\(y&#95;i\\)</span> values in the dataset.

Then, notice that <span class="math-inline">\\(w^*\\)</span> (the optimal slope) from part **d)** is the same formula as <span class="math-inline">\\(k^*\\)</span> (the optimal stretching factor) from part **b)**! This is not a coincidence: the problem in part **d)** is equivalent to the problem stated at the start of this question, it's just stated differently! This may be a bit confusing, since:

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

<details markdown="1"><summary>Solution</summary>

Minimizing

<div class="math-display">
$$
R_\text{sq}(w) = \frac{1}{n}\sum_{i=1}^n (y_i - w x_i)^2
$$
</div>

 is equivalent to minimizing

<div class="math-display">
$$
\lVert \vec y - w \vec x \rVert^2
$$
</div>

 because the vector of residuals has components <span class="math-inline">\\(y&#95;i - w x&#95;i\\)</span>, and squaring and summing those components is exactly the squared Euclidean norm of <span class="math-inline">\\(\vec y - w \vec x\\)</span>. Thus, choosing the best slope <span class="math-inline">\\(w\\)</span> in the regression problem is the same as choosing the best scalar <span class="math-inline">\\(k\\)</span> that makes <span class="math-inline">\\(k\vec x\\)</span> as close as possible to <span class="math-inline">\\(\vec y\\)</span>.

</details>

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

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\|\vec v\|_2 &= \sqrt{3^2 + (-6)^2 + 0^2 + 2^2}
= \sqrt{9 + 36 + 0 + 4}
= \sqrt{49}
= 7,\\\\
\|\vec v\|_1 &= |3| + |-6| + |0| + |2|
= 3 + 6 + 0 + 2
= 11,\\\\
\|\vec v\|_\infty &= \max\{\,|3|,\,|-6|,\,|0|,\,|2|\,\}
= \max\{3,6,0,2\}
= 6.
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

We want to check whether the parallelogram law holds for the <span class="math-inline">\\(L&#95;1\\)</span> norm

<div class="math-display">
$$
\|\vec u+\vec v\|_1^2 + \|\vec u-\vec v\|_1^2 \stackrel{?}{=} 2\|\vec u\|_1^2 + 2\|\vec v\|_1^2
$$
</div>

Choose

<div class="math-display">
$$
\vec u=\begin{bmatrix}1\\\\0\end{bmatrix}
\qquad
\vec v=\begin{bmatrix}0\\\\1\end{bmatrix}
$$
</div>

Left-hand side

<div class="math-display">
$$
\vec u+\vec v=\begin{bmatrix}1\\\\1\end{bmatrix},\quad
\|\vec u+\vec v\|_1=|1|+|1|=2,\quad
\|\vec u+\vec v\|_1^2=2^2=4
$$
</div>



<div class="math-display">
$$
\vec u-\vec v=\begin{bmatrix}1\\\\-1\end{bmatrix},\quad
\|\vec u-\vec v\|_1=|1|+|-1|=2,\quad
\|\vec u-\vec v\|_1^2=2^2=4
$$
</div>



<div class="math-display">
$$
\|\vec u+\vec v\|_1^2+\|\vec u-\vec v\|_1^2=4+4=8
$$
</div>

Right-hand side

<div class="math-display">
$$
\|\vec u\|_1=|1|+|0|=1,\quad \|\vec v\|_1=|0|+|1|=1
$$
</div>



<div class="math-display">
$$
2\|\vec u\|_1^2+2\|\vec v\|_1^2 = 2\cdot 1^2 + 2\cdot 1^2 = 2+2=4
$$
</div>

Since <span class="math-inline">\\(8\neq 4\\)</span>, the parallelogram law does not hold for the <span class="math-inline">\\(L&#95;1\\)</span> norm with this choice of <span class="math-inline">\\(\vec u,\vec v\\)</span>

</details>

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

<details markdown="1"><summary>Solution</summary>

Start from the definition of the <span class="math-inline">\\(L&#95;2\\)</span> norm

<div class="math-display">
$$
\begin{align*}
\|\vec v\|_2^2 &= \sum_{i=1}^n v_i^2
\end{align*}
$$
</div>

For each index <span class="math-inline">\\(i\\)</span>, by the definition of the <span class="math-inline">\\(L&#95;\infty\\)</span> norm we have <span class="math-inline">\\(|v&#95;i|\le \|\vec v\|&#95;\infty\\)</span>

<div class="math-display">
$$
\begin{align*}
v_i^2 \le \|\vec v\|_\infty^2 \quad \text{for each } i
\end{align*}
$$
</div>

Sum these inequalities over <span class="math-inline">\\(i=1,\dots,n\\)</span>

<div class="math-display">
$$
\begin{align*}
\sum_{i=1}^n v_i^2 \le \sum_{i=1}^n \|\vec v\|_\infty^2 = n\,\|\vec v\|_\infty^2
\end{align*}
$$
</div>

Thus

<div class="math-display">
$$
\begin{align*}
\|\vec v\|_2^2 \le n\,\|\vec v\|_\infty^2
\end{align*}
$$
</div>

Both sides are nonnegative, so taking square roots preserves the inequality

<div class="math-display">
$$
\|\vec v\|_2 \le \sqrt{n}\,\|\vec v\|_\infty
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

As the hint implies, let's start by expanding the definition of <span class="math-inline">\\(\|\vec v\|&#95;1^2\\)</span>. We write the <span class="math-inline">\\(L&#95;1\\)</span> norm as one square to avoid carrying a square root

<div class="math-display">
$$
\|\vec v\|_1^2 = \big(|v_1| + |v_2| + \cdots + |v_n|\big)^2
$$
</div>

For intuition, recall the perspective from part **(c)**: by definition, the <span class="math-inline">\\(L&#95;\infty\\)</span> norm is the largest absolute value among the components, so <span class="math-inline">\\(\|\vec v\|&#95;\infty \ge |v&#95;i|\\)</span> for every <span class="math-inline">\\(i\\)</span>, and this remains true after squaring because both sides are nonnegative. Here, we will instead use the hint and expand the <span class="math-inline">\\(L&#95;1\\)</span> square into "square" terms and "cross" terms

<div class="math-display">
$$
\|\vec v\|_1^2 = \underbrace{|v_1|^2 + |v_2|^2 + \cdots + |v_n|^2}_{\text{squares}}
\;+\; \underbrace{2\big(|v_1||v_2| + |v_1||v_3| + \cdots + |v_{n-1}||v_n|\big)}_{\text{cross terms}}
$$
</div>

Each cross term <span class="math-inline">\\(|v&#95;i||v&#95;j|\\)</span> is nonnegative, so the cross--term sum shown above is <span class="math-inline">\\(\ge 0\\)</span>

<div class="math-display">
$$
\|\vec v\|_1^2 \;\ge\; |v_1|^2 + |v_2|^2 + \cdots + |v_n|^2
$$
</div>

The right--hand side is exactly the square of the <span class="math-inline">\\(L&#95;2\\)</span> norm

<div class="math-display">
$$
|v_1|^2 + \cdots + |v_n|^2 \;=\; \|\vec v\|_2^2
$$
</div>

Therefore

<div class="math-display">
$$
\|\vec v\|_1^2 \;\ge\; \|\vec v\|_2^2
$$
</div>

Both sides are nonnegative, so taking square roots preserves the inequality

<div class="math-display">
$$
\|\vec v\|_2 \;\le\; \|\vec v\|_1
$$
</div>

</details>

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

{% endraw %}
