---
layout: page
title: "Homework 2: Empirical Risk and Simple Linear Regression"
description: "Homework 2: Empirical Risk and Simple Linear Regression problems."
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

# Homework 2: Empirical Risk and Simple Linear Regression

**due** Wednesday, May 13th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw02/hw02.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw02/hw02-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Homework 1 Solutions Review](#problem-1-homework-1-solutions-review-10-pts)
- [Problem 2: Stonks](#problem-2-stonks-7-pts)
- [Problem 3: Slippery Slope](#problem-3-slippery-slope-9-pts)
- [Problem 4: Fun with Correlation](#problem-4-fun-with-correlation-8-pts)
- [Problem 5: Switching Sides](#problem-5-switching-sides-9-pts)
- [Problem 6: Simple LAD](#problem-6-simple-lad-9-pts)

---

Total Points: 10 + 7 + 9 + 8 + 9 + 9 = 52

---

## Problem 1: Homework 1 Solutions Review (10 pts)

Review the solutions to Homework 1. Pick **two problem parts** (for example, Problem 3a and Problem 5) from Homework 1 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 1, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

<details markdown="1"><summary>Solution</summary>

</details>

---

## Problem 2: Stonks (7 pts)

This problem will eventually have something to do with machine learning. But first, a life lesson.

Suppose you invest in a stock, and:

-   In year 1, your investment increases by 50%.

-   In year 2, your investment decreases by 50%.

-   In year 3, your investment increases by 50%.

-   In year 4, your investment decreases by 50%.

What is the average growth rate of your investment, **per year**? The answer is not 0%, because ultimately you've **lost money**, even though it looks like the gains and losses should cancel out.

Why? At end of year 1, you have more money than you started with, and so losing 50% of that money in year 2 hurts more than losing 50% of your starting amount. Then, going up 50% in year 3 earns you less money than originally going up 50% in year 1 did, and so on.

Before we calculate the average growth rate, let's calculate the final value of your investment. To do so, we should convert these growth rates from percentages multipliers, using the formula:

<div class="math-display">
$$
\text{multiplier} = 1 + \frac{\text{percentage}}{100}
$$
</div>

So,

<div class="math-display">
$$
\text{final value} = \text{initial value} \cdot \underbrace{1.5}_{\text{year } 1} \cdot \underbrace{0.5}_{\text{year } 2} \cdot \underbrace{1.5}_{\text{year } 3} \cdot \underbrace{0.5}_{\text{year } 4} = \text{initial value} \cdot 0.5625
$$
</div>

Converting <span class="math-inline">\\(0.5625\\)</span> from a percentage back to a growth rate gives us:

<div class="math-display">
$$
\text{percentage} = 0.5625 - 1 = -0.4375 = -43.75\%
$$
</div>

So, in total, we lost 43.75% of our money.

This doesn't give us our average growth rate, though. The average growth rate, as a multiplier, should be a value <span class="math-inline">\\(g\\)</span> such that if our investment grows by <span class="math-inline">\\(g\\)</span> each year, we end up with <span class="math-inline">\\(1.5 \cdot 0.5 \cdot 1.5 \cdot 0.5 \cdot \text{initial value}\\)</span>. In other words:

<div class="math-display">
$$
\text{final value} = \text{initial value} \cdot g^4
$$
</div>

So, as a multiplier, we have that:

<div class="math-display">
$$
g^4 = 1.5 \cdot 0.5 \cdot 1.5 \cdot 0.5 \implies g = \left( 1.5 \cdot 0.5 \cdot 1.5 \cdot 0.5 \right)^{1/4} \approx 0.8660
$$
</div>

Converting <span class="math-inline">\\(g\\)</span> back to a percentage gives us:

<div class="math-display">
$$
\text{percentage} = 0.8660 - 1 = -0.1340 = -13.40\%
$$
</div>

So, the average growth rate of our investment, **per year**, is <span class="math-inline">\\(-13.40\%\\)</span> --- not the 0% that we might initially guess.

What does this have to do with machine learning? Let's re-visit one particular calculation above.

<div class="math-display">
$$
g = \left( 1.5 \cdot 0.5 \cdot 1.5 \cdot 0.5 \right)^{1/4}
$$
</div>

Here, <span class="math-inline">\\(g\\)</span>, is the **geometric mean** of the numbers 1.5, 0.5, 1.5, and 0.5. Geometric means are useful in computing the average of growth rates (when expressed as multipliers). In general, if <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span> are **positive** numbers, then their geometric mean is:

<div class="math-display">
$$
\left(y_1 \cdot y_2 \cdot \ldots \cdot y_n\right)^{1/n} = \left(\prod_{i=1}^n y_i\right)^{1/n}
$$
</div>

Like the arithmetic mean, as we saw in [Chapter 1.2](https://notes.eecs245.org/introduction-to-supervised-learning/squared-loss-constant-model/), and the harmonic mean, as we saw in Lab 2, the geometric mean is the constant prediction that minimizes average loss for some loss function.

In this case, the loss function is the log-quotient loss, defined as:

<div class="math-display">
$$
\begin{aligned}
L_{LQ}(y_i, h(x_i)) &= \left[\log\left(\frac{y_i}{h(x_i)}\right)\right]^2
\end{aligned}
$$
</div>

Note that <span class="math-inline">\\(\log(\cdot)\\)</span> is the natural logarithm, with base <span class="math-inline">\\(e\\)</span>.

Prove that the geometric mean of <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span> is the constant prediction that minimizes average log-quotient loss for the constant model, i.e. that the geometric mean minimizes:

<div class="math-display">
$$
R_{LQ}(w) = \frac{1}{n} \sum_{i=1}^n \left[\log\left(\frac{y_i}{w}\right)\right]^2
$$
</div>

<em>Hint: This is a question involving the three-step modeling process. You'll want to start by finding <span class="math-inline">\\(\frac{\text{d}}{\text{d}w} R_{LQ}(w)\\)</span> and setting that to 0. As a sub-problem, you'll need to find <span class="math-inline">\\(\frac{\text{d}}{\text{d}w} \left[\log\left(\frac{y_i}{w}\right)\right]\\)</span>. Work one step at a time and make sure your logic is clearly justified. Review the logarithm rules presented in <a href="https://eecs245.org/resources/homeworks/hw01/#problem-5-mean-imputation-6-pts">Homework 1, Problem 5</a>, and also use the fact that if <span class="math-inline">\\(b = \log(a)\\)</span>, then <span class="math-inline">\\(a = e^b\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

First, we find the derivative of <span class="math-inline">\\(R_{LQ}(w)\\)</span> with respect to <span class="math-inline">\\(w\\)</span>. In doing so, you'll notice that we use the fact that <span class="math-inline">\\(\log \left(\frac{y_i}{w}\right) = \log(y_i) - \log(w)\\)</span> to simplify.

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}}{\text{d}w} R_{LQ}(w) &= \frac{\text{d}}{\text{d}w} \left( \frac{1}{n} \sum_{i=1}^n \left[\log\left(\frac{y_i}{w}\right)\right]^2 \right) \\\\
&= \frac{1}{n} \sum_{i=1}^n \frac{\text{d}}{\text{d}w} \left[\log\left(\frac{y_i}{w}\right)\right]^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n 2 \left[\log\left(\frac{y_i}{w}\right)\right] \underbrace{\frac{\text{d}}{\text{d}w} \left[\log\left(\frac{y_i}{w}\right)\right]}_{\text{chain rule}} \\\\
&= \frac{1}{n} \sum_{i=1}^n 2 \left[\log\left(\frac{y_i}{w}\right)\right] \frac{\text{d}}{\text{d}w} \underbrace{\left[\log(y_i) - \log(w)\right]}_{\text{simplification}} \\\\
&= \frac{1}{n} \sum_{i=1}^n 2 \left[\log\left(\frac{y_i}{w}\right)\right] \left( -\frac{1}{w} \right) \\\\
&= -\frac{2}{nw} \sum_{i=1}^n \left[\log\left(\frac{y_i}{w}\right)\right] \\\\
\end{align*}
$$
</div>

Next, we'll set this derivative to 0 and solve for the resulting value of <span class="math-inline">\\(w\\)</span>, called <span class="math-inline">\\(w^*\\)</span>.

Setting this equal to 0 yields:

<div class="math-display">
$$
-\frac{2}{nw} \sum_{i=1}^n \left[\log\left(\frac{y_i}{w}\right)\right] = 0
$$
</div>

From here, we can multiply both sides by <span class="math-inline">\\(-\frac{n}{2}\\)</span>.

<div class="math-display">
$$
\frac{1}{w} \sum_{i=1}^n \left[\log\left(\frac{y_i}{w}\right)\right] = 0
$$
</div>

Next, we'll multiply both sides by <span class="math-inline">\\(w\\)</span>. <span class="math-inline">\\(\frac{1}{w}\\)</span> could never be 0, so this is fine, since it won't change the set of possible values for <span class="math-inline">\\(w^*\\)</span>.

<div class="math-display">
$$
\sum_{i=1}^n \left[\log\left(\frac{y_i}{w}\right)\right] = 0
$$
</div>

From here, we'll use the simplification that <span class="math-inline">\\(\log\left(\frac{y_i}{w}\right) = \log(y_i) - \log(w)\\)</span>.

<div class="math-display">
$$
\sum_{i=1}^n \left[\log(y_i) - \log(w)\right] = 0
$$
</div>

Distributing the sum gives us:

<div class="math-display">
$$
\sum_{i=1}^n \log(y_i) - \sum_{i=1}^n \log(w) = 0
$$
</div>

The second term is the sum of <span class="math-inline">\\(n\\)</span> terms of <span class="math-inline">\\(\log(w)\\)</span>, which is <span class="math-inline">\\(n \log(w)\\)</span>.

<div class="math-display">
$$
\sum_{i=1}^n \log(y_i) - n \log(w) = 0
$$
</div>

Remember, the goal is to isolate <span class="math-inline">\\(w\\)</span>. We're almost there. Adding <span class="math-inline">\\(n \log(w)\\)</span> to both sides and dividing by <span class="math-inline">\\(n\\)</span> gives us:

<div class="math-display">
$$
\log(w) = \frac{1}{n} \sum_{i=1}^n \log(y_i)
$$
</div>

How do we undo the logarithm? By exponentiating both sides, as the hint suggests.

<div class="math-display">
$$
e^{\log(w)} = e^{\frac{1}{n} \sum_{i=1}^n \log(y_i)}
$$
</div>

But <span class="math-inline">\\(e^{\log(w)} = w\\)</span>, so we have:

<div class="math-display">
$$
w = e^{\frac{1}{n} \sum_{i=1}^n \log(y_i)}
$$
</div>

We know that we eventually need to make the right-hand side look like the geometric mean. To help us get there, we can use the fact that <span class="math-inline">\\(\log(a) + \log(b) + \log(c) + ... = \log(a \cdot b \cdot c \cdot ...)\\)</span>.

<div class="math-display">
$$
w = e^{\frac{1}{n} \log(y_1 \cdot y_2 \cdot \ldots \cdot y_n)}
$$
</div>

Then, using the fact that <span class="math-inline">\\(e^{ab} = (e^a)^b\\)</span>, we have:

<div class="math-display">
$$
w = \left( e^{\log(y_1 \cdot y_2 \cdot \ldots \cdot y_n)} \right)^{1/n}
$$
</div>

And finally, using the fact that <span class="math-inline">\\(\log(x)\\)</span> is the inverse of <span class="math-inline">\\(e^x\\)</span>, we have:

<div class="math-display">
$$
w^* = \left( y_1 \cdot y_2 \cdot \ldots \cdot y_n \right)^{1/n} = \boxed{\left( \prod_{i=1}^n y_i \right)^{1/n}}
$$
</div>

which is the geometric mean of <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span>! So, we've shown that the geometric mean minimizes average log-quotient loss for the constant model.

</details>

---

## Problem 3: Slippery Slope (9 pts)

In [Chapter 1.3](https://notes.eecs245.org/introduction-to-supervised-learning/absolute-loss/), we found that <span class="math-inline">\\(w^* = \mathrm{Median}(y_1, y_2, \ldots, y_n)\\)</span> is the constant prediction that minimizes mean absolute error: 

<div class="math-display">
$$
R_{\mathrm{abs}}(w) = \frac{1}{n} \sum_{i=1}^n |y_i - w|
$$
</div>

Suppose that we have a dataset of numbers <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span> such that <span class="math-inline">\\(n\\)</span> is **odd** and the values are arranged in increasing order. That is, <span class="math-inline">\\(y_1 \leq y_2 \leq \cdots \leq y_n\\)</span>.

**Note: Parts a) and b) are independent of each other.**

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose that <span class="math-inline">\\(R_{\mathrm{abs}}(\alpha) = V\\)</span>, where <span class="math-inline">\\(V\\)</span> is the minimum value of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> and <span class="math-inline">\\(\alpha\\)</span> is one of the numbers in our dataset.

Let <span class="math-inline">\\(\alpha + \beta\\)</span> be the smallest value greater than <span class="math-inline">\\(\alpha\\)</span> in our dataset, where <span class="math-inline">\\(\beta &gt; 0\\)</span>. Another way of thinking about this is that <span class="math-inline">\\(\beta =\\)</span> (smallest value greater than <span class="math-inline">\\(\alpha\\)</span>) <span class="math-inline">\\(- \alpha\\)</span>.

Suppose we modify our dataset by replacing the value <span class="math-inline">\\(\alpha\\)</span> with the value <span class="math-inline">\\(\alpha + \beta + 1\\)</span>. In our **new** dataset of <span class="math-inline">\\(n\\)</span> values:

1.  What value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span>?

2.  What is the new minimum value of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span>?

Both of your answers should be expressions involving <span class="math-inline">\\(V\\)</span>, <span class="math-inline">\\(\alpha\\)</span>, <span class="math-inline">\\(\beta\\)</span>, and/or constants.

<em>Hint: Think about the problem on your own for a while. If you're stuck, watch this <a href="https://www.loom.com/share/f0980c9f4d5f4fada99b307014e05cd8?sid=2807514e-c1aa-42d8-8883-7e6d1fab5168">hint video</a>.</em>

<details markdown="1"><summary>Solution</summary>

The new minimum of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> is <span class="math-inline">\\(V + \frac{1}{n}\\)</span>, and the <span class="math-inline">\\(w^*\\)</span> that minimizes <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> for the new dataset is <span class="math-inline">\\(\alpha + \beta\\)</span>.

Make sure to refer to the [hint video](https://www.loom.com/share/f0980c9f4d5f4fada99b307014e05cd8?sid=0066ee1b-a23b-4f5c-bebf-ee751b09a4a4) we recorded for this problem, since it walks through much of our solution.

We are told that <span class="math-inline">\\(\alpha\\)</span> minimizes the mean absolute error on the original dataset. This indicates that <span class="math-inline">\\(\alpha\\)</span> is the median of the dataset, and since we've given that <span class="math-inline">\\(n\\)</span> is odd, it is the unique minimizer of mean absolute error. Before modifying <span class="math-inline">\\(\alpha\\)</span>, here's how our values look on a number line; note that since <span class="math-inline">\\(n\\)</span> is odd, there are <span class="math-inline">\\(\frac{n-1}{2}\\)</span> values to the left of the median, 1 value equal to the median, and <span class="math-inline">\\(\frac{n-1}{2}\\)</span> values to the right of the median.

<div class="math-display">
$$
\underbrace{y_1 \:\:\:\: y_2 \:\:\:\: ... \:\:\:\: y_\frac{n-1}{2}}_{\text{the smallest $\frac{n-1}{2}$ values}} \:\:\:\: \underbrace{\color{blue}\alpha}_\text{the current median} \:\:\:\: \underbrace{{\color{red}\alpha + \beta} \:\:\:\: y_{\frac{n-1}{2} + 3} \:\:\:\: y_{\frac{n-1}{2} + 4} \:\:\:\: ... \:\:\:\: y_n}_{\text{the largest $\frac{n-1}{2}$ values}}
$$
</div>

When we modify the the value of <span class="math-inline">\\(\alpha\\)</span> to be <span class="math-inline">\\(\alpha + \beta + 1\\)</span>, the new median becomes <span class="math-inline">\\(\alpha + \beta\\)</span>, which is the value that was immediately to the right of the old median. The old median and new median swap places.

<div class="math-display">
$$
\underbrace{y_1 \:\:\:\: y_2 \:\:\:\: ... \:\:\:\: y_\frac{n-1}{2}}_{\text{the smallest $\frac{n-1}{2}$ values}} \:\:\:\: \underbrace{{\color{red}\alpha + \beta}}_\text{the new median} \:\:\:\: \underbrace{{\color{blue}\alpha + \beta + 1} \:\:\:\: y_{\frac{n-1}{2} + 3} \:\:\:\: y_{\frac{n-1}{2} + 4} \:\:\:\: ... \:\:\:\: y_n}_{\text{the largest $\frac{n-1}{2}$ values}}
$$
</div>

**Throughout the solution, especially when we break the problem into four cases, make sure to keep refering to the diagram above.**

Now that we know that the new minimizer of <span class="math-inline">\\(R_\text{abs}(w)\\)</span> on the new dataset is <span class="math-inline">\\(\alpha + \beta\\)</span>, we need to calculate <span class="math-inline">\\(R_\text{abs}(\alpha + \beta)\\)</span> on the new dataset --- in other words, we need the mean absolute distance of each point in the new dataset from the new median, <span class="math-inline">\\(\alpha + \beta\\)</span>.

To do so, we'll find the new **sum** of absolute distances from the median and divide it by <span class="math-inline">\\(n\\)</span>, as we'll see that it's easier to think in terms of the sum, or total, absolute error of the whole dataset from the median.

On the old dataset, the sum of absolute distances from the median is <span class="math-inline">\\(Vn\\)</span>, since the old mean absolute distances from the median is <span class="math-inline">\\(V\\)</span>. (We're using the term "absolute distance" here because it feels more intuitive than "absolute error" for this particular problem, but the terms are equivalent.) We'll approach the problem by determining what to add or subtract from <span class="math-inline">\\(Vn\\)</span> to get the new sum of absolute distances from the median.

We can break this into four cases:

-   For the smallest <span class="math-inline">\\(\frac{n-1}{2}\\)</span> values, the new median is now <span class="math-inline">\\(\beta\\)</span> units further away than the old median was --- the new median is <span class="math-inline">\\(\alpha + \beta\\)</span>, which is <span class="math-inline">\\(\beta\\)</span> units further away than the old median was. This adds <span class="math-inline">\\(\boxed{\beta \cdot \left( \frac{n-1}{2} \right)}\\)</span> to the sum of absolute errors from the median.

-   In the old dataset, exactly one of the <span class="math-inline">\\(n\\)</span> values was equal to the median, and that point had an absolute distance of 0 from the median. That's still the case in the new dataset, so this fact alone doesn't change the sum of absolute errors from the median.

-   The distance between the median and the point immediately to the right of it used to be <span class="math-inline">\\(({\color{red}\alpha + \beta}) - {\color{blue}\alpha} = \beta\\)</span>, but is now <span class="math-inline">\\(({\color{blue}\alpha + \beta + 1}) - ({\color{red}\alpha + \beta}) = 1\\)</span>. The difference between these two is <span class="math-inline">\\(1 - \beta\\)</span>; if <span class="math-inline">\\(\beta &gt; 1\\)</span>, these two points are now closer than they were before, and if <span class="math-inline">\\(\beta &lt; 1\\)</span>, these two points are now further than they were before. This adds <span class="math-inline">\\(\boxed{1 - \beta}\\)</span> to the sum of absolute errors from the median.

-   For the largest <span class="math-inline">\\(\frac{n-1}{2} - 1\\)</span> values --- that is, the last bracket from the diagram, excluding <span class="math-inline">\\(\alpha + \beta + 1\\)</span> --- the new median is now <span class="math-inline">\\(\beta\\)</span> units closer than the old median was. This subtracts <span class="math-inline">\\(\beta \cdot \left( \frac{n-1}{2} - 1 \right)\\)</span> from the sum of absolute errors from the median, or equivalently, adds <span class="math-inline">\\(\boxed{-\beta \cdot \left( \frac{n-1}{2} - 1 \right)}\\)</span>.

So, the new sum of absolute errors from the median is:

<div class="math-display">
$$
Vn + \beta \cdot \left( \frac{n-1}{2} \right) + 1 - \beta - \beta \cdot \left( \frac{n-1}{2} - 1 \right) = Vn + 1
$$
</div>

And so the mean of absolute errors from the median, <span class="math-inline">\\(R_\text{abs}(\alpha + \beta)\\)</span>, in the new dataset, is:

<div class="math-display">
$$
\frac{Vn+1}{n} = \boxed{V + \frac{1}{n}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(y_a\\)</span> and <span class="math-inline">\\(y_b\\)</span> be two values in our dataset such that <span class="math-inline">\\(y_a &lt; y_b\\)</span> and that the slope of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> between <span class="math-inline">\\(w = y_a\\)</span> and <span class="math-inline">\\(w = y_b\\)</span> is constant, and equal to <span class="math-inline">\\(-\frac{2}{3}\\)</span>.

Suppose we introduce a new value to our dataset that is less than <span class="math-inline">\\(y_a\\)</span>. In our **new** dataset of <span class="math-inline">\\(n+1\\)</span> values, what is the slope of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> between <span class="math-inline">\\(w = y_a\\)</span> and <span class="math-inline">\\(w = y_b\\)</span>? Your answer should be an expression involving <span class="math-inline">\\(n\\)</span> and/or constants, but should not contain <span class="math-inline">\\(a\\)</span> or <span class="math-inline">\\(b\\)</span>, or any value of <span class="math-inline">\\(y\\)</span>.

<details markdown="1"><summary>Solution</summary>

We know from Chapter 1.3 that the slope of <span class="math-inline">\\(R_\text{abs}(w)\\)</span> at any <span class="math-inline">\\(w\\)</span> that is not a data point is:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_{\mathrm{abs}}(w) = \frac{\# \text{ left of } w - \# \text{ right of } w}{n}
$$
</div>

In the region between <span class="math-inline">\\(w = y_a\\)</span> and <span class="math-inline">\\(w = y_b\\)</span>, the slope is constant, meaning there are no data points between <span class="math-inline">\\(y_a\\)</span> and <span class="math-inline">\\(y_b\\)</span>, since if there were, the slope would change at that point.

Suppose <span class="math-inline">\\(w'\\)</span> is some value between <span class="math-inline">\\(y_a\\)</span> and <span class="math-inline">\\(y_b\\)</span>, meaning that it's on the line segment whose slope we know about. Let <span class="math-inline">\\(k\\)</span> be the number of data points less than <span class="math-inline">\\(w'\\)</span>. Then, the number of data points greater than <span class="math-inline">\\(w'\\)</span> is <span class="math-inline">\\(n - k\\)</span>, and:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_{\mathrm{abs}}(w') = \frac{k - (n - k)}{n} = \frac{2k - n}{n} = \underbrace{-\frac{2}{3}}_{\text{given to us in the question}}
$$
</div>

In the new dataset, since we add a point to the left of <span class="math-inline">\\(y_a\\)</span>, the number of data points less than <span class="math-inline">\\(w'\\)</span> is now <span class="math-inline">\\(k+1\\)</span>, while the number of data points greater than <span class="math-inline">\\(w'\\)</span> is still <span class="math-inline">\\(n - k\\)</span>. Therefore, in the **new** dataset, the slope of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> between <span class="math-inline">\\(w = y_a\\)</span> and <span class="math-inline">\\(w = y_b\\)</span> is:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_{\mathrm{abs}}(w') = \frac{(k+1) - (n - k)}{n+1} = \frac{2k + 1 - n}{n+1} = s
$$
</div>

(<span class="math-inline">\\(s\\)</span> is a new variable we've introduced here to represent the slope in the new dataset.)

The problem now boils down to re-writing <span class="math-inline">\\(s\\)</span> in terms of <span class="math-inline">\\(n\\)</span> only, not involving <span class="math-inline">\\(k\\)</span>. To do this, we'll use the final result from the first equation:

<div class="math-display">
$$
\frac{2k - n}{n} = -\frac{2}{3} \implies 2k - n = -\frac{2}{3}n \implies 2k = \frac{n}{3} \implies k = \frac{n}{6}
$$
</div>

Plugging <span class="math-inline">\\(k = \frac{n}{6}\\)</span> into the equation for <span class="math-inline">\\(s\\)</span>, we get:

<div class="math-display">
$$
\begin{align*}
s &= \frac{2k + 1 - n}{n+1} \\\\
&= \frac{2 \cdot \frac{n}{6} + 1 - n}{n+1} \\\\
&= \frac{\frac{n}{3} + 1 - n}{n+1} \\\\
&= \boxed{\frac{-\frac{2}{3}n + 1}{n+1}}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 4: Fun with Correlation (8 pts)

As we will see in [Chapter 2.4](https://notes.eecs245.org/simple-linear-regression/correlation/), the correlation coefficient <span class="math-inline">\\(r\\)</span> between two variables <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> measures the strength of the linear association between them, or intuitively, how tightly the points cluster around a line. Formally, <span class="math-inline">\\(r\\)</span> is defined as: 

<div class="math-display">
$$
r = \frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right)
$$
</div>

where <span class="math-inline">\\(\bar{x}\\)</span> and <span class="math-inline">\\(\bar{y}\\)</span> are the means of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>, respectively, and <span class="math-inline">\\(\sigma_x\\)</span> and <span class="math-inline">\\(\sigma_y\\)</span> are the standard deviations of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>, respectively.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(r\\)</span> be the correlation coefficient between <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>. Let <span class="math-inline">\\(t\\)</span> be a new variable defined as:

<div class="math-display">
$$
t_i = -2x_i + 5, \qquad i = 1, \ldots, n
$$
</div>

Let <span class="math-inline">\\(r'\\)</span> be the correlation coefficient between <span class="math-inline">\\(t\\)</span> and <span class="math-inline">\\(y\\)</span>. Prove that <span class="math-inline">\\(r' = -r\\)</span>.

<em>Hint: You can use the facts that if <span class="math-inline">\\(t_i = ax_i + b\\)</span>, then <span class="math-inline">\\(\bar{t} = a\bar{x} + b\\)</span> and <span class="math-inline">\\(\sigma_t = |a|\sigma_x\\)</span>, without proof. Everything else must be derived from the definition of the correlation coefficient.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
r'&= \frac{1}{n} \sum_{i=1}^n \left( \frac{t_i - \bar{t}}{\sigma_t} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right) \\\\
&= \frac{1}{n} \sum_{i=1}^n \left( \frac{-2x_i+5 - (-2\bar{x}+5)}{2\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right) \\\\
&= \frac{1}{n} \sum_{i=1}^n \left( \frac{-2x_i + 2\bar{x}}{2\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right) \\\\
&= \frac{1}{n} \sum_{i=1}^n \left( \frac{-2(x_i -\bar{x})}{2\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right) \\\\
&= \frac{1}{n} \sum_{i=1}^n \left( -\frac{x_i -\bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right) \\\\
&= -\frac{1}{n} \sum_{i=1}^n \left( \frac{x_i -\bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right) \\\\
&= -r
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose we fit two simple linear regression models by minimizing mean squared error.

-   Model 1: <span class="math-inline">\\(\text{predicted } y_i = h(x_i) = w_0^* + w_1^* x_i\\)</span>

-   Model 2: <span class="math-inline">\\(\text{predicted } y_i = h'(t_i) = w_0' + w_1' t_i\\)</span>

(The <span class="math-inline">\\('\\)</span> does not indicate a derivative here!)

We already know that <span class="math-inline">\\(r' = -r\\)</span>. How do the other quantities compare between the two lines?

1.  Express <span class="math-inline">\\(w_1'\\)</span> in terms of <span class="math-inline">\\(w_1^*\\)</span>, <span class="math-inline">\\(w_0^*\\)</span>, and/or constants (but no other variables).

2.  Express <span class="math-inline">\\(w_0'\\)</span> in terms of <span class="math-inline">\\(w_0^*\\)</span>, <span class="math-inline">\\(w_1^*\\)</span>, and/or constants (but no other variables).

3.  Above, you should have found that the new slope, <span class="math-inline">\\(w_1'\\)</span>, and new intercept, <span class="math-inline">\\(w_0'\\)</span>, are different than the original slope and intercept. However, it turns out that the mean squared error of both model's predictions are the same. That is:

    

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n (y_i - (w_0' + w_1' t_i))^2 = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0^* + w_1^* x_i))^2
$$
</div>

   Give a two-sentence English explanation of why this is the case.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
w_1'&=r'\frac{\sigma_y}{\sigma_t} \\\\
&=-r\frac{\sigma_y}{2\sigma_x} \\\\
&=-\frac{1}{2}r\frac{\sigma_y}{\sigma_x} \\\\
&=-\frac{1}{2}w_1^* \\\\
\\\\
w_0'&=\bar{y}-w_1'\bar{t} \\\\
&=\bar{y}-(-\frac{1}{2}w_1^* \cdot (-2\bar{x}+5)) \\\\
&=\bar{y}-(w_1^*\bar{x} - \frac{5}{2}w_1^*) \\\\
&=\bar{y}-w_1^*\bar{x} + \frac{5}{2}w_1^* \\\\
&=w_0^* + \frac{5}{2}w_1^*
\end{align*}
$$
</div>

When you apply a scaling or shifting transformation on <span class="math-inline">\\(x\\)</span>, the model's line will adjust its slope and intercept to give the same predictions as before to MSE. The model aims to minimize the difference between the actual <span class="math-inline">\\(y\\)</span>'s and the predictions, so if the actual <span class="math-inline">\\(y\\)</span>'s and predictions stay the same, then the MSE will also be the same.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(0 pts, **optional**) This part is challenging and potentially time-consuming, so we've made it optional. It's good exam practice though, so if you don't do it now, you should return to it later on when you have more time. It is independent of the previous two parts of this problem.

Prove that, for any dataset <span class="math-inline">\\((x_1, y_1), \ldots, (x_n, y_n)\\)</span> with a correlation coefficient <span class="math-inline">\\(r\\)</span>,

<div class="math-display">
$$
\underbrace{\frac{1}{n} \sum_{i=1}^n (y_i - (w_0^* + w_1^* x_i))^2}_{\text{mean squared error of optimal SLR model}} = \underbrace{\sigma_y^2 (1 - r^2)}_{\text{function of correlation coefficient}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
&\frac{1}{n} \sum_{i=1}^n (y_i - (w_0^* + w_1^* x_i))^2 \\\\
&=\frac{1}{n} \sum_{i=1}^n (y_i - (\bar{y}-w_1^*\bar{x} + w_1^* x_i))^2 && \text{sub in } w_0^* \\\\
&=\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y}+w_1^*\bar{x} - w_1^* x_i)^2 \\\\
&=\frac{1}{n} \sum_{i=1}^n ((y_i - \bar{y})-w_1^*(x_i-\bar{x}))^2 \\\\
&=\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2-2((y_i - \bar{y})\cdot w_1^*(x_i-\bar{x}))+(w_1^*(x_i-\bar{x}))^2 && \text{expand square} \\\\
&=\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2-\frac{1}{n} \sum_{i=1}^n2((y_i - \bar{y})\cdot w_1^*(x_i-\bar{x}))+\frac{1}{n} \sum_{i=1}^n(w_1^*(x_i-\bar{x}))^2 && \text{expand summation}
\end{align*}
$$
</div>

Let's simplify each of the summations separately, starting with the one on the left which we can rewrite in terms of <span class="math-inline">\\(\sigma_y\\)</span>:

<div class="math-display">
$$
\begin{align*}
\sigma_y &= \sqrt{\frac{1}{n} \sum_{i=1}^n(y_i-\bar{y})^2} \\\\
\sigma_y^2 &= \frac{1}{n} \sum_{i=1}^n(y_i-\bar{y})^2
\end{align*}
$$
</div>

We can apply a similar method to the term on the right:

<div class="math-display">
$$
\begin{align*}
&\frac{1}{n} \sum_{i=1}^n(w_1^*(x_i-\bar{x}))^2 \\\\
&=\frac{1}{n} \sum_{i=1}^n((r\frac{\sigma_y}{\sigma_x})(x_i-\bar{x}))^2 \\\\
&=\frac{1}{n} \sum_{i=1}^n(r\frac{\sigma_y}{\sigma_x})^2(x_i-\bar{x})^2 \\\\
&=(r\frac{\sigma_y}{\sigma_x})^2 \cdot \big(\frac{1}{n} \sum_{i=1}^n(x_i-\bar{x})^2 \big) \\\\
&=(r\frac{\sigma_y}{\sigma_x})^2 \cdot \sigma_x^2 \\\\
&=r^2\sigma_y^2
\end{align*}
$$
</div>

Next, simplify the middle term:

<div class="math-display">
$$
\begin{align*}
&\frac{1}{n} \sum_{i=1}^n2((y_i - \bar{y})\cdot w_1^*(x_i-\bar{x})) \\\\
&=2w_1^* \cdot \big(\frac{1}{n} \sum_{i=1}^n(y_i - \bar{y})\cdot (x_i-\bar{x}) \big) \\\\
&=2w_1^* \cdot r\sigma_x \sigma_y \:\:\:\:\:\: \text{rewriting in terms of } r=\frac{1}{n}\sum_{i=1}^{n}(\frac{x_i-\bar{x}}{\sigma_x})(\frac{y_i-\bar{y}}{\sigma_y}) \\\\
&=2r\frac{\sigma_y}{\sigma_x} \cdot r\sigma_x \sigma_y \:\:\:\:\: \text{substitute } w_1^* \\\\
&=2r^2\sigma_y^2
\end{align*}
$$
</div>

Finally, let's put all of that together:

<div class="math-display">
$$
\begin{align*}
&\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2-\frac{1}{n} \sum_{i=1}^n2((y_i - \bar{y})\cdot w_1^*(x_i-\bar{x}))+\frac{1}{n} \sum_{i=1}^n(w_1^*(x_i-\bar{x}))^2 \\\\
&=\sigma_y^2 - 2r^2\sigma_y^2+r^2\sigma_y^2 \\\\
&=\sigma_y^2(1-2r^2+r^2) \\\\
&=\sigma_y^2(1-r^2)
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 5: Switching Sides (9 pts)

Consider two datasets, <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>. Both datasets have <span class="math-inline">\\(n = 50\\)</span> points, of which 49 are identical, and only one is different between the two datasets:

-   **Dataset <span class="math-inline">\\(A\\)</span>**: <span class="math-inline">\\((22, 10), (x_2, y_2), \ldots, (x_{49}, y_{49}), (x_{50}, y_{50})\\)</span>

-   **Dataset <span class="math-inline">\\(B\\)</span>**: <span class="math-inline">\\((22, 50), \underbrace{(x_2, y_2), \ldots, (x_{49}, y_{49}), (x_{50}, y_{50})}_{\text{identical in both datasets}}\\)</span>

Suppose that in both datasets, the <span class="math-inline">\\(x\\)</span>-values have a mean of <span class="math-inline">\\(\bar{x} = 26\\)</span> and a standard deviation of <span class="math-inline">\\(\sigma_x = \sqrt{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2} = 3\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose we fit a simple linear regression model by minimizing mean squared error, separately for each dataset.

Let <span class="math-inline">\\(w_1^A\\)</span> and <span class="math-inline">\\(w_1^B\\)</span> be the optimal slopes for datasets <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, respectively. Determine the difference between <span class="math-inline">\\(w_1^B\\)</span> and <span class="math-inline">\\(w_1^A\\)</span>. That is, find:

<div class="math-display">
$$
w_1^B - w_1^A
$$
</div>

Your answer should be a number with no variables.

<em>Hint: There are many equivalent formulas for the slope of the regression line. We recommend using this one for this problem: </em>

<div class="math-display">
$$
w_1^* = \displaystyle\frac{\displaystyle\sum_{i=1}^n (x_i - \overline x)y_i}{\displaystyle\sum_{i=1}^n (x_i - \overline x)^2}
$$
</div>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(-\frac{16}{45}\\)</span>

Since the datasets are identical for all <span class="math-inline">\\(i&gt;1\\)</span>, we can rewrite the summation 

<div class="math-display">
$$
\sum_{i=1}^n (x_i-\overline{x})y_i
$$
</div>

 as 

<div class="math-display">
$$
(x_1-\overline{x})y_1 + \sum_{i=2}^n(x_i-\overline{x})y_i
$$
</div>

In dataset <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(x_1 = 22\\)</span> and <span class="math-inline">\\(y_1 = 10\\)</span>. In dataset <span class="math-inline">\\(B\\)</span>, <span class="math-inline">\\(x_1 = 22\\)</span> and <span class="math-inline">\\(y_1 = 50\\)</span>. But in both datasets, 

<div class="math-display">
$$
\sum_{i=2}^n (x_i - \overline{x})y_i
$$
</div>

 is the same, and so is 

<div class="math-display">
$$
\sum_{i=1}^n (x_i - \overline{x})^2
$$
</div>

So, **the difference** between their two optimal slopes is:

<div class="math-display">
$$
\begin{align*}
w_1^B - w_1^A
&= \frac{(22-26)50 + \sum_{i=2}^n (x_i - \overline{x})y_i}{\sum_{i=1}^n (x_i - \overline{x})^2}
- \frac{(22-26)10 + \sum_{i=2}^n (x_i - \overline{x})y_i}{\sum_{i=1}^n (x_i - \overline{x})^2} \\\\
&= \frac{(22-26)(50-10)}{\sum_{i=1}^n (x_i - \overline{x})^2}
\end{align*}
$$
</div>

The denominator, <span class="math-inline">\\(\sum_{i=1}^n (x_i - \overline{x})^2\\)</span>, is <span class="math-inline">\\(n\\)</span> times the variance of the <span class="math-inline">\\(x\\)</span>-values, which is 

<div class="math-display">
$$
n\sigma_x^2 = 50 \cdot 3^2 = 450
$$
</div>

So numerically the difference is: 

<div class="math-display">
$$
w_1^B - w_1^A
= \frac{(22-26)(50-10)}{450}
= \frac{-160}{450}
= -\frac{16}{45}
$$
</div>

So, since <span class="math-inline">\\(x_1 &lt; \bar{x}\\)</span>, dataset <span class="math-inline">\\(B\\)</span>'s slope is less than dataset <span class="math-inline">\\(A\\)</span>'s slope.

To further our understanding of the problem, if <span class="math-inline">\\(x_1 &gt; \bar{x}\\)</span>, dataset B's slope would have been greater than dataset A's slope.

We've produced an interactive visualization of what's going on.

[Find the visualization here.](https://eecs245.org/resources/homeworks/hw02/hw02-regression-point-vis.html)

The slider you'll see in the resulting visualization will allow you to change the value of <span class="math-inline">\\(x_1\\)</span> and observe how the fitted regression lines change in response. In the visualization, as you move <span class="math-inline">\\(x_1\\)</span>, the mean <span class="math-inline">\\(\bar{x}\\)</span> changes ever so slightly to reflect your new choice of <span class="math-inline">\\(x_1\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(h_A\\)</span> and <span class="math-inline">\\(h_B\\)</span> be the simple linear regression lines for datasets <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, respectively. That is, <span class="math-inline">\\(h_A(x_i) = w_0^A + w_1^A x_i\\)</span> and <span class="math-inline">\\(h_B(x_i) = w_0^B + w_1^B x_i\\)</span>.

Which of the following values is greater: <span class="math-inline">\\(|h_A(40) - h_B(40)|\\)</span> or <span class="math-inline">\\(|h_A(42) - h_B(42)|\\)</span>? Why?

<em>Hint: Intuitively, we're asking which input's predicted value changes more by switching from <span class="math-inline">\\(A\\)</span> to <span class="math-inline">\\(B\\)</span>. Don't try and expand the absolute differences or find their values exactly. Instead, draw a picture of both lines. For each line, there is one point that it is guaranteed to pass through. Using your knowledge of that point, and the slopes of the lines, you should be able to reason about which difference is greater. In your picture, assume that the lines intersect at some point to the left of <span class="math-inline">\\(x = 40\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(|h_A(42) - h_B(42)| \text{ is greater.}\\)</span>

From part (a), we know that 

<div class="math-display">
$$
w_1^B < w_1^A
$$
</div>

 so the two regression lines are not parallel.

From [Chapter 2.3](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/#regression-line-passes-through-the-mean), we know that each regression line is guaranteed to pass through the point <span class="math-inline">\\((\overline{x}, \overline{y})\\)</span> for its own dataset.

Since <span class="math-inline">\\(y_1^B &gt; y_1^A\\)</span> (that is, since <span class="math-inline">\\(50 &gt; 10\\)</span>), we know that <span class="math-inline">\\(\overline{y}^B &gt; \overline{y}^A\\)</span>. More precisely, dataset <span class="math-inline">\\(B\\)</span> increases the total sum of <span class="math-inline">\\(y\\)</span>-values by <span class="math-inline">\\(40\\)</span>, so 

<div class="math-display">
$$
\bar{y}^B
= \frac{40 + 50 \cdot \bar{y}^A}{50}
= \bar{y}^A + \frac{4}{5}
$$
</div>

This means that dataset <span class="math-inline">\\(A\\)</span>'s regression line passes through <span class="math-inline">\\((26, \bar{y}^A)\\)</span>, while dataset <span class="math-inline">\\(B\\)</span>'s regression line passes through <span class="math-inline">\\((26, \bar{y}^A + \frac{4}{5})\\)</span>.

Because <span class="math-inline">\\(x_1 = 22 &lt; \bar{x} = 26\\)</span>, we showed in part (a) that <span class="math-inline">\\(w_1^B &lt; w_1^A\\)</span>. This implies that the two regression lines intersect at some point to the **right** of <span class="math-inline">\\(x = 26\\)</span>.

The difference between the two models' predictions is larger for inputs that are farther from the point of intersection. Since the intersection occurs to the right of <span class="math-inline">\\(x = 26\\)</span> **but to the left of <span class="math-inline">\\(x=40\\)</span>** (as mentioned in the problem), the input <span class="math-inline">\\(x = 42\\)</span> is farther from the intersection than <span class="math-inline">\\(x = 40\\)</span> is.

Therefore, 

<div class="math-display">
$$
|h_A(42) - h_B(42)| > |h_A(40) - h_B(40)|
$$
</div>

![image](imgs/hw02-problem4-sol.png)

</details>

</div>
</div>

</div>

---

## Problem 6: Simple LAD (9 pts)

This problem involves writing code and submitting it to the Gradescope autograder.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open `homeworks/hw02/hw02.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw02%2Fhw02.ipynb&branch=main) to open `hw02.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

To receive credit for the programming portion of the homework, you'll need to submit your completed notebook to the autograder on Gradescope. Your submission time for Homework 2 is the **latter** of your PDF and code submission times.

{% endraw %}
