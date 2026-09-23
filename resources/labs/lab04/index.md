---
layout: page
title: "Lab 4: Orthogonality and Projections"
description: "Lab 4: Orthogonality and Projections activities."
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

# Lab 4: Orthogonality and Projections

**due** by the end of your lab section on Wednesday, September 23rd, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab04/lab04.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab04/lab04-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete all activities and show your lab TA by the end of the lab section. To receive credit for Activity 1, you'll need to show your lab TA that all test cases have passed **and** that you have answered the written questions in Task 4. Instructions on how to do this are in the lab notebook.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Presidential Speeches and Cosine Similarity](#activity-1-presidential-speeches-and-cosine-similarity)
- [Activity 2: Sum-Difference Orthogonality](#activity-2-sum-difference-orthogonality)
- [Activity 3: Orthogonal Projections](#activity-3-orthogonal-projections)
- [Activity 4: Orthogonal Decomposition with Orthonormal Vectors](#activity-4-orthogonal-decomposition-with-orthonormal-vectors)
- [Activity 5: Orthogonal Decomposition with Non-Unit Vectors](#activity-5-orthogonal-decomposition-with-non-unit-vectors)
- [Activity 6: A Plane from Spanning Vectors](#activity-6-a-plane-from-spanning-vectors)

---

## Recap: Projections

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

([Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/)) The **orthogonal projection** of the vector <span class="math-inline">\\(\vec u\\)</span> onto the vector <span class="math-inline">\\(\vec v\\)</span> is given by

<div class="math-display">
$$
\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v
$$
</div>

 Above, the scalar <span class="math-inline">\\(k^{\ast} = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v}\\)</span> was chosen to minimize <span class="math-inline">\\(\lVert \vec u - k \vec v \rVert^2\\)</span>.

</li>
<li markdown="1">

The vector <span class="math-inline">\\(\vec p\\)</span> is called the orthogonal projection because the resulting error vector,

<div class="math-display">
$$
\vec e = \vec u - \vec p = \vec u - k^* \vec v
$$
</div>

 is orthogonal to <span class="math-inline">\\(\vec v\\)</span>, meaning <span class="math-inline">\\(\vec e \cdot \vec v = 0\\)</span>.

</li>
</ul>

---

## Activity 1: Presidential Speeches and Cosine Similarity

Complete the tasks in the `lab04.ipynb` notebook.

There are two ways to access the supplemental Jupyter Notebook:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

**Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/fa26-code/tree/main), and open `labs/lab04/lab04.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

</li>
<li markdown="1">

**Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Flabs%2Flab04%2Flab04.ipynb&branch=main) to open `lab04.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

</li>
</ul>

To receive credit for Activity 1, you'll need to show your lab TA that all test cases have passed **and** that you have answered the written questions in Task 4.

---

## Activity 2: Sum-Difference Orthogonality

Let <span class="math-inline">\\(\vec u=\begin{bmatrix}2\\\\-1\\\\0\\\\5\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\2\\\\4\\\\-3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Show that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal.

<details markdown="1"><summary>Solution</summary>

Let's start by computing the two vectors:

<div class="math-display">
$$
\vec u+\vec v=\begin{bmatrix}3\\\\1\\\\4\\\\2\end{bmatrix},\qquad
\vec u-\vec v=\begin{bmatrix}1\\\\-3\\\\-4\\\\8\end{bmatrix}.
$$
</div>

 Their dot product is

<div class="math-display">
$$
(\vec u+\vec v)\cdot(\vec u-\vec v)
=3\cdot1+1\cdot(-3)+4\cdot(-4)+2\cdot 8
=3-3-16+16
=0.
$$
</div>

 Since the dot product is <span class="math-inline">\\(0\\)</span>, the vectors are orthogonal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now suppose <span class="math-inline">\\(\vec u,\vec v\in\mathbb{R}^n\\)</span> are arbitrary vectors with the same number of components. Is it always true that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal?

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

If so, prove why.

</li>
<li markdown="1">

If not, specify conditions under which it's guaranteed that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal.

</li>
</ul>

<em>Hint: Use the distributive property of the dot product, which states that </em>

<div class="math-display">
$$
(\vec a + \vec b) \cdot (\vec c + \vec d) = \vec a \cdot \vec c + \vec a \cdot \vec d + \vec b \cdot \vec c + \vec b \cdot \vec d
$$
</div>

<details markdown="1"><summary>Solution</summary>

For any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>,

<div class="math-display">
$$
(\vec u+\vec v)\cdot(\vec u-\vec v)
= \vec u\cdot\vec u - \vec u\cdot\vec v + \vec v\cdot\vec u - \vec v\cdot\vec v
= \|\vec u\|^2 - \|\vec v\|^2,
$$
</div>

 since <span class="math-inline">\\(\vec u\cdot\vec v=\vec v\cdot\vec u\\)</span>.

So, in order for <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> to be orthogonal, we need

<div class="math-display">
$$
\|\vec u\|^2 - \|\vec v\|^2 = 0
$$
</div>

 which means

<div class="math-display">
$$
\|\vec u\| = \|\vec v\|
$$
</div>

So, <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal if (and only if!) the two vectors have equal length. That was the case in part **a)** --- both vectors had a norm of <span class="math-inline">\\(\sqrt{2^2 + (-1)^2 + 0^2 + 5^2} = \sqrt{30}\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 3: Orthogonal Projections

Let <span class="math-inline">\\(\vec c = \begin{bmatrix} 1 \\\\ 2 \\\\ -4 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec d = \begin{bmatrix} 3 \\\\ 2 \\\\ 0 \\\\ -1 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find the orthogonal projection of <span class="math-inline">\\(\vec c\\)</span> onto <span class="math-inline">\\(\vec d\\)</span>. Call this vector <span class="math-inline">\\(\vec q\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\vec q &= \left(\frac{\vec c \cdot \vec d}{\vec d \cdot \vec d}\right)\vec d \\\\
&= \frac{1 \cdot 3 + 2 \cdot 2 + (-4) \cdot 0 + 0 \cdot (-1)}{3^2 + 2^2 + 0^2 + (-1)^2} \vec d \\\\
&= \frac{3+4}{9+4+1} \vec{d} \\\\
&= \frac{7}{14} \vec{d} \\\\
&= \frac{1}{2} \vec{d} \\\\
&= \begin{bmatrix} 1.5 \\\\ 1 \\\\ 0 \\\\ -0.5 \end{bmatrix}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find the error vector, <span class="math-inline">\\(\vec r = \vec c - \vec q\\)</span>. Which vector is <span class="math-inline">\\(\vec r\\)</span> orthogonal to, <span class="math-inline">\\(\vec c\\)</span> or <span class="math-inline">\\(\vec d\\)</span>? Draw a rough picture of the relationship between <span class="math-inline">\\(\vec c\\)</span>, <span class="math-inline">\\(\vec d\\)</span>, <span class="math-inline">\\(\vec q\\)</span>, and <span class="math-inline">\\(\vec r\\)</span>. *You may want to review [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/).*

<details markdown="1"><summary>Solution</summary>

First, let's find <span class="math-inline">\\(\vec{r}\\)</span>.

<div class="math-display">
$$
\begin{align*}
\vec{r} &= \vec{c} - \vec{q} \\\\
&= \begin{bmatrix} 1 \\\\ 2 \\\\ -4 \\\\ 0 \end{bmatrix} - \begin{bmatrix} 1.5 \\\\ 1 \\\\ 0 \\\\ -0.5 \end{bmatrix} \\\\
&=\begin{bmatrix} -0.5 \\\\ 1 \\\\ -4 \\\\ 0.5 \end{bmatrix}
\end{align*}
$$
</div>

<span class="math-inline">\\(\vec{r}\\)</span> is orthogonal to <span class="math-inline">\\(\vec{d}\\)</span>, not <span class="math-inline">\\(\vec{c}\\)</span>, as confirmed by the dot products. The key idea we introduced in [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/) is that the error vector is orthogonal to the vector we projected onto. Here, <span class="math-inline">\\(\vec r\\)</span> is the error vector and <span class="math-inline">\\(\vec d\\)</span> is the vector we projected onto.

<div class="math-display">
$$
\begin{align*}
\vec{r} \cdot \vec{c} &= (-0.5) \cdot 1 + 1 \cdot 2 + (-4) \cdot (-4) + 0.5 \cdot 0 \\\\
&= -0.5 + 2 + 16 \\\\
&= 17.5 \\\\
\\\\
\vec{r} \cdot \vec{d} &= (-0.5) \cdot 3 + 1 \cdot 2 + (-4) \cdot 0 + 0.5 \cdot (-1) \\\\
&= -1.5 + 2-0.5 \\\\
&=0
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Activity 4: Orthogonal Decomposition with Orthonormal Vectors

Let

<div class="math-display">
$$
\vec{v}_1
=
\begin{bmatrix}
\frac{1}{\sqrt{5}}\\\\[2pt]
\frac{2}{\sqrt{5}}
\end{bmatrix},
\qquad
\vec{v}_2
=
\begin{bmatrix}
-\frac{2}{\sqrt{5}}\\\\[2pt]
\frac{1}{\sqrt{5}}
\end{bmatrix}
$$
</div>

<span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> are called **orthonormal**, because they are:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

unit vectors: <span class="math-inline">\\(\lVert \vec v&#95;1 \rVert = 1\\)</span> and <span class="math-inline">\\(\rVert \vec v&#95;2 \rVert = 1\\)</span>.

</li>
<li markdown="1">

orthogonal: <span class="math-inline">\\(\vec v&#95;1 \cdot \vec v&#95;2 = 0\\)</span>.

</li>
</ul>

Additionally, let <span class="math-inline">\\(\vec u = \begin{bmatrix} 4 \\\\ -1 \end{bmatrix}\\)</span>.

Our goal in this activity is to write <span class="math-inline">\\(\vec{u}\\)</span> as a linear combination of <span class="math-inline">\\(\vec{v}&#95;1\\)</span> and <span class="math-inline">\\(\vec{v}&#95;2\\)</span>. The fact that <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> are orthonormal makes this simple.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec u \cdot \vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec u \cdot \vec v&#95;2\\)</span>. Your answer should involve <span class="math-inline">\\(\sqrt{5}\\)</span>; don't use a calculator.

<details markdown="1"><summary>Solution</summary>

To find each dot product, we multiply corresponding components and add:

<div class="math-display">
$$
\begin{align*}
\vec u \cdot \vec v_1
&= 4 \cdot \frac{1}{\sqrt{5}} + (-1) \cdot \frac{2}{\sqrt{5}}
= \frac{4 - 2}{\sqrt{5}}
= \boxed{\frac{2}{\sqrt{5}}} \\\\
\vec u \cdot \vec v_2
&= 4 \cdot \left(-\frac{2}{\sqrt{5}}\right) + (-1) \cdot \frac{1}{\sqrt{5}}
= \frac{-8 - 1}{\sqrt{5}}
= \boxed{-\frac{9}{\sqrt{5}}}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Evaluate

<div class="math-display">
$$
(\vec u \cdot \vec v_1) \vec v_1 + (\vec u \cdot \vec v_2) \vec v_2
$$
</div>

What do you notice?

<details markdown="1"><summary>Solution</summary>

Using the dot products we found in part **a)**, we have

<div class="math-display">
$$
\begin{align*}
(\vec u \cdot \vec v_1)\vec v_1 + (\vec u \cdot \vec v_2)\vec v_2
&= \frac{2}{\sqrt{5}}\begin{bmatrix} \frac{1}{\sqrt{5}} \\\\ \frac{2}{\sqrt{5}} \end{bmatrix}
- \frac{9}{\sqrt{5}}\begin{bmatrix} -\frac{2}{\sqrt{5}} \\\\ \frac{1}{\sqrt{5}} \end{bmatrix} \\\\
&= \begin{bmatrix} \frac{2}{5} \\\\ \frac{4}{5} \end{bmatrix}
+ \begin{bmatrix} \frac{18}{5} \\\\ -\frac{9}{5} \end{bmatrix} \\\\
&= \begin{bmatrix} 4 \\\\ -1 \end{bmatrix}
= \boxed{\vec u}
\end{align*}
$$
</div>

We get back <span class="math-inline">\\(\vec u\\)</span>! In other words, the dot products from part **a)** are exactly the coefficients we need to write <span class="math-inline">\\(\vec u\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Why is <span class="math-inline">\\((\vec u \cdot \vec v&#95;1) \vec v&#95;1 + (\vec u \cdot \vec v&#95;2) \vec v&#95;2 = \vec u\\)</span>?

<em>Hint: Start by drawing a picture of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v&#95;1\\)</span>, and <span class="math-inline">\\(\vec v&#95;2\\)</span>, and reviewing the <a href="https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-decomposition">"Orthogonal Decomposition" section of Chapter 3.4</a> and the very last example discussed in <a href="https://eecs245.org/resources/lecture-pdfs/lec07-filled.pdf#page=17">yesterday's lecture</a>.</em>

<details markdown="1"><summary>Solution</summary>

The two terms in part **b)** are the projections of <span class="math-inline">\\(\vec u\\)</span> onto the orthogonal directions <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span>. Since these vectors are orthogonal, their projections add to <span class="math-inline">\\(\vec u\\)</span>, just as in the orthogonal decomposition we saw in lecture.
</details>

</div>
</div>

</div>

---

## Activity 5: Orthogonal Decomposition with Non-Unit Vectors

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(\vec{v}&#95;1 = \begin{bmatrix} -1 \\\\ 2 \\\\ 2 \end{bmatrix}\\)</span> <span class="math-inline">\\(\vec{v}&#95;2 = \begin{bmatrix} 2 \\\\ 2 \\\\ -1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec{v}&#95;3 = \begin{bmatrix} 2 \\\\ -1 \\\\ 2 \end{bmatrix}\\)</span>. Write <span class="math-inline">\\(\vec{u} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span> as a linear combination of <span class="math-inline">\\(\vec{v}&#95;1\\)</span>, <span class="math-inline">\\(\vec{v}&#95;2\\)</span>, and <span class="math-inline">\\(\vec{v}&#95;3\\)</span>, and verify that your answer is correct. Note that <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span> are pairwise orthogonal.

<details markdown="1"><summary>Solution</summary>

We are given

<div class="math-display">
$$
\vec v_1=\begin{bmatrix}-1\\\\2\\\\2\end{bmatrix}\quad
\vec v_2=\begin{bmatrix}2\\\\2\\\\-1\end{bmatrix}\quad
\vec v_3=\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}\quad
\vec u=\begin{bmatrix}1\\\\1\\\\1\end{bmatrix}
$$
</div>

We're looking for scalars <span class="math-inline">\\(a,b,c\\)</span> such that <span class="math-inline">\\(\vec u=a\vec v&#95;1+b\vec v&#95;2+c\vec v&#95;3\\)</span>.

**Solution 1: Solving a system of equations**

<div class="math-display">
$$
a\!\begin{bmatrix}-1\\\\2\\\\2\end{bmatrix}
+b\!\begin{bmatrix}2\\\\2\\\\-1\end{bmatrix}
+c\!\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}
=\begin{bmatrix}1\\\\1\\\\1\end{bmatrix}
$$
</div>

Is equivalent to the system of equations:

<div class="math-display">
$$
\begin{align}
-a+2b+2c=1 \\\\
2a+2b-c=1 \\\\
2a-b+2c=1
\end{align}
$$
</div>

Using elimination:

<div class="math-display">
$$
\begin{align*}
\text{(Eq.\,2)}-\text{(Eq.\,3)}&:\quad (2a-2a)+(2b-(-b))+(-c-2c)=0
\\\\[-2pt]
&\qquad\Rightarrow\quad 3b-3c=0 \quad\Rightarrow\quad b=c
\\\\[6pt]
\text{(Eq.\,2)}-\text{(Eq.\,1)}&:\quad (2a-(-a))+(2b-2b)+(-c-2c)=0
\\\\[-2pt]
&\qquad\Rightarrow\quad 3a-3c=0 \quad\Rightarrow\quad a=c
\end{align*}
$$
</div>

This tells us that <span class="math-inline">\\(a = b = c\\)</span>. Plugging this back into Eq. 2 gives us:

<div class="math-display">
$$
-a + 2a + 2a = 1 \rightarrow 3a = 1 \rightarrow a = \frac{1}{3}
$$
</div>

So, <span class="math-inline">\\(a = b = c = \frac{1}{3}\\)</span>, and:

<div class="math-display">
$$
\vec u=\tfrac13\,\vec v_1+\tfrac13\,\vec v_2+\tfrac13\,\vec v_3
$$
</div>

We can verify that we did this correctly by computing the right-hand side above:

<div class="math-display">
$$
\frac{1}{3}\vec v_1+\frac{1}{3}\vec v_2+\frac{1}{3}\vec v_3
=\frac{1}{3}\begin{bmatrix}-1\\\\2\\\\2\end{bmatrix}+\frac{1}{3}\begin{bmatrix}2\\\\2\\\\-1\end{bmatrix}+\frac{1}{3}\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}
=\begin{bmatrix}-1/3+2/3+2/3\\\\2/3+2/3-1/3\\\\2/3-1/3+2/3\end{bmatrix}
=\begin{bmatrix}1\\\\1\\\\1\end{bmatrix}
=\vec u
$$
</div>

**Solution 2: Using the fact that <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span> are orthogonal**

As is alluded to in part **b)**, we can use the fact that <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \vec v&#95;3\\)</span> are orthogonal to find coefficients <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> by projecting <span class="math-inline">\\(\vec u\\)</span> onto each of the <span class="math-inline">\\(\vec v&#95;i\\)</span>s. This is similar to what was done in the [Orthogonal Decomposition](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/#orthogonal-decomposition) section of Chapter 3.4.

Let <span class="math-inline">\\(\vec p&#95;i\\)</span> be the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v&#95;i\\)</span>, for <span class="math-inline">\\(i = 1, 2, 3\\)</span>. Then, we have:

<div class="math-display">
$$
\vec p_1 = \frac{\vec u \cdot \vec v_1}{\vec v_1 \cdot \vec v_1} \vec v_1 = \frac{1 \cdot (-1) + 1 \cdot 2 + 1 \cdot 2}{(-1)^2 + 2^2 + 2^2} \vec v_1 = \frac{3}{9} \vec v_1 = \frac{1}{3} \vec v_1
$$
</div>



<div class="math-display">
$$
\vec p_2 = \frac{\vec u \cdot \vec v_2}{\vec v_2 \cdot \vec v_2} \vec v_2 = \frac{1 \cdot 2 + 1 \cdot 2 + 1 \cdot (-1)}{2^2 + 2^2 + (-1)^2} \vec v_2 = \frac{3}{9} \vec v_2 = \frac{1}{3} \vec v_2
$$
</div>



<div class="math-display">
$$
\vec p_3 = \frac{\vec u \cdot \vec v_3}{\vec v_3 \cdot \vec v_3} \vec v_3 = \frac{1 \cdot 2 + 1 \cdot (-1) + 1 \cdot 2}{2^2 + (-1)^2 + 2^2} \vec v_3 = \frac{3}{9} \vec v_3 = \frac{1}{3} \vec v_3
$$
</div>

Adding <span class="math-inline">\\(\vec p&#95;1, \vec p&#95;2, \vec p&#95;3\\)</span> gives us:

<div class="math-display">
$$
\vec p_1 + \vec p_2 + \vec p_3 = \frac{1}{3} \vec v_1 + \frac{1}{3} \vec v_2 + \frac{1}{3} \vec v_3 = \vec u
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
In general, suppose that <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span> are **orthogonal** vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>, meaning that <span class="math-inline">\\(\vec v&#95;i \cdot \vec v&#95;j = 0\\)</span> for all <span class="math-inline">\\(i \neq j\\)</span>. **Given that** it is possible to write <span class="math-inline">\\(\vec u\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span>,

show that the coefficients of the linear combination

<div class="math-display">
$$
\vec u = a_1 \vec v_1 + a_2 \vec v_2 + \cdots + a_d \vec v_d
$$
</div>

are given by

<div class="math-display">
$$
a_i = \frac{\vec u \cdot \vec v_i}{\vec v_i \cdot \vec v_i}
$$
</div>

<em>Hint: Start by taking the dot product of both sides of the linear combination equation with <span class="math-inline">\\(\vec v&#95;1\\)</span>. What do you notice?</em>

<details markdown="1"><summary>Solution</summary>

We're told to assume that any pair of vectors among <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span> are orthogonal, and that <span class="math-inline">\\(\vec u\\)</span> can be written as a linear combination of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span>.

<div class="math-display">
$$
\vec u = a_1 \vec v_1 + a_2 \vec v_2 + \cdots + a_d \vec v_d
$$
</div>

As the hint suggests, let's take the dot product of both sides with <span class="math-inline">\\(\vec v&#95;i\\)</span>, where <span class="math-inline">\\(i\\)</span> is some value in <span class="math-inline">\\(\lbrace1, 2, \ldots, d\rbrace\\)</span>.

<div class="math-display">
$$
\vec u\cdot \vec v_i
=\bigl(a_1\vec v_1+\cdots+a_d\vec v_d\bigr)\cdot \vec v_i
$$
</div>

Since <span class="math-inline">\\(\vec v&#95;i\cdot \vec v&#95;j=0\\)</span> for <span class="math-inline">\\(i\neq j\\)</span>, only the <span class="math-inline">\\(i=j\\)</span> term survives:

<div class="math-display">
$$
\begin{align*}
\vec u\cdot \vec v_i
&= \bigl(a_1\vec v_1+\cdots+a_d\vec v_d\bigr)\cdot \vec v_i
\\\\[6pt]
&= a_1(\vec v_1\cdot \vec v_i)+\cdots+a_{i-1}(\vec v_{i-1}\cdot \vec v_i)
+a_i(\vec v_i\cdot \vec v_i)
+a_{i+1}(\vec v_{i+1}\cdot \vec v_i)+\cdots+a_d(\vec v_d\cdot \vec v_i)
\\\\[6pt]
&= a_1(0)+\cdots+a_{i-1}(0)
+a_i(\vec v_i\cdot \vec v_i)
+a_{i+1}(0)+\cdots+a_d(0)
\\\\[6pt]
&= a_i(\vec v_i\cdot \vec v_i)
\\\\[6pt]
\end{align*}
$$
</div>

Solving for <span class="math-inline">\\(a&#95;i\\)</span> above gives us

<div class="math-display">
$$
\vec u \cdot \vec v_i = a_i(\vec v_i\cdot \vec v_i) \implies a_i = \frac{\vec u \cdot \vec v_i}{\vec v_i\cdot \vec v_i}
$$
</div>

Since <span class="math-inline">\\(i\\)</span> was arbitrary, the same calculation holds for any value of <span class="math-inline">\\(i\\)</span> in <span class="math-inline">\\(\lbrace1, 2, \ldots, d\rbrace\\)</span>.

What we proved here in part **b)** is that when writing a vector <span class="math-inline">\\(\vec u\\)</span> as a linear combination of orthogonal vectors, the coefficients of the linear combination can be found by projecting the vector <span class="math-inline">\\(\vec u\\)</span> onto each of the orthogonal vectors and adding the results, rather than solving a system of equations.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
In Activity 4, why didn't we divide by <span class="math-inline">\\(\vec v&#95;1 \cdot \vec v&#95;1\\)</span> (and <span class="math-inline">\\(\vec v&#95;2 \cdot \vec v&#95;2\\)</span>) when finding the coefficients?

<details markdown="1"><summary>Solution</summary>

The vectors in Activity 4 are unit vectors, so <span class="math-inline">\\(\vec v&#95;1 \cdot \vec v&#95;1 = \lVert \vec v&#95;1 \rVert^2 = 1\\)</span>, and likewise for <span class="math-inline">\\(\vec v&#95;2\\)</span>. Dividing by these dot products would just mean dividing by 1.
</details>

</div>
</div>

</div>

---

## Activity 6: A Plane from Spanning Vectors

This activity previews ideas that we will explore in upcoming lectures.

An important idea from [Chapter 4.1](https://notes.eecs245.org/linear-independence/span/) is that two non-parallel vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> (where <span class="math-inline">\\(n \geq 2\\)</span>) span a plane in <span class="math-inline">\\(n\\)</span>-dimensional space. Here, we'll show you how to find the equation of such a plane, given two vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. This is also touched on in [Chapter 4.4](https://notes.eecs245.org/linear-independence/lines-planes-hyperplanes/).

Let

<div class="math-display">
$$
\vec u = \begin{bmatrix} 5 \\\\ -7 \\\\ 3 \end{bmatrix}, \qquad
\vec v = \begin{bmatrix} 4 \\\\ 1 \\\\ -2 \end{bmatrix}, \qquad
P = \operatorname{span}(\{\vec u, \vec v\})
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a nonzero vector <span class="math-inline">\\(\vec n\\)</span> that is orthogonal to both <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. Verify your answer using dot products.

<details markdown="1"><summary>Solution</summary>

Write <span class="math-inline">\\(\vec n = \begin{bmatrix} a \\\\ b \\\\ c \end{bmatrix}\\)</span>. Orthogonality requires

<div class="math-display">
$$
5a - 7b + 3c = 0, \qquad 4a + b - 2c = 0.
$$
</div>

 The second equation gives <span class="math-inline">\\(b = 2c - 4a\\)</span>. Substituting into the first gives <span class="math-inline">\\(33a - 11c = 0\\)</span>, so <span class="math-inline">\\(c = 3a\\)</span> and <span class="math-inline">\\(b = 2a\\)</span>.

Note that there are infinitely many choices of <span class="math-inline">\\(a\\)</span>, meaning there are infinitely many <span class="math-inline">\\(\vec n\\)</span> that satisfy the constraints of the question. All we were asked for is **a** nonzero vector that is orthogonal to both <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>; once we find one such vector, any scalar multiple of it (of which there are infinitely many!) will also be orthogonal to both <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. Since we just need one vector, let's keep it simple: pick <span class="math-inline">\\(a = 1\\)</span>. Then,

<div class="math-display">
$$
\boxed{\vec n = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}}.
$$
</div>

 Indeed, <span class="math-inline">\\(\vec n \cdot \vec u = 5 - 14 + 9 = 0\\)</span> and <span class="math-inline">\\(\vec n \cdot \vec v = 4 + 2 - 6 = 0\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose your vector is <span class="math-inline">\\(\vec n = \begin{bmatrix} a \\\\ b \\\\ c \end{bmatrix}\\)</span>. Verify that both <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> satisfy

<div class="math-display">
$$
ax + by + cz = 0
$$
</div>

 Then, graph your equation on Desmos, [desmos.com/3d](https://www.desmos.com/3d).

<details markdown="1"><summary>Solution</summary>

Using <span class="math-inline">\\(\vec n = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}\\)</span> from part **a)**, the equation is

<div class="math-display">
$$
\boxed{x + 2y + 3z = 0}.
$$
</div>

 Substituting the components of <span class="math-inline">\\(\vec u\\)</span> gives <span class="math-inline">\\(5 + 2(-7) + 3(3) = 0\\)</span>, and substituting the components of <span class="math-inline">\\(\vec v\\)</span> gives <span class="math-inline">\\(4 + 2(1) + 3(-2) = 0\\)</span>. Thus, both vectors satisfy the equation. The graph in Desmos is the plane through the origin spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.
</details>
</div>
</div>

</div>

{% endraw %}
