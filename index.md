---
layout: page
title: 🏡 Home
description: >-
  "Information about EECS 245: Mathematics for Machine Learning in Fall 2025 at the University of Michigan."
nav_order: 1
---

# Mathematics for Machine Learning 🧠
{: .no_toc }
{: .mb-2 }
EECS 245*, Fall 2025 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }

<small>4 credits • Open to all majors • Satisfies linear algebra requirement for CS majors and EECS 445</small><br>
<small>*Officially numbered EECS 298-004 and EECS 298-005; EECS 245 will be used starting Winter 2026</small>

{% for staffer in site.staffersnobio %}
{{ staffer }}
{% endfor %}

[Jump to Week 11](#week-11-gradient-descent-eigenvalues-and-eigenvectors){: .btn .btn-green } [Announcements on Ed 📣](https://edstem.org/us/courses/81392/discussion/6878182){: .btn .btn-purple }

{: .green }
> - **There is no live lecture on Tuesday, November 4th.** Find the relevant recording [**here**](https://www.loom.com/share/0b459d47827d4a2093d58a0632c9a97e).
> - **Midterm 2 is on Tuesday, November 11th in lecture.** Lectures 11-19, Chapters 2.6-4.3, Labs 6-10, and Homeworks 5-9 are all in scope. Come to the mock exam **this Friday from 2:30-5:30PM in 1365 LCSIB**.

{% for module in site.modules %}
{{ module }}
{% endfor %}

<!-- {: .green }
Linear algebra forms the basis of modern machine learning and artificial intelligence. _Mathematics for Machine Learning_ will introduce students to the theory of linear algebra while exposing them to its applications to real-world machine learning problems using Python. After taking this course, students will understand the mathematical underpinnings of linear regression, neural networks, gradient descent, decision trees, dimensionality reduction, and other core ideas in machine learning. -->

<!-- 1. TOC
{:toc} -->

<!-- ## Content

Linear algebra, calculus, and probability form the basis of modern machine learning and artificial intelligence. **This course will introduce linear algebra from scratch by focusing on methods and examples from machine learning.** It will give students strong intuition for how linear algebra, calculus and probability are used in machine learning. While the course is primarily theoretical, we'll look at practical applications involving real data in Python each week, so that students are able to apply what they've learned.

Each topic below corresponds to ~1-2 lectures.

- Python, Jupyter Notebooks, and `numpy`.
- Introduction to supervised learning: parameters, loss functions, and empirical risk minimization.
- Optimization in single and multiple variables.
- Vectors, the dot product, and projections.
- Vector spaces and spans.
- Matrices, linear independence, and rank.
- Multiple linear regression, using both projections and vector calculus.
- Partial derivatives and gradient vectors.
- Gradient descent.
- Eigenvalues and eigenvectors.
- Singular value decomposition (SVD) and Principal Components Analysis (PCA).
- The PageRank algorithm.
- Random variables.
- Independence and conditional independence.
- Maximum likelihood estimation.


## Format

- **Lectures (TuTh 3-4:30PM, 1013 DOW)**: Introduce core content in an interactive format. Recorded, and attendance will **not** be taken.
- **Labs (W 12:30-2:30PM or W 4:30-6:30PM)**: Provide supervised practice with mathematical ideas and a venue for exploring practical applications in Python. Attendance **will** be taken.
- **Homeworks**: Assigned and due weekly. Will consist of ~80% math on paper and ~20% code in Python.
- **Exams**: 1-2 Midterm Exams and one Final Exam, all in-person and on-paper.

 -->
