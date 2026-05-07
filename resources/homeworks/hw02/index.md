---
layout: page
title: "Homework 2: Empirical Risk and Simple Linear Regression"
description: "Homework 2: Empirical Risk and Simple Linear Regression problems."
nav_exclude: true
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
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
</style>

# Homework 2: Empirical Risk and Simple Linear Regression

**due** Wednesday, May 13th, 2026 at 11:59PM Ann Arbor Time

<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw02/hw02.pdf" target="_blank">View as PDF ✏️</a>

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
- [Problem 3: Pythagorean Means](#problem-3-pythagorean-means-7-pts)
- [Problem 4: Slippery Slope](#problem-4-slippery-slope-9-pts)
- [Problem 5: Fun with Correlation](#problem-5-fun-with-correlation-8-pts)
- [Problem 6: Switching Sides](#problem-6-switching-sides-9-pts)
- [Problem 7: Simple LAD](#problem-7-simple-lad-9-pts)

---

Total Points: 10 + 7 + 9 + 8 + 9 + 9 = 52

---

## Problem 1: Homework 1 Solutions Review (10 pts)

Review the solutions to Homework 1. Pick **two problem parts** (for example, Problem 3a and Problem 5) from Homework 1 in which your solutions have the most room for improvement, i.e., where they have unsound reasoning, could be significantly more efficient or clearer, etc. **Include a screenshot of your solution to each problem part**, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 1, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

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

Like the arithmetic mean, as we saw in [Chapter 1.2](https://notes.eecs245.org/supervised-learning/loss-functions-constant-model/), and the harmonic mean, as we saw in Lab 2, the geometric mean is the constant prediction that minimizes average loss for some loss function.

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

<em>Hint: As in Lecture 3, you'll want to start by finding <span class="math-inline">\\(\frac{\text{d}}{\text{d}w} R_{LQ}(w)\\)</span> and setting that to 0. As a sub-problem, you'll need to find <span class="math-inline">\\(\frac{\text{d}}{\text{d}w} \left[\log\left(\frac{y_i}{w}\right)\right]\\)</span>. Work one step at a time and make sure your logic is clearly justified. Review the logarithm rules presented in [Homework 1, Problem 5](https://eecs245.org/resources/homeworks/hw01/hw01.pdf), and also use the fact that if <span class="math-inline">\\(b = \log(a)\\)</span>, then <span class="math-inline">\\(a = e^b\\)</span>.</em>

---

## Problem 3: Pythagorean Means (7 pts)

In Problem 1, you discovered the geometric mean, and saw that it's useful in computing the average of growth rates. In Labs 1 and 2, you discovered the harmonic mean, and saw that it's useful to compute the average of rates, like speeds. The geometric mean, harmonic mean, and the "regular" arithmetic mean are collectively known as "Pythagorean means".

For an arbitrary dataset of **positive** numbers <span class="math-inline">\\(y_1, \ldots, y_n\\)</span>, they are defined as follows:

-   **Arithmetic mean:** <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum_{i=1}^n y_i\\)</span>

-   **Geometric mean:** <span class="math-inline">\\(\displaystyle \left( \prod_{i=1}^n y_i \right)^{1/n}\\)</span>

-   **Harmonic mean:** <span class="math-inline">\\(\displaystyle \frac{n}{\sum_{i=1}^n \frac{1}{y_i}}\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) For the following dataset, compute all three of the means defined above.

<div class="math-display">
$$
1, 2, 2, 4, 8
$$
</div>

Then, think about why the definitions of the geometric and harmonic means require the numbers to be positive. (You don't need to write your answer anywhere.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) In the above example, you may have noticed that:

<div class="math-display">
$$
\text{arithmetic mean} \geq \text{geometric mean} \geq \text{harmonic mean}
$$
</div>

This inequality is true in general, for any dataset of positive numbers <span class="math-inline">\\(y_1, \ldots, y_n\\)</span>. This is known as the AM-GM-HM inequality.

Use the fact that the AM-GM inequality holds true to prove the GM-HM inequality. That is, given that: 

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n y_i \geq \left( \prod_{i=1}^n y_i \right)^{1/n}
$$
</div>

 Prove that: 

<div class="math-display">
$$
\left( \prod_{i=1}^n y_i \right)^{1/n} \geq \frac{n}{\sum_{i=1}^n \frac{1}{y_i}}
$$
</div>

<em>Hint: Start by assuming the AM-GM inequality holds true, and define <span class="math-inline">\\(z_i = \frac{1}{y_i}\\)</span>. Then, try and re-write the right side of the inequality to look like <span class="math-inline">\\(\frac{1}{n} \sum_{i=1}^n z_i\\)</span>.</em>

If you're curious, read more about the history of the Pythagorean means [here](https://historyofdsc.com/resources/slides/lec03-annotated.pdf#page=4). These means were developed by the followers of ancient mathematician Pythagoras (whose namesake theorem you're familiar with) in the context of understanding harmonies in music. And you now know how to derive each one by minimizing average loss for the constant model, each one through a different loss function!

</div>
</div>

</div>
---

## Problem 4: Slippery Slope (9 pts)

In [Chapter 1.3](https://notes.eecs245.org/supervised-learning/empirical-risk-minimization/), we found that <span class="math-inline">\\(w^* = \mathrm{Median}(y_1, y_2, \ldots, y_n)\\)</span> is the constant prediction that minimizes mean absolute error: 

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

Let <span class="math-inline">\\(\alpha + \beta\\)</span> be the smallest value greater than <span class="math-inline">\\(\alpha\\)</span> in our dataset, where <span class="math-inline">\\(\beta > 0\\)</span>. Another way of thinking about this is that <span class="math-inline">\\(\beta =\\)</span> (smallest value greater than <span class="math-inline">\\(\alpha\\)</span>) <span class="math-inline">\\(- \alpha\\)</span>.

Suppose we modify our dataset by replacing the value <span class="math-inline">\\(\alpha\\)</span> with the value <span class="math-inline">\\(\alpha + \beta + 1\\)</span>. In our **new** dataset of <span class="math-inline">\\(n\\)</span> values:

1.  What value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span>?

2.  What is the new minimum value of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span>?

Both of your answers should be expressions involving <span class="math-inline">\\(V\\)</span>, <span class="math-inline">\\(\alpha\\)</span>, <span class="math-inline">\\(\beta\\)</span>, and/or constants.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Let <span class="math-inline">\\(y_a\\)</span> and <span class="math-inline">\\(y_b\\)</span> be two values in our dataset such that <span class="math-inline">\\(y_a < y_b\\)</span> and that the slope of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> between <span class="math-inline">\\(w = y_a\\)</span> and <span class="math-inline">\\(w = y_b\\)</span> is constant, and equal to <span class="math-inline">\\(-\frac{2}{3}\\)</span>.

Suppose we introduce a new value to our dataset that is less than <span class="math-inline">\\(y_a\\)</span>. In our **new** dataset of <span class="math-inline">\\(n+1\\)</span> values, what is the slope of <span class="math-inline">\\(R_{\mathrm{abs}}(w)\\)</span> between <span class="math-inline">\\(w = y_a\\)</span> and <span class="math-inline">\\(w = y_b\\)</span>? Your answer should be an expression involving <span class="math-inline">\\(n\\)</span> and/or constants, but should not contain <span class="math-inline">\\(a\\)</span> or <span class="math-inline">\\(b\\)</span>, or any value of <span class="math-inline">\\(y\\)</span>.

</div>
</div>

</div>
---

## Problem 5: Fun with Correlation (8 pts)

As we saw in Chapter 1.4, the correlation coefficient <span class="math-inline">\\(r\\)</span> between two variables <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> measures the strength of the linear association between them, or intuitively, how tightly the points cluster around a line. Formally, <span class="math-inline">\\(r\\)</span> is defined as: 

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
(3 pts) Let <span class="math-inline">\\(r\\)</span> be the correlation coefficient between <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>. Let <span class="math-inline">\\(z\\)</span> be a new variable defined as:

<div class="math-display">
$$
z_i = -2x_i + 5, \qquad i = 1, \ldots, n
$$
</div>

Let <span class="math-inline">\\(r'\\)</span> be the correlation coefficient between <span class="math-inline">\\(z\\)</span> and <span class="math-inline">\\(y\\)</span>. Prove that <span class="math-inline">\\(r' = -r\\)</span>.

<em>Hint: You can use the facts that if <span class="math-inline">\\(z_i = ax_i + b\\)</span>, then <span class="math-inline">\\(\bar{z} = a\bar{x} + b\\)</span> and <span class="math-inline">\\(\sigma_z = |a|\sigma_x\\)</span>, without proof. Everything else must be derived from the definition of the correlation coefficient.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose we fit two simple linear regression models by minimizing mean squared error.

-   Model 1: <span class="math-inline">\\(\text{predicted } y_i = h(x_i) = w_0^* + w_1^* x_i\\)</span>

-   Model 2: <span class="math-inline">\\(\text{predicted } y_i = h'(z_i) = w_0' + w_1' z_i\\)</span>

(The <span class="math-inline">\\('\\)</span> does not indicate a derivative here!)

We already know that <span class="math-inline">\\(r' = -r\\)</span>. How do the other quantities compare between the two lines?

1.  Express <span class="math-inline">\\(w_1'\\)</span> in terms of <span class="math-inline">\\(w_1^*\\)</span>, <span class="math-inline">\\(w_0^*\\)</span>, and/or constants (but no other variables).

2.  Express <span class="math-inline">\\(w_0'\\)</span> in terms of <span class="math-inline">\\(w_0^*\\)</span>, <span class="math-inline">\\(w_1^*\\)</span>, and/or constants (but no other variables).

3.  Above, you should have found that the new slope, <span class="math-inline">\\(w_1'\\)</span>, and new intercept, <span class="math-inline">\\(w_0'\\)</span>, are different than the original slope and intercept. However, it turns out that the mean squared error of both model's predictions are the same. That is:

    

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n (y_i - (w_0' + w_1' z_i))^2 = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0^* + w_1^* x_i))^2
$$
</div>

   Give a two-sentence English explanation of why this is the case.

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

</div>
</div>

</div>
---

## Problem 6: Switching Sides (9 pts)

Consider two datasets, <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>. Both datasets have <span class="math-inline">\\(n = 50\\)</span> points, of which 49 are identical, and only one is different between the two datasets:

-   **Dataset <span class="math-inline">\\(A\\)</span>**: <span class="math-inline">\\((26, 10), (x_2, y_2), \ldots, (x_{49}, y_{49}), (x_{50}, y_{50})\\)</span>

-   **Dataset <span class="math-inline">\\(B\\)</span>**: <span class="math-inline">\\((26, 50), \underbrace{(x_2, y_2), \ldots, (x_{49}, y_{49}), (x_{50}, y_{50})}_{\text{identical in both datasets}}\\)</span>

Suppose that in both datasets, the <span class="math-inline">\\(x\\)</span>-values have a mean of <span class="math-inline">\\(\bar{x} = 26\\)</span> and a standard deviation of <span class="math-inline">\\(\sigma_x = \sqrt{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2} = 3\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Suppose we fit a simple linear regression model by minimizing mean squared error, separately for each dataset.

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

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Let <span class="math-inline">\\(h_A\\)</span> and <span class="math-inline">\\(h_B\\)</span> be the simple linear regression lines for datasets <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, respectively. That is, <span class="math-inline">\\(h_A(x_i) = w_0^A + w_1^A x_i\\)</span> and <span class="math-inline">\\(h_B(x_i) = w_0^B + w_1^B x_i\\)</span>.

Which of the following values is greater: <span class="math-inline">\\(|h_A(43) - h_B(43)|\\)</span> or <span class="math-inline">\\(|h_A(24) - h_B(24)|\\)</span>? Why?

<em>Hint: Intuitively, we're asking which input's predicted value changes more by switching from <span class="math-inline">\\(A\\)</span> to <span class="math-inline">\\(B\\)</span>. Don't try and expand the absolute differences or find their values exactly. Instead, draw a picture of both lines. For each line, there is one point that it is guaranteed to pass through. Using your knowledge of that point, and the slopes of the lines, you should be able to reason about which difference is greater.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) When initially writing this problem, we gave it a real-world theme involving athletes and their salaries. However, we decided that the story made the problem too long, and made it more difficult to understand the relevant ideas. But, you may feel that the resulting problem seemed too abstract.

Would you have preferred a real-world theme in this problem, or do you prefer the simplified, straight-forward version, and why? (As long as you provide an answer and a reason, you'll receive full credit. There is no right answer.)

</div>
</div>

</div>
---

## Problem 7: Simple LAD (9 pts)

This problem involves writing code and submitting it to the Gradescope autograder.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa25&urlpath=tree%2Ffa25%2Fhomeworks%2Fhw02%2Fhw02.ipynb&branch=main) to open `hw02.ipynb` on DataHub. Before doing so, read the instructions on the [Tech Support](https://eecs245.org/tech-support/#option-1-using-the-eecs-245-datahub) page on how to use the DataHub.

-   **Option 2**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/fa25), and open `homeworks/hw02/hw02.ipynb`. For instructions on how to do this, see the [Tech Support](https://eecs245.org/tech-support) page of the course website.

To receive credit for the programming portion of the homework, you'll need to submit your completed notebook to the autograder on Gradescope. Your submission time for Homework 2 is the **latter** of your PDF and code submission times.
