---
layout: page
title: "Lab 2: Empirical Risk and Simple Linear Regression"
description: "Lab 2: Empirical Risk and Simple Linear Regression activities."
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
</style>

# Lab 2: Empirical Risk and Simple Linear Regression

**due** for completion at 11:59PM Ann Arbor Time on Monday, May 11th, 2026

<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab02/lab02.pdf" target="_blank">View as PDF ✏️</a>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Relative Squared Loss](#activity-1-relative-squared-loss)
- [Activity 2: Rapid Fire](#activity-2-rapid-fire)
- [Activity 3: Slope of Mean Absolute Error](#activity-3-slope-of-mean-absolute-error)
- [Activity 4: Programming](#activity-4-programming)
- [Activity 5: Visualizing Changes in the Data](#activity-5-visualizing-changes-in-the-data)
- [Activity 6: Relative Squared Loss, Continued](#activity-6-relative-squared-loss-continued)

---

## Recap: The Modeling Recipe

In [Chapter 1.3](https://notes.eecs245.org/introduction-to-supervised-learning/absolute-loss/), we introduced the three-step modeling recipe for finding optimal model parameters, which ultimately helps us make the best possible predictions.

1.  **Choose a model.**

    

<div class="math-display">
$$
\underbrace{h(x_i) = w}_{\text{constant model}} \quad\quad \underbrace{h(x_i) = w_0 + w_1 x_i}_{\text{simple linear regression model}}
$$
</div>

2.  **Choose a loss function.**

    

<div class="math-display">
$$
\underbrace{L_{\text{sq}}(y_i, h(x_i)) = (y_i - h(x_i))^2}_{\text{squared loss}} \quad\quad \underbrace{L_{\text{abs}}(y_i, h(x_i)) = |y_i - h(x_i)|}_{\text{absolute loss}}
$$
</div>

3.  **Minimize *average loss* (also called *empirical risk*) to find optimal model parameters.**

    -   Constant model, squared loss: <span class="math-inline">\\(\displaystyle R_{\text{sq}}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - w)^2 \implies w^* = \bar{y}\\)</span>

    -   Constant model, absolute loss: <span class="math-inline">\\(\displaystyle R_{\text{abs}}(w) = \frac{1}{n} \sum_{i=1}^n |y_i - w| \implies w^* = \text{Median}(y_1, y_2, \ldots, y_n)\\)</span>

    -   Simple linear regression model, squared loss: 

<div class="math-display">
$$
\displaystyle R_{\text{sq}}(w_0, w_1) = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i))^2 \implies w_1^* = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad w_0^* = \bar{y} - w_1^* \bar{x}
$$
</div>

## Activity 1: Relative Squared Loss

Suppose we'd like to find the optimal parameter, <span class="math-inline">\\(w^*\\)</span>, for the constant model <span class="math-inline">\\(h(x_i) = w\\)</span>. To do so, we use the following loss function, called the **relative squared loss**:

<div class="math-display">
$$
L_{\text{rsq}}(y_i, h(x_i)) = \frac{(y_i - h(x_i))^2}{y_i}
$$
</div>

What value of <span class="math-inline">\\(w\\)</span> minimizes the average loss (i.e. empirical risk) when using the relative squared loss function -- that is, what is <span class="math-inline">\\(w^*\\)</span>? Your answer should only be in terms of the variables <span class="math-inline">\\(n, y_1, y_2, \ldots, y_n\\)</span>, and any constants.

---

## Activity 2: Rapid Fire

Consider a dataset of <span class="math-inline">\\(n\\)</span> **integers**, <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span>, whose histogram is given below:

![image](imgs/hist-dist.png)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^*\\)</span> that minimizes:

<div class="math-display">
$$
\frac{1}{n} \sum_{i = 1}^n
\begin{cases}
0 \quad  y_i = w \\\\
1 \quad y_i \neq w
\end{cases}
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(7\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(11\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(30\\)</span></span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^*\\)</span> that minimizes:

<div class="math-display">
$$
\frac{1}{n} \sum_{i = 1}^n |y_i - w|
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(7\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(11\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(30\\)</span></span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^*\\)</span> that minimizes:

<div class="math-display">
$$
\frac{1}{n} \sum_{i = 1}^n (y_i - w)^2
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(7\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(11\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(30\\)</span></span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
Which of the following is closest to the constant prediction <span class="math-inline">\\(w^*\\)</span> that minimizes:

<div class="math-display">
$$
\lim_{p \rightarrow \infty} \frac{1}{n} \sum_{i = 1}^n |y_i - w|^p
$$
</div>

<em>Hint: Think about the effect of outliers.</em>

<div class="mc-options"><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(7\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(11\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="math-inline">\\(\bigcirc\\)</span> <span class="math-inline">\\(30\\)</span></span></div>

</div>
</div>

</div>
---

## Activity 3: Slope of Mean Absolute Error

Consider a dataset of 8 points, <span class="math-inline">\\(y_1, y_2, \ldots, y_8\\)</span> that are in sorted order, i.e. <span class="math-inline">\\(y_1 < y_2 < \ldots < y_8\\)</span>.

Recall that mean absolute error, <span class="math-inline">\\(R_{\text{abs}}(w)\\)</span>, for the constant model <span class="math-inline">\\(h(x_i) = w\\)</span> is defined as: 

<div class="math-display">
$$
R_{\text{abs}}(w)=\frac{1}{n} \sum_{i=1}^n |y_i - w|
$$
</div>

This is a piecewise linear function that changes slope at each data point. The slope of <span class="math-inline">\\(R_{\text{abs}}(w)\\)</span> at any <span class="math-inline">\\(w\\)</span> that is not a data point is:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_{\text{abs}}(w) = \frac{\text{# left of } w - \text{# right of } w}{n}
$$
</div>

Suppose that <span class="math-inline">\\(y_4=10\\)</span>, <span class="math-inline">\\(y_5=14\\)</span>, <span class="math-inline">\\(y_6=22\\)</span>, and <span class="math-inline">\\(R_{\text{abs}}(11)=9\\)</span>. What is <span class="math-inline">\\(R_{\text{abs}}(22)\\)</span>?

<em>Hint: You don't have all 8 of the <span class="math-inline">\\(y\\)</span>-values, so you can't find <span class="math-inline">\\(R_\text{abs}(22)\\)</span> just by plugging in numbers into the formula for <span class="math-inline">\\(R_\text{abs}(w)\\)</span>. Instead, think about how to use the slope formula.</em>

---

## Activity 4: Programming

Complete the tasks in the `lab02.ipynb` notebook.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/sp26-code/tree/main/labs/lab02/lab02.ipynb), and open `labs/lab02/lab02.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Flabs%2Flab02%2Flab02.ipynb&branch=main) to open `lab02.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

Once you're done, include a screenshot of your completed Activity 4 implementation in your PDF submission of Lab 2 to Gradescope, making sure to include proof that the (local) autograder passed.

---

## Activity 5: Visualizing Changes in the Data

The problems in this final activity will help you visualize how changes in the data affect the optimal simple linear regression line. To recap, this is the line <span class="math-inline">\\(h(x_i) = w_0 + w_1 x_i\\)</span> defined by:

<div class="math-display">
$$
w_1^* = r \frac{\sigma_y}{\sigma_x} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \qquad w_0^* = \bar{y} - w_1^* \bar{x}
$$
</div>

<span class="math-inline">\\(r\\)</span> is the correlation coefficient between <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>, <span class="math-inline">\\(\sigma_x\\)</span> is the standard deviation of <span class="math-inline">\\(x\\)</span>, and <span class="math-inline">\\(\sigma_y\\)</span> is the standard deviation of <span class="math-inline">\\(y\\)</span>.

Assume all data is in the first quadrant, i.e. all <span class="math-inline">\\(x_i\\)</span> and <span class="math-inline">\\(y_i\\)</span> are positive.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
In each dataset shown below, how will the slope and intercept of the regression line change if we move the red point in the direction of the arrow?

![image](imgs/dsc-prob-6.png) ![image](imgs/dsc-prob-7.png)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Compare two different possible changes to the dataset shown below.

-   Move the dashed point down <span class="math-inline">\\(c\\)</span> units.

-   Move the solid point down <span class="math-inline">\\(c\\)</span> units.

Which move will change the slope of the regression line more? Why? *Hint: We're not looking for a formal proof. But, if you want to read more, look at [Chapter 2.3](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/#regression-line-passes-through-the-mean).*

![image](imgs/dsc-prob-10-bw-arrows.png)

**The rest of this worksheet is extra practice. Don't feel pressured to answer all of these problems in lab, but make sure to attempt them at some point.**

</div>
</div>

</div>
---

## Activity 6: Relative Squared Loss, Continued

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
Let <span class="math-inline">\\(C(y_1, y_2, ..., y_n)\\)</span> be your minimizer <span class="math-inline">\\(w^*\\)</span> from Activity 1. That is, for a particular dataset <span class="math-inline">\\(y_1, y_2, ..., y_n\\)</span>, <span class="math-inline">\\(C(y_1, y_2, ..., y_n)\\)</span> is the value of <span class="math-inline">\\(w\\)</span> that minimizes empirical risk for relative squared loss on that dataset.

What is the value of <span class="math-inline">\\(\displaystyle\lim_{y_4 \rightarrow \infty} C(1, 3, 5, y_4)\\)</span> in terms of <span class="math-inline">\\(C(1, 3, 5)\\)</span>? Your answer should involve the function <span class="math-inline">\\(C\\)</span> and/or one or more constants.

<em>Hint: To notice the pattern, evaluate <span class="math-inline">\\(C(1, 3, 5, 100)\\)</span>, <span class="math-inline">\\(C(1, 3, 5, 10000)\\)</span>, and <span class="math-inline">\\(C(1, 3, 5, 1000000)\\)</span>.</em>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
What is the value of <span class="math-inline">\\(\displaystyle\lim_{y_4 \rightarrow 0} C(1, 3, 5, y_4)\\)</span>? Again, your answer should involve the function <span class="math-inline">\\(C\\)</span> and/or one or more constants.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Based on the results of the previous two parts, when is the prediction <span class="math-inline">\\(C(y_1, y_2, ..., y_n)\\)</span> robust to outliers? When is it not robust to outliers?
</div>
</div>

</div>
