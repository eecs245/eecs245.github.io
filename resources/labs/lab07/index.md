---
layout: page
title: "Lab 7: Null Space and Inverses"
description: "Lab 7: Null Space and Inverses activities."
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

# Lab 7: Null Space and Inverses

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

- [Activity 1: PrairieLearn Practice Problems](#activity-1-prairielearn-practice-problems)
- [Activity 2: Null Space of a Matrix with Linearly Independent Columns](#activity-2-null-space-of-a-matrix-with-linearly-independent-columns)
- [Activity 3: Null Space from Column Relationships](#activity-3-null-space-from-column-relationships)
- [Activity 4: The Systems of Equations View](#activity-4-the-systems-of-equations-view)
- [Activity 5: Symbolic Inverses](#activity-5-symbolic-inverses)
- [Activity 6: Basics of Invertibility](#activity-6-basics-of-invertibility)
- [Activity 7: Invertibility of $X^TX$](#activity-7-invertibility-of-xtx)
- [Activity 8: Doing Things Differently](#activity-8-doing-things-differently)

---

## Recap: Rank, Column Space, Null Space, and Inverses

<ul class="assignment-list" markdown="1" data-item-count="4">
<li markdown="1">

For an <span class="math-inline">\\(n\times d\\)</span> matrix <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(\operatorname{colsp}(A)\subseteq\mathbb R^n\\)</span> has dimension <span class="math-inline">\\(\operatorname{rank}(A)\\)</span>.

</li>
<li markdown="1">

<span class="math-inline">\\(\operatorname{nullsp}(A)=\lbrace\vec x\in\mathbb R^d:A\vec x=\vec 0\rbrace\\)</span>, and <span class="math-inline">\\(\dim(\operatorname{nullsp}(A))=d-\operatorname{rank}(A)\\)</span>.

</li>
<li markdown="1">

<span class="math-inline">\\(\operatorname{rank}(A^T)=\operatorname{rank}(A)\\)</span>.

</li>
<li markdown="1">

A square matrix <span class="math-inline">\\(A\\)</span> is invertible if and only if it has full rank. Its inverse satisfies <span class="math-inline">\\(AA^{-1}=A^{-1}A=I\\)</span>.

</li>
</ul>

---

## Activity 1: PrairieLearn Practice Problems

We're testing out a new website for practicing linear algebra problems: PrairieLearn.

Click [**this link**](https://us.prairielearn.com/pl/course_instance/217357) to access the relevant problems for this activity. It consists of 6 problems, each worth 1 point. The numbers in the problems are randomized; everyone will receive slightly different problems.

To get credit for Activity 1, you must **eventually** correctly answer all 6 problems, earning a score of 6/6. If you answer a problem incorrectly, click "New Variant" to generate a new version and then try again. There is no penalty for answering a problem incorrectly, as long as you eventually get it correct.

To be clear, you don't need to include anything in your PDF for Activity 1; we will manually verify that you've finished all 6 problems.

If you have trouble accessing PrairieLearn, message Suraj on Slack.

---

## Activity 2: Null Space of a Matrix with Linearly Independent Columns

Let <span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 0 \\\\ 0 &amp; 4 \\\\ 1 &amp; 0 \end{bmatrix}\\)</span>. What is <span class="math-inline">\\(\text{nullsp}(A)\\)</span>?

<details markdown="1"><summary>Solution</summary>

The columns of <span class="math-inline">\\(A\\)</span> are linearly independent, so the only linear combination that gives <span class="math-inline">\\(\vec0\\)</span> has both coefficients zero. Equivalently,

<div class="math-display">
$$
A\begin{bmatrix}x_1\\\\x_2\end{bmatrix}=\begin{bmatrix}3x_1\\\\4x_2\\\\x_1\end{bmatrix}=\vec0
\quad\Longrightarrow\quad x_1=x_2=0
$$
</div>

 Thus <span class="math-inline">\\(\boxed{\text{nullsp}(A)=\left\lbrace\begin{bmatrix}0\\\\0\end{bmatrix}\right\rbrace}\\)</span>.
</details>

---

## Activity 3: Null Space from Column Relationships

Let <span class="math-inline">\\(X=\begin{bmatrix}1 &amp; 2 &amp; -1 &amp; 3 &amp; 4 &amp; 4 \\\\ 2 &amp; 5 &amp; -2 &amp; 7 &amp; 11 &amp; 10 \\\\ 4 &amp; 8 &amp; -4 &amp; 12 &amp; 16 &amp; 16\end{bmatrix}\\)</span>.

This is the matrix from Lab 6. Recall that its first two columns form a basis for its column space and its rank is 2.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blanks: <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

<details markdown="1"><summary>Solution</summary>

From [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/), the **rank-nullity theorem** states that for any <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(X\\)</span>,

<div class="math-display">
$$
\text{rank}(X) + \dim(\text{nullsp}(X)) = \underbrace{d}_{\text{# columns in } X}
$$
</div>

The rank of <span class="math-inline">\\(X\\)</span> was found to be <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(X\\)</span> has <span class="math-inline">\\(6\\)</span> columns, so

<div class="math-display">
$$
2 + \dim(\text{nullsp}(X)) = 6
$$
</div>



<div class="math-display">
$$
\dim(\text{nullsp}(X)) = 6 - 2 = 4
$$
</div>

By definition, <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is the set of all vectors <span class="math-inline">\\(\vec{v} \in \mathbb{R}^6\\)</span> such that <span class="math-inline">\\(X\vec{v} = \vec{0}\\)</span>. Therefore, it is a subspace of <span class="math-inline">\\(\mathbb{R}^6\\)</span>.

<div class="math-display">
$$
\boxed{
\text{nullsp}(X) \text{ is a 4-dimensional subspace of } \mathbb{R}^6
}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. <em>Hint: You should be able to answer this without solving equations.</em>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec v&#95;j\\)</span> be column <span class="math-inline">\\(j\\)</span> of <span class="math-inline">\\(X\\)</span>. The relationships

<div class="math-display">
$$
\vec v_1+\vec v_3=\vec0,\quad
\vec v_1+\vec v_2-\vec v_4=\vec0,\quad
-2\vec v_1+3\vec v_2-\vec v_5=\vec0,\quad
2\vec v_2-\vec v_6=\vec0
$$
</div>

 give the following four vectors in the null space:

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

 They are linearly independent: looking at coordinates 3, 4, 5, and 6 in a linear combination equal to zero forces all four coefficients to be zero. Since the null space has dimension 4, these four independent vectors form a basis.
</details>

</div>
</div>

</div>

---

## Activity 4: The Systems of Equations View

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

If <span class="math-inline">\\(A\vec{x} = \vec{b}\\)</span> has no solution for some <span class="math-inline">\\(\vec{b}\\)</span>, then <span class="math-inline">\\(\vec{b}\\)</span> does not lie in <span class="math-inline">\\(\text{colsp}(A)\\)</span>. Thus, the column space of <span class="math-inline">\\(A\\)</span> is a proper subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, meaning its dimension (the rank) is strictly less than <span class="math-inline">\\(n\\)</span>:

<div class="math-display">
$$
r < n
$$
</div>

 By general rank properties, rank cannot exceed either the number of rows or columns:

<div class="math-display">
$$
r \le n, \quad r \le d
$$
</div>

 Combining these gives:

<div class="math-display">
$$
\boxed{r < n \quad \text{and} \quad r \le d}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
How do you know that <span class="math-inline">\\(A^T\vec y= \vec 0\\)</span> has solutions other than <span class="math-inline">\\(\vec y=\vec 0\\)</span>?

<details markdown="1"><summary>Solution</summary>

By the rank-nullity theorem,

<div class="math-display">
$$
\text{rank}(A^T) + \dim(\text{nullsp}(A^T)) = \underbrace{n}_{\text{# columns in } A^T}
$$
</div>

 and since <span class="math-inline">\\(\text{rank}(A^T)=r&lt;n\\)</span>, it follows that <span class="math-inline">\\(\dim(\text{nullsp}(A^T))=n-r&gt;0\\)</span>. Therefore, <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> contains non-zero vectors, so there must exist some <span class="math-inline">\\(\vec{y} \ne \vec{0}\\)</span> such that <span class="math-inline">\\(A^T \vec{y} = \vec{0}\\)</span>.
</details>

</div>
</div>

</div>

---

## Activity 5: Symbolic Inverses

Given that <span class="math-inline">\\(A\\)</span> is an invertible <span class="math-inline">\\(n \times n\\)</span> matrix that satisfies <span class="math-inline">\\(A^4 - 3A^2 + 2A - 4I = 0\\)</span>, find an expression for <span class="math-inline">\\(A^{-1}\\)</span> in terms of <span class="math-inline">\\(A\\)</span>.

<details markdown="1"><summary>Solution</summary>

The goal is to find another matrix <span class="math-inline">\\(B\\)</span> such that <span class="math-inline">\\(AB = BA = I\\)</span>. We can do this by isolating the identity matrix, <span class="math-inline">\\(I\\)</span>, and then trying to write the other side of the equation as <span class="math-inline">\\(A\\)</span> times some other matrix.

<div class="math-display">
$$
\begin{align*}
A^4 - 3A^2 + 2A - 4I &= 0 \\\\
A^4 - 3A^2 + 2A &= 4I \\\\
A(A^3 - 3A + 2I) &= 4I \\\\
A \left( \frac{1}{4}(A^3 - 3A + 2I) \right) &= I
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\boxed{A^{-1} = \frac{1}{4}(A^3 - 3A + 2I)}\\)</span>.

Because <span class="math-inline">\\(A\\)</span> is invertible, multiplying <span class="math-inline">\\(A(A^3-3A+2I)=4I\\)</span> on the left by <span class="math-inline">\\(A^{-1}\\)</span> proves the formula. Also, any polynomial in <span class="math-inline">\\(A\\)</span> commutes with <span class="math-inline">\\(A\\)</span>, so the displayed candidate satisfies both <span class="math-inline">\\(AB=I\\)</span> and <span class="math-inline">\\(BA=I\\)</span>.
</details>

---

## Activity 6: Basics of Invertibility

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix. State as many of the equivalent conditions for invertibility as you can.

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix, then <span class="math-inline">\\(A\\)</span> is invertible if and only if:

<ul class="assignment-list" markdown="1" data-item-count="5">
<li markdown="1">

<span class="math-inline">\\(\text{rank}(A) = n\\)</span>

</li>
<li markdown="1">

<span class="math-inline">\\(A\\)</span>'s columns are linearly independent (and hence <span class="math-inline">\\(\text{colsp}(A) = \mathbb{R}^n\\)</span>)

</li>
<li markdown="1">

<span class="math-inline">\\(A\\)</span>'s rows are linearly independent (and hence <span class="math-inline">\\(\text{rowsp}(A) = \text{colsp}(A^T) = \mathbb{R}^n\\)</span>)

</li>
<li markdown="1">

<span class="math-inline">\\(A\\)</span>'s null space is only the zero vector, i.e. <span class="math-inline">\\(\text{nullsp}(A) = \lbrace\vec 0\rbrace\\)</span>

</li>
<li markdown="1">

<span class="math-inline">\\(\text{det}(A) \neq 0\\)</span>

</li>
</ul>
</details>

---

## Activity 7: Invertibility of <span class="math-inline">\\(X^TX\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(X\\)</span> be an <span class="math-inline">\\(n \times d\\)</span> matrix. Fill in the blanks: <span class="math-inline">\\(X^TX\\)</span> is invertible if and only if <span class="math-inline">\\(X\\)</span>'s columns are \_\_\_\_.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(X^TX\\)</span> is invertible if and only if <span class="math-inline">\\(X\\)</span>'s columns are **linearly independent**. This is because <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^TX)\\)</span>, as we proved in [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-rank-of-x-tx), and a square matrix is invertible if and only if its rank is equal to its number of columns.

For <span class="math-inline">\\(\text{rank}(X^TX) = d\\)</span>, we need <span class="math-inline">\\(\text{rank}(X) = d\\)</span>, meaning <span class="math-inline">\\(X\\)</span>'s columns must be linearly independent.
</details>

</div>
</div>

</div>

---

## Activity 8: Doing Things Differently

Matrix multiplication does not always behave like multiplication of numbers. All matrices below are <span class="math-inline">\\(2\times2\\)</span>, and all vectors are in <span class="math-inline">\\(\mathbb R^2\\)</span>. Justify each answer. For a counterexample, give specific matrices or vectors and show the relevant products.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
If <span class="math-inline">\\(B\vec v=\vec0\\)</span>, must <span class="math-inline">\\(AB\vec v=\vec0\\)</span>? If <span class="math-inline">\\(AB\vec v=\vec0\\)</span>, must <span class="math-inline">\\(B\vec v=\vec0\\)</span>? Address both directions.

<details markdown="1"><summary>Solution</summary>

Yes in the first direction: <span class="math-inline">\\(AB\vec v=A(B\vec v)=A\vec0=\vec0\\)</span>. The converse is false. Take

<div class="math-display">
$$
A=\begin{bmatrix}1&0\\\\0&0\end{bmatrix},\quad B=I,\quad\vec v=\begin{bmatrix}0\\\\1\end{bmatrix}
$$
</div>

 Then <span class="math-inline">\\(B\vec v=\vec v\ne\vec0\\)</span>, but <span class="math-inline">\\(AB\vec v=A\vec v=\vec0\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Can <span class="math-inline">\\(AB=0&#95;{2\times2}\\)</span> even when neither <span class="math-inline">\\(A\\)</span> nor <span class="math-inline">\\(B\\)</span> is the zero matrix? Give an example or explain why it is impossible.

<details markdown="1"><summary>Solution</summary>

Yes. For example,

<div class="math-display">
$$
A=\begin{bmatrix}1&0\\\\0&0\end{bmatrix},\qquad
B=\begin{bmatrix}0&0\\\\0&1\end{bmatrix},\qquad
AB=\begin{bmatrix}0&0\\\\0&0\end{bmatrix}
$$
</div>

 Both factors are nonzero.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Expand <span class="math-inline">\\((A+B)^2\\)</span> using distributivity, keeping the factors in their original order. Is it always equal to <span class="math-inline">\\(A^2+2AB+B^2\\)</span>? If not, give a counterexample.

<details markdown="1"><summary>Solution</summary>

Distributivity gives

<div class="math-display">
$$
(A+B)^2=A^2+AB+BA+B^2
$$
</div>

 This equals <span class="math-inline">\\(A^2+2AB+B^2\\)</span> if and only if <span class="math-inline">\\(AB=BA\\)</span>, which need not hold. For example, take

<div class="math-display">
$$
A=\begin{bmatrix}1&0\\\\0&0\end{bmatrix},\qquad B=\begin{bmatrix}0&1\\\\0&0\end{bmatrix}
$$
</div>

 Then <span class="math-inline">\\(A^2=A\\)</span>, <span class="math-inline">\\(B^2=0\\)</span>, <span class="math-inline">\\(AB=B\\)</span>, and <span class="math-inline">\\(BA=0\\)</span>. Hence

<div class="math-display">
$$
(A+B)^2=\begin{bmatrix}1&1\\\\0&0\end{bmatrix}
\ne\begin{bmatrix}1&2\\\\0&0\end{bmatrix}=A^2+2AB+B^2
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
