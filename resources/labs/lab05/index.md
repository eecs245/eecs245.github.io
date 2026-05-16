---
layout: page
title: "Lab 5: Vector Spaces, Subspaces, Bases, and Dimension"
description: "Lab 5: Vector Spaces, Subspaces, Bases, and Dimension activities."
nav_exclude: true
hide_footer_hr: true
---

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

Suppose <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_d \in \mathbb{R}^n\\)</span>, and that <span class="math-inline">\\(\vec b \in \text{span}(\lbrace\vec v_1, \vec v_2, \ldots, \vec v_d\rbrace)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Give a one sentence English explanation of what it means for <span class="math-inline">\\(\vec b \in \text{span}(\lbrace\vec v_1, \vec v_2, \ldots, \vec v_d\rbrace)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose that <span class="math-inline">\\(a_1 \vec v_1 + a_2 \vec v_2 + \ldots + a_d \vec v_d = \vec b\\)</span> **and** <span class="math-inline">\\(c_1 \vec v_1 + c_2 \vec v_2 + \ldots + c_d \vec v_d = \vec b\\)</span>, where at least one of the <span class="math-inline">\\(a_i\\)</span>'s is different from its corresponding <span class="math-inline">\\(c_i\\)</span>.

Using the formal definition of linear independence from [Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/), determine whether or not <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_d\\)</span> are linearly independent, and prove your answer.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find another set of coefficients <span class="math-inline">\\(k_1, k_2, \ldots, k_d\\)</span> such that

<div class="math-display">
$$
k_1 \vec v_1 + k_2 \vec v_2 + \ldots + k_d \vec v_d = \vec b
$$
</div>

and at least one of the <span class="math-inline">\\(k_i\\)</span>'s is different from its corresponding <span class="math-inline">\\(a_i\\)</span> or <span class="math-inline">\\(c_i\\)</span>.

By doing this, you're showing that if there is at least one way to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of a set of vectors, then there are infinitely many ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of those vectors; there can't just be two or three ways to do it.

</div>
</div>

</div>

---

## Activity 2: Thinking in Higher Dimensions

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_8\\)</span> are 8 vectors in <span class="math-inline">\\(\mathbb{R}^5\\)</span>. Fill in each blank below with one of the provided options, and explain your reasoning.

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
Suppose <span class="math-inline">\\(\vec u_1, \vec u_2, \ldots, \vec u_{10}\\)</span> are 10 non-zero vectors in <span class="math-inline">\\(\mathbb{R}^{11}\\)</span>.

Furthermore, suppose that <span class="math-inline">\\(\text{span}(\lbrace\vec u_1, \vec u_2, \ldots, \vec u_{10}\rbrace)\\)</span> is a 6-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^{11}\\)</span>. This means that there exists a subset of 6 of these vectors that is linearly independent and spans the same 6-dimensional subspace as the original 10 vectors; we just don't know which 6.

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

---

## Activity 4: Finding Non-Examples of Subspaces

In this activity, you'll find sets of vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> that satisfy some, but not all, of the requirements for a subspace. Think creatively, and since we're working in <span class="math-inline">\\(\mathbb{R}^2\\)</span>, visualize the vectors!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a set of vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> such that the sum of any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> in the set is also in the set, but <span class="math-inline">\\(\frac{1}{2} \vec v\\)</span> is possibly not in the set.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find a set of vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span> such that <span class="math-inline">\\(c \vec v\\)</span> is in the set for any vector <span class="math-inline">\\(\vec v\\)</span> in the set and any scalar <span class="math-inline">\\(c\\)</span>, but the sum of any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> in the set is possibly not in the set.

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(S = \left\lbrace \begin{bmatrix} v_1 \\\\ v_2 \end{bmatrix} \mid v_1 = - v_2; v_1, v_2 \in \mathbb{R} \right\rbrace\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(S = \left\lbrace \begin{bmatrix} v_1 \\\\ v_2 \\\\ v_3 \\\\ v_4 \end{bmatrix} \mid \ v_4 = 0; v_1, v_2, v_3 \in \mathbb{R} \right\rbrace\\)</span>
</div>
</div>

</div>
