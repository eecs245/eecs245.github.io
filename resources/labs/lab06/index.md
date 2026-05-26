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

---

## Activity 2: Fundamentals

Let <span class="math-inline">\\(X=\begin{bmatrix}1 &amp; 2 &amp; -1 &amp; 3 &amp; 4 &amp; 4 \\\\ 2 &amp; 5 &amp; -2 &amp; 7 &amp; 11 &amp; 10 \\\\ 4 &amp; 8 &amp; -4 &amp; 12 &amp; 16 &amp; 16\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>. What is <span class="math-inline">\\(\text{rank}(X)\\)</span>? Why? <em>Hint: Column 5 is a linear combination of columns 1 and 2. With this fact, you should be able to answer this relatively quickly.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blanks: <span class="math-inline">\\(\text{colsp}(X^T)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Fill in the blanks: <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is a \_\_\_\_-dimensional subspace of \_\_\_\_.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Find a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. <em>Hint: You should be able to answer this without solving equations.</em>

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Under what conditions is <span class="math-inline">\\(\text{rank}(A) = 2\\)</span>? What about <span class="math-inline">\\(\text{rank}(A) &lt; 2\\)</span>? <em>Hint: First, think about what happens when multiplying <span class="math-inline">\\(A\\)</span> by a vector <span class="math-inline">\\(\vec x \in \mathbb{R}^n\\)</span>. Can you write this as a linear combination of some other vectors? The case for <span class="math-inline">\\(\text{rank}(A) = 2\\)</span> is more complicated than "<span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec w\\)</span> are linearly independent."</em>

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
How do you know that <span class="math-inline">\\(A^T\vec y= \vec 0\\)</span> has solutions other than <span class="math-inline">\\(\vec y=\vec 0\\)</span>?

</div>
</div>

</div>

---

## Activity 5: Symbolic Inverses

Given that <span class="math-inline">\\(A\\)</span> is an invertible <span class="math-inline">\\(n \times n\\)</span> matrix that satisfies <span class="math-inline">\\(A^4 - 3A^2 + 2A - 4I = 0\\)</span>, find an expression for <span class="math-inline">\\(A^{-1}\\)</span> in terms of <span class="math-inline">\\(A\\)</span>.

---

## Activity 6: Basics of Invertibility

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix. State as many of the equivalent conditions for invertibility as you can.

---

## Activity 7: Programming

Complete the tasks in the `lab06.ipynb` notebook. Watch [this video](https://youtu.be/HZtoekU9NcE) first with tips on using `numpy` for linear algebra.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/HZtoekU9NcE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/sp26-code/tree/main/labs/lab06/lab06.ipynb), and open `labs/lab06/lab06.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Flabs%2Flab06%2Flab06.ipynb&branch=main) to open `lab06.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

Once you're done, include a screenshot of your completed Activity 7 implementation in your PDF submission of Lab 6 to Gradescope, making sure to include proof that the (local) autograder passed. Instructions on how to do this are in the lab notebook.

{% endraw %}
