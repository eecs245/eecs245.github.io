---
layout: page
title: "Lab 3: Vectors and the Dot Product"
description: "Lab 3: Vectors and the Dot Product activities."
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

# Lab 3: Vectors and the Dot Product

**due** for completion at 11:59PM Ann Arbor Time on Wednesday, May 13th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Linear Combinations](#activity-1-linear-combinations)
- [Activity 2: The Dot Product](#activity-2-the-dot-product)
- [Activity 3: Angles and Orthogonality](#activity-3-angles-and-orthogonality)
- [Activity 4: Sum--Difference Orthogonality](#activity-4-sum--difference-orthogonality)
- [Activity 5: Triangle Inequality](#activity-5-triangle-inequality)
- [Activity 6: Arrays in NumPy](#activity-6-arrays-in-numpy)

---

## Recap: Vectors and the Dot Product

-   ([Chapters 3.1](https://notes.eecs245.org/vectors/vectors-and-linear-combinations/) and [3.2](https://notes.eecs245.org/vectors/norms/)) The **norm** of a vector <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span> measures its length: 

<div class="math-display">
$$
\lVert \vec v \rVert = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}
$$
</div>

 This is the default norm for vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span>, but other norms exist.

-   ([3.1](https://notes.eecs245.org/vectors/vectors-and-linear-combinations/)) A **linear combination** of the vectors <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2, \dots,\vec v&#95;d\\)</span> is any vector that can be written as 

<div class="math-display">
$$
a_1\vec v_1 + a_2\vec v_2+\dots+a_d\vec v_d
$$
</div>

 where <span class="math-inline">\\(a&#95;1, a&#95;2, \dots, a&#95;d\\)</span> are scalars. We can think of this as taking bits of each vector and adding them together. The <span class="math-inline">\\(a&#95;i\\)</span>'s are called the **coefficients** of the linear combination.

-   ([3.3](https://notes.eecs245.org/vectors/dot-product/)) The **dot product** of two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> is defined as: 

<div class="math-display">
$$
\vec u \cdot \vec v = \begin{bmatrix}u_1 \\\\ u_2 \\\\ \dots \\\\ u_n\end{bmatrix} \cdot \begin{bmatrix}v_1 \\\\ v_2 \\\\ \dots \\\\ v_n\end{bmatrix} = u_1v_1 + u_2v_2 + \dots + u_nv_n
$$
</div>

 The result is a **scalar**, not another vector.

-   ([3.3](https://notes.eecs245.org/vectors/dot-product/)) The dot product also has a geometric definition, involving the norms (lengths) of the vectors and the angle between them: 

<div class="math-display">
$$
\vec u \cdot \vec v = ||\vec u|| ||\vec v|| \text{cos}\theta
$$
</div>

-   ([3.3](https://notes.eecs245.org/vectors/dot-product/)) The key takeaway from the dot product is that it tells us how similar the directions of two vectors are. When two vectors have a dot product of 0, they are **orthogonal**, or have a 90 degree angle between them.

---

## Activity 1: Linear Combinations

Let <span class="math-inline">\\(\vec u = \begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec v = \begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec w = \begin{bmatrix} -6 \\\\ 9 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that <span class="math-inline">\\(a \vec u + b \vec v = \vec w\\)</span>. By finding <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>, you have written <span class="math-inline">\\(\vec w\\)</span> as a **linear combination** of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>.

<details markdown="1"><summary>Solution</summary>

We can pose this problem as solving a system of equations. By scalar multiplication, we have:

<div class="math-display">
$$
\begin{align*}
a \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} &= \begin{bmatrix} -6 \\\\ 9 \end{bmatrix} \\\\
\begin{bmatrix} 4a \\\\ 3a \end{bmatrix} + \begin{bmatrix} -b \\\\ -3b \end{bmatrix} &= \begin{bmatrix} -6 \\\\ 9 \end{bmatrix} \\\\
\begin{bmatrix} 4a - b \\\\ 3a - 3b \end{bmatrix} &= \begin{bmatrix} -6 \\\\ 9 \end{bmatrix}
\end{align*}
$$
</div>

The vector equation on the last line is equivalent to the system of equations:

<div class="math-display">
$$
\begin{cases}
  4a - b &= -6 \\\\
  3a - 3b &= 9
\end{cases}
$$
</div>

So, we just need to solve this system of equations to find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>.

To do so, we can multiply the first equation by 3 to get:

<div class="math-display">
$$
\begin{cases}
  12a - 3b &= -18 \\\\
  3a - 3b &= 9
\end{cases}
$$
</div>

Then, we can subtract the second equation from the first to get:

<div class="math-display">
$$
9a = -27 \implies a = -3
$$
</div>

Substituting <span class="math-inline">\\(a = -3\\)</span> back into the second equation, we get:

<div class="math-display">
$$
3(-3) - 3b = 9 \implies -9 - 3b = 9 \implies -3b = 18 \implies b = -6
$$
</div>

So, we have <span class="math-inline">\\(\boxed{a = -3}\\)</span> and <span class="math-inline">\\(\boxed{b = -6}\\)</span>.

To verify that this solution works, we can substitute <span class="math-inline">\\(a = -3\\)</span> and <span class="math-inline">\\(b = -6\\)</span> back into the original equation:

<div class="math-display">
$$
(-3)\begin{bmatrix}4\\\\3\end{bmatrix} + (-6)\begin{bmatrix}-1\\\\-3\end{bmatrix}
= \begin{bmatrix}-12\\\\-9\end{bmatrix} + \begin{bmatrix}6\\\\18\end{bmatrix}
= \begin{bmatrix}-6\\\\9\end{bmatrix}=\vec w
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now, try and write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span>. In other words, try and find values of <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that

<div class="math-display">
$$
a \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} + c \begin{bmatrix} 2 \\\\ 1 \end{bmatrix} = \vec w
$$
</div>

What happens? Why?

<details markdown="1"><summary>Solution</summary>

We can start by trying to solve the corresponding system of equations: 

<div class="math-display">
$$
\begin{cases}
4a - b + 2c = -6\\\\
3a - 3b + c = 9
\end{cases}
$$
</div>

There are 2 equations and 3 unknowns, **which means thare are infinitely many solutions for <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span>**.

What's the linear algebra reason for this?

-   With just <span class="math-inline">\\(\begin{bmatrix}4\\\\3\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-1\\\\-3\end{bmatrix}\\)</span>, you can already create any other vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>. That is, any vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span> can be written as a linear combination of <span class="math-inline">\\(\begin{bmatrix}4\\\\3\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-1\\\\-3\end{bmatrix}\\)</span>.

-   That is, for **any** vector <span class="math-inline">\\(\vec w \in \mathbb{R}^2\\)</span> (not just the one in this question), there exist **unique values** of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that 

<div class="math-display">
$$
a \begin{bmatrix}4\\\\3\end{bmatrix} + b \begin{bmatrix}-1\\\\-3\end{bmatrix} = \vec w
$$
</div>

-   Since <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span> already can create any other vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>, adding <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> to the linear combination doesn't "unlock" any new vectors --- we can still create any other vector in <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

-   But, because <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> already can be created using <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span>, adding it to the linear combination makes it so that there are infinitely many solutions for <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> in 

<div class="math-display">
$$
a \begin{bmatrix}4\\\\3\end{bmatrix} + b \begin{bmatrix}-1\\\\-3\end{bmatrix} + c \begin{bmatrix}2\\\\1\end{bmatrix} = \vec w
$$
</div>

If there are infinitely many solutions, how do we find them? Let's treat <span class="math-inline">\\(c\\)</span> as a free variable, and solve for <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> in terms of <span class="math-inline">\\(c\\)</span>.

<div class="math-display">
$$
\begin{cases}
4a - b + 2c = -6\\\\
3a - 3b + c = 9
\end{cases}
$$
</div>

Multiplying the first equation by 3 gives us:

<div class="math-display">
$$
\begin{cases}
12a - 3b + 6c = -18\\\\
3a - 3b + c = 9
\end{cases}
$$
</div>

Subtracting the second equation from the (new) first gives us:

<div class="math-display">
$$
9a + 5c = -27 \implies a = -3 - \frac{5}{9}c
$$
</div>

Similarly, multiplying the first equation by 3 and the second equation by 4 gives us:

<div class="math-display">
$$
\begin{cases}
12a - 3b + 6c = -18\\\\
12a - 12b + 4c = 36
\end{cases}
$$
</div>

Subtracting the (new) second equation from the (new) first gives us:

<div class="math-display">
$$
9b + 2c = -54 \implies b = -6 - \frac{2}{9}c
$$
</div>

So, the values of <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> that satisfy

<div class="math-display">
$$
a \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + b \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} + c \begin{bmatrix} 2 \\\\ 1 \end{bmatrix} = \begin{bmatrix} -6 \\\\ 9 \end{bmatrix}
$$
</div>

are

<div class="math-display">
$$
\boxed{a = -3 - \frac{5}{9}c, \qquad b = -6 - \frac{2}{9}c, \qquad c = c, c \in \mathbb{R}}
$$
</div>

<span class="math-inline">\\(c\\)</span> can be anything, which is why there are infinitely many solutions. If we let <span class="math-inline">\\(c = 0\\)</span>, then we get back <span class="math-inline">\\(a = -3\\)</span> and <span class="math-inline">\\(b = -6\\)</span> from part **a)**. But, say, if we let <span class="math-inline">\\(c = -9\\)</span>, then we get <span class="math-inline">\\(a = 2\\)</span> and <span class="math-inline">\\(b = -4\\)</span>, which also works:

<div class="math-display">
$$
2 \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} - 4 \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} + (-9) \begin{bmatrix} 2 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 8 \\\\ 6 \end{bmatrix} - \begin{bmatrix} -4 \\\\ -12 \end{bmatrix} + \begin{bmatrix} -18 \\\\ -9 \end{bmatrix} = \begin{bmatrix} -6 \\\\ 9 \end{bmatrix} = \vec w
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Now, try and write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -4 \\\\ -2 \end{bmatrix}\\)</span>. What happens? Why?

<details markdown="1"><summary>Solution</summary>

Note <span class="math-inline">\\(\begin{bmatrix}-4\\\\-2\end{bmatrix}=-2\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, which means these vectors point in the same direction, or lie on the same line. (The formal term is that these vectors are **collinear**.)

Since <span class="math-inline">\\(\vec w=\begin{bmatrix}-6\\\\9\end{bmatrix}\\)</span> is not a scalar multiple of <span class="math-inline">\\(\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span> (ratios <span class="math-inline">\\(-6/2=-3\\)</span> vs. <span class="math-inline">\\(9/1=9\\)</span> disagree), **no solution exists**!

To conclude, because the two vectors <span class="math-inline">\\(\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-4\\\\-2\end{bmatrix}\\)</span> are collinear, it is impossible to write <span class="math-inline">\\(\vec w\\)</span> as a linear combination of them. The only possible linear combinations are of the form <span class="math-inline">\\(c \begin{bmatrix}2\\\\1\end{bmatrix}\\)</span> for some <span class="math-inline">\\(c \in \mathbb{R}\\)</span>.

</details>

</div>
</div>

</div>

---

## Activity 2: The Dot Product

For each pair of vectors below (1) draw them on the grid at the bottom of the page and (2) compute their dot product.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot 1 + 6\cdot 0 = 8.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} -5 \\\\ 0 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot (-5) + 6\cdot 0 = -40.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 6 \\\\ 8 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot 6 + 6\cdot 8 = 48 + 48 = 96.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} 8 \\\\ 6 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot 8 + 6\cdot 6 = 64 + 36 = 100.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\begin{bmatrix} 8 \\\\ 6 \end{bmatrix} \text { and } \begin{bmatrix} -3 \\\\ 4 \end{bmatrix}\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
8\cdot (-3) + 6\cdot 4 = -24 + 24 = 0.
$$
</div>

Since the dot product is <span class="math-inline">\\(0\\)</span>, the vectors are **orthogonal**.

</details>

![image](imgs/activity-2-blank-grid.png)

<details markdown="1"><summary>Solution</summary>

![image](imgs/activity-3-solutions.png)

</details>

</div>
</div>

</div>

---

## Activity 3: Angles and Orthogonality

In this activity, we will investigate the relationship between the two definitions of the dot product and learn how to use this equivalence to measure the similarity between two vectors. 

<div class="math-display">
$$
\vec u \cdot \vec v = \begin{bmatrix}u_1 \\\\ u_2 \\\\ \dots \\\\ u_n\end{bmatrix} \cdot \begin{bmatrix}v_1 \\\\ v_2 \\\\ \dots \\\\ v_n\end{bmatrix} = u_1v_1 + u_2v_2 + \dots + u_nv_n
$$
</div>

 

<div class="math-display">
$$
\vec u \cdot \vec v = ||\vec u|| ||\vec v|| \text{cos}\theta
$$
</div>

 Let <span class="math-inline">\\(\vec w=\begin{bmatrix}5\\\\0\\\\-4\\\\1\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec x=\begin{bmatrix}9\\\\1\\\\2\\\\3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\vec w \cdot \vec x\\)</span>, <span class="math-inline">\\(\lVert \vec w \rVert\\)</span>, and <span class="math-inline">\\(\lVert \vec x \rVert\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\vec w \cdot \vec x = 5\cdot 9 + 0\cdot 1 + (-4)\cdot 2 + 1\cdot 3 = 45 + 0 - 8 + 3 = \boxed{40}.
$$
</div>

 

<div class="math-display">
$$
\lVert \vec w \rVert = \sqrt{5^2 + 0^2 + (-4)^2 + 1^2} = \sqrt{25 + 0 + 16 + 1} = \boxed{\sqrt{42}}.
$$
</div>

 

<div class="math-display">
$$
\lVert \vec x \rVert = \sqrt{9^2 + 1^2 + 2^2 + 3^2} = \sqrt{81 + 1 + 4 + 9} = \boxed{\sqrt{95}}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Using the results of part **a)**, find the angle between <span class="math-inline">\\(\vec w\\)</span> and <span class="math-inline">\\(\vec x\\)</span>. Leave your answer in the form <span class="math-inline">\\(\cos^{-1}(\cdot)\\)</span>.

<details markdown="1"><summary>Solution</summary>

Using <span class="math-inline">\\(\vec w \cdot \vec x=\|\vec w\|\,\|\vec x\|\cos\theta\\)</span>, 

<div class="math-display">
$$
\cos \theta = \frac{\vec w \cdot \vec x}{\|\vec w\|\,\|\vec x\|}
= \frac{40}{\sqrt{42}\,\sqrt{95}}.
$$
</div>

 Therefore 

<div class="math-display">
$$
\boxed{\;\theta = \cos^{-1}\!\left(\frac{40}{\sqrt{42\cdot 95}}\right)\;}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
What is <span class="math-inline">\\(\cos(90^\circ)\\)</span>? What does this have to do with orthogonality?

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\cos(90^\circ)=0.
$$
</div>

 If the angle <span class="math-inline">\\(\theta\\)</span> between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(90^\circ\\)</span>, then 

<div class="math-display">
$$
\vec u\cdot\vec v=\|\vec u\|\,\|\vec v\|\cos\theta=\|\vec u\|\,\|\vec v\| \cdot 0 = 0,
$$
</div>

 so the vectors are **orthogonal**. Conversely, if <span class="math-inline">\\(\vec u\cdot\vec v=0\\)</span> (and neither vector is the zero vector), then <span class="math-inline">\\(\cos\theta=0\\)</span> and <span class="math-inline">\\(\theta=90^\circ\\)</span>.

</details>

</div>
</div>

</div>

---

## Activity 4: Sum--Difference Orthogonality

Let <span class="math-inline">\\(\vec u=\begin{bmatrix}2\\\\-1\\\\0\\\\5\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\2\\\\4\\\\-3\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Show that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal.

<details markdown="1"><summary>Solution</summary>

Let's start by computing the two vectors: 

<div class="math-display">
$$
\vec u+\vec v=\begin{bmatrix}3\\\\1\\\\4\\\\2\end{bmatrix},\qquad
\vec u-\vec v=\begin{bmatrix}1\\\\-3\\\\-4\\\\8\end{bmatrix}.
$$
</div>

 Their dot product is 

<div class="math-display">
$$
(\vec u+\vec v)\cdot(\vec u-\vec v)
=3\cdot1+1\cdot(-3)+4\cdot(-4)+2\cdot 8
=3-3-16+16
=0.
$$
</div>

 Since the dot product is <span class="math-inline">\\(0\\)</span>, the vectors are orthogonal.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now suppose <span class="math-inline">\\(\vec u,\vec v\in\mathbb{R}^n\\)</span> are arbitrary vectors with the same number of components. Is it always true that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal?

-   If so, prove why.

-   If not, specify conditions under which it's guaranteed that <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal.

<em>Hint: Use the distributive property of the dot product, which states that </em>

<div class="math-display">
$$
(\vec a + \vec b) \cdot (\vec c + \vec d) = \vec a \cdot \vec c + \vec a \cdot \vec d + \vec b \cdot \vec c + \vec b \cdot \vec d
$$
</div>

<details markdown="1"><summary>Solution</summary>

For any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, 

<div class="math-display">
$$
(\vec u+\vec v)\cdot(\vec u-\vec v)
= \vec u\cdot\vec u - \vec u\cdot\vec v + \vec v\cdot\vec u - \vec v\cdot\vec v
= \|\vec u\|^2 - \|\vec v\|^2,
$$
</div>

 since <span class="math-inline">\\(\vec u\cdot\vec v=\vec v\cdot\vec u\\)</span>.

So, in order for <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> to be orthogonal, we need 

<div class="math-display">
$$
\|\vec u\|^2 - \|\vec v\|^2 = 0
$$
</div>

 which means 

<div class="math-display">
$$
\|\vec u\| = \|\vec v\|
$$
</div>

So, <span class="math-inline">\\(\vec u+\vec v\\)</span> and <span class="math-inline">\\(\vec u-\vec v\\)</span> are orthogonal if (and only if!) the two vectors have equal length. That was the case in part **a)** --- both vectors had a norm of <span class="math-inline">\\(\sqrt{2^2 + (-1)^2 + 0^2 + 5^2} = \sqrt{30}\\)</span>.

</details>

</div>
</div>

</div>

---

## Activity 5: Triangle Inequality

The triangle inequality states that for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n:\\)</span> 

<div class="math-display">
$$
\lVert \vec u + \vec v \rVert \leq \lVert \vec u \rVert + \lVert \vec v \rVert
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
**For the vectors <span class="math-inline">\\(\vec u = \begin{bmatrix} 4 \\\\ 3 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} -1 \\\\ -3 \end{bmatrix}\\)</span>**, verify that the triangle inequality holds. That is, show that the left-hand side is less than or equal to the right-hand side.

<details markdown="1"><summary>Solution</summary>

First, let's find <span class="math-inline">\\(\lVert \vec u + \vec v \rVert\\)</span>.

<div class="math-display">
$$
\begin{align*}
\lVert \vec u + \vec v \rVert
&= \left\lVert \begin{bmatrix} 4 \\\\ 3 \end{bmatrix} + \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} \right\rVert \\\\
&= \left\lVert \begin{bmatrix} 4-1 \\\\ 3-3 \end{bmatrix} \right\rVert \\\\
&= \left\lVert \begin{bmatrix} 3 \\\\ 0 \end{bmatrix} \right\rVert \\\\
&= \sqrt{3^2 + 0^2} \\\\
&= \sqrt{9} \\\\
&= 3
\end{align*}
$$
</div>

We found that <span class="math-inline">\\(\lVert \vec u \rVert = 5\\)</span> in part **a)**. What's <span class="math-inline">\\(\lVert \vec v \rVert\\)</span>?

<div class="math-display">
$$
\begin{align*}
\lVert \vec v \rVert
&= \left\lVert \begin{bmatrix} -1 \\\\ -3 \end{bmatrix} \right\rVert \\\\
&= \sqrt{(-1)^2 + (-3)^2} \\\\
&= \sqrt{1 + 9} \\\\
&= \sqrt{10}
\end{align*}
$$
</div>

So, the triangle inequality claims that

<div class="math-display">
$$
\lVert \vec u + \vec v \rVert \leq \lVert \vec u \rVert + \lVert \vec v \rVert
$$
</div>

which, here, is

<div class="math-display">
$$
3 \leq 5 + \sqrt{10}
$$
</div>

This is true, since 5 alone is greater than 3, so <span class="math-inline">\\(5 + \sqrt{10}\\)</span> is surely also greater than (or equal to) 3.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find two **different** vectors in <span class="math-inline">\\(\vec x, \vec y \in \mathbb{R}^2\\)</span> such that the triangle inequality achieves **equality**, i.e. where

<div class="math-display">
$$
\lVert \vec x + \vec y \rVert = \lVert \vec x \rVert + \lVert \vec y \rVert
$$
</div>

What is the relationship between the <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> you found?

<details markdown="1"><summary>Solution</summary>

Example: let <span class="math-inline">\\(\vec x = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec y = \begin{bmatrix} 2 \\\\ 2 \end{bmatrix}\\)</span>. Then,

<div class="math-display">
$$
\left\lVert \vec x + \vec y \right\rVert = \left\lVert \begin{bmatrix} 3 \\\\ 3 \end{bmatrix} \right\rVert = \sqrt{3^2 + 3^2} = 3 \sqrt{2}
$$
</div>

 

<div class="math-display">
$$
\lVert \vec x \rVert + \lVert \vec y \rVert = \sqrt{1^2 + 1^2} + \sqrt{2^2 + 2^2} = \sqrt{2} + \sqrt{8} = \sqrt{2} + 2 \sqrt{2} = 3 \sqrt{2}
$$
</div>

So, in this case, the triangle inequality achieves equality. What you'll notice is that <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> point in the same direction, i.e. <span class="math-inline">\\(\vec y = 2 \vec x\\)</span>.

</details>

</div>
</div>

</div>

---

## Activity 6: Arrays in NumPy

Instead of writing code in a separate Jupyter Notebook for this lab, you will interact with the code cells that exist in the course notes.

In particular, go to [Chapter 3.2](https://notes.eecs245.org/vectors/norms/) of the course notes, scroll all the way to the bottom, and complete **Activity 5** there. Once you're done, include a screenshot of your completed Activity 5 in your PDF submission of Lab 3 to Gradescope, making sure to include proof that you've completed the activity.
