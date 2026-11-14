---
layout: page
title: "Homework 9: Practical Machine Learning, Eigenvalues"
description: "Homework 9: Practical Machine Learning, Eigenvalues problems."
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
.main-content img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
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

# Homework 9: Practical Machine Learning, Eigenvalues

**due** Tuesday, November 24th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw09/hw09.pdf" target="_blank">View as PDF ✏️</a>
</div>

{: .yellow }
<div markdown="1">
For Problems 2-5, write your solutions either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Include the requested screenshots in the same PDF. Submit your PDF, your Problem 1 video link, and your notebook for Problems 6 and 7 to their respective assignments on Pensive by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Midterm 2 Reflection Video](#problem-1-midterm-2-reflection-video-15-pts)
- [Problem 2: Eigenvector Fundamentals](#problem-2-eigenvector-fundamentals-15-pts)
- [Problem 3: Jensen's Inequality](#problem-3-jensens-inequality-15-pts)
- [Problem 4: Home Run!](#problem-4-home-run-14-pts)
- [Problem 5: Polynomial Regression](#problem-5-polynomial-regression-14-pts)
- [Problem 6: One Hot Encoding in sklearn](#problem-6-one-hot-encoding-in-sklearn-13-pts)
- [Problem 7: Implementing Gradient Descent](#problem-7-implementing-gradient-descent-14-pts)

---

Total Points: 15 + 15 + 15 + 14 + 14 + 13 + 14 = 100

---

## Problem 1: Midterm 2 Reflection Video (15 pts)

Record a **2-5 minute video** responding to the following prompt:

> Think of one specific topic you struggled with while studying for Midterm 2. What did you do to make sense of it, and how did it go on the exam? If you were studying for Midterm 2 again, what would you do differently?

The video should be **just you speaking into the camera**. Your face must be visible while you are talking for the entire video. Do not include slides, a screen recording, written work, or any other visuals.

Submit your video link to the separate assignment on Pensive called **Homework 9, Problem 1 Video Link**. You can upload your video to YouTube as unlisted, share a Zoom recording link, or share a Google Drive link; whatever works. Make sure the course staff can view the video using that link.

Your submission time for Homework 9 is the latest of your three submission times: your Problem 1 video link, your PDF, and your notebook.

**This problem is graded on completion.** Record a video of the required length and make an honest effort to explain the question, and you will receive full credit. Your explanation does not need to be polished or perfect.

---

## Problem 2: Eigenvector Fundamentals (15 pts)

For each <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(A\\)</span> below:

<ol class="assignment-list" markdown="1" data-item-count="3" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Find the characteristic polynomial of <span class="math-inline">\\(A\\)</span>, and use it to find the eigenvalues of <span class="math-inline">\\(A\\)</span>.

</li>
<li markdown="1" value="2">

Find one eigenvector for each eigenvalue of <span class="math-inline">\\(A\\)</span>. Verify that each eigenvector is indeed an eigenvector of <span class="math-inline">\\(A\\)</span> by multiplying it by <span class="math-inline">\\(A\\)</span>.

</li>
<li markdown="1" value="3">

**By hand (not using Python or Desmos)**, draw a picture (like the one in Chapter 9.1 titled [Visualizing the eigenvectors of <span class="math-inline">\\(A\\)</span>](https://notes.eecs245.org/eigenvalues-and-eigenvectors/eigenvalues-eigenvectors/#a-first-example)) with vectors <span class="math-inline">\\(\vec v&#95;1, A \vec v&#95;1, \vec v&#95;2, A \vec v&#95;2\\)</span> as arrows (where <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> are the eigenvectors you found above).

</li>
</ol>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 4 \\\\ 4 &amp; 3 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 1 \\\\ -2 &amp; 8 \end{bmatrix}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts)
<span class="math-inline">\\(A = \begin{bmatrix} 3 &amp; 0 \\\\ 0 &amp; 4 \end{bmatrix}\\)</span>

</div>
</div>

</div>

---

## Problem 3: Jensen's Inequality (15 pts)

As we've seen several times, the variance of a dataset <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> is defined

<div class="math-display">
$$
\sigma_x^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2
$$
</div>

 where <span class="math-inline">\\(\bar{x} = \text{Mean}(x&#95;1, x&#95;2, ..., x&#95;n)\\)</span>. By expanding the summation (as we've done in several homework problems), we find that

<div class="math-display">
$$
\sigma_x^2 = \frac{1}{n} \sum_{i = 1}^n x_i^2 - \bar{x}^2
$$
</div>

 Another way of expressing this equation is

<div class="math-display">
$$
\sigma_x^2 = \text{Mean}(x_1^2, ..., x_n^2) - (\text{Mean}(x_1, ..., x_n))^2
$$
</div>

 Since <span class="math-inline">\\(\sigma&#95;x^2 \geq 0\\)</span>, this implies that

<div class="math-display">
$$
\text{Mean}(x_1^2, ..., x_n^2) - (\text{Mean}(x_1, ..., x_n))^2 \ge 0
\implies
\text{Mean}(x_1^2, ..., x_n^2) \geq (\text{Mean}(x_1, ..., x_n))^2
$$
</div>

 The inequality on the last line can be expressed more generally as

<div class="math-display">
$$
\boxed{\text{Mean}(g(x_1), g(x_2), ..., g(x_n)) \ge g(\text{Mean}(x_1, ..., x_n))}
$$
</div>

 The inequality above holds for all **convex functions** <span class="math-inline">\\(g(x)\\)</span> and is known as Jensen's inequality, named after [Johan Jensen](https://en.wikipedia.org/wiki/Johan_Jensen_%28mathematician%29) (not the former CEO of NVIDIA). Let's see how we can use Jensen's inequality to prove something useful!

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Using the second derivative test for convexity, prove that <span class="math-inline">\\(g(x) = -\log(x)\\)</span> is convex across its entire domain, <span class="math-inline">\\((0, \infty)\\)</span>. (It would be difficult to prove this using the formal definition of convexity.)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Using Jensen's inequality with <span class="math-inline">\\(g(x) = -\log(x)\\)</span>, prove that, for any dataset of positive numbers <span class="math-inline">\\(x&#95;1,x&#95;2,...,x&#95;n\\)</span>,

<div class="math-display">
$$
\frac{x_1 + x_2 + ... + x_n}{n} \geq (x_1 \cdot x_2 \cdot ... \cdot x_n)^{1/n}
$$
</div>

The quantity on the left is the familiar arithmetic mean (AM), while the quantity on the right is known as the geometric mean (GM) of <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span>. The entire inequality above is known as the "AM-GM inequality".

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(7 pts) Using Jensen's inequality with **some** convex function <span class="math-inline">\\(g(x)\\)</span>, prove that the arithmetic mean is greater than or equal to the harmonic mean for any dataset of positive numbers <span class="math-inline">\\(x&#95;1,x&#95;2,...,x&#95;n\\)</span>, i.e.

<div class="math-display">
$$
\frac{x_1 + x_2 + ... + x_n}{n} \geq \frac{n}{\frac{1}{x_1} + \frac{1}{x_2} + ... + \frac{1}{x_n}}
$$
</div>

Note that you must prove your choice of function <span class="math-inline">\\(g(x)\\)</span> is convex (using the second derivative test for convexity)!

<em>Hint: You can use a function that is only convex on an interval, as long as the only inputs you pass into that function are some from that interval.</em>

</div>
</div>

</div>

---

## Problem 4: Home Run! (14 pts)

In this problem, we'll work with a real dataset that describes the number of home runs in the MLB per year. Our goal will be to fit various models that predict the number of home runs, <span class="math-inline">\\(y&#95;i\\)</span>, given the year, <span class="math-inline">\\(x&#95;i\\)</span>.

Open the **supplemental Jupyter Notebook** we've created for Homework 9, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw09%2Fhw09.ipynb&branch=main) on DataHub, or by opening `homeworks/hw09/hw09.ipynb` in our [course repository](https://github.com/eecs245/fa26-code/tree/main).

**Note: Many problems in this homework refer to this notebook. For Problems 4 and 5, include the requested work in your PDF. For Problems 6 and 7, submit your completed notebook to the autograder on Pensive.**

In parts **a)** through **c)**, you are given a model. For each one:

<ol class="assignment-list" markdown="1" data-item-count="2" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Implement the necessary data transformations and use `sklearn`'s `LinearRegression` class to fit the model.

</li>
<li markdown="1" value="2">

**In your PDF**, include screenshots of your code and a scatter plot of your model's predictions. Write the formula for <span class="math-inline">\\(h(x&#95;i)\\)</span>, the *root* mean squared error, and the <span class="math-inline">\\(R^2\\)</span> score.

</li>
</ol>

Root mean squared error is the square root of mean squared error; its values are in the same units as <span class="math-inline">\\(y\\)</span>. The <span class="math-inline">\\(R^2\\)</span> score of a model's predictions is equal to <span class="math-inline">\\(\text{correlation}(\text{actual y values}, \text{predicted y values})^2\\)</span>.

There are helper functions in the supplemental Jupyter Notebook to help you with all steps; start by understanding how they work. Part **a)** has been done for you as an example.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i + w&#95;2 x&#95;i^2\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts)
<span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i + w&#95;2 x&#95;i^2 + w&#95;3 x&#95;i^3 + w&#95;4 x&#95;i^4\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts)
<span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i + w&#95;2 (x&#95;i - 1900) \cos\left(\frac{2 \pi}{25} x&#95;i \right) + w&#95;3 e^{\frac{x&#95;i - 1900}{100}}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) Explain why we can't use linear regression to fit the model

<span class="math-inline">\\(h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i + w&#95;2 (x&#95;i - 1900) \cos (w&#95;3 x&#95;i) + w&#95;4 e^{\frac{x&#95;i - 1900}{w&#95;5}}\\)</span>.

</div>
</div>

</div>

---

## Problem 5: Polynomial Regression (14 pts)

In this problem, we'll explore the implications of adding more and more complex features to a model.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> is an observation vector, <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times (d+1)\\)</span> design matrix, and <span class="math-inline">\\(X'\\)</span> is an <span class="math-inline">\\(n \times (d+2)\\)</span> design matrix whose first <span class="math-inline">\\(d+1\\)</span> columns are identical to <span class="math-inline">\\(X\\)</span>'s and whose last column contains some other new information.

<div class="math-display">
$$
X' = \begin{bmatrix} & | \\\\ X & \vec x^{(d+1)} \\\\ & | \end{bmatrix}
$$
</div>

These design matrices correspond to models <span class="math-inline">\\(h(\vec x&#95;i)\\)</span> and <span class="math-inline">\\(h'(\vec x&#95;i)\\)</span>, in which <span class="math-inline">\\(h'(\vec x&#95;i)\\)</span> includes one additional feature. (The <span class="math-inline">\\('\\)</span> is not a derivative.)

Let <span class="math-inline">\\(\vec w^{\ast} \in \mathbb{R}^{d+1}\\)</span> be a minimizer of <span class="math-inline">\\(\frac{1}{n} \lVert \vec y - X \vec w \rVert^2\\)</span> and <span class="math-inline">\\(\vec w' \in \mathbb{R}^{d+2}\\)</span> be a minimizer of <span class="math-inline">\\(\frac{1}{n} \lVert \vec y - X' \vec w \rVert^2\\)</span>. In general, the components of <span class="math-inline">\\(\vec w^{\ast}\\)</span> and <span class="math-inline">\\(\vec w'\\)</span> have no direct relationship; adding a new feature can change the optimal parameters for all of the existing features.

Explain why

<div class="math-display">
$$
\frac{1}{n} \lVert \vec y - X' \vec w' \rVert^2 \leq \frac{1}{n} \lVert \vec y - X \vec w^* \rVert^2
$$
</div>

The inequality above is equivalent to the statement "adding a feature never increases the mean squared error of the model's predictions on the data it was trained on".

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) In the previous part, we had you think about how adding a new feature impacts the model's **training** mean squared error, i.e. its performance on the <span class="math-inline">\\(n\\)</span> data points it was trained on. But, adding new features can hurt a model's performance on unseen data, often called **test** data, which is ultimately the performance we care about. So, to assess a model's ability to **generalize** to unseen data, we typically split our data into a training set and test set, fit the model on just the training set, and then evaluate its performance on the test set.

<div style="text-align: center;">
<img src="imgs/train-test-first.png" alt="image" style="width: 50%; max-width: 100%;">
</div>

Here's the general idea we'll explore. Suppose we want to fit a polynomial regression model of degree <span class="math-inline">\\(d\\)</span>, i.e. a model of the form

<div class="math-display">
$$
h(x_i) = w_0 + w_1 x_i + w_2 x_i^2 + ... + w_d x_i^d
$$
</div>

where <span class="math-inline">\\(x&#95;i\\)</span> is a scalar. The question is, what value of <span class="math-inline">\\(d\\)</span> should we choose? As <span class="math-inline">\\(d\\)</span> increases, the model's training mean squared error will stay the same or decrease. But, its test mean squared error may increase.

Open the **supplemental Jupyter Notebook** we've created for Homework 9, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw09%2Fhw09.ipynb&branch=main) on DataHub, or by opening `homeworks/hw09/hw09.ipynb` in our [course repository](https://github.com/eecs245/fa26-code/tree/main).

In that notebook, we provide you with code that implements a train-test split, and code that uses `sklearn`'s `Pipeline` and `PolynomialFeatures` classes to quickly fit polynomial regression models of varying degrees.

Your job is to use that code to:

<ol class="assignment-list" markdown="1" data-item-count="4" start="1" style="list-style-type: decimal;">
<li markdown="1" value="1">

Fit 25 polynomial regression models on the training set (degree 1, degree 2, \..., degree 25).

</li>
<li markdown="1" value="2">

For each model, compute both its training and test mean squared error.

</li>
<li markdown="1" value="3">

Create a line plot of the training and test mean squared error vs. degree.

</li>
<li markdown="1" value="4">

**In your PDF**, include screenshots of your code and the resulting plot.

</li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) You'll have noticed that the choice of <span class="math-inline">\\(d\\)</span> (degree) with the smallest **test** mean squared error is a relatively small number. (There will be a few values of <span class="math-inline">\\(d\\)</span> with very similar test mean squared errors, but hover over your plot: there is a unique minimum.)

In 1-3 English sentences, explain **why** adding more and more features (i.e. increasing <span class="math-inline">\\(d\\)</span>) leads to worse model performance on the test set, and what lesson we can take from this in the context of building (not necessarily just polynomial) regression models that generalize to unseen data.

If you'd like to learn more about the core ideas explored in this problem, consult [EECS 398: Practical Data Science](https://practicaldsc.org/).

</div>
</div>

</div>

---

## Problem 6: One Hot Encoding in sklearn (13 pts)

In this problem, you'll learn how to use one hot encoding directly in sklearn, as part of a larger modeling pipeline that implements both feature engineering and model training steps. Specifically, you'll implement a regression pipeline that predicts housing prices.

Open the **supplemental Jupyter Notebook** we've created for Homework 9, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw09%2Fhw09.ipynb&branch=main) on DataHub, or by opening `homeworks/hw09/hw09.ipynb` in our [course repository](https://github.com/eecs245/fa26-code/tree/main).

**This problem is entirely autograded.** Complete both in the notebook and submit it once under **Homework 9, Problems 6 and 7 Code** on Pensive.

---

## Problem 7: Implementing Gradient Descent (14 pts)

In this problem, you'll manually implement gradient descent to fit a line using a custom loss function.

Open the **supplemental Jupyter Notebook** we've created for Homework 9, which can either be found [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Ffa26-code&urlpath=tree%2Ffa26-code%2Fhomeworks%2Fhw09%2Fhw09.ipynb&branch=main) on DataHub, or by opening `homeworks/hw09/hw09.ipynb` in our [course repository](https://github.com/eecs245/fa26-code/tree/main).

**This problem is entirely autograded.** Complete both in the notebook and submit it once under **Homework 9, Problems 6 and 7 Code** on Pensive.

{% endraw %}
