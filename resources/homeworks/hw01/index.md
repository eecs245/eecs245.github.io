---
layout: page
title: "Homework 1: Means, Sums, and Calculus"
description: "Homework 1: Means, Sums, and Calculus problems."
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

# Homework 1: Means, Sums, and Calculus

**due** Sunday, May 10th, 2026 at 11:59PM Ann Arbor Time

<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw01/hw01.pdf" target="_blank">View as PDF ✏️</a>

{: .yellow }
<div markdown="1">
Write your solutions to the following problems either by writing them on a piece of paper or on a tablet and scanning your answers as a PDF. Note that you are not allowed to use LaTeX, Google Docs, or any other digital document creation software to type your answers. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).
</div>

---

## Problems

- [Problem 1: Welcome Survey](#problem-1-welcome-survey-5-pts)
- [Problem 2: Fun with Loops](#problem-2-fun-with-loops-8-pts)
- [Problem 3: Simpson's Paradox](#problem-3-simpsons-paradox-5-pts)
- [Problem 4: The Proof is in the Pudding](#problem-4-the-proof-is-in-the-pudding-8-pts)
- [Problem 5: Mean Imputation](#problem-5-mean-imputation-6-pts)
- [Problem 6: Bias-Variance Decomposition](#problem-6-bias-variance-decomposition-8-pts)
- [Problem 7: Coin Flipping](#problem-7-coin-flipping-9-pts)

---

Total Points: 5 + 8 + 5 + 8 + 6 + 8 + 9 = 49

---

## Problem 1: Welcome Survey (5 pts)

Make sure to fill out the [Welcome Survey](https://docs.google.com/forms/d/e/1FAIpQLSee14997ZWHuI-eYwNZHh4tI6i9Xu0kRLYMm_ve9uoSxbjVgA/viewform?usp=dialog) for 5 points on the homework.

---

## Problem 2: Fun with Loops (8 pts)

This problem involves writing code and submitting it to the Gradescope autograder.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open `homeworks/hw01/hw01.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Fhomeworks%2Fhw01%2Fhw01.ipynb&branch=main) to open `hw01.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

To receive credit for the programming portion of the homework, you'll need to submit your completed notebook to the autograder on Gradescope. Your submission time for Homework 1 is the **latter** of your PDF and code submission times.

---

## Problem 3: Simpson's Paradox (5 pts)

In this problem, we'll look at an example of how "simple" data analysis is not always so simple. Consider two students, Lisa and Bart, who have completed three semesters at Michigan. **In each semester, Lisa earns a higher GPA than Bart.**

|              |          |         |          |         |
|:------------:|:--------:|:-------:|:--------:|:-------:|
| **Semester** | **Lisa** |         | **Bart** |         |
|              |   GPA    | Credits |   GPA    | Credits |
|     FA24     |   2.3    |   20    |   2.0    |    5    |
|     WN25     |   3.0    |   18    |   2.7    |    5    |
|     FA25     |   4.0    |    5    |   3.7    |   22    |

But, **Bart has a higher overall GPA**! Remember that GPA is a **weighted average**, where each course grade is weighted by the number of credits the course is worth. Lisa's overall GPA is

<div class="math-display">
$$
\text{Lisa's overall GPA} = \frac{2.3 \cdot 20 + 3.0 \cdot 18 + 4.0 \cdot 5}{20 + 18 + 5} \approx 2.79
$$
</div>

You should verify that Bart's GPA is indeed higher than Lisa's.

Why does this happen? Even though Lisa has a higher GPA in every semester, Bart takes many more credits in the semester where both of them perform well (FA25), while Lisa takes more credits in the semesters where both perform worse. This phenomenon ---- where data shows one trend overall but the opposite trend when broken down by subgroups -- is known as **Simpson's Paradox**.

In a similar vein, consider the following data on the weights of dogs in Veterinarian Kyle's care, separated by district and breed.

|              |                      |       |                     |       |
|:------------:|:--------------------:|:-----:|:-------------------:|:-----:|
|              | **Golden Retriever** |       | **German Shepherd** |       |
| **District** |     Mean Weight      | Count |     Mean Weight     | Count |
|  District 1  |          30          |   4   |         20          |   3   |
|  District 2  |          45          |   1   |         <span class="math-inline">\\(a\\)</span>         |  <span class="math-inline">\\(b\\)</span>  |

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) What is the mean weight of all Golden Retrievers in Kyle's care?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find **integers** <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that the following all hold:

-   In District 1, the mean weight of Golden Retrievers is greater than the mean weight of German Shepherds.

-   In District 2, the mean weight of Golden Retrievers is greater than the mean weight of German Shepherds.

-   Overall, the mean weight of Golden Retrievers is less than the mean weight of German Shepherds.

There are infinitely many solutions. Give a solution with the **smallest possible value of <span class="math-inline">\\(a\\)</span>**. If multiple values of <span class="math-inline">\\(b\\)</span> remain, give the smallest such value. Remember to show your work, as with every other problem in this homework.

</div>
</div>

</div>
---

## Problem 4: The Proof is in the Pudding (8 pts)

To rigorously understand the math behind machine learning, we'll need to be able to **prove** various statements. But the proofs we'll write in machine learning are of a different flavor than the proofs you'd write in a discrete math class. In this problem, we'll discuss the general approach to proving statements in this class. The problem looks long, but most of it is explaining *how* to answer it!

**Here, you'll prove or disprove various statements about a dataset of numbers, <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span>.**

To prove that a statement is always true, you must provide some sort of reason as to *why* it is always true, no matter what the values in <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span> are. For example, consider the statement:

> *Suppose we add <span class="math-inline">\\(5\\)</span> to each <span class="math-inline">\\(y_i\\)</span>. The mean of the new dataset must be greater than the mean of the original dataset.*

This statement is always true, but it's not enough just to say *"This statement is always true; since we're adding a positive number to each value, the mean will also increase."* That's good intuition to have, but we need to provide a more rigorous justification.

It's also not enough to come up with a specific example that satisfies the statement --- specific examples are an important first step to convince yourself that the statement is true, but they're not enough to prove it.

Here's what a more rigorous justification might look like:

> *The mean of the original dataset is <span class="math-inline">\\(\bar{y} = \displaystyle\frac{1}{n} \sum_{i=1}^n y_i\\)</span>. The mean of the new dataset is:* 

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n (y_i + 5) = \frac{1}{n} \left( \sum_{i=1}^n y_i + \sum_{i=1}^n 5 \right) = \frac{1}{n} \left( \sum_{i=1}^n y_i \right) + \frac{1}{n} \left( \sum_{i=1}^n 5 \right) = \bar{y} + 5
$$
</div>

 *Therefore, the mean of the new dataset is equal to the original dataset's mean plus <span class="math-inline">\\(5\\)</span>, so the mean of the new dataset is greater than the mean of the original dataset, and so the statement is always true.*

Note that in the argument above, we didn't assume anything specifically about the numbers in the original dataset --- we didn't use a specific example. Just because a statement holds true for one example, doesn't mean it always holds true!

On the other hand, to *disprove* a statement, what you need to show is that it is **not** always true. The easiest way to do this is to provide a **counterexample**, i.e. a set of values <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span> where the statement is false. For example, consider the statement:

> *The smallest number in the dataset must be less than the mean.*

Upon first glance, it may seem like this statement is true. If we consider the numbers <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(9\\)</span> (just three numbers we made up for an example), the smallest number (<span class="math-inline">\\(1\\)</span>) is indeed less than the mean (<span class="math-inline">\\(\frac{1+2+9}{3} = 4\\)</span>). But, this statement is not true in general. Valid justification might look like:

> *This statement is not always true. For example, consider the dataset <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(1\\)</span>, and <span class="math-inline">\\(1\\)</span>. The smallest number and mean are both <span class="math-inline">\\(1\\)</span>, so the smallest number is not less than the mean, so the statement is not always true.*

This is a counterexample, and is a sufficient disproof. Now, it's your turn!

Consider a dataset of numbers <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span>. For each of the following statements, either provide a proof or a counterexample to disprove the statement.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) At least half of the numbers in the dataset must be less than the mean.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose that all of the numbers in the dataset are unique. Then, removing the largest number from the dataset will increase the mean.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose that all of the numbers in the dataset are unique, that <span class="math-inline">\\(n\\)</span> is odd, and that the mean of the dataset is not equal to the median of the dataset. Then, if we remove the median value from the dataset, the median of the new dataset must be different from the median of the original dataset.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose we introduce a new number to the dataset that is greater than the mean of the existing dataset. The mean of the new dataset must be greater than the mean of the original dataset.

</div>
</div>

</div>
---

## Problem 5: Mean Imputation (6 pts)

In the real world, it's common to have missing values in a dataset --- for example, a survey may ask for a person's age, but they may not want to answer that question. One strategy for dealing with missing values is to *impute* (i.e. fill in) the missing values with the mean of the dataset. In this problem, we'll explore the implications of this strategy.

Before proceeding, you may want to review [Appendix 1](https://notes.eecs245.org/math-foundations/summation/), on summation notation and the mean.

Consider a dataset of <span class="math-inline">\\(n\\)</span> numbers <span class="math-inline">\\(y_1, y_2, \ldots, y_n\\)</span> with mean <span class="math-inline">\\(\bar{y}\\)</span> and standard deviation <span class="math-inline">\\(s\\)</span>: 

<div class="math-display">
$$
s = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2}
$$
</div>

Suppose we introduce <span class="math-inline">\\(k\\)</span> new values to the dataset, <span class="math-inline">\\(y_{n+1}, y_{n+2}, \ldots, y_{n+k}\\)</span>, all of which are equal to <span class="math-inline">\\(\bar{y}\\)</span>.

Let the new mean and standard deviation of all <span class="math-inline">\\(n + k\\)</span> values be <span class="math-inline">\\(\bar{y}'\\)</span> and <span class="math-inline">\\(s'\\)</span>, respectively.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\bar{y}'\\)</span> in terms of <span class="math-inline">\\(\bar{y}\\)</span>, <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(k\\)</span>, and <span class="math-inline">\\(s\\)</span>. You may not need to use all of these variables in your answer. Remember that simply writing a formula for <span class="math-inline">\\(\bar{y}'\\)</span> is not enough; you must show your work.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(s'\\)</span> in terms of <span class="math-inline">\\(\bar{y}\\)</span>, <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(k\\)</span>, and <span class="math-inline">\\(s\\)</span>. Again, you may not need to use all of these variables in your answer.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) In part **b)**, you should have found that the value of <span class="math-inline">\\(s'\\)</span> is less than the value of <span class="math-inline">\\(s\\)</span>. Give an intuitive explanation of *why* this is the case, as long as <span class="math-inline">\\(k > 0\\)</span>. What is the standard deviation of a dataset supposed to measure?

</div>
</div>

</div>
---

## Problem 6: Bias-Variance Decomposition (8 pts)

The main result in [Chapter 1.2](https://notes.eecs245.org/introduction-to-supervised-learning/squared-loss-constant-model/) is that <span class="math-inline">\\(w^* = \bar{y} = \operatorname{Mean}(y_1, y_2, \ldots, y_n)\\)</span> is the constant prediction that minimizes mean squared error: 

<div class="math-display">
$$
R_{\text{sq}}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - w)^2
$$
</div>

To arrive at this result, we used calculus: we took the derivative of <span class="math-inline">\\(R_{\text{sq}}(w)\\)</span> with respect to <span class="math-inline">\\(w\\)</span>, set it equal to <span class="math-inline">\\(0\\)</span>, and solved for the resulting value of <span class="math-inline">\\(w\\)</span>, which we called <span class="math-inline">\\(w^*\\)</span>.

In this problem, we'll analyze <span class="math-inline">\\(R_{\text{sq}}(w)\\)</span> in a way that doesn't use calculus. The general idea is this: if <span class="math-inline">\\(f(x) = a(x-c)^2 + k\\)</span>, then we know that <span class="math-inline">\\(f(x)\\)</span> is a quadratic function that opens upwards, with a vertex at <span class="math-inline">\\((c, k)\\)</span>. This means that <span class="math-inline">\\(f(x)\\)</span> is minimized at <span class="math-inline">\\(x = c\\)</span>.

We know from [Chapter 1.2](https://notes.eecs245.org/introduction-to-supervised-learning/squared-loss-constant-model/) that <span class="math-inline">\\(R_{\text{sq}}(w)\\)</span> is a quadratic function of <span class="math-inline">\\(w\\)</span>, so if we can write it in the form <span class="math-inline">\\(R_{\text{sq}}(w) = a(w-c)^2 + k\\)</span>, then we know that <span class="math-inline">\\(R_{\text{sq}}(w)\\)</span> is minimized at <span class="math-inline">\\(w = c\\)</span>.

Consider a dataset of numbers <span class="math-inline">\\(y_1, \ldots, y_n\\)</span> with a mean of <span class="math-inline">\\(\bar{y}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) What is the value of <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})\\)</span>? Show your work, even if the answer is familiar from [Appendix 1](https://notes.eecs245.org/math-foundations/summation/).

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Show that:

<div class="math-display">
$$
R_{\text{sq}}(w) = \frac{1}{n} \sum_{i=1}^n \left((y_i - \bar{y})^2 + 2(y_i - \bar{y})(\bar{y} - w) + (\bar{y} - w)^2\right)
$$
</div>

 Some guidance:

-   To proceed, start by rewriting <span class="math-inline">\\(y_i - w\\)</span> in the definition of <span class="math-inline">\\(R_{\text{sq}}(w)\\)</span> as <span class="math-inline">\\((y_i - \bar{y}) + (\bar{y} - w)\\)</span>. Why is this a valid step?

-   Make sure not to expand unnecessarily. Your work should only take 3-4 lines.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Using your results from the previous two parts, show that:

<div class="math-display">
$$
R_{\text{sq}}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 + (\bar{y} - w)^2
$$
</div>

 This is called the **bias-variance decomposition** of <span class="math-inline">\\(R_{\text{sq}}(w)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) Why does the result in part **c)** prove that <span class="math-inline">\\(w^* = \bar{y}\\)</span> minimizes <span class="math-inline">\\(R_{\text{sq}}(w)\\)</span>?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) In part **c)**, you showed that:

<div class="math-display">
$$
R_{\text{sq}}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 + (\bar{y} - w)^2
$$
</div>

Take a close look at the equation above, then fill in the blank below with a **single word**:

The value of <span class="math-inline">\\(R_{\text{sq}}(w^*)\\)</span>, when <span class="math-inline">\\(w^* = \bar{y}\\)</span>, is equal to the

<span class="answer-blank"></span>

of the data.

</div>
</div>

</div>
---

## Problem 7: Coin Flipping (9 pts)

In this problem, we'll plant the seeds of how probability, calculus, and machine learning are all related.

Suppose we find a coin on the ground, and we're unsure of whether the coin is fair. We decide to flip the coin repeatedly to estimate its bias, <span class="math-inline">\\(p\\)</span>, which is the probability of flipping heads on any particular flip. (The probability of flipping tails on any particular flip, then, is <span class="math-inline">\\(1 - p\\)</span>.)

Suppose we flip the coin 100 times and see 65 heads. Assuming that each flip is independent, this is a possible result, no matter what the value of <span class="math-inline">\\(p\\)</span> is, as long as <span class="math-inline">\\(0 < p < 1\\)</span>. But, some values of <span class="math-inline">\\(p\\)</span> are more believable than others.

For example, if <span class="math-inline">\\(p = 0.5\\)</span>, the probability of seeing 65 heads and 35 tails is: 

<div class="math-display">
$$
\mathbb{P}(\text{65 heads} \mid p = 0.5) = \binom{100}{65} (0.5)^{65} (0.5)^{35} \approx 0.00086
$$
</div>

 If <span class="math-inline">\\(p = 0.7\\)</span>, the probability of seeing 65 heads and 35 tails is: 

<div class="math-display">
$$
\mathbb{P}(\text{65 heads} \mid p = 0.7) = \binom{100}{65} (0.7)^{65} (0.3)^{35} \approx 0.04678
$$
</div>

The <span class="math-inline">\\(\binom{100}{65}\\)</span> term, pronounced "100 choose 65", represents the number of ways to arrange 65 heads and 35 tails in 100 flips. Don't worry if these calculations are unfamiliar, and you only have a shaky grasp of probability --- calculating probabilities is not the main point of this exercise.

**Question**: What value of <span class="math-inline">\\(p\\)</span> maximizes the probability calculation above? This is the idea we'll explore in this problem.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4 pts) First, let's phrase the problem in slightly more general terms. Suppose we flip a coin <span class="math-inline">\\(n\\)</span> times, and see <span class="math-inline">\\(k\\)</span> heads. Then, the probability of seeing <span class="math-inline">\\(k\\)</span> heads and <span class="math-inline">\\(n - k\\)</span> tails, given a bias of <span class="math-inline">\\(p\\)</span>, is:

<div class="math-display">
$$
L(p) = \binom{n}{k} p^k (1 - p)^{n - k}
$$
</div>

The letter <span class="math-inline">\\(L\\)</span> stands for "likelihood". For now, just think of <span class="math-inline">\\(L(p)\\)</span> as a function of just <span class="math-inline">\\(p\\)</span>; treat <span class="math-inline">\\(n\\)</span> and <span class="math-inline">\\(k\\)</span> as constants.

Find <span class="math-inline">\\(\frac{\text{d}L}{\text{d}p}\\)</span>, and use it to find the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span>. (You do not need to perform a second derivative test.) Feel free to refer to the [Appendix 2](https://notes.eecs245.org/math-foundations/derivatives/) for a review of derivative rules.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Computing <span class="math-inline">\\(\frac{\text{d}L}{\text{d}p}\\)</span> was quite messy. Let's investigate another approach.

A technique often used in machine learning is to take the **natural** logarithm (with base <span class="math-inline">\\(e\\)</span>) of the function we're trying to minimize. Let's test this out, and then reason about why this is a valid step.

First, some useful properties of logarithms:

<div class="math-display">
$$
\begin{align*}
\log(ab) &= \log(a) + \log(b) \\\\
\log(a^b) &= b \log(a) \\\\
\frac{\text{d} \log(x)}{\text{d}x} &= \frac{1}{x} \\\\
\frac{\text{d} \log(f(x))}{\text{d}x} &= \frac{1}{f(x)} \cdot \frac{\text{d} f}{\text{d}x} \quad \text{(by the chain rule)}
\end{align*}
$$
</div>

Show that:

<div class="math-display">
$$
\frac{\text{d} \log(L(p))}{\text{d}p} = \frac{k}{p} - \frac{n - k}{1 - p}
$$
</div>

Then, show that the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span> is the same as the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(\log(L(p))\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) You should have noticed that computing the derivative of <span class="math-inline">\\(\log(L(p))\\)</span> and solving for where it is equal to 0 was much, much easier than computing the derivative of <span class="math-inline">\\(L(p)\\)</span> and solving for where it is equal to 0. This is because the logarithm function allows us to turn products into sums, which are much easier to work with.

But why was this a valid step? Why does the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span> have to be the same as the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(\log(L(p))\\)</span>? It has to do with the graph of the logarithm function.

![image](imgs/log_plot.png)

As we see above, the function <span class="math-inline">\\(f(x) = \log(x)\\)</span> is a **strictly monotonically increasing** function. This means that if <span class="math-inline">\\(a > b\\)</span>, then <span class="math-inline">\\(\log(a) > \log(b)\\)</span>, i.e. the graph of <span class="math-inline">\\(\log(x)\\)</span> always increases as we move from left to right.

Provide a **two sentence explanation** of why the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span> is the same as the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(\log(L(p))\\)</span>. You don't need to "prove" or write any math here, as the answer was already provided to you implicitly in this problem --- we want to ensure you understand *why* the fact that <span class="math-inline">\\(\log(x)\\)</span> is strictly monotonically increasing implies that the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span> is the same as the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(\log(L(p))\\)</span>.
</div>
</div>

</div>
