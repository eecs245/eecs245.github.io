---
layout: page
title: "Lab 1: Math Foundations and Environment Setup"
description: "Lab 1: Math Foundations and Environment Setup activities."
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

# Lab 1: Math Foundations and Environment Setup

**Due:** for completion at 11:59PM Ann Arbor Time on Wednesday, May 6th, 2026

<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab01/lab01.pdf" target="_blank">View as PDF ✏️</a>

{: .yellow }
<div markdown="1">
Each lab worksheet will contain several activities, some of which will involve writing code and others that will involve writing math on paper. To receive credit for a lab, you must complete as many of the activities as you can in 2 hours and submit a PDF of your work to Gradescope. We will provide specific instructions on how to submit programming activities (e.g. submitting the notebook or including a screenshot of some output).

Feel free to work with others in the course, but you must submit individually.
</div>

---

## Activities

- [Activity 1: Environment Setup and Python Basics](#activity-1-environment-setup-and-python-basics)
- [Activity 2: Running Mean](#activity-2-running-mean)
- [Activity 3: A New Meaning](#activity-3-a-new-meaning)
- [Activity 4: The Meaning of Calculus](#activity-4-the-meaning-of-calculus)
- [Activity 5: Basics of Summation Notation](#activity-5-basics-of-summation-notation)
- [Activity 6: The Meaning of Calculus, Continued](#activity-6-the-meaning-of-calculus-continued)
- [Activity 7: Summation Notation Properties](#activity-7-summation-notation-properties)
- [Activity 8: Manipulating Sums](#activity-8-manipulating-sums)

---

## Activity 1: Environment Setup and Python Basics

Labs and homeworks will both involve writing some Python code in a Jupyter Notebook.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1 (preferred)**: Set up a Jupyter Notebook environment locally, use `git` to clone our [course repository](https://github.com/eecs245/sp26-code/tree/main/labs/lab01/lab01.ipynb), and open `labs/lab01/lab01.ipynb`. For instructions on how to do this, see the [Environment Setup](https://eecs245.org/env-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fsp26-code&urlpath=tree%2Fsp26-code%2Flabs%2Flab01%2Flab01.ipynb&branch=main) to open `lab01.ipynb` on DataHub. Before doing so, read the instructions on the [Environment Setup](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

Read the Environment Setup section of the course website, [eecs245.org/env-setup](https://eecs245.org/env-setup/), for detailed steps on setting up a local environment on your machine. Take the time to follow the steps under **Option 1: Local Setup**, and let us know if you have any questions.

Then, open the notebook `labs/lab01/lab01.ipynb`, read it, and complete the tasks inside. Once you're done, include a screenshot of your completed Task 5 implementation in your PDF submission of Lab 1 to Gradescope, making sure to include proof that the (local) autograder passed.

**Optionally**, you can submit your completed notebook itself to the Lab 1 Notebook (for practice) assignment on Gradescope; this is not required for credit, but it's a good way to practice submitting code to Gradescope, which you'll need to do for some homeworks.

---

## Activity 2: Running Mean

Over the break, you ran a hot chocolate stand. On days 1 through 5 (inclusive), you averaged 50 dollars per day in sales. On days 6 and 7, you averaged 22 dollars per day in sales. What were your average daily sales from days 1 through 7?

---

## Activity 3: A New Meaning

Over the break, in addition to running your hot chocolate stand, you took a road trip to Chicago, 240 miles away.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
For the first 120 miles, you averaged 80 miles per hour (mph). For the second 120 miles, you averaged 50 mph. What was your average speed throughout the entire journey? Leave your answer unsimplified in terms of fractions, but plug it into a calculator to get an approximation.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose, instead, you drove 3 segments of 80 miles each, in which you averaged 80 mph, 80 mph, and 50 mph. What was your average speed throughout the entire journey?

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
In general, suppose you drove <span class="math-inline">\\(n\\)</span> segments of equal length, and averaged <span class="math-inline">\\(x_i\\)</span> mph in segment <span class="math-inline">\\(i\\)</span> (<span class="math-inline">\\(i = 1, 2, ..., n\\)</span>). What was your average speed throughout the entire journey? Give your answer using **summation notation**. Your answer is the formula for the **harmonic mean** of the numbers <span class="math-inline">\\(x_1, x_2, ..., x_n\\)</span>.

</div>
</div>

</div>
---

## Activity 4: The Meaning of Calculus

Here, we'll review key ideas from Calculus 1. If you'd like a refresher, see [Appendix 2](https://notes.eecs245.org/math-foundations/derivatives/) of the course notes, [notes.eecs245.org](https://notes.eecs245.org).

Consider the function:

<div class="math-display">
$$
f(x) = (x-3)^2 + (x-4)^2 + (x-5)^2 + (x - 16)^2
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
What is the shape of <span class="math-inline">\\(f(x)\\)</span>? Your answer should be a single word.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\frac{\text{d}f}{\text{d}x}\\)</span>, the derivative of <span class="math-inline">\\(f(x)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(x^*\\)</span>, the value of <span class="math-inline">\\(x\\)</span> that minimizes <span class="math-inline">\\(f(x)\\)</span>, and prove that it is indeed a minimum, rather than a maximum.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
What does the value of <span class="math-inline">\\(x^*\\)</span> have to do with the numbers 3, 4, 5, and 16?

</div>
</div>

</div>
---

## Activity 5: Basics of Summation Notation

Here, we'll review the basics of summation notation. If you'd like a refresher, see [Appendix 1](https://notes.eecs245.org/math-foundations/summation/) of the course notes, [notes.eecs245.org](https://notes.eecs245.org).

Consider the following formula involving the first <span class="math-inline">\\(n\\)</span> natural numbers, <span class="math-inline">\\(1,2,\dots, n\\)</span>. 

<div class="math-display">
$$
1 + 2 + 3 + \ldots + n = \sum_{i=1}^n i = \frac{n(n+1)}{2}
$$
</div>

 **Using the fact above**, find <span class="math-inline">\\(\displaystyle \sum_{k = 4}^{12} (k+2)\\)</span>. Verify your answer by calculating the sum directly.

**The rest of this worksheet is extra practice. Don't feel pressured to answer all of these problems in lab, but make sure to attempt them at some point.**

---

## Activity 6: The Meaning of Calculus, Continued

<div class="math-display">
$$
f(x) = (x-3)^2 + (x-4)^2 + (x-5)^2 + (x - 16)^2
$$
</div>

For each of the following functions <span class="math-inline">\\(g(x)\\)</span>, identify all extrema (that is, maximums and/or minimums). You don't need to take the derivative in each case, but explain your reasoning.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(g(x) = \frac{1}{4} f(x)\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(g(x) = -f(2x)\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(g(x) = \sqrt{f(x)}\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(g(x) = f(x) + cx^2\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> (Hint: This may take more effort than the previous 4 did.)

</div>
</div>

</div>
---

## Activity 7: Summation Notation Properties

Suppose <span class="math-inline">\\(x_1, x_2, \dots, x_n\\)</span> and <span class="math-inline">\\(y_1, y_2, \dots, y_n\\)</span> are both lists of numbers. Determine whether each of the following expressions is true or false.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i=1}^n (a x_i + b) = a \sum_{i=1}^n x_i + bn\\)</span>, where <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> are constants.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i=1}^n (x_i + y_i)^2=\sum_{i=1}^n x_i^2 + \sum_{i=1}^n y_i^2\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i=2}^n x_i=\sum_{i=2}^k x_i + \sum_{i=k}^n x_i\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i=1}^n (x_i - \bar{x})=\sum_{i=1}^n x_i - n\bar x\\)</span>, where <span class="math-inline">\\(\displaystyle \bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i\\)</span>

</div>
</div>

</div>
---

## Activity 8: Manipulating Sums

Consider the following summations involving the first <span class="math-inline">\\(n\\)</span> natural numbers, <span class="math-inline">\\(1, 2, 3, ..., n\\)</span>.

<div class="math-display">
$$
\begin{align*}
    1 + 2 + 3 + \ldots + n &= \sum_{i=1}^n i = \frac{n(n+1)}{2} \\\\
    1^2 + 2^2 + 3^2 + \ldots + n^2 &= \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}
    % 1^3 + 2^3 + 3^3 + \ldots + n^3 &= \sum_{i=1}^n i^3 = \left( \frac{n(n+1)}{2} \right)^2
  \end{align*}
$$
</div>

Using the formulas above, determine the values of each of the following sums.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i = 5}^{15} i^2\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i = 4}^{9} 3\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{j = 1}^{20} (1 - 3j)^2\\)</span>
</div>
</div>

</div>
