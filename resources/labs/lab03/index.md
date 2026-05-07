---
layout: page
title: "Lab 3: Simple Linear Regression and Partial Derivatives"
description: "Lab 3: Simple Linear Regression and Partial Derivatives activities."
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

# Lab 3: Simple Linear Regression and Partial Derivatives

**due** for completion at 11:59PM Ann Arbor Time on Wednesday, May 13th, 2026

<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab03/lab03.pdf" target="_blank">View as PDF ✏️</a>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: The Meaning of Mean Squared Error](#activity-1-the-meaning-of-mean-squared-error)
- [Activity 2: What Do You Mean?](#activity-2-what-do-you-mean)
- [Activity 3: Reverse Regression](#activity-3-reverse-regression)
- [Activity 4: Partial Derivatives and Minimization](#activity-4-partial-derivatives-and-minimization)
- [Activity 5: Systems of Equations](#activity-5-systems-of-equations)
- [Activity 6: Transformed Data](#activity-6-transformed-data)
- [Activity 7: A Refresher](#activity-7-a-refresher)

---

## Recap: Simple Linear Regression

We've spent all of [Chapter 2](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/) learning about the simple linear regression model, <span class="math-inline">\\(h(x_i) = w_0 + w_1 x_i\\)</span>.

To find the optimal intercept, <span class="math-inline">\\(w_0^*\\)</span>, and slope, <span class="math-inline">\\(w_1^*\\)</span>, we minimized mean squared error: 

<div class="math-display">
$$
R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i=1}^{n} (y_i - (w_0 + w_1 x_i))^2
$$
</div>

-   **<span class="math-inline">\\(R_\text{sq}\\)</span> is a function of <span class="math-inline">\\(w_0\\)</span> and <span class="math-inline">\\(w_1\\)</span>, and looks like a bowl in 3D.** Since it has two input variables, we found its minimum by taking the partial derivatives of <span class="math-inline">\\(R_\text{sq}(w_0, w_1)\\)</span> with respect to <span class="math-inline">\\(w_0\\)</span> and <span class="math-inline">\\(w_1\\)</span>, setting both of them equal to 0, and then solving for the resulting <span class="math-inline">\\(w_0^*\\)</span> and <span class="math-inline">\\(w_1^*\\)</span>.

-   A partial derivative is defined as the derivative with respect to one variable **while treating all others as constants**. 

<div class="math-display">
$$
f(x, y) = x^2 + 3xy^2 \implies \frac{\partial f}{\partial x} = 2x + 3y^2
$$
</div>

-   An important fact about the line <span class="math-inline">\\(h^*(x_i)=w_0^*+w_1^*x_i\\)</span> is that it is guaranteed to pass through <span class="math-inline">\\((\bar x, \bar y)\\)</span> --- in other words, an average input always predicts an average output.

-   There are several equivalent ways to write the optimal slope, <span class="math-inline">\\(w_1^*\\)</span>. One of them involves the correlation coefficient, <span class="math-inline">\\(r\\)</span>. 

<div class="math-display">
$$
\underbrace{r = \frac{1}{n} \sum_{i=1}^n \left( \frac{x_i-\bar x}{\sigma_x} \right) \left( \frac{y_i-\bar y}{\sigma_y} \right)}_{\text{average product of <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>, once both are standardized}} \qquad w_1^* = r \frac{\sigma_y}{\sigma_x} = \frac{\sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)}{\sum_{i=1}^n (x_i-\bar x)^2}, \quad w_0^* = \bar y - w_1^* \bar x
$$
</div>

## Activity 1: The Meaning of Mean Squared Error

Suppose we'd like to predict the number of minutes a delivery will take, <span class="math-inline">\\(y\\)</span>, as a function of distance, <span class="math-inline">\\(x\\)</span>. To do so, we look to our dataset of <span class="math-inline">\\(n\\)</span> deliveries, <span class="math-inline">\\((x_1, y_1), (x_2,y_2), \dots, (x_n,y_n)\\)</span>, and fit two simple linear models:

-   <span class="math-inline">\\(F(x_i)=a_0+a_1x_i\\)</span>, where: 

<div class="math-display">
$$
a_1=r\frac{\sigma_y}{\sigma_x}, \qquad  a_0=\bar y - a_1 \bar x
$$
</div>

 Here, <span class="math-inline">\\(r\\)</span> is the correlation coefficient between <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span>, <span class="math-inline">\\(\bar x\\)</span> and <span class="math-inline">\\(\bar y\\)</span> are their respective means, and <span class="math-inline">\\(\sigma_x\\)</span> and <span class="math-inline">\\(\sigma_y\\)</span> are their respective standard deviations.

-   <span class="math-inline">\\(G(x_i)=b_0+b_1x_i\\)</span>, where <span class="math-inline">\\(b_0\\)</span> and <span class="math-inline">\\(b_1\\)</span> are chosen such that <span class="math-inline">\\(G(x_i)=b_0+b_1x_i\\)</span> minimizes **mean absolute error** on the dataset. Assume that no other line minimizes mean absolute error on the dataset, i.e. that the values of <span class="math-inline">\\(b_0\\)</span> and <span class="math-inline">\\(b_1\\)</span> are unique.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Fill in the :

<div class="math-display">
$$
\displaystyle \sum_{i=1}^{n}(y_i-F(x_i))^2  \quad \fbox{???} \quad \sum_{i=1}^{n}(y_i-G(x_i))^2
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Fill in the :

<div class="math-display">
$$
\displaystyle \left(\sum_{i=1}^{n}|y_i-F(x_i)|\right)^2  \quad \fbox{???} \quad \left(\sum_{i=1}^{n}|y_i-G(x_i)|\right)^2
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Below, we've drawn the lines for both <span class="math-inline">\\(F\\)</span> and <span class="math-inline">\\(G\\)</span> along with a scatter plot for the original <span class="math-inline">\\(n\\)</span> deliveries:

![image](imgs/regression.png)

Which line corresponds to <span class="math-inline">\\(F\\)</span>?

</div>
</div>

</div>
---

## Activity 2: What Do You Mean?

Suppose we want to fit a simple linear model (using squared loss) that predicts the number of ingredients in a product given its price. We're given that:

-   The average cost of a product in our dataset is \<span class="math-inline">\\(40, i.e. \\)</span>\bar x=40$

-   The average number of ingredients in a product in our dataset is 15, i.e. <span class="math-inline">\\(\bar y =15\\)</span>

The intercept and slope of the regression line are <span class="math-inline">\\(w_0^*=11\\)</span> and <span class="math-inline">\\(w_1^*=\frac{1}{10}\\)</span>, respectively.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose Victors' Veil (a skincare product) costs \$40 and has 11 ingredients. What is the squared loss of our model's predicted number of ingredients for Victors' Veil?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Is it possible to answer part **a)** above **just** by knowing <span class="math-inline">\\(\bar x\\)</span> and <span class="math-inline">\\(\bar y\\)</span>, i.e. **without** knowing the values of <span class="math-inline">\\(w_0^*\\)</span> and <span class="math-inline">\\(w_1^*\\)</span>? Once you select an answer, explain it to your peers.

</div>
</div>

</div>
---

## Activity 3: Reverse Regression

Suppose we have a dataset of <span class="math-inline">\\(n\\)</span> houses that were recently sold in the Ann Arbor area. For each house, we have its square footage and most recent sale price. The correlation between square footage and price is <span class="math-inline">\\(r\\)</span>.

First, we minimize mean squared error to fit a simple linear model that uses square footage to predict price. The resulting regression line has an intercept of <span class="math-inline">\\(w_0^*\\)</span> and slope of <span class="math-inline">\\(w_1^*\\)</span>. 

<div class="math-display">
$$
\text{predicted price}_i=w_0^*+w_1^* \cdot \text{square footage}_i
$$
</div>

 We're now interested in minimizing mean squared error to fit a simple linear model **that uses price to predict square footage** --- that is, we're "reversing" the <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> variables. Suppose this new regression line has an intercept of <span class="math-inline">\\(\beta_0^*\\)</span> and slope of <span class="math-inline">\\(\beta_1^*\\)</span>.

Find <span class="math-inline">\\(\beta_1^*\\)</span>. Give your answer in terms of one or more of <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(r\\)</span>, <span class="math-inline">\\(w_0^*\\)</span>, and <span class="math-inline">\\(w_1^*\\)</span>.

---

## Activity 4: Partial Derivatives and Minimization

Consider the function 

<div class="math-display">
$$
g(x_1, x_2)=100(x_2-x_1^2)^2+(1-x_1)^2
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\frac{\partial g}{\partial x_1}\\)</span> and <span class="math-inline">\\(\frac{\partial g}{\partial x_2}\\)</span>, the partial derivatives of <span class="math-inline">\\(g\\)</span> with respect to <span class="math-inline">\\(x_1\\)</span> and <span class="math-inline">\\(x_2\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find the values of <span class="math-inline">\\(x_1\\)</span> and <span class="math-inline">\\(x_2\\)</span> that minimize <span class="math-inline">\\(g\\)</span>. You do not need to use the second derivative test to verify that you've found a minimum. (In fact, "the second derivative test" for functions with multiple input variables is much more complicated, and involves linear algebra.)

</div>
</div>

</div>
---

## Activity 5: Systems of Equations

Next week, we'll start learning about vectors, and various applications of them will involve solving systems of equations. Here, you'll practice solving systems of equations with three variables.

In each of the following systems of equations, solve for <span class="math-inline">\\(x_1\\)</span>, <span class="math-inline">\\(x_2\\)</span>, and <span class="math-inline">\\(x_3\\)</span>. If you cannot find a unique solution, explain why.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<div class="math-display">
$$
\begin{align*}
-4x_1+7x_2-2x_3&=2
\\\\x_1-2x_2+x_3&=3
\\\\2x_1-3x_2+x_3&=-4
\end{align*}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<div class="math-display">
$$
\begin{align*}
x_1+2x_2-x_3&=4
\\\\2x_1+4x_2-2x_3&=8
\\\\x_1-x_2+3x_3&=1
\end{align*}
$$
</div>

**The rest of this worksheet is extra practice (taken from past exams that Suraj wrote). Don't feel pressured to answer all of these problems in lab, but make sure to attempt them at some point.**

</div>
</div>

</div>
---

## Activity 6: Transformed Data

Suppose we're given a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x_1, y_1), (x_2,y_2), \dots, (x_n,y_n)\\)</span>, where <span class="math-inline">\\(\bar x\\)</span> is the mean of <span class="math-inline">\\(x_1, x_2, \dots, x_n\\)</span> and <span class="math-inline">\\(\bar y\\)</span> is the mean of <span class="math-inline">\\(y_1, y_2, \dots, y_n\\)</span>.

Using this dataset, we create a *transformed* dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x_1', y_1'), (x_2',y_2'), \dots, (x_n',y_n')\\)</span>, where: 

<div class="math-display">
$$
x_i'=4x_i-3 \qquad y_i'=y_i+24
$$
</div>

 So the transformed dataset is of the form 

<div class="math-display">
$$
(4x_1-3, y_1+24), (4x_2-3,y_2+24), \dots, (4x_n-3,y_n+24)
$$
</div>

 We decide to fit a simple linear model <span class="math-inline">\\(h(x_i')=w_0+w_1x_i'\\)</span> on the transformed dataset using squared loss. We find that <span class="math-inline">\\(w_0^*=7\\)</span> and <span class="math-inline">\\(w_1^*=2\\)</span>, so <span class="math-inline">\\(h^*(x_i')=7+2x_i'\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
Suppose we were to fit a simple linear model through the original dataset, <span class="math-inline">\\((x_1, y_1), (x_2,y_2), \dots, (x_n,y_n)\\)</span>, again using squared loss. What would the optimal slope on the original dataset be?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Recall, the model <span class="math-inline">\\(h^*(x_i')=w_0+w_1x_i'\\)</span> was fit on the transformed dataset, <span class="math-inline">\\((x_1', y_1'), (x_2',y_2'), \dots, (x_n',y_n')\\)</span>. <span class="math-inline">\\(h^*(x_i')\\)</span> happens to pass through the point <span class="math-inline">\\((\bar x, \bar y)\\)</span>. What is the value of <span class="math-inline">\\(\bar x\\)</span>? Give your answer as an integer with no variables. *Hint: What else does <span class="math-inline">\\(h^*(x_i')\\)</span> pass through?*

</div>
</div>

</div>
---

## Activity 7: A Refresher

Consider a dataset of <span class="math-inline">\\(y_1, y_2, \dots, y_n\\)</span>, all of which are **positive**. We want to fit a constant model, <span class="math-inline">\\(h(x_i)=w\\)</span>, to the data.

Let <span class="math-inline">\\(w_p^*\\)</span> be the optimal constant prediction that minimizes average degree-<span class="math-inline">\\(p\\)</span> loss, <span class="math-inline">\\(R_p(w)\\)</span>, defined below: 

<div class="math-display">
$$
R_p(w)= \displaystyle \frac{1}{n} \sum_{i=1}^{n}|y_i-w|^p
$$
</div>

 For example, <span class="math-inline">\\(w_2^*\\)</span> is the optimal constant prediction that minimizes <span class="math-inline">\\(R_2(w)= \displaystyle \frac{1}{n} \sum_{i=1}^{n}|y_i-w|^2\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
In each of the parts below, determine the value of the quantity provided. By "the data", we are referring to <span class="math-inline">\\(y_1, y_2, \dots, y_n\\)</span>. The answer choices are as follows; **select one item in each row**.

-   The standard deviation of the data

-   The variance of the data

-   The mean of the data

-   The median of the data

-   The midrange of the data, <span class="math-inline">\\(\frac{y_\text{min} + y_\text{max}}{2}\\)</span>

-   The mode of the data

-   None of these

|         |              |     |     |     |     |     |     |     |
|--------:|:-------------|:----|:----|:----|:----|:----|:----|:----|
|         |              | A   | B   | C   | D   | E   | F   | G   |
|   <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(h_0^*\\)</span>      |     |     |     |     |     |     |     |
|  <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(h_1^*\\)</span>      |     |     |     |     |     |     |     |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(R_1(h_1^*)\\)</span> |     |     |     |     |     |     |     |
|  <span class="math-inline">\\(iv\\)</span> | <span class="math-inline">\\(h_2^*\\)</span>      |     |     |     |     |     |     |     |
|   <span class="math-inline">\\(v\\)</span> | <span class="math-inline">\\(R_2(h_2^*)\\)</span> |     |     |     |     |     |     |     |

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Now, suppose we want to find the optimal constant prediction, <span class="math-inline">\\(h_\text{U}^*\\)</span>, using the "Ulta" loss function, defined below:

<div class="math-display">
$$
L_\text{U}(y_i, w) = y_i(y_i-w)^2
$$
</div>

To find <span class="math-inline">\\(h_\text{U}^*\\)</span>, we minimize <span class="math-inline">\\(R_\text{U}(w)\\)</span>, the average Ulta loss. How does <span class="math-inline">\\(h_\text{U}^*\\)</span> compare to the mean of the data, <span class="math-inline">\\(M\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Finally, to find the optimal constant prediction, we will instead minimize **regularized** average Ulta loss, <span class="math-inline">\\(R_\lambda(w)\\)</span>, defined below:

<div class="math-display">
$$
\displaystyle R_\lambda(w) = \left(\frac{1}{n} \sum_{i=1}^{n} y_i(y_i-w)^2\right)+\lambda w^2
$$
</div>

Here, assume <span class="math-inline">\\(\lambda > 0\\)</span> is some positive constant. (We will cover regularization in more detail later in the term.)

Find <span class="math-inline">\\(w^*\\)</span>, the constant prediction that minimizes <span class="math-inline">\\(R_\lambda(w)\\)</span>. Give your answer as an expression in terms of the <span class="math-inline">\\(y_i\\)</span>'s, <span class="math-inline">\\(n\\)</span>, and/or <span class="math-inline">\\(\lambda\\)</span>.
</div>
</div>

</div>
