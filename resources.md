---
layout: page
title: 📚 Resources
description: Additional resources to supplement the course.
nav_order: 5
---

# 📚 Resources

Here, we'll provide links to past exams, as well as other materials online that contain practice problems and alternative explanations of the course material. Find anything that you think is helpful or interesting? Let us know and we'll add it here.

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

---

## Videos

Several supplemental videos have been recorded for this class, and all of them can be found [here](https://www.youtube.com/@rampureatumich/videos). When relevant, you can find these videos linked in the relevant sections of the course notes, the course homepage, and assignment solutions.

---

## Past Exams

Note that the midterm exams in Fall 2025 were 80 minutes long and administered in lecture, while the midterm exams in Winter 2026 will be 120 minutes (2 hours) long and administered in the evenings. This change was made to give students more time to complete the exam; we plan on making the midterms roughly the same length as they were in Fall 2025.

| Semester | Midterm 1 | Midterm 2 | Final Exam |
| --- | --- | --- | --- |
| Spring 2026 | [Exam](../resources/exams/sp26-mt1.pdf), [Solutions](../resources/exams/sp26-mt1-solutions.pdf) | [Exam](../resources/exams/sp26-mt2.pdf), [Solutions](../resources/exams/sp26-mt2-solutions.pdf) | [Exam](../resources/exams/sp26-final.pdf), [Solutions](../resources/exams/sp26-final-solutions.pdf) |
| Winter 2026 | [Exam](../resources/exams/wn26-mt1.pdf), [Solutions](../resources/exams/wn26-mt1-solutions.pdf), [Videos 🎥](https://www.youtube.com/playlist?list=PLEFTQpsm47qQWmh2Js1moAv8MqQCMEjWx) | [Exam](../resources/exams/wn26-mt2.pdf), [Solutions](../resources/exams/wn26-mt2-solutions.pdf) | [Exam](../resources/exams/wn26-final.pdf), [Solutions](../resources/exams/wn26-final-solutions.pdf) |
| Fall 2025 | [Exam](../resources/exams/fa25-mt1.pdf), [Solutions](../resources/exams/fa25-mt1-solutions.pdf), [Videos 🎥](https://www.youtube.com/playlist?list=PLEFTQpsm47qRjWWjsENcWsxgtgJ2bJAl4) | [Exam](../resources/exams/fa25-mt2.pdf), [Solutions](../resources/exams/fa25-mt2-solutions.pdf) | [Exam](../resources/exams/fa25-final.pdf), [Solutions](../resources/exams/fa25-final-solutions.pdf), [Videos 🎥](https://www.youtube.com/playlist?list=PLEFTQpsm47qS-QgZ2hY-FJkqClfbGu7ds) |
| Mock Exams | [Exam](../resources/exams/mock-mt1.pdf), [Solutions](../resources/exams/mock-mt1-solutions.pdf) | [Exam](../resources/exams/mock-mt2.pdf), [Solutions](../resources/exams/mock-mt2-solutions.pdf) | In lieu of a mock Final Exam, we provided these [Post-Midterm 2 practice problems](../post-mt2-practice) |

### Problems by Topic

Problems are linked based on the chapter they correspond to in the [course notes](https://notes.eecs245.org). Generally, Chapters 1-4 correspond to Midterm 1 and Chapters 5-8 correspond to Midterm 2. If any questions seem miscategorized, let us know.

<style>
.exam-topic-browser {
  display: grid;
  grid-template-columns: 55fr 45fr;
  gap: 1rem;
  margin-top: 0.75rem;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}
.exam-topic-list {
  border: 1px solid #d0d7de;
  border-radius: 3px;
  padding: 0.5rem;
  background: #f6f8fa;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.07), 0 4px 14px rgba(0, 0, 0, 0.05);
}
.exam-topic-btn {
  width: 100%;
  text-align: left;
  border: 0;
  border-radius: 3px;
  padding: 0.55rem 0.65rem;
  margin: 0.2rem 0;
  background: transparent;
  color: #24292f;
  cursor: pointer;
  font: inherit;
}
.exam-topic-btn small {
  display: block;
  margin-top: 0.2rem;
  color: #57606a;
  font-weight: 400;
  line-height: 1.3;
}
.exam-topic-btn:hover {
  background: #eaeef2;
}
.exam-topic-btn.active {
  background: #dbeafe;
  font-weight: 600;
}
.exam-topic-content {
  border: 1px solid #d0d7de;
  border-radius: 3px;
  padding: 0.9rem 1rem;
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.07), 0 4px 14px rgba(0, 0, 0, 0.05);
  width: 100%;
  max-width: 430px;
  justify-self: start;
}
@media (max-width: 900px) {
  .exam-topic-browser {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="exam-topic-browser">
  <div id="exam-topic-list" class="exam-topic-list" aria-label="Notes chapters"></div>
  <div class="exam-topic-content">
    <ul id="exam-topic-links"></ul>
  </div>
</div>

<script>
const examTopics = [
  {
    title: "1. Introduction to Supervised Learning",
    summary: "squared loss and the constant model, absolute loss, comparing loss functions",
    links: [
      ["FA25 MT1 Problem 1", "../resources/exams/fa25-mt1.pdf#page=3"],
      ["FA25 MT1 Problem 2", "../resources/exams/fa25-mt1.pdf#page=4"],
      ["FA25 Final Problem 1", "../resources/exams/fa25-final.pdf#page=3"],
      ["Mock MT1 Problem 1", "../resources/exams/mock-mt1.pdf#page=3"],
      ["Mock MT1 Problem 2", "../resources/exams/mock-mt1.pdf#page=4"],
      ["WN26 MT1 Problem 1", "../resources/exams/wn26-mt1.pdf#page=3"],
      ["WN26 MT1 Problem 7", "../resources/exams/wn26-mt1.pdf#page=10"],
      ["WN26 Final Problem 1", "../resources/exams/wn26-final.pdf#page=3"],
      ["SP26 MT1 Problem 1", "../resources/exams/sp26-mt1.pdf#page=3"],
      ["SP26 MT1 Problem 2", "../resources/exams/sp26-mt1.pdf#page=4"],
      ["SP26 Final Problem 1", "../resources/exams/sp26-final.pdf#page=3"]
    ]
  },
  {
    title: "2. Simple Linear Regression",
    summary: "partial derivatives, finding optimal parameters, correlation",
    links: [
      ["FA25 MT1 Problem 3", "../resources/exams/fa25-mt1.pdf#page=6"],
      ["FA25 Final Problem 2", "../resources/exams/fa25-final.pdf#page=4"],
      ["Mock MT1 Problem 3", "../resources/exams/mock-mt1.pdf#page=6"],
      ["WN26 MT1 Problem 2", "../resources/exams/wn26-mt1.pdf#page=5"],
      ["WN26 Final Problem 2", "../resources/exams/wn26-final.pdf#page=4"],
      ["SP26 MT1 Problem 3", "../resources/exams/sp26-mt1.pdf#page=5"],
      ["SP26 Final Problem 2", "../resources/exams/sp26-final.pdf#page=5"]
    ]
  },
  {
    title: "3. Vectors",
    summary: "vectors and linear combinations, norms, dot product, projecting onto a single vector",
    links: [
      ["FA25 MT1 Problem 4", "../resources/exams/fa25-mt1.pdf#page=7"],
      ["FA25 MT1 Problem 8", "../resources/exams/fa25-mt1.pdf#page=11"],
      ["FA25 Final Problem 3", "../resources/exams/fa25-final.pdf#page=5"],
      ["Mock MT1 Problem 4", "../resources/exams/mock-mt1.pdf#page=7"],
      ["Mock MT1 Problem 7", "../resources/exams/mock-mt1.pdf#page=11"],
      ["WN26 MT1 Problem 4", "../resources/exams/wn26-mt1.pdf#page=7"],
      ["WN26 Final Problem 3", "../resources/exams/wn26-final.pdf#page=5"],
      ["SP26 MT1 Problem 4", "../resources/exams/sp26-mt1.pdf#page=6"],
      ["SP26 MT1 Problem 5", "../resources/exams/sp26-mt1.pdf#page=7"],
      ["SP26 MT1 Problem 9", "../resources/exams/sp26-mt1.pdf#page=11"],
      ["SP26 Final Problem 3", "../resources/exams/sp26-final.pdf#page=7"]
    ]
  },
  {
    title: "4. Linear Independence",
    summary: "span, linear independence, lines/planes/hyperplanes, vector spaces/basis/dimension",
    links: [
      ["FA25 MT1 Problem 6", "../resources/exams/fa25-mt1.pdf#page=9"],
      ["FA25 MT1 Problem 7", "../resources/exams/fa25-mt1.pdf#page=10"],
      ["FA25 Final Problem 4", "../resources/exams/fa25-final.pdf#page=6"],
      ["Mock MT1 Problem 5", "../resources/exams/mock-mt1.pdf#page=9"],
      ["Mock MT1 Problem 6", "../resources/exams/mock-mt1.pdf#page=10"],
      ["WN26 MT1 Problem 6", "../resources/exams/wn26-mt1.pdf#page=9"],
      ["WN26 Final Problem 4", "../resources/exams/wn26-final.pdf#page=6"],
      ["SP26 MT1 Problem 6", "../resources/exams/sp26-mt1.pdf#page=8"],
      ["SP26 MT1 Problem 7", "../resources/exams/sp26-mt1.pdf#page=9"],
      ["SP26 MT1 Problem 8", "../resources/exams/sp26-mt1.pdf#page=10"],
      ["SP26 Final Problem 4", "../resources/exams/sp26-final.pdf#page=9"]
    ]
  },
  {
    title: "5. Matrices",
    summary: "matrix operations, special matrices, rank and column space, null space and rank-nullity",
    links: [
      ["FA25 MT2 Problem 1", "../resources/exams/fa25-mt2.pdf#page=3"],
      ["FA25 MT2 Problem 2", "../resources/exams/fa25-mt2.pdf#page=4"],
      ["FA25 MT2 Problem 3", "../resources/exams/fa25-mt2.pdf#page=6"],
      ["FA25 Final Problem 5", "../resources/exams/fa25-final.pdf#page=7"],
      ["Mock MT2 Problem 1", "../resources/exams/mock-mt2.pdf#page=3"],
      ["Mock MT2 Problem 2", "../resources/exams/mock-mt2.pdf#page=4"],
      ["Mock MT2 Problem 4", "../resources/exams/mock-mt2.pdf#page=8"],
      ["WN26 MT2 Problem 2", "../resources/exams/wn26-mt2.pdf#page=4"],
      ["WN26 MT2 Problem 3", "../resources/exams/wn26-mt2.pdf#page=5"],
      ["WN26 MT2 Problem 5", "../resources/exams/wn26-mt2.pdf#page=7"],
      ["WN26 Final Problem 5", "../resources/exams/wn26-final.pdf#page=6"],
      ["SP26 MT2 Problem 1", "../resources/exams/sp26-mt2.pdf#page=3"],
      ["SP26 MT2 Problem 2", "../resources/exams/sp26-mt2.pdf#page=4"],
      ["SP26 MT2 Problem 3", "../resources/exams/sp26-mt2.pdf#page=6"],
      ["SP26 Final Problem 5", "../resources/exams/sp26-final.pdf#page=9"]
    ]
  },
  {
    title: "6. Linear Transformations and Projections",
    summary: "linear transformations, inverses, projecting onto column space, complete solution to the normal equations",
    links: [
      ["FA25 MT1 Problem 5", "../resources/exams/fa25-mt1.pdf#page=8"],
      ["FA25 MT2 Problem 5", "../resources/exams/fa25-mt2.pdf#page=9"],
      ["Mock MT2 Problem 3", "../resources/exams/mock-mt2.pdf#page=5"],
      ["WN26 MT1 Problem 3", "../resources/exams/wn26-mt1.pdf#page=6"],
      ["WN26 MT1 Problem 5", "../resources/exams/wn26-mt1.pdf#page=8"],
      ["WN26 MT2 Problem 4", "../resources/exams/wn26-mt2.pdf#page=6"],
      ["WN26 Final Problem 6", "../resources/exams/wn26-final.pdf#page=7"],
      ["WN26 Final Problem 5", "../resources/exams/wn26-final.pdf#page=6"],
      ["SP26 MT2 Problem 4", "../resources/exams/sp26-mt2.pdf#page=7"],
      ["SP26 Final Problem 6", "../resources/exams/sp26-final.pdf#page=9"],
      ["SP26 Final Problem 7", "../resources/exams/sp26-final.pdf#page=10"]
    ]
  },
  {
    title: "7. Regression Using Linear Algebra",
    summary: "regression using linear algebra, design matrices",
    links: [
      ["FA25 MT2 Problem 4", "../resources/exams/fa25-mt2.pdf#page=7"],
      ["FA25 Final Problem 8", "../resources/exams/fa25-final.pdf#page=9"],
      ["Mock MT2 Problem 5", "../resources/exams/mock-mt2.pdf#page=9"],
      ["WN26 MT2 Problem 6", "../resources/exams/wn26-mt2.pdf#page=8"],
      ["WN26 Final Problem 7", "../resources/exams/wn26-final.pdf#page=8"],
      ["SP26 MT2 Problem 5", "../resources/exams/sp26-mt2.pdf#page=8"],
      ["SP26 Final Problem 8", "../resources/exams/sp26-final.pdf#page=12"]
    ]
  },
  {
    title: "8. Gradients",
    summary: "gradient vector, gradients + matrix/vector operations, gradient descent, convexity, positive definite matrices",
    links: [
      ["FA25 MT2 Problem 6", "../resources/exams/fa25-mt2.pdf#page=10"],
      ["FA25 MT2 Problem 7", "../resources/exams/fa25-mt2.pdf#page=11"],
      ["FA25 Final Problem 6", "../resources/exams/fa25-final.pdf#page=8"],
      ["FA25 Final Problem 7", "../resources/exams/fa25-final.pdf#page=8"],
      ["Mock MT2 Problem 6", "../resources/exams/mock-mt2.pdf#page=11"],
      ["Mock MT2 Problem 7", "../resources/exams/mock-mt2.pdf#page=12"],
      ["Mock MT2 Problem 8", "../resources/exams/mock-mt2.pdf#page=13"],
      ["WN26 MT2 Problem 7", "../resources/exams/wn26-mt2.pdf#page=10"],
      ["WN26 MT2 Problem 8", "../resources/exams/wn26-mt2.pdf#page=11"],
      ["WN26 Final Problem 8", "../resources/exams/wn26-final.pdf#page=9"],
      ["SP26 MT2 Problem 6", "../resources/exams/sp26-mt2.pdf#page=10"],
      ["SP26 MT2 Problem 7", "../resources/exams/sp26-mt2.pdf#page=11"],
      ["SP26 Final Problem 9", "../resources/exams/sp26-final.pdf#page=14"]
    ]
  },
  {
    title: "9. Eigenvalues and Eigenvectors",
    summary: "eigenvalues and eigenvectors, characteristic polynomial, markov chains + adjacency matrices, multiplicities + diagonalization",
    links: [
      ["FA25 Final Problem 9", "../resources/exams/fa25-final.pdf#page=10"],
      ["FA25 Final Problem 10", "../resources/exams/fa25-final.pdf#page=11"],
      ["FA25 Final Problem 11", "../resources/exams/fa25-final.pdf#page=12"],
      ["WN26 MT2 Problem 1", "../resources/exams/wn26-mt2.pdf#page=3"],
      ["WN26 Final Problem 9", "../resources/exams/wn26-final.pdf#page=10"],
      ["WN26 Final Problem 10", "../resources/exams/wn26-final.pdf#page=11"],
      ["WN26 Final Problem 11", "../resources/exams/wn26-final.pdf#page=12"],
      ["SP26 Final Problem 10", "../resources/exams/sp26-final.pdf#page=15"],
      ["SP26 Final Problem 11", "../resources/exams/sp26-final.pdf#page=16"],
      ["SP26 Final Problem 12", "../resources/exams/sp26-final.pdf#page=17"]
    ]
  },
  {
    title: "10. Singular Value Decomposition",
    summary: "computing SVD, low-rank approximation, best direction, principal components analysis",
    links: [
      ["FA25 Final Problem 12", "../resources/exams/fa25-final.pdf#page=13"],
      ["WN26 Final Problem 12", "../resources/exams/wn26-final.pdf#page=13"],
      ["SP26 Final Problem 13", "../resources/exams/sp26-final.pdf#page=18"]
    ]
  }
];

const topicList = document.getElementById("exam-topic-list");
const topicLinks = document.getElementById("exam-topic-links");
const TOPIC_STORAGE_KEY = "resources_exam_topic_index_v1";

function termRank(label) {
  if (label.startsWith("Mock ")) return 0;
  if (label.startsWith("FA25 ")) return 1;
  if (label.startsWith("WN26 ")) return 2;
  if (label.startsWith("SP26 ")) return 3;
  return 99;
}

function examTypeRank(label) {
  if (label.includes(" MT1 ")) return 0;
  if (label.includes(" MT2 ")) return 1;
  if (label.includes(" Final ")) return 2;
  return 99;
}

function problemNumber(label) {
  const match = label.match(/Problem\\s+(\\d+)/);
  return match ? Number(match[1]) : 999;
}

function sortTopicLinks(links) {
  return [...links].sort((a, b) => {
    const labelA = a[0];
    const labelB = b[0];
    const byTerm = termRank(labelA) - termRank(labelB);
    if (byTerm !== 0) return byTerm;
    const byType = examTypeRank(labelA) - examTypeRank(labelB);
    if (byType !== 0) return byType;
    return problemNumber(labelA) - problemNumber(labelB);
  });
}

function renderTopic(index) {
  topicLinks.innerHTML = "";
  const sortedLinks = sortTopicLinks(examTopics[index].links);
  for (const [label, href] of sortedLinks) {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = href;
    a.textContent = label;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    li.appendChild(a);
    topicLinks.appendChild(li);
  }
  const buttons = topicList.querySelectorAll(".exam-topic-btn");
  buttons.forEach((btn, i) => {
    btn.classList.toggle("active", i === index);
    btn.setAttribute("aria-selected", i === index ? "true" : "false");
  });
  try {
    localStorage.setItem(TOPIC_STORAGE_KEY, String(index));
  } catch (err) {}
}

examTopics.forEach((topic, index) => {
  const btn = document.createElement("button");
  btn.type = "button";
  btn.className = "exam-topic-btn";
  btn.innerHTML = `${topic.title}<small>${topic.summary}</small>`;
  btn.setAttribute("role", "tab");
  btn.onclick = () => renderTopic(index);
  topicList.appendChild(btn);
});

let initialTopicIndex = 0;
try {
  const saved = localStorage.getItem(TOPIC_STORAGE_KEY);
  const parsed = Number(saved);
  if (Number.isInteger(parsed) && parsed >= 0 && parsed < examTopics.length) {
    initialTopicIndex = parsed;
  }
} catch (err) {}

renderTopic(initialTopicIndex);
</script>

---

## Textbooks

Note that some of these resources will use different notation and terminology than we do in the course. Some examples include:
- the **image** of a matrix $$A$$, $$\text{im}(A)$$, which we call the **column space** of $$A$$, $$\text{colsp}(A)$$.
- the **kernel** of a matrix $$A$$, $$\text{ker}(A)$$, which we call the **null space** of $$A$$, $$\text{nullsp}(A)$$.
- the **nullity** of a matrix $$A$$, $$\text{nullity}(A)$$, which we call the **dimension of the null space** of $$A$$, $$\dim(\text{nullsp}(A))$$.


The one textbook that I've referenced the most while developing EECS 245 is [Introduction to Linear Algebra](https://math.mit.edu/~gs/linearalgebra/ila6/indexila6.html) by Gilbert Strang. (The textbook itself isn't free, but this link contains links to several chapters and old exams.) You can find many of his videos [online](https://www.youtube.com/watch?v=0MtwqhIwdrI&list=PLE7DDD91010BC51F8).

The following textbooks are more similar in style to our course notes, in that they're (somewhat) designed from the perspective of machine learning.
- [Linear Algebra: Essence & Form](https://www2.math.upenn.edu/~ghrist/preprints/LAEF.pdf) by Robert Ghrist.
- [Vectors, Matrices, and Least Squares](https://web.stanford.edu/~boyd/vmls/vmls.pdf) by Boyd and Vandenberghe.
- [Mathematical Methods in Data Science](https://mmids-textbook.github.io/index.html) by Sebastien Roch.

---

## Practice Problems

### Linear Algebra

- For Post-Midterm 2 content, we have our own [practice problems page](../post-mt2-practice).
- [Problems in Linear Algebra](https://www.lem.ma/books/Ai_Km5W5WPfsPZqqV2XWGg/problems), a site with interactive problems (multiple choice and short answer).
- [18.06](https://web.mit.edu/18.06/www/old.shtml) at MIT.
- [Math 214](https://dept.math.lsa.umich.edu/courses/214/exams.html) at Michigan.
- [ECE 133A](https://www.seas.ucla.edu/~vandenbe/133A/133A-exercises.pdf) at UCLA.
- [Math 4571](https://dummit.cos.northeastern.edu/teaching_sp23_4571) at Northeastern.

### Linear Regression and Machine Learning

- [Michigan EECS 398's Study Site](https://study.practicaldsc.org/): poke around for practice problems; each exam or worksheet likely has _something_ that's relevant to our course.
- [UCSD DSC 40A's Practice Site](https://practice.dsc40a.com/): ^likewise. In particular, these worksheets may be of interest:
    - [Constant Model](https://practice.dsc40a.com/summary-statistics-and-the-constant-model/index.html).
    - [Simple Linear Regression](https://practice.dsc40a.com/simple-linear-regression/index.html).
    - [Matrices and Vectors](https://practice.dsc40a.com/matrix-vectors-properties/index.html).
    - [Gradient Descent and Convexity](https://practice.dsc40a.com/gradient-descent-convexity/index.html).

---

## Other Resources

- [An overview of gradient descent optimization algorithms](https://www.ruder.io/optimizing-gradient-descent/) by Sebastian Ruder, useful if you want to learn more about gradient descent and its many variants.
