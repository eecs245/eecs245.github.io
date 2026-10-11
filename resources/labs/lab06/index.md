---
layout: page
title: "Lab 6: Rank and Column Space"
description: "Lab 6: Rank and Column Space activities."
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

# Lab 6: Rank and Column Space

**due** by the end of your lab section on Wednesday, October 14th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab06/lab06.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab06/lab06-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete all activities and show your lab TA by the end of the lab section.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Matrix--Vector Practice](#activity-1-matrix--vector-practice)
- [Activity 2: Fundamentals and CR Decomposition](#activity-2-fundamentals-and-cr-decomposition)
- [Activity 3: Outer Products](#activity-3-outer-products)
- [Activity 4: Transforming a Triangle](#activity-4-transforming-a-triangle)
- [Activity 5: Can We Work Backward?](#activity-5-can-we-work-backward)

---

## Recap: Rank and Column Space ([Chapter 5.3](https://notes.eecs245.org/matrices/rank-and-column-space/))

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix. Then, <span class="math-inline">\\(\text{rank}(A)\\)</span> is the number of linearly independent columns of <span class="math-inline">\\(A\\)</span>.

<table>
<thead>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: center;"><strong>Notation</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: center;"><strong>Dimension</strong></th>
<th style="text-align: center;"><strong>Subspace of</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Column space</td>
<td style="text-align: center;"><span class="math-inline">\(\text{colsp}(A)\)</span></td>
<td style="text-align: left;">Span of the columns of <span class="math-inline">\(A\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(\text{rank}(A)\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(\mathbb{R}^n\)</span></td>
</tr>
<tr>
<td style="text-align: left;">Row space</td>
<td style="text-align: center;"><span class="math-inline">\(\text{colsp}(A^T)\)</span></td>
<td style="text-align: left;">Span of the rows of <span class="math-inline">\(A\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(\text{rank}(A)\)</span></td>
<td style="text-align: center;"><span class="math-inline">\(\mathbb{R}^d\)</span></td>
</tr>
</tbody>
</table>

**CR Decomposition**

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix with rank <span class="math-inline">\\(r\\)</span>. A CR decomposition of <span class="math-inline">\\(A\\)</span> is a product of two matrices <span class="math-inline">\\(C\\)</span> and <span class="math-inline">\\(R\\)</span>, where <span class="math-inline">\\(A = CR\\)</span> and:

<ul class="assignment-list" markdown="1" data-item-count="3">
<li markdown="1">

<span class="math-inline">\\(C\\)</span> is an <span class="math-inline">\\(n \times r\\)</span> matrix and <span class="math-inline">\\(R\\)</span> is a <span class="math-inline">\\(r \times d\\)</span> matrix

</li>
<li markdown="1">

<span class="math-inline">\\(C\\)</span> contains the linearly independent columns of <span class="math-inline">\\(A\\)</span>, selected left-to-right

</li>
<li markdown="1">

<span class="math-inline">\\(R\\)</span> tells how to "mix'' the columns of <span class="math-inline">\\(C\\)</span> (which are linearly independent) to reconstruct the columns of <span class="math-inline">\\(A\\)</span>

</li>
</ul>

---

## Activity 1: Matrix--Vector Practice

Compute each product, or explain why it is undefined. For each defined product, state the shape of the output. Show your arithmetic.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \begin{bmatrix}-8&amp;0&amp;0&amp;0&amp;0\\\\0&amp;\frac32&amp;0&amp;0&amp;0\\\\0&amp;0&amp;11&amp;0&amp;0\\\\0&amp;0&amp;0&amp;-5&amp;0\\\\0&amp;0&amp;0&amp;0&amp;7\end{bmatrix} \begin{bmatrix}3\\\\-4\\\\2\\\\6\\\\-3\end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \begin{bmatrix}12&amp;-7&amp;\frac12&amp;9\end{bmatrix}\begin{bmatrix}3\\\\-2\\\\8\\\\-4\end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \begin{bmatrix}-5&amp;8&amp;3&amp;12\\\\7&amp;-2&amp;6&amp;-9\end{bmatrix}\begin{bmatrix}4\\\\-1\\\\5\end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

**(a)** A diagonal matrix scales each coordinate separately:

<div class="math-display">
$$
\begin{bmatrix}-8(3)\\\\(3/2)(-4)\\\\11(2)\\\\-5(6)\\\\7(-3)\end{bmatrix}
=\boxed{\begin{bmatrix}-24\\\\-6\\\\22\\\\-30\\\\-21\end{bmatrix}}
$$
</div>

 The output is a <span class="math-inline">\\(5\times1\\)</span> column vector.

**(b)** This is a row-vector--column-vector product:

<div class="math-display">
$$
12(3)+(-7)(-2)+\tfrac12(8)+9(-4)=36+14+4-36=\boxed{18}
$$
</div>

 The output has shape <span class="math-inline">\\(1\times1\\)</span> and can be written as a scalar.

**(c)** **Undefined.** The matrix has four columns, but the input has only three entries. We would need one input entry for each of the four columns.
</details>

</div>
</div>

</div>

---

## Activity 2: Fundamentals and CR Decomposition

Let <span class="math-inline">\\(X=\begin{bmatrix}1 &amp; 2 &amp; -1 &amp; 3 &amp; 4 &amp; 4 \\\\ 2 &amp; 5 &amp; -2 &amp; 7 &amp; 11 &amp; 10 \\\\ 4 &amp; 8 &amp; -4 &amp; 12 &amp; 16 &amp; 16\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>. What is <span class="math-inline">\\(\text{rank}(X)\\)</span>? Why? <em>Hint: Column 5 is a linear combination of columns 1 and 2. With this fact, you should be able to answer this relatively quickly.</em>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec v&#95;1,\ldots,\vec v&#95;6\\)</span> denote the columns of <span class="math-inline">\\(X\\)</span>. The first two columns are not multiples of each other, so they are linearly independent. The remaining columns satisfy

<div class="math-display">
$$
\vec v_3=-\vec v_1,\qquad \vec v_4=\vec v_1+\vec v_2,\qquad
\vec v_5=-2\vec v_1+3\vec v_2,\qquad \vec v_6=2\vec v_2
$$
</div>

 Thus the first two columns span the column space, and

<div class="math-display">
$$
\boxed{\text{A basis is }\left\{\begin{bmatrix}1\\\\2\\\\4\end{bmatrix},\begin{bmatrix}2\\\\5\\\\8\end{bmatrix}\right\},\qquad\text{rank}(X)=2}
$$
</div>

</details>

Let's keep working with <span class="math-inline">\\(X = \begin{bmatrix}1 &amp; 2 &amp; -1 &amp; 3 &amp; 4 &amp; 4 \\\\ 2 &amp; 5 &amp; -2 &amp; 7 &amp; 11 &amp; 10 \\\\ 4 &amp; 8 &amp; -4 &amp; 12 &amp; 16 &amp; 16\end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blanks:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

<span class="math-inline">\\(\text{colsp}(X)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

</li>
<li markdown="1">

<span class="math-inline">\\(\text{colsp}(X^T)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

</li>
</ul>

<details markdown="1"><summary>Solution</summary>

Both spaces have dimension <span class="math-inline">\\(\text{rank}(X)=2\\)</span>. The columns of <span class="math-inline">\\(X\\)</span> lie in <span class="math-inline">\\(\mathbb R^3\\)</span>, while the columns of <span class="math-inline">\\(X^T\\)</span> lie in <span class="math-inline">\\(\mathbb R^6\\)</span>. Thus,

<div class="math-display">
$$
\boxed{\text{colsp}(X)\text{ is a 2-dimensional subspace of }\mathbb R^3}
$$
</div>



<div class="math-display">
$$
\boxed{\text{colsp}(X^T)\text{ is a 2-dimensional subspace of }\mathbb R^6}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find a CR decomposition of <span class="math-inline">\\(X\\)</span>. This shouldn't take very much work; review your work from part **a)** in finding a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Use the first two columns of <span class="math-inline">\\(X\\)</span> for <span class="math-inline">\\(C\\)</span>. Each column of <span class="math-inline">\\(R\\)</span> gives the coefficients needed to reconstruct the corresponding column of <span class="math-inline">\\(X\\)</span>:

<div class="math-display">
$$
\boxed{C=\begin{bmatrix}1&2\\\\2&5\\\\4&8\end{bmatrix},\qquad
R=\begin{bmatrix}1&0&-1&1&-2&0\\\\0&1&0&1&3&2\end{bmatrix}}
$$
</div>

 For example, the fifth column of <span class="math-inline">\\(R\\)</span> is <span class="math-inline">\\(\begin{bmatrix}-2\\\\3\end{bmatrix}\\)</span> because <span class="math-inline">\\(\vec v&#95;5=-2\vec v&#95;1+3\vec v&#95;2\\)</span>. Multiplying verifies

<div class="math-display">
$$
CR=\begin{bmatrix}1&2&-1&3&4&4\\\\2&5&-2&7&11&10\\\\4&8&-4&12&16&16\end{bmatrix}=X
$$
</div>

 <span class="math-inline">\\(C\\)</span> has shape <span class="math-inline">\\(3\times2\\)</span> and <span class="math-inline">\\(R\\)</span> has shape <span class="math-inline">\\(2\times6\\)</span>.
</details>

The key idea being assessed here is that in <span class="math-inline">\\(A = CR\\)</span>, the columns of <span class="math-inline">\\(C\\)</span> are linearly independent and a basis for <span class="math-inline">\\(\text{colsp}(A)\\)</span>, while the rows of <span class="math-inline">\\(R\\)</span> are linearly independent and a basis for <span class="math-inline">\\(\text{colsp}(A^T)\\)</span>!

</div>
</div>

</div>

---

## Activity 3: Outer Products

Recall that in lecture, we mentioned that you can use the transpose operation to write the dot product of two vectors in <span class="math-inline">\\(\mathbb R^n\\)</span> as a matrix multiplication. For example, let

<div class="math-display">
$$
\vec u=\begin{bmatrix}1\\\\2\\\\-1\\\\3\end{bmatrix},\qquad
\vec v=\begin{bmatrix}2\\\\0\\\\4\\\\-1\end{bmatrix}
$$
</div>

 Then,

<div class="math-display">
$$
\vec v^T\vec u=
\begin{bmatrix}2&0&4&-1\end{bmatrix}\begin{bmatrix}1\\\\2\\\\-1\\\\3\end{bmatrix}
=2(1)+0(2)+4(-1)+(-1)(3)=-5=\vec v\cdot\vec u
$$
</div>

 A related operation that looks similar but does something very different is the **outer product** of two vectors: <span class="math-inline">\\(\vec u\vec v^T\\)</span> instead of <span class="math-inline">\\(\vec v^T\vec u\\)</span>. For the same vectors,

<div class="math-display">
$$
\vec u\vec v^T=
\begin{bmatrix}1\\\\2\\\\-1\\\\3\end{bmatrix}\begin{bmatrix}2&0&4&-1\end{bmatrix}
=\begin{bmatrix}2&0&4&-1\\\\4&0&8&-2\\\\-2&0&-4&1\\\\6&0&12&-3\end{bmatrix}
$$
</div>

 The dot product is a scalar; the outer product here is a <span class="math-inline">\\(4\times4\\)</span> matrix.

Suppose <span class="math-inline">\\(A = \vec u \vec v^T + \vec w \vec z^T\\)</span>, where <span class="math-inline">\\(\vec u, \vec v, \vec w, \vec z \in \mathbb{R}^n\\)</span> are non-zero vectors.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
What is <span class="math-inline">\\(\text{rank}(\vec u \vec v^T)\\)</span>?

<details markdown="1"><summary>Solution</summary>

The <span class="math-inline">\\(j\\)</span>th column of <span class="math-inline">\\(\vec u\vec v^T\\)</span> is <span class="math-inline">\\(v&#95;j\vec u\\)</span>, so every column is a multiple of <span class="math-inline">\\(\vec u\\)</span>. Since <span class="math-inline">\\(\vec v\ne\vec0\\)</span>, at least one <span class="math-inline">\\(v&#95;j\\)</span> is nonzero; because <span class="math-inline">\\(\vec u\ne\vec0\\)</span>, that column is nonzero. Therefore,

<div class="math-display">
$$
\boxed{\text{rank}(\vec u\vec v^T)=1}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Under what conditions is <span class="math-inline">\\(\text{rank}(A) = 2\\)</span>? What about <span class="math-inline">\\(\text{rank}(A) &lt; 2\\)</span>? <em>Hint: First, think about what happens when multiplying <span class="math-inline">\\(A\\)</span> by a vector <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span>. Can you write this as a linear combination of some other vectors? The case for <span class="math-inline">\\(\text{rank}(A) = 2\\)</span> is more complicated than "<span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> are linearly independent."</em>

<details markdown="1"><summary>Solution</summary>

For every <span class="math-inline">\\(\vec x\in\mathbb R^n\\)</span>,

<div class="math-display">
$$
A\vec x=(\vec v^T\vec x)\vec u+(\vec z^T\vec x)\vec w
$$
</div>

 so <span class="math-inline">\\(\text{colsp}(A)\subseteq\text{span}(\lbrace\vec u,\vec w\rbrace)\\)</span> and <span class="math-inline">\\(\text{rank}(A)\le2\\)</span>.

**Rank 2:** This occurs if and only if both pairs <span class="math-inline">\\(\lbrace\vec u,\vec w\rbrace\\)</span> and <span class="math-inline">\\(\lbrace\vec v,\vec z\rbrace\\)</span> are linearly independent. If either pair is dependent, the columns or rows of <span class="math-inline">\\(A\\)</span> span at most a line, so rank 2 is impossible.

Conversely, suppose both pairs are independent. Then <span class="math-inline">\\(\vec v^T\vec x=c\\)</span> and <span class="math-inline">\\(\vec z^T\vec x=d\\)</span> can be solved for every <span class="math-inline">\\(c,d\in\mathbb R\\)</span>, since the two-row coefficient matrix has rank 2 and column space <span class="math-inline">\\(\mathbb R^2\\)</span>. Therefore every <span class="math-inline">\\(c\vec u+d\vec w\\)</span> is an output of <span class="math-inline">\\(A\\)</span>. Its column space is exactly <span class="math-inline">\\(\text{span}(\lbrace\vec u,\vec w\rbrace)\\)</span>, which has dimension 2.

**Rank less than 2:** This occurs if and only if at least one of those pairs is dependent. The rank is 1 unless the two outer products cancel, in which case it is 0. More explicitly, because all four vectors are nonzero,

<div class="math-display">
$$
A=0\quad\Longleftrightarrow\quad
\vec w=c\vec u\text{ and }\vec z=-\frac1c\vec v
\quad\text{for some }c\ne0
$$
</div>

 For example, <span class="math-inline">\\(\vec w=\vec u\\)</span> and <span class="math-inline">\\(\vec z=-\vec v\\)</span> give <span class="math-inline">\\(A=0\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 4: Transforming a Triangle

The act of multiplying a vector by a matrix performs a **linear transformation** of the vector.

Suppose <span class="math-inline">\\(\vec x=\begin{bmatrix}x\\\\y\end{bmatrix}\\)</span>. Multiplying <span class="math-inline">\\(\vec x\\)</span> by the rotation matrix

<div class="math-display">
$$
R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\\\sin\theta&\cos\theta\end{bmatrix}
$$
</div>

 gives

<div class="math-display">
$$
R_\theta\vec x=\begin{bmatrix}\cos\theta&-\sin\theta\\\\\sin\theta&\cos\theta\end{bmatrix}\begin{bmatrix}x\\\\y\end{bmatrix}
=\begin{bmatrix}x\cos\theta-y\sin\theta\\\\x\sin\theta+y\cos\theta\end{bmatrix},
$$
</div>

 which rotates <span class="math-inline">\\(\vec x\\)</span> counterclockwise by <span class="math-inline">\\(\theta\\)</span> about the origin.

Consider the triangle with vertices <span class="math-inline">\\(\begin{bmatrix}0\\\\0\end{bmatrix}\\)</span>, <span class="math-inline">\\(\begin{bmatrix}4\\\\0\end{bmatrix}\\)</span>, and <span class="math-inline">\\(\begin{bmatrix}0\\\\2\end{bmatrix}\\)</span>.

<img src="imgs/tikz-d33c33a3113c.png" alt="Figure from the assignment PDF" style="width: 60%; max-width: 100%;">

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(Q=R&#95;{45^\circ}\\)</span>. Write <span class="math-inline">\\(Q\\)</span> explicitly, then multiply all three original vertices by <span class="math-inline">\\(Q\\)</span>, showing your arithmetic. Draw the corresponding triangle and label its vertices.

<details markdown="1"><summary>Solution</summary>

The rotation matrix is

<div class="math-display">
$$
Q=\frac1{\sqrt2}\begin{bmatrix}1&-1\\\\1&1\end{bmatrix}
$$
</div>

 Multiplying each vertex gives

<div class="math-display">
$$
Q\begin{bmatrix}0\\\\0\end{bmatrix}=\begin{bmatrix}0\\\\0\end{bmatrix},\qquad
Q\begin{bmatrix}4\\\\0\end{bmatrix}=\frac1{\sqrt2}\begin{bmatrix}4\\\\4\end{bmatrix}=\begin{bmatrix}2\sqrt2\\\\2\sqrt2\end{bmatrix},\qquad
Q\begin{bmatrix}0\\\\2\end{bmatrix}=\frac1{\sqrt2}\begin{bmatrix}-2\\\\2\end{bmatrix}=\begin{bmatrix}-\sqrt2\\\\\sqrt2\end{bmatrix}
$$
</div>

 Connect these three points to draw the rotated triangle.

<div style="text-align: center;">
<img src="imgs/triangle-rotate.png" alt="image" style="width: 65%; max-width: 100%;">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(D=\begin{bmatrix}2&amp;0\\\\0&amp;1\end{bmatrix}\\)</span>. Since <span class="math-inline">\\(D\begin{bmatrix}x\\\\y\end{bmatrix}=\begin{bmatrix}2x\\\\y\end{bmatrix}\\)</span>, it stretches a point horizontally by a factor of <span class="math-inline">\\(2\\)</span>. Multiply all three original vertices by <span class="math-inline">\\(D\\)</span>, showing your arithmetic. Draw the corresponding triangle and label its vertices.

<details markdown="1"><summary>Solution</summary>

Multiplication doubles each horizontal coordinate:

<div class="math-display">
$$
D\begin{bmatrix}0\\\\0\end{bmatrix}=\begin{bmatrix}0\\\\0\end{bmatrix},\qquad
D\begin{bmatrix}4\\\\0\end{bmatrix}=\begin{bmatrix}2(4)\\\\0\end{bmatrix}=\begin{bmatrix}8\\\\0\end{bmatrix},\qquad
D\begin{bmatrix}0\\\\2\end{bmatrix}=\begin{bmatrix}2(0)\\\\2\end{bmatrix}=\begin{bmatrix}0\\\\2\end{bmatrix}
$$
</div>

 Connect these points to draw the horizontally stretched triangle.

<div style="text-align: center;">
<img src="imgs/triangle-stretch.png" alt="image" style="width: 65%; max-width: 100%;">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Compute <span class="math-inline">\\(QD\\)</span>. For each original vertex <span class="math-inline">\\(\vec x\\)</span>, multiply out <span class="math-inline">\\((QD)\vec x\\)</span>. Draw the resulting triangle on a coordinate plane and label all three vertices. Explain why <span class="math-inline">\\(QD\\)</span> stretches first and then rotates.

<details markdown="1"><summary>Solution</summary>

Stretching first gives <span class="math-inline">\\(D\vec x\\)</span>; rotating that result gives <span class="math-inline">\\(Q(D\vec x)\\)</span>. Thus the combined matrix is

<div class="math-display">
$$
\boxed{QD=\frac1{\sqrt2}\begin{bmatrix}2&-1\\\\2&1\end{bmatrix}}
$$
</div>

 The three vertices become

<div class="math-display">
$$
\begin{bmatrix}0\\\\0\end{bmatrix}\mapsto\begin{bmatrix}0\\\\0\end{bmatrix},\quad
\begin{bmatrix}4\\\\0\end{bmatrix}\mapsto\begin{bmatrix}4\sqrt2\\\\4\sqrt2\end{bmatrix},\quad
\begin{bmatrix}0\\\\2\end{bmatrix}\mapsto\begin{bmatrix}-\sqrt2\\\\\sqrt2\end{bmatrix}
$$
</div>

<div style="text-align: center;">
<img src="imgs/triangle-stretch-rotate.png" alt="image" style="width: 78%; max-width: 100%;">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Compute <span class="math-inline">\\(DQ\\)</span>. For each original vertex <span class="math-inline">\\(\vec x\\)</span>, multiply out <span class="math-inline">\\((DQ)\vec x\\)</span>. Draw the resulting triangle on a second coordinate plane with the same scale and label all three vertices. Which operation happens first? How do the triangles for <span class="math-inline">\\(QD\\)</span> and <span class="math-inline">\\(DQ\\)</span> differ?

<details markdown="1"><summary>Solution</summary>

Rotating first and stretching second gives

<div class="math-display">
$$
\boxed{DQ=\frac1{\sqrt2}\begin{bmatrix}2&-2\\\\1&1\end{bmatrix}}
$$
</div>

 Now the vertices become

<div class="math-display">
$$
\begin{bmatrix}0\\\\0\end{bmatrix}\mapsto\begin{bmatrix}0\\\\0\end{bmatrix},\quad
\begin{bmatrix}4\\\\0\end{bmatrix}\mapsto\begin{bmatrix}4\sqrt2\\\\2\sqrt2\end{bmatrix},\quad
\begin{bmatrix}0\\\\2\end{bmatrix}\mapsto\begin{bmatrix}-2\sqrt2\\\\\sqrt2\end{bmatrix}
$$
</div>

<div style="text-align: center;">
<img src="imgs/triangle-rotate-stretch.png" alt="image" style="width: 78%; max-width: 100%;">
</div>

The first triangle is taller and narrower. It still has a right angle at the origin: stretching along the original coordinate axes preserves that right angle, and rotating preserves all angles. In the second triangle, stretching after rotation changes the angle between the tilted sides, so the angle at the origin is no longer a right angle.
</details>

Note that the last page of this worksheet is empty if you need extra space to draw.

</div>
</div>

</div>

---

## Activity 5: Can We Work Backward?

Let <span class="math-inline">\\(\displaystyle A=\begin{bmatrix}4&amp;-6\\\\-2&amp;3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find two different vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(A\vec u=A\vec v=\begin{bmatrix}12\\\\-6\end{bmatrix}\\)</span>.

<details markdown="1"><summary>Solution</summary>

The system is

<div class="math-display">
$$
4x-6y=12,\qquad -2x+3y=-6
$$
</div>

 The second equation is <span class="math-inline">\\(-1/2\\)</span> times the first, so there is only one independent restriction. Solving gives <span class="math-inline">\\(x=3+\tfrac32y\\)</span>. Choosing <span class="math-inline">\\(y=0\\)</span> and <span class="math-inline">\\(y=2\\)</span>, for example, gives

<div class="math-display">
$$
\boxed{\vec u=\begin{bmatrix}3\\\\0\end{bmatrix},\qquad
\vec v=\begin{bmatrix}6\\\\2\end{bmatrix}}
$$
</div>

 Indeed, both products are <span class="math-inline">\\(\begin{bmatrix}12\\\\-6\end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Is there a vector <span class="math-inline">\\(\vec x\\)</span> such that <span class="math-inline">\\(A\vec x=\begin{bmatrix}12\\\\-5\end{bmatrix}\\)</span>? In your answer, reference <span class="math-inline">\\(\text{colsp}(A)\\)</span>.

<details markdown="1"><summary>Solution</summary>

**No.** The second column is <span class="math-inline">\\(-3/2\\)</span> times the first, so every output is in

<div class="math-display">
$$
\operatorname{span}\!\left(\begin{bmatrix}4\\\\-2\end{bmatrix}\right)
$$
</div>

 Every vector in this span has second entry equal to <span class="math-inline">\\(-1/2\\)</span> times its first entry. An output with first entry <span class="math-inline">\\(12\\)</span> must have second entry <span class="math-inline">\\(-6\\)</span>, not <span class="math-inline">\\(-5\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Using your <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> from part (a), find a nonzero vector <span class="math-inline">\\(\vec w\\)</span> such that <span class="math-inline">\\(A\vec w=\vec0\\)</span>.

<details markdown="1"><summary>Solution</summary>

Subtract the two inputs from part (a):

<div class="math-display">
$$
\boxed{\vec v-\vec u=\begin{bmatrix}3\\\\2\end{bmatrix}}
$$
</div>

 This vector is nonzero, and linearity gives

<div class="math-display">
$$
A(\vec v-\vec u)=A\vec v-A\vec u
=\begin{bmatrix}12\\\\-6\end{bmatrix}-\begin{bmatrix}12\\\\-6\end{bmatrix}=\vec0
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
