---
layout: page
title: "Homework 1: Means, Sums, and Calculus"
description: "Homework 1: Means, Sums, and Calculus problems."
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

# Homework 1: Means, Sums, and Calculus

**due** Sunday, May 10th, 2026 at 11:59PM Ann Arbor Time

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw01/hw01.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/homeworks/hw01/hw01-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

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

| **Semester** | **Lisa** |         | **Bart** |         |
|:------------:|:--------:|:-------:|:--------:|:-------:|
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

|              | **Golden Retriever** |       | **German Shepherd** |       |
|:------------:|:--------------------:|:-----:|:-------------------:|:-----:|
| **District** |     Mean Weight      | Count |     Mean Weight     | Count |
|  District 1  |          30          |   4   |         20          |   3   |
|  District 2  |          45          |   1   |         <span class="math-inline">\\(a\\)</span>         |  <span class="math-inline">\\(b\\)</span>  |

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) What is the mean weight of all Golden Retrievers in Kyle's care?

<details markdown="1"><summary>Solution</summary>

Since the data is grouped, we compute a weighted average:

<div class="math-display">
$$
\begin{align*}
\frac{30 \cdot 4 + 45 \cdot 1}{4 + 1}
&= \frac{165}{5}
= \boxed{33}
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

The first condition already holds since <span class="math-inline">\\(30 &gt; 20\\)</span>.

For District 2, we require 

<div class="math-display">
$$
45 > a
$$
</div>

From part (a), the overall mean weight of Golden Retrievers is <span class="math-inline">\\(33\\)</span>. Since the German Shepherd mean in District 1 is below <span class="math-inline">\\(33\\)</span>, the mean in District 2 must exceed <span class="math-inline">\\(33\\)</span> to raise the overall average above <span class="math-inline">\\(33\\)</span>.

The smallest integer satisfying this is 

<div class="math-display">
$$
a = 34
$$
</div>

The overall mean weight of German Shepherds is then 

<div class="math-display">
$$
\frac{20 \cdot 3 + 34b}{3 + b}
$$
</div>

We require this quantity to be greater than <span class="math-inline">\\(33\\)</span>:

<div class="math-display">
$$
\begin{align*}
\frac{60 + 34b}{3 + b} &> 33 \\\\
60 + 34b &> 99 + 33b \\\\
b &> 39
\end{align*}
$$
</div>

The smallest integer satisfying this inequality is <span class="math-inline">\\(b = 40\\)</span>, so 

<div class="math-display">
$$
\boxed{a = 34 \quad b = 40}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 4: The Proof is in the Pudding (8 pts)

To rigorously understand the math behind machine learning, we'll need to be able to **prove** various statements. But the proofs we'll write in machine learning are of a different flavor than the proofs you'd write in a discrete math class. In this problem, we'll discuss the general approach to proving statements in this class. The problem looks long, but most of it is explaining *how* to answer it!

**Here, you'll prove or disprove various statements about a dataset of numbers, <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>.**

To prove that a statement is always true, you must provide some sort of reason as to *why* it is always true, no matter what the values in <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> are. For example, consider the statement:

> *Suppose we add <span class="math-inline">\\(5\\)</span> to each <span class="math-inline">\\(y&#95;i\\)</span>. The mean of the new dataset must be greater than the mean of the original dataset.*

This statement is always true, but it's not enough just to say *"This statement is always true; since we're adding a positive number to each value, the mean will also increase."* That's good intuition to have, but we need to provide a more rigorous justification.

It's also not enough to come up with a specific example that satisfies the statement --- specific examples are an important first step to convince yourself that the statement is true, but they're not enough to prove it.

Here's what a more rigorous justification might look like:

> *The mean of the original dataset is <span class="math-inline">\\(\bar{y} = \displaystyle\frac{1}{n} \sum&#95;{i=1}^n y&#95;i\\)</span>. The mean of the new dataset is:* 

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n (y_i + 5) = \frac{1}{n} \left( \sum_{i=1}^n y_i + \sum_{i=1}^n 5 \right) = \frac{1}{n} \left( \sum_{i=1}^n y_i \right) + \frac{1}{n} \left( \sum_{i=1}^n 5 \right) = \bar{y} + 5
$$
</div>

 *Therefore, the mean of the new dataset is equal to the original dataset's mean plus <span class="math-inline">\\(5\\)</span>, so the mean of the new dataset is greater than the mean of the original dataset, and so the statement is always true.*

Note that in the argument above, we didn't assume anything specifically about the numbers in the original dataset --- we didn't use a specific example. Just because a statement holds true for one example, doesn't mean it always holds true!

On the other hand, to *disprove* a statement, what you need to show is that it is **not** always true. The easiest way to do this is to provide a **counterexample**, i.e. a set of values <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> where the statement is false. For example, consider the statement:

> *The smallest number in the dataset must be less than the mean.*

Upon first glance, it may seem like this statement is true. If we consider the numbers <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(9\\)</span> (just three numbers we made up for an example), the smallest number (<span class="math-inline">\\(1\\)</span>) is indeed less than the mean (<span class="math-inline">\\(\frac{1+2+9}{3} = 4\\)</span>). But, this statement is not true in general. Valid justification might look like:

> *This statement is not always true. For example, consider the dataset <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(1\\)</span>, and <span class="math-inline">\\(1\\)</span>. The smallest number and mean are both <span class="math-inline">\\(1\\)</span>, so the smallest number is not less than the mean, so the statement is not always true.*

This is a counterexample, and is a sufficient disproof. Now, it's your turn!

Consider a dataset of numbers <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>. For each of the following statements, either provide a proof or a counterexample to disprove the statement.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) At least half of the numbers in the dataset must be less than the mean.

<details markdown="1"><summary>Solution</summary>

False. Consider the dataset <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(1\\)</span>, and <span class="math-inline">\\(1\\)</span>. The mean is <span class="math-inline">\\(1\\)</span>, and none of the numbers in the dataset are less than it, so it does not have to be the case that at least half of the numbers in the dataset are less than the mean.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose that all of the numbers in the dataset are unique. Then, removing the largest number from the dataset will increase the mean.

<details markdown="1"><summary>Solution</summary>

False. Consider the dataset <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(3\\)</span>. The mean is <span class="math-inline">\\(2\\)</span>. If we remove the largest number, <span class="math-inline">\\(3\\)</span>, the mean becomes <span class="math-inline">\\(1.5\\)</span>, which is less than <span class="math-inline">\\(2\\)</span>, the original mean, so it does not have to be true in general that removing the largest number from the dataset will increase the mean.

This statement was designed to sound tricky, but if you pay close attention to the wording, you'll see that it's almost nonsensical --- removing the largest number should decrease the mean, intuitively, not increase it.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose that all of the numbers in the dataset are unique, that <span class="math-inline">\\(n\\)</span> is odd, and that the mean of the dataset is not equal to the median of the dataset. Then, if we remove the median value from the dataset, the median of the new dataset must be different from the median of the original dataset.

<details markdown="1"><summary>Solution</summary>

False. Consider the dataset <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(3\\)</span>, <span class="math-inline">\\(5\\)</span>, <span class="math-inline">\\(7\\)</span> <span class="math-inline">\\(10\\)</span>. The median is <span class="math-inline">\\(5\\)</span>, and the mean is <span class="math-inline">\\(\frac{26}{5}\\)</span>. If we remove the median, the median becomes <span class="math-inline">\\(\frac{(3+7)}{2}\\)</span>, which is still 5.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Suppose we introduce a new number to the dataset that is greater than the mean of the existing dataset. The mean of the new dataset must be greater than the mean of the original dataset.

<details markdown="1"><summary>Solution</summary>

True. Let <span class="math-inline">\\(\bar{y}\\)</span> be the mean of the existing dataset, <span class="math-inline">\\(\bar{y}&#39;\\)</span> be the mean of the new dataset, and <span class="math-inline">\\(y&#95;{n+1}=\bar{y}+c\\)</span> where <span class="math-inline">\\(c&gt;0\\)</span>.

<div class="math-display">
$$
\begin{align*}
\bar{y}' &= \frac{1}{n+1} \sum_{i = 1}^{n + 1} y_i \\\\
&= \frac{1}{n+1} \left( \sum_{i = 1}^{n} y_i + y_{n+1}\right) \\\\
&= \frac{1}{n+1} \left( \bar{y} \cdot n + y_{n+1} \right) \\\\
&= \frac{1}{n+1} \left( \bar{y} \cdot n + \bar{y}+c \right) \\\\
&= \frac{1}{n+1} \left( \bar{y}(n+1) + c \right) \\\\
&= \frac{1}{n+1} \left( \bar{y}(n+1) + c \right) \\\\
&= \frac{\bar{y}(n+1)}{n+1} + \frac{c}{n+1} \\\\
&= \bar{y} + \frac{c}{n+1}
\end{align*}
$$
</div>

Since <span class="math-inline">\\(c&gt;0\\)</span>, our new mean is greater than the old mean.

</details>

</div>
</div>

</div>

---

## Problem 5: Mean Imputation (6 pts)

In the real world, it's common to have missing values in a dataset --- for example, a survey may ask for a person's age, but they may not want to answer that question. One strategy for dealing with missing values is to *impute* (i.e. fill in) the missing values with the mean of the dataset. In this problem, we'll explore the implications of this strategy.

Before proceeding, you may want to review [Appendix 1](https://notes.eecs245.org/math-foundations/summation/), on summation notation and the mean.

Consider a dataset of <span class="math-inline">\\(n\\)</span> numbers <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> with mean <span class="math-inline">\\(\bar{y}\\)</span> and standard deviation <span class="math-inline">\\(s\\)</span>: 

<div class="math-display">
$$
s = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2}
$$
</div>

Suppose we introduce <span class="math-inline">\\(k\\)</span> new values to the dataset, <span class="math-inline">\\(y&#95;{n+1}, y&#95;{n+2}, \ldots, y&#95;{n+k}\\)</span>, all of which are equal to <span class="math-inline">\\(\bar{y}\\)</span>.

Let the new mean and standard deviation of all <span class="math-inline">\\(n + k\\)</span> values be <span class="math-inline">\\(\bar{y}&#39;\\)</span> and <span class="math-inline">\\(s&#39;\\)</span>, respectively.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) Find <span class="math-inline">\\(\bar{y}&#39;\\)</span> in terms of <span class="math-inline">\\(\bar{y}\\)</span>, <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(k\\)</span>, and <span class="math-inline">\\(s\\)</span>. You may not need to use all of these variables in your answer. Remember that simply writing a formula for <span class="math-inline">\\(\bar{y}&#39;\\)</span> is not enough; you must show your work.

<details markdown="1"><summary>Solution</summary>

To proceed, we'll start by finding the sum of the existing <span class="math-inline">\\(n\\)</span> values. We can then use this to find the new mean, which will be the sum of the existing <span class="math-inline">\\(n\\)</span> values plus the sum of the <span class="math-inline">\\(k\\)</span> new values, all divided by <span class="math-inline">\\(n + k\\)</span>.

<div class="math-display">
$$
\frac{1}{n}\sum_{i=1}^n y_i = \bar{y} \implies \sum_{i=1}^ny_i = \bar{y}\cdot n
$$
</div>

So, the new mean, <span class="math-inline">\\(\bar{y}&#39; = \frac{1}{n + k} \sum&#95;{i = 1}^{n + k} y&#95;i\\)</span>, is:

<div class="math-display">
$$
\begin{align*}
\bar{y}' &= \frac{1}{n+k} \sum_{i = 1}^{n + k} y_i \\\\
&= \frac{1}{n+k} \left( \sum_{i = 1}^n y_i + \sum_{i = n+1}^{n+k} y_i \right) \:\:\:\: \text{(separating the sum)} \\\\
&= \frac{1}{n+k} \left( \bar{y} \cdot n + \sum_{i = n+1}^{n+k} y_i \right) \:\:\:\: \text{(using the fact that the old sum is $\bar{y} \cdot n$ from above)} \\\\
&= \frac{1}{n+k} \left( \bar{y} \cdot n + \sum_{i = n+1}^{n+k} \bar{y} \right) \:\:\:\: \text{(using the fact that all $k$ of the new values are equal to $\bar{y}$)} \\\\
&= \frac{1}{n+k} \left( \bar{y} \cdot n + \bar{y} \cdot k \right) \\\\
&= \frac{1}{n+k} \bar{y}(n + k) \\\\
&= \bar{y}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3 pts) Find <span class="math-inline">\\(s&#39;\\)</span> in terms of <span class="math-inline">\\(\bar{y}\\)</span>, <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(k\\)</span>, and <span class="math-inline">\\(s\\)</span>. Again, you may not need to use all of these variables in your answer.

<details markdown="1"><summary>Solution</summary>

In part **a)**, we showed that the new mean, <span class="math-inline">\\(\bar{y}&#39;\\)</span>, is equal to the old mean, <span class="math-inline">\\(\bar{y}\\)</span>. The old standard deviation, <span class="math-inline">\\(s\\)</span>, is:

<div class="math-display">
$$
s = \sqrt{\frac{\sum_{i = 1}^n (y_i - \bar{y})^2}{n}}
$$
</div>

Similar to in part **a)**, it'll help to express the summation <span class="math-inline">\\(\sum&#95;{i = 1}^n (y&#95;i - \bar{y})^2\\)</span> in terms of <span class="math-inline">\\(s\\)</span> and <span class="math-inline">\\(n\\)</span>:

<div class="math-display">
$$
\begin{align*}
s &= \sqrt{\frac{\sum_{i = 1}^n (y_i - \bar{y})^2}{n}} \\\\
s^2 &= \frac{\sum_{i = 1}^n (y_i - \bar{y})^2}{n} \\\\
ns^2 &= \sum_{i = 1}^n (y_i - \bar{y})^2
\end{align*}
$$
</div>

With this in mind, let's try and solve for <span class="math-inline">\\(s&#39;\\)</span>. Note that we will use the same mean, <span class="math-inline">\\(\bar{y}\\)</span>, as we did in the first part, since the mean of the first <span class="math-inline">\\(n\\)</span> values is the same as the mean of all <span class="math-inline">\\(n+k\\)</span> values. Here we go!

<div class="math-display">
$$
\begin{align*}
s' &= \sqrt{\frac{\sum_{i = 1}^{n+k} (y_i - \bar{y})^2}{n+k}} \\\\
&= \sqrt{\frac{\sum_{i = 1}^{n} (y_i - \bar{y})^2 + \sum_{i = n+1}^{n+k} (y_i - \bar{y})^2}{n+k}} \:\:\:\: \text{(separating the sum)} \\\\
&= \sqrt{\frac{ns^2 + \sum_{i = n+1}^{n+k} (y_i - \bar{y})^2}{n+k}} \:\:\:\: \text{(substituting $ns^2$ for $\sum_{i = 1}^{n} (y_i - \bar{y})^2$ from above)} \\\\
&= \sqrt{\frac{ns^2 + \sum_{i = n+1}^{n+k} (\bar{y} - \bar{y})^2}{n+k}} \:\:\:\: \text{(using the fact that all $k$ of the new values are equal to $\bar{y}$)} \\\\
&= \sqrt{\frac{ns^2 + \sum_{i = n+1}^{n+k} 0}{n+k}} \\\\
&= \sqrt{\frac{ns^2}{n+k}} \\\\
&= s\sqrt{\frac{n}{n+k}} \\\\
\end{align*}
$$
</div>

So, the new standard deviation <span class="math-inline">\\(s&#39;\\)</span> is equal to <span class="math-inline">\\(\boxed{s \sqrt{\frac{n}{n+k}}}\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) In part **b)**, you should have found that the value of <span class="math-inline">\\(s&#39;\\)</span> is less than the value of <span class="math-inline">\\(s\\)</span>. Give an intuitive explanation of *why* this is the case, as long as <span class="math-inline">\\(k &gt; 0\\)</span>. What is the standard deviation of a dataset supposed to measure?

<details markdown="1"><summary>Solution</summary>

The standard deviation is a rough measure of how far values are from the mean across the dataset. If <span class="math-inline">\\(k&gt;0\\)</span>, then we're adding extra values equal to the mean to our dataset, which decreases the standard deviation.

</details>

</div>
</div>

</div>

---

## Problem 6: Bias-Variance Decomposition (8 pts)

The main result in [Chapter 1.2](https://notes.eecs245.org/introduction-to-supervised-learning/squared-loss-constant-model/) is that <span class="math-inline">\\(w^&#42; = \bar{y} = \operatorname{Mean}(y&#95;1, y&#95;2, \ldots, y&#95;n)\\)</span> is the constant prediction that minimizes mean squared error: 

<div class="math-display">
$$
R_{\text{sq}}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - w)^2
$$
</div>

To arrive at this result, we used calculus: we took the derivative of <span class="math-inline">\\(R&#95;{\text{sq}}(w)\\)</span> with respect to <span class="math-inline">\\(w\\)</span>, set it equal to <span class="math-inline">\\(0\\)</span>, and solved for the resulting value of <span class="math-inline">\\(w\\)</span>, which we called <span class="math-inline">\\(w^&#42;\\)</span>.

In this problem, we'll analyze <span class="math-inline">\\(R&#95;{\text{sq}}(w)\\)</span> in a way that doesn't use calculus. The general idea is this: if <span class="math-inline">\\(f(x) = a(x-c)^2 + k\\)</span>, then we know that <span class="math-inline">\\(f(x)\\)</span> is a quadratic function that opens upwards, with a vertex at <span class="math-inline">\\((c, k)\\)</span>. This means that <span class="math-inline">\\(f(x)\\)</span> is minimized at <span class="math-inline">\\(x = c\\)</span>.

We know from [Chapter 1.2](https://notes.eecs245.org/introduction-to-supervised-learning/squared-loss-constant-model/) that <span class="math-inline">\\(R&#95;{\text{sq}}(w)\\)</span> is a quadratic function of <span class="math-inline">\\(w\\)</span>, so if we can write it in the form <span class="math-inline">\\(R&#95;{\text{sq}}(w) = a(w-c)^2 + k\\)</span>, then we know that <span class="math-inline">\\(R&#95;{\text{sq}}(w)\\)</span> is minimized at <span class="math-inline">\\(w = c\\)</span>.

Consider a dataset of numbers <span class="math-inline">\\(y&#95;1, \ldots, y&#95;n\\)</span> with a mean of <span class="math-inline">\\(\bar{y}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) What is the value of <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - \bar{y})\\)</span>? Show your work, even if the answer is familiar from [Appendix 1](https://notes.eecs245.org/math-foundations/summation/).

<details markdown="1"><summary>Solution</summary>

To proceed, we'll use the fact that <span class="math-inline">\\(\bar{y}\\)</span>, by definition, is <span class="math-inline">\\(\bar{y} = \frac{1}{n} \sum&#95;{i = 1}^n y&#95;i\\)</span>, meaning that <span class="math-inline">\\(\sum&#95;{i = 1}^n y&#95;i = n \bar{y}\\)</span>.

<div class="math-display">
$$
\begin{align*}
\frac{1}{n}\sum_{i = 1}^n (y_i - \bar{y}) &= \frac{1}{n}\big(\sum_{i = 1}^n y_i - \sum_{i = 1}^n \bar{y} \big)\\\\
&= \frac{1}{n} \big( n \bar{y} - \sum_{i = 1}^n \bar{y}\big) \\\\
&= \frac{1}{n} \big( n \bar{y} - n \bar{y} \big) \\\\
&= \boxed{0}
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\frac{1}{n}\sum&#95;{i = 1}^n (y&#95;i - \bar{y}) = 0\\)</span>.

</details>

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

-   To proceed, start by rewriting <span class="math-inline">\\(y&#95;i - w\\)</span> in the definition of <span class="math-inline">\\(R&#95;{\text{sq}}(w)\\)</span> as <span class="math-inline">\\((y&#95;i - \bar{y}) + (\bar{y} - w)\\)</span>. Why is this a valid step?

-   Make sure not to expand unnecessarily. Your work should only take 3-4 lines.

<details markdown="1"><summary>Solution</summary>

We know that <span class="math-inline">\\(R&#95;\text{sq}(w) = \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i-w)^2\\)</span>. We can write this out as

<div class="math-display">
$$
\begin{align*}
R_\text{sq}(w) &= \frac{1}{n}\sum_{i=1}^n (y_i-w)^2 \\\\
&= \frac{1}{n}\sum_{i=1}^n ((y_i-\bar{y})+(\bar{y}-w))^2 \\\\
&= \frac{1}{n}\sum_{i=1}^n ((y_i-\bar{y})^2+ 2(y_i-\bar{y})(\bar{y}-w)+(\bar{y}-w)^2) \:\:\:\:\:\: \text{\parbox{4cm}{(expanding the square $(a+b)^2=a^2+2ab+b^2$ \\\\
and rearranging terms)}}
\end{align*}
$$
</div>

</details>

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

 This is called the **bias-variance decomposition** of <span class="math-inline">\\(R&#95;{\text{sq}}(w)\\)</span>.

<details markdown="1"><summary>Solution</summary>

From part **b)**, we know <span class="math-inline">\\(\displaystyle R&#95;{\text{sq}}(w) = \frac{1}{n}\sum&#95;{i=1}^n ((y&#95;i-\bar{y})^2+ 2(y&#95;i-\bar{y})(\bar{y}-w)+(\bar{y}-w)^2)\\)</span>.

<div class="math-display">
$$
\begin{align*}
&\implies R_{\text{sq}}(w) =\frac{1}{n} \left( \sum_{i=1}^n (y_i-\bar{y})^2+ \sum_{i=1}^n2(y_i-\bar{y})(\bar{y}-w)+\sum_{i=1}^n(\bar{y}-w)^2\right) \\\\
&=\frac{1}{n} \left( \sum_{i=1}^n (y_i-\bar{y})^2+ 2(\bar{y}-w)\sum_{i=1}^n(y_i-\bar{y})+\sum_{i=1}^n(\bar{y}-w)^2\right)\\\\
&=\frac{1}{n} \left( \sum_{i=1}^n (y_i-\bar{y})^2+ 2(\bar{y}-w)\cdot0+\sum_{i=1}^n(\bar{y}-w)^2\right)\:\:\:\:(\text{from 3.1, we know} \sum_{i=1}^n (y_i-\bar{y}) = 0) \\\\
&=\frac{1}{n} \left( \sum_{i=1}^n (y_i-\bar{y})^2+ 0+\sum_{i=1}^n(\bar{y}-w)^2\right) \\\\
&=\frac{1}{n} \left( \sum_{i=1}^n (y_i-\bar{y})^2+\sum_{i=1}^n(\bar{y}-w)^2\right) \\\\
&=\frac{1}{n} \left( \sum_{i=1}^n (y_i-\bar{y})^2+n\cdot(\bar{y}-w)^2\right)\\\\
&=\frac{1}{n} \sum_{i=1}^n (y_i-\bar{y})^2+(\bar{y}-w)^2\\\\
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(1 pt) Why does the result in part **c)** prove that <span class="math-inline">\\(w^&#42; = \bar{y}\\)</span> minimizes <span class="math-inline">\\(R&#95;{\text{sq}}(w)\\)</span>?

<details markdown="1"><summary>Solution</summary>

From part **c)**, we know <span class="math-inline">\\(R&#95;\text{sq}(w) = \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i-\bar{y})^2+(\bar{y}-w)^2\\)</span>. The term <span class="math-inline">\\(\frac{1}{n} \sum&#95;{i=1}^n (y&#95;i-\bar{y})^2\\)</span> is the variance, which is a constant that does not depend on <span class="math-inline">\\(w\\)</span>, so we only need to minimize <span class="math-inline">\\((\bar{y}-w)^2\\)</span>. The minimum possible value for this is 0, since it is a squared term and cannot have a negative value. We set <span class="math-inline">\\((\bar{y} - w) = 0\\)</span> which gives us the equation <span class="math-inline">\\(w=\bar{y}\\)</span>. Thus the minimizing value of <span class="math-inline">\\(w\\)</span> is <span class="math-inline">\\(w^&#42; = \bar{y}\\)</span>.

</details>

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

The value of <span class="math-inline">\\(R&#95;{\text{sq}}(w^&#42;)\\)</span>, when <span class="math-inline">\\(w^&#42; = \bar{y}\\)</span>, is equal to the

<span class="answer-blank"></span>

of the data.

<details markdown="1"><summary>Solution</summary>

variance

</details>

</div>
</div>

</div>

---

## Problem 7: Coin Flipping (9 pts)

In this problem, we'll plant the seeds of how probability, calculus, and machine learning are all related.

Suppose we find a coin on the ground, and we're unsure of whether the coin is fair. We decide to flip the coin repeatedly to estimate its bias, <span class="math-inline">\\(p\\)</span>, which is the probability of flipping heads on any particular flip. (The probability of flipping tails on any particular flip, then, is <span class="math-inline">\\(1 - p\\)</span>.)

Suppose we flip the coin 100 times and see 65 heads. Assuming that each flip is independent, this is a possible result, no matter what the value of <span class="math-inline">\\(p\\)</span> is, as long as <span class="math-inline">\\(0 &lt; p &lt; 1\\)</span>. But, some values of <span class="math-inline">\\(p\\)</span> are more believable than others.

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

<details markdown="1"><summary>Solution</summary>

We'll start by finding the derivative <span class="math-inline">\\(\frac{\text{d}L}{\text{d}p}\\)</span>:

<div class="math-display">
$$
\begin{align*}
L(p) &= { n \choose k } p^k (1-p)^{n-k} \\\\
\frac{d}{dp}L(p) &= \frac{d}{dp} \big[{ n \choose k } p^k (1-p)^{n-k} \big] \\\\
&= { n \choose k } \frac{d}{dp} \big[ p^k (1-p)^{n-k} \big] \:\:\:\: \text{(factor out constant)} \\\\
&= { n \choose k } \big(\frac{d}{dp}p^k \cdot (1-p)^{n-k} + p^k \cdot \frac{d}{dp} (1-p)^{n-k}\big) \:\:\:\: \text{(product rule)}\\\\
&= { n \choose k } \big(kp^{k-1} (1-p)^{n-k} + p^k (n-k)(1-p)^{n-k-1} \frac{d}{dp}(1-p)\big) \:\:\:\: \text{(chain rule)} \\\\
&= { n \choose k } \big( kp^{k-1} (1-p)^{n-k} + p^k (n-k)(1-p)^{n-k-1}(-1) \big)
\end{align*}
$$
</div>

Next, we set <span class="math-inline">\\(\frac{\text{d}L}{\text{d}p}\\)</span> to 0 and solve for <span class="math-inline">\\(p\\)</span>.

<div class="math-display">
$$
\begin{align*}
{ n \choose k }\cdot \left( kp^{k-1} (1-p)^{n-k} + p^k (n-k)(1-p)^{n-k-1}(-1) \right) &= 0 \\\\
kp^{k-1} (1-p)^{n-k} - p^k (n-k)(1-p)^{n-k-1} &= 0 \\\\
kp^{k-1} (1-p)^{n-k} &= p^k (n-k)(1-p)^{n-k-1} \\\\
k (1-p) &= p (n-k) \\\\
k - p k &= p n - p k \\\\
k &= p n \\\\
p^* &= \boxed{\frac{k}{n}}
\end{align*}
$$
</div>

</details>

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

<details markdown="1"><summary>Solution</summary>

We'll start by simplifying <span class="math-inline">\\(\log L(p)\\)</span>:

<div class="math-display">
$$
\begin{align*}
L(p) &= {n \choose k} p^k (1-p)^{n-k} \\\\
\log L(p) &= \log \left( {n \choose k} p^k (1-p)^{n-k} \right) \\\\
&= \log {n \choose k}  + \log \left(p^k \right) + \log \left((1 - p)^{n-k}\right) \\\\
&= \log {n \choose k} + k \log p + (n - k) \log (1 - p)
\end{align*}
$$
</div>

Next, take the derivative of <span class="math-inline">\\(\log L(p)\\)</span>:

<div class="math-display">
$$
\begin{align*}
\frac{d}{dp} \log L(p) &= \frac{d}{dp} \big[\log {n \choose k} + k \log p + (n - k) \log (1 - p)\big] \\\\
&=\frac{d}{dp}\log {n \choose k} + \frac{d}{dp}k \log p + \frac{d}{dp}(n - k) \log (1 - p) \\\\
&= 0 + k \cdot \frac{1}{p} + (n - k) \cdot\frac{1}{1 - p}\frac{d}{dp}(1-p) \:\:\:\: \text{(chain rule)} \\\\
&= 0 + k \cdot \frac{1}{p} + (n - k) \cdot\frac{1}{1 - p}(-1) \\\\
& = \frac{k}{p} - \frac{n - k}{1 - p} \\\\
\end{align*}
$$
</div>

Finally, set to 0 and solve:

<div class="math-display">
$$
\begin{align*}
0 &= \frac{k}{p} - \frac{n - k}{1 - p} \\\\
\frac{k}{p} &= \frac{n - k}{1 - p} \\\\
k - p k &= p n - p k \\\\
k &= p n \\\\
p^* &= \boxed{\frac{k}{n}}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2 pts) You should have noticed that computing the derivative of <span class="math-inline">\\(\log(L(p))\\)</span> and solving for where it is equal to 0 was much, much easier than computing the derivative of <span class="math-inline">\\(L(p)\\)</span> and solving for where it is equal to 0. This is because the logarithm function allows us to turn products into sums, which are much easier to work with.

But why was this a valid step? Why does the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span> have to be the same as the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(\log(L(p))\\)</span>? It has to do with the graph of the logarithm function.

![image](imgs/log_plot.png)

As we see above, the function <span class="math-inline">\\(f(x) = \log(x)\\)</span> is a **strictly monotonically increasing** function. This means that if <span class="math-inline">\\(a &gt; b\\)</span>, then <span class="math-inline">\\(\log(a) &gt; \log(b)\\)</span>, i.e. the graph of <span class="math-inline">\\(\log(x)\\)</span> always increases as we move from left to right.

Provide a **two sentence explanation** of why the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span> is the same as the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(\log(L(p))\\)</span>. You don't need to "prove" or write any math here, as the answer was already provided to you implicitly in this problem --- we want to ensure you understand *why* the fact that <span class="math-inline">\\(\log(x)\\)</span> is strictly monotonically increasing implies that the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(L(p)\\)</span> is the same as the value of <span class="math-inline">\\(p\\)</span> that maximizes <span class="math-inline">\\(\log(L(p))\\)</span>.

<details markdown="1"><summary>Solution</summary>

If there's a maximum value at <span class="math-inline">\\(L(p^&#42;)\\)</span>, then there's also a maximum value at <span class="math-inline">\\(\log (L(p^&#42;))\\)</span>. This holds because <span class="math-inline">\\(L(p^&#42;) &gt; L(p)\\)</span> for all <span class="math-inline">\\(p \neq p^&#42;\\)</span>, so by the properties of a monotonically increasing function <span class="math-inline">\\(\log L(p^&#42;) &gt; \log L(p)\\)</span> for all <span class="math-inline">\\(p \neq p^&#42;\\)</span>.

</details>
</div>
</div>

</div>
