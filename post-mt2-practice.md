---
layout: page
title: Post-Midterm 2 Practice Problems
description: Practice problems for the content introduced after Midterm 2.
nav_exclude: true
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

# Post-Midterm 2 Practice Problems

This page contains several practice problems for content introduced after Midterm 2. They are sorted by topic:

- Problems 1-14 are on [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors).
- Problems 15-20 are on the [Singular Value Decomposition](#singular-value-decomposition).
- Problems 21-24 are on [Principal Components Analysis](#principal-components-analysis).

The problems range in difficulty, and aren't necessarily indicative of the difficulty or styles of problems you will see on the real exam; some problems are more open-ended than we'd ask on an exam, and are designed to encourage you to review parts of the course notes.

As we're able to, we will embed videos to certain problems here.

---

## Eigenvalues and Eigenvectors

### Problem 1 (A problem just like this one will appear on the Final Exam!)

Let 

$$A = \begin{bmatrix} 3 & -1 & 1 \\ 0 & 5 & 4 \\ 0 & 0 & 5 \end{bmatrix}$$ 

Find the eigenvalues and eigenvectors of $$A$$. If $$A$$ is diagonalizable, write it in the form $$A = V \Lambda V^{-1}$$, and if it is not, explain why not.

---

### Problem 2

Suppose $$A$$ is a $$3 \times 3$$ matrix such that the eigenspace for $$\lambda = 1$$ is the line spanned by $$\begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$, and the eigenspace for $$\lambda = -5$$ is the plane $$2x - 3y + 4z = 0$$.

1. Why is $$A$$ diagonalizable?
2. Find matrices $$V$$ and $$\Lambda$$ such that $$A = V \Lambda V^{-1}$$.

---

### Problem 3

In each part, answer the following questions about the $$n \times n$$ matrix $$A$$:

- What is the value of $$n$$?
- Is $$A$$ invertible?
- Is $$A$$ diagonalizable, or is it impossible to tell?

1. $$A$$ has characteristic polynomial $$p(\lambda) = \lambda^3 - 16\lambda$$.

2. $$A$$ has characteristic polynomial $$p(\lambda) = (2 - \lambda)(4 - \lambda)(5 - \lambda)^2$$.

---

### Problem 4

Suppose $$A$$ is an $$n \times n$$ matrix with characteristic polynomial $$p(\lambda) = \lambda^3 (2 - \lambda)(4 - \lambda)$$.

Fill in the blank: $$A$$ is diagonalizable if and only if $$\text{rank}(A) = \_\_\_\_$$.

<center><iframe width="640" height="360" src="https://www.loom.com/embed/16e913f28c0140999769f34d52cf719e" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></center>

---

### Problem 5

Suppose $$A$$ is a $$2 \times 2$$ matrix with characteristic polynomial $$p(\lambda)$$, where $$p(0) = 0$$ and $$p(1) = -5$$.

Find two possible matrices $$A$$.

---

### Problem 6

Suppose $$A$$ is a diagonalizable $$3 \times 3$$ matrix with eigenvalue decomposition $$A = V \Lambda V^{-1}$$.

Suppose $$\vec v_1$$, $$\vec v_2$$, and $$\vec v_3$$ are the columns of $$V$$, and suppose $$\vec x \in \mathbb{R}^3$$ is some other vector such that

$$x = 3 \vec v_1 - 2 \vec v_2 + 4 \vec v_3, \qquad A \vec x = 15 \vec v_1 - 8 \vec v_3$$

1. Why is it guaranteed that no other linear combination of $$\vec v_1$$, $$\vec v_2$$, and $$\vec v_3$$ can equal $$\vec x$$?

2. Find $$V^{-1} \vec x$$.

3. What are the eigenvalues of $$A$$?

<center><iframe width="640" height="360" src="https://www.loom.com/embed/ffc2db21fe4a4c0892d8de7ec5dfbde5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></center>

---

### Problem 7

Identify whether each of the following statements is true or false, and justify your answer.

1. If $$A$$ is upper triangular, then $$A$$ is diagonalizable.
1. Every $$13 \times 13$$ matrix has at least one real eigenvalue.
1. There exists a $$7 \times 7$$ matrix with an eigenvalue $$\lambda$$ with algebraic multiplicity $$\text{AM}(\lambda) = 3$$ and geometric multiplicity $$\text{GM}(\lambda) = 4$$.
1.  There exists a non-zero $$7 \times 7$$ matrix with an eigenvalue of $$0$$ with geometric multiplicity $$\text{GM}(0) = 7$$.
1. If two matrices have the same characteristic polynomial, then either they are both diagonalizable, or they are both not diagonalizable.

---

### Problem 8

Suppose $$A$$ and $$B$$ are both $$2 \times 2$$ matrices with an eigenvalue of $$5$$.

1. Is $$AB$$ also guaranteed to have an eigenvalue of $$5$$?
2. Is $$A + B$$ also guaranteed to have an eigenvalue of $$5$$?

---

### Problem 9

1. Suppose $$A$$ has an eigenvalue of $$\lambda$$. Show that $$A^k$$ has an eigenvalue of $$\lambda^k$$ with the same eigenvector.
1. The converse of the statement above is false --- that is, just because $$A^k$$ has an eigenvalue of $$\lambda^k$$, it does not mean $$A$$ has an eigenvalue of $$\lambda$$. Find a counterexample, by finding a matrix $$A$$ such that $$A^2$$ has an eigenvalue of $$1$$, but $$A$$ does not have an eigenvalue of $$\pm 1$$. Is $$A$$ diagonalizable?

---

### Problem 10

Let $$A = \begin{bmatrix} 1 & 3 \\ 3 & 1 \end{bmatrix}$$. 

1. What is the name of the theorem that guarantees that $$A$$ is diagonalizable?
1. What does that theorem say about the eigenvectors of $$A$$?

---

### Problem 11

Prove that if $$\vec u$$ and $$\vec v$$ are eigenvectors of the symmetric matrix $$S$$ corresponding to different eigenvalues, then $$\vec u$$ and $$\vec v$$ are orthogonal. This is the essence of the spectral theorem.

---

### Problem 12

Consider the **symmetric** matrix $$A = \begin{bmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{bmatrix}$$. $$A$$ can be diagonalized into $$A = V \Lambda V^{-1}$$ as follows:

$$\underbrace{\begin{bmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{bmatrix}}_{A} = \underbrace{\begin{bmatrix} \dfrac{1}{\sqrt{3}} & \dfrac{2}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & -\dfrac{2}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \end{bmatrix}}_{V} \underbrace{\begin{bmatrix} 6 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{bmatrix}}_{\Lambda} \underbrace{\left( \begin{bmatrix} \dfrac{1}{\sqrt{3}} & \dfrac{2}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & -\dfrac{2}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \end{bmatrix} \right)^{-1}}_{V^{-1}}$$

Note that $$V$$ is **not** an orthogonal matrix.

1. Why is the above statement **not** a contradiction of the spectral theorem?
2. What is the name of the process that allows us to convert a collection of vectors into an orthonormal basis?
3. Find matrices $$Q$$ and $$\Lambda$$ such that $$A = Q \Lambda Q^T$$.

---

### Problem 13

Recall, a symmetric matrix $$A$$ is positive semidefinite if $$\vec v^T A \vec v \geq 0$$ for all $$\vec v \in \mathbb{R}^n$$.

1. Are all positive semidefinite matrices invertible?
1. Are all positive semidefinite matrices diagonalizable?
1. If we change positive semidefinite to positive definite, how do the answers to the previous statements change?
1. Fill in the blanks: A symmetric matrix $$A$$ is positive semidefinite if and only if all of its eigenvalues are ________.
1. Draw a Venn diagram of the relationship between the following sets of square matrices: positive semidefinite, positive definite, symmetric, diagonalizable, and invertible.

---

### Problem 14

Consider the function

$$f(x, y) = \frac{8xy + 15y^2}{x^2 + y^2}$$

visualized [here on Desmos](https://www.desmos.com/3d/qzawsle26j).

The goal of this problem is to find the minimum and maximum values of $$f(x, y)$$, **without** taking any partial derivatives. You might want to review [this section](https://notes.eecs245.org/eigenvalues/principal-components-analysis/#the-rayleigh-quotient) of Chapter 5.4.

1. Write the numerator of $$f(x, y)$$ as a quadratic form, $$\vec x^T A \vec x$$, where $$\vec x = \begin{bmatrix} x \\ y \end{bmatrix}$$ and $$A$$ is a $$2 \times 2$$ matrix.
1. Using the quadratic form, find the minimum and maximum values of $$f(x, y)$$.
1. There are infinitely many points that minimize $$f(x, y)$$ and infinitely many points that maximize $$f(x, y)$$. Where do these points lie?

---

## Singular Value Decomposition

**Note**: None of these questions are of the form "find the singular value decomposition of a matrix"; you can find problems like those in [Chapter 5.3](https://notes.eecs245.org/eigenvalues/singular-value-decomposition/#examples) and in Homework 11. Make sure to practice those too.

### Problem 15

Suppose the $$2 \times 3$$ matrix $$A$$ has the singular value decomposition $$A = U \Sigma V^T$$ where

- $$U = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$
- $$\Sigma = \begin{bmatrix} 5 & 0 & 0 \\ 0 & 2 & 0 \end{bmatrix}$$
- $$\vec v_1$$, the first column of $$V$$, is $$\begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{bmatrix}$$

Find $$A$$.

---

### Problem 16

Consider the rank-$$2$$ matrix $$A = \begin{bmatrix} 1 & 2 & 2 \\ 1 & 3 & 3 \end{bmatrix}$$.

1. Write $$A$$ as a sum of two rank-1 outer products, e.g. $$A = \vec x_1 \vec y_1^T + \vec x_2 \vec y_2^T$$.
1. Find $$AA^T$$ and $$A^TA$$, and the trace and determinant of each.
1. If $$A$$ is any $$n \times d$$ matrix, which of the following are guaranteed to be true, and why?

- $$\text{trace}(AA^T) = \text{trace}(A^TA)$$
- $$\text{det}(AA^T) = \text{det}(A^TA)$$

---

### Problem 17

Suppose $$X$$ is a symmetric $$n \times n$$ matrix with singular value decomposition $$X = U \Sigma V^T$$. (Note that we are assuming $$X$$ is square, which isn't typically the case for the singular value decomposition.

Show that the diagonal entries of $$\Sigma$$ are the **absolute values** of the eigenvalues of $$X$$.

---

### Problem 18

To find the singular values of $$X$$, we take the square roots of the non-zero eigenvalues of $$X^TX$$ (which are the same as the non-zero eigenvalues of $$XX^T$$).

$$\sigma_i = \sqrt{\lambda_i}$$

Why is it guaranteed that the eigenvalues of $$X^TX$$ are non-negative? (Hint: What does this have to do with [Problem 13](#problem-13)?)

---

### Problem 18

Suppose $$X = U \Sigma V^T$$ is the singular value decomposition of some $$n \times d$$ matrix $$X$$. Furthermore, suppose the columns of $$U$$ are $$\vec u_1, \vec u_2, \ldots, \vec u_n \in \mathbb{R}^n$$, the singular values of $$X$$ are $$\sigma_1, \sigma_2, \ldots, \sigma_r > 0$$, the columns of $$V^T$$ are $$\vec v_1, \vec v_2, \ldots, \vec v_d \in \mathbb{R}^d$$, and $$r = \text{rank}(X)$$.

Earlier in the semester, we saw that the matrix $$\vec a \vec b^T + \vec c \vec e^T$$ had a rank of 1 **or** 2.

Why is it **guaranteed** that the matrix $$\sigma_1 \vec u_1 \vec v_1^T + \sigma_2 \vec u_2 \vec v_2^T$$ has a rank of **exactly** 2?

---

### Problem 19

Give the SVD of a matrix, mostly about low-rank approximation.

- Frobenius norm of the difference

---

### Problem 20

Suppose $$X$$ is a $$5 \times 2$$ matrix with singular value decomposition $$X = U \Sigma V^T$$.

Suppose $$\vec v_1$$ and $$\vec v_2$$ are the first and second columns of $$V$$, respectively. Furthermore, suppose $$\vec w \in \mathbb{R}^2$$ is a vector such that

$$\vec w = 3 \vec v_1 - \vec v_2$$

**Problem 20.1

Find $$V^T \vec w$$.

**Problem 20.2

Suppose $$X$$'s two singular values are $$\sigma_1 = 10$$ and $$\sigma_2 = 3$$.

Find $$\Sigma V^T \vec w$$.

**Problem 20.3

Let $$\vec z = \Sigma V^T \vec w$$. Give English interpretations of $$\vec z$$ and $$U \vec z$$.

---

### Problem 21

Let $$X = U \Sigma V^T$$ be singular value decomposition of some $$n \times d$$ matrix $$X$$, and let $$P = U \Sigma$$. Suppose we compute the singular value decomposition of $$P$$ into

$$P = U_P \Sigma_P V_P^T$$

What is $$V_P^T$$? Justify your answer **conceptually**, not just algebraically. *Hint: What is $$P^TP$$ in terms of $$U$$ and $$\Sigma$$?*

---

## Principal Components Analysis

### Problem 22

In Homework 11, Problem 4 (and in Chapter 5.4), we plotted a 2-dimensional representation of a higher-dimensional dataset.

Fill in the blanks: to create this plot, we plotted the first 2 __(i)__ of __(ii)__.

1. (i) rows / columns
2. (ii) $$\tilde X$$ / $$U$$ / $$V$$ / $$V^T$$ / $$U \Sigma$$ / $$\Sigma V^T$$ / $$U \Sigma V^T$$

---

### Problem 23

Suppose $$X$$ is a $$51 \times 5$$ matrix, whose **first 3 rows** are given by

$$\text{first 3 rows of } X = \begin{bmatrix} 3 & 12 & 5 & 1 & 5 \\ 3 & 4 & 8 & 2 & 1 \\ 1 & 2 & 7 & 2 & 1 \end{bmatrix}$$

Consider the following information about the columns of $$X$$.

| | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
|---|---|---|---|---|---|
| Mean | 2 | 3 | 10 | 5 | 1 |
| Variance | 0.3 | 0.3 | _ | 0.3 | 0.3 |

Let $$\tilde X$$ be the centered version of $$X$$, and let $$\tilde X = U \Sigma V^T$$ be the singular value decomposition of $$\tilde X$$.

Suppose the values along the diagonal of $$\Sigma$$ are $$9$$, $$4$$, $$2$$, $$1$$, and $$0$$.

**Problem 23.1

What is $$\text{rank}(X)$$? Give your answer as an integer.

**Problem 23.2

What proportion of the total variance in $$X$$ is accounted for by the second principal component? Give your answer as a fraction.

**Problem 23.3

We want to choose the first $$k$$ principal components, such that at least $$95\%$$ of the variance in $$X$$ is accounted for. What is the smallest possible value of $$k$$ that we can choose?

**Problem 23.4

Notice that the table provided does not include the variance of column $$3$$. Given all the information above, what is the variance of column $$3$$?

**Problem 23.5

Suppose $$\vec v_3 = \begin{bmatrix} 4/5 \\ 3/5 \\ 0 \\ 0 \\ 0 \end{bmatrix}$$ is the third column of $$V$$.

What is the **first entry** of $$\vec u_3$$, the third column of $$U$$? *Hint: Remember that $$U \Sigma V^T$$ is the singular value decomposition of $$\tilde X$$, not $$X$$.*

**Problem 23.6

Prove that the entries of $$\tilde X \vec w$$ sum to 0, for any $$\vec w \in \mathbb{R}^5$$.

**Problem 23.7

[Image placeholder: pc-4-plots.png]

---

### Problem 24

Let $$X$$ be a $$20 \times 3$$ matrix, let $$\tilde X$$ be the centered version of $$X$$, and let $$\tilde X = U \Sigma V^T$$ be the singular value decomposition of $$\tilde X$$.

Suppose the variances of the 3 columns of $$\tilde X$$ are $$125$$, $$20$$, and $$5$$, respectively. What is the **smallest possible value** of $$\sigma_1$$, the largest singular value of $$\tilde X$$?

---

### Problem 25

Suppose $$A$$, $$B$$, and $$C$$ are each $$100 \times 2$$ matrices, representing $$n = 100$$ points in $$\mathbb{R}^2$$. The three datasets are shown in the scatter plots below. (Matrix $$A$$ is in Plot A, matrix $$B$$ is in Plot B, and matrix $$C$$ is in Plot C.)

[Image placeholder: pc-3-plots.png]

Assume that $$A$$, $$B$$, and $$C$$ are each already centered.

**Problem 25.1

---

### Problem 26

Two columns, correlation $$r$$ and standard deviations.