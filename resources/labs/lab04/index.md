---
layout: page
title: "Lab 4: Projections, Span, and Linear Independence"
description: "Lab 4: Projections, Span, and Linear Independence activities."
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

# Lab 4: Projections, Span, and Linear Independence

**due** for completion at 11:59PM Ann Arbor Time on Monday, May 18th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab04/lab04.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Presidential Speeches and Cosine Similarity](#activity-1-presidential-speeches-and-cosine-similarity)
- [Activity 2: Orthogonal Projections](#activity-2-orthogonal-projections)
- [Activity 3: Orthogonal Decomposition](#activity-3-orthogonal-decomposition)
- [Activity 4: Planes and the Cross Product](#activity-4-planes-and-the-cross-product)
- [Activity 5: Finding a Linearly Independent Subset](#activity-5-finding-a-linearly-independent-subset)

---

## Recap: Projections, Span, and Linear Independence

-   ([Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/)) The **orthogonal projection** of the vector <span class="math-inline">\\(\vec u\\)</span> onto the vector <span class="math-inline">\\(\vec v\\)</span> is given by 

<div class="math-display">
$$
\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v
$$
</div>

 Above, the scalar <span class="math-inline">\\(k^* = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v}\\)</span> was chosen to minimize <span class="math-inline">\\(\lVert \vec u - k \vec v \rVert^2\\)</span>.

-   The vector <span class="math-inline">\\(\vec p\\)</span> is called the orthogonal projection because the resulting error vector, 

<div class="math-display">
$$
\vec e = \vec u - \vec p = \vec u - k^* \vec v
$$
</div>

 is orthogonal to <span class="math-inline">\\(\vec v\\)</span>. 

<div class="math-display">
$$
\vec e \cdot \vec v = 0
$$
</div>

-   ([4.1](https://notes.eecs245.org/linear-independence/span/)) The **span** of a set of vectors is the set of all possible linear combinations of the vectors in the set. 

<div class="math-display">
$$
\text{span}(\{\vec v_1, \vec v_2, \ldots, \vec v_d\}) = \{a_1 \vec v_1 + a_2 \vec v_2 + \cdots + a_d \vec v_d \mid a_1, a_2, \ldots, a_d \in \mathbb{R}\}
$$
</div>

-   The span of one vector in <span class="math-inline">\\(\mathbb{R}^n\\)</span> is a line through the origin.

-   The span of two **non-parallel** vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> is a plane through the origin; this plane is called a **2-dimensional subspace** of <span class="math-inline">\\(\mathbb{R}^n\\)</span>.

-   In general, the span of <span class="math-inline">\\(d\\)</span> vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> is a subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> of dimension <span class="math-inline">\\(0\\)</span> to <span class="math-inline">\\(d\\)</span>, depending on the vectors and their relationships.

-   Think of a <span class="math-inline">\\(d\\)</span>-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> as a "slice" of <span class="math-inline">\\(\mathbb{R}^n\\)</span> that goes through the origin, in which you can move in <span class="math-inline">\\(d\\)</span> directions.

---

## Activity 1: Presidential Speeches and Cosine Similarity

Complete the tasks in the `lab04.ipynb` notebook.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/sp26-code/tree/main/labs/lab04/lab04.ipynb), and open `labs/lab04/lab04.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Flabs%2Flab04%2Flab04.ipynb&branch=main) to open `lab04.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

Once you're done, include a screenshot of your completed Activity 1 implementation in your PDF submission of Lab 4 to Gradescope, making sure to include proof that the (local) autograder passed. Instructions on how to do this are in the lab notebook.

---

## Activity 2: Orthogonal Projections

Let <span class="math-inline">\\(\vec c = \begin{bmatrix} 1 \\\\ 2 \\\\ -4 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec d = \begin{bmatrix} 3 \\\\ 2 \\\\ 0 \\\\ -1 \end{bmatrix}\\)</span>. Note that <span class="math-inline">\\(\lVert \vec c \rVert^2 = 21, \lVert \vec d \rVert^2 = 14\\)</span>, and <span class="math-inline">\\(\vec c \cdot \vec d = 7\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find the orthogonal projection of <span class="math-inline">\\(\vec c\\)</span> onto <span class="math-inline">\\(\vec d\\)</span>. Call this vector <span class="math-inline">\\(\vec q\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find the error vector, <span class="math-inline">\\(\vec r = \vec c - \vec q\\)</span>. Which vector is <span class="math-inline">\\(\vec r\\)</span> orthogonal to, <span class="math-inline">\\(\vec c\\)</span> or <span class="math-inline">\\(\vec d\\)</span>? Draw a rough picture of the relationship between <span class="math-inline">\\(\vec c\\)</span>, <span class="math-inline">\\(\vec d\\)</span>, <span class="math-inline">\\(\vec q\\)</span>, and <span class="math-inline">\\(\vec r\\)</span>.

</div>
</div>

</div>

---

## Activity 3: Orthogonal Decomposition

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(\vec{v}_1 = \begin{bmatrix} -1 \\\\ 2 \\\\ 2 \end{bmatrix}\\)</span> <span class="math-inline">\\(\vec{v}_2 = \begin{bmatrix} 2 \\\\ 2 \\\\ -1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec{v}_3 = \begin{bmatrix} 2 \\\\ -1 \\\\ 2 \end{bmatrix}\\)</span>. Write <span class="math-inline">\\(\vec{u} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span> as a linear combination of <span class="math-inline">\\(\vec{v}_1\\)</span>, <span class="math-inline">\\(\vec{v}_2\\)</span>, and <span class="math-inline">\\(\vec{v}_3\\)</span>, and verify that your answer is correct. Note that <span class="math-inline">\\(\vec v_1\\)</span>, <span class="math-inline">\\(\vec v_2\\)</span>, and <span class="math-inline">\\(\vec v_3\\)</span> are pairwise orthogonal.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
In general, suppose that <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_d\\)</span> are **orthogonal** vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>, meaning that <span class="math-inline">\\(\vec v_i \cdot \vec v_j = 0\\)</span> for all <span class="math-inline">\\(i \neq j\\)</span>. **Given that** it is possible to write <span class="math-inline">\\(\vec u\\)</span> as a linear combination of <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_d\\)</span>,

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

<em>Hint: Start by taking the dot product of both sides of the linear combination equation with <span class="math-inline">\\(\vec v_1\\)</span>. What do you notice?</em>

</div>
</div>

</div>

---

## Activity 4: Planes and the Cross Product

An important idea from [Chapter 4.1](https://notes.eecs245.org/linear-independence/span/) is that two non-parallel vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> (where <span class="math-inline">\\(n \geq 2\\)</span>) span a plane in <span class="math-inline">\\(n\\)</span>-dimensional space. Here, we'll show you how to find the equation of such a plane, given two vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. This is also touched on in [Chapter 4.4](https://notes.eecs245.org/linear-independence/lines-planes-hyperplanes/).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Given two vectors <span class="math-inline">\\(\vec a, \vec b \in \mathbb{R}^3\\)</span>, show that the vector <span class="math-inline">\\(\vec q\\)</span> is orthogonal to both <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span>.

<div class="math-display">
$$
\vec q = \begin{bmatrix} a_2 b_3 - a_3 b_2 \\\\ a_3 b_1 - a_1 b_3 \\\\ a_1 b_2 - a_2 b_1 \end{bmatrix}
$$
</div>

 The vector <span class="math-inline">\\(\vec q\\)</span> is called the **cross product** of <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span>. The cross product is only defined for two vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> specifically, and the product is another vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. (This differentiates it from the dot product, which is defined for two vectors in any <span class="math-inline">\\(\mathbb{R}^n\\)</span>, and whose output is a scalar.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find the cross product of <span class="math-inline">\\(\vec v_1 = \begin{bmatrix} 2 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v_2 = \begin{bmatrix} 1 \\\\ 2 \\\\ -1 \end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(\vec q = \begin{bmatrix} q_1 \\\\ q_2 \\\\ q_3 \end{bmatrix}\\)</span> be your answer to part **b)**.

Verify that the points <span class="math-inline">\\((0, 0, 0)\\)</span>, <span class="math-inline">\\((2, -1, 3)\\)</span> and <span class="math-inline">\\((1, 2, -1)\\)</span> satisfy the equation 

<div class="math-display">
$$
q_1 x + q_2 y + q_3 z = 0
$$
</div>

(Those points are the endpoints of the vectors <span class="math-inline">\\(\vec v_1\\)</span> and <span class="math-inline">\\(\vec v_2\\)</span>, along with the origin.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Above, we wrote the equation of the plane spanned by <span class="math-inline">\\(\vec v_1\\)</span> and <span class="math-inline">\\(\vec v_2\\)</span> in the "standard form" for planes in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, <span class="math-inline">\\(ax + by + cz + d = 0\\)</span> (where <span class="math-inline">\\(d = 0\\)</span>). Now, write the equation of the plane spanned by <span class="math-inline">\\(\vec v_1\\)</span> and <span class="math-inline">\\(\vec v_2\\)</span> in **parametric** form. The parametric form of a plane is given by

<div class="math-display">
$$
P = \vec p_0 + s \vec u + t \vec v, \quad s, t \in \mathbb{R}
$$
</div>

This won't require much work; it's more that we want you to understand that there are two ways of expressing planes in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. In higher dimensions, all planes (also called 2-dimensional subspaces) must be expressed in parametric form. Read [Chapter 4.4](https://notes.eecs245.org/linear-independence/lines-planes-hyperplanes/).

</div>
</div>

</div>

---

## Activity 5: Finding a Linearly Independent Subset

Recall from [Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/#finding-linearly-independent-subsets-with-the-same-span) that a set of vectors <span class="math-inline">\\(\vec v_1, \vec v_2, \ldots, \vec v_d\\)</span> is **linearly independent** if either of the following equivalent conditions hold:

-   None of the vectors can be written as a linear combination of the others.

-   The only way to create the zero vector as a linear combination of the vectors is if all the coefficients are zero. In other words, the only solution to 

<div class="math-display">
$$
a_1 \vec v_1 + a_2 \vec v_2 + \ldots + a_d \vec v_d = \vec 0
$$
</div>

 is <span class="math-inline">\\(a_1 = a_2 = \ldots = a_d = 0\\)</span>.

[Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/#finding-linearly-independent-subsets-with-the-same-span) introduces an algorithm for finding a linearly independent subset of a given set of vectors with the same span as the original set:

    given v_1, v_2, ..., v_d
    initialize linearly independent set S = {v_1}
    for i = 2 to d:
   if v_i is not a linear combination of S:
            add v_i to S

In each of the parts below, find **a linearly independent** set of vectors that spans the same span as the given set of vectors. There are multiple possible answers for each part, but all of them have the same number of vectors.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<div class="math-display">
$$
\vec v_1 = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}, \quad \vec v_2 = \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \quad \vec v_3 = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}, \quad \vec v_4 = \begin{bmatrix} 2 \\\\ 3 \\\\ 4 \end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<div class="math-display">
$$
\vec v_1 = \begin{bmatrix} 1 \\\\ -1 \\\\ 0 \\\\ 0 \end{bmatrix}, \quad \vec v_2 = \begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\\\ 0 \end{bmatrix}, \quad \vec v_3 = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ -1 \end{bmatrix}, \quad \vec v_4 = \begin{bmatrix} 0 \\\\ 1 \\\\ -1 \\\\ 0 \end{bmatrix}, \quad \vec v_5 = \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \\\\ -1 \end{bmatrix}, \quad \vec v_6 = \begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ -1 \end{bmatrix}
$$
</div>

<em>Hint: Use the 0's in the vectors strategically, plus use the fact that you can't have more than 4 linearly independent vectors in <span class="math-inline">\\(\mathbb{R}^4\\)</span>.</em>
</div>
</div>

</div>
