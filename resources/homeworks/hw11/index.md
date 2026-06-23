---
layout: page
title: "Homework 11: Singular Value Decomposition"
description: "Homework 11: Singular Value Decomposition problems."
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
</style>

# Homework 11: Singular Value Decomposition

**due** Sunday, June 21st, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw11/hw11.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw11/hw11-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 10 Solutions Review](#problem-1-homework-10-solutions-review-10-pts)
- [Problem 2: SVD Fundamentals](#problem-2-svd-fundamentals-18-pts)
- [Problem 3: Frobenius Norm and Low-Rank Approximation](#problem-3-frobenius-norm-and-low-rank-approximation-22-pts)
- [Problem 4: Principal Components Analysis](#problem-4-principal-components-analysis-15-pts)

---

Total Points: 10 + 18 + 22 + 15 = 65

---

## Problem 1: Homework 10 Solutions Review (10 pts)

Review [the solutions to Homework 10](https://eecs245.org/resources/homeworks/hw10/). Pick **two problem parts** (for example, Problem 6b and Problem 7c) from Homework 10 in which your solutions have the most room for improvement, i.e. where they have unsound reasoning, could be significantly more efficient or clearer, etc. Include a screenshot of your solution to each problem part, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 10, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

<details markdown="1"><summary>Solution</summary>

Make sure to review the solutions to Homework 10 to figure out ways of answering questions more efficiently, as you'll need to on the Final Exam.
</details>

---

## Problem 2: SVD Fundamentals (18 pts)

Before getting started, make sure to refer to [Chapter 10.1](https://notes.eecs245.org/singular-value-decomposition/computing-svd/). These problems aren't as computationally intensive as they look; think about ways to be efficient.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(A\\)</span> be a <span class="math-inline">\\(2 \times 2\\)</span> matrix with singular value decomposition <span class="math-inline">\\(A = U \Sigma V^T\\)</span> where:

-   The first column of <span class="math-inline">\\(U\\)</span> is <span class="math-inline">\\(\vec u&#95;1 = \begin{bmatrix} 2/\sqrt{5} \\\\ 1/\sqrt{5} \end{bmatrix}\\)</span>.

-   <span class="math-inline">\\(A \vec v&#95;1 = 3 \vec u&#95;1\\)</span>, where <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix} 1/\sqrt{2} \\\\ 1/\sqrt{2} \end{bmatrix}\\)</span> is the first column of <span class="math-inline">\\(V\\)</span>.

-   The second singular value of <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(\sigma&#95;2 = 1\\)</span>.

Given this information, find <span class="math-inline">\\(U\\)</span>, <span class="math-inline">\\(\Sigma\\)</span>, and <span class="math-inline">\\(V^T\\)</span>.

<details markdown="1"><summary>Solution</summary>

We are given the first left singular vector

<div class="math-display">
$$
\vec u_1 =
\begin{bmatrix}
\frac{2}{\sqrt{5}} \\\\[4pt]
\frac{1}{\sqrt{5}}
\end{bmatrix}
$$
</div>

 and the first right singular vector

<div class="math-display">
$$
\vec v_1 = \begin{bmatrix} \frac{1}{\sqrt{2}} \\\\[4pt] \frac{1}{\sqrt{2}} \end{bmatrix}
$$
</div>

 From <span class="math-inline">\\(A \vec v&#95;1 = 3 \vec u&#95;1\\)</span>, the defining SVD relationship <span class="math-inline">\\(A \vec v&#95;i = \sigma&#95;i \vec u&#95;i\\)</span> immediately tells us that <span class="math-inline">\\(\sigma&#95;1 = 3\\)</span>. Combined with the given <span class="math-inline">\\(\sigma&#95;2 = 1\\)</span>:

<div class="math-display">
$$
\Sigma =
\begin{bmatrix}
3 & 0 \\\\[4pt]
0 & 1
\end{bmatrix}
$$
</div>

**Finding <span class="math-inline">\\(U\\)</span>:** Since <span class="math-inline">\\(U\\)</span> is orthonormal and its first column is <span class="math-inline">\\(\vec u&#95;1\\)</span>, the second column must be a unit vector orthogonal to <span class="math-inline">\\(\vec u&#95;1\\)</span>. Writing <span class="math-inline">\\(\vec u&#95;2 = \begin{bmatrix} a \\\\ b \end{bmatrix}\\)</span> and requiring orthogonality:

<div class="math-display">
$$
\frac{2}{\sqrt{5}}\,a + \frac{1}{\sqrt{5}}\,b = 0
\implies 2a + b = 0 \implies b = -2a
$$
</div>

 Imposing <span class="math-inline">\\(\|\vec u&#95;2\| = 1\\)</span>:

<div class="math-display">
$$
\sqrt{a^2 + 4a^2} = \sqrt{5}\,|a| = 1 \implies a = \frac{1}{\sqrt{5}},\; b = -\frac{2}{\sqrt{5}}
$$
</div>

 so

<div class="math-display">
$$
\boxed{U =
\begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\\\[6pt]
\frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{5}}
\end{bmatrix}}
$$
</div>

**Finding <span class="math-inline">\\(V^T\\)</span>:** We are given <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix} \frac{1}{\sqrt{2}} \\\\[4pt] \frac{1}{\sqrt{2}} \end{bmatrix}\\)</span>. The second column of <span class="math-inline">\\(V\\)</span> must be a unit vector orthogonal to <span class="math-inline">\\(\vec v&#95;1\\)</span>. Writing <span class="math-inline">\\(\vec v&#95;2 = \begin{bmatrix} c \\\\ d \end{bmatrix}\\)</span>:

<div class="math-display">
$$
\frac{1}{\sqrt{2}}\,c + \frac{1}{\sqrt{2}}\,d = 0 \implies c = -d
$$
</div>

 With <span class="math-inline">\\(\|\vec v&#95;2\| = 1\\)</span>: <span class="math-inline">\\(c = \frac{1}{\sqrt{2}}, d = -\frac{1}{\sqrt{2}}\\)</span>, giving

<div class="math-display">
$$
\boxed{V^T =
\begin{bmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\\\[6pt]
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{bmatrix}}
$$
</div>

Putting everything together, the unique singular value decomposition consistent with all the given information is:

<div class="math-display">
$$
U =
\begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\\\[6pt]
\frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{5}}
\end{bmatrix}
\qquad
\Sigma =
\begin{bmatrix}
3 & 0 \\\\[4pt]
0 & 1
\end{bmatrix}
\qquad
V^T =
\begin{bmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\\\[6pt]
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{bmatrix}
$$
</div>

 and the matrix <span class="math-inline">\\(A\\)</span> itself is therefore

<div class="math-display">
$$
A = U\Sigma V^T =
\begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\\\[6pt]
\frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{5}}
\end{bmatrix}
\begin{bmatrix}
3 & 0 \\\\[4pt]
0 & 1
\end{bmatrix}
\begin{bmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\\\[6pt]
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Let <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; 0 \\\\ 0 &amp; 1 \\\\ 2 &amp; -1 \\\\ 2 &amp; 2 \end{bmatrix}\\)</span>.

1.  Compute the singular value decomposition (that is, find <span class="math-inline">\\(U\\)</span>, <span class="math-inline">\\(\Sigma\\)</span>, and <span class="math-inline">\\(V^T\\)</span>) for <span class="math-inline">\\(X\\)</span>. Do this by hand, but use `np.linalg.svd` in Python to verify your work.

2.  Now, compute the singular value decomposition for <span class="math-inline">\\(X^T = \begin{bmatrix} 1 &amp; 0 &amp; 2 &amp; 2 \\\\ 0 &amp; 1 &amp; -1 &amp; 2 \end{bmatrix}\\)</span>. How can you reuse your work in finding the SVD of <span class="math-inline">\\(X\\)</span> to compute the SVD of <span class="math-inline">\\(X^T\\)</span>?

<details markdown="1"><summary>Solution</summary>

**(i)** To compute the singular value decomposition of

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & 0 \\\\
0 & 1 \\\\
2 & -1 \\\\
2 & 2
\end{bmatrix}
$$
</div>

 we begin by forming the matrix <span class="math-inline">\\(X^T X\\)</span>, since its eigenvalues give the squared singular values of <span class="math-inline">\\(X\\)</span>:

<div class="math-display">
$$
X^T X
=
\begin{bmatrix}
1^2 + 0^2 + 2^2 + 2^2 & 1\cdot 0 + 0\cdot 1 + 2(-1) + 2\cdot 2 \\\\[6pt]
1\cdot 0 + 0\cdot 1 + 2(-1) + 2\cdot 2 &
0^2 + 1^2 + (-1)^2 + 2^2
\end{bmatrix}
=
\begin{bmatrix}
9 & 2 \\\\[4pt]
2 & 6
\end{bmatrix}
$$
</div>

 To find the singular values, we compute the eigenvalues of this <span class="math-inline">\\(2\times 2\\)</span> matrix. Its characteristic polynomial is

<div class="math-display">
$$
p(\lambda) =
\begin{vmatrix}
9 - \lambda & 2 \\\\
2 & 6 - \lambda
\end{vmatrix}
=
(9-\lambda)(6-\lambda) - 4 = \lambda^2 - 15 \lambda + 50
$$
</div>

This factors as

<div class="math-display">
$$
p(\lambda) = \lambda^2 - 15 \lambda + 50 = (\lambda - 10)(\lambda - 5)
$$
</div>

so the two eigenvalues are <span class="math-inline">\\(\lambda&#95;1 = 10\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 5\\)</span>. The singular values of <span class="math-inline">\\(X\\)</span> are therefore

<div class="math-display">
$$
\sigma_1 = \sqrt{10} \qquad \sigma_2 = \sqrt{5}
$$
</div>

and so we've found one piece of the puzzle:

<div class="math-display">
$$
\boxed{\Sigma = \begin{bmatrix} \sqrt{10} & 0 \\\\ 0 & \sqrt{5} \\\\ 0 & 0 \\\\ 0 & 0 \end{bmatrix}}
$$
</div>

(Remember that <span class="math-inline">\\(\Sigma\\)</span> is diagonal but also the same shape as <span class="math-inline">\\(X\\)</span>, hence the extra <span class="math-inline">\\(0\\)</span>'s.)

To compute the right singular vectors (i.e. the <span class="math-inline">\\(\vec v&#95;i\\)</span>'s), we find eigenvectors of <span class="math-inline">\\(X^T X\\)</span> corresponding to the eigenvalues <span class="math-inline">\\(\lambda&#95;1 = 10\\)</span> and <span class="math-inline">\\(\lambda&#95;2 = 5\\)</span>. Recall that

<div class="math-display">
$$
X^T X =
\begin{bmatrix}
9 & 2 \\\\
2 & 6
\end{bmatrix}
$$
</div>

**Right singular vector for <span class="math-inline">\\(\lambda&#95;1 = 10\\)</span>:**

<div class="math-display">
$$
(X^T X - 10I) \vec v_1 = 0
$$
</div>



<div class="math-display">
$$
\begin{bmatrix}
9 - 10 & 2 \\\\
2 & 6 - 10
\end{bmatrix}
\begin{bmatrix}
x \\\\ y
\end{bmatrix}
=
\begin{bmatrix}
-1 & 2 \\\\
2 & -4
\end{bmatrix}
\begin{bmatrix}
x \\\\ y
\end{bmatrix}
=
\begin{bmatrix}
0 \\\\ 0
\end{bmatrix}
$$
</div>

 The first row gives <span class="math-inline">\\(-x + 2y = 0\\)</span>, so <span class="math-inline">\\(x = 2y\\)</span>. Thus an eigenvector is

<div class="math-display">
$$
\vec v_1 =
\begin{bmatrix}
2 \\\\ 1
\end{bmatrix}
$$
</div>

 Normalizing gives <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix} \frac{2}{\sqrt{5}} \\\\ \frac{1}{\sqrt{5}} \end{bmatrix}\\)</span>.

**Right singular vector for <span class="math-inline">\\(\lambda&#95;2 = 5\\)</span>:**

<div class="math-display">
$$
(X^T X - 5I) \vec v_2 = 0
$$
</div>



<div class="math-display">
$$
\begin{bmatrix}
9 - 5 & 2 \\\\
2 & 6 - 5
\end{bmatrix}
\begin{bmatrix}
x \\\\ y
\end{bmatrix}
=
\begin{bmatrix}
4 & 2 \\\\
2 & 1
\end{bmatrix}
\begin{bmatrix}
x \\\\ y
\end{bmatrix}
=
\begin{bmatrix}
0 \\\\ 0
\end{bmatrix}
$$
</div>

 The first row gives <span class="math-inline">\\(4x + 2y = 0\\)</span>, so <span class="math-inline">\\(y = -2x\\)</span>. Thus an eigenvector is

<div class="math-display">
$$
\vec v_2 =
\begin{bmatrix}
1 \\\\[4pt] -2
\end{bmatrix}
$$
</div>

 Normalizing gives <span class="math-inline">\\(\vec v&#95;2 = \begin{bmatrix} \frac{1}{\sqrt{5}} \\\\ -\frac{2}{\sqrt{5}} \end{bmatrix}\\)</span>. **Note that we could have found this vector** just by finding a vector orthogonal to <span class="math-inline">\\(\vec v&#95;1\\)</span> and normalizing it, since the columns of <span class="math-inline">\\(V\\)</span> must be orthonormal.

So, <span class="math-inline">\\(V\\)</span> is

<div class="math-display">
$$
V =
\begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\\\
\frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{5}}
\end{bmatrix}
\implies
\boxed{V^T =
\begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\\\
\frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{5}}
\end{bmatrix}}
$$
</div>

Almost there!

**Left singular vectors:** the defining SVD identity <span class="math-inline">\\(X \vec v&#95;i = \sigma&#95;i \vec u&#95;i\\)</span> allows us to compute each <span class="math-inline">\\(\vec u&#95;i\\)</span> explicitly.

For <span class="math-inline">\\(\vec u&#95;1\\)</span>,

<div class="math-display">
$$
X \vec v_1
=
\begin{bmatrix}
1 & 0 \\\\
0 & 1 \\\\
2 & -1 \\\\
2 & 2
\end{bmatrix}
\begin{bmatrix}
\frac{2}{\sqrt{5}} \\\\[4pt]
\frac{1}{\sqrt{5}}
\end{bmatrix}
=
\begin{bmatrix}
\frac{2}{\sqrt{5}} \\\\
\frac{1}{\sqrt{5}} \\\\
\frac{2(2) - 1}{\sqrt{5}} \\\\
\frac{2(2) + 2}{\sqrt{5}}
\end{bmatrix}
=
\frac{1}{\sqrt{5}}
\begin{bmatrix}
2 \\\\[4pt] 1 \\\\[4pt] 3 \\\\[4pt] 6
\end{bmatrix}
$$
</div>

 Since <span class="math-inline">\\(\sigma&#95;1 = \sqrt{10}\\)</span>, we divide to obtain

<div class="math-display">
$$
\vec u_1 = \frac{1}{\sigma_1} X v_1
= \frac{1}{\sqrt{10}}
\cdot \frac{1}{\sqrt{5}}
\begin{bmatrix}
2 \\\\ 1 \\\\ 3 \\\\ 6
\end{bmatrix}
=
\frac{1}{\sqrt{50}}
\begin{bmatrix}
2 \\\\ 1 \\\\ 3 \\\\ 6
\end{bmatrix}
$$
</div>

For <span class="math-inline">\\(\vec u&#95;2\\)</span>,

<div class="math-display">
$$
X \vec v_2
=
\begin{bmatrix}
1 & 0 \\\\
0 & 1 \\\\
2 & -1 \\\\
2 & 2
\end{bmatrix}
\begin{bmatrix}
-\frac{1}{\sqrt{5}} \\\\[4pt]
\frac{2}{\sqrt{5}}
\end{bmatrix}
=
\frac{1}{\sqrt{5}}
\begin{bmatrix}
-1 \\\\
2 \\\\
-(2)(1) - 2 \\\\
2(-1) + 4
\end{bmatrix}
=
\frac{1}{\sqrt{5}}
\begin{bmatrix}
-1 \\\\[4pt] 2 \\\\[4pt] -4 \\\\[4pt] 2
\end{bmatrix}
$$
</div>

 Since <span class="math-inline">\\(\sigma&#95;2 = \sqrt{5}\\)</span>, dividing gives

<div class="math-display">
$$
\vec u_2 = \frac{1}{\sigma_2} X \vec v_2
= \frac{1}{\sqrt{5}}
\cdot
\frac{1}{\sqrt{5}}
\begin{bmatrix}
-1 \\\\ 2 \\\\ -4 \\\\ 2
\end{bmatrix}
=
\frac{1}{5}
\begin{bmatrix}
-1 \\\\ 2 \\\\ -4 \\\\ 2
\end{bmatrix}
$$
</div>

Both <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> are already unit vectors, which we expect from the definition of the SVD, given that we started with unit vectors <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span>.

Since <span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(4\times 2\\)</span> matrix, the full SVD requires a <span class="math-inline">\\(4\times 4\\)</span> orthogonal matrix <span class="math-inline">\\(U\\)</span>. We've used

<div class="math-display">
$$
X \vec v_i = \sigma_i \vec u_i
$$
</div>

to find the first two columns of <span class="math-inline">\\(U\\)</span>, but this won't work any further, since <span class="math-inline">\\(X\\)</span> has no more non-zero singular values. Instead, we look for vectors <span class="math-inline">\\(\vec u&#95;3\\)</span> and <span class="math-inline">\\(\vec u&#95;4\\)</span> that are (1) in <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span> and (2) orthogonal to each other, as we first saw in Chapter 10.1.

Recall,

<div class="math-display">
$$
X = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 2 & -1 \\\\ 2 & 2 \end{bmatrix} \implies X^T = \begin{bmatrix} 1 & 0 & 2 & 2 \\\\ 0 & 1 & -1 & 2 \end{bmatrix}
$$
</div>

We could solve a system of equations to find vectors that span <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span>, but we've chosen numbers that are small enough to reason through without needing to do that. Since <span class="math-inline">\\(\text{rank}(X) = 2\\)</span>, we know that <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span> is of dimension <span class="math-inline">\\(4 - 2 = 2\\)</span>, so it is spanned by two vectors.

The first and second columns of <span class="math-inline">\\(X^T\\)</span> are the standard basis vectors in <span class="math-inline">\\(\mathbb{R}^2\\)</span>. The third column of <span class="math-inline">\\(X^T\\)</span> is <span class="math-inline">\\(2 \cdot \text{column 1} - \text{column 2}\\)</span>, and the fourth column of <span class="math-inline">\\(X^T\\)</span> is <span class="math-inline">\\(2 \cdot \text{column 1} + \text{column 2}\\)</span>. This tells us the vectors

<div class="math-display">
$$
\vec n_1 = \begin{bmatrix} 2 \\\\ -1 \\\\ -1 \\\\ 0 \end{bmatrix}, \vec n_2 = \begin{bmatrix} 2 \\\\ 2 \\\\ 0 \\\\ -1 \end{bmatrix}
$$
</div>

span <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span>. We can't place these in <span class="math-inline">\\(U\\)</span> directly, since they need to be orthogonal to one another, which they are not currently. (Though, they are automatically orthogonal to <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> as a consequence of the spectral theorem, which says that eigenvectors corresponding to different eigenvalues are orthogonal for symmetric matrices, and <span class="math-inline">\\(XX^T\\)</span> is symmetric. Remember that the <span class="math-inline">\\(\vec u&#95;i\\)</span>'s are eigenvectors of <span class="math-inline">\\(XX^T\\)</span>, not <span class="math-inline">\\(X^TX\\)</span>.)

To make them orthogonal while preserving their span, we can use the Gram-Schmidt process. Since we only have two vectors, this boils down to keeping <span class="math-inline">\\(\vec n&#95;1\\)</span> and computing the **error** of the projection of <span class="math-inline">\\(\vec n&#95;2\\)</span> onto <span class="math-inline">\\(\vec n&#95;1\\)</span>, which must be orthogonal to <span class="math-inline">\\(\vec n&#95;1\\)</span>.

First, let's find <span class="math-inline">\\(\vec u&#95;3\\)</span> by normalizing <span class="math-inline">\\(\vec n&#95;1\\)</span>:

<div class="math-display">
$$
\|\vec n_1\| = \sqrt{(-2)^2 + 1^2 + 1^2}
       = \sqrt{6}
\qquad
\vec u_3 = \frac{1}{\sqrt{6}}
\begin{bmatrix}
2\\\\ -1\\\\ -1\\\\ 0
\end{bmatrix}
$$
</div>

Next, we find the error of the projection of <span class="math-inline">\\(\vec n&#95;2\\)</span> onto <span class="math-inline">\\(\vec u&#95;3\\)</span>.

<div class="math-display">
$$
\begin{align*}
\vec e &= \vec n_2 - \text{proj}_{\vec u_3}(\vec n_2) \\\\
&= \vec n_2 - (\vec u_3 \cdot \vec n_2) \vec u_3 \\\\
&=
\begin{bmatrix} 2 \\\\ 2 \\\\ 0 \\\\ -1 \end{bmatrix}
- \left(
\frac{1}{\sqrt{6}}
\begin{bmatrix} 2 \\\\ -1 \\\\ -1 \\\\ 0 \end{bmatrix}
\cdot
\begin{bmatrix} 2 \\\\ 2 \\\\ 0 \\\\ -1 \end{bmatrix}
\right)
\frac{1}{\sqrt{6}}
\begin{bmatrix} 2 \\\\ -1 \\\\ -1 \\\\ 0 \end{bmatrix} \\\\
&= \begin{bmatrix} 2 \\\\ 2 \\\\ 0 \\\\ -1 \end{bmatrix} - \frac{1}{3} \begin{bmatrix} 2 \\\\ -1 \\\\ -1 \\\\ 0 \end{bmatrix} \\\\
&= \begin{bmatrix} 4/3 \\\\ 7/3 \\\\ 1/3 \\\\ -1 \end{bmatrix}
\end{align*}
$$
</div>

As a unit vector, this is

<div class="math-display">
$$
\vec u_4
= \frac{\vec e}{\lVert \vec e \rVert}
= \frac{1}{5\sqrt{3}}
\begin{bmatrix}
4\\\\ 7\\\\ 1\\\\ -3
\end{bmatrix}
$$
</div>

With these two additional vectors, the full <span class="math-inline">\\(U\\)</span> matrix is

<div class="math-display">
$$
U =
\begin{bmatrix}
\frac{2}{\sqrt{50}} & -\frac{1}{5}
                      & \frac{2}{\sqrt{6}}
                      & \frac{4}{5\sqrt{3}} \\\\[6pt]
\frac{1}{\sqrt{50}} &  \frac{2}{5}
                      & -\frac{1}{\sqrt{6}}
                      & \frac{7}{5\sqrt{3}} \\\\[6pt]
\frac{3}{\sqrt{50}} & -\frac{4}{5}
                      & -\frac{1}{\sqrt{6}}
                      & \frac{1}{5\sqrt{3}} \\\\[6pt]
\frac{6}{\sqrt{50}} &  \frac{2}{5}
                      & 0
                      & -\frac{3}{5\sqrt{3}}
\end{bmatrix}
$$
</div>

 which is now a complete orthonormal basis of <span class="math-inline">\\(\mathbb{R}^4\\)</span>. These were not the only two choices of <span class="math-inline">\\(\vec u&#95;3\\)</span> and <span class="math-inline">\\(\vec u&#95;4\\)</span>: there are infinitely many orthonormal bases for <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span>, and any of them could have been used.

So, finally, the SVD of <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; 0\\\\ 0 &amp; 1\\\\ 2 &amp; -1\\\\ 2 &amp; 2 \end{bmatrix}\\)</span> is:

<div class="math-display">
$$
X =
\underbrace{
  \begin{bmatrix}
  \frac{2}{\sqrt{50}} & -\frac{1}{5}
                        & \frac{2}{\sqrt{6}}
                        & \frac{4}{5\sqrt{3}} \\\\[6pt]
  \frac{1}{\sqrt{50}} &  \frac{2}{5}
                        & -\frac{1}{\sqrt{6}}
                        & \frac{7}{5\sqrt{3}} \\\\[6pt]
  \frac{3}{\sqrt{50}} & -\frac{4}{5}
                        & -\frac{1}{\sqrt{6}}
                        & \frac{1}{5\sqrt{3}} \\\\[6pt]
  \frac{6}{\sqrt{50}} &  \frac{2}{5}
                        & 0
                        & -\frac{3}{5\sqrt{3}}
  \end{bmatrix}
}_{U}
\;
\underbrace{
\begin{bmatrix}
\sqrt{10} & 0 \\\\
0 & \sqrt{5} \\\\
0 & 0 \\\\
0 & 0
\end{bmatrix}
}_{\Sigma}
\;
\underbrace{
\begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\\\
\frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{5}}
\end{bmatrix}
}_{V^T}
$$
</div>

**(ii)** Observe that no new computation is needed to obtain the SVD of <span class="math-inline">\\(X^T\\)</span>. Transposing the decomposition <span class="math-inline">\\(X = U \Sigma V^T\\)</span> gives

<div class="math-display">
$$
X^T = V \Sigma U^T,
$$
</div>

 which is already an SVD because <span class="math-inline">\\(\Sigma\\)</span> is diagonal and both <span class="math-inline">\\(U\\)</span> and <span class="math-inline">\\(V\\)</span> are orthonormal. Thus the left singular vectors of <span class="math-inline">\\(X\\)</span> become the right singular vectors of <span class="math-inline">\\(X^T\\)</span>, the right singular vectors of <span class="math-inline">\\(X\\)</span> become the left singular vectors of <span class="math-inline">\\(X^T\\)</span>, and the singular values remain unchanged. This reuse of the original computation highlights the symmetry built into the singular value decomposition.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Compute the singular value decomposition for the diagonal matrix <span class="math-inline">\\(X = \begin{bmatrix} 3 &amp; 0 &amp; 0 \\\\ 0 &amp; -2 &amp; 0 \\\\ 0 &amp; 0 &amp; -2 \end{bmatrix}\\)</span>.

<details markdown="1"><summary>Solution</summary>

To compute the singular value decomposition of the diagonal matrix

<div class="math-display">
$$
X = \begin{bmatrix}
3 & 0 & 0 \\\\
0 & -2 & 0 \\\\
0 & 0 & -2
\end{bmatrix}
$$
</div>

first form the matrix <span class="math-inline">\\(X^T X\\)</span>. Because <span class="math-inline">\\(X\\)</span> is diagonal, its transpose equals itself, and multiplying gives us

<div class="math-display">
$$
X^T X
=
\begin{bmatrix}
3^2 & 0 & 0 \\\\
0 & (-2)^2 & 0 \\\\
0 & 0 & (-2)^2
\end{bmatrix}
=
\begin{bmatrix}
9 & 0 & 0 \\\\
0 & 4 & 0 \\\\
0 & 0 & 4
\end{bmatrix}
$$
</div>

The singular values of <span class="math-inline">\\(X\\)</span> are defined to be the square roots of the eigenvalues of <span class="math-inline">\\(X^T X\\)</span>. Since the eigenvalues can be read directly from the diagonal, we obtain

<div class="math-display">
$$
\lambda_1 = 9 \qquad \lambda_2 = 4 \qquad \lambda_3 = 4
$$
</div>

 Taking square roots gives the singular values

<div class="math-display">
$$
\sigma_1 = \sqrt{9} = 3 \qquad
\sigma_2 = \sqrt{4} = 2 \qquad
\sigma_3 = \sqrt{4} = 2
$$
</div>

meaning

<div class="math-display">
$$
\boxed{\Sigma = \begin{bmatrix} 3 & 0 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 2 \end{bmatrix}}
$$
</div>

The eigenvectors of a diagonal matrix are just the standard basis vectors, <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>. For example, <span class="math-inline">\\(X^TX \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix} = 4 \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>. So, the matrix <span class="math-inline">\\(V\\)</span> is

<div class="math-display">
$$
V =
\boxed{\begin{bmatrix}
1 & 0 & 0\\\\
0 & 1 & 0\\\\
0 & 0 & 1
\end{bmatrix} = V^T}
$$
</div>

Here's where we need to be careful. It's tempting to use the same logic in reverse and say that <span class="math-inline">\\(U = I\\)</span> as well, but this would lead us astray. Instead, we need to make sure that each column of <span class="math-inline">\\(U\\)</span> matches up with the corresponding column of <span class="math-inline">\\(V\\)</span>, through the relationship

<div class="math-display">
$$
X \vec v_i = \sigma_i \vec u_i
$$
</div>

<div class="math-display">
$$
X \vec v_1 = 3 \vec u_1 \implies 3 \vec u_1 = \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix} \implies \vec u_1 = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

<div class="math-display">
$$
X \vec v_2 = 2 \vec u_2 \implies 2 \vec u_2 = \begin{bmatrix} 0 \\\\ -2 \\\\ 0 \end{bmatrix} \implies \vec u_2 = \begin{bmatrix} 0 \\\\ -1 \\\\ 0 \end{bmatrix}
$$
</div>

<div class="math-display">
$$
X \vec v_3 = 2 \vec u_3 \implies 2 \vec u_3 = \begin{bmatrix} 0 \\\\ 0 \\\\ -2 \end{bmatrix} \implies \vec u_3 = \begin{bmatrix} 0 \\\\ 0 \\\\ -1 \end{bmatrix}
$$
</div>

This means that

<div class="math-display">
$$
U =
\begin{bmatrix}
1 & 0 & 0\\\\
0 & -1 & 0\\\\
0 & 0 & -1
\end{bmatrix}
$$
</div>

So, the SVD of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
X
=
U \Sigma V^T
=
\underbrace{
\begin{bmatrix}
1 & 0 & 0\\\\
0 & -1 & 0\\\\
0 & 0 & -1
\end{bmatrix}
}_{U}
\underbrace{
\begin{bmatrix}
3 & 0 & 0\\\\
0 & 2 & 0\\\\
0 & 0 & 2
\end{bmatrix}
}_{\Sigma}
\underbrace{
\begin{bmatrix}
1 & 0 & 0\\\\
0 & 1 & 0\\\\
0 & 0 & 1
\end{bmatrix}
}_{V^T}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Compute the singular value decomposition for the rank-one matrix <span class="math-inline">\\(X = \begin{bmatrix} 0 &amp; 0 \\\\ 3 &amp; 4 \\\\ 6 &amp; 8 \end{bmatrix}\\)</span>.

<em>Hint: Can you write <span class="math-inline">\\(X\\)</span> as an outer product of two vectors? If you can, how do those vectors relate to the singular values and singular vectors of <span class="math-inline">\\(X\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
X =
\begin{bmatrix}
0 & 0 \\\\
3 & 4 \\\\
6 & 8
\end{bmatrix}
$$
</div>

 In <span class="math-inline">\\(X\\)</span>, note that the two non-zero rows,

<div class="math-display">
$$
\begin{bmatrix} 3 & 4 \end{bmatrix}
\qquad\text{and}\qquad
\begin{bmatrix} 6 & 8 \end{bmatrix}
$$
</div>

 are scalar multiples of each other. This means that all non-zero rows lie in the span of the single vector <span class="math-inline">\\(\begin{bmatrix} 3 &amp; 4 \end{bmatrix}\\)</span>. Because the rank of a matrix equals the dimension of the space spanned by its rows (or equivalently, its columns), we see immediately that <span class="math-inline">\\(\mathrm{rank}(X)=1\\)</span>.

Once the rank is known to be one, the **hint** suggests looking for an outer--product factorization. Indeed, every rank--one matrix can be written in the form

<div class="math-display">
$$
X = \vec u\, \vec v^T
$$
</div>

 where <span class="math-inline">\\(\vec u\in\mathbb{R}^3\\)</span> and <span class="math-inline">\\(\vec v \in\mathbb{R}^2\\)</span>. We obtain the correct factorization by observing that each row of <span class="math-inline">\\(X\\)</span> is a scalar multiple of the vector <span class="math-inline">\\(\begin{bmatrix} 3 &amp; 4 \end{bmatrix}\\)</span>:

<div class="math-display">
$$
X =
\begin{bmatrix}
0 \\\\
1 \\\\
2
\end{bmatrix}
\begin{bmatrix}
3 & 4
\end{bmatrix}
=
\vec u \vec v^T
\qquad
\vec u =
\begin{bmatrix}
0 \\\\ 1 \\\\ 2
\end{bmatrix}
\quad
\vec v =
\begin{bmatrix}
3 \\\\ 4
\end{bmatrix}
$$
</div>

Writing <span class="math-inline">\\(X\\)</span> in this form makes the relationship to the singular value decomposition slightly clearer. The SVD of a rank-1 matrix always takes the form

<div class="math-display">
$$
X = \sigma_1\, \vec u_1 \vec v_1^T
$$
</div>

 where <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;1\\)</span> are unit vectors. All we need to do is normalize the <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> we found; the extra constant factors are placed into <span class="math-inline">\\(\sigma&#95;1\\)</span>.

<div class="math-display">
$$
\vec u_1 = \frac{\vec u}{\lVert \vec u \rVert} = \frac{1}{\sqrt{5}} \begin{bmatrix} 0 \\\\ 1 \\\\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\\\ \frac{1}{\sqrt{5}} \\\\ \frac{2}{\sqrt{5}} \end{bmatrix}
$$
</div>

<div class="math-display">
$$
\vec v_1 = \frac{\vec v}{\lVert \vec v \rVert} = \frac{1}{5} \begin{bmatrix} 3 \\\\ 4 \end{bmatrix} = \begin{bmatrix} \frac{3}{5} \\\\ \frac{4}{5} \end{bmatrix}
$$
</div>

The matrix <span class="math-inline">\\(X\\)</span> can now be expressed as

<div class="math-display">
$$
X = (\sqrt{5})(5)\; \vec u_1 \vec v_1^T
= 5\sqrt{5}\; \vec u_1 \vec v_1^T
$$
</div>

 This shows that the single non-zero singular value is

<div class="math-display">
$$
\sigma_1 = 5\sqrt{5} \implies \boxed{\Sigma = \begin{bmatrix} 5\sqrt{5} & 0 \\\\ 0 & 0 \\\\ 0 & 0 \end{bmatrix}}
$$
</div>

Since <span class="math-inline">\\(X\\)</span> is <span class="math-inline">\\(3\times 2\\)</span>, the matrices <span class="math-inline">\\(U\in\mathbb{R}^{3\times 3}\\)</span> and <span class="math-inline">\\(V\in\mathbb{R}^{2\times 2}\\)</span> must be completed with additional orthonormal columns. The remaining singular values must be zero, so we choose any orthonormal vectors orthogonal to <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;1\\)</span> to complete each matrix.

A convenient choice for the remaining column of <span class="math-inline">\\(V\\)</span> is

<div class="math-display">
$$
\vec v_2 =
\begin{bmatrix}
-\frac{4}{5}\\\\[4pt]
\frac{3}{5}
\end{bmatrix}
$$
</div>

 which satisfies <span class="math-inline">\\(\vec v&#95;1 \cdot \vec v&#95;2 = 0\\)</span> and has unit length. So,

<div class="math-display">
$$
V = \begin{bmatrix}
\frac{3}{5} & -\frac{4}{5}\\\\[4pt]
\frac{4}{5} & \frac{3}{5}
\end{bmatrix},
\qquad
\boxed{V^T =
\begin{bmatrix}
\frac{3}{5} & \frac{4}{5}\\\\[4pt]
-\frac{4}{5} & \frac{3}{5}
\end{bmatrix}}
$$
</div>

To complete the matrix <span class="math-inline">\\(U\\)</span>, we need two additional orthonormal vectors that are orthogonal to

<div class="math-display">
$$
\vec u_1 =
\begin{bmatrix}
0 \\\\[4pt] \tfrac{1}{\sqrt{5}} \\\\[4pt] \tfrac{2}{\sqrt{5}}
\end{bmatrix}
$$
</div>

We can follow a similar pattern to that of <span class="math-inline">\\(V\\)</span> and use

<div class="math-display">
$$
\vec u_2 = \begin{bmatrix} 0 \\\\ -\frac{2}{\sqrt{5}} \\\\ \frac{1}{\sqrt{5}} \end{bmatrix}
$$
</div>

as one vector. As the final vector, note that both <span class="math-inline">\\(\vec u&#95;1\\)</span> and <span class="math-inline">\\(\vec u&#95;2\\)</span> have 0 as their first component, so both are orthogonal to

<div class="math-display">
$$
\vec u_3 = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

Placing these <span class="math-inline">\\(\vec u&#95;i\\)</span>'s in the columns of <span class="math-inline">\\(U\\)</span> gives us

<div class="math-display">
$$
U =
\begin{bmatrix}
0 & 0 & 1 \\\\
\frac{1}{\sqrt{5}} &  -\frac{2}{\sqrt{5}} & 0 \\\\
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} & 0
\end{bmatrix}
$$
</div>

 Putting everything together, the singular value decomposition of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
X = U \Sigma V^T
=
\underbrace{
\begin{bmatrix}
  0 & 0 & 1 \\\\
  \frac{1}{\sqrt{5}} &  -\frac{2}{\sqrt{5}} & 0 \\\\
  \frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} & 0
  \end{bmatrix}
}_{U}
\;
\underbrace{
\begin{bmatrix}
5\sqrt{5} & 0 \\\\
0 & 0 \\\\
0 & 0
\end{bmatrix}
}_{\Sigma}
\;
\underbrace{
\begin{bmatrix}
\frac{3}{5} & \frac{4}{5} \\\\
-\frac{4}{5} & \frac{3}{5}
\end{bmatrix}
}_{V^T}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 3: Frobenius Norm and Low-Rank Approximation (22 pts)

As we first saw in Chapter 2.1, the norm of a vector is a measure of its size. The "default" norm is the Euclidean, or <span class="math-inline">\\(L&#95;2\\)</span> norm, <span class="math-inline">\\(\lVert \vec v \rVert&#95;2 = \sqrt{v&#95;1^2 + v&#95;2^2 + \cdots + v&#95;n^2}\\)</span>.

Similarly, the norm of a matrix is a measure of its size. The most common matrix norm is the **Frobenius norm**, defined as

<div class="math-display">
$$
\lVert X \rVert_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^d x_{ij}^2}
$$
</div>

 That is, <span class="math-inline">\\(\lVert X \rVert&#95;F\\)</span> is the square root of the sum of the squares of the elements of <span class="math-inline">\\(X\\)</span>; it treats <span class="math-inline">\\(X\\)</span> as a vector and computes its <span class="math-inline">\\(L&#95;2\\)</span> norm.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Verify that <span class="math-inline">\\(\lVert X \rVert&#95;F = \sqrt{15}\\)</span> for <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; 0 \\\\ 0 &amp; 1 \\\\ 2 &amp; -1 \\\\ 2 &amp; 2 \end{bmatrix}\\)</span>.

*Notice that <span class="math-inline">\\(\sqrt{15} = \sqrt{10 + 5}\\)</span>, and in Problem 2a), you found that <span class="math-inline">\\(X\\)</span>'s singular values were <span class="math-inline">\\(\sigma&#95;1 = \sqrt{10}\\)</span> and <span class="math-inline">\\(\sigma&#95;2 = \sqrt{5}\\)</span>. We build on this idea in part **c)**.*

<details markdown="1"><summary>Solution</summary>

To compute the Frobenius norm of the matrix

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & 0 \\\\
0 & 1 \\\\
2 & -1 \\\\
2 & 2
\end{bmatrix}
$$
</div>

 we use the definition

<div class="math-display">
$$
\|X\|_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^d x_{ij}^2}
$$
</div>

 which tells us to square every entry of the matrix, sum those squares, and then take a square root.

Writing out the squares of all eight entries and simplifying gives

<div class="math-display">
$$
\|X\|_F^2
= 1^2 + 0^2 + 0^2 + 1^2 + 2^2 + (-1)^2 + 2^2 + 2^2 = 15
$$
</div>

Therefore,

<div class="math-display">
$$
\|X\|_F = \sqrt{15}
$$
</div>

Notice that <span class="math-inline">\\(\sqrt{15}\\)</span> is also equal to <span class="math-inline">\\(\sqrt{10 + 5}\\)</span>, and <span class="math-inline">\\(\sqrt{10}\\)</span> and <span class="math-inline">\\(\sqrt{5}\\)</span> are the singular values of <span class="math-inline">\\(X\\)</span> from Problem 2a. We build on this connection shortly.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Another equivalent formula for the Frobenius norm is

<div class="math-display">
$$
\lVert X \rVert_F^2 = \text{trace}(X^T X)
$$
</div>

 where <span class="math-inline">\\(\text{trace}(X^T X)\\)</span> is the sum of the diagonal entries of <span class="math-inline">\\(X^TX\\)</span>. (Notice the square on the left-hand side!) **Explain why** this is equivalent to the first definition of the Frobenius norm.

<details markdown="1"><summary>Solution</summary>

To see why the identity

<div class="math-display">
$$
\|X\|_F^2 = \operatorname{trace}(X^T X)
$$
</div>

 matches the original definition of the Frobenius norm, it's helpful to examine what the matrix product <span class="math-inline">\\(X^T X\\)</span> looks like entry by entry. Recall that the Frobenius norm is defined by

<div class="math-display">
$$
\|X\|_F^2 = \sum_{i=1}^n \sum_{j=1}^d x_{ij}^2
$$
</div>

 which is the sum of the squares of all entries of <span class="math-inline">\\(X\\)</span>.

Now consider the matrix <span class="math-inline">\\(X^T X\\)</span>. This matrix contains the dot products of all pairs of columns of <span class="math-inline">\\(X\\)</span>. Along its diagonal, it contains the dot products of each column with itself. That is, element <span class="math-inline">\\((k,k)\\)</span> of <span class="math-inline">\\(X^T X\\)</span> is the dot product of the <span class="math-inline">\\(k\\)</span>-th column of <span class="math-inline">\\(X\\)</span> with itself, **which is just the sum of the squares of the entries in the <span class="math-inline">\\(k\\)</span>-th column of <span class="math-inline">\\(X\\)</span>**.

<div class="math-display">
$$
(X^TX)_{kk} = (\text{column } k \text{ of } X) \cdot (\text{column } k \text{ of } X) = \sum_{i=1}^n x_{ik}^2
$$
</div>

The trace of a matrix is the sum of its diagonal entries, so

<div class="math-display">
$$
\operatorname{trace}(X^T X) = \sum_{k=1}^d (X^T X)_{kk} = \sum_{k=1}^d \left( \text{column } k \text{ of } X \cdot \text{column } k \text{ of } X \right) = \sum_{k=1}^d \sum_{i=1}^n x_{ik}^2
$$
</div>

This sum loops over every single entry of <span class="math-inline">\\(X\\)</span> exactly once and sums its square, just as the original definition of the Frobenius norm did!

This shows that

<div class="math-display">
$$
\|X\|_F^2 = \operatorname{trace}(X^T X)
$$
</div>

 is equivalent to the definition

<div class="math-display">
$$
\|X\|_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^d x_{ij}^2 }
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Another equivalent formula for the Frobenius norm is

<div class="math-display">
$$
\lVert X \rVert_F^2 = \sum_{i=1}^r \sigma_i^2
$$
</div>

 where <span class="math-inline">\\(\sigma&#95;1, \sigma&#95;2, \ldots, \sigma&#95;r\\)</span> are the singular values of <span class="math-inline">\\(X\\)</span> and <span class="math-inline">\\(r = \text{rank}(X)\\)</span>. **Explain why** this is equivalent to the definition of the Frobenius norm from part **b)**. <em>Hint: What is the relationship between the singular values of <span class="math-inline">\\(X\\)</span> and the eigenvalues of some other matrix?</em>

<details markdown="1"><summary>Solution</summary>

The goal is to understand why the Frobenius norm can also be written in terms of the singular values of <span class="math-inline">\\(X\\)</span>. From **part b)**, we already know that

<div class="math-display">
$$
\|X\|_F^2 = \operatorname{trace}(X^T X)
$$
</div>

 so it's enough to explain why the trace of <span class="math-inline">\\(X^T X\\)</span> is equal to the sum of the squares of the singular values.

The **hint** suggests recalling the relationship between the singular values of a matrix and the eigenvalues of another matrix.

Here's the key: in the singular value decomposition, the singular values <span class="math-inline">\\(\sigma&#95;1,\ldots,\sigma&#95;r\\)</span> of <span class="math-inline">\\(X\\)</span> are defined to be the square roots of the non-zero eigenvalues of the symmetric matrix <span class="math-inline">\\(X^T X\\)</span>. If we denote these eigenvalues by

<div class="math-display">
$$
\lambda_1, \lambda_2, \ldots, \lambda_r,
$$
</div>

 then the SVD tells us that

<div class="math-display">
$$
\lambda_i = \sigma_i^2 \qquad \text{for each } i=1,\ldots,r
$$
</div>

But, from [Chapter 9.2](https://notes.eecs245.org/eigenvalues-and-eigenvectors/characteristic-polynomial/#trace-and-determinant), we know that the trace of a matrix is the sum of its eigenvalues, so

<div class="math-display">
$$
\operatorname{trace}(X^T X) = \lambda_1 + \lambda_2 + \cdots + \lambda_r
$$
</div>

But, <span class="math-inline">\\(\lambda&#95;1 + \lambda&#95;2 + \cdots + \lambda&#95;r = \sigma&#95;1^2 + \sigma&#95;2^2 + \cdots + \sigma&#95;r^2\\)</span>, and <span class="math-inline">\\(\lVert X \rVert&#95;F^2 = \operatorname{trace}(X^T X)\\)</span>, so

<div class="math-display">
$$
\lVert X \rVert_F^2 = \operatorname{trace}(X^T X) = \lambda_1 + \lambda_2 + \cdots + \lambda_r = \sigma_1^2 + \sigma_2^2 + \cdots + \sigma_r^2
$$
</div>

and thus

<div class="math-display">
$$
\lVert X \rVert_F^2 = \sum_{i=1}^r \sigma_i^2
$$
</div>

 as required.
</details>

The Frobenius norm allows us to make more precise the idea of a rank-<span class="math-inline">\\(k\\)</span> approximation of a matrix, first introduced in [Chapter 10.2](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation/).

Suppose <span class="math-inline">\\(X = U \Sigma V^T\\)</span> is the singular value decomposition of the <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(X\\)</span>, where the columns of <span class="math-inline">\\(U\\)</span> are <span class="math-inline">\\(\vec u&#95;1, \vec u&#95;2, \ldots, \vec u&#95;n \in \mathbb{R}^n\\)</span>, the singular values of <span class="math-inline">\\(X\\)</span> are <span class="math-inline">\\(\sigma&#95;1, \sigma&#95;2, \ldots, \sigma&#95;r &gt; 0\\)</span>, the rows of <span class="math-inline">\\(V^T\\)</span> are <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d \in \mathbb{R}^d\\)</span>, and <span class="math-inline">\\(r = \text{rank}(X)\\)</span>.

The Eckart--Young--Mirsky theorem states that, for any integer <span class="math-inline">\\(k\\)</span> between 1 and <span class="math-inline">\\(r\\)</span>, the <span class="math-inline">\\(n \times d\\)</span> matrix

<div class="math-display">
$$
X_k = \sum_{i=1}^k \sigma_i \vec u_i \vec v_i^T
$$
</div>

 is the closest rank-<span class="math-inline">\\(k\\)</span> matrix to <span class="math-inline">\\(X\\)</span>, in terms of Frobenius norm. That is, if <span class="math-inline">\\(Y\\)</span> is any other <span class="math-inline">\\(n \times d\\)</span> matrix of rank <span class="math-inline">\\(k\\)</span>, then <span class="math-inline">\\(\lVert X - X&#95;k \rVert&#95;F \leq \lVert X - Y \rVert&#95;F\\)</span>. More intuitively, this says that <span class="math-inline">\\(X&#95;k\\)</span> is the matrix with the smallest mean squared error from <span class="math-inline">\\(X\\)</span>, among all <span class="math-inline">\\(n \times d\\)</span> matrices of rank <span class="math-inline">\\(k\\)</span>. We will not prove this theorem in class.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Let's illustrate the above with an example. Consider the <span class="math-inline">\\(3 \times 4\\)</span> matrix <span class="math-inline">\\(X\\)</span>, whose singular value decomposition is given by

<div class="math-display">
$$
\underbrace{\begin{bmatrix} 24 & 0 & 0 & 24 \\\\ 7 & 25 & 25 & 7 \\\\ 1 & -1 & 1 & -1 \end{bmatrix}}_{X} = \underbrace{\begin{bmatrix} 0.6 & 0.8 & 0 \\\\ 0.8 & -0.6 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}}_{U} \underbrace{\begin{bmatrix} 40 & 0 & 0 & 0 \\\\ 0 & 30 & 0 & 0 \\\\ 0 & 0 & 2 & 0 \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} 1/2 & 1/2 & 1/2 & 1/2 \\\\ 1/2 & -1/2 & -1/2 & 1/2 \\\\ 1/2 & -1/2 & 1/2 & -1/2 \\\\ -1/2 & -1/2 & 1/2 & 1/2 \end{bmatrix}}_{V^T}
$$
</div>

For <span class="math-inline">\\(k = 1, 2, 3\\)</span>, compute the rank-<span class="math-inline">\\(k\\)</span> approximation <span class="math-inline">\\(X&#95;k = \sum&#95;{i=1}^k \sigma&#95;i \vec u&#95;i \vec v&#95;i^T\\)</span> and the Frobenius norm of the approximation error, <span class="math-inline">\\(\lVert X - X&#95;k \rVert&#95;F\\)</span>.

Feel free to do the computations by hand or using `numpy`. If you use `numpy`, make sure to include screenshots of any code you write and its outputs, and **don't** use `np.linalg.svd`; instead, enter the SVD we provided you with and use `np.outer` to compute the outer product of two vectors.

<details markdown="1"><summary>Solution</summary>

The matrix <span class="math-inline">\\(X\\)</span> is given together with its singular value decomposition

<div class="math-display">
$$
X = U \Sigma V^T
$$
</div>

 where

<div class="math-display">
$$
U =
\begin{bmatrix}
0.6 & 0.8 & 0 \\\\
0.8 & -0.6 & 0 \\\\
0 & 0 & 1
\end{bmatrix}
\qquad
\Sigma =
\begin{bmatrix}
40 & 0 & 0 & 0 \\\\
0 & 30 & 0 & 0 \\\\
0 & 0 & 2 & 0
\end{bmatrix}
\qquad
V^T =
\begin{bmatrix} 1/2 & 1/2 & 1/2 & 1/2 \\\\ 1/2 & -1/2 & -1/2 & 1/2 \\\\ 1/2 & -1/2 & 1/2 & -1/2 \\\\ -1/2 & -1/2 & 1/2 & 1/2 \end{bmatrix}
$$
</div>

 Thus its singular values are

<div class="math-display">
$$
\sigma_1 = 40 \qquad \sigma_2 = 30 \qquad \sigma_3 = 2
$$
</div>

 and the corresponding singular vectors are the columns of <span class="math-inline">\\(U\\)</span> and <span class="math-inline">\\(V\\)</span>.

The Eckart--Young--Mirsky theorem states that the best rank--<span class="math-inline">\\(k\\)</span> approximation of <span class="math-inline">\\(X\\)</span> in Frobenius norm is

<div class="math-display">
$$
X_k = \sum_{i=1}^k \sigma_i\, \vec u_i \vec v_i^T
$$
</div>

 which is a sum of outer products.

#### Rank-1 approximation

The relevant outer product is

<div class="math-display">
$$
\vec u_1 \vec v_1^T
=
\begin{bmatrix}
0.6\\\\ 0.8\\\\ 0
\end{bmatrix}
\begin{bmatrix}
1/2 & 1/2 & 1/2 & 1/2
\end{bmatrix}
=
\begin{bmatrix}
0.3 & 0.3 & 0.3 & 0.3\\\\
0.4 & 0.4 & 0.4 & 0.4\\\\
0   & 0   & 0   & 0
\end{bmatrix}
$$
</div>

 So the rank-1 approximation is

<div class="math-display">
$$
X_1 = 40\, \vec u_1 \vec v_1^T
=
\begin{bmatrix}
12 & 12 & 12 & 12\\\\
16 & 16 & 16 & 16\\\\
0  & 0  & 0  & 0
\end{bmatrix}
$$
</div>

To compute the approximation error, we subtract:

<div class="math-display">
$$
X - X_1 =
\begin{bmatrix}
24 & 0 & 0 & 24 \\\\
7 & 25 & 25 & 7 \\\\
1 & -1 & 1 & -1
\end{bmatrix}
-
\begin{bmatrix}
12 & 12 & 12 & 12\\\\
16 & 16 & 16 & 16\\\\
0  & 0  & 0  & 0
\end{bmatrix}
=
\begin{bmatrix}
12 & -12 & -12 & 12\\\\
-9 & 9 & 9 & -9 \\\\
1 & -1 & 1 & -1
\end{bmatrix}
$$
</div>

 The Frobenius norm is

<div class="math-display">
$$
\|X - X_1\|_F^2
=
4(12^2) + 4(9^2) + 4(1^2)
= 4(144 + 81 + 1)
= 4(226)
= 904
$$
</div>

 Thus

<div class="math-display">
$$
\boxed{\|X - X_1\|_F = \sqrt{904}}
$$
</div>

Notice that <span class="math-inline">\\(\sqrt{904}\\)</span> is also equal to <span class="math-inline">\\(\sqrt{30^2 + 2^2}\\)</span>, which is the square root of the sum of the singular values past the first one!

#### Rank-2 approximation

We now include a second outer product:

<div class="math-display">
$$
\vec u_2 \vec v_2^T
=
\begin{bmatrix}
0.8\\\\ -0.6\\\\ 0
\end{bmatrix}
\begin{bmatrix}
1/2 & -1/2 & -1/2 & 1/2
\end{bmatrix}
=
\begin{bmatrix}
0.4 & -0.4 & -0.4 & 0.4\\\\
-0.3 & 0.3 & 0.3 & -0.3\\\\
0 & 0 & 0 & 0
\end{bmatrix}
$$
</div>

 Multiplying by <span class="math-inline">\\(\sigma&#95;2 = 30\\)</span> gives

<div class="math-display">
$$
30\,\vec u_2 \vec v_2^T
=
\begin{bmatrix}
12 & -12 & -12 & 12\\\\
-9 & 9 & 9 & -9 \\\\
0 & 0 & 0 & 0
\end{bmatrix}
$$
</div>

Thus the rank-2 approximation is

<div class="math-display">
$$
X_2 = \sigma_1 \vec u_1 \vec v_1^T + \sigma_2 \vec u_2 \vec v_2^T = X_1 + 30 \vec u_2 \vec v_2^T
=
\begin{bmatrix}
24 & 0 & 0 & 24\\\\
7 & 25 & 25 & 7\\\\
0 & 0 & 0 & 0
\end{bmatrix}
$$
</div>

The approximation error is now

<div class="math-display">
$$
X - X_2 =
\begin{bmatrix}
0 & 0 & 0 & 0\\\\
0 & 0 & 0 & 0\\\\
1 & -1 & 1 & -1
\end{bmatrix}
$$
</div>

 Hence

<div class="math-display">
$$
\|X - X_2\|_F^2
= 1^2 + (-1)^2 + 1^2 + (-1)^2
= 4
\qquad
\boxed{\|X - X_2\|_F = 2}
$$
</div>

#### Rank-3 approximation

<span class="math-inline">\\(X\\)</span> itself is rank 3, so a rank-3 approximation of it is just <span class="math-inline">\\(X\\)</span> itself. If you sum <span class="math-inline">\\(\sigma&#95;1 \vec u&#95;1 \vec v&#95;1^T + \sigma&#95;2 \vec u&#95;2 \vec v&#95;2^T + \sigma&#95;3 \vec u&#95;3 \vec v&#95;3^T\\)</span>, you will get back <span class="math-inline">\\(X\\)</span>.

Now we summarizing all three rank--<span class="math-inline">\\(k\\)</span> approximations and their errors:

<div class="math-display">
$$

$$
</div>

\begin{aligned}
X_1 &= 40 u_1 v_1^T
&\quad \|X - X_1\|_F &= \sqrt{904}\\[6pt]
X_2 &= 40u_1 v_1^T + 30u_2 v_2^T
&\quad \|X - X_2\|_F &= 2\\[6pt]
X_3 &= X
&\quad \|X - X_3\|_F &= 0
\end{aligned}

<div class="math-display">
$$

$$
</div>

Note that the Frobenius norm of the approximation error is decreasing as we add more outer products --- specifically, the error for the rank-<span class="math-inline">\\(k\\)</span> approximation is <span class="math-inline">\\(\sqrt{\sum&#95;{i=k+1}^r \sigma&#95;i^2}\\)</span>, i.e. the sum of the squares of the singular values past the <span class="math-inline">\\(k\\)</span>-th one.

Here are the rank-<span class="math-inline">\\(k\\)</span> approximation computations done using `numpy`.

<div style="text-align: center;">
<img src="imgs/hw11-prob3c-ss1.png" alt="image" style="width: 100%; max-width: 100%;">
</div>

<div style="text-align: center;">
<img src="imgs/hw11-prob3c-ss2.png" alt="image" style="width: 100%; max-width: 100%;">
</div>

<div style="text-align: center;">
<img src="imgs/hw11-prob3c-ss3.png" alt="image" style="width: 100%; max-width: 100%;">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Open the **the supplemental Jupyter Notebook** we've created for Homework 11, which can either be found [here](https://github.com/eecs245/sp26-code/blob/main/homeworks/hw11/hw11.ipynb) in the course GitHub repository, or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw11%2Fhw11.ipynb&branch=main) on DataHub.

There, you're asked to implement the rank-<span class="math-inline">\\(k\\)</span> approximation of an image of your choosing, similar to the [Image Compression example in Chapter 10.2](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation/#example-image-compression).

More instructions are provided in the notebook. This problem is **not autograded**. Rather, in your submission to this part, include screenshots of all of your code and outputs here.

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="imgs/hw11-prob3e-sol.png" alt="image" style="width: 100%; max-width: 100%;">
</div>

<div style="text-align: center;">
<img src="imgs/hw11-prob3e-plot.png" alt="image" style="width: 100%; max-width: 100%;">
</div>
</details>

</div>
</div>

</div>

---

## Problem 4: Principal Components Analysis (15 pts)

**Make sure you've completed Problem 3 before attempting this problem.**

This problem involves a practical exploration of principal components analysis (PCA), perhaps the most interesting application of the singular value decomposition.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open `homeworks/hw11/hw11.ipynb`. For instructions on how to do this, see the [Tech Support](https://eecs245.org/env-setup/#option-1-local-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw11%2Fhw11.ipynb&branch=main) to open `hw11.ipynb` on DataHub. Before doing so, read the instructions on the [Tech Support](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

**This problem is NOT autograded**. Instead, complete the five tasks mentioned in Problem 4, and include screenshots of all of your code and outputs here, along with your written answers to Tasks 3 and 5.

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="imgs/hw11-prob4-sol.png" alt="image" style="width: 100%; max-width: 100%;">
</div>

<div style="text-align: center;">
<img src="imgs/PC 2 vs PC 1 for World Bank Data.png" alt="image" style="width: 100%; max-width: 100%;">
</div>

<div style="text-align: center;">
<img src="imgs/scree-plot-variance-explained-by-principal-components-top-10.png" alt="image" style="width: 100%; max-width: 100%;">
</div>

<div style="text-align: center;">
<img src="imgs/hw11-prob4-10-features.png" alt="image" style="width: 100%; max-width: 100%;">
</div>
</details>

{% endraw %}
