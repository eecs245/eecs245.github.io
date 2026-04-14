---
layout: page
title: Post-Midterm 2 Practice Problems
description: Practice problems for the content introduced after Midterm 2.
nav_exclude: true
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

# Post-Midterm 2 Practice Problems

_last updated on April 13, 2026 at 3:15PM_

This page contains several practice problems for content introduced after Midterm 2. They are sorted by topic:

- Problems 1-14 are on [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors).
- Problems 15-18 are on the [Singular Value Decomposition](#singular-value-decomposition).
- Problems 19-21 are on [Principal Components Analysis](#principal-components-analysis).

The problems range in difficulty, and aren't necessarily indicative of the difficulty or styles of problems you will see on the real exam; some problems are more open-ended than we'd ask on an exam, and are designed to encourage you to review parts of the course notes.

As we're able to, we will embed videos to certain problems here. A few have already been embedded below.

---

## Eigenvalues and Eigenvectors

### Problem 1

Let

$$A = \begin{bmatrix} 3 & -1 & 1 \\ 0 & 5 & 4 \\ 0 & 0 & 5 \end{bmatrix}$$

Find the eigenvalues and eigenvectors of $$A$$. If $$A$$ is diagonalizable, write it in the form $$A = V \Lambda V^{-1}$$, and if it is not, explain why not.

<details markdown="1"><summary>Solution</summary>

Since $$A$$ is upper triangular, its eigenvalues are the entries on its diagonal: $$3$$, $$5$$, and $$5$$.

For $$\lambda = 3$$,

$$A - 3I = \begin{bmatrix} 0 & -1 & 1 \\ 0 & 2 & 4 \\ 0 & 0 & 2 \end{bmatrix}$$

We're looking for vectors in the null space of $$A - 3I$$. $$\text{rank}(A - 3I) = 2$$, so $$\text{dim}(\text{nullsp}(A - 3I)) = 1$$; since $$A - 3I$$'s first column is $$\vec 0$$, the null space is spanned by $$\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$$.

$$\text{nullsp}(A - 3I) = \text{span}\left(\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \right\} \right)$$

For $$\lambda = 5$$,

$$A - 5I = \begin{bmatrix} -2 & -1 & 1 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$$

Again, $$\text{rank}(A - 5I) = 2$$, so $$\text{dim}(\text{nullsp}(A - 5I)) = 1$$. Since $$A$$'s first column is double its second column, $$\text{nullsp}(A - 5I)$$ is spanned by $$\begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix}$$.

$$\text{nullsp}(A - 5I) = \text{span}\left(\left\{ \begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix} \right\}\right)$$

The eigenvalue $$5$$ has algebraic multiplicity 2 but geometric multiplicity 1, so $$A$$ is **not** diagonalizable.

</details>

---

### Problem 2

Suppose $$A$$ is a $$3 \times 3$$ matrix such that the eigenspace for $$\lambda = 1$$ is the line spanned by $$\begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$, and the eigenspace for $$\lambda = -5$$ is the plane $$2x - 3y + 4z = 0$$.

1. Why is $$A$$ diagonalizable?
2. Find matrices $$V$$ and $$\Lambda$$ such that $$A = V \Lambda V^{-1}$$.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/tGyqgj-378U?si=J5ydwrAqTIiZuKAF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

<details markdown="1"><summary>Solution</summary>

The eigenspace for $$\lambda = 1$$ is 1-dimensional, and the eigenspace for $$\lambda = -5$$ is a plane, so it is 2-dimensional. That gives us 3 linearly independent eigenvectors in $$\mathbb{R}^3$$, which is exactly what we need for diagonalizability.

One eigenvector for $$\lambda = 1$$ is

$$\vec v_1 = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$

To find two eigenvectors in the plane $$2x - 3y + 4z = 0$$, we can choose convenient values:

- If $$y = 2$$ and $$z = 0$$, then $$x = 3$$, so one choice is $$\vec v_2 = \begin{bmatrix} 3 \\ 2 \\ 0 \end{bmatrix}$$
- If $$y = 0$$ and $$z = 1$$, then $$x = -2$$, so another choice is $$\vec v_3 = \begin{bmatrix} -2 \\ 0 \\ 1 \end{bmatrix}$$

So one valid answer is

$$V = \begin{bmatrix} 1 & 3 & -2 \\ 2 & 2 & 0 \\ 2 & 0 & 1 \end{bmatrix}, \qquad \Lambda = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -5 & 0 \\ 0 & 0 & -5 \end{bmatrix}$$

</details>

---

### Problem 3

In each part, answer the following questions about the $$n \times n$$ matrix $$A$$:

- What is the value of $$n$$?
- Is $$A$$ invertible?
- Is $$A$$ diagonalizable, or is it impossible to tell?

1. $$A$$ has characteristic polynomial $$p(\lambda) = \lambda^3 - 16\lambda$$.

2. $$A$$ has characteristic polynomial $$p(\lambda) = (2 - \lambda)(4 - \lambda)(5 - \lambda)^2$$.

<details markdown="1"><summary>Solution</summary>

**Part 1**

$$p(\lambda) = \lambda^3 - 16\lambda = \lambda(\lambda - 4)(\lambda + 4)$$

So:

- $$n = 3$$, since the characteristic polynomial has degree 3.
- $$A$$ is **not** invertible, since $$0$$ is an eigenvalue.
- $$A$$ **is** diagonalizable, since it has 3 distinct eigenvalues.

<br>

**Part 2**

$$p(\lambda) = (2 - \lambda)(4 - \lambda)(5 - \lambda)^2$$

So:

- $$n = 4$$, since the characteristic polynomial has degree 4.
- $$A$$ **is** invertible, since none of its eigenvalues are 0.
- It is **impossible to tell** whether $$A$$ is diagonalizable. The repeated eigenvalue $$5$$ has algebraic multiplicity 2, but its eigenspace could be either 1-dimensional or 2-dimensional.

</details>

---

### Problem 4

Suppose $$A$$ is an $$n \times n$$ matrix with characteristic polynomial $$p(\lambda) = \lambda^3 (2 - \lambda)(4 - \lambda)$$.

Fill in the blank: $$A$$ is diagonalizable if and only if $$\text{rank}(A) = \_\_\_\_$$.

<center><iframe width="640" height="360" src="https://www.loom.com/embed/16e913f28c0140999769f34d52cf719e" title="Problem 4 solution video" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></center>

<details markdown="1"><summary>Solution</summary>

The eigenvalue $$0$$ has algebraic multiplicity 3, while $$2$$ and $$4$$ each have algebraic multiplicity 1. So $$A$$ is diagonalizable if and only if the eigenspace for $$\lambda = 0$$ has dimension 3, since this would mean the geometric multiplicity of each eigenvalue is equal to its algebraic multiplicity.

But the eigenspace for $$\lambda = 0$$ is just $$\text{nullsp}(A)$$. So we need

$$\text{dim}(\text{nullsp}(A)) = 3$$

By rank-nullity, that means

$$\text{rank}(A) = 5 - 3 = 2$$

So, $$A$$ is invertible if and only if $$\text{rank}(A) = 2$$, and the blank is $$\boxed{2}$$.

</details>

---

### Problem 5

Suppose $$A$$ is a $$2 \times 2$$ matrix with characteristic polynomial $$p(\lambda)$$, where $$p(0) = 0$$ and $$p(1) = -5$$.

Find two possible matrices $$A$$.

<details markdown="1"><summary>Solution</summary>

For a $$2 \times 2$$ matrix,

$$p(\lambda) = \lambda^2 - \text{trace}(A)\lambda + \det(A)$$

Notice this means that $$p(0) = \text{det}(A)$$. Since we were told that $$p(0) = 0$$, we have $$\text{det}(A) = 0$$, meaning $$A$$ is not invertible, and 0 is one of its eigenvalues.

Furthermore,

$$p(1) = 1 - \text{trace}(A) + \text{det}(A) = 1 - \text{trace}(A) + \text{det}(A) = -5$$

so for this matrix, $$\text{trace}(A) = 6$$.

That means we just need a non-invertible $$2 \times 2$$ matrix with $$\text{trace}(A) = 6$$. Here are two possible answers:

$$A = \begin{bmatrix} 6 & 0 \\ 0 & 0 \end{bmatrix}, \qquad A = \begin{bmatrix} 1 & 5 \\ 1 & 5 \end{bmatrix}$$

There are plenty of other possible answers too.

</details>

---

### Problem 6

Suppose $$A$$ is a diagonalizable $$3 \times 3$$ matrix with eigenvalue decomposition $$A = V \Lambda V^{-1}$$.

Suppose $$\vec v_1$$, $$\vec v_2$$, and $$\vec v_3$$ are the columns of $$V$$, and suppose $$\vec x \in \mathbb{R}^3$$ is some other vector such that

$$x = 3 \vec v_1 - 2 \vec v_2 + 4 \vec v_3, \qquad A \vec x = 15 \vec v_1 - 8 \vec v_3$$

1. Why is it guaranteed that no other linear combination of $$\vec v_1$$, $$\vec v_2$$, and $$\vec v_3$$ can equal $$\vec x$$?

2. Find $$V^{-1} \vec x$$.

3. What are the eigenvalues of $$A$$?

<center><iframe width="640" height="360" src="https://www.loom.com/embed/ffc2db21fe4a4c0892d8de7ec5dfbde5" title="Problem 6 solution video" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></center>

<details markdown="1"><summary>Solution</summary>

Since $$A$$ is diagonalizable, the columns of $$V$$ – which are the eigenvectors of $$A$$ – are linearly independent. So $$\vec v_1, \vec v_2, \vec v_3$$ form a basis for $$\mathbb{R}^3$$, and coordinates in a basis are unique (i.e, the linear combinations of linearly independent vectors are unique). That is why no other linear combination of these three vectors can equal $$\vec x$$.

Because $$V$$ has columns $$\vec v_1, \vec v_2, \vec v_3$$, the vector $$V^{-1}\vec x$$ contains the coefficients on the basis vectors $$\vec v_1, \vec v_2, \vec v_3$$ that sum to $$\vec x$$:

$$V^{-1}\vec x = \begin{bmatrix} 3 \\ -2 \\ 4 \end{bmatrix}$$

Now, note that

$$
\begin{align*}
A \vec x &= A(3 \vec v_1 - 2 \vec v_2 + 4 \vec v_3) \\
         &= 3A\vec v_1 - 2A\vec v_2 + 4A\vec v_3 \\
         &= 3\lambda_1 \vec v_1 - 2\lambda_2 \vec v_2 + 4\lambda_3 \vec v_3
\end{align*}
$$

But we were also told that

$$A \vec x = 15 \vec v_1 - 8 \vec v_3$$

Matching coefficients gives

$$3\lambda_1 = 15,\qquad -2\lambda_2 = 0,\qquad 4\lambda_3 = -8,$$

so

$$\lambda_1 = 5,\qquad \lambda_2 = 0,\qquad \lambda_3 = -2$$

</details>

---

### Problem 7

Identify whether each of the following statements is true or false, and justify your answer.

1. If $$A$$ is upper triangular, then $$A$$ is diagonalizable.
1. Every $$13 \times 13$$ matrix has at least one real eigenvalue.
1. There exists a $$7 \times 7$$ matrix with an eigenvalue $$\lambda$$ with algebraic multiplicity $$\text{AM}(\lambda) = 3$$ and geometric multiplicity $$\text{GM}(\lambda) = 4$$.
1.  There exists a non-zero $$7 \times 7$$ matrix with an eigenvalue of $$0$$ with geometric multiplicity $$\text{GM}(0) = 7$$.
1. If two matrices have the same characteristic polynomial, then either they are both diagonalizable, or they are both not diagonalizable.

<details markdown="1"><summary>Solution</summary>

1. **False.** For example, $$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$ is upper triangular but not diagonalizable.
2. **True.** A $$13 \times 13$$ matrix has a degree-13 characteristic polynomial, and every odd-degree real polynomial has at least one real root. Remember that odd-degree polynomials have tails in opposite directions, so they must cross the x-axis at least once.
3. **False.** Geometric multiplicity can never exceed algebraic multiplicity.
4. **False.** If $$\text{GM}(0) = 7$$ for a $$7 \times 7$$ matrix, then $$\text{dim}(\text{nullsp}(A)) = 7$$, so $$A\vec x = \vec 0$$ for every vector $$\vec x$$. That forces $$A = 0_{7 \times 7}$$.
5. **False.** The matrices $$I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$ and $$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$ have the same characteristic polynomial, $$p(\lambda) = (1-\lambda)^2$$, but only the first is diagonalizable.

</details>

---

### Problem 8

Suppose $$A$$ and $$B$$ are both $$2 \times 2$$ matrices with an eigenvalue of $$5$$.

1. Is $$AB$$ also guaranteed to have an eigenvalue of $$5$$?
2. Is $$A + B$$ also guaranteed to have an eigenvalue of $$5$$?

<details markdown="1"><summary>Solution</summary>

1. **No.** For example, let 

    $$A = 5I = \begin{bmatrix} 5 & 0 \\ 0 & 5 \end{bmatrix}, \qquad B = \begin{bmatrix} 5 & 0 \\ 0 & 0 \end{bmatrix}$$

    Both matrices have eigenvalue $$5$$, but
    $$AB = \begin{bmatrix} 25 & 0 \\ 0 & 0 \end{bmatrix}$$
    whose eigenvalues are $$25$$ and $$0$$.

2. **No.** Take $$A = B = 5I$$. Then $$A + B = 10I$$, whose only eigenvalue is 10.

</details>

---

### Problem 9

1. Suppose $$A$$ has an eigenvalue of $$\lambda$$. Show that $$A^k$$ has an eigenvalue of $$\lambda^k$$ with the same eigenvector.
1. The converse of the statement above is false --- that is, just because $$A^k$$ has an eigenvalue of $$\lambda^k$$, it does not mean $$A$$ has an eigenvalue of $$\lambda$$. Find a counterexample, by finding a matrix $$A$$ such that $$A^2$$ has an eigenvalue of $$-1$$ such that $$A$$ has no real eigenvalues. Is $$A$$ diagonalizable?

<details markdown="1"><summary>Solution</summary>

**Part 1**

If $$A\vec v = \lambda \vec v$$, then

$$A^2 \vec v = A(A\vec v) = A(\lambda \vec v) = \lambda A\vec v = \lambda^2 \vec v$$

Repeating this same argument gives

$$A^k \vec v = \lambda^k \vec v$$

So $$A^k$$ has eigenvalue $$\lambda^k$$ with the same eigenvector.

<br>

**Part 2**

Now, we need to show that the converse of the statement in Part 1 is false. That is, we need to find a matrix $$A$$ such that $$A^2$$ has an eigenvalue of $$-1$$, but $$A$$ has no real eigenvalues.

For a counterexample, take

$$A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$

Then

$$A^2 = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix} = -I,$$

so $$A^2$$ has eigenvalue $$-1$$. But $$A$$ has no real eigenvalues; its eigenvalues are $$i$$ and $$-i$$.

The source of the issue is that $$A$$ is not diagonalizable, since it does not even have a real eigenvector. (What linear transformation does $$A$$ represent?)

</details>

---

### Problem 10

Let $$A = \begin{bmatrix} 1 & 3 \\ 3 & 1 \end{bmatrix}$$.

1. What is the name of the theorem that guarantees that $$A$$ is diagonalizable?
1. What does that theorem say about the eigenvectors of $$A$$?

<details markdown="1"><summary>Solution</summary>

The theorem is the **spectral theorem**.

It says that every real symmetric matrix is diagonalizable by an orthogonal matrix, i.e.

$$A = Q \Lambda Q^T$$
where $$Q$$ is an orthogonal matrix and $$\Lambda$$ is a diagonal matrix with the eigenvalues of $$A$$ on the diagonal.

The key is that eigenvectors of $$A$$ corresponding to different eigenvalues are orthogonal. (For the same eigenvalue, eigenvectors are not necessarily orthogonal, but they can be chosen to be, using Gram-Schmidt for instance.)

This means that for any real-valued symmetric matrix $$A$$, there exists an orthogonal matrix $$Q$$ whose columns are the eigenvectors of $$A$$.

</details>

---

### Problem 11

Prove that if $$\vec u$$ and $$\vec v$$ are eigenvectors of the symmetric matrix $$S$$ corresponding to different eigenvalues, then $$\vec u$$ and $$\vec v$$ are orthogonal. This is the essence of the spectral theorem.

<details markdown="1"><summary>Solution</summary>

Suppose

$$S\vec u = \lambda \vec u, \qquad S\vec v = \mu \vec v,$$

with $$\lambda \neq \mu$$. Since $$S$$ is symmetric, $$S^T = S$$. Now compute $$\vec u^T S \vec v$$ in two ways:

$$\vec u^T S \vec v = \vec u^T (\mu \vec v) = \mu \vec u^T \vec v,$$

and also

$$\vec u^T S \vec v = (S\vec u)^T \vec v = (\lambda \vec u)^T \vec v = \lambda \vec u^T \vec v$$

So

$$\lambda \vec u^T \vec v = \mu \vec u^T \vec v$$

Rearranging gives

$$(\lambda - \mu)\vec u^T \vec v = 0$$

Since $$\lambda \neq \mu$$, it must be the case that $$\vec u^T \vec v = 0$$. Therefore, $$\vec u$$ and $$\vec v$$ are orthogonal.

This proof was also in [Chapter 9.5](https://notes.eecs245.org/eigenvalues-and-eigenvectors/symmetric-matrices-spectral-theorem/#the-spectral-theorem).

</details>

---

### Problem 12

Consider the **symmetric** matrix $$A = \begin{bmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{bmatrix}$$. $$A$$ can be diagonalized into $$A = V \Lambda V^{-1}$$ as follows:

$$\underbrace{\begin{bmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{bmatrix}}_{A} = \underbrace{\begin{bmatrix} \dfrac{1}{\sqrt{3}} & \dfrac{2}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & -\dfrac{2}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \end{bmatrix}}_{V} \underbrace{\begin{bmatrix} 6 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{bmatrix}}_{\Lambda} \underbrace{\left( \begin{bmatrix} \dfrac{1}{\sqrt{3}} & \dfrac{2}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & -\dfrac{2}{\sqrt{6}} \\ \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & \dfrac{1}{\sqrt{6}} \end{bmatrix} \right)^{-1}}_{V^{-1}}$$

Note that $$V$$ is **not** an orthogonal matrix.

1. Why is the above statement **not** a contradiction of the spectral theorem?
2. What is the name of the process that allows us to convert a collection of vectors into an orthonormal basis?
3. Find matrices $$Q$$ and $$\Lambda$$ such that $$A = Q \Lambda Q^T$$.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/XDR_4bTFZ6s?si=dO_jrIhUeKum9Q6G" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

<details markdown="1"><summary>Solution</summary>

This is not a contradiction of the spectral theorem because the spectral theorem says that a symmetric matrix can be diagonalized by an orthogonal matrix. It does **not** say that every possible eigenvector matrix has to be orthogonal. Put another way, it guarantees that the eigenvectors for **different** eigenvalues are orthogonal, but within the eigenspace for one particular eigenvalue, the eigenvectors are not always orthogonal: you need to pick them to be.

Here, the eigenvalue $$3$$ has multiplicity 2, so there are many possible bases for its eigenspace. Some of those bases are orthogonal, and some are not. The columns of the given $$V$$ happen to be eigenvectors, but columns 2 and 3 are not orthogonal.

The process that converts a linearly independent set into an orthonormal set with the same span is the **Gram-Schmidt process**. Here, we just need to apply it to the last two columns of $$V$$, which span the eigenspace for eigenvalue $$3$$. (The first column of $$V$$ corresponds to eigenvalue $$6$$, and is already orthogonal to the other two, and is already a unit vector.)

If we let $$\vec v_2 = \begin{bmatrix} \frac{2}{\sqrt{6}} \\ -\frac{1}{\sqrt{6}} \\ -\frac{1}{\sqrt{6}} \end{bmatrix}$$ and $$\vec v_3 = \begin{bmatrix} \frac{1}{\sqrt{6}} \\ -\frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \end{bmatrix}$$, a vector in $$\text{span}\left(\left\{ \vec v_2, \vec v_3 \right\}\right)$$ that is orthogonal to $$\vec v_2$$ is the error of the projection of $$\vec v_3$$ onto $$\vec v_2$$ (this is all Gram-Schmidt does):

$$\text{error} = \vec v_3 - \text{proj}_{\vec v_2}(\vec v_3) = \vec v_3 - \frac{\vec v_2 \cdot \vec v_3}{\vec v_2 \cdot \vec v_2} \vec v_2 = \vec v_3 - \frac{1}{2} \vec v_2 = \begin{bmatrix} 0 \\ -\frac{3}{2 \sqrt{6}} \\ \frac{3}{2 \sqrt{6}} \end{bmatrix}$$

To construct $$Q$$, we set the first column to be $$\vec v_1$$, the second column to be $$\vec v_2$$, and the third column to be this new vector we found. So,

$$Q = \begin{bmatrix} \dfrac{1}{\sqrt{3}} & \dfrac{2}{\sqrt{6}} & 0 \\[1em] \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & -\dfrac{3}{2\sqrt{6}} \\[1em] \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} & \dfrac{3}{2\sqrt{6}} \end{bmatrix}$$

$$\Lambda$$ is the same as in the original problem statement.

</details>

---

### Problem 13

Recall, a symmetric matrix $$A$$ is positive semidefinite if $$\vec v^T A \vec v \geq 0$$ for all $$\vec v \in \mathbb{R}^n$$.

1. Are all positive semidefinite matrices invertible?
1. Are all positive semidefinite matrices diagonalizable?
1. If we change positive semidefinite to positive definite, how do the answers to the previous statements change?
1. Fill in the blanks: A symmetric matrix $$A$$ is positive semidefinite if and only if all of its eigenvalues are ________.
1. Draw a Venn diagram of the relationship between the following sets of square matrices: positive semidefinite, positive definite, symmetric, diagonalizable, and invertible.

<center><iframe width="640" height="360" src="https://www.loom.com/embed/aea647a2947c4fefa5439afe0fc6acb5" title="Problem 13 solution video" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></center>

<details markdown="1"><summary>Solution</summary>

1. Are all positive semidefinite matrices invertible? **No.** The zero matrix is positive semidefinite, since $$\vec v^T 0_{n \times n} \vec v = 0 \geq 0$$ for all $$\vec v \in \mathbb{R}^n$$, but it is not invertible.
2. Are all positive semidefinite matrices diagonalizable? **Yes.** Positive semidefinite matrices are symmetric, and every real symmetric matrix is diagonalizable.
3. If we strengthen this to positive definite, then both answers become **yes**. Positive definite matrices are symmetric, hence diagonalizable, and all of their eigenvalues are strictly positive, so they are invertible (because 0 is guaranteed to not be an eigenvalue).
4. A symmetric matrix $$A$$ is positive semidefinite if and only if all of its eigenvalues are **non-negative**.
5. The video above draws the Venn diagram.

</details>

---

### Problem 14

Consider the function

$$f(x, y) = \frac{8xy + 15y^2}{x^2 + y^2}$$

visualized [here on Desmos](https://www.desmos.com/3d/qzawsle26j).

The goal of this problem is to find the minimum and maximum values of $$f(x, y)$$, **without** taking any partial derivatives. You might want to review [Chapter 9.6](https://notes.eecs245.org/eigenvalues-and-eigenvectors/rayleigh-quotient/).

1. Write the numerator of $$f(x, y)$$ as a quadratic form, $$\vec x^T A \vec x$$, where $$\vec x = \begin{bmatrix} x \\ y \end{bmatrix}$$ and $$A$$ is a $$2 \times 2$$ matrix.
1. Using the quadratic form, find the minimum and maximum values of $$f(x, y)$$.
1. There are infinitely many points that minimize $$f(x, y)$$ and infinitely many points that maximize $$f(x, y)$$. Where do these points lie?

<details markdown="1"><summary>Solution</summary>

We want

$$\vec x^T A \vec x = 8xy + 15y^2$$

So we can take

$$A = \begin{bmatrix} 0 & 4 \\ 4 & 15 \end{bmatrix}$$

since

$$
\begin{align*}
\vec x^T A \vec x = \begin{bmatrix} x & y \end{bmatrix}
\begin{bmatrix} 0 & 4 \\ 4 & 15 \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
&= \begin{bmatrix} x & y \end{bmatrix}
\begin{bmatrix} 0x + 4y \\ 4x + 15y \end{bmatrix} \\
&= 4xy + 4xy + 15y^2 \\
&= 8xy + 15y^2
\end{align*}
$$

That means

$$f(x, y) = \frac{\vec x^T A \vec x}{\vec x^T \vec x}$$

which is a Rayleigh quotient. So its maximum and minimum values are the largest and smallest eigenvalues of $$A$$, as discussed in [Chapter 9.6](https://notes.eecs245.org/eigenvalues-and-eigenvectors/rayleigh-quotient/).

What are those eigenvalues? The characteristic polynomial of $$A$$ is

$$\det(A - \lambda I) = \begin{vmatrix} -\lambda & 4 \\ 4 & 15 - \lambda \end{vmatrix}
= \lambda^2 - 15\lambda - 16$$

so the eigenvalues are

$$\lambda = \frac{15 \pm 17}{2}$$

meaning

$$\lambda_{\max} = 16, \qquad \lambda_{\min} = -1$$

So the maximum value of $$f(x, y)$$ is $$\boxed{16}$$ and the minimum value is $$\boxed{-1}$$. The graph on Desmos corroborates this.

The maximizing points lie on the eigenspace for $$\lambda = 16$$, which is the line $$y = 4x$$ (i.e. the span of the vector $$\begin{bmatrix} 1 \\ 4 \end{bmatrix}$$). The minimizing points lie on the eigenspace for $$\lambda = -1$$, which is the line $$y = -x/4$$ (i.e. the span of the vector $$\begin{bmatrix} 4 \\ -1 \end{bmatrix}$$). Excluding $$ (0,0) $$, every point on those lines gives the corresponding extremum.

</details>

---

## Singular Value Decomposition

**Note**: None of these questions are of the form "find the singular value decomposition of a matrix"; you can find many problems like those in [Chapter 10.1](https://notes.eecs245.org/singular-value-decomposition/computing-svd/) and in Homework 11. Make sure to practice those too.

### Problem 15

Suppose $$X$$ is a symmetric $$n \times n$$ matrix with singular value decomposition $$X = U \Sigma V^T$$. (Note that we are assuming $$X$$ is square, which isn't typically the case for the singular value decomposition.)

Show that the diagonal entries of $$\Sigma$$ are the **absolute values** of the eigenvalues of $$X$$, i.e. $$\sigma_i = \mid \lambda_i \mid$$ for all $$i = 1, 2, ..., \text{rank}(X)$$.

<details markdown="1"><summary>Solution</summary>

Since $$X$$ is symmetric, $$X^T = X$$, so

$$X^T X = X^2$$

If $$\lambda_i$$ is an eigenvalue of $$X$$ with eigenvector $$\vec v_i$$, then

$$X^2 \vec v_i = X(\lambda_i \vec v_i) = \lambda_i X \vec v_i = \lambda_i^2 \vec v_i$$

So the eigenvalues of $$X^T X$$ are the squares of the eigenvalues of $$X$$.

But the singular values of $$X$$ are defined by

$$\sigma_i = \sqrt{\text{eigenvalue}_i(X^T X)}$$

Therefore,

$$\sigma_i = \sqrt{\lambda_i^2} = |\lambda_i|$$

That is exactly what we wanted to show.

</details>

---

### Problem 16

To find the singular values of $$X$$, we take the square roots of the non-zero eigenvalues of $$X^TX$$ (which are the same as the non-zero eigenvalues of $$XX^T$$).

$$\sigma_i = \sqrt{\lambda_i}$$

Why is it guaranteed that the eigenvalues of $$X^TX$$ are non-negative? (Hint: What does this have to do with [Problem 13](#problem-13)?)

<details markdown="1"><summary>Solution</summary>

The matrix $$X^T X$$ is always symmetric. Also, for any vector $$\vec v$$,

$$\vec v^T X^T X \vec v = (X\vec v)^T (X\vec v) = \|X\vec v\|^2 \geq 0$$

So $$X^T X$$ is positive semidefinite.

By Problem 13, every positive semidefinite matrix has non-negative eigenvalues. That is why taking square roots here is always possible.

</details>

---

### Problem 17

Consider the matrix $$X$$ whose singular value decomposition is given by

$$X = \underbrace{\begin{bmatrix} 1/2 & 1/2 & 1/2 & 1/2
\\ 1/2 & 1/2 & -1/2 & -1/2
\\ 1/2 & -1/2 & 1/2 & -1/2
\\ 1/2 & -1/2 & -1/2 & 1/2 \end{bmatrix}}_{U} \underbrace{\begin{bmatrix} 8 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} \sqrt{2}/2 & \sqrt{2}/2 & 0 \\ -\sqrt{2}/2 & \sqrt{2}/2 & 0 \\ 0 & 0 & 1 \end{bmatrix}}_{V^T}$$

1. Find the best rank-1 approximation of $$X$$.
1. Let $$X_1$$ be the matrix you found in the previous part. In Homework 11, Problem 2, you were introduced to the Frobenius norm of a matrix, which can be thought of as the length of the norm of the matrix, if you think of it as one long $$n \times d$$ vector. Explain why the Frobenius norm of $$X - X_1$$ is equal to $$\sqrt{3^2 + 1^2} = \sqrt{10}$$.
1. Find the best rank-2 approximation of $$X$$. There's no need to work out the entire calculation, but make sure you know how to do it.

<details markdown="1"><summary>Solution</summary>

The best rank-1 approximation keeps only the largest singular value:

$$X_1 = \sigma_1 \vec u_1 \vec v_1^T$$

Here,

$$\vec u_1 = \frac{1}{2}\begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}, \qquad
\vec v_1^T = \begin{bmatrix} \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \end{bmatrix}, \qquad
\sigma_1 = 8$$

So

$$X_1 = 8 \vec u_1 \vec v_1^T
= \begin{bmatrix}
2\sqrt{2} & 2\sqrt{2} & 0 \\
2\sqrt{2} & 2\sqrt{2} & 0 \\
2\sqrt{2} & 2\sqrt{2} & 0 \\
2\sqrt{2} & 2\sqrt{2} & 0
\end{bmatrix}$$

Now,

$$X - X_1 = 3\vec u_2 \vec v_2^T + 1 \vec u_3 \vec v_3^T$$

These two rank-1 pieces are orthogonal to each other in the Frobenius inner product, because the left singular vectors are orthonormal and the right singular vectors are orthonormal. So their squared Frobenius norms add:

$$\|X - X_1\|_F^2 = 3^2 + 1^2 = 10,$$

which means

$$\|X - X_1\|_F = \sqrt{10}$$

The best rank-2 approximation is

$$X_2 = \sigma_1 \vec u_1 \vec v_1^T + \sigma_2 \vec u_2 \vec v_2^T$$

If you multiply that out, you get

$$X_2 =
\begin{bmatrix}
\frac{5\sqrt{2}}{4} & \frac{11\sqrt{2}}{4} & 0 \\
\frac{5\sqrt{2}}{4} & \frac{11\sqrt{2}}{4} & 0 \\
\frac{11\sqrt{2}}{4} & \frac{5\sqrt{2}}{4} & 0 \\
\frac{11\sqrt{2}}{4} & \frac{5\sqrt{2}}{4} & 0
\end{bmatrix}$$

</details>

---

### Problem 18

Let $$X = U \Sigma V^T$$ be singular value decomposition of some $$n \times d$$ matrix $$X$$, and let $$P = U \Sigma$$. Suppose we compute the singular value decomposition of $$P$$ into

$$P = U_P \Sigma_P V_P^T$$

What is $$V_P^T$$? Justify your answer **conceptually**, not just algebraically. *Hint: What is $$P^TP$$ in terms of $$U$$ and $$\Sigma$$?*

<details markdown="1"><summary>Solution</summary>

The answer is

$$V_P^T = I$$

up to the usual harmless ambiguity in any zero-singular-value directions.

Here is the conceptual reason. In the factorization

$$X = U \Sigma V^T,$$

the matrix $$V^T$$ is the part that rotates the standard coordinate directions into the right-singular-vector directions of $$X$$. But in

$$P = U\Sigma,$$

that rotation is already gone. The columns of $$P$$ are just the columns of $$U$$ scaled by the singular values, with any trailing zero columns left as zero.

That means the "right-side directions" of $$P$$ are already the standard basis directions. Equivalently,

$$P^T P = \Sigma^T U^T U \Sigma = \Sigma^T \Sigma,$$

which is already diagonal, so no additional right-side rotation is needed. Hence the natural choice is $$V_P^T = I$$.

</details>

---

## Principal Components Analysis

### Problem 19

In Homework 11, Problem 4 (and in [Chapter 10.4](https://notes.eecs245.org/singular-value-decomposition/principal-components-analysis/#example-from-mathbb-r-2-to-mathbb-r-2)), we plotted a 2-dimensional representation of a higher-dimensional dataset. Let $$\tilde X$$ be the mean-centered version of the dataset.

Fill in the blanks: to create this plot, we plotted the first 2 __(1)__ of __(2)__.

1. rows / columns
1. $$\tilde X \qquad U \qquad V \qquad V^T \qquad U \Sigma \qquad \Sigma V^T \qquad \tilde X V \qquad U \Sigma V^T$$

(there may be more than one correct answer; identify all of them)

<details markdown="1"><summary>Solution</summary>

The correct choice for blank (1) is **columns**.

The correct choices for blank (2) are

$$U\Sigma \qquad \text{and} \qquad \tilde X V$$

Why? Because the principal component values are

$$\tilde X \vec v_j = \sigma_j \vec u_j,$$

so the $$j$$-th principal component is the $$j$$-th column of both $$\tilde X V$$ and $$U\Sigma$$. Therefore, the 2-dimensional PCA plot comes from the first two **columns** of either of those matrices.

</details>

---

### Problem 20

Suppose $$X$$ is a $$51 \times 5$$ matrix, whose **first 3 rows** are given by

$$\text{first 3 rows of } X = \begin{bmatrix} 3 & 12 & 5 & 1 & 5 \\ 3 & 4 & 8 & 2 & 1 \\ 1 & 2 & 7 & 2 & 1 \end{bmatrix}$$

Consider the following information about the columns of $$X$$.

| | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
|---|---|---|---|---|---|
| Mean | 2 | 3 | 10 | 5 | 1 |
| Variance | 0.3 | 0.3 | _ | 0.3 | 0.3 |

Let $$\tilde X$$ be the mean-centered version of $$X$$, and let $$\tilde X = U \Sigma V^T$$ be the singular value decomposition of $$\tilde X$$.

Suppose the values along the diagonal of $$\Sigma$$ are $$9$$, $$4$$, $$2$$, $$1$$, and $$0$$.

1. What is $$\text{rank}(\tilde X)$$? (Note that in general, **unlike** I accidentally said in Thursday's lecture, $$\text{rank}(\tilde X)$$ is not necessarily equal to $$\text{rank}(X)$$: it is possible for $$\text{rank}(\tilde X)$$ to equal $$\text{rank}(X) - 1$$. Think about why this is the case!)
1. We want to choose the first $$k$$ principal components, such that at least $$95\%$$ of the variance in $$X$$ is accounted for. What is the smallest possible value of $$k$$ that we can choose?
1. Notice that the table provided does not include the variance of column $$3$$. Given all the information above, what is the variance of column $$3$$?
1. Suppose $$\vec v_3 = \begin{bmatrix} 4/5 \\ 3/5 \\ 0 \\ 0 \\ 0 \end{bmatrix}$$ is the third column of $$V$$. What is the **first entry** of $$\vec u_3$$, the third column of $$U$$? *Hint: Remember that $$U \Sigma V^T$$ is the singular value decomposition of $$\tilde X$$, not $$X$$.*
1. Prove that the entries of $$\tilde X \vec w$$ sum to 0, for any $$\vec w \in \mathbb{R}^5$$.
1. Which of these four plots visualizes principal component 2 vs. principal component 1?

<center><img src="../assets/rev-imgs/pc-4-plots.png" alt="Principal component 2 vs. principal component 1" style="width: 50%; height: auto;"></center>

<iframe width="640" height="448" src="https://www.loom.com/embed/c1db77f7a58e4d58add90e555409bab3" title="Problem 20 solution video" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

<details markdown="1"><summary>Solution</summary>

Since the non-zero singular values are $$9, 4, 2, 1$$, the rank is

$$\text{rank}(\tilde X) = 4$$

The proportion of variance explained by the first $$k$$ principal components comes from the squared singular values. Here,

$$9^2 + 4^2 + 2^2 + 1^2 = 81 + 16 + 4 + 1 = 102$$

Using the first principal component alone gives

$$\frac{81}{102} \approx 79.4\%$$

Using the first two gives

$$\frac{81 + 16}{102} = \frac{97}{102} \approx 95.1\%$$

So the smallest possible value of $$k$$ is $$\boxed{2}$$.

Now use the fact that the total variance in $$X$$ equals

$$\frac{1}{n}\sum_{j=1}^r \sigma_j^2 = \frac{102}{51} = 2$$

So the five column variances must add to 2. Four of them are already given:

$$0.3 + 0.3 + 0.3 + 0.3 = 1.2$$

Therefore, the missing variance is

$$2 - 1.2 = 0.8$$

For the next part, the first row of $$\tilde X$$ is

$$\begin{bmatrix} 3-2 & 12-3 & 5-10 & 1-5 & 5-1 \end{bmatrix}
= \begin{bmatrix} 1 & 9 & -5 & -4 & 4 \end{bmatrix}$$

Since $$\tilde X \vec v_3 = \sigma_3 \vec u_3$$ and $$\sigma_3 = 2$$, the first entry of $$\vec u_3$$ should be

$$\frac{1}{2}\begin{bmatrix} 1 & 9 & -5 & -4 & 4 \end{bmatrix}
\begin{bmatrix} 4/5 \\ 3/5 \\ 0 \\ 0 \\ 0 \end{bmatrix}
= \frac{1}{2}\left(\frac{4}{5} + \frac{27}{5}\right)
= \frac{31}{10}$$

So, using the numbers exactly as written, the answer is $$\boxed{31/10}$$. That said, this part appears to have a typo somewhere, since an entry of a unit vector cannot have absolute value larger than 1.

For the fifth part, let $$\vec 1$$ be the length-51 vector of all 1s. Since $$\tilde X$$ is mean-centered, each of its columns sums to 0, which means

$$\vec 1^T \tilde X = \vec 0^T$$

So for any $$\vec w \in \mathbb{R}^5$$,

$$\vec 1^T (\tilde X \vec w) = (\vec 1^T \tilde X)\vec w = \vec 0^T \vec w = 0$$

But $$\vec 1^T (\tilde X \vec w)$$ is exactly the sum of the entries of $$\tilde X \vec w$$, so those entries sum to 0.

For the last part, the correct plot is **Plot D**. In principal component coordinates, the data should be centered at the origin, axis-aligned, and have more spread in PC1 than in PC2 because $$\sigma_1 = 9 > \sigma_2 = 4$$. Plot D is the best match.

</details>

---

### Problem 21

Let $$X$$ be a $$20 \times 3$$ matrix, let $$\tilde X$$ be the centered version of $$X$$, and let $$\tilde X = U \Sigma V^T$$ be the singular value decomposition of $$\tilde X$$.

Suppose the variances of the 3 columns of $$\tilde X$$ are $$125$$, $$20$$, and $$5$$, respectively. What is the **smallest possible value** of $$\sigma_1$$, the largest singular value of $$\tilde X$$?

<details markdown="1"><summary>Solution</summary>

The key is that $$\sigma_1$$ is the largest singular value, so

$$\sigma_1 = \max_{\|\vec v\|=1} \|\tilde X \vec v\|$$

If we choose $$\vec v = \vec e_1$$, the first standard basis vector, then $$\tilde X \vec e_1$$ is just the first column of $$\tilde X$$. So

$$\sigma_1 \geq \|\text{column 1 of } \tilde X\|$$

The variance of column 1 is 125, and there are $$n = 20$$ rows, so

$$\|\text{column 1 of } \tilde X\|^2 = 20 \cdot 125 = 2500$$

Therefore,

$$\sigma_1 \geq \sqrt{2500} = 50$$

This lower bound is achievable if the three columns are orthogonal, since then $$\tilde X^T \tilde X$$ is diagonal with diagonal entries $$2500, 400, 100$$, and the singular values are $$50, 20, 10$$.

So the smallest possible value of $$\sigma_1$$ is $$\boxed{50}$$

</details>

---

<small>Some problems were borrowed from [this site](https://ds100.org/su20/resources).</small>
