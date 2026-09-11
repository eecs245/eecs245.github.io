---
layout: page
title: "Lab 2: Empirical Risk and Simple Linear Regression"
description: "Lab 2: Empirical Risk and Simple Linear Regression activities."
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

# Lab 2: Empirical Risk and Simple Linear Regression

**due** by the end of your lab section on Wednesday, September 9th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab02/lab02.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab02/lab02-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete all required activities and show your lab TA by the end of the lab section.

While you must get checked off by your lab TA **individually**, we encourage you to form groups with 1-2 other students to complete the activities together.
</div>

---

## Activities

- [Activity 1: Relative Squared Loss](#activity-1-relative-squared-loss)
- [Activity 2: Rapid Fire](#activity-2-rapid-fire)
- [Activity 3: Slope of Mean Absolute Error](#activity-3-slope-of-mean-absolute-error)
- [Activity 4: Programming](#activity-4-programming)
- [Activity 5: What Do You Mean?](#activity-5-what-do-you-mean)
- [Activity 6: The Meaning of Mean Squared Error](#activity-6-the-meaning-of-mean-squared-error)
- [Activity 7: Relative Squared Loss, Continued](#activity-7-relative-squared-loss-continued)
- [Activity 8: A Refresher](#activity-8-a-refresher)

---

## Recap: The Modeling Recipe

In [Chapter 1.3](https://notes.eecs245.org/introduction-to-supervised-learning/absolute-loss/), we introduced the three-step modeling recipe for finding optimal model parameters, which ultimately helps us make the best possible predictions.

<ol class="assignment-list" markdown="1" data-item-count="3" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

**Choose a model.**

<div class="math-display">
$$
\underbrace{h(x_i) = w}_{\text{constant model}} \quad\quad \underbrace{h(x_i) = w_0 + w_1 x_i}_{\text{simple linear regression model}}
$$
</div>

</li>
<li markdown="1" value="2">

**Choose a loss function.**

<div class="math-display">
$$
\underbrace{L_{\text{sq}}(y_i, h(x_i)) = (y_i - h(x_i))^2}_{\text{squared loss}} \quad\quad \underbrace{L_{\text{abs}}(y_i, h(x_i)) = |y_i - h(x_i)|}_{\text{absolute loss}}
$$
</div>

</li>
<li markdown="1" value="3">

**Minimize *average loss* (also called *empirical risk*) to find optimal model parameters.**

<ul class="assignment-list" markdown="1" data-item-count="3">
<li markdown="1">

Constant model, squared loss: <span class="math-inline">\\(\displaystyle R&#95;{\text{sq}}(w) = \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - w)^2 \implies w^{\ast} = \bar{y}\\)</span>

</li>
<li markdown="1">

Constant model, absolute loss: <span class="math-inline">\\(\displaystyle R&#95;{\text{abs}}(w) = \frac{1}{n} \sum&#95;{i=1}^n |y&#95;i - w| \implies w^{\ast} = \text{Median}(y&#95;1, y&#95;2, \ldots, y&#95;n)\\)</span>

</li>
<li markdown="1">

Simple linear regression model, squared loss:

<div class="math-display">
$$
\displaystyle R_{\text{sq}}(w_0, w_1) = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i))^2 \implies w_1^* = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad w_0^* = \bar{y} - w_1^* \bar{x}
$$
</div>

</li>
</ul>
</li>
</ol>

---

## Activity 1: Relative Squared Loss

Suppose we'd like to find the optimal parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>. To do so, we use the following loss function, called the **relative squared loss**:

<div class="math-display">
$$
L_{\text{rsq}}(y_i, h(x_i)) = \frac{(y_i - h(x_i))^2}{y_i}
$$
</div>

What value of <span class="math-inline">\\(w\\)</span> minimizes the average loss (i.e. empirical risk) when using the relative squared loss function -- that is, what is <span class="math-inline">\\(w^{\ast}\\)</span>? Your answer should only be in terms of the variables <span class="math-inline">\\(n, y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>, and any constants.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(h(x&#95;i) = w\\)</span> for the constant model, relative squared loss for the constant model is:

<div class="math-display">
$$
L_{\text{rsq}}(y_i, w) = \frac{(y_i - w)^2}{y_i}
$$
</div>

and so average relative squared loss for the constant model is:

<div class="math-display">
$$
R_{\text{rsq}}(w) = \frac{1}{n} \sum_{i = 1}^n \frac{(y_i - w)^2}{y_i}
$$
</div>

To find the value of <span class="math-inline">\\(w\\)</span> that minimizes <span class="math-inline">\\(R&#95;{\text{rsq}}(w)\\)</span>, we'll first find its first derivative and set it to zero. The first derivative of <span class="math-inline">\\(R&#95;{\text{rsq}}(w)\\)</span> is:

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}}{\text{d} w} R_{\text{rsq}}(w) &=  \frac{\text{d}}{\text{d} w} \left( \frac{1}{n} \sum_{i = 1}^n \frac{(y_i - w)^2}{y_i} \right) \\\\
&= \frac{1}{n} \sum_{i = 1}^n \frac{\text{d}}{\text{d} w} \left( \frac{(y_i - w)^2}{y_i} \right) \\\\
\end{align*}
$$
</div>

At this point, it'll be useful to step aside and find the derivative of <span class="math-inline">\\(L&#95;{\text{rsq}}(y&#95;i, w)\\)</span> with respect to <span class="math-inline">\\(w\\)</span>, as this is the expression being summed. The derivative of <span class="math-inline">\\(L&#95;{\text{rsq}}(y&#95;i, w)\\)</span> with respect to <span class="math-inline">\\(w\\)</span> is:

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}}{\text{d}w} L_{\text{rsq}}(y_i, w) &= \frac{\text{d}}{\text{d}w} \frac{(y_i - w)^2}{y_i} \\\\
&= \frac{1}{y_i} \cdot \frac{\text{d}}{\text{d}w} (y_i-w)^2 \\\\
&= \frac{1}{y_i} \cdot 2 (y_i-w) \cdot (-1) \\\\
&= -2 \cdot \frac{y_i-w}{y_i} \\\\
&= \boxed{2\cdot \frac{w}{y_i} -2}
\end{align*}
$$
</div>

Back to <span class="math-inline">\\(\frac{\text{d}}{\text{d} w}R&#95;{\text{rsq}}(w)\\)</span>, we have:

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}}{\text{d} w} R_{\text{rsq}}(w) &= \frac{1}{n} \sum_{i = 1}^n \frac{\text{d}}{\text{d} w} \left( \frac{(y_i - w)^2}{y_i} \right) \\\\
&= \frac{1}{n} \sum_{i = 1}^n \left( 2\cdot \frac{w}{y_i} -2 \right) \\\\
&= \frac{2w}{n} \sum_{i=1}^n (\frac{1}{y_i}) - \frac{1}{n} \sum_{i=1}^n 2 \\\\
&= \frac{2w}{n} \sum_{i=1}^n (\frac{1}{y_i}) - 2
\end{align*}
$$
</div>

Setting this equal to 0 yields:

<div class="math-display">
$$
\begin{align*}
\frac{2w}{n} \sum_{i=1}^n (\frac{1}{y_i}) - 2 &= 0 \\\\
\frac{w}{n} \sum_{i=1}^n (\frac{1}{y_i}) &= 1 \\\\
w^* &= \frac{1}{\frac{1}{n} \sum_{i=1}^n (\frac{1}{y_i})} \\\\
w^* &= \boxed{\frac{n}{\sum_{i=1}^n \frac{1}{y_i}}} \\\\
\end{align*}
$$
</div>

This is known as the **harmonic mean** of <span class="math-inline">\\(y&#95;1, y&#95;2, ..., y&#95;n\\)</span>.
</details>

---

## Activity 2: Rapid Fire

Consider a dataset of <span class="math-inline">\\(n\\)</span> **integers**, <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>, whose histogram is given below:

<div style="text-align: center;">
<img src="imgs/hist-dist.png" alt="image" style="width: 80%; max-width: 100%;">
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes:

<div class="math-display">
$$
\frac{1}{n} \sum_{i = 1}^n
\begin{cases}
0 \quad  y_i = w \\\\
1 \quad y_i \neq w
\end{cases}
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 30</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 30</span></div>

**<span class="math-inline">\\(30\\)</span>.**

The minimizer of average 0-1 loss is the **mode**.

See: [Chapter 1.4: Beyond Absolute and Squared Loss](https://notes.eecs245.org/introduction-to-supervised-learning/comparing-loss-functions/#beyond-absolute-and-squared-loss)
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes:

<div class="math-display">
$$
\frac{1}{n} \sum_{i = 1}^n |y_i - w|
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 30</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 30</span></div>

**<span class="math-inline">\\(7\\)</span>.**

The minimizer of average absolute loss is the **median**. The outliers near <span class="math-inline">\\(30\\)</span> shift it from <span class="math-inline">\\(6\\)</span> to <span class="math-inline">\\(7\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes:

<div class="math-display">
$$
\frac{1}{n} \sum_{i = 1}^n (y_i - w)^2
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 30</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 30</span></div>

**<span class="math-inline">\\(11\\)</span>.**

The minimizer of average squared loss is the **mean**, pulled upward by the heavy right tail, so it's above the median (<span class="math-inline">\\(7\\)</span>) and closest to <span class="math-inline">\\(11\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes:

<div class="math-display">
$$
\lim_{p \rightarrow \infty} \frac{1}{n} \sum_{i = 1}^n |y_i - w|^p
$$
</div>

<em>Hint: Think about the effect of outliers.</em>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 30</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 11</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 15</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 30</span></div>

**<span class="math-inline">\\(15\\)</span>.**

As <span class="math-inline">\\(p \to \infty\\)</span>, the minimizer is the **midrange**, halfway between min and max.
</details>

</div>
</div>

</div>

---

## Activity 3: Slope of Mean Absolute Error

Consider a dataset of 8 points, <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;8\\)</span> that are in sorted order, i.e. <span class="math-inline">\\(y&#95;1 &lt; y&#95;2 &lt; \ldots &lt; y&#95;8\\)</span>.

Recall that mean absolute error, <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span> is defined as:

<div class="math-display">
$$
R_{\text{abs}}(w)=\frac{1}{n} \sum_{i=1}^n |y_i - w|
$$
</div>

This is a piecewise linear function that changes slope at each data point. The slope of <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span> at any <span class="math-inline">\\(w\\)</span> that is not a data point is:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w}R_{\text{abs}}(w) = \frac{\text{# of points left of }w-\text{# of points right of }w}{n}, \qquad w\notin\{y_1,\ldots,y_n\}
$$
</div>

Suppose that <span class="math-inline">\\(y&#95;4=10\\)</span>, <span class="math-inline">\\(y&#95;5=14\\)</span>, <span class="math-inline">\\(y&#95;6=22\\)</span>, and <span class="math-inline">\\(R&#95;{\text{abs}}(11)=9\\)</span>. What is <span class="math-inline">\\(R&#95;{\text{abs}}(22)\\)</span>?

<em>Hint: You don't have all 8 of the <span class="math-inline">\\(y\\)</span>-values, so you can't find <span class="math-inline">\\(R&#95;\text{abs}(22)\\)</span> just by plugging in numbers into the formula for <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>. Instead, think about how to use the slope formula.</em>

<details markdown="1"><summary>Solution</summary>

**<span class="math-inline">\\(R&#95;{\text{abs}}(22)=11\\)</span>**.

We can write the points given to us as:

<div class="math-display">
$$
\begin{align*}
y_1, y_2, y_3, 10, 14, 22, y_7, y_8
\end{align*}
$$
</div>

Since there are an even number of data points (<span class="math-inline">\\(n=8\\)</span>), the minimizer of absolute error is not a single point but the entire interval between the two middle points. Here, the middle two are <span class="math-inline">\\(10\\)</span> and <span class="math-inline">\\(14\\)</span>, so every <span class="math-inline">\\(w \in [10,14]\\)</span> minimizes <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span>. This explains why the error is *flat* inside that interval: the number of points on the left equals the number on the right, so shifting <span class="math-inline">\\(w\\)</span> around does not change the error. As a result, <span class="math-inline">\\(R&#95;{\text{abs}}(11)=9\\)</span> and <span class="math-inline">\\(R&#95;{\text{abs}}(14)=9\\)</span>.

Once we move beyond <span class="math-inline">\\(14\\)</span>, the balance breaks. There are now five points to the left and only three to the right, so the slope of <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span> becomes positive. The slope formula tells us:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w}R_{\text{abs}}(w) = \frac{\text{# of points left of }w-\text{# of points right of }w}{n}, \qquad w\notin\{y_1,\ldots,y_n\}
$$
</div>

 so for any <span class="math-inline">\\(w \in (14,22)\\)</span> we have

<div class="math-display">
$$
\frac{d}{dw}R_{\text{abs}}(w) = \frac{5-3}{8} = \tfrac{1}{4}.
$$
</div>

This means that for every one unit we move to the right of <span class="math-inline">\\(w=14\\)</span>, the error increases by <span class="math-inline">\\(\tfrac{1}{4}\\)</span>. Moving from <span class="math-inline">\\(w=14\\)</span> to <span class="math-inline">\\(w=22\\)</span> is a distance of <span class="math-inline">\\(22-14=8\\)</span> units, so the error increases by

<div class="math-display">
$$
8 \cdot \tfrac{1}{4} = 2.
$$
</div>

Adding this to the baseline error of <span class="math-inline">\\(R&#95;{\text{abs}}(14)=9\\)</span>, we get:

<div class="math-display">
$$
\begin{align*}
R_{\text{abs}}(22) &= R_{\text{abs}}(14) + (22-14)\cdot \tfrac{1}{4} \\\\
&= 9 + 2 = 11.
\end{align*}
$$
</div>

</details>

---

## Activity 4: Programming

Complete the tasks in the `lab02.ipynb` notebook.

There are two ways to access the supplemental Jupyter Notebook:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

**Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/fa26-code/tree/main), and open `labs/lab02/lab02.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

</li>
<li markdown="1">

**Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Flabs%2Flab02%2Flab02.ipynb&branch=main) to open `lab02.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

</li>
</ul>

To receive credit for Activity 4, you'll need to show your lab TA that all test cases have passed.

---

## Activity 5: What Do You Mean?

Suppose we want to fit a simple linear model (using squared loss) that predicts the number of ingredients in a product given its price. We're given that:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

The average cost of a product in our dataset is &#36;40, i.e. <span class="math-inline">\\(\bar x=40\\)</span>

</li>
<li markdown="1">

The average number of ingredients in a product in our dataset is 15, i.e. <span class="math-inline">\\(\bar y =15\\)</span>

</li>
</ul>

The intercept and slope of the regression line are <span class="math-inline">\\(w&#95;0^{\ast}=11\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}=\frac{1}{10}\\)</span>, respectively.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose Victors' Veil (a skincare product) costs &#36;40 and has 11 ingredients. What is the squared loss of our model's predicted number of ingredients for Victors' Veil?

<details markdown="1"><summary>Solution</summary>

Using the equation of the regression model we have seen in class:

<div class="math-display">
$$
h(x_i)=w_0^*+w_1^*x_i
$$
</div>

 Plugging in <span class="math-inline">\\(w&#95;0^{\ast}=11\\)</span>, <span class="math-inline">\\(w&#95;1^{\ast}=\frac{1}{10}\\)</span>, and <span class="math-inline">\\(x=40\\)</span> gives us:

<div class="math-display">
$$
h(x_i)=11+\frac{1}{10}\cdot 40 = 15
$$
</div>

 The squared loss is <span class="math-inline">\\(L=(y&#95;i-h(x&#95;i))^2\\)</span>, substituting <span class="math-inline">\\(y=11\\)</span> (actual) and <span class="math-inline">\\(h(x&#95;i)=15\\)</span> (predicted) gives us:

<div class="math-display">
$$
L=(11-15)^2=16
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Is it possible to answer part **a)** above **just** by knowing <span class="math-inline">\\(\bar x\\)</span> and <span class="math-inline">\\(\bar y\\)</span>, i.e. **without** knowing the values of <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>? Once you select an answer, explain it to your peers.

<em>Hint: If you're stuck, look through the headings of the sections of <a href="https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/">Chapter 2.3</a>.</em>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes, it's possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No, it's not possible</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Yes, it's possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No, it's not possible</span></div>

Yes, the values of <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> don't impact the answer to part a).

The simple linear model minimizing mean squared error will always go through the point <span class="math-inline">\\((\bar x, \bar y)\\)</span>. We're given <span class="math-inline">\\(\bar x=40\\)</span> and <span class="math-inline">\\(\bar y=15\\)</span>, meaning that for a product that costs &#36;40 we will predict that it has 15 ingredients, no matter what the slope and intercept end up being.
</details>

</div>
</div>

</div>

---

## Activity 6: The Meaning of Mean Squared Error

Suppose we'd like to predict the number of minutes a delivery will take, <span class="math-inline">\\(y\\)</span>, as a function of distance, <span class="math-inline">\\(x\\)</span>. To do so, we look to our dataset of <span class="math-inline">\\(n\\)</span> deliveries, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2,y&#95;2), \dots, (x&#95;n,y&#95;n)\\)</span>, and fit two simple linear models:

<ul class="assignment-list" markdown="1" data-item-count="2">
<li markdown="1">

<span class="math-inline">\\(F(x&#95;i)=a&#95;0+a&#95;1x&#95;i\\)</span>, where:

<div class="math-display">
$$
a_1=\frac{\sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^n (x_i-\bar{x})^2}, \qquad  a_0=\bar y - a_1 \bar x
$$
</div>

 Here, <span class="math-inline">\\(\bar{x}\\)</span> and <span class="math-inline">\\(\bar{y}\\)</span> are the respective means of the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values.

</li>
<li markdown="1">

<span class="math-inline">\\(G(x&#95;i)=b&#95;0+b&#95;1x&#95;i\\)</span>, where <span class="math-inline">\\(b&#95;0\\)</span> and <span class="math-inline">\\(b&#95;1\\)</span> are chosen such that <span class="math-inline">\\(G(x&#95;i)=b&#95;0+b&#95;1x&#95;i\\)</span> minimizes **mean absolute error** on the dataset. Assume that no other line minimizes mean absolute error on the dataset, i.e. that the values of <span class="math-inline">\\(b&#95;0\\)</span> and <span class="math-inline">\\(b&#95;1\\)</span> are unique. Assume also that <span class="math-inline">\\(F\\)</span> and <span class="math-inline">\\(G\\)</span> are distinct lines.

</li>
</ul>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Fill in the <span class="math-inline">\\(\boxed{???}\\)</span>:

<div class="math-display">
$$
\displaystyle \sum_{i=1}^{n}(y_i-F(x_i))^2  \quad \boxed{???} \quad \sum_{i=1}^{n}(y_i-G(x_i))^2
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(&gt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\geq\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(=\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\leq\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(&lt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(&gt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\geq\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(=\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\leq\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\(&lt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

The quantity on the left hand side is the **total squared error** of model <span class="math-inline">\\(F\\)</span>. By definition, <span class="math-inline">\\(F\\)</span>, is the line that minimizes MSE over all possible linear models.

The quantity on the right hand side is the total squared error of model <span class="math-inline">\\(G\\)</span>. However, <span class="math-inline">\\(G\\)</span> is optimized for **mean absolute error**, not MSE.

The question tells us that <span class="math-inline">\\(F\\)</span> and <span class="math-inline">\\(G\\)</span> are different, so <span class="math-inline">\\(\displaystyle \sum&#95;{i=1}^{n}(y&#95;i-F(x&#95;i))^2 &lt; \sum&#95;{i=1}^{n}(y&#95;i-G(x&#95;i))^2\\)</span> must be true.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Fill in the <span class="math-inline">\\(\boxed{???}\\)</span>:

<div class="math-display">
$$
\displaystyle \left(\sum_{i=1}^{n}|y_i-F(x_i)|\right)^2  \quad \boxed{???} \quad \left(\sum_{i=1}^{n}|y_i-G(x_i)|\right)^2
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(&gt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\geq\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(=\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\leq\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(&lt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\(&gt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\geq\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(=\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(\leq\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(&lt;\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

The quantity on the left hand side is the **squared total absolute error** of model <span class="math-inline">\\(F\\)</span>.

The quantity on the right hand side is the **squared total absolute error** of model <span class="math-inline">\\(G\\)</span>. By definition, <span class="math-inline">\\(G\\)</span>, is the line that minimizes MAE over all possible linear models.

The total absolute error of <span class="math-inline">\\(G\\)</span> must be less than the total absolute error of <span class="math-inline">\\(F\\)</span>, and squaring them doesn't change that relationship because both totals are guaranteed to be positive numbers (sums of absolute values).

Finally, <span class="math-inline">\\(F\\)</span> and <span class="math-inline">\\(G\\)</span> are different, so <span class="math-inline">\\(\displaystyle \left(\sum&#95;{i=1}^{n}|y&#95;i-F(x&#95;i)|\right)^2 &gt; \left(\sum&#95;{i=1}^{n}|y&#95;i-G(x&#95;i)|\right)^2\\)</span>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Below, we've drawn the lines for both <span class="math-inline">\\(F\\)</span> and <span class="math-inline">\\(G\\)</span> along with a scatter plot for the original <span class="math-inline">\\(n\\)</span> deliveries:

<div style="text-align: center;">
<img src="imgs/regression.png" alt="image" style="width: 70%; max-width: 100%;">
</div>

Which line corresponds to <span class="math-inline">\\(F\\)</span>?
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Line 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Line 2</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Line 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Line 2</span></div>

Line 1

The key idea is that models trained with squared loss (MSE) are more sensitive to outliers than models trained with absolute loss (MAE).

Since Line 1 appears to be "pulled up" more strongly by an outlier, it suggests that this line was influenced more heavily by extreme values. This behavior aligns with how MSE-based regression works: outliers have a greater impact on the overall loss because squaring the errors makes large deviations even more significant.

In contrast, MAE-based regression (Line 2) is less sensitive to outliers because absolute differences do not grow as quickly.

Therefore, Line 1 corresponds to <span class="math-inline">\\(F\\)</span>, the MSE-minimizing line.
</details>

</div>
</div>

</div>

---

{: .yellow }
> **The following are extra practice. Don't feel pressured to answer all of these problems in lab, but make sure to attempt them at some point.**

## Activity 7: Relative Squared Loss, Continued

Recall the formula for **relative squared loss** from Activity 1:

<div class="math-display">
$$
L_{\text{rsq}}(y_i, h(x_i)) = \frac{(y_i - h(x_i))^2}{y_i}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Let <span class="math-inline">\\(C(y&#95;1, y&#95;2, ..., y&#95;n)\\)</span> be your minimizer <span class="math-inline">\\(w^{\ast}\\)</span> from Activity 1. That is, for a particular dataset <span class="math-inline">\\(y&#95;1, y&#95;2, ..., y&#95;n\\)</span>, <span class="math-inline">\\(C(y&#95;1, y&#95;2, ..., y&#95;n)\\)</span> is the value of <span class="math-inline">\\(w\\)</span> that minimizes empirical risk for relative squared loss on that dataset.

What is the value of <span class="math-inline">\\(\displaystyle\lim&#95;{y&#95;4 \rightarrow \infty} C(1, 3, 5, y&#95;4)\\)</span> in terms of <span class="math-inline">\\(C(1, 3, 5)\\)</span>? Your answer should involve the function <span class="math-inline">\\(C\\)</span> and/or one or more constants.

<em>Hint: To notice the pattern, evaluate <span class="math-inline">\\(C(1, 3, 5, 100)\\)</span>, <span class="math-inline">\\(C(1, 3, 5, 10000)\\)</span>, and <span class="math-inline">\\(C(1, 3, 5, 1000000)\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\lim_{y_4 \rightarrow \infty} C(1, 3, 5, y_4) &= \lim_{y_4 \rightarrow \infty} \frac{4}{\frac{1}{1} + \frac{1}{3} + \frac{1}{5} + \frac{1}{y_4}} \\\\
&= \frac{4}{\frac{1}{1} + \frac{1}{3} + \frac{1}{5} + 0} \\\\
&= \frac{4}{3} \cdot \frac{3}{\frac{1}{1} + \frac{1}{3} + \frac{1}{5}} \\\\
&= \frac{4}{3} \cdot C(1, 3, 5)
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
What is the value of <span class="math-inline">\\(\displaystyle\lim&#95;{y&#95;4 \rightarrow 0} C(1, 3, 5, y&#95;4)\\)</span>? Again, your answer should involve the function <span class="math-inline">\\(C\\)</span> and/or one or more constants.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\lim_{y_4 \rightarrow 0} C(1, 3, 5, y_4) &= \lim_{y_4 \rightarrow 0} \frac{4}{\frac{1}{1} + \frac{1}{3} + \frac{1}{5} + \frac{1}{y_4}} \\\\
&= \frac{4}{\frac{1}{1} + \frac{1}{3} + \frac{1}{5} + \infty} \\\\
&= \frac{4}{\infty} = 0
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Based on the results of the previous two parts, when is the prediction <span class="math-inline">\\(C(y&#95;1, y&#95;2, ..., y&#95;n)\\)</span> robust to outliers? When is it not robust to outliers?

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(C(y&#95;1, y&#95;2, ..., y&#95;n)\\)</span> is great at ignoring large outliers. No matter how large you make any particular value, <span class="math-inline">\\(C(y&#95;1, y&#95;2, ..., y&#95;n)\\)</span> is upper-bounded by <span class="math-inline">\\(\frac{n}{n-1}\\)</span> multiplied by the value of <span class="math-inline">\\(C\\)</span> applied to all data points excluding the large outlier. This is as opposed to the regular "arithmetic mean", where if you make a single data point arbitrarily large, the mean also becomes arbitrarily large (i.e. if <span class="math-inline">\\(y&#95;n \rightarrow \infty\\)</span>, then <span class="math-inline">\\(\text{Mean}(y&#95;1, y&#95;2, ..., y&#95;n) \rightarrow \infty\\)</span> too).

However, <span class="math-inline">\\(C(y&#95;1, y&#95;2, ..., y&#95;n)\\)</span> is not robust to small outliers. As a particular data point approaches 0, the value of <span class="math-inline">\\(C(y&#95;1, y&#95;2, ..., y&#95;n)\\)</span> also approaches 0 no matter how large the other data points are.
</details>

</div>
</div>

</div>

---

## Activity 8: A Refresher

Consider a dataset of <span class="math-inline">\\(y&#95;1, y&#95;2, \dots, y&#95;n\\)</span>, all of which are **positive**. We want to fit a constant model, <span class="math-inline">\\(h(x&#95;i)=w\\)</span>, to the data.

Let <span class="math-inline">\\(w&#95;p^{\ast}\\)</span> be the optimal constant prediction that minimizes average degree-<span class="math-inline">\\(p\\)</span> loss, <span class="math-inline">\\(R&#95;p(w)\\)</span>, defined below:

<div class="math-display">
$$
R_p(w)= \displaystyle \frac{1}{n} \sum_{i=1}^{n}|y_i-w|^p
$$
</div>

 For example, <span class="math-inline">\\(w&#95;2^{\ast}\\)</span> is the optimal constant prediction that minimizes <span class="math-inline">\\(R&#95;2(w)= \displaystyle \frac{1}{n} \sum&#95;{i=1}^{n}|y&#95;i-w|^2\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
In each of the parts below, determine the value of the quantity provided. By "the data", we are referring to <span class="math-inline">\\(y&#95;1, y&#95;2, \dots, y&#95;n\\)</span>. The answer choices are as follows; **select one item in each row**.

<ul class="assignment-list" markdown="1" data-item-count="7">
<li markdown="1">

**A:** The standard deviation of the data

</li>
<li markdown="1">

**B:** The variance of the data

</li>
<li markdown="1">

**C:** The mean of the data

</li>
<li markdown="1">

**D:** The median of the data

</li>
<li markdown="1">

**E:** The midrange of the data, <span class="math-inline">\\(\frac{y&#95;\text{min} + y&#95;\text{max}}{2}\\)</span>

</li>
<li markdown="1">

**F:** The mode of the data

</li>
<li markdown="1">

**G:** None of these

</li>
</ul>

<table class="answer-choice-table">
<tbody>
<tr>
<td style="text-align: right;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">A</td>
<td style="text-align: left;">B</td>
<td style="text-align: left;">C</td>
<td style="text-align: left;">D</td>
<td style="text-align: left;">E</td>
<td style="text-align: left;">F</td>
<td style="text-align: left;">G</td>
</tr>
<tr>
<td style="text-align: right;">(i)</td>
<td style="text-align: left;"><span class="math-inline">\(w&#95;0^{\ast}\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
</tr>
<tr>
<td style="text-align: right;">(ii)</td>
<td style="text-align: left;"><span class="math-inline">\(w&#95;1^{\ast}\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
</tr>
<tr>
<td style="text-align: right;">(iii)</td>
<td style="text-align: left;"><span class="math-inline">\(R&#95;1(w&#95;1^{\ast})\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
</tr>
<tr>
<td style="text-align: right;">(iv)</td>
<td style="text-align: left;"><span class="math-inline">\(w&#95;2^{\ast}\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
</tr>
<tr>
<td style="text-align: right;">(v)</td>
<td style="text-align: left;"><span class="math-inline">\(R&#95;2(w&#95;2^{\ast})\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
<td style="text-align: left;"><span class="math-inline">\(\bigcirc\)</span></td>
</tr>
</tbody>
</table>

<details markdown="1"><summary>Solution</summary>

<ul class="assignment-list" markdown="1" data-item-count="5">
<li markdown="1">

**(i)** **None of these.** When <span class="math-inline">\\(w=y&#95;i\\)</span>, the term <span class="math-inline">\\(|y&#95;i-w|^0\\)</span> becomes <span class="math-inline">\\(0^0\\)</span>, which is undefined. Thus, <span class="math-inline">\\(R&#95;0(w)\\)</span> is not well-defined for all <span class="math-inline">\\(w\\)</span> as written. The intended loss function was 0-1 loss, which would have made the empirical risk

<div class="math-display">
$$
\begin{align*}
R_{0,1}(w) &= \frac{1}{n} \sum_{i=1}^n L_{0,1}(y_i,w) \\\\
&= \frac{\text{number of points not equal to } w}{n}.
\end{align*}
$$
</div>

To minimize this empirical risk, we would choose <span class="math-inline">\\(w\\)</span> to be the **mode** of the data, since it is the value that the greatest number of data points are equal to.

</li>
<li markdown="1">

**(ii)** <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> is the median of the data, since <span class="math-inline">\\(R&#95;1(w)= \displaystyle \frac{1}{n} \sum&#95;{i=1}^{n}|y&#95;i-w|\\)</span>

</li>
<li markdown="1">

**(iii)** <span class="math-inline">\\(R&#95;1(w&#95;1^{\ast})\\)</span> is the minimum mean absolute error, which is none of these.

</li>
<li markdown="1">

**(iv)** <span class="math-inline">\\(w&#95;2^{\ast}\\)</span> is the mean of the data, since <span class="math-inline">\\(R&#95;2(w)= \displaystyle \frac{1}{n} \sum&#95;{i=1}^{n}|y&#95;i-w|^2\\)</span> is equivalent to mean squared error.

</li>
<li markdown="1">

**(v)** <span class="math-inline">\\(R&#95;2(w&#95;2^{\ast})\\)</span> is the variance of the data, or the minimum mean squared error, shown below:

<div class="math-display">
$$
\begin{align*}
R_2(w_2^*)&=\displaystyle \frac{1}{n} \sum_{i=1}^{n}|y_i-w_2^*|^2
\\\\&=\displaystyle \frac{1}{n} \sum_{i=1}^{n}|y_i-\bar y|^2
\\\\&=\displaystyle \frac{1}{n} \sum_{i=1}^{n}(y_i-\bar y)^2 = \sigma_y^2
\end{align*}
$$
</div>

</li>
</ul>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now, suppose we want to find the optimal constant prediction, <span class="math-inline">\\(w&#95;\text{U}^{\ast}\\)</span>, using the "Ulta" loss function, defined below:

<div class="math-display">
$$
L_\text{U}(y_i, w) = y_i(y_i-w)^2
$$
</div>

To find <span class="math-inline">\\(w&#95;\text{U}^{\ast}\\)</span>, we minimize <span class="math-inline">\\(R&#95;\text{U}(w)\\)</span>, the average Ulta loss. How does <span class="math-inline">\\(w&#95;\text{U}^{\ast}\\)</span> compare to the mean of the data, <span class="math-inline">\\(M\\)</span>?

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} &gt; M\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} \geq M\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} = M\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} \leq M\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} &lt; M\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} &gt; M\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} \geq M\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} = M\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} \leq M\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\(w&#95;\text{U}^{\ast} &lt; M\)</span></span></div>

Minimizing the average Ulta loss means minimizing the empirical risk:

<div class="math-display">
$$
R_\text{U}(w)=\displaystyle \frac{1}{n} \sum_{i=1}^{n}y_i(y_i-w)^2
$$
</div>

 The minimizer is <span class="math-inline">\\(w&#95;\text{U}^{\ast} = \frac{\sum&#95;{i=1}^n y&#95;i^2}{\sum&#95;{i=1}^n y&#95;i}\\)</span>. Since <span class="math-inline">\\(M &gt; 0\\)</span>, we have <span class="math-inline">\\(w&#95;\text{U}^{\ast} - M = \frac{\frac{1}{n}\sum&#95;{i=1}^n (y&#95;i-M)^2}{M} \geq 0\\)</span>. Thus, <span class="math-inline">\\(w&#95;\text{U}^{\ast} \geq M\\)</span>, with equality exactly when all the <span class="math-inline">\\(y&#95;i\\)</span> values are equal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Finally, to find the optimal constant prediction, we will instead minimize **regularized** average Ulta loss, <span class="math-inline">\\(R&#95;\lambda(w)\\)</span>, defined below:

<div class="math-display">
$$
\displaystyle R_\lambda(w) = \left(\frac{1}{n} \sum_{i=1}^{n} y_i(y_i-w)^2\right)+\lambda w^2
$$
</div>

Here, assume <span class="math-inline">\\(\lambda &gt; 0\\)</span> is some positive constant. (We will cover regularization in more detail later in the term.)

Find <span class="math-inline">\\(w^{\ast}\\)</span>, the constant prediction that minimizes <span class="math-inline">\\(R&#95;\lambda(w)\\)</span>. Give your answer as an expression in terms of the <span class="math-inline">\\(y&#95;i\\)</span>'s, <span class="math-inline">\\(n\\)</span>, and/or <span class="math-inline">\\(\lambda\\)</span>.

<details markdown="1"><summary>Solution</summary>

To minimize the regularized average Ulta loss, we solve for <span class="math-inline">\\(w\\)</span> by setting <span class="math-inline">\\(\displaystyle \frac{\partial R}{\partial w}=0\\)</span> and solving for <span class="math-inline">\\(w\\)</span>.

Step 1: Compute the derivative and set to 0.

<div class="math-display">
$$
\begin{align*}
\displaystyle \frac{\partial R_\lambda}{\partial w}(w) &= \frac{\partial}{\partial w}\left[\left(\frac{1}{n} \sum_{i=1}^{n} y_i(y_i-w)^2\right)+\lambda w^2\right]
\\\\&=-2\left(\frac{1}{n} \sum_{i=1}^{n} y_i(y_i-w)\right)+2\lambda w = 0
\end{align*}
$$
</div>

Step 2: Expand and simplify.

<div class="math-display">
$$
\begin{align*}
-2\left(\frac{1}{n} \sum_{i=1}^{n} y_i(y_i-w)\right)+2\lambda w &= 0
\\\\\frac{1}{n} \sum_{i=1}^{n} y_i(y_i-w)-\lambda w &= 0
\\\\\frac{1}{n} \sum_{i=1}^{n} y_i^2 - \frac{1}{n} \sum_{i=1}^{n} y_iw-\lambda w &= 0
\\\\\frac{1}{n} \sum_{i=1}^{n} y_i^2 &= \frac{1}{n} \sum_{i=1}^{n} y_iw+\lambda w
\end{align*}
$$
</div>

Step 3: Solve for <span class="math-inline">\\(w\\)</span>.

<div class="math-display">
$$
\begin{align*}
\frac{1}{n} \sum_{i=1}^{n} y_i^2 &= \frac{1}{n} \sum_{i=1}^{n} y_iw+\lambda w
\\\\\frac{1}{n} \sum_{i=1}^{n} y_i^2 &= w\left(\frac{1}{n} \sum_{i=1}^{n} y_i+\lambda\right)
\\\\\frac{\frac{1}{n} \sum_{i=1}^{n} y_i^2}{\frac{1}{n} \sum_{i=1}^{n} y_i+\lambda} &= w
\end{align*}
$$
</div>

Step 4: Multiply by <span class="math-inline">\\(\frac{n}{n}\\)</span>

<div class="math-display">
$$
w^* = \frac{\sum_{i=1}^{n} y_i^2}{\sum_{i=1}^{n} y_i+n\lambda}
$$
</div>

</details>
</div>
</div>

</div>

{% endraw %}
