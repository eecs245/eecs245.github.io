---
layout: page
title: "Homework 6: Rank and Inverses"
description: "Homework 6: Rank and Inverses problems."
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

# Homework 6: Rank and Inverses

**due** Sunday, November 1st, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw06/hw06.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
Except for the video link in Problem 1, write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Pensive by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 5 Concept Video](#problem-1-homework-5-concept-video-10-pts)
- [Problem 2: Rank-Nullity Practice](#problem-2-rank-nullity-practice-8-pts)
- [Problem 3: Spaces](#problem-3-spaces-17-pts)
- [Problem 4: Finding Inverses](#problem-4-finding-inverses-5-pts)
- [Problem 5: Inverse of a Rotation](#problem-5-inverse-of-a-rotation-8-pts)
- [Problem 6: Trickster](#problem-6-trickster-3-pts)
- [Problem 7: Numbers of Solutions](#problem-7-numbers-of-solutions-12-pts)
- [Problem 8: Diagonal and Triangular Matrices](#problem-8-diagonal-and-triangular-matrices-9-pts)
- [Problem 9: Invertibility of $XX^T$](#problem-9-invertibility-of-xxt-6-pts)
- [Problem 10: Sherman-Morrison Inverse](#problem-10-sherman-morrison-inverse-14-pts)
- [Problem 11: Canva245](#problem-11-canva245-8-pts)

---

Total Points: <span class="math-inline">\\(10+8+17+5+8+3+12+9+6+14+8=100\\)</span>

---

## Problem 1: Homework 5 Concept Video (10 pts)

Record a **2- to 5-minute video** answering **one** of the prompts below. These prompts are related to the ideas in Homework 5.

<ol class="assignment-list" markdown="1" data-item-count="4" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

If you swap two columns of an orthogonal matrix, is the resulting matrix still orthogonal, and why?

</li>
<li markdown="1" value="2">

If you append to a matrix a new column equal to the sum of its first two columns, how can you update its <span class="math-inline">\\(CR\\)</span> decomposition, and does its rank change?

</li>
<li markdown="1" value="3">

If <span class="math-inline">\\(P\\)</span> projects onto a nonzero vector and <span class="math-inline">\\(R\\)</span> reflects across that same vector, does <span class="math-inline">\\(PR=P\\)</span>, <span class="math-inline">\\(PR=R\\)</span>, or neither, and why?

</li>
<li markdown="1" value="4">

Can a matrix that projects onto a nonzero vector in <span class="math-inline">\\(\mathbb R^2\\)</span> be orthogonal, and why or why not?

</li>
</ol>

The video should be **just you speaking into the camera**. Your face must be visible while you are talking for the entire video. Do not include slides, a screen recording, written work, or any other visuals.

Submit your video link to the separate assignment on Pensive called **Homework 6, Problem 1 Video Link**. You can upload your video to YouTube as unlisted, share a Zoom recording link, or share a Google Drive link; whatever works. Make sure the course staff can view the video using that link.

Your submission time for Homework 6 is the later of the two submission times: your Problem 1 video link and your regular Homework 6 PDF.

**This problem is graded on completion.** Record a video of the required length and make an honest effort to explain the question, and you will receive full credit. Your explanation does not need to be polished or perfect.

---

## Problem 2: Rank-Nullity Practice (8 pts)

In each part, identify whether the statement is true or false, and explain why.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(A\\)</span> with <span class="math-inline">\\(\text{rank}(A) = 4\\)</span> and <span class="math-inline">\\(\text{dim}(\text{colsp}(A)) = 3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(B\\)</span> with <span class="math-inline">\\(\text{rank}(B) = 3\\)</span> and <span class="math-inline">\\(\text{dim}(\text{nullsp}(B)) = 2\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) There exists a <span class="math-inline">\\(4 \times 5\\)</span> matrix <span class="math-inline">\\(C\\)</span> with <span class="math-inline">\\(\text{dim}(\text{nullsp}(C)) = 4\\)</span> and <span class="math-inline">\\(\text{dim}(\text{nullsp}(C^T)) = 1\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) There exists an invertible <span class="math-inline">\\(3 \times 3\\)</span> matrix <span class="math-inline">\\(D\\)</span> with <span class="math-inline">\\(\text{dim}(\text{nullsp}(D^T)) = 1\\)</span>.

</div>
</div>

</div>

---

## Problem 3: Spaces (17 pts)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\text{nullsp}(A) = \text{span}\left(\left\{\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix}\right\}\right)
$$
</div>

What is <span class="math-inline">\\(\text{rank}(A)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Find a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\text{nullsp}(A) = \text{span}\left(\left\{\begin{bmatrix} 2 \\\\ 2 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \\\\ 1 \end{bmatrix}\right\}\right)
$$
</div>

What is <span class="math-inline">\\(\text{rank}(A)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Find a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 1 \\\\ 5 \end{bmatrix} \in \text{colsp}(A), \quad \begin{bmatrix} 0 \\\\ 3 \\\\ 1 \end{bmatrix} \in \text{colsp}(A), \quad \begin{bmatrix} 1 \\\\ 1 \\\\ 2 \end{bmatrix} \in \text{nullsp}(A)
$$
</div>

What is <span class="math-inline">\\(\text{rank}(A)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 3 \\\\ 4 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} 8 \\\\ -2 \\\\ 3 \end{bmatrix}\\)</span>. Explain why there **does not** exist a matrix <span class="math-inline">\\(A\\)</span> such that

<div class="math-display">
$$
\vec u \in \text{colsp}(A), \quad \vec v \in \text{nullsp}(A^T)
$$
</div>

and propose one change we could make to <span class="math-inline">\\(\vec v\\)</span> that would allow such an <span class="math-inline">\\(A\\)</span> to exist.

<em>Hint: In the <a href="https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements">Orthogonal Complements example in Chapter 5.4</a>, and in <a href="https://youtu.be/dcqA-6-vYA4">this video</a>, we discuss a fact related to this question. If you want to make a claim about the required relationship between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, you need to re-prove it here. This shouldn't take too many lines of work.</em>

</div>
</div>

</div>

---

## Problem 4: Finding Inverses (5 pts)

Suppose <span class="math-inline">\\(A=BC\\)</span>, where <span class="math-inline">\\(B\\)</span> is an unknown invertible <span class="math-inline">\\(2\times2\\)</span> matrix and

<div class="math-display">
$$
A=\begin{bmatrix}1&5\\\\0&3\end{bmatrix},\qquad
C=\begin{bmatrix}1&2\\\\-1&1\end{bmatrix}
$$
</div>

 Find <span class="math-inline">\\(B^{-1}\\)</span>. For full credit, you may only use the formula for the inverse of a <span class="math-inline">\\(2\times2\\)</span> matrix **once**; you do not need to find <span class="math-inline">\\(B\\)</span> first.

---

## Problem 5: Inverse of a Rotation (8 pts)

As we've seen, the matrix

<div class="math-display">
$$
R=\begin{bmatrix}\cos\theta&-\sin\theta\\\\\sin\theta&\cos\theta\end{bmatrix}
$$
</div>

 rotates vectors in <span class="math-inline">\\(\mathbb R^2\\)</span> counterclockwise by <span class="math-inline">\\(\theta\\)</span> radians.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(R^{-1}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Now, find <span class="math-inline">\\(R\\)</span> for a rotation of <span class="math-inline">\\(\theta\\)</span> radians clockwise, i.e. for <span class="math-inline">\\(-\theta\\)</span>. What do you notice, and why?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) A linear transformation <span class="math-inline">\\(T:\mathbb R^2\to\mathbb R^2\\)</span> first rotates vectors counterclockwise by <span class="math-inline">\\(30^\circ\\)</span>, then multiplies their horizontal coordinates by <span class="math-inline">\\(5\\)</span> and their vertical coordinates by <span class="math-inline">\\(\frac12\\)</span>. Find the matrix of <span class="math-inline">\\(T^{-1}\\)</span>. <em>Hint: While it's possible to do this by first finding the matrix for <span class="math-inline">\\(T\\)</span>, that is not necessary!</em>

</div>
</div>

</div>

---

## Problem 6: Trickster (3 pts)

Find a matrix <span class="math-inline">\\(A\\)</span> that is **not equal to the identity matrix**, but where <span class="math-inline">\\(A^6 = I\\)</span>.

Once you've found your answer, explain how you found it and verify in Python that <span class="math-inline">\\(A^6=I\\)</span>. You can do this either in the Terminal (as described in [**this video**](https://youtu.be/HZtoekU9NcE)), or in the supplemental notebook for this homework, linked [**here**](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw06%2Fhw06.ipynb&branch=main) on DataHub or [**here**](https://github.com/eecs245/fa26-code/blob/main/homeworks/hw06/hw06.ipynb) in the course GitHub repository. Include a screenshot of your Python code and output.

---

## Problem 7: Numbers of Solutions (12 pts)

Recall that if <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix, <span class="math-inline">\\(\vec x \in \mathbb{R}^d\\)</span>, and <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>, then

<div class="math-display">
$$
A \vec x = \vec b
$$
</div>

 is a system of <span class="math-inline">\\(n\\)</span> equations in <span class="math-inline">\\(d\\)</span> unknowns, where the unknowns are the components of <span class="math-inline">\\(\vec x\\)</span>, i.e. <span class="math-inline">\\(x&#95;1\\)</span>, <span class="math-inline">\\(x&#95;2\\)</span>, <span class="math-inline">\\(\ldots\\)</span>, <span class="math-inline">\\(x&#95;d\\)</span>. Solving this system is equivalent to writing <span class="math-inline">\\(\vec b\\)</span> as a **linear combination of the columns of <span class="math-inline">\\(A\\)</span>**.

In each part, do two things:

<ol class="assignment-list" markdown="1" data-item-count="2" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Construct a matrix <span class="math-inline">\\(A\\)</span> for which the number of solutions (that is, number of valid <span class="math-inline">\\(\vec x\\)</span>'s) to the system <span class="math-inline">\\(A \vec x = \vec b\\)</span> is the number provided.

</li>
<li markdown="1" value="2">

Determine whether the function <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span> is one-to-one, onto, both, or neither. (See [Chapter 6.2](https://notes.eecs245.org/linear-transformations-and-projections/inverses/#inverting-a-transformation) for a refresher on the definitions.)

</li>
</ol>

The first part has been done for you as an example.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(1\\)</span>, depending on <span class="math-inline">\\(\vec b\\)</span>

<ol class="assignment-list" markdown="1" data-item-count="2" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

If there are either 0 or 1 solutions, we know that <span class="math-inline">\\(A\\)</span>'s columns must be linearly independent. This is because if a given set of vectors is linearly independent, then any linear combination of them can only be written in one way (a fact that we proved in [Chapter 4.2](https://notes.eecs245.org/linear-independence/linear-independence/#unique-linear-combinations)). <span class="math-inline">\\(A\\)</span>'s columns must also **not** span all of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, since there are some <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span> with no solutions for <span class="math-inline">\\(\vec x\\)</span>, so <span class="math-inline">\\(A\\)</span> must have fewer columns than rows.

One possible <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 \\\\ 0 &amp; 2 \\\\ 0 &amp; 0 \end{bmatrix}\\)</span>. For example, <span class="math-inline">\\(\vec b = \begin{bmatrix} -3 \\\\ 4 \\\\ 0 \end{bmatrix}\\)</span> only has a single solution for <span class="math-inline">\\(\vec x\\)</span>, which is <span class="math-inline">\\(\vec x = \begin{bmatrix} -3 \\\\ 2 \end{bmatrix}\\)</span>, while <span class="math-inline">\\(\vec c = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}\\)</span> has no solution for <span class="math-inline">\\(\vec x\\)</span>.

</li>
<li markdown="1" value="2">

The function <span class="math-inline">\\(f(\vec x) = A \vec x\\)</span> is one-to-one, but not onto. It is one-to-one because of the fact that any linear combination of <span class="math-inline">\\(A\\)</span>'s columns can only be written in one way, so if <span class="math-inline">\\(\vec x \neq \vec y\\)</span>, then <span class="math-inline">\\(A \vec x\\)</span> and <span class="math-inline">\\(A \vec y\\)</span> must also be different. It is not onto, since there are vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> (like <span class="math-inline">\\(\vec c\\)</span> above) that aren't the output of <span class="math-inline">\\(f(\vec x)\\)</span>.

</li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(\infty\\)</span>, no matter what <span class="math-inline">\\(\vec b\\)</span> is

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(\infty\\)</span>, depending on what <span class="math-inline">\\(\vec b\\)</span> is

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts)
<span class="math-inline">\\(1\\)</span>, no matter what <span class="math-inline">\\(\vec b\\)</span> is

</div>
</div>

</div>

---

## Problem 8: Diagonal and Triangular Matrices (9 pts)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) A square matrix is **diagonal** if all entries off the main diagonal are zero, as in the matrix below.

<div class="math-display">
$$
A=\begin{bmatrix}2&0&0\\\\0&-3&0\\\\0&0&4\end{bmatrix},\qquad
\vec b=\begin{bmatrix}6\\\\6\\\\8\end{bmatrix}
$$
</div>

 Write <span class="math-inline">\\(A\vec x=\vec b\\)</span> as a system of equations using the variable names <span class="math-inline">\\(x&#95;1\\)</span>, <span class="math-inline">\\(x&#95;2\\)</span>, and <span class="math-inline">\\(x&#95;3\\)</span>, and solve it by hand.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) A square matrix is **upper triangular** if all entries below the main diagonal are zero, as in the matrix below.

<div class="math-display">
$$
A=\begin{bmatrix}2&-1&3\\\\0&-3&2\\\\0&0&4\end{bmatrix},\qquad
\vec b=\begin{bmatrix}13\\\\12\\\\12\end{bmatrix}
$$
</div>

 Write <span class="math-inline">\\(A\vec x=\vec b\\)</span> as a system of equations using the variable names <span class="math-inline">\\(x&#95;1\\)</span>, <span class="math-inline">\\(x&#95;2\\)</span>, and <span class="math-inline">\\(x&#95;3\\)</span>, and solve it by hand.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose <span class="math-inline">\\(T\\)</span> is an <span class="math-inline">\\(n\times n\\)</span> upper triangular matrix whose diagonal entries are all nonzero.

<ol class="assignment-list" markdown="1" data-item-count="3" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Explain why <span class="math-inline">\\(T\vec x=\vec b\\)</span> has exactly one solution for every <span class="math-inline">\\(\vec b\in\mathbb R^n\\)</span>.

</li>
<li markdown="1" value="2">

What is the rank of <span class="math-inline">\\(T\\)</span>?

</li>
<li markdown="1" value="3">

A square matrix is **lower triangular** if all entries above the main diagonal are zero. Would the same conclusions hold if <span class="math-inline">\\(T\\)</span> were lower triangular instead?

</li>
</ol>

</div>
</div>

</div>

---

## Problem 9: Invertibility of <span class="math-inline">\\(XX^T\\)</span> (6 pts)

In [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-rank-of-x-tx), and in [this video](https://youtu.be/hOyaHqGmO1I), we proved that <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^TX)\\)</span>.

Here, you'll explore the rank of <span class="math-inline">\\(XX^T\\)</span>. Note that <span class="math-inline">\\(X^TX\\)</span> is a matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s **columns**, while <span class="math-inline">\\(XX^T\\)</span> is a matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s **rows**.

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix, and <span class="math-inline">\\(XX^T\\)</span> is invertible. Find and explain **all** inequalities that **must** be true between <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(d\\)</span>, and <span class="math-inline">\\(r = \text{rank}(X)\\)</span>.

---

## Problem 10: Sherman-Morrison Inverse (14 pts)

In EECS 280 or EECS 281, you may have learned about **memoization**, which involves storing results of an earlier calculation to help speed up future calculations. This problem involves something similar.

Suppose we have an <span class="math-inline">\\(n \times n\\)</span> matrix <span class="math-inline">\\(A\\)</span> whose inverse, <span class="math-inline">\\(A^{-1}\\)</span>, we already know. Remember that finding inverses in general is a difficult task, so once we've found one, we'd like to avoid having to invert again.

And, suppose that we need to know the inverse of

<div class="math-display">
$$
B = A + \vec u \vec v^T
$$
</div>

which is the sum of <span class="math-inline">\\(A\\)</span> and a rank 1 matrix created by taking the "outer product" of <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> (as discussed in [Chapter 5.3](https://notes.eecs245.org/matrices/rank-and-column-space/#example-vector-outer-product)). Think of <span class="math-inline">\\(B\\)</span> as a small update to <span class="math-inline">\\(A\\)</span>.

The Sherman-Morrison formula states that

<div class="math-display">
$$
B^{-1} = (A + \vec u \vec v^T)^{-1} = A^{-1} - \frac{A^{-1} \vec u \vec v^T A^{-1}}{1 + \vec v^T A^{-1} \vec u}
$$
</div>

The formula allows us to find the inverse of <span class="math-inline">\\(A + \vec u \vec v^T\\)</span> just by knowing <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(A^{-1}\\)</span>, meaning we don't need to recompute the inverse!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) To start, we'll consider a simpler case of the Sherman-Morrison formula, where <span class="math-inline">\\(A = I\\)</span>, the identity matrix. Then, since <span class="math-inline">\\(I = I^{-1}\\)</span>, the matrix we're inverting is

<div class="math-display">
$$
B = A + \vec u \vec v^T
$$
</div>

and its inverse is

<div class="math-display">
$$
B^{-1} = (I + \vec u \vec v^T)^{-1} = I - \frac{\vec u \vec v^T}{1 + \vec v^T \vec u}
$$
</div>

<span class="math-inline">\\(B\\)</span> is invertible, **except when** the denominator of the fraction above is 0, i.e. <span class="math-inline">\\(1 + \vec v^T \vec u = 0\\)</span>.

When <span class="math-inline">\\(1 + \vec v^T \vec u = 0\\)</span>, what is true about <span class="math-inline">\\(B\\)</span>?

<em>Hint: Evaluate <span class="math-inline">\\(B \vec u\\)</span>. What does the result tell you about <span class="math-inline">\\(\text{nullsp}(B)\\)</span>?</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Prove that as long as <span class="math-inline">\\(1 + \vec v^T \vec u \neq 0\\)</span>, that

<div class="math-display">
$$
(I + \vec u \vec v^T) \left( I - \frac{\vec u \vec v^T}{1 + \vec v^T \vec u} \right) = I
$$
</div>

(Yes, this involves a fair bit of algebra.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Now, let's return to the full-fledged Sherman-Morrison formula, where

<div class="math-display">
$$
B = A + \vec u \vec v^T, \qquad B^{-1} = (A + \vec u \vec v^T)^{-1} = A^{-1} - \frac{A^{-1} \vec u \vec v^T A^{-1}}{1 + \vec v^T A^{-1} \vec u}
$$
</div>

Open the **supplemental Jupyter Notebook** we've created for Homework 6, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw06%2Fhw06.ipynb&branch=main) on DataHub, or [here](https://github.com/eecs245/fa26-code/blob/main/homeworks/hw06/hw06.ipynb) in the course GitHub repository; also watch [this video](https://youtu.be/HZtoekU9NcE) first with tips on using `numpy` for linear algebra.

There, you're asked to implement the Sherman-Morrison formula, and run some experiments to quantify how much quicker using the formula is than computing the inverse of <span class="math-inline">\\(B\\)</span> from scratch.

This problem is **not autograded**. Rather, in your submission to this part, include screenshots of your implementations of functions `generate_random_data`, `invert_B_directly`,

`invert_B_with_sherman_morrison`, `run_one_experiment`, and `many_experiments_mean_sd`, along with their outputs on the provided examples.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Include screenshots of the code you used to call `many_experiments_mean_sd` for the values provided in the question, the outputs of the print statements you were asked to add, and the `plotly` line chart you were asked to create.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Answer the question posed in the Problem 10(e) section of the supplemental Jupyter Notebook. (This shouldn't be a screenshot; just write your answer in this PDF the same way you answered the other written problems.)

If you're curious, look into [Low-Rank Adaptions (LoRA)](https://www.ibm.com/think/topics/lora), a relatively recent development in large language model research! The general idea is the same as we've worked with here.

</div>
</div>

</div>

---

## Problem 11: Canva245 (8 pts)

Your goal here is to build a very basic image editing app, called **Canva245**, using what you've learned about linear transformations and matrix multiplication.

Open the **supplemental Jupyter Notebook** we've created for Homework 6, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw06%2Fhw06.ipynb&branch=main) on DataHub, or [here](https://github.com/eecs245/fa26-code/blob/main/homeworks/hw06/hw06.ipynb) in the course GitHub repository; also watch [this video](https://youtu.be/HZtoekU9NcE) first with tips on using `numpy` for linear algebra.

You won't need to submit the notebook anywhere. To get credit, complete all four tasks in the notebook and include the requested screenshots in your PDF submission to Homework 6 on Pensive, specifically under **Problem 11**. The notebook specifies what to submit for each task:

<ol class="assignment-list" markdown="1" data-item-count="4" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

**Task 1 (2 pts):** Sepia.

</li>
<li markdown="1" value="2">

**Task 2 (2 pts):** Color tint.

</li>
<li markdown="1" value="3">

**Task 3 (2 pts):** Shearing.

</li>
<li markdown="1" value="4">

**Task 4 (2 pts):** Rotation.

</li>
</ol>

{% endraw %}
