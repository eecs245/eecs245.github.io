---
layout: page
title: "Lab 7: Null Space and the Rank-Nullity Theorem"
description: "Lab 7: Null Space and the Rank-Nullity Theorem activities."
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

# Lab 7: Null Space and the Rank-Nullity Theorem

**due** by the end of your lab section on Wednesday, October 21st, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab07/lab07.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab07/lab07-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete all activities and show your lab TA by the end of the lab section.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Null Space of a Matrix with Linearly Independent Columns](#activity-1-null-space-of-a-matrix-with-linearly-independent-columns)
- [Activity 2: Null Space from Column Relationships](#activity-2-null-space-from-column-relationships)
- [Activity 3: Four Spaces Warm-Up](#activity-3-four-spaces-warm-up)
- [Activity 4: Constructing a Matrix](#activity-4-constructing-a-matrix)
- [Activity 5: The Systems of Equations View](#activity-5-the-systems-of-equations-view)
- [Activity 6: Columns in a Null Space](#activity-6-columns-in-a-null-space)
- [Activity 7: Can the Column Space Equal the Null Space?](#activity-7-can-the-column-space-equal-the-null-space)

---

## Recap: Rank, Column Space, and Null Space

<ul class="assignment-list" markdown="1" data-item-count="5">
<li markdown="1">

For an <span class="math-inline">\\(n\times d\\)</span> matrix <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(\operatorname{colsp}(A)\\)</span> is a subspace of <span class="math-inline">\\(\mathbb R^n\\)</span>; it is the span of <span class="math-inline">\\(A\\)</span>'s columns.

</li>
<li markdown="1">

<span class="math-inline">\\(\operatorname{rank}(A)=\dim(\operatorname{colsp}(A))\\)</span>.

</li>
<li markdown="1">

<span class="math-inline">\\(\operatorname{nullsp}(A)=\lbrace\vec x\in\mathbb R^d:A\vec x=\vec 0\rbrace\\)</span>.

</li>
<li markdown="1">

The **Rank-Nullity Theorem** states that

<div class="math-display">
$$
\operatorname{rank}(A)+\dim(\operatorname{nullsp}(A))=d
$$
</div>

</li>
<li markdown="1">

<span class="math-inline">\\(\operatorname{rank}(A^T)=\operatorname{rank}(A)\\)</span>.

</li>
</ul>

---

## Activity 1: Null Space of a Matrix with Linearly Independent Columns

Let <span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 0 \\\\ 0 &amp; 4 \\\\ 1 &amp; 0 \end{bmatrix}\\)</span>. What is <span class="math-inline">\\(\text{nullsp}(A)\\)</span>?

<details markdown="1"><summary>Solution</summary>

The columns of <span class="math-inline">\\(A\\)</span> are linearly independent. So, the only way to combine them to get <span class="math-inline">\\(\vec 0\\)</span> is to use zero for both coefficients. This means

<div class="math-display">
$$
\boxed{\text{nullsp}(A)=\left\{\begin{bmatrix}0\\\\0\end{bmatrix}\right\}}
$$
</div>

 Notice that the null space contains the zero vector in <span class="math-inline">\\(\mathbb R^2\\)</span>, not <span class="math-inline">\\(\mathbb R^3\\)</span>, since <span class="math-inline">\\(A\\)</span> has two columns.
</details>

---

## Activity 2: Null Space from Column Relationships

Let <span class="math-inline">\\(X=\begin{bmatrix}1 &amp; 2 &amp; -1 &amp; 3 &amp; 4 &amp; 4 \\\\ 2 &amp; 5 &amp; -2 &amp; 7 &amp; 11 &amp; 10 \\\\ 4 &amp; 8 &amp; -4 &amp; 12 &amp; 16 &amp; 16\end{bmatrix}\\)</span>.

Note that <span class="math-inline">\\(X\\)</span>'s first two columns form a basis for its column space; verify this before proceeding.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blanks: <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

<details markdown="1"><summary>Solution</summary>

The Rank-Nullity Theorem tells us that

<div class="math-display">
$$
2+\dim(\text{nullsp}(X))=6
$$
</div>

 so <span class="math-inline">\\(\dim(\text{nullsp}(X))=4\\)</span>. Since <span class="math-inline">\\(X\\)</span> has six columns, the vectors in its null space have six components.

So, the blanks are <span class="math-inline">\\(\boxed{4}\\)</span> and <span class="math-inline">\\(\boxed{\mathbb R^6}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. <em>Hint: You should be able to answer this without solving equations.</em>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec v&#95;j\\)</span> be column <span class="math-inline">\\(j\\)</span> of <span class="math-inline">\\(X\\)</span>. From the columns, we can see that

<div class="math-display">
$$
\vec v_3=-\vec v_1,\qquad \vec v_4=\vec v_1+\vec v_2,\qquad
\vec v_5=-2\vec v_1+3\vec v_2,\qquad \vec v_6=2\vec v_2
$$
</div>

 Moving everything to one side in each equation gives a linear combination of the columns equal to <span class="math-inline">\\(\vec 0\\)</span>. The coefficients give us four vectors in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>:

<div class="math-display">
$$
\boxed{\left\{
\begin{bmatrix}1\\\\0\\\\1\\\\0\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}1\\\\1\\\\0\\\\-1\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}-2\\\\3\\\\0\\\\0\\\\-1\\\\0\end{bmatrix},
\begin{bmatrix}0\\\\2\\\\0\\\\0\\\\0\\\\-1\end{bmatrix}
\right\}}
$$
</div>

 These vectors are linearly independent: in components 3 through 6, each vector has a non-zero entry where the other three have zeros. Since the null space has dimension 4, these four vectors form a basis.
</details>

</div>
</div>

</div>

---

## Activity 3: Four Spaces Warm-Up

Let <span class="math-inline">\\(A\\)</span> be a <span class="math-inline">\\(7 \times 9\\)</span> matrix with rank <span class="math-inline">\\(5\\)</span>. For each space below, state its dimension and the space <span class="math-inline">\\(\mathbb R^k\\)</span> of which it is a subspace.

<table>
<thead>
<tr>
<th style="text-align: left;">Space</th>
<th style="text-align: center;">Dimension</th>
<th style="text-align: center;">Subspace of <span class="math-inline">\(\mathbb R^k\)</span> (state <span class="math-inline">\(k\)</span>)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{colsp}(A)\)</span></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{colsp}(A^T)\)</span></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{nullsp}(A)\)</span></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{nullsp}(A^T)\)</span></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

<details markdown="1"><summary>Solution</summary>

The completed table is:

<table>
<thead>
<tr>
<th style="text-align: left;">Space</th>
<th style="text-align: center;">Dimension</th>
<th style="text-align: center;">Subspace of</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{colsp}(A)\)</span></td>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><span class="math-inline">\(\mathbb R^7\)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{colsp}(A^T)\)</span></td>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><span class="math-inline">\(\mathbb R^9\)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{nullsp}(A)\)</span></td>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><span class="math-inline">\(\mathbb R^9\)</span></td>
</tr>
<tr>
<td style="text-align: left;"><span class="math-inline">\(\text{nullsp}(A^T)\)</span></td>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><span class="math-inline">\(\mathbb R^7\)</span></td>
</tr>
</tbody>
</table>

Both column spaces have dimension 5, since <span class="math-inline">\\(\text{rank}(A)=\text{rank}(A^T)=5\\)</span>. For the null spaces, apply the Rank-Nullity Theorem to <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(A^T\\)</span>:

<div class="math-display">
$$
\dim(\text{nullsp}(A))=9-5=4,\qquad \dim(\text{nullsp}(A^T))=7-5=2
$$
</div>

 Remember that <span class="math-inline">\\(A^T\\)</span> has shape <span class="math-inline">\\(9\times 7\\)</span>.
</details>

---

## Activity 4: Constructing a Matrix

Find a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\begin{bmatrix}3\\\\1\end{bmatrix}\in\text{colsp}(A)
\qquad\text{and}\qquad
\begin{bmatrix}1\\\\3\end{bmatrix}\in\text{nullsp}(A).
$$
</div>

<details markdown="1"><summary>Solution</summary>

The first condition tells us that <span class="math-inline">\\(A\\)</span> needs two rows, and the second tells us that it needs two columns.

Let's make the first column <span class="math-inline">\\(\begin{bmatrix}3\\\\1\end{bmatrix}\\)</span>. Then the first condition is automatically satisfied. For the second condition, we need the first column plus three times the second column to be <span class="math-inline">\\(\vec 0\\)</span>. So, one answer is

<div class="math-display">
$$
\boxed{A=\begin{bmatrix}3&-1\\\\1&-1/3\end{bmatrix}}
$$
</div>

 We can check that

<div class="math-display">
$$
A\begin{bmatrix}1\\\\3\end{bmatrix}=\begin{bmatrix}3-3\\\\1-1\end{bmatrix}=\vec 0
$$
</div>

 There are many other correct answers!
</details>

---

## Activity 5: The Systems of Equations View

Let <span class="math-inline">\\(A\\)</span> be an <span class="math-inline">\\(n \times d\\)</span> matrix of rank <span class="math-inline">\\(r\\)</span>, and suppose there exist vectors <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span> such that

<div class="math-display">
$$
A \vec x = \vec b
$$
</div>

does not have a solution (meaning no <span class="math-inline">\\(\vec x\\)</span> makes <span class="math-inline">\\(A \vec x = \vec b\\)</span>).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
What are all inequalities (<span class="math-inline">\\(&lt;\\)</span> or <span class="math-inline">\\(\le\\)</span>) that must be true between <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(d\\)</span>, and <span class="math-inline">\\(r\\)</span>?

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(A\vec x=\vec b\\)</span> has no solution, then <span class="math-inline">\\(\vec b\\)</span> is not in <span class="math-inline">\\(\text{colsp}(A)\\)</span>. So, the columns of <span class="math-inline">\\(A\\)</span> don't span all of <span class="math-inline">\\(\mathbb R^n\\)</span>, which means <span class="math-inline">\\(r&lt;n\\)</span>.

Also, <span class="math-inline">\\(A\\)</span> only has <span class="math-inline">\\(d\\)</span> columns, so it can't have more than <span class="math-inline">\\(d\\)</span> linearly independent columns. This gives

<div class="math-display">
$$
\boxed{r<n\qquad\text{and}\qquad r\le d}
$$
</div>

 We can't conclude whether <span class="math-inline">\\(n&lt;d\\)</span>, <span class="math-inline">\\(n=d\\)</span>, or <span class="math-inline">\\(n&gt;d\\)</span>; all three are possible.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
How do you know that <span class="math-inline">\\(A^T\vec y= \vec 0\\)</span> has solutions other than <span class="math-inline">\\(\vec y=\vec 0\\)</span>?

<details markdown="1"><summary>Solution</summary>

From part (a), <span class="math-inline">\\(r&lt;n\\)</span>. Since <span class="math-inline">\\(A^T\\)</span> has <span class="math-inline">\\(n\\)</span> columns and rank <span class="math-inline">\\(r\\)</span>, the Rank-Nullity Theorem gives

<div class="math-display">
$$
\dim(\text{nullsp}(A^T))=n-r>0
$$
</div>

 So, <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> contains more than just the zero vector. Any non-zero vector in this null space is a solution to <span class="math-inline">\\(A^T\vec y=\vec 0\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 6: Columns in a Null Space

Let <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> be non-zero <span class="math-inline">\\(6 \times 6\\)</span> matrices. Suppose <span class="math-inline">\\(\text{rank}(A)=4\\)</span>, and that every column of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Show that every row of <span class="math-inline">\\(A\\)</span> is orthogonal to every column of <span class="math-inline">\\(B\\)</span>.

<details markdown="1"><summary>Solution</summary>

Take any column <span class="math-inline">\\(\vec b\\)</span> of <span class="math-inline">\\(B\\)</span>. Since <span class="math-inline">\\(\vec b\in\text{nullsp}(A)\\)</span>, we know that <span class="math-inline">\\(A\vec b=\vec 0\\)</span>.

Each entry of <span class="math-inline">\\(A\vec b\\)</span> is the dot product of a row of <span class="math-inline">\\(A\\)</span> with <span class="math-inline">\\(\vec b\\)</span>. Since every entry is zero, every row of <span class="math-inline">\\(A\\)</span> is orthogonal to <span class="math-inline">\\(\vec b\\)</span>. This works for every column of <span class="math-inline">\\(B\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(AB\\)</span> and <span class="math-inline">\\(\text{rank}(AB)\\)</span>. Justify your answers.

<details markdown="1"><summary>Solution</summary>

Each column of <span class="math-inline">\\(AB\\)</span> is <span class="math-inline">\\(A\\)</span> times the corresponding column of <span class="math-inline">\\(B\\)</span>. All of these products are <span class="math-inline">\\(\vec 0\\)</span>, so

<div class="math-display">
$$
\boxed{AB=0_{6\times6}\qquad\text{and}\qquad\text{rank}(AB)=0}
$$
</div>

 The zero matrix has no linearly independent columns.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
What are the possible values of <span class="math-inline">\\(\text{rank}(B)\\)</span>? Explain why these are the only possibilities, and why each one is possible.

<details markdown="1"><summary>Solution</summary>

By the Rank-Nullity Theorem, <span class="math-inline">\\(\dim(\text{nullsp}(A))=6-4=2\\)</span>. Every column of <span class="math-inline">\\(B\\)</span> is in this two-dimensional space, so at most two columns of <span class="math-inline">\\(B\\)</span> can be linearly independent. Also, <span class="math-inline">\\(B\\)</span> is non-zero, so its rank can't be 0.

This leaves <span class="math-inline">\\(\boxed{\text{rank}(B)\in\lbrace1,2\rbrace}\\)</span>. Both are possible. Let <span class="math-inline">\\(\lbrace\vec u,\vec v\rbrace\\)</span> be a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

For rank 1, make every column of <span class="math-inline">\\(B\\)</span> equal to <span class="math-inline">\\(\vec u\\)</span>.

</li>
<li markdown="1">

For rank 2, make the first two columns <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and make the remaining columns <span class="math-inline">\\(\vec 0\\)</span>.

</li>
</ul>

Both choices satisfy all of the conditions in the question.
</details>

</div>
</div>

</div>

---

## Activity 7: Can the Column Space Equal the Null Space?

In each part, determine whether it's possible to find a matrix whose column space and null space are the same. If it is, give an example and show that it works. If not, explain why not.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Can you find a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(A\\)</span> such that <span class="math-inline">\\(\text{colsp}(A)=\text{nullsp}(A)\\)</span>?

<details markdown="1"><summary>Solution</summary>

Yes! One example is

<div class="math-display">
$$
\boxed{A=\begin{bmatrix}0&1\\\\0&0\end{bmatrix}}
$$
</div>

 Its column space is <span class="math-inline">\\(\text{span}\left\lbrace\begin{bmatrix}1\\\\0\end{bmatrix}\right\rbrace\\)</span>. To find its null space, note that

<div class="math-display">
$$
A\begin{bmatrix}x_1\\\\x_2\end{bmatrix}=\begin{bmatrix}x_2\\\\0\end{bmatrix}=\vec 0
\quad\Longleftrightarrow\quad x_2=0
$$
</div>

 So, its null space is also <span class="math-inline">\\(\text{span}\left\lbrace\begin{bmatrix}1\\\\0\end{bmatrix}\right\rbrace\\)</span>. Both spaces are the horizontal axis in <span class="math-inline">\\(\mathbb R^2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Can you find a <span class="math-inline">\\(3 \times 3\\)</span> matrix <span class="math-inline">\\(A\\)</span> such that <span class="math-inline">\\(\text{colsp}(A)=\text{nullsp}(A)\\)</span>?

<details markdown="1"><summary>Solution</summary>

No. If the column space and null space were equal, they would have the same dimension. Calling this dimension <span class="math-inline">\\(r\\)</span>, the Rank-Nullity Theorem would give

<div class="math-display">
$$
r+r=3\quad\Longrightarrow\quad r=\frac32
$$
</div>

 But the dimension of a subspace must be an integer, so this is impossible.
</details>
</div>
</div>

</div>

{% endraw %}
