---
layout: page
title: "Lab 9: Gradient Descent and Convexity"
description: "Lab 9: Gradient Descent and Convexity activities."
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

# Lab 9: Gradient Descent and Convexity

**due** for completion at 11:59PM Ann Arbor Time on Monday, June 8th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab09/lab09.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab09/lab09-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).
</div>

---

## Activities

- [Activity 1: Gradient Descent Gone Wrong](#activity-1-gradient-descent-gone-wrong)
- [Activity 2: Gradient Descent for Empirical Risk Minimization](#activity-2-gradient-descent-for-empirical-risk-minimization)
- [Activity 3: Convexity and Gradient Descent](#activity-3-convexity-and-gradient-descent)
- [Activity 4: Linear Approximation](#activity-4-linear-approximation)
- [Activity 5: Using Convexity to Prove Inequalities](#activity-5-using-convexity-to-prove-inequalities)

---

**Recap: Gradient Descent** ([Chapter 8.3](https://notes.eecs245.org/gradients/gradient-descent/))

Suppose <span class="math-inline">\\(f: \mathbb{R}^d \rightarrow \mathbb{R}\\)</span> is a **differentiable** vector-to-scalar function, meaning that all of its partial derivatives are defined everywhere. To find <span class="math-inline">\\(\vec x^{\ast}\\)</span>, the **minimizer** of <span class="math-inline">\\(f\\)</span>:

1.  Choose a positive number, <span class="math-inline">\\(\mathbf{\alpha}\\)</span>. This number is called the **learning rate**, or **step size**.

2.  Choose an **initial guess** for the minimizer, <span class="math-inline">\\(\vec x^{(0)}\\)</span>.

3.  Then, repeatedly update the guess using the **update rule**:

<div class="math-display">
$$
\vec x^{(t+1)} = \vec x^{(t)} - \alpha \nabla f(\vec x^{(t)})
$$
</div>

4.  Terminate once the algorithm converges, which happens when the norm of the gradient, <span class="math-inline">\\(\lVert \nabla f(\vec x^{(t)}) \rVert\\)</span>, is below some small **tolerance** level, e.g. <span class="math-inline">\\(0.001\\)</span> (since this must mean we're very close to a minimum).

**Intuition**: The gradient vector <span class="math-inline">\\(\nabla f(\vec x^{(t)})\\)</span> tells us the direction of greatest increase in <span class="math-inline">\\(f\\)</span> at the current guess <span class="math-inline">\\(\vec x^{(t)}\\)</span>, so <span class="math-inline">\\(-\nabla f(\vec x^{(t)})\\)</span> is the direction that will **decrease** our function the most. The distance moved in that direction is determined by the step size <span class="math-inline">\\(\alpha\\)</span>, which scales <span class="math-inline">\\(-\nabla f(\vec x^{(t)})\\)</span>. To update our guess, we add <span class="math-inline">\\(-\alpha \nabla f(\vec x^{(t)})\\)</span> to the old guess, <span class="math-inline">\\(\vec x^{(t)}\\)</span>. Then, we repeat this process.

<img src="imgs/gradient-descent-contour.png" alt="image" style="width: 100%; max-width: 100%;">

Example gradient descent path for a function <span class="math-inline">\\(f: \mathbb{R}^2 \to \mathbb{R}\\)</span>.

---

## Activity 1: Gradient Descent Gone Wrong

Suppose <span class="math-inline">\\(\vec x \in \mathbb{R}^2\\)</span>. Let

<div class="math-display">
$$
f(\vec x) = x_1^3 + \lVert \vec x \rVert^2 = x_1^3 + x_1^2 + x_2^2
$$
</div>

To minimize <span class="math-inline">\\(f(\vec x)\\)</span>, we use gradient descent, with a learning rate of <span class="math-inline">\\(\alpha = \frac{1}{4}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Open Desmos and plot the related function <span class="math-inline">\\(g(x) = x^3 + x^2\\)</span>. Even though this is a scalar-to-scalar function, and <span class="math-inline">\\(f\\)</span> is vector-to-scalar, they are related. What do you notice about the shape of the graph?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(g(x)\\)</span> is a cubic function, with a local minimum and local maximum and no global minimum nor maximum. It is not convex.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>, the gradient of <span class="math-inline">\\(f(\vec x)\\)</span>.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\nabla f(\vec x) = \begin{bmatrix} 3x_1^2 + 2x_1 \\\\ 2x_2 \end{bmatrix} = \begin{bmatrix} 3x_1^2 \\\\ 0 \end{bmatrix} + 2 \vec x
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Recall, <span class="math-inline">\\(\vec x^{(t)}\\)</span> is the guess for <span class="math-inline">\\(\vec x^{\ast}\\)</span> at timestep <span class="math-inline">\\(t\\)</span>. Let <span class="math-inline">\\(\vec x^{(t)} = \begin{bmatrix} x&#95;1^{(t)} \\\\ x&#95;2^{(t)} \end{bmatrix}\\)</span>.

Show that

<div class="math-display">
$$
x_1^{(t+1)} = \frac{1}{2} x_1^{(t)} - \frac{3}{4} (x_1^{(t)})^2, \qquad x_2^{(t+1)} = \frac{1}{2}x_2^{(t)}
$$
</div>

<details markdown="1"><summary>Solution</summary>

The gradient descent update rule states that <span class="math-inline">\\(\vec x^{(t+1)}=\vec x^{(t)}-\alpha \nabla f(\vec x^{(t)})\\)</span>. But, since <span class="math-inline">\\(\nabla f(\vec x) = \begin{bmatrix} \frac{\partial f}{\partial x&#95;1} \\\\ \frac{\partial f}{\partial x&#95;2} \end{bmatrix}\\)</span>, we can think of the update rule as being two separate update rules:

<div class="math-display">
$$
x_i^{(t+1)} = x_i^{(t)} - \alpha \frac{\partial f}{\partial x_i}(\vec x^{(t)}), \quad i = 1, 2
$$
</div>

Then,

<div class="math-display">
$$
\begin{align*}
x_1^{(t+1)}&=x_1^{(t)}-\alpha \frac{\partial f}{\partial x_1}(\vec x^{(t)})
\\\\&=x_1^{(t)}-\frac{1}{4}(3(x_1^{(t)})^2 + 2x_1)
\\\\&=x_1^{(t)}-\frac{3}{4}(x_1^{(t)})^2-\frac{2}{4}x_1^{(t)}
\\\\&=\frac{1}{2}x_1^{(t)}-\frac{3}{4}(x_1^{(t)})^2
\end{align*}
$$
</div>

<div class="math-display">
$$
\begin{align*}
x_2^{(t+1)}&=x_2^{(t)}-\alpha \frac{\partial f}{\partial x_2}(\vec x^{(t)})
\\\\&=x_2^{(t)}-\frac{1}{4}(2x_2^{(t)})
\\\\&=x_2^{(t)}-\frac{1}{2}x_2^{(t)}
\\\\&=\frac{1}{2}x_2^{(t)}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
For any initial guess <span class="math-inline">\\(\vec x^{(0)}\\)</span>, what does <span class="math-inline">\\(x&#95;2^{(t)}\\)</span> converge to as <span class="math-inline">\\(t \to \infty\\)</span>?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(x&#95;2^{(t)}\\)</span> converges to 0 as <span class="math-inline">\\(t \to \infty\\)</span> because it's being divided in half at each iteration.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\vec x^{(0)}=\begin{bmatrix} -1 \\\\ 0 \end{bmatrix}\\)</span>.

1.  Find <span class="math-inline">\\(\vec x^{(1)}\\)</span>.

2.  Will gradient descent eventually converge, given this initial guess and learning rate?

<details markdown="1"><summary>Solution</summary>

i\. Recall that <span class="math-inline">\\(x&#95;2^{(t+1)} = \frac{1}{2}x&#95;2^{(t)}\\)</span>. So, <span class="math-inline">\\(x&#95;2^{(1)} = \frac{1}{2}x&#95;2^{(0)} = \frac{1}{2} \cdot 0 = 0\\)</span>. As for <span class="math-inline">\\(x&#95;1^{(1)}\\)</span>, we have

<div class="math-display">
$$
\begin{align*}
x_1^{(1)}&=\frac{1}{2}x_1^{(0)}-\frac{3}{4}(x_1^{(0)})^2
\\\\&=\frac{1}{2}(-1)-\frac{3}{4}(-1)^2
\\\\&=-\frac{1}{2}-\frac{3}{4}
\\\\&=-\frac{5}{4}
\end{align*}
$$
</div>

ii. Gradient descent will not converge: the guesses for <span class="math-inline">\\(x&#95;1^{(t)}\\)</span> will get larger and larger in magnitude, approaching <span class="math-inline">\\(-\infty\\)</span>. This happens because the term <span class="math-inline">\\(-\frac{3}{4} (x&#95;1^{(t)})^2\\)</span> dominates the term <span class="math-inline">\\(\frac{1}{2} x&#95;1^{(t)}\\)</span> in the iteration rule. Since <span class="math-inline">\\(x&#95;1^{(1)}\\)</span> is already larger than 1 in magnitude, <span class="math-inline">\\((x&#95;1^{(1)})^2\\)</span> will be even larger than that (since when you square a number greater than 1, it increases in size), which propagates to the next iteration and so on.

<div class="math-display">
$$
x_1^{(t+1)} = \frac{1}{2} x_1^{(t)} - \frac{3}{4} (x_1^{(t)})^2
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(\vec x^{(0)}=\begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span>.

1.  Find <span class="math-inline">\\(\vec x^{(1)}\\)</span>.

2.  Will gradient descent eventually converge, given this initial guess and learning rate?

<details markdown="1"><summary>Solution</summary>

i\. Similar to part **e)**, we only have to find <span class="math-inline">\\(x&#95;1^{(1)}\\)</span>.

<div class="math-display">
$$
\begin{align*}
x_1^{(1)}&=\frac{1}{2}x_1^{(0)}-\frac{3}{4}(x_1^{(0)})^2
\\\\&=\frac{1}{2}(1)-\frac{3}{4}(1)^2
\\\\&=-\frac{1}{4}
\end{align*}
$$
</div>

ii. Here, gradient descent **will** converge, since the absolute value of <span class="math-inline">\\(x&#95;1^{(1)}\\)</span> is less than 1. If we run more iterations, we'll see that <span class="math-inline">\\(x&#95;1^{(t)}\\)</span> is approacing zero because the absolute value keeps decreasing. <span class="math-inline">\\(x&#95;1^{(2)}\\)</span>, for instance, is <span class="math-inline">\\(-\frac{11}{64}\\)</span>, and <span class="math-inline">\\(|-\frac{11}{64}| &lt; |-\frac{1}{4}|\\)</span>.

</details>

</div>
</div>

</div>

---

## Activity 2: Gradient Descent for Empirical Risk Minimization

Suppose we have a dataset of <span class="math-inline">\\(3\\)</span> points, <span class="math-inline">\\((1, 2), (3, 5), (6, -1)\\)</span>. We'd like to fit a simple linear regression model, <span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i\\)</span>, to this dataset by minimizing average squared loss.

While we already know a closed-form solution for the optimal parameters --- we've seen multiple equivalent versions of these formulas throughout the semester --- let's use gradient descent to find them.

Let <span class="math-inline">\\(\vec w = \begin{bmatrix} w&#95;0 \\\\ w&#95;1 \end{bmatrix}\\)</span>. Using an initial guess of <span class="math-inline">\\(\vec w^{(0)} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}\\)</span> and a step size of <span class="math-inline">\\(\alpha = 0.1\\)</span>, perform one iteration of gradient descent. What is <span class="math-inline">\\(\vec w^{(1)}\\)</span>?

<em>Hint: You can proceed either by using the gradient of <span class="math-inline">\\(R&#95;\text{sq}(\vec w) = \frac{1}{n} \lVert \vec y - X \vec w \rVert^2\\)</span> from the notes or by computing the partial derivatives of <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1) = \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - (w&#95;0 + w&#95;1 x&#95;i))^2\\)</span> with respect to <span class="math-inline">\\(w&#95;0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

Let's use the gradient of <span class="math-inline">\\(R&#95;\text{sq}(\vec w) = \frac{1}{n} \lVert \vec y - X \vec w \rVert^2\\)</span> from the notes.

<div class="math-display">
$$
\nabla R_\text{sq}(\vec w) = - \frac{2}{n} (X^T \vec y - X^TX \vec w) = \frac{2}{n} X^T (X \vec w - \vec y)
$$
</div>

Here, <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; 1 \\\\ 1 &amp; 3 \\\\ 1 &amp; 6 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec y = \begin{bmatrix} 2 \\\\ 5 \\\\ -1 \end{bmatrix}\\)</span>.

So, the gradient descent update is given by

<div class="math-display">
$$
\vec w^{(1)} = \vec w^{(0)} - \alpha \nabla R_\text{sq}(\vec w^{(0)}) = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix} - 0.1 \cdot \frac{2}{3} \begin{bmatrix} 1 & 1 & 1 \\\\ 1 & 3 & 6 \end{bmatrix} \left( \begin{bmatrix} 1 & 1 \\\\ 1 & 3 \\\\ 1 & 6 \end{bmatrix} \begin{bmatrix} 0 \\\\ 0 \end{bmatrix} - \begin{bmatrix} 2 \\\\ 5 \\\\ -1 \end{bmatrix} \right) = \boxed{\begin{bmatrix} 2/5 \\\\ 11/15 \end{bmatrix}}
$$
</div>

Note that if you did this using the partial derivatives of <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1) = \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - (w&#95;0 + w&#95;1 x&#95;i))^2\\)</span> with respect to <span class="math-inline">\\(w&#95;0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span>, you would get the same answer!

<div class="math-display">
$$
\nabla R_\text{sq}(\vec w) = \begin{bmatrix} \frac{\partial R_\text{sq}}{\partial w_0} \\\\ \frac{\partial R_\text{sq}}{\partial w_1} \end{bmatrix} = \begin{bmatrix} \displaystyle -\frac{2}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i)) \\\\ \displaystyle -\frac{2}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i)) x_i \end{bmatrix}
$$
</div>

Plugging in <span class="math-inline">\\(n=3\\)</span>, <span class="math-inline">\\(x&#95;1 = 1, x&#95;2 = 3, x&#95;3 = 6\\)</span>, <span class="math-inline">\\(y&#95;1 = 2, y&#95;2 = 5, y&#95;3 = -1\\)</span>, and <span class="math-inline">\\(w&#95;0^{(0)} = 0, w&#95;1^{(0)} = 0\\)</span>, we get

<div class="math-display">
$$
\begin{align*}
\nabla R_\text{sq}(\vec w^{(0)})
&= \begin{bmatrix}
-\frac{2}{n} \sum_{i=1}^n \left(y_i - (w_0^{(0)} + w_1^{(0)} x_i)\right)\\\\
-\frac{2}{n} \sum_{i=1}^n \left(y_i - (w_0^{(0)} + w_1^{(0)} x_i)\right) x_i
\end{bmatrix} \\\\
&= \begin{bmatrix}
-\frac{2}{3} \sum_{i=1}^3 \left(y_i - (0 + 0 \cdot x_i)\right)\\\\
-\frac{2}{3} \sum_{i=1}^3 \left(y_i - (0 + 0 \cdot x_i)\right) x_i
\end{bmatrix} \\\\
&= \begin{bmatrix}
-\frac{2}{3} \sum_{i=1}^3 y_i \\\\
-\frac{2}{3} \sum_{i=1}^3 y_i x_i
\end{bmatrix} \\\\
&= \begin{bmatrix}
-\frac{2}{3} (2 + 5 + (-1)) \\\\
-\frac{2}{3} (2 \cdot 1 + 5 \cdot 3 + (-1) \cdot 6)
\end{bmatrix} \\\\
&= \begin{bmatrix}
-4 \\\\
-22/3
\end{bmatrix}
\end{align*}
$$
</div>

Then, <span class="math-inline">\\(\vec w^{(1)}\\)</span> is given by

<div class="math-display">
$$
\begin{align*}
\vec w^{(1)}
&= \vec w^{(0)} - \alpha \nabla R_\text{sq}(\vec w^{(0)}) \\\\
&=
\begin{bmatrix} 0 \\\\ 0 \end{bmatrix}
- 0.1
\begin{bmatrix} -4 \\\\ -22/3 \end{bmatrix} \\\\
&=
\begin{bmatrix}
2/5 \\\\
11/15
\end{bmatrix}
\end{align*}
$$
</div>

which is the same result as before!

</details>

---

## Activity 3: Convexity and Gradient Descent

A function <span class="math-inline">\\(f: \mathbb{R}^d \to \mathbb{R}\\)</span> is convex if for all <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> in its domain, and for any <span class="math-inline">\\(t \in [0, 1]\\)</span>,

<div class="math-display">
$$
f((1-t) \vec x + t \vec y) \leq (1-t) f(\vec x) + t f(\vec y)
$$
</div>

 The English interpretation of this definition is that **the line connecting any two points on the graph of <span class="math-inline">\\(f\\)</span> always lies on or above the graph of <span class="math-inline">\\(f\\)</span>**. Intuitively, a convex function is a function that curves upward, like a bowl.

<img src="imgs/non-convex.png" alt="image" style="width: 50%; max-width: 100%;">

A non-convex function.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
If a function is convex, it **must** have a global minimum.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. For example, <span class="math-inline">\\(f(x) = e^x\\)</span> is convex, but it doesn't have a global minimum. It approaches <span class="math-inline">\\(0\\)</span> as <span class="math-inline">\\(x \to -\infty\\)</span>, but it never actually reaches it. <span class="math-inline">\\(f(x) = x\\)</span> is also convex and doesn't have a global minimum.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
If a function is convex, then gradient descent **must** converge on it given any initial guess and step size.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is also false. If we choose a step size <span class="math-inline">\\(\alpha\\)</span> that is too large, gradient descent may oscillate or diverge, as we've seen in examples in [Chapter 8.3](https://notes.eecs245.org/gradients/gradient-descent/).

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
If a function is convex, then any local minimum is also a global minimum.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true; a proof is given in [Chapter 8.5](https://notes.eecs245.org/gradients/convexity/).

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
If a function is convex and has a global minimum, then its minimizer **must** be unique.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false: a function can have multiple local minima that are all adjacent to each other, like a flat "ridge" at the very bottom.

<div style="text-align: center;">
<img src="imgs/flat-bottom.png" alt="image" style="width: 60%; max-width: 100%;">
</div>

</details>

</div>
</div>

</div>

---

## Activity 4: Linear Approximation

Suppose <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span>, i.e. <span class="math-inline">\\(f\\)</span> is a scalar-to-scalar function. In general, the **tangent line** to <span class="math-inline">\\(f(x)\\)</span> at <span class="math-inline">\\(x=a\\)</span> is given by the equation

<div class="math-display">
$$
f(x) \approx \underbrace{f(a) + \left( \frac{\text{d} f}{\text{d} x}(a) \right)(x-a)}_{\text{tangent line}}
$$
</div>

The <span class="math-inline">\\(\approx\\)</span> symbol means that the tangent line is an approximation of <span class="math-inline">\\(f(x)\\)</span> near <span class="math-inline">\\(x = a\\)</span>; in [Appendix 2](https://notes.eecs245.org/math-foundations/derivatives/), we defined it as the **best linear approximation** of <span class="math-inline">\\(f(x)\\)</span> near <span class="math-inline">\\(x = a\\)</span>. The expression on the right is a line with slope <span class="math-inline">\\(\frac{\text{d} f}{\text{d} x}(a)\\)</span> that passes through the point <span class="math-inline">\\((a, f(a))\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Draw <span class="math-inline">\\(f(x) = (x - 2)^2 + 5\\)</span> and its tangent line at <span class="math-inline">\\(x = 3\\)</span>.

<details markdown="1"><summary>Solution</summary>

First, let's find the derivative of <span class="math-inline">\\(f(x) = (x - 2)^2 + 5\\)</span>.

<div class="math-display">
$$
\frac{\text{d} f}{\text{d} x} = 2(x - 2)
$$
</div>

So, the tangent line to <span class="math-inline">\\(f(x)\\)</span> at <span class="math-inline">\\(x = 3\\)</span> is given by

<div class="math-display">
$$
f(x) \approx f(3) + \left( \frac{\text{d} f}{\text{d} x}(3) \right)(x-3) = 6 + 2(3-2)(x - 3) = 6 + 2x - 6 = \boxed{2x}
$$
</div>

<div style="text-align: center;">
<img src="imgs/tangent-line.png" alt="image" style="width: 50%; max-width: 100%;">
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
For vector-to-scalar functions, the best linear approximation at <span class="math-inline">\\(\vec x = \vec a\\)</span> is given by

<div class="math-display">
$$
f(\vec x) \approx f(\vec a) + \left(\nabla f(\vec a) \right) \cdot (\vec x - \vec a)
$$
</div>

If <span class="math-inline">\\(\vec x \in \mathbb{R}^2\\)</span>, this is called the **tangent plane**; if <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span> or higher, it is called the **tangent hyperplane**.

<img src="imgs/tangent-plane.png" alt="image" style="width: 40%; max-width: 100%;">

Tangent plane for a function <span class="math-inline">\\(f: \mathbb{R}^2 \to \mathbb{R}\\)</span>.

Find the tangent plane to <span class="math-inline">\\(f(\vec x) = \lVert \vec x \rVert^2 - 3\\)</span> at <span class="math-inline">\\(\vec x = \begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let's start by finding the gradient of <span class="math-inline">\\(f(\vec x) = \lVert \vec x \rVert^2 - 3\\)</span>. Remember that <span class="math-inline">\\(\nabla(\lVert \vec x \rVert^2) = 2 \vec x\\)</span>. So,

<div class="math-display">
$$
\nabla f(\vec x) = 2 \vec x
$$
</div>

as well.

So, the tangent plane to <span class="math-inline">\\(f(\vec x)\\)</span> at <span class="math-inline">\\(\vec x = \begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\\)</span> is given by

<div class="math-display">
$$
\begin{align*}
f(\vec x) &\approx f\left(\begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\right) + \left(\nabla f\left(\begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\right) \right) \cdot \left(\vec x - \begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\right) \\\\
&= (2^2 + 5^2 - 3) + \left( 2\begin{bmatrix} 2 \\\\ 5 \end{bmatrix} \right) \cdot \left(\vec x - \begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\right) \\\\
&= 26 + \begin{bmatrix} 4 \\\\ 10 \end{bmatrix} \cdot \vec x - \begin{bmatrix} 4 \\\\ 10 \end{bmatrix} \cdot \begin{bmatrix} 2 \\\\ 5 \end{bmatrix} \\\\
&= 26 - (8 + 50) + \begin{bmatrix} 4 \\\\ 10 \end{bmatrix} \cdot \vec x \\\\
&= \boxed{\begin{bmatrix} 4 \\\\ 10 \end{bmatrix} \cdot \vec x - 32} \\\\
&= \boxed{4x_1 + 10x_2 - 32}
\end{align*}
$$
</div>

The last two boxed expressions are both equivalent ways of writing the tangent plane. This plane passes through <span class="math-inline">\\((2, 5, f(2, 5))\\)</span> while having the same gradient as <span class="math-inline">\\(f(\vec x)\\)</span> at that point.

-   Plugging in <span class="math-inline">\\(x&#95;1 = 2\\)</span> and <span class="math-inline">\\(x&#95;2 = 5\\)</span> into the final expression gives 26, which also matches the value of <span class="math-inline">\\(f\left( \begin{bmatrix} 2 \\\\ 5 \end{bmatrix} \right) = 26\\)</span>.

-   In the latter form, the coefficients on <span class="math-inline">\\(x&#95;1\\)</span> and <span class="math-inline">\\(x&#95;2\\)</span> are 4 and 10, respectively, which match the components of the gradient vector <span class="math-inline">\\(\nabla f\left(\begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\right) = \begin{bmatrix} 4 \\\\ 10 \end{bmatrix}\\)</span>.

So, the boxed plane is **the** tangent plane to <span class="math-inline">\\(f(\vec x)\\)</span> at <span class="math-inline">\\(\vec x = \begin{bmatrix} 2 \\\\ 5 \end{bmatrix}\\)</span>. It's the best linear approximation of <span class="math-inline">\\(f(\vec x)\\)</span> near that point.

</details>

</div>
</div>

</div>

---

## Activity 5: Using Convexity to Prove Inequalities

Proofs like this will not appear on Midterm 2 but will appear on the Final Exam.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span> is a convex function such that <span class="math-inline">\\(f(0) = 0\\)</span>. Prove that for all <span class="math-inline">\\(y \in \mathbb{R}\\)</span> and <span class="math-inline">\\(t \in [0, 1]\\)</span>,

<div class="math-display">
$$
f(ty) \leq t f(y)
$$
</div>

<details markdown="1"><summary>Solution</summary>

Since the definition of convexity states that

<div class="math-display">
$$
f((1-t) x + t y) \leq (1-t) f(x) + t f(y)
$$
</div>

 **for all** <span class="math-inline">\\(x, y \in \mathbb{R}\\)</span>, we can substitute whatever we'd like for <span class="math-inline">\\(x\\)</span> or <span class="math-inline">\\(y\\)</span>. Let's plug in <span class="math-inline">\\(x = 0\\)</span>. Then,

<div class="math-display">
$$
\begin{align*}
f((1-t)\cdot 0 + ty) &\leq (1-t) f(0) + t f(y)
\\\\f(ty) &\leq tf(y)
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span> be a convex function. Prove that <span class="math-inline">\\(2f(5) \leq f(3) + f(7)\\)</span>.

<details markdown="1"><summary>Solution</summary>

We'll start by solving for <span class="math-inline">\\(t\\)</span> using <span class="math-inline">\\(x=3\\)</span> and <span class="math-inline">\\(y=7\\)</span> with the expression for the input on the left side of the inequality.

<div class="math-display">
$$
\begin{align*}
5&=(1-t)x + ty
\\\\&=(1-t)\cdot 3 + 7t
\\\\&=3-3t + 7t
\\\\&=3+4t, \:\: t=\frac{1}{2}
\end{align*}
$$
</div>

Then, plug the variables into the inequality and simplify.

<div class="math-display">
$$
\begin{align*}
f((1-\frac{1}{2})\cdot 3 + \frac{1}{2} \cdot 7) &\leq (1-\frac{1}{2})\cdot f(3) + \frac{1}{2}\cdot f(7)
\\\\f(\frac{3}{2} + \frac{7}{2}) &\leq \frac{f(3)}{2} + \frac{f(7)}{2}
\\\\f(5) &\leq \frac{f(3)}{2} + \frac{f(7)}{2}
\\\\2f(5) &\leq f(3) + f(7)
\end{align*}
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
