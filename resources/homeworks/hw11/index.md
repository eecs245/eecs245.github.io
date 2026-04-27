---
layout: page
title: "Homework 11: Singular Value Decomposition"
description: "Homework 11: Singular Value Decomposition problems."
nav_exclude: true
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
</style>

# Homework 11: Singular Value Decomposition

**Due:** Tuesday, April 21st, 2026 at 11:59PM Ann Arbor Time

{: .yellow }
**Why is this homework a webpage instead of a PDF?**<br>Starting on April 24, 2026, all public universities must make their content digitally accessible for students with disabilities. Webpages can be more accessible than PDFs for those who use screen readers or other assistive technologies. To experiment with the best practices for accessibility, we've converted this homework to a webpage. A PDF version, and Overleaf template, are still linked below. In the End-of-Semester Survey, we'll ask for your feedback on this format.

<a class="btn btn-info btn-sm" href="/resources/homeworks/hw11/hw11.pdf" target="_blank">✏️ PDF</a>
<a class="btn btn-info btn-sm" href="https://www.overleaf.com/read/vjyvfvswbpnj#9556ea" target="_blank">🍃 LaTeX Template</a>

Write your solutions to the following problems by either typing them up or handwriting them on another piece of paper. Homeworks are due to Gradescope by 11:59PM on the due date. See the [syllabus](https://eecs245.org/syllabus/#homeworks) for details on the slip day policy.

Homework will be evaluated not only on the correctness of your answers, but on your ability to present your ideas clearly and logically. You should always explain and justify your conclusions, using sound reasoning. Your goal should be to convince the reader of your assertions. If a question does not require explanation, it will be explicitly stated.

Before proceeding, make sure you're familiar with the [collaboration policy](https://eecs245.org/syllabus/#homeworks).

## Problems

- [Problem 1: Homework 10 Solutions Review](#problem-1-homework-10-solutions-review-10-pts)
- [Problem 2: SVD Fundamentals](#problem-2-svd-fundamentals-18-pts)
- [Problem 3: Frobenius Norm and Low-Rank Approximation](#problem-3-frobenius-norm-and-low-rank-approximation-22-pts)
- [Problem 4: Principal Components Analysis](#problem-4-principal-components-analysis-15-pts)

Total Points: 10 + 18 + 22 + 15 = 65

---

## Problem 1: Homework 10 Solutions Review <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

Review the solutions to Homework 10. Pick **two problem parts** (for example, Problem 6b and Problem 7c) from Homework 10 in which your solutions have the most room for improvement, i.e. where they have unsound reasoning, could be significantly more efficient or clearer, etc. Include a screenshot of your solution to each problem part, and in a few sentences, explain what was deficient and how it could be fixed.

Alternatively, if you think one of your solutions is significantly better than the posted one, copy it here and explain why you think it is better. If you didn't do Homework 10, choose two problem parts from it that look challenging to you, and in a few sentences, explain the key ideas behind their solutions in your own words.

---

## Problem 2: SVD Fundamentals <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">18 pts</span>

Before getting started, make sure to refer to [Chapter 10.1](https://notes.eecs245.org/singular-value-decomposition/computing-svd/). These problems aren't as computationally intensive as they look; think about ways to be efficient.

### Part a) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

Let \\(A\\) be a \\(2 \times 2\\) matrix with singular value decomposition \\(A = U \Sigma V^T\\) where:

-   The first column of \\(U\\) is \\(\vec u_1 = \begin{bmatrix} 2/\sqrt{5} \\\\ 1/\sqrt{5} \end{bmatrix}\\).

-   \\(A \vec v_1 = 3 \vec u_1\\), where \\(\vec v_1 = \begin{bmatrix} 1/\sqrt{2} \\\\ 1/\sqrt{2} \end{bmatrix}\\) is the first column of \\(V\\).

-   The second singular value of \\(A\\) is \\(\sigma_2 = 1\\).

Given this information, find \\(U\\), \\(\Sigma\\), and \\(V^T\\).

### Part b) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span>

Let \\(X = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 2 & -1 \\\\ 2 & 2 \end{bmatrix}\\).

1.  Compute the singular value decomposition (that is, find \\(U\\), \\(\Sigma\\), and \\(V^T\\)) for \\(X\\). Do this by hand, but use `np.linalg.svd` in Python to verify your work.

2.  Now, compute the singular value decomposition for \\(X^T = \begin{bmatrix} 1 & 0 & 2 & 2 \\\\ 0 & 1 & -1 & 2 \end{bmatrix}\\). How can you reuse your work in finding the SVD of \\(X\\) to compute the SVD of \\(X^T\\)?

### Part c) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

Compute the singular value decomposition for the diagonal matrix \\(X = \begin{bmatrix} 3 & 0 & 0 \\\\ 0 & -2 & 0 \\\\ 0 & 0 & -2 \end{bmatrix}\\).

### Part d) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

Compute the singular value decomposition for the rank-one matrix \\(X = \begin{bmatrix} 0 & 0 \\\\ 3 & 4 \\\\ 6 & 8 \end{bmatrix}\\).\
*Hint: Can you write \\(X\\) as an outer product of two vectors? If you can, how do those vectors relate to the singular values and singular vectors of \\(X\\)?*

---

## Problem 3: Frobenius Norm and Low-Rank Approximation <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">22 pts</span>

As we first saw in Chapter 2.1, the norm of a vector is a measure of its size. The "default" norm is the Euclidean, or \\(L_2\\) norm, \\(\lVert \vec v \rVert_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}\\).

Similarly, the norm of a matrix is a measure of its size. The most common matrix norm is the **Frobenius norm**, defined as $$\lVert X \rVert_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^d x_{ij}^2}$$ That is, \\(\lVert X \rVert_F\\) is the square root of the sum of the squares of the elements of \\(X\\); it treats \\(X\\) as a vector and computes its \\(L_2\\) norm.

### Part a) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span>

Verify that \\(\lVert X \rVert_F = \sqrt{15}\\) for \\(X = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 2 & -1 \\\\ 2 & 2 \end{bmatrix}\\).\
*Notice that \\(\sqrt{15} = \sqrt{10 + 5}\\), and in Problem 2a), you found that \\(X\\)'s singular values were \\(\sigma_1 = \sqrt{10}\\) and \\(\sigma_2 = \sqrt{5}\\). We build on this idea in part **c)**.*

### Part b) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

Another equivalent formula for the Frobenius norm is $$\lVert X \rVert_F^2 = \text{trace}(X^T X)$$ where \\(\text{trace}(X^T X)\\) is the sum of the diagonal entries of \\(X^TX\\). (Notice the square on the left-hand side!) **Explain why** this is equivalent to the first definition of the Frobenius norm.

### Part c) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

Another equivalent formula for the Frobenius norm is $$\lVert X \rVert_F^2 = \sum_{i=1}^r \sigma_i^2$$ where \\(\sigma_1, \sigma_2, \ldots, \sigma_r\\) are the singular values of \\(X\\) and \\(r = \text{rank}(X)\\). **Explain why** this is equivalent to the definition of the Frobenius norm from part **b)**. *Hint: What is the relationship between the singular values of \\(X\\) and the eigenvalues of some other matrix?*

The Frobenius norm allows us to make more precise the idea of a rank-\\(k\\) approximation of a matrix, first introduced in [Chapter 10.2](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation/).\
Suppose \\(X = U \Sigma V^T\\) is the singular value decomposition of the \\(n \times d\\) matrix \\(X\\), where the columns of \\(U\\) are \\(\vec u_1, \vec u_2, \ldots, \vec u_n \in \mathbb{R}^n\\), the singular values of \\(X\\) are \\(\sigma_1, \sigma_2, \ldots, \sigma_r > 0\\), the rows of \\(V^T\\) are \\(\vec v_1, \vec v_2, \ldots, \vec v_d \in \mathbb{R}^d\\), and \\(r = \text{rank}(X)\\).\
The Eckart--Young--Mirsky theorem states that, for any integer \\(k\\) between 1 and \\(r\\), the \\(n \times d\\) matrix

$$X_k = \sum_{i=1}^k \sigma_i \vec u_i \vec v_i^T$$ 

is the closest rank-\\(k\\) matrix to \\(X\\), in terms of Frobenius norm. That is, if \\(Y\\) is any other \\(n \times d\\) matrix of rank \\(k\\), then \\(\lVert X - X_k \rVert_F \leq \lVert X - Y \rVert_F\\). More intuitively, this says that \\(X_k\\) is the matrix with the smallest mean squared error from \\(X\\), among all \\(n \times d\\) matrices of rank \\(k\\). We will not prove this theorem in class.

### Part d) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span>

Let's illustrate the above with an example. Consider the \\(3 \times 4\\) matrix \\(X\\), whose singular value decomposition is given by

$$\underbrace{\begin{bmatrix} 24 & 0 & 0 & 24 \\\\ 7 & 25 & 25 & 7 \\\\ 1 & -1 & 1 & -1 \end{bmatrix}}_{X} = \underbrace{\begin{bmatrix} 0.6 & 0.8 & 0 \\\\ 0.8 & -0.6 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}}_{U} \underbrace{\begin{bmatrix} 40 & 0 & 0 & 0 \\\\ 0 & 30 & 0 & 0 \\\\ 0 & 0 & 2 & 0 \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} 1/2 & 1/2 & 1/2 & 1/2 \\\\ 1/2 & -1/2 & -1/2 & 1/2 \\\\ 1/2 & -1/2 & 1/2 & -1/2 \\\\ -1/2 & -1/2 & 1/2 & 1/2 \end{bmatrix}}_{V^T}$$

For \\(k = 1, 2, 3\\), compute the rank-\\(k\\) approximation \\(X_k = \sum_{i=1}^k \sigma_i \vec u_i \vec v_i^T\\) and the Frobenius norm of the approximation error, \\(\lVert X - X_k \rVert_F\\).\
Feel free to do the computations by hand or using `numpy`. If you use `numpy`, make sure to include screenshots of any code you write and its outputs, and **don't** use `np.linalg.svd`; instead, enter the SVD we provided you with and use `np.outer` to compute the outer product of two vectors.

### Part e) <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span>

Open the **the supplemental Jupyter Notebook** we've created for Homework 11, which can either be found [here](https://github.com/eecs245/wn26-code/blob/main/homeworks/hw11/hw11.ipynb) in the course GitHub repository, or [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fwn26-code&urlpath=tree%2Fwn26-code%2Fhomeworks%2Fhw11%2Fhw11.ipynb&branch=main) on DataHub.\
There, you're asked to implement the rank-\\(k\\) approximation of an image of your choosing, similar to the [Image Compression example in Chapter 10.2](https://notes.eecs245.org/singular-value-decomposition/low-rank-approximation/#example-image-compression).

More instructions are provided in the notebook. This problem is **not autograded**. Rather, in your submission to this part, include screenshots of all of your code and outputs here.

---

## Problem 4: Principal Components Analysis <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">15 pts</span>

**Make sure you've completed Problem 3 before attempting this problem.**

This problem involves a practical exploration of principal components analysis (PCA), perhaps the most interesting application of the singular value decomposition.

There are two ways to access the supplemental Jupyter Notebook:

-   **Option 1**: Set up a Jupyter Notebook environment locally, use `git` to clone our course repository, and open `homeworks/hw11/hw11.ipynb`. For instructions on how to do this, see the [Tech Support](https://eecs245.org/env-setup/#option-1-local-setup) page of the course website.

-   **Option 2**: Click [here](https://datahub.eecs245.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Feecs245%2Fwn26-code&urlpath=tree%2Fwn26-code%2Fhomeworks%2Fhw11%2Fhw11.ipynb&branch=main) to open `hw11.ipynb` on DataHub. Before doing so, read the instructions on the [Tech Support](https://eecs245.org/env-setup/#option-2-using-the-eecs-245-datahub) page on how to use the DataHub.

**This problem is NOT autograded**. Instead, complete the five tasks mentioned in Problem 4, and include screenshots of all of your code and outputs here, along with your written answers to Tasks 3 and 5.
