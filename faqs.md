---
layout: page
title: 🙋 FAQs
description: Answers to frequently asked logistical questions.
nav_order: 2
toc_max_heading_level: 2
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>


# 🙋FAQs

**Who is teaching the class?**

{% for staffer in site.staffersnobio %}
{{ staffer }}
{% endfor %}

Since this information is not on ATLAS, course evaluations from Suraj's Fall 2024 offering of a different course can be found [here](https://practicaldsc.org/assets/marketing/fa24-evals.pdf).

**What are the prerequisites?**

- EECS 203 or Math 116 (or Math 215, 216, 275, 285, or 295).
- Some 100-level programming class (e.g. EECS 183, ENGR 101, ROB 102, or similar).

If you're not sure if you meet the prerequisites, email the instructor.

<a name="credit">

**What does this course count for?**

This course is worth 4 credits, and is currently approved to count towards:

- The linear algebra requirement for the CS-Eng major.
- The linear algebra "category" for the CS-LSA major (see [here](https://docs.google.com/document/d/1i0W77CzwMK6l3FFFdG7_7urp8H_oE4EaOzRPFOJdrxo/preview?tab=t.0#heading=h.m67kk7886dyq) for the CS-LSA program guide).
- The linear algebra prerequisite for EECS 445.

As of 4/13, the course is **not currently approved** to count for the DS major. 

If the course is approved to count for other programs, we will update this page.

**How is this course formatted?**

- **Lectures (TuTh 3-4:30PM, 1013 DOW):** Introduce core content in an interactive format. Recorded, and attendance will not be taken.
- **Labs (W 12:30-2:30PM or W 4:30-6:30PM):** Provide supervised practice with mathematical ideas and a venue for exploring practical applications in Python. Attendance will be taken.
- **Homeworks:** Assigned and due weekly. Will consist of ~80% math on paper and ~20% code in Python.
- **Exams:** 2 Midterm Exams and 1 Final Exam (see dates on the [course homepage](../)), all in-person and on-paper.

**Who should take this class?**

Anyone who:
- Hasn't already taken a linear algebra course (if you've already taken Math 214, 217, 417, or 419, this course is not for you).
- Plans on taking Upper-Level CS courses about machine learning and artificial intelligence (e.g. EECS 445) **and/or** wants to gain exposure to machine learning and Python early in their academic careers.

**What makes this different from other linear algebra courses?**

This course aims to provide:
- Enough rigor to ensure students can succeed in more theoretical ULCS courses (like EECS 445).
- Enough context, motivation, and applications for students to see _why_ linear algebra is useful in machine learning, throughout the entire course.

**Is this class the same as EECS 398: Practical Data Science?**

No, this class is completely separate from EECS 398: Practical Data Science. EECS 298: Mathematics for Machine Learning focuses on the theoretical foundations of machine learning, while EECS 398: Practical Data Science took a more practical approach. EECS 398: Practical Data Science won't be offered in Fall 2025, but we hope to offer it again in the future.
