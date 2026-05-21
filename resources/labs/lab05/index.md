---
layout: page
title: "Lab 5: Vector Spaces, Subspaces, Bases, and Dimension"
description: "Lab 5: Vector Spaces, Subspaces, Bases, and Dimension activities."
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

# Lab 5: Vector Spaces, Subspaces, Bases, and Dimension

**due** for completion at 11:59PM Ann Arbor Time on Wednesday, May 20th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab05/lab05.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab05/lab05-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Formal Definition of Linear Independence](#activity-1-formal-definition-of-linear-independence)
- [Activity 2: Thinking in Higher Dimensions](#activity-2-thinking-in-higher-dimensions)
- [Activity 3: Introduction to Subspaces](#activity-3-introduction-to-subspaces)
- [Activity 4: Finding Non-Examples of Subspaces](#activity-4-finding-non-examples-of-subspaces)
- [Activity 5: Finding Bases for Subspaces](#activity-5-finding-bases-for-subspaces)

---

**Recap: Vector Spaces, Subspaces, Bases, and Dimension** ([Chapter 4.3](https://notes.eecs245.org/linear-independence/vector-spaces-basis-dimension/))

-   A **subspace** <span class="math-inline">\\(S\\)</span> of a vector space <span class="math-inline">\\(V\\)</span> is a set of vectors where:

    1.  <span class="math-inline">\\(\vec{0} \in S\\)</span>

    2.  <span class="math-inline">\\(\vec{u}, \vec{v} \in S \rightarrow \vec{u} + \vec{v} \in S\\)</span>

    3.  <span class="math-inline">\\(\vec{u} \in S, c \in \mathbb{R} \rightarrow c\vec{u} \in S\\)</span>

    If you take any two vectors <span class="math-inline">\\(\vec{u}, \vec{v} \in S\\)</span>, then any linear combination <span class="math-inline">\\(c\vec{u}+d\vec{v}\\)</span> must also be in <span class="math-inline">\\(S\\)</span>.

-   As an example, let's consider <span class="math-inline">\\(\mathbb{R}^2\\)</span>, which itself is a vector space.

    ![image](imgs/lab06-lines.jpg)

-   The line through the origin **is** a subspace of <span class="math-inline">\\(\mathbb{R}^2\\)</span>, with dimension 1. It is the span of the vector <span class="math-inline">\\(\begin{bmatrix}1 \\\\ 1\end{bmatrix}\\)</span>.

-   The other line, however, is **not** a subspace of <span class="math-inline">\\(\mathbb{R}^2\\)</span>, since it doesn't pass through the origin.

-   A **basis** for a subspace <span class="math-inline">\\(S\\)</span> is a set of vectors that:

    1.  span all of <span class="math-inline">\\(S\\)</span>

    2.  are linearly independent

    A basis for a subspace is a minimal set of vectors that spans the whole subspace. All subspaces have infinitely many bases. For example, <span class="math-inline">\\(\left \lbrace \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 1 \end{bmatrix} \right\rbrace\\)</span> and <span class="math-inline">\\(\left \lbrace \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 2 \\\\ 3 \end{bmatrix} \right\rbrace\\)</span> are both bases for <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

-   The **dimension** of a subspace <span class="math-inline">\\(S\\)</span>, denoted <span class="math-inline">\\(\text{dim}(S)\\)</span>, is the number of vectors in any basis for <span class="math-inline">\\(S\\)</span>.

---

## Activity 1: Formal Definition of Linear Independence

Suppose <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d \in \mathbb{R}^n\\)</span>, and that <span class="math-inline">\\(\vec b \in \text{span}(\lbrace\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\rbrace)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Give a one sentence English explanation of what it means for <span class="math-inline">\\(\vec b \in \text{span}(\lbrace\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\rbrace)\\)</span>.

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\vec b \in \text{span}(\lbrace\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\rbrace)\\)</span>, then there exist scalars <span class="math-inline">\\(a&#95;1, a&#95;2, \ldots, a&#95;d\\)</span> such that <span class="math-inline">\\(\vec b = a&#95;1 \vec v&#95;1 + a&#95;2 \vec v&#95;2 + \ldots + a&#95;d \vec v&#95;d\\)</span>, i.e. <span class="math-inline">\\(\vec b\\)</span> can be written as a linear combination of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose that <span class="math-inline">\\(a&#95;1 \vec v&#95;1 + a&#95;2 \vec v&#95;2 + \ldots + a&#95;d \vec v&#95;d = \vec b\\)</span> **and** <span class="math-inline">\\(c&#95;1 \vec v&#95;1 + c&#95;2 \vec v&#95;2 + \ldots + c&#95;d \vec v&#95;d = \vec b\\)</span>, where at least one of the <span class="math-inline">\\(a&#95;i\\)</span>'s is different from its corresponding <span class="math-inline">\\(c&#95;i\\)</span>.

Using the formal definition of linear independence from [Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/), determine whether or not <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span> are linearly independent, and prove your answer.

<details markdown="1"><summary>Solution</summary>

We're given that

<div class="math-display">
$$
\begin{align*}
a_1 \vec v_1 + a_2 \vec v_2 + \ldots + a_d \vec v_d &= \vec b \\\\
c_1 \vec v_1 + c_2 \vec v_2 + \ldots + c_d \vec v_d &= \vec b
\end{align*}
$$
</div>

Subtracting the two equations gives us

<div class="math-display">
$$
(a_1 - c_1) \vec v_1 + (a_2 - c_2) \vec v_2 + \ldots + (a_d - c_d) \vec v_d = \vec 0
$$
</div>

We know that vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span> are linearly independent if the only way to write the zero vector <span class="math-inline">\\(\vec 0\\)</span> as a linear combination of them is to have all the coefficients be zero.

But here, we were told that at least one of the <span class="math-inline">\\(a&#95;i\\)</span>'s is different from its corresponding <span class="math-inline">\\(c&#95;i\\)</span>, meaning that at least one of the <span class="math-inline">\\((a&#95;i - c&#95;i)\\)</span> values is non-zero. This means that there is some way to create <span class="math-inline">\\(\vec 0\\)</span> using a non-zero linear combination of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span>, which means that <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span> are linearly dependent.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find another set of coefficients <span class="math-inline">\\(k&#95;1, k&#95;2, \ldots, k&#95;d\\)</span> such that

<div class="math-display">
$$
k_1 \vec v_1 + k_2 \vec v_2 + \ldots + k_d \vec v_d = \vec b
$$
</div>

and at least one of the <span class="math-inline">\\(k&#95;i\\)</span>'s is different from its corresponding <span class="math-inline">\\(a&#95;i\\)</span> or <span class="math-inline">\\(c&#95;i\\)</span>.

By doing this, you're showing that if there is at least one way to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of a set of vectors, then there are infinitely many ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of those vectors; there can't just be two or three ways to do it.

<details markdown="1"><summary>Solution</summary>

In the previous proof we subtracted the following two equations. What if we add them?

<div class="math-display">
$$
\begin{align*}
a_1 \vec v_1 + a_2 \vec v_2 + \ldots + a_d \vec v_d &= \vec b \\\\
c_1 \vec v_1 + c_2 \vec v_2 + \ldots + c_d \vec v_d &= \vec b
\end{align*}
$$
</div>

This would give us

<div class="math-display">
$$
(a_1 + c_1) \vec v_1 + (a_2 + c_2) \vec v_2 + \ldots + (a_d + c_d) \vec v_d = 2 \vec b
$$
</div>

Dividing both sides by 2 gives us

<div class="math-display">
$$
\left( \frac{a_1 + c_1}{2} \right) \vec v_1 + \left( \frac{a_2 + c_2}{2} \right) \vec v_2 + \ldots + \left( \frac{a_d + c_d}{2} \right) \vec v_d = \vec b
$$
</div>

This is another linear combination of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span> that equals <span class="math-inline">\\(\vec b\\)</span>! So <span class="math-inline">\\(k&#95;1 = \frac{a&#95;1 + c&#95;1}{2}, k&#95;2 = \frac{a&#95;2 + c&#95;2}{2}, \ldots, k&#95;d = \frac{a&#95;d + c&#95;d}{2}\\)</span>.

Why does this imply that there are infinitely many ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span>? It's because we could repeat this process once again, to get <span class="math-inline">\\(\frac{a&#95;1 + k&#95;1}{2}\\)</span>, <span class="math-inline">\\(\frac{a&#95;2 + k&#95;2}{2}\\)</span>, <span class="math-inline">\\(\ldots\\)</span>, <span class="math-inline">\\(\frac{a&#95;d + k&#95;d}{2}\\)</span> as coefficients, and then again, and again. There are other ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\\)</span> since they're linearly dependent, but we'd need to know more about the specific relationships between the vectors to find more.

</details>

</div>
</div>

</div>

---

## Activity 2: Thinking in Higher Dimensions

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;8\\)</span> are 8 vectors in <span class="math-inline">\\(\mathbb{R}^5\\)</span>. Fill in each blank below with one of the provided options, and explain your reasoning.

1.  These vectors \_\_\_\_\_\_\_\_ span all of <span class="math-inline">\\(\mathbb{R}^5\\)</span>.

    (options: do, do not, might)

2.  These vectors \_\_\_\_\_\_\_\_ linearly independent.

    (options: are, are not, might be)

3.  Any 5 of these vectors \_\_\_\_\_\_\_\_ span all of <span class="math-inline">\\(\mathbb{R}^5\\)</span>.

    (options: do, do not, might)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\vec u&#95;1, \vec u&#95;2, \ldots, \vec u&#95;{10}\\)</span> are 10 non-zero vectors in <span class="math-inline">\\(\mathbb{R}^{11}\\)</span>.

Furthermore, suppose that <span class="math-inline">\\(\text{span}(\lbrace\vec u&#95;1, \vec u&#95;2, \ldots, \vec u&#95;{10}\rbrace)\\)</span> is a 6-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^{11}\\)</span>. This means that there exists a subset of 6 of these vectors that is linearly independent and spans the same 6-dimensional subspace as the original 10 vectors; we just don't know which 6.

1.  Let <span class="math-inline">\\(k\\)</span> be the dimension of the subspace spanned by a subset of 4 of these vectors. What are all possible values of <span class="math-inline">\\(k\\)</span>?

2.  Let <span class="math-inline">\\(m\\)</span> be the dimension of the subspace spanned by a subset of 7 of these vectors. What are all possible values of <span class="math-inline">\\(m\\)</span>?

</div>
</div>

</div>

---

## Activity 3: Introduction to Subspaces

Only one of the following is a subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span>. Which one? Explain why the others are not subspaces.

The set of vectors <span class="math-inline">\\(\vec v = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> in <span class="math-inline">\\(\mathbb{R}^3\\)</span> such that

1.  <span class="math-inline">\\(x + 2y - 3z = 4\\)</span>

2.  <span class="math-inline">\\(\vec v\\)</span> is on the line <span class="math-inline">\\(L = \begin{bmatrix} 1 \\\\ -2 \\\\ 0 \end{bmatrix} + t \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}, t \in \mathbb{R}\\)</span>

3.  <span class="math-inline">\\(x + y + z = 0\\)</span> and <span class="math-inline">\\(x - y + z = 1\\)</span>

4.  <span class="math-inline">\\(x = -z\\)</span> and <span class="math-inline">\\(x = z\\)</span>

5.  <span class="math-inline">\\(x^2 + y^2 = z\\)</span>

<details markdown="1"><summary>Solution</summary>

Recall that a subspace must contain the zero vector and must be closed under addition and scalar multiplication.

1.  <span class="math-inline">\\(x + 2y - 3z = 4\\)</span> is **not a subspace**. The zero vector is not in the set, since plugging in <span class="math-inline">\\(x = 0, y = 0, z = 0\\)</span> to the equation <span class="math-inline">\\(x + 2y - 3z = 4\\)</span> gives us <span class="math-inline">\\(0 + 0 - 0 = 4\\)</span>, which is not true. <span class="math-inline">\\(x + 2y - 3z = 4\\)</span> is a plane in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, and planes are subspaces only when they contain the zero vector.

2.  The line <span class="math-inline">\\(L = \begin{bmatrix} 1 \\\\ -2 \\\\ 0 \end{bmatrix} + t \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}, t \in \mathbb{R}\\)</span> is **not a subspace**. The zero vector is not in the set, since no value of <span class="math-inline">\\(t\\)</span> makes <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ 0 \end{bmatrix} + t \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. The first equation implies <span class="math-inline">\\(1 + 2t = 0 \implies t = -\frac{1}{2}\\)</span>, while the last implies <span class="math-inline">\\(0 + 4t = 0 \implies t = 0\\)</span>, which is a contradiction.

3.  <span class="math-inline">\\(x + y + z = 0\\)</span> and <span class="math-inline">\\(x - y + z = 1\\)</span> is **not a subspace**. These are two non-parallel planes in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, which means their intersection is a line in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. Lines are subspaces only when they pass through the origin, i.e. contain the zero vector. But the second equation requires <span class="math-inline">\\(x - y + z = 1\\)</span>, but at <span class="math-inline">\\((0, 0, 0)\\)</span> this is <span class="math-inline">\\(0 - 0 + 0 = 1\\)</span>, which is not true, meaning that the zero vector is not in the set and so the set is not a subspace.

4.  <span class="math-inline">\\(x = -z\\)</span> and <span class="math-inline">\\(x = z\\)</span> <span class="math-inline">\\(\boxed{\textbf{is a subspace}}\\)</span>. For <span class="math-inline">\\(x = -z\\)</span> and <span class="math-inline">\\(x = z\\)</span> to both be true, we'd need <span class="math-inline">\\(z = -z\\)</span>, which implies <span class="math-inline">\\(z = 0\\)</span> and <span class="math-inline">\\(x = 0\\)</span>. So, this is the set of all vectors whose first and third components are 0. The zero vector is in the set (since the zero vector's first and third components are 0), and the set is closed under addition and scalar multiplication, since if



<div class="math-display">
$$
\vec u = \begin{bmatrix} 0 \\\\ a \\\\ 0 \end{bmatrix}, \quad \vec v = \begin{bmatrix} 0 \\\\ b \\\\ 0 \end{bmatrix}
$$
</div>

    then

<div class="math-display">
$$
c \vec u + d \vec v = \begin{bmatrix} 0 \\\\ ca + db \\\\ 0 \end{bmatrix}
$$
</div>

    is also in the set. So, the set of vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> that satisfy <span class="math-inline">\\(x = -z\\)</span> and <span class="math-inline">\\(x = z\\)</span> is a subspace.

5.  <span class="math-inline">\\(x^2 + y^2 = z\\)</span> is **not a subspace**. The zero vector is the set, since plugging in <span class="math-inline">\\((x, y, z) = (0, 0, 0)\\)</span> gives us <span class="math-inline">\\(0^2 + 0^2 = 0\\)</span>, which is fine. But, the set is not closed under scalar multiplication. For example, consider <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 4 \\\\ 25 \end{bmatrix}\\)</span>, which is in the set, but <span class="math-inline">\\(2 \begin{bmatrix} 3 \\\\ 4 \\\\ 25 \end{bmatrix} = \begin{bmatrix} 6 \\\\ 8 \\\\ 50 \end{bmatrix}\\)</span> is not in the set, since <span class="math-inline">\\(6^2 + 8^2 = 100 \neq 50\\)</span>.

</details>

---

## Activity 4: Finding Non-Examples of Subspaces

In this activity, you'll find sets of vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> that satisfy some, but not all, of the requirements for a subspace. Think creatively, and since we're working in <span class="math-inline">\\(\mathbb{R}^2\\)</span>, visualize the vectors!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a set of vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> such that the sum of any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> in the set is also in the set, but <span class="math-inline">\\(\frac{1}{2} \vec v\\)</span> is possibly not in the set.

<details markdown="1"><summary>Solution</summary>

One possible answer is the set of all vectors with integer components, e.g.

<div class="math-display">
$$
S = \left\{ \begin{bmatrix} a \\\\ b \end{bmatrix} \mid a, b \in \mathbb{Z} \right\}
$$
</div>

The sum of any two vectors in <span class="math-inline">\\(S\\)</span> is also in <span class="math-inline">\\(S\\)</span>, since the sum of two integers is another integer. However, <span class="math-inline">\\(\frac{1}{2} \vec v\\)</span> is not necessarily in <span class="math-inline">\\(S\\)</span>; for example, <span class="math-inline">\\(\frac{1}{2} \begin{bmatrix} 1 \\\\ 1 \end{bmatrix} = \begin{bmatrix} \frac{1}{2} \\\\ \frac{1}{2} \end{bmatrix}\\)</span> is not in <span class="math-inline">\\(S\\)</span>.

So, this <span class="math-inline">\\(S\\)</span> is a sub**set**, but not a sub**space**.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a set of vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> such that <span class="math-inline">\\(c \vec v\\)</span> is in the set for any vector <span class="math-inline">\\(\vec v\\)</span> in the set and any scalar <span class="math-inline">\\(c\\)</span>, but the sum of any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> in the set is possibly not in the set.

<details markdown="1"><summary>Solution</summary>

One possible answer is the set of all vectors in which either both components are positive, both components are negative, or both components are zero. In other words, this is the set of all vectors that exist in the top-right and bottom-left quadrants of the <span class="math-inline">\\(xy\\)</span>-plane.

<div class="math-display">
$$
S = \left\{ \begin{bmatrix} a \\\\ b \end{bmatrix} \mid a, b \in \mathbb{R}, a \geq 0, b \geq 0 \text{ or } a \leq 0, b \leq 0 \text{ or } a = 0, b = 0 \right\}
$$
</div>

![image](imgs/blank-axes.png)

Two vectors in <span class="math-inline">\\(S\\)</span>, for example, are <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 3 \end{bmatrix}\\)</span> (top right) and <span class="math-inline">\\(\begin{bmatrix} -4 \\\\ -1 \end{bmatrix}\\)</span> (bottom left). Any scalar multiple of <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 3 \end{bmatrix}\\)</span> is also in <span class="math-inline">\\(S\\)</span>; <span class="math-inline">\\(k \begin{bmatrix} 2 \\\\ 3 \end{bmatrix} = \begin{bmatrix} 2k \\\\ 3k \end{bmatrix}\\)</span> is in the top-right quadrant if <span class="math-inline">\\(k &gt; 0\\)</span> and in the bottom-left quadrant if <span class="math-inline">\\(k &lt; 0\\)</span>.

But, the sum <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 3 \end{bmatrix} + \begin{bmatrix} -4 \\\\ -1 \end{bmatrix} = \begin{bmatrix} -2 \\\\ 2 \end{bmatrix}\\)</span> is not in <span class="math-inline">\\(S\\)</span>, since it is in the second quadrant.

</details>

</div>
</div>

</div>

---

## Activity 5: Finding Bases for Subspaces

In each part below, find **two different possible bases** for the given subspace, and state the **dimension** of the subspace.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(S = \text{span} \left( \left\lbrace \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}, \begin{bmatrix} -3 \\\\ -9 \\\\ -9 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}, \begin{bmatrix} 2 \\\\ 7 \\\\ 4 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix} \right\rbrace \right)\\)</span>

<details markdown="1"><summary>Solution</summary>

Here, we'll employ the algorithm mentioned at the end of [Chapter 4.3](https://notes.eecs245.org/linear-independence/linear-independence/#algorithm-for-finding-linearly-independent-subsets-with-the-same-span) to find a linearly independent subset of <span class="math-inline">\\(S\\)</span> that spans it.

Let's call the set of vectors in our basis <span class="math-inline">\\(B\\)</span>.

-   We'll start with <span class="math-inline">\\(B = \left\lbrace \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix} \right\rbrace\\)</span>.

-   <span class="math-inline">\\(\begin{bmatrix} -3 \\\\ -9 \\\\ -9 \end{bmatrix}\\)</span> is just <span class="math-inline">\\(-3 \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>, so we won't add it.

-   <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span> is not a scalar multiple of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>. We know this because if it were the case that <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix} = k \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> for some scalar <span class="math-inline">\\(k\\)</span>, then we'd need <span class="math-inline">\\(1 = k\\)</span>, <span class="math-inline">\\(5 = 3k\\)</span>, and <span class="math-inline">\\(-1 = 3k\\)</span>, which are inconsistent. So, we'll add <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span> to <span class="math-inline">\\(B\\)</span>, which now is <span class="math-inline">\\(B = \left\lbrace \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix} \right\rbrace\\)</span>.

-   Is <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 7 \\\\ 4 \end{bmatrix}\\)</span> a linear combination of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>? To determine whether it is, we'll look for scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that



<div class="math-display">
$$
a \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix} = \begin{bmatrix} 2 \\\\ 7 \\\\ 4 \end{bmatrix}
$$
</div>

    This is equivalent to the system



<div class="math-display">
$$
\begin{align*}
    a + b &= 2 \\\\
    3a + 5b &= 7 \\\\
    3a - b &= 4
    \end{align*}
$$
</div>

    Subtracting equations 2 and 3 gives <span class="math-inline">\\(6b = 3 \implies b = \frac{1}{2}\\)</span>, and plugging this into equation 1 gives <span class="math-inline">\\(a + \frac{1}{2} = 2 \implies a = \frac{3}{2}\\)</span>. Let's check if this system is consistent. Evaluating <span class="math-inline">\\(\frac{3}{2} \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix} + \frac{1}{2} \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span> gives us



<div class="math-display">
$$
\begin{align*}
    \frac{3}{2} \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix} + \frac{1}{2} \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix} &= \begin{bmatrix} 3 / 2 \\\\ 9 / 2 \\\\ 9 / 2 \end{bmatrix} + \begin{bmatrix} 1 / 2 \\\\ 5 / 2 \\\\ -1 / 2 \end{bmatrix} \\\\
    &= \begin{bmatrix} 2 \\\\ 7 \\\\ 4 \end{bmatrix}
    \end{align*}
$$
</div>

    So, <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 7 \\\\ 4 \end{bmatrix}\\)</span> is a linear combination of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>, so we won't add it to <span class="math-inline">\\(B\\)</span>. (Remember, the point of <span class="math-inline">\\(B\\)</span> is that it is linearly independent and spans <span class="math-inline">\\(S\\)</span>.)

-   What's left is <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span>. Is it a linear combination of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>? To determine whether it is, we'll look for scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that



<div class="math-display">
$$
a \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix} = \begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}
$$
</div>

    This is equivalent to the system



<div class="math-display">
$$
\begin{align*}
    a + b &= 1 \\\\
    3a + 5b &= 4 \\\\
    3a - b &= 1
    \end{align*}
$$
</div>

    Subtracting equations 2 and 3 gives <span class="math-inline">\\(6b = 3 \implies b = \frac{1}{2}\\)</span>, and plugging this into equation 1 gives <span class="math-inline">\\(a + \frac{1}{2} = 1 \implies a = \frac{1}{2}\\)</span>. Let's check if this system is consistent. Evaluating <span class="math-inline">\\(\frac{1}{2} \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix} + \frac{1}{2} \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span> gives us <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span>.

    So, <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span> is a linear combination of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>, so we won't add it to <span class="math-inline">\\(B\\)</span>.

So, <span class="math-inline">\\(B = \left\lbrace \begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix} \right\rbrace\\)</span> is a linearly independent subset of <span class="math-inline">\\(S\\)</span> that spans <span class="math-inline">\\(S\\)</span>, i.e. it is a basis for <span class="math-inline">\\(S\\)</span>. **The dimension of <span class="math-inline">\\(S\\)</span> is 2.**

If we want another basis, we could just swap out <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> for <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span>, the most recent vector we considered adding to <span class="math-inline">\\(B\\)</span>. We didn't add <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span> to <span class="math-inline">\\(B\\)</span> since it's a linear combination of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>, but that also means that <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> is a linear combination of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>, meaning that we can create with <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span> anything we could create with <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>. So, another basis for <span class="math-inline">\\(S\\)</span> is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 1 \\\\ 4 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 5 \\\\ -1 \end{bmatrix} \right\rbrace\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(S = \left\lbrace \begin{bmatrix} v&#95;1 \\\\ v&#95;2 \end{bmatrix} \mid v&#95;1 = - v&#95;2; v&#95;1, v&#95;2 \in \mathbb{R} \right\rbrace\\)</span>

<details markdown="1"><summary>Solution</summary>

One basis for <span class="math-inline">\\(S\\)</span> is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 1 \\\\ -1 \end{bmatrix} \right\rbrace\\)</span>, since any vector in <span class="math-inline">\\(S\\)</span> is a scalar multiple of <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \end{bmatrix}\\)</span>. The dimension of <span class="math-inline">\\(S\\)</span> is 1.

Another basis for <span class="math-inline">\\(S\\)</span> is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} -5 \\\\ 5 \end{bmatrix} \right\rbrace\\)</span>. There's nothing special about the number 5 -- replace it with any other non-zero number and you'll get another basis for <span class="math-inline">\\(S\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(S = \left\lbrace \begin{bmatrix} v&#95;1 \\\\ v&#95;2 \\\\ v&#95;3 \\\\ v&#95;4 \end{bmatrix} \mid \ v&#95;4 = 0; v&#95;1, v&#95;2, v&#95;3 \in \mathbb{R} \right\rbrace\\)</span>

<details markdown="1"><summary>Solution</summary>

One basis for <span class="math-inline">\\(S\\)</span> is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix} \right\rbrace\\)</span>, since any vector in <span class="math-inline">\\(S\\)</span> is a linear combination of these three vectors. The dimension of <span class="math-inline">\\(S\\)</span> is 3.

The example basis above is perhaps the simplest possible basis for <span class="math-inline">\\(S\\)</span>, but there are infinitely many other bases for <span class="math-inline">\\(S\\)</span>. For example, other ones are

<div class="math-display">
$$
\left\{ \begin{bmatrix} 2 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ -394 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 15 \\\\ 0 \end{bmatrix} \right\}
$$
</div>

and

<div class="math-display">
$$
\left\{ \begin{bmatrix} 3 \\\\ 5 \\\\ 2 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ -394 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 15 \\\\ 0 \end{bmatrix} \right\}
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
