---
layout: page
title: "Lab 6: Rank, Column Space, Null Space, and Inverses"
description: "Lab 6: Rank, Column Space, Null Space, and Inverses activities."
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

# Lab 6: Rank, Column Space, Null Space, and Inverses

**due** for completion at 11:59PM Ann Arbor Time on Wednesday, May 27th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab06/lab06.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab06/lab06-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Null Space of a Matrix with Linearly Independent Columns](#activity-1-null-space-of-a-matrix-with-linearly-independent-columns)
- [Activity 2: Fundamentals](#activity-2-fundamentals)
- [Activity 3: Outer Products](#activity-3-outer-products)
- [Activity 4: The Systems of Equations View](#activity-4-the-systems-of-equations-view)
- [Activity 5: Symbolic Inverses](#activity-5-symbolic-inverses)
- [Activity 6: Basics of Invertibility](#activity-6-basics-of-invertibility)
- [Activity 7: Programming](#activity-7-programming)

---

**Note**: You may find it helpful to work on the first few problems of Homework 5 before starting this lab.

**Recap: Rank, Column Space, and Null Space** ([Chapter 5.3](https://notes.eecs245.org/matrices/rank-and-column-space/) and [5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/))

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix. Then, <span class="math-inline">\\(\text{rank}(A)\\)</span> is the number of linearly independent columns of <span class="math-inline">\\(A\\)</span>.

|  | **Notation** | **Description** | **Dimension** | **Subspace of** |
|:---|:--:|:---|:--:|:--:|
| Column space | <span class="math-inline">\\(\text{colsp}(A)\\)</span> | Span of the columns of <span class="math-inline">\\(A\\)</span> | <span class="math-inline">\\(\text{rank}(A)\\)</span> | <span class="math-inline">\\(\mathbb{R}^n\\)</span> |
| Row space | <span class="math-inline">\\(\text{colsp}(A^T)\\)</span> | Span of the rows of <span class="math-inline">\\(A\\)</span> | <span class="math-inline">\\(\text{rank}(A)\\)</span> | <span class="math-inline">\\(\mathbb{R}^d\\)</span> |
| Null space | <span class="math-inline">\\(\text{nullsp}(A)\\)</span> | Set of all vectors <span class="math-inline">\\(\vec{x}\\)</span> such that <span class="math-inline">\\(A\vec{x} = \vec{0}\\)</span> | <span class="math-inline">\\(d - \text{rank}(A)\\)</span> | <span class="math-inline">\\(\mathbb{R}^d\\)</span> |

Additionally, note that you can write the dot product of two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> as <span class="math-inline">\\(\vec u^T\vec v\\)</span>:

<span class="math-inline">\\(\vec u^T = \begin{bmatrix}u&#95;1 &amp; u&#95;2 &amp; \cdots &amp; u&#95;n\end{bmatrix} \qquad \vec v = \begin{bmatrix}v&#95;1 \\\\ \vdots \\\\ v&#95;n\end{bmatrix}\\)</span>

<span class="math-inline">\\(\displaystyle \vec u^T\vec v = u&#95;1v&#95;1 + \dots + u&#95;nv&#95;n = \sum&#95;{i=1}^{n}(u&#95;iv&#95;i) = \vec u \cdot \vec v\\)</span> (**not** <span class="math-inline">\\(\vec u^T \cdot \vec v\\)</span>)

---

## Activity 1: Null Space of a Matrix with Linearly Independent Columns

Let <span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 0 \\\\ 0 &amp; 4 \\\\ 1 &amp; 0 \end{bmatrix}\\)</span>. What is <span class="math-inline">\\(\text{nullsp}(A)\\)</span>?

<details markdown="1"><summary>Solution</summary>

We are asked to find the null space of

<div class="math-display">
$$
A = \begin{bmatrix} 3 & 0 \\\\ 0 & 4 \\\\ 1 & 0 \end{bmatrix}
$$
</div>

The null space of <span class="math-inline">\\(A\\)</span>, denoted <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, is the set of all vectors <span class="math-inline">\\(\vec{x}\\)</span> such that

<div class="math-display">
$$
A\vec{x} = \vec{0}
$$
</div>

**In practice, we know that since <span class="math-inline">\\(A\\)</span>'s columns are all linearly independent, we know that the only vector in its nullspace is <span class="math-inline">\\(\vec 0 = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}\\)</span>.** This is because the only linear combination of linearly independent vectors that gives the zero vector is the trivial combination, where all coefficients are zero. So,

<div class="math-display">
$$
\text{nullsp}(A) = \{ \vec 0 \} = \{ \begin{bmatrix} 0 \\\\ 0 \end{bmatrix} \}
$$
</div>

But, let's suppose we didn't realize this, and wanted to systematically solve the system of equations to find the null space. Let <span class="math-inline">\\(\vec{x} = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span> Then:

<div class="math-display">
$$
A\vec{x} =
\begin{bmatrix}
3 & 0 \\\\
0 & 4 \\\\
1 & 0
\end{bmatrix}
\begin{bmatrix}
x_1 \\\\
x_2
\end{bmatrix}
=
\begin{bmatrix}
3x_1 \\\\
4x_2 \\\\
x_1
\end{bmatrix}
$$
</div>

<div class="math-display">
$$
\begin{bmatrix}
3x_1 \\\\
4x_2 \\\\
x_1
\end{bmatrix}
=
\begin{bmatrix}
0 \\\\
0 \\\\
0
\end{bmatrix}
$$
</div>

This gives the system of equations:

<div class="math-display">
$$
\begin{align*}
3x_1 &= 0 \\\\
4x_2 &= 0 \\\\
x_1 &= 0
\end{align*}
$$
</div>

<div class="math-display">
$$
x_1 = 0 \quad x_2 = 0
$$
</div>

The only vector that satisfies this system is

<div class="math-display">
$$
\vec{x} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}
$$
</div>

which confirms our initial approach.

</details>

---

## Activity 2: Fundamentals

Let <span class="math-inline">\\(X=\begin{bmatrix}1 &amp; 2 &amp; -1 &amp; 3 &amp; 4 &amp; 4 \\\\ 2 &amp; 5 &amp; -2 &amp; 7 &amp; 11 &amp; 10 \\\\ 4 &amp; 8 &amp; -4 &amp; 12 &amp; 16 &amp; 16\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>. What is <span class="math-inline">\\(\text{rank}(X)\\)</span>? Why? <em>Hint: Column 5 is a linear combination of columns 1 and 2. With this fact, you should be able to answer this relatively quickly.</em>

<details markdown="1"><summary>Solution</summary>

We are given

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & 2 & -1 & 3 & 4 & 4 \\\\
2 & 5 & -2 & 7 & 11 & 10 \\\\
4 & 8 & -4 & 12 & 16 & 16
\end{bmatrix}
$$
</div>

 Let the columns of <span class="math-inline">\\(X\\)</span> be

<div class="math-display">
$$
\vec{v}_1 =
\begin{bmatrix}1\\\\2\\\\4\end{bmatrix} \quad
\vec{v}_2 =
\begin{bmatrix}2\\\\5\\\\8\end{bmatrix} \quad
\vec{v}_3 =
\begin{bmatrix}-1\\\\-2\\\\-4\end{bmatrix} \quad
\vec{v}_4 =
\begin{bmatrix}3\\\\7\\\\12\end{bmatrix} \quad
\vec{v}_5 =
\begin{bmatrix}4\\\\11\\\\16\end{bmatrix} \quad
\vec{v}_6 =
\begin{bmatrix}4\\\\10\\\\16\end{bmatrix}
$$
</div>

The "textbook" way to find a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span> is to use the algorithm from [Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/#algorithm-for-finding-linearly-independent-subsets-with-the-same-span) to find a linearly independent subset of <span class="math-inline">\\(S\\)</span> that spans it (where <span class="math-inline">\\(S = \text{colsp}(X)\\)</span>).

> Given <span class="math-inline">\\(\vec{v}&#95;1, \vec{v}&#95;2, \dots, \vec{v}&#95;d\\)</span>

> Initialize <span class="math-inline">\\(S = \lbrace\vec{v}&#95;1\rbrace\\)</span>

> For <span class="math-inline">\\(i = 2, \dots, d\\)</span>

> If <span class="math-inline">\\(\vec{v}&#95;i\\)</span> is not a linear combination of <span class="math-inline">\\(S\\)</span>, add <span class="math-inline">\\(\vec{v}&#95;i\\)</span> to <span class="math-inline">\\(S\\)</span>

But, we've picked the numbers such that the relationships are relatively easy to see. Reading from left to right:

1.  <span class="math-inline">\\(\vec v&#95;1\\)</span> is the first vector we've seen, so it's linearly independent and we add it to our basis.

2.  <span class="math-inline">\\(\vec v&#95;2\\)</span> is not a multiple of <span class="math-inline">\\(\vec v&#95;1\\)</span>, so we add it to our basis.

3.  <span class="math-inline">\\(\vec v&#95;3 =- \vec v&#95;1\\)</span>, so don't add it.

4.  <span class="math-inline">\\(\vec v&#95;4 = \vec v&#95;1 + \vec v&#95;2\\)</span>, so don't add it.

5.  <span class="math-inline">\\(\vec v&#95;5 = -2 \vec v&#95;1 + 3 \vec v&#95;2\\)</span>, so don't add it.

6.  <span class="math-inline">\\(\vec v&#95;6 = 2 \vec v&#95;2\\)</span>, so don't add it.

So,

<div class="math-display">
$$
\boxed{
\text{Basis for } \text{colsp}(X) = S = \left\{
\begin{bmatrix}1\\\\2\\\\4\end{bmatrix},
\begin{bmatrix}2\\\\5\\\\8\end{bmatrix}
\right\}
\quad
\text{rank}(X) = 2
}
$$
</div>

The rank equals the number of linearly independent columns identified by the algorithm.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blanks: <span class="math-inline">\\(\text{colsp}(X^T)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

<details markdown="1"><summary>Solution</summary>

We know that <span class="math-inline">\\(\text{colsp}(X^T)\\)</span> is the row space of <span class="math-inline">\\(X\\)</span> and from the previous part <span class="math-inline">\\(\text{rank}(X) = 2\\)</span>.

The dimension of the row space is equal to the rank of the matrix:

<div class="math-display">
$$
\dim(\text{colsp}(X^T)) = \text{rank}(X) = 2
$$
</div>

The rows of <span class="math-inline">\\(X\\)</span> each lie in <span class="math-inline">\\(\mathbb{R}^6\\)</span> so the row space is a subspace of <span class="math-inline">\\(\mathbb{R}^6\\)</span>.

<div class="math-display">
$$
\boxed{
\text{colsp}(X^T) \text{ is a 2-dimensional subspace of } \mathbb{R}^6
}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blanks: <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

<details markdown="1"><summary>Solution</summary>

From [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/), the **rank-nullity theorem** states that for any <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(X\\)</span>,

<div class="math-display">
$$
\text{rank}(X) + \dim(\text{nullsp}(X)) = \underbrace{d}_{\text{\# columns in } X}
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
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. <em>Hint: You should be able to answer this without solving equations.</em>

<details markdown="1"><summary>Solution</summary>

The "easy way" to find a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is to find all of the ways that <span class="math-inline">\\(\vec 0\\)</span> can be written as a linear combination of <span class="math-inline">\\(X\\)</span>'s columns. The previous part told us that <span class="math-inline">\\(\text{dim}(\text{nullsp}(X)) = 4\\)</span>, so we need to find 4 linearly independent vectors that satisfy <span class="math-inline">\\(X\vec{v} = \vec{0}\\)</span>.

Recall from the solutions to part **a)** that <span class="math-inline">\\(\lbrace\vec v&#95;1, \vec v&#95;2\rbrace\\)</span> form a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>, meaning the other four columns of <span class="math-inline">\\(X\\)</span> can be written as linear combinations of them. Rearranging these linear independence relationships gives us ways to write <span class="math-inline">\\(\vec 0\\)</span>:

-   <span class="math-inline">\\(\vec v&#95;3 =- \vec v&#95;1 \implies \vec v&#95;1 + \vec v&#95;3 = \vec 0\\)</span>

-   <span class="math-inline">\\(\vec v&#95;4 = \vec v&#95;1 + \vec v&#95;2 \implies \vec v&#95;1 + \vec v&#95;2 - \vec v&#95;4 = \vec 0\\)</span>

-   <span class="math-inline">\\(\vec v&#95;5 = -2 \vec v&#95;1 + 3 \vec v&#95;2 \implies -2 \vec v&#95;1 + 3 \vec v&#95;2 - \vec v&#95;5 = \vec 0\\)</span>

-   <span class="math-inline">\\(\vec v&#95;6 = 2 \vec v&#95;2 \implies 2 \vec v&#95;2 - \vec v&#95;6 = \vec 0\\)</span>

Let's look at the first bullet point. <span class="math-inline">\\(\vec v&#95;1 + \vec v&#95;3 = \vec 0\\)</span> implies that:

<div class="math-display">
$$
X \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} = \begin{bmatrix}
    1 & 2 & -1 & 3 & 4 & 4 \\\\
    2 & 5 & -2 & 7 & 11 & 10 \\\\
    4 & 8 & -4 & 12 & 16 & 16
    \end{bmatrix} \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} = \vec 0
$$
</div>

The second bullet point, <span class="math-inline">\\(\vec v&#95;1 + \vec v&#95;2 - \vec v&#95;4 = \vec 0\\)</span> implies that:

<div class="math-display">
$$
X \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 0 \end{bmatrix} = \vec 0
$$
</div>

and similarly with <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 3 \\\\ 0 \\\\ 0 \\\\ -1 \\\\ 0 \end{bmatrix}\\)</span> (bullet point 3, i.e. from <span class="math-inline">\\(-2 \vec v&#95;1 + 3 \vec v&#95;2 - \vec v&#95;5 = \vec 0\\)</span>) and <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 2 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ -1 \end{bmatrix}\\)</span> (bullet point 4, i.e. from <span class="math-inline">\\(2 \vec v&#95;2 - \vec v&#95;6 = \vec 0\\)</span>).

So, a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is:

<div class="math-display">
$$
\boxed{
\left\{
\begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix},
\begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 0 \end{bmatrix},
\begin{bmatrix} -2 \\\\ 3 \\\\ 0 \\\\ 0 \\\\ -1 \\\\ 0 \end{bmatrix},
\begin{bmatrix} 0 \\\\ 2 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ -1 \end{bmatrix}
\right\}
}
$$
</div>

Notice that these vectors are linearly independent, because each successive vector has a non-zero entry in a position that the previous vectors all have zeros in. They span the entirety of <span class="math-inline">\\(\text{nullsp}(X)\\)</span> --- any linear combination of them will, when multiplied by <span class="math-inline">\\(X\\)</span>, give the zero vector.

</details>

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix with rank <span class="math-inline">\\(r\\)</span>. A CR decomposition of <span class="math-inline">\\(A\\)</span> is a product of two matrices <span class="math-inline">\\(C\\)</span> and <span class="math-inline">\\(R\\)</span>, where <span class="math-inline">\\(A = CR\\)</span> and:

-   <span class="math-inline">\\(C\\)</span> is an <span class="math-inline">\\(n \times r\\)</span> matrix and <span class="math-inline">\\(R\\)</span> is a <span class="math-inline">\\(r \times d\\)</span> matrix

-   <span class="math-inline">\\(C\\)</span> contains the linearly independent columns of <span class="math-inline">\\(A\\)</span>, selected left-to-right

-   <span class="math-inline">\\(R\\)</span> tells how to "mix'' the columns of <span class="math-inline">\\(C\\)</span> (which are linearly independent) to reconstruct the columns of <span class="math-inline">\\(A\\)</span>

Let's keep working with <span class="math-inline">\\(X = \begin{bmatrix}1 &amp; 2 &amp; -1 &amp; 3 &amp; 4 &amp; 4 \\\\ 2 &amp; 5 &amp; -2 &amp; 7 &amp; 11 &amp; 10 \\\\ 4 &amp; 8 &amp; -4 &amp; 12 &amp; 16 &amp; 16\end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Find a CR decomposition of <span class="math-inline">\\(X\\)</span>. This shouldn't take very much work; review your work from part **a)** in finding a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<details markdown="1"><summary>Solution</summary>

We are asked to find a CR decomposition of

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & 2 & -1 & 3 & 4 & 4 \\\\
2 & 5 & -2 & 7 & 11 & 10 \\\\
4 & 8 & -4 & 12 & 16 & 16
\end{bmatrix}
$$
</div>

From part **a)**, we determined that

<div class="math-display">
$$
\text{rank}(X) = 2
\quad \text{and} \quad
\text{basis for } \text{colsp}(X) =
\left\{
\begin{bmatrix} 1 \\\\ 2 \\\\ 4 \end{bmatrix},
\begin{bmatrix} 2 \\\\ 5 \\\\ 8 \end{bmatrix}
\right\}
$$
</div>

 These two columns of <span class="math-inline">\\(X\\)</span> are linearly independent, and all other columns of <span class="math-inline">\\(X\\)</span> can be written as linear combinations of them.

By definition of the CR decomposition, the matrix <span class="math-inline">\\(C\\)</span> contains the linearly independent columns of <span class="math-inline">\\(X\\)</span> (selected left-to-right). Thus,

<div class="math-display">
$$
C =
\begin{bmatrix}
1 & 2 \\\\
2 & 5 \\\\
4 & 8
\end{bmatrix}
$$
</div>

 <span class="math-inline">\\(C\\)</span> has shape <span class="math-inline">\\(3\times 2\\)</span>, and its two columns form a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

The matrix <span class="math-inline">\\(R\\)</span> describes how to "mix'' the columns of <span class="math-inline">\\(C\\)</span> to obtain all six columns of <span class="math-inline">\\(X\\)</span>. That is, each column of <span class="math-inline">\\(R\\)</span> contains the coefficients expressing one column of <span class="math-inline">\\(X\\)</span> as a linear combination of the two columns of <span class="math-inline">\\(C\\)</span>.

Fortunately, we did all of the heavy lifting in part **d)**, when finding a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. We just need to rearrange our work. Recall that:

<div class="math-display">
$$
\vec v_3 = -\vec v_1, \quad \vec v_4 = \vec v_1 + \vec v_2, \quad \vec v_5 = -2 \vec v_1 + 3 \vec v_2, \quad \vec v_6 = 2 \vec v_2
$$
</div>

So,

<div class="math-display">
$$
R =
\begin{bmatrix}
1 & 0 & -1 & 1 & -2 & 0\\\\
0 & 1 & 0 & 1 & 3 & 2
\end{bmatrix}
$$
</div>

Where did the first two columns of <span class="math-inline">\\(R\\)</span> come from? We want the first column of <span class="math-inline">\\(X\\)</span> to be just the first column of <span class="math-inline">\\(C\\)</span>, which we get by taking 1 of column 1 and 0 of column 2. Similarly, the second column of <span class="math-inline">\\(X\\)</span> is just the second column of <span class="math-inline">\\(C\\)</span>, which we get by taking 0 of column 1 and 1 of column 2.

So, in a CR decomposition that is constructed by taking the linearly independent columns of <span class="math-inline">\\(X\\)</span> from left-to-right, the first <span class="math-inline">\\(r\\)</span> columns are the <span class="math-inline">\\(r \times r\\)</span> identity matrix, and the remaining columns are the coefficients needed to write the remaining <span class="math-inline">\\(d - r\\)</span> columns of <span class="math-inline">\\(X\\)</span> as linear combinations of the <span class="math-inline">\\(r\\)</span> columns of <span class="math-inline">\\(C\\)</span>.

Verifying,

<div class="math-display">
$$
C R =
\begin{bmatrix}
1 & 2 \\\\
2 & 5 \\\\
4 & 8
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -1 & 1 & -2 & 0\\\\
0 & 1 & 0 & 1 & 3 & 2
\end{bmatrix}
=
\begin{bmatrix}
1 & 2 & -1 & 3 & 4 & 4\\\\
2 & 5 & -2 & 7 & 11 & 10\\\\
4 & 8 & -4 & 12 & 16 & 16
\end{bmatrix}
= X
$$
</div>

<div class="math-display">
$$
\boxed{
C =
\begin{bmatrix}
1 & 2 \\\\
2 & 5 \\\\
4 & 8
\end{bmatrix}
\quad
R =
\begin{bmatrix}
1 & 0 & -1 & 1 & -2 & 0\\\\
0 & 1 & 0 & 1 & 3 & 2
\end{bmatrix}
\quad
\text{and } X = C R
}
$$
</div>

</details>

The key idea being assessed here is that in <span class="math-inline">\\(A = CR\\)</span>, the columns of <span class="math-inline">\\(C\\)</span> are linearly independent and a basis for <span class="math-inline">\\(\text{colsp}(A)\\)</span>, while the rows of <span class="math-inline">\\(R\\)</span> are linearly independent and a basis for <span class="math-inline">\\(\text{colsp}(A^T)\\)</span>!

</div>
</div>

</div>

---

## Activity 3: Outer Products

Suppose <span class="math-inline">\\(A = \vec u \vec v^T + \vec w \vec z^T\\)</span>, where <span class="math-inline">\\(\vec u, \vec v, \vec w, \vec z \in \mathbb{R}^n\\)</span> are non-zero vectors.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
What is <span class="math-inline">\\(\text{rank}(\vec u \vec v^T)\\)</span>?

<details markdown="1"><summary>Solution</summary>

The matrix <span class="math-inline">\\(\vec{u}\vec{v}^T\\)</span> is formed by multiplying a column vector <span class="math-inline">\\(\vec{u}\\)</span> by a row vector <span class="math-inline">\\(\vec{v}^T\\)</span>:

<div class="math-display">
$$
\vec{u}\vec{v}^T =
\begin{bmatrix}
u_1 \\\\[2pt] u_2 \\\\[2pt] \vdots \\\\[2pt] u_n
\end{bmatrix}
\begin{bmatrix}
v_1 & v_2 & \cdots & v_n
\end{bmatrix}
=
\begin{bmatrix}
u_1v_1 & u_1v_2 & \cdots & u_1v_n \\\\[2pt]
u_2v_1 & u_2v_2 & \cdots & u_2v_n \\\\[2pt]
\vdots & \vdots & \ddots & \vdots \\\\[2pt]
u_nv_1 & u_nv_2 & \cdots & u_nv_n
\end{bmatrix}
$$
</div>

Each column of this matrix is a scalar multiple of the same vector <span class="math-inline">\\(\vec{u}\\)</span>. For example:

<div class="math-display">
$$
\text{First column: } v_1\vec{u}, \quad
\text{Second column: } v_2\vec{u}, \quad \dots, \quad
\text{n-th column: } v_n\vec{u}.
$$
</div>

Thus, every column lies in the same one-dimensional subspace spanned by <span class="math-inline">\\(\vec{u}\\)</span>:

<div class="math-display">
$$
\text{colsp}(\vec{u}\vec{v}^T) = \text{span}(\{\vec{u}\})
$$
</div>

Since all columns are proportional to <span class="math-inline">\\(\vec{u}\\)</span>, there is exactly one linearly independent column. The dimension of the column space (and hence the rank) is therefore 1:

<div class="math-display">
$$
\boxed{\text{rank}(\vec{u}\vec{v}^T) = 1}
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

**The short answer is that** <span class="math-inline">\\(\text{rank}(A) = 2\\)</span> if and only if <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> are linearly independent and <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec z\\)</span> are linearly independent. If either <span class="math-inline">\\(\lbrace \vec u, \vec w \rbrace\\)</span> or <span class="math-inline">\\(\lbrace \vec v, \vec z \rbrace\\)</span> are linearly dependent, then <span class="math-inline">\\(\text{rank}(A) = 1\\)</span>. The easy way to reason about this is that:

-   The columns of <span class="math-inline">\\(\vec u \vec v^T\\)</span> are all scalar multiples of <span class="math-inline">\\(\vec u\\)</span> and the columns of <span class="math-inline">\\(\vec w \vec z^T\\)</span> are all scalar multiples of <span class="math-inline">\\(\vec w\\)</span>. If <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> are linearly **dependent**, then all columns of <span class="math-inline">\\(A\\)</span> are scalar multiples of <span class="math-inline">\\(\vec u\\)</span> (or <span class="math-inline">\\(\vec w\\)</span>), meaning <span class="math-inline">\\(\text{dim}(\text{colsp}(A)) = 1\\)</span>, which means <span class="math-inline">\\(\text{rank}(A) = 1\\)</span>.

-   The rows of <span class="math-inline">\\(\vec u \vec v^T\\)</span> are all scalar multiples of <span class="math-inline">\\(\vec v^T\\)</span> and the rows of <span class="math-inline">\\(\vec w \vec z^T\\)</span> are all scalar multiples of <span class="math-inline">\\(\vec z^T\\)</span>. If <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec z\\)</span> are linearly **dependent**, then all rows of <span class="math-inline">\\(A\\)</span> are scalar multiples of <span class="math-inline">\\(\vec v^T\\)</span> (or <span class="math-inline">\\(\vec z^T\\)</span>), meaning <span class="math-inline">\\(\text{dim}(\text{rowsp}(A)) = 1\\)</span>, which means <span class="math-inline">\\(\text{rank}(A) = 1\\)</span>.

-   In order for <span class="math-inline">\\(\text{rank}(A) = 2\\)</span>, there need to be at least two linearly independent columns and two linearly independent rows, which means that both pairs <span class="math-inline">\\(\lbrace \vec u, \vec v \rbrace\\)</span> and <span class="math-inline">\\(\lbrace \vec w, \vec z \rbrace\\)</span> must be linearly independent.

For a more detailed explanation, let's start from the beginning.

We are given

<div class="math-display">
$$
A = \vec{u}\vec{v}^T + \vec{w}\vec{z}^T
$$
</div>

 with each outer product being rank 1. As the hint suggests, let's think about what happens when multiplying <span class="math-inline">\\(A\\)</span> by a vector <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span>:

<div class="math-display">
$$
A \vec x = (\vec{u}\vec{v}^T + \vec{w}\vec{z}^T) \vec x = (\vec{v}^T\vec{x})\vec{u} + (\vec{z}^T\vec{x})\vec{w}
$$
</div>

This shows that <span class="math-inline">\\(A \vec x\\)</span> is always a linear combination of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{w}\\)</span>. So, <span class="math-inline">\\(\text{colsp}(A)\\)</span> **is a subspace of <span class="math-inline">\\(\text{span}(\lbrace\vec{u}, \vec{w}\rbrace)\\)</span>**, since every vector in <span class="math-inline">\\(\text{colsp}(A)\\)</span> can be written as a linear combination of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{w}\\)</span>.

-   If <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{w}\\)</span> themselves point in the same direction (i.e. are linearly **dependent**), then any vector in <span class="math-inline">\\(\text{colsp}(A)\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec u\\)</span> (or, equivalently, of <span class="math-inline">\\(\vec w\\)</span>). This would mean <span class="math-inline">\\(\text{dim}(\text{colsp}(A)) = 1\\)</span>, which means <span class="math-inline">\\(\text{rank}(A) = 1\\)</span>.

-   With that case out of the way, let's suppose <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> are linearly independent. Does this automatically mean that <span class="math-inline">\\(\text{dim}(\text{colsp}(A)) = 2\\)</span>? No: all we know for sure is that every vector of the form <span class="math-inline">\\(A \vec x\\)</span> is a linear combination of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span>. We don't yet know that the converse is true, i.e. that every linear combination of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> can be written as <span class="math-inline">\\(A \vec x\\)</span>, for some <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span>.

   In order for it to be the case that <span class="math-inline">\\(\text{colsp}(A) = \text{span}(\lbrace\vec{u}, \vec{w}\rbrace)\\)</span>, we must be able to take **any** linear combination of <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{w}\\)</span> and write it as <span class="math-inline">\\(A \vec x\\)</span> for some <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span>. Meaning, for any <span class="math-inline">\\(c\\)</span> and <span class="math-inline">\\(d\\)</span>, we must be able to find some <span class="math-inline">\\(\vec x\\)</span> such that:

<div class="math-display">
$$
A \vec x = c \vec u + d \vec w
$$
</div>

 But, we know that

<div class="math-display">
$$
A \vec x = (\vec{v}^T\vec{x})\vec{u} + (\vec{z}^T\vec{x})\vec{w}
$$
</div>

 So, the question really is, is it **always** possible, for any <span class="math-inline">\\(c\\)</span>, <span class="math-inline">\\(d\\)</span>, to find an <span class="math-inline">\\(\vec x\\)</span> that satisfies:

<div class="math-display">
$$
c = \vec{v}^T\vec{x}, \qquad d = \vec{z}^T\vec{x}
$$
</div>

 This may seem a bit abstract, so let's just plug in specific numbers for <span class="math-inline">\\(c\\)</span> and <span class="math-inline">\\(d\\)</span> to make things a bit more clear.

<div class="math-display">
$$
3 = \vec{v}^T\vec{x}, \qquad 4 = \vec{z}^T\vec{x}
$$
</div>

 Remember that <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec z\\)</span> are fixed here. Given them, can we find an <span class="math-inline">\\(\vec x\\)</span> that satisfies both of these equations? **We can, as long as <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec z\\)</span> are linearly independent too!** If they are, then <span class="math-inline">\\(\vec v^T \vec x = 3\\)</span> is one equation with <span class="math-inline">\\(n\\)</span> unknowns, and <span class="math-inline">\\(\vec z^T \vec x = 4\\)</span> is another equation with <span class="math-inline">\\(n\\)</span> unknowns. Since there are <span class="math-inline">\\(n\\)</span> unknowns and 2 equations, the system is overdetermined, and there are infinitely many solutions for <span class="math-inline">\\(\vec x\\)</span>, we just need to pick one of them.

   Again, let's give an example. Suppose <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> are linearly independent (a prerequisite for the case we're considering), let <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 \\\\ 4 \\\\ 5 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec z = \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span> (which are also linearly independent as a pair), and suppose <span class="math-inline">\\(A \vec x = 3 \vec u + 4 \vec w\\)</span>. Then, <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ x&#95;3 \end{bmatrix}\\)</span> must satisfy:



<div class="math-display">
$$
\vec v^T \vec x = 3 \implies 3x_1 + 4x_2 + 5x_3 = 3
$$
</div>



<div class="math-display">
$$
\vec z^T \vec x = 4 \implies 0x_1 + 0x_2 + 1x_3 = 4
$$
</div>

 Solving these, we get:

<div class="math-display">
$$
x_3 = 4
$$
</div>



<div class="math-display">
$$
3x_1 + 4x_2 + 20 = 3 \implies 3x_1 + 4x_2 = -17
$$
</div>

 So, as long as we pick <span class="math-inline">\\(x&#95;3 = 4\\)</span> and <span class="math-inline">\\(x&#95;1\\)</span> and <span class="math-inline">\\(x&#95;2\\)</span> to satisfy <span class="math-inline">\\(3x&#95;1 + 4x&#95;2 = -17\\)</span>, we can find an <span class="math-inline">\\(\vec x\\)</span> that satisfies both of the equations, meaning we're able to find an <span class="math-inline">\\(\vec x\\)</span> to make <span class="math-inline">\\(A \vec x = 3 \vec u + 4 \vec w\\)</span>.

   Nothing was special about <span class="math-inline">\\(c = 3\\)</span> and <span class="math-inline">\\(d = 4\\)</span>. What was special was that in addition to <span class="math-inline">\\(\lbrace \vec u, \vec w \rbrace\\)</span> being linearly independent, we also had <span class="math-inline">\\(\lbrace \vec v, \vec z \rbrace\\)</span> being linearly independent. This is the condition that makes it possible to find an <span class="math-inline">\\(\vec x\\)</span> that satisfies both of the equations. If they weren't linearly independent, it isn't guaranteed that we can find an <span class="math-inline">\\(\vec x\\)</span> that satisfies both of the equations. Suppose we revisit the same example, but instead with <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 \\\\ 4 \\\\ 5 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec z = \begin{bmatrix} 30 \\\\ 40 \\\\ 50 \end{bmatrix}\\)</span> (which are linearly dependent as a pair). Then, <span class="math-inline">\\(\vec v^T \vec x = 3\\)</span> and <span class="math-inline">\\(\vec z^T \vec x = 4\\)</span> are two equations with <span class="math-inline">\\(n\\)</span> unknowns still, but <span class="math-inline">\\(\vec x\\)</span> would need to satisfy



<div class="math-display">
$$
3x_1 + 4x_2 + 5x_3 = 3
$$
</div>



<div class="math-display">
$$
30x_1 + 40x_2 + 50x_3 = 4
$$
</div>

   which has no solutions, meaning we're not able to find an <span class="math-inline">\\(\vec x\\)</span> to make <span class="math-inline">\\(A \vec x = 3 \vec u + 4 \vec w\\)</span>, meaning <span class="math-inline">\\(\text{colsp}(A) \neq \text{span}(\lbrace\vec{u}, \vec{w}\rbrace)\\)</span>.

That was a long solution, in which we tried to build intuition for how you might think about this. But to summarize:

-   <span class="math-inline">\\(\text{rank}(A) = 2\\)</span> if and only if <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> are linearly independent and <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec z\\)</span> are linearly independent.

-   If either <span class="math-inline">\\(\lbrace \vec u, \vec w \rbrace\\)</span> or <span class="math-inline">\\(\lbrace \vec v, \vec z \rbrace\\)</span> are linearly dependent, then <span class="math-inline">\\(\text{rank}(A) = 1\\)</span>.

-   If any of the vectors are the zero vector, then <span class="math-inline">\\(\text{rank}(A) = 0\\)</span>.

</details>

</div>
</div>

</div>

---

## Activity 4: The Systems of Equations View

Let <span class="math-inline">\\(A\\)</span> be an <span class="math-inline">\\(n \times d\\)</span> matrix of rank <span class="math-inline">\\(r\\)</span>, and suppose there exists vectors <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span> such that

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
\text{rank}(A^T) + \dim(\text{nullsp}(A^T)) = \underbrace{n}_{\text{\# columns in } A^T}
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

We derived <span class="math-inline">\\(A^{-1}\\)</span> by factoring out <span class="math-inline">\\(A\\)</span> on the left, i.e. <span class="math-inline">\\(A \left( \frac{1}{4}(A^3 - 3A + 2I) \right) = I\\)</span>. For <span class="math-inline">\\(A^{-1}\\)</span> to be the inverse of <span class="math-inline">\\(A\\)</span>, it must also be true that <span class="math-inline">\\(\left( \frac{1}{4}(A^3 - 3A + 2I) \right) A = I\\)</span>; this fact is not automatically true in general, since the order of multiplication matters. But here, we don't need to do any additional work, since our factorization only involved powers of <span class="math-inline">\\(A\\)</span>, and in (say) <span class="math-inline">\\(A^2 = AA\\)</span> the order of multiplication doesn't matter.

</details>

---

## Activity 6: Basics of Invertibility

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix. State as many of the equivalent conditions for invertibility as you can.

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix, then <span class="math-inline">\\(A\\)</span> is invertible if and only if:

-   <span class="math-inline">\\(\text{rank}(A) = n\\)</span>

-   <span class="math-inline">\\(A\\)</span>'s columns are linearly independent (and hence <span class="math-inline">\\(\text{colsp}(A) = \mathbb{R}^n\\)</span>)

-   <span class="math-inline">\\(A\\)</span>'s rows are linearly independent (and hence <span class="math-inline">\\(\text{rowsp}(A) = \text{colsp}(A^T) = \mathbb{R}^n\\)</span>)

-   <span class="math-inline">\\(A\\)</span>'s null space is only the zero vector, i.e. <span class="math-inline">\\(\text{nullsp}(A) = \lbrace\vec 0\rbrace\\)</span>

-   <span class="math-inline">\\(\text{det}(A) \neq 0\\)</span>

</details>

---

## Activity 7: Programming

Complete the tasks in the `lab06.ipynb` notebook. Watch [this video](https://youtu.be/HZtoekU9NcE) first with tips on using `numpy` for linear algebra.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/HZtoekU9NcE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/sp26-code/tree/main/labs/lab06/lab06.ipynb), and open `labs/lab06/lab06.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Flabs%2Flab06%2Flab06.ipynb&branch=main) to open `lab06.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

Once you're done, include a screenshot of your completed Activity 7 implementation in your PDF submission of Lab 6 to Gradescope, making sure to include proof that the (local) autograder passed. Instructions on how to do this are in the lab notebook.

{% endraw %}
