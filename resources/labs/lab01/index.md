---
layout: page
title: "Lab 1: Math Foundations and Environment Setup"
description: "Lab 1: Math Foundations and Environment Setup activities."
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
.assignment-solution {
  background: #f5f5f5;
  border: 1px solid #b8b8b8;
  border-radius: 4px;
  margin: 1rem 0;
  padding: 0.75rem 0.9rem;
}
.assignment-solution summary {
  cursor: pointer;
  font-weight: 600;
}
.assignment-solution > :last-child {
  margin-bottom: 0;
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

# Lab 1: Math Foundations and Environment Setup

**due** for completion at 11:59PM Ann Arbor Time on Wednesday, May 6th, 2026

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab01/lab01.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/labs/lab01/lab01-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

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

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

The key fact being assessed here is:

<div class="math-display">
$$
\text{mean} = \frac{\text{sum}}{\text{count}}
$$
</div>

To find your new average daily sales, we need to find the sum of sales across all 7 days, and divide by the number of days (7).

-   From days 1 to 5, you averaged 50 dollars per day, meaning your total sales from days 1 to 5 were <span class="math-inline">\\(50 \cdot 5 = 250\\)</span> dollars.

-   Similarly, your total sales from days 6 and 7 combined were <span class="math-inline">\\(22 \cdot 2 = 44\\)</span> dollars.

So, your average daily sales across all 7 days is:

<div class="math-display">
$$
\frac{50 \cdot 5 + 22 \cdot 2}{7} = \frac{294}{7} = 42
$$
</div>

Note that the first expression above can be written as:

<div class="math-display">
$$
\frac{5}{7} \cdot 50 + \frac{2}{7} \cdot 22
$$
</div>

This is a **weighted average** or **weighted mean** of the numbers 50 and 22, with weights <span class="math-inline">\\(\frac{5}{7}\\)</span> and <span class="math-inline">\\(\frac{2}{7}\\)</span>, respectively. Weighted averages appear all of the time in machine learning, but even in day-to-day life: your GPA is a weighted average of your grades in each class, where the weights are the number of credits earned.

</details>

---

## Activity 3: A New Meaning

Over the break, in addition to running your hot chocolate stand, you took a road trip to Chicago, 240 miles away.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
For the first 120 miles, you averaged 80 miles per hour (mph). For the second 120 miles, you averaged 50 mph. What was your average speed throughout the entire journey? Leave your answer unsimplified in terms of fractions, but plug it into a calculator to get an approximation.

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

Following the same principle of <span class="math-inline">\\(\text{mean} = \frac{\text{sum}}{\text{count}}\\)</span> from the Running Mean activity, we have that:

<div class="math-display">
$$
\text{mean speed} = \frac{\text{total distance}}{\text{total time}}
$$
</div>

The total distance traveled was 120 miles. What was the total time taken? We can break this up into <span class="math-inline">\\(\text{time for Segment 1} + \text{time for Segment 2}\\)</span>.

-   In Segment 1, we traveled 80 miles per hour for 120 miles, so:

    

<div class="math-display">
$$
80 \text{ miles per hour} = \frac{120 \text{ miles}}{\text{time for Segment 1}} \implies \text{time for Segment 1} = \frac{120}{80} \text{ hours}
$$
</div>

-   In Segment 2, we traveled 50 miles per hour for 120 miles, so:

    

<div class="math-display">
$$
\text{time for Segment 2} = \frac{120}{50} \text{ hours}
$$
</div>

Putting this all together, we have:

<div class="math-display">
$$
\text{mean speed} = \frac{240 \text{ miles}}{\frac{120}{80} + \frac{120}{50} \text{ hours}}
$$
</div>

Notice that both the numerator and denominator have a factor of 120. Pulling this out, we have:

<div class="math-display">
$$
\text{mean speed} = \frac{2}{\frac{1}{80} + \frac{1}{50}} \approx 61.54 \text{ miles per hour}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Suppose, instead, you drove 3 segments of 80 miles each, in which you averaged 80 mph, 80 mph, and 50 mph. What was your average speed throughout the entire journey?

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

Following the same pattern, we'd have:

<div class="math-display">
$$
\text{mean speed} = \frac{240 \text{ miles}}{\frac{80}{80} + \frac{80}{80} + \frac{80}{50} \text{ hours}} = \frac{3}{\frac{1}{80} + \frac{1}{80} + \frac{1}{50}} \approx 66.67 \text{ miles per hour}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
In general, suppose you drove <span class="math-inline">\\(n\\)</span> segments of equal length, and averaged <span class="math-inline">\\(x_i\\)</span> mph in segment <span class="math-inline">\\(i\\)</span> (<span class="math-inline">\\(i = 1, 2, ..., n\\)</span>). What was your average speed throughout the entire journey? Give your answer using **summation notation**. Your answer is the formula for the **harmonic mean** of the numbers <span class="math-inline">\\(x_1, x_2, ..., x_n\\)</span>.

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

If we generalize the calculations from the previous two parts, we have:

<div class="math-display">
$$
\begin{aligned}
\text{mean speed} &= \frac{240}{\frac{\frac{240}{n}}{x_1} + \frac{\frac{240}{n}}{x_2} + \ldots + \frac{\frac{240}{n}}{x_n}} \\\\
&= \frac{240}{\frac{240}{n} \left( \frac{1}{x_1} + \frac{1}{x_2} + \ldots + \frac{1}{x_n} \right)} \\\\
&= \frac{1}{\frac{1}{n} \left( \frac{1}{x_1} + \frac{1}{x_2} + \ldots + \frac{1}{x_n} \right)} \\\\
&= \frac{n}{\frac{1}{x_1} + \frac{1}{x_2} + \ldots + \frac{1}{x_n}} \\\\
&= \frac{n}{\sum_{i=1}^n \frac{1}{x_i}}
\end{aligned}
$$
</div>

This formula computes the **harmonic mean** of the numbers <span class="math-inline">\\(x_1, x_2, ..., x_n\\)</span>. Notice that 240 doesn't appear in the final answer.

</details>

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

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(f(x)\\)</span> is a quadratic function, i.e. a parabola. We're not sure where it's centered yet --- that's the goal of parts (b) and (c).

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(\frac{\text{d}f}{\text{d}x}\\)</span>, the derivative of <span class="math-inline">\\(f(x)\\)</span>.

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}f}{\text{d}x} &= \frac{\text{d}}{\text{d}x} \left( (x-3)^2 + (x-4)^2 + (x-5)^2 + (x - 16)^2 \right) \\\\
&= 2(x-3) + 2(x-4) + 2(x-5) + 2(x-16)
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
Find <span class="math-inline">\\(x^&#42;\\)</span>, the value of <span class="math-inline">\\(x\\)</span> that minimizes <span class="math-inline">\\(f(x)\\)</span>, and prove that it is indeed a minimum, rather than a maximum.

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

First, we'll set the derivative we found in part (b) to 0:

<div class="math-display">
$$
2(x-3) + 2(x-4) + 2(x-5) + 2(x-16) = 0
$$
</div>

We can divide both sides by 2:

<div class="math-display">
$$
x-3 + x-4 + x-5 + x-16 = 0
$$
</div>

Finally, we have:

<div class="math-display">
$$
4x = (3 + 4 + 5 + 16) \implies \boxed{x^* = \frac{3 + 4 + 5 + 16}{4} = 7}
$$
</div>

To show that <span class="math-inline">\\(x^&#42;\\)</span> is indeed a minimum, we need to show that the second derivative of <span class="math-inline">\\(f(x)\\)</span> is positive at <span class="math-inline">\\(x^&#42;\\)</span>.

<div class="math-display">
$$
\frac{\text{d}^2f}{\text{d}x^2} = \frac{\text{d}}{\text{d}x} \left( 2(x-3) + 2(x-4) + 2(x-5) + 2(x-16) \right) = 2 + 2 + 2 + 2 = 8
$$
</div>

Since the second derivative is positive everywhere, <span class="math-inline">\\(f(x)\\)</span> is a convex function, and therefore has a global minimum at <span class="math-inline">\\(x^&#42;\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
What does the value of <span class="math-inline">\\(x^&#42;\\)</span> have to do with the numbers 3, 4, 5, and 16?

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(x^&#42;\\)</span> is the mean of the numbers 3, 4, 5, and 16.

<div class="math-display">
$$
4x = (3 + 4 + 5 + 16) \implies x^* = \frac{3 + 4 + 5 + 16}{4} = 7
$$
</div>

</details>

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

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

We can separate the sum into two smaller sums:

<div class="math-display">
$$
\sum_{k=4}^{12} (k+2) = \sum_{k=4}^{12} k + \sum_{k=4}^{12} 2
$$
</div>

The first sum, <span class="math-inline">\\(\displaystyle \sum_{k=4}^{12} k\\)</span>, can be rewritten as <span class="math-inline">\\(\displaystyle \sum_{k=1}^{12} k-\sum_{k=1}^{3} k\\)</span>, or the sum of the first <span class="math-inline">\\(12\\)</span> natural numbers minus the sum of the first <span class="math-inline">\\(3\\)</span>. Using the formula gives us the following: 

<div class="math-display">
$$
\frac{12\cdot 13}{2}-\frac{3 \cdot 4}{2}=\frac{156-12}{2}=72
$$
</div>

 The second sum, <span class="math-inline">\\(\displaystyle \sum_{k=4}^{12} 2\\)</span>, is just <span class="math-inline">\\(2\\)</span> added together, <span class="math-inline">\\(9\\)</span> times, which is <span class="math-inline">\\(2 \cdot 9 = 18\\)</span>.

So, the full sum is:

<div class="math-display">
$$
\sum_{k=4}^{12} (k+2) = \sum_{k=4}^{12} k + \sum_{k=4}^{12} 2=68+18=90
$$
</div>

Another way of arriving at the solution is to recognize that:

<div class="math-display">
$$
\sum_{k=4}^{12} (k+2) = \sum_{k=6}^{14} k = \left( \sum_{k=1}^{14} k \right) - \left( \sum_{k=1}^{5} k \right) = \frac{14 \cdot 15}{2} - \frac{5 \cdot 6}{2} = \frac{210-30}{2}=90
$$
</div>

</details>

---

{: .yellow }
> **The rest of this worksheet is extra practice. Don't feel pressured to answer all of these problems in lab, but make sure to attempt them at some point.**

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

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(g(x)\\)</span> is minimized at <span class="math-inline">\\(x^&#42; = 7\\)</span>.

<span class="math-inline">\\(g(x)\\)</span> has the same vertex as <span class="math-inline">\\(f(x)\\)</span>, but it is scaled vertically by a factor of <span class="math-inline">\\(\frac{1}{4}\\)</span>.

If that's not convincing, note that the derivative of <span class="math-inline">\\(g(x)\\)</span> is just <span class="math-inline">\\(\frac{1}{4}\\)</span> times the derivative of <span class="math-inline">\\(f(x)\\)</span>. When we set the derivative of <span class="math-inline">\\(g(x)\\)</span> to 0, we'll end up solving the same equation for <span class="math-inline">\\(x^&#42;\\)</span> as we did in part (c):

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}g}{\text{d}x} &= 0 \\\\
\frac{\text{d}}{\text{d}x} \left( \frac{1}{4} f(x) \right) &= 0 \\\\
\frac{1}{4} \frac{\text{d}f}{\text{d}x} &= 0 \\\\
\frac{\text{d}f}{\text{d}x} &= 0 \\\\
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(g(x) = -f(2x)\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(g(x)\\)</span> is maximized at <span class="math-inline">\\(x^&#42; = \frac{7}{2}\\)</span>.

<span class="math-inline">\\(g(x)\\)</span> is a **downward-facing** parabola, compressed horizontally by a factor of 2. It's a little more difficult to reason about horizontal compressions, so let's work through the derivative:

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}g}{\text{d}x} &= \frac{\text{d}}{\text{d}x} \left( -f(2x) \right) \\\\
&= - \frac{\text{d}}{\text{d}x} \left( (2x-3)^2 + (2x-4)^2 + (2x-5)^2 + (2x-16)^2 \right) \\\\
&= - 2(2x-3) \cdot 2 - 2(2x-4) \cdot 2 - 2(2x-5) \cdot 2 - 2(2x-16) \cdot 2 \\\\
&= - 4(2x-3) - 4(2x-4) - 4(2x-5) - 4(2x-16)
\end{align*}
$$
</div>

In the second-last line above, the additional factors of two are the result of the chain rule (the derivative of <span class="math-inline">\\(2x - 3\\)</span> with respect to <span class="math-inline">\\(x\\)</span> is <span class="math-inline">\\(2\\)</span>), and you'll notice that each term in parentheses involves <span class="math-inline">\\(2x\\)</span>, not just <span class="math-inline">\\(x\\)</span> as with <span class="math-inline">\\(f(x)\\)</span>.

Setting the derivative of <span class="math-inline">\\(g(x)\\)</span> to 0, we have:

<div class="math-display">
$$
\begin{align*}
-4(2x-3) - 4(2x-4) - 4(2x-5) - 4(2x-16) &= 0 \\\\
2x-3 + 2x-4 + 2x-5 + 2x-16 &= 0 \\\\
8x &= 3 + 4 + 5 + 16 \\\\
x^* &= \frac{3 + 4 + 5 + 16}{8} = \frac{7}{2}
\end{align*}
$$
</div>

Intuitively, if we set <span class="math-inline">\\(u = 2x\\)</span>, then <span class="math-inline">\\(g(x) = -f(u)\\)</span>, and we know that <span class="math-inline">\\(-f(u)\\)</span> is maximized where <span class="math-inline">\\(f(u)\\)</span> is minimized, which is at <span class="math-inline">\\(u^&#42; = 7\\)</span>. Since <span class="math-inline">\\(u = 2x\\)</span>, we have <span class="math-inline">\\(x^&#42; = \frac{u^&#42;}{2} = \frac{7}{2}\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(g(x) = \sqrt{f(x)}\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(g(x)\\)</span> is minimized at <span class="math-inline">\\(x^&#42; = 7\\)</span>.

<span class="math-inline">\\(\sqrt{x}\\)</span> is a **strictly monotonically increasing** function across its domain, which is <span class="math-inline">\\([0, \infty)\\)</span>. What this means is that if <span class="math-inline">\\(a &gt; b\\)</span>, then <span class="math-inline">\\(\sqrt{a} &gt; \sqrt{b}\\)</span>, or in other words, as we move from left to right, the graph of the function only increases, never stays the same or decreases. Strictly monotonically increasing functions preserve the order of their inputs.

<span class="math-inline">\\(\log(x)\\)</span> is also a strictly monotonically increasing function. <span class="math-inline">\\(x^2\\)</span> is **not**, because, for example, <span class="math-inline">\\((-3)^2 &gt; 2^2\\)</span>, but <span class="math-inline">\\(-3\\)</span> is not greater than <span class="math-inline">\\(2\\)</span>.

What does this have to do with finding the extrema of <span class="math-inline">\\(g(x)\\)</span>? Well, since we know that <span class="math-inline">\\(f(7)\\)</span> is at the bottom of the graph of <span class="math-inline">\\(f(x)\\)</span>, we know that <span class="math-inline">\\(\sqrt{f(7)}\\)</span> is at the bottom of the graph of <span class="math-inline">\\(\sqrt{f(x)}\\)</span>, because of the fact that <span class="math-inline">\\(\sqrt{x}\\)</span> is strictly monotonically increasing, meaning that order is preserved.

If that's not a convincing argument, we can also work through the derivative:

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}g}{\text{d}x} &= \frac{\text{d}}{\text{d}x} \left( \sqrt{f(x)} \right) \\\\
&= \frac{\text{d}}{\text{d}x} \left( f(x) \right)^{\frac{1}{2}} \\\\
&= \frac{1}{2} \left( f(x) \right)^{-\frac{1}{2}} \cdot \frac{\text{d}f}{\text{d}x} \\\\
&= \frac{1}{2\sqrt{f(x)}} \cdot \frac{\text{d}f}{\text{d}x}
\end{align*}
$$
</div>

To solve for the extrema of <span class="math-inline">\\(g(x)\\)</span>, we need to set its derivative to 0. Its derivative contains two factors, one of which is <span class="math-inline">\\(\frac{\text{d}f}{\text{d}x}\\)</span> --- which we know is 0 at <span class="math-inline">\\(x^&#42; = 7\\)</span> --- and the other is <span class="math-inline">\\(\frac{1}{2\sqrt{f(x)}}\\)</span>, which can never be 0 (think about why). So, <span class="math-inline">\\(g(x)\\)</span> must be minimized at <span class="math-inline">\\(x^&#42; = 7\\)</span>.

Visualize <span class="math-inline">\\(f(x)\\)</span> and <span class="math-inline">\\(g(x)\\)</span> [here](https://www.desmos.com/calculator/vclhujhle8) on Desmos.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(g(x) = f(x) + cx^2\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> (Hint: This may take more effort than the previous 4 did.)

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(g(x)\\)</span> is minimized at <span class="math-inline">\\(x^&#42; = \frac{28}{4 + c}\\)</span>.

It's hard to reason about the extrema of <span class="math-inline">\\(g(x)\\)</span> without taking the derivative, at least at first.

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}g}{\text{d}x} &= \frac{\text{d}}{\text{d}x} \left( f(x) + cx^2 \right) \\\\
&= \frac{\text{d}}{\text{d}x} \left( f(x) \right) + \frac{\text{d}}{\text{d}x} \left( cx^2 \right) \\\\
&= 2(x-3) + 2(x-4) + 2(x-5) + 2(x-16) + 2cx
\end{align*}
$$
</div>

Setting the derivative to 0, we have:

<div class="math-display">
$$
\begin{align*}
2(x-3) + 2(x-4) + 2(x-5) + 2(x-16) + 2cx &= 0 \\\\
x-3 + x-4 + x-5 + x-16 + cx &= 0 \\\\
(4+c)x &= 3 + 4 + 5 + 16 \\\\
\end{align*}
$$
</div>

So: 

<div class="math-display">
$$
x^* = \frac{3 + 4 + 5 + 16}{4 + c} = \boxed{\frac{28}{4 + c}}
$$
</div>

You'll notice that if <span class="math-inline">\\(c = 0\\)</span>, then <span class="math-inline">\\(x^&#42; = 7\\)</span>, which is the same as the minimum of <span class="math-inline">\\(f(x)\\)</span>, as this equates to "turning off" the new <span class="math-inline">\\(cx^2\\)</span> term.

How else could we have reasoned about <span class="math-inline">\\(x^&#42;\\)</span>? One way to think about it is that <span class="math-inline">\\(\text{Mean}(x_1, x_2, ..., x_n)\\)</span> minimizes:

<div class="math-display">
$$
(x - x_1)^2 + (x - x_2)^2 + \ldots + (x - x_n)^2
$$
</div>

This is a generalization of your discovery from part (d), where <span class="math-inline">\\(x_1, x_2, ..., x_n\\)</span> were the numbers 3, 4, 5, and 16.

When we added <span class="math-inline">\\(cx^2\\)</span> to <span class="math-inline">\\(f(x)\\)</span>, it was almost like adding the value <span class="math-inline">\\(x^2\\)</span>, or equivalently, <span class="math-inline">\\((x-0)^2\\)</span>, <span class="math-inline">\\(c\\)</span> times. In other words:

<div class="math-display">
$$
g(x) = (x-3)^2 + (x-4)^2 + (x-5)^2 + (x-16)^2 + \underbrace{x^2 + x^2 + \ldots + x^2}_{c \text{ times}}
$$
</div>

So, knowing that the mean minimizes the sum of squared errors, we can conclude that <span class="math-inline">\\(x^&#42;\\)</span> should be the mean of the numbers <span class="math-inline">\\(3, 4, 5, 16, 0, ..., 0\\)</span> (where there are <span class="math-inline">\\(c\\)</span> zeros). The mean of these numbers is their sum over their count; their sum is <span class="math-inline">\\(3 + 4 + 5 + 16 + 0 + ... + 0 = 28\\)</span>, and their count is <span class="math-inline">\\(4 + c\\)</span>. So, <span class="math-inline">\\(x^&#42; = \frac{28}{4 + c}\\)</span>.

This logic is not perfect, since <span class="math-inline">\\(c\\)</span> didn't need to be an integer, but it helps build intuition for the answer.

</details>

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

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

We'll start by splitting the sum into two parts: 

<div class="math-display">
$$
\displaystyle \sum_{i=1}^n (a x_i + b)=\sum_{i=1}^n ax_i + \sum_{i=1}^n b
$$
</div>

We can factor out the constant in the first sum, <span class="math-inline">\\(\displaystyle \sum_{i=1}^n ax_i\\)</span>, to rewrite it as <span class="math-inline">\\(\displaystyle a\sum_{i=1}^n x_i\\)</span>.

The second sum, <span class="math-inline">\\(\displaystyle \sum_{i=1}^n b\\)</span> can be rewritten as <span class="math-inline">\\(bn\\)</span> because it's equivalent to adding <span class="math-inline">\\(b\\)</span> together <span class="math-inline">\\(n\\)</span> times. So, the statement is true.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i=1}^n (x_i + y_i)^2=\sum_{i=1}^n x_i^2 + \sum_{i=1}^n y_i^2\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

Expanding out the square in the sum gives us the following: 

<div class="math-display">
$$
\displaystyle \sum_{i=1}^{n}(x_i+y_i)^2=\sum_{i=1}^{n}(x_i^2+2x_i y_i + y_i^2)
$$
</div>

Then, we split the terms: 

<div class="math-display">
$$
\displaystyle \sum_{i=1}^{n}(x_i+y_i)^2=\sum_{i=1}^{n}x_i^2+ \sum_{i=1}^{n} 2x_i y_i +\sum_{i=1}^{n}y_i^2
$$
</div>

There's no way for us to get rid of the second term, so the answer is false in general.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i=2}^n x_i=\sum_{i=2}^k x_i + \sum_{i=k}^n x_i\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

False, this is an off by one error. Since summations are inclusive, the right hand side is double counting <span class="math-inline">\\(x_k\\)</span>.

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i=1}^n (x_i - \bar{x})=\sum_{i=1}^n x_i - n\bar x\\)</span>, where <span class="math-inline">\\(\displaystyle \bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

Once again, we'll start by splitting the sum into two parts: 

<div class="math-display">
$$
\displaystyle \sum_{i=1}^n (x_i - \bar{x})=\sum_{i=1}^n x_i - \sum_{i=1}^n \bar x
$$
</div>

 The key to this problem is that <span class="math-inline">\\(\bar x\\)</span> is the mean of the <span class="math-inline">\\(x_i\\)</span>'s, and the mean is a fixed value. In other words, <span class="math-inline">\\(\bar x\\)</span> is a **constant**, not a variable! Using this fact, we can simplify the second term further: 

<div class="math-display">
$$
\sum_{i=1}^n x_i - \sum_{i=1}^n \bar x=\sum_{i=1}^n x_i - n \bar x
$$
</div>

 So, the answer is true. Furthermore, <span class="math-inline">\\(\sum_{i = 1}^n x_i = n \bar x\\)</span>, so both sides of the equation are equal to <span class="math-inline">\\(0\\)</span>.

</details>

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
\end{align*}
$$
</div>

Using the formulas above, determine the values of each of the following sums.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i = 5}^{15} i^2\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

The key is recognizing that we can express the sum we're looking for as the difference of two other sums that have closed-form expressions:

<div class="math-display">
$$
\sum_{i=5}^{15} i^2 = \sum_{i=1}^{15} i^2 - \sum_{i=1}^{4} i^2
$$
</div>

Given that, we have:

<div class="math-display">
$$
\begin{align*}
\sum_{i=5}^{15} i^2 &= \sum_{i=1}^{15} i^2 - \sum_{i=1}^{4} i^2 \\\\
&= \frac{15(16)(31)}{6} - \frac{4(5)(9)}{6} \\\\
&= 1240 - 30 \\\\
&= 1210
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{i = 4}^{9} 3\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

Notice that the sum we're looking for is just <span class="math-inline">\\(3\\)</span> added together, several times --- it does not involve <span class="math-inline">\\(i\\)</span>.

How many times are we adding <span class="math-inline">\\(3\\)</span>? It's tempting to think it's <span class="math-inline">\\(5\\)</span> times, since <span class="math-inline">\\(9 - 4 = 5\\)</span>, but that is one short. Count out the numbers from <span class="math-inline">\\(4\\)</span> to <span class="math-inline">\\(9\\)</span> to see that the range includes 6 numbers, when we include both endpoints.

So, the sum is:

<div class="math-display">
$$
\sum_{i=4}^{9} 3 = 3 + 3 + 3 + 3 + 3 + 3 = 3 \cdot (9 - 4 + 1) = 3 \cdot 6 = 18
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="math-inline">\\(\displaystyle \sum_{j = 1}^{20} (1 - 3j)^2\\)</span>

<details class="assignment-solution" markdown="1"><summary>Solution</summary>

We'll have to expand a fair bit here:

<div class="math-display">
$$
\begin{align*}
\sum_{j=1}^{20} (1 - 3j)^2 &= \sum_{j=1}^{20} (1 - 6j + 9j^2) \\\\
&= \sum_{j=1}^{20} 1 - \sum_{j=1}^{20} 6j + \sum_{j=1}^{20} 9j^2 \\\\
&= 20 - 6 \sum_{j=1}^{20} j + 9 \sum_{j=1}^{20} j^2 \\\\
\end{align*}
$$
</div>

We know that <span class="math-inline">\\(\displaystyle \sum_{j=1}^{20} j = \frac{20 \cdot 21}{2} = 210\\)</span> and <span class="math-inline">\\(\displaystyle \sum_{j=1}^{20} j^2 = \frac{20 \cdot 21 \cdot 41}{6} = 2870\\)</span>. So, we have:

<div class="math-display">
$$
\begin{align*}
\sum_{j=1}^{20} (1 - 3j)^2 &= 20 - 6 \cdot 210 + 9 \cdot 2870 \\\\
&= 20 - 1260 + 25830 \\\\
&= 24590
\end{align*}
$$
</div>

</details>
</div>
</div>

</div>
