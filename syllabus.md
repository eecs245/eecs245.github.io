---
layout: page
title: 📖 Syllabus
description: >-
  Course policies and information.
nav_order: 2
---


<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>


# 📖 Syllabus
{:.no_toc}

{: .red }
**Coming soon!**

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


{: .yellow}
> <b>Note about Accessibility</b><br>
> It's important to us that all students are able to fully engage with our course content. We're working to ensure that all digital materials – the website, course notes, homework and lab PDFs, supplemental videos, etc. – meet [WCAG 2.1 AA](https://www.w3.org/TR/WCAG21/) accessibility standards, as mandated by the federal government of all public universities in the United States. If you find any accessibility issues (hard-to-read colors, missing alt text, videos with missing captions, or anything else that makes the content difficult to access), please let Suraj know as soon as possible at rampure@umich.edu.

## Overview

### Instructor

The instructor is Suraj Rampure. If you need to get in touch, please reach out
on Slack or email rampure@umich.edu.

### Content

Linear algebra, calculus, and probability form the basis of modern machine learning and artificial intelligence. This course will introduce linear algebra from scratch by focusing on methods and examples from machine learning. It will give students strong intuition for how linear algebra, calculus and probability are used in machine learning. While the course is primarily theoretical, we’ll look at practical applications involving real data in Python each week, so that students are able to apply what they’ve learned.

This course aims to provide:
- Enough rigor to ensure students can succeed in more theoretical ULCS courses (like EECS 445).
- Enough context, motivation, and applications for students to see _why_ linear algebra is useful in machine learning, throughout the entire course.

### Credit

This course is worth 4 credits, and is currently approved to count towards the **linear algebra requirement for**:

- **Computer Science** majors (CS-Eng and CS-LSA*).
- **Data Science** majors (DS-Eng and DS-LSA).
- **Statistics** majors.
- **Artificial Intelligence** minors.

And the linear algebra prerequisite for:
- EECS 442, EECS 445, EECS 448, EECS 474, EECS 476, and CSE 576.
- **Any** 400-level STATS or DATASCI course with a linear algebra prerequisite.

<small>*CS-LSA students don't have a linear algebra requirement, but this course fits in the linear algebra "bucket" for the second math course; see [here](https://docs.google.com/document/d/1i0W77CzwMK6l3FFFdG7_7urp8H_oE4EaOzRPFOJdrxo/preview?tab=t.0#heading=h.m67kk7886dyq) for details.</small>

<details><summary><b>Who should take this course?</b></summary>

<br>

You should take this course if you:
<ul>
<li>Have not already taken a linear algebra course (if you've already taken Math 214, 217, 417, or 419, this course is not necessary, though you still may gain some perspective from taking it).</li>
<li>Plan on taking Upper-Level CS courses about machine learning and artificial intelligence (e.g. EECS 445) <b>and/or</b> want to gain exposure to machine learning and Python early in your academic career.</li>
</ul>

</details>

### Prerequisites

- EECS 203 or Math 116 (or Math 215, 216, 275, 285, or 295), i.e. some math course after Calculus 1.
- Some 100-level programming class (e.g. EECS 183, ENGR 101, ROB 102, or similar).

If you're not sure if you meet the prerequisites – or if you don't, but are still interested in taking the course nonetheless – email the instructor.

---

## Getting Started

The course website, [eecs245.org](../), will contain links to all
course content. There are also a few things you'll need to do to get set up.

### Computer and Network Recommendations

Make sure you have a laptop consistent with [CAEN recommendations](https://caen.engin.umich.edu/percomps/).

<details><summary><b>More details</b></summary>

<br>

Test your internet connection with the <a href="http://umich.speedtestcustom.com/">UM Custom Speedtest website</a> and make sure it meets the <a href="https://teamdynamix.umich.edu/TDClient/76/Portal/KB/ArticleDet?ID=5091">minimum requirements for any UM service</a>. You'll need more bandwidth if there will be multiple simultaneous users in your household.

<br>

Resources for help with computing equipment:
<ul>
<li>Information and Technology Services (ITS) <a href="https://its.umich.edu/computing/computers-software/sites-at-home">Laptop loaner program</a></li>
<li>College of Engineering (CoE) <a href="https://studentaffairs.engin.umich.edu/">Office of Student Affairs</a>, email requests to coe-studentaffairs@umich.edu</li>
</ul>

You may also use computer workstations in CAEN labs on campus or <a href="https://caen.engin.umich.edu/connect/">connect remotely</a>.

</details>

### Websites

You'll need to make accounts on the following sites:

- **Slack:** We’ll be using Slack as our course message and discussion board.
  More details are in the [Communication](#communication) section below. You
  should receive an invitation to the course Slack workspace; if not, please
  let us know as soon as possible.

- **Gradescope:** You’ll submit all assignments to
  [Gradescope](TODO), and this is where all of
  your grades will live as well. All homeworks must be handwritten, scanned into a PDF, and submitted to Gradescope. Some homeworks may also involve submitting code to an autograder on Gradescope; we will not be using the EECS department-specific autograder. You should have received an email invitation for Gradescope, but if not please let us know as soon as possible.

{: .red }
Note that we will **not** be using Canvas for anything this semester (so please don't try and send us messages on Canvas!).

### Programming Environment

Some labs and homeworks will involve writing Python code in Jupyter Notebooks. **As soon as you can**, follow the steps in the [Environment Setup](../env-setup) page to set up your programming environment locally on your computer. Alternatively, we've created a Jupyter Notebook server that will allow you to access and write code directly from your browser, but it can be unreliable, so you should only use it as a last resort.

### Forms

Please fill out the required [Welcome Survey](#TODO) to tell us a bit more about your background and whether you need alternate exams **no later than Sunday, May 10th**.

---

## Communication

This semester, we’ll be using Slack as our course message board. Since the
course is relatively small, Slack should be better suited than Ed to the kinds
of smaller group discussions we expect to have.

If you have a question about course logistics, feel free to DM the instructor
directly. If you have a conceptual question – if you’re stuck on a problem,
didn’t understand something from lecture, or want to ask a general question
about machine learning – please post in `#general` so that other students can
chime in and see the response. Explaining something is a great way to solidify
your understanding of it!

We’ll use `#announcements` to announce the release of new assignments and
upcoming events, such as exams. You are responsible for keeping up with
messages posted there.

---

## Course Components

### Lectures

Lectures will be held in-person on Tuesdays and Thursdays from 1-4PM in 1690 BBB. Because the spring term is compressed, each lecture will cover roughly two lectures' worth of material from the regular semester. Attendance is not strictly required, though each lecture you attend earns you 1 [engagement point](#engagement), and engagement points are worth 5% of your overall course grade. It is possible to earn 100% in the course without attending lecture, but this part of the grade is designed to encourage you to come.

A recording will be posted after each lecture, either from the spring or from a previous semester. (Since we only have a few students in the class, in-person lectures may feel a bit more casual and personalized to the students present than in a regular semester, hence the posting of previous semester recordings.) We will do our best to make lectures interactive and well worth your time.

 As part of your participation in this course, you may be recorded (e.g. if you answer a question). If you do not wish to be recorded, please email the instructor to discuss alternate arrangements.

Course notes have been written specifically for EECS 245, and will be your main resource in this class. These can be found at [notes.eecs245.org](https://notes.eecs245.org).

{: .yellow }
**These notes aren't optional readings, they're mandatory.** It is nearly impossible to succeed in this course without reading them regularly. See the [Advice](https://notes.eecs245.org/advice) section of the notes for testimonies from previous students.

If you find any typos or ways to improve the notes, please fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSfrAu2o3eBa9ZvjerOFxqDHV63GlR9NoYdA4TOgK8BBoSguCg/viewform?usp=dialog).

Live lectures will closely follow the notes. Instead of presenting using slides in lecture, we will start with a blank document on a tablet, and write out the lecture content in real time, allowing us to move at a pace that is appropriate for the class and to focus on the high-level ideas (details can be found in the notes). Anything we write in live lectures will be posted as a PDF on the course website after lecture.

### Labs

In a traditional semester, labs are held in person for 2 hours each week. Since
our course is relatively small, we do not have any TAs, and we already have a
high number of contact hours, we will not hold physical lab sections this term.
Instead, each Sunday, we will post two lab worksheets:
- A Monday worksheet, containing problems from the previous Thursday's lecture
- A Wednesday worksheet, containing problems from the previous Tuesday's lecture

Lab worksheets are meant to provide hands-on practice with the recent lecture material and preparation for the upcoming homeworks and exams. Each worksheet will be broken into several activities. Some activities may involve writing math, and others may involve writing code in a Jupyter Notebook.

(These worksheets are what students in a standard semester of EECS 245 would complete in lab.)

We ask that you spend roughly 2 hours working on each worksheet, asking
questions on Slack or in office hours as needed, and then submit your best
attempt to Gradescope. There will be 13 lab worksheets in total. Each lab
worksheet you submit will earn you 1 lab point, up to a maximum of 10 lab
points. Your lab score will be the number of lab points you earn out of 10.
This means **you can miss up to 3 labs for any reason** (late add, extenuating
circumstances, etc.) and still earn a full lab score. Details can be found in
the [Grades](#grades) section below.

Lab worksheets and solutions will be posted on the course website.

### Homeworks

This class will have regular homework assignments throughout the compressed term, which are to be completed **individually**. Homework due dates may vary throughout the term; see the [course homepage](../) for the most up-to-date deadline schedule. We will try to always give you a week to work on each homework, except the first one.

**Collaboration Policy**

The majority of homework problems will involve writing solutions to math problems, but some will involve writing code in a Jupyter Notebook. The point of a homework problem is not really to "find the answer" – we know the answers, and ChatGPT can easily provide answers to any homework problem we could ask you. Rather, the point of a homework problem is to help you **deeply understand the material**, **apply it to new problems**, and build **problem-solving skills** along the way that will pay dividends in future courses and in your life as a graduate of the University of Michigan.

Think of it like this: driving 10 miles is a lot easier than running 10 miles, and in many cases, driving makes total sense. But, if you're trying to exercise, driving 10 miles won't really help you achieve your goals. If you buy that analogy, just think of driving as "copying the answers from someone else" and running as "thinking through problems yourself" – both may earn you the same score on homeworks, but only the latter will help you in the long run.

**With that in mind, you can – and are actually encouraged to! – talk to other students in the class about the problems and discuss solution strategies. Talking and debating about challenging ideas is a great way to solidify your own understanding of the material.** That said, you should not share any written communication. You can tell someone how to approach a homework problem if they're stuck, but you cannot show them how to do it. One way to tell if you are respecting this boundary is to ask yourself whether your collaboration could take place over the phone. Additionally, the content of your verbal communication should involve the problem-solving strategy and approach, and you should not directly compare answers with classmates.

Similarly, you can ask generative AI tools like ChatGPT for help with concepts, because these tools _can_ be genuinely useful. Just be cautious that they can also lead you astray. If you find a particularly useful explanation online, either on a website or from a generative AI tool, please let us know! **You cannot ask generative AI tools to solve homework problems for you or to verify your answers.** Doing so is only cheating yourself. **Remember you will not be able to use these tools during the exams, which are worth 70% of your overall grade.**

If we suspect that your homework answers are not the result of your own work, we reserve the right to interview you in-person and ask you to answer and explain similar questions, and submit a case to the [Honor Council](https://ecas.engin.umich.edu/honor-council/).

You may post homework-related questions on Slack, though your questions and answers should be about approaches, not answers to specific problems. If your question includes some or all of an answer (even if you’re not sure it’s right), please DM the instructor instead of posting it publicly. We are not able to tell you whether your answer is correct.

**Late Policy, Slip Days, and Drops**

All homeworks must be submitted by 11:59PM Ann Arbor time on the due date to
be considered on time. If you make a submission after the
deadline, your assignment will be counted as late.

Every student has 4 slip days by default. A slip day extends the deadline of a homework by 24 hours, and slip days will be applied automatically to late homework submissions. You may use a maximum of 1 slip day per homework, so that we can release homework solutions shortly after the deadline.

If you need more than 4 slip days, you have to ask me on Slack before the relevant deadline. If I don't hear from you before the deadline and you are out of slip days, the extension won't be granted. If a student is going to fall behind, I want to know about it.

In addition, your lowest 2 homework scores will be dropped from your final grade. This means that you can miss up to 2 homeworks for any reason and still earn a full homework score.

**Regrade Requests**

Most homework problems will be graded manually by our excellent graders, strictly adhering to a rubric. If you believe that the grader has made a mistake in applying the rubric shown to you on Gradescope, you may submit a regrade request directly on Gradescope within one week of the grades being released. If you do not submit a regrade request within one week, your original grade will be final. Part of your grade is clarity, so if your answer was mostly right but unclear you may still not be eligible for full credit.

Some homework problems will be graded automatically by the autograder. If you believe that the autograder has made a mistake in grading your homework, send the instructor an email, again, within one week of the grades being released. Note that it's rare that something is wrong with the autograder, and if that's the case, we'll typically fix the necessary test cases and re-run the autograder for the entire class.

Homeworks must be handwritten by each student individually, scanned into a single PDF, and submitted to Gradescope. In past semesters we provided an Overleaf template for students who wanted to typeset solutions, but we will not be doing that this term.

### Office Hours

The instructor will usually be free shortly before and shortly after lecture to
answer homework questions. The standard way to attend office hours is to make an
appointment using [this Google Calendar
link](https://calendar.app.google/TNqfWMxkjuaLGi6n9). Appointments are 15
minutes long, though they can run longer if needed, and are available both on
Zoom and in person. If you'd like to meet with the instructor but no times are
available, let them know on Slack.

Each office hours appointment counts as 1 engagement point, up to a maximum of
2 office hours engagement points per week.

In a theoretical class such as this one, it's important to make good use of office hours. Homework assignments will be challenging, so you should plan to attend office hours at least once a week. Even if you don’t have specific questions, you will likely get a lot out of conversing about the material and hearing others' questions. And even if you've mastered the material, still come and say hi – take advantage of the fact that this is a relatively small class.

---

## Exams

This class has two Midterm Exams and one Final Exam, all of which will be administered in-person and on paper.

| Exam | Date and Time | Content |
| --- | --- | --- |
| Midterm 1 | Monday, May 25th, 12-2PM | Chapters 1-4 of the [course notes](https://notes.eecs245.org) |
| Midterm 2 | Tuesday, June 9th, 1-3PM | Chapters 5-8 of the [course notes](https://notes.eecs245.org) |
| Final Exam | Wednesday, June 24th, 8-10AM | Cumulative; see the homepage for the latest review materials |

Midterm 2 is not cumulative. The Final Exam will be cumulative, and broken into three parts:

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

1. **Part 1** of the Final Exam will be based on Midterm 1 content. If you score higher on Part 1 than you did on Midterm 1, we will replace your Midterm 1 score with $$\frac{\text{Part 1 score} + \text{Midterm 1 score}}{2}$$.
2. **Part 2** of the Final Exam will be based on Midterm 2 content. If you score higher on Part 2 than you did on Midterm 2, we will replace your Midterm 2 score with $$\frac{\text{Part 2 score} + \text{Midterm 2 score}}{2}$$.
3. **Part 3** of the Final Exam will be based on the content introduced after Midterm 2.

This "redemption policy" for Parts 1 and 2 is designed to help you boost your Midterm 1 and Midterm 2 scores if you didn't do as well as you'd hoped. This policy can only help your grade; it can't hurt. To be clear, all three parts of the Final Exam are required and part of your Final Exam score.

If you have conflicts with any of the exams, please let us know on the [Welcome Survey](#TODO). We may provide alternate exam times for students with a valid, documented conflict with a required activity in another course or official university-affiliated activity, or to help students avoid negative academic consequences when their religious obligations conflict with academic requirements.

Exams are to be completed individually, with absolutely no collaboration allowed. Any suspected violations will be reported to the [Honor Council](https://ecas.engin.umich.edu/honor-council/).

---

## Grades

In addition to exams, homeworks, and labs, the course includes an **engagement**
component. You can earn 1 engagement point for each lecture you attend and each
office hours appointment you attend, up to a maximum of 2 office hours
engagement points per week. There will be more than 14 opportunities to earn
points during the term; earning at least 14 engagement points gives you full
engagement credit.

### Weights

| Component                               | Weight              | Notes                           |
| --------------------------------------- | ------------------- | ------------------------------- |
| Midterm 1                                    | 20% | see [Exams](#exams) section above |
| Midterm 2                                    | 20% | see [Exams](#exams) section above  |
| Final Exam                                   | 30%                 |  |
| Homeworks | 15% | • Due dates may vary throughout the term <br> • 4 slip days by default; max 1 per homework; ask for more <br> • Lowest 2 scores dropped |
| Labs | 10% | 13 total; 3 lowest scores dropped |
| Engagement | 5% | Earn 1 point for each lecture attended and each office hours appointment attended; 14 points earns full credit |


### Letter Grades

Grading for this class is not curved in the sense that the average is set at
(say) a B+ and half of the class must receive a grade lower than that. If
everyone does well and shows mastery of the material, everyone can receive an A
(this would be awesome!). If no one does well (this is unlikely), then everyone
can receive a C.

Grading for this class is curved in the sense that we do not have a pre-defined
mapping from project and exam scores to a final GPA. There is no pre-determined
score (e.g., 90% of all possible points) that earns an A or a B or a C or any
other grade. To determine the final grade, we will ask questions like “Did this
student master the material?”. With that said, grades will not be any stricter
than the standard grading scale (where an A+ is a 97+, A is 93+, A- is 90+,
etc). For instance, the threshold for an “A” will never be higher than 93%.

You can see Fall 2025's letter grade distribution [here](https://eecs245.org/next/#workload-and-final-grade-distribution); we will aim to achieve a similar distribution this semester, but minor variations are expected.

Try your best not to worry about grades, and we’ll reciprocate by being fair.
We’re in this together ❤️.

---

## Student Support and Well-Being

### Accommodations

If you need, or think you might need, an accommodation for a disability, please let us know during the first three weeks of the semester. Some aspects of this course may be modified to facilitate your participation and progress. As soon as you make us aware of your needs, we can work with the [Services for Students with Disabilities (SSD)](http://ssd.umich.edu) office to help us determine appropriate academic accommodations. SSD ([ssd.umich.edu](https://ssd.umich.edu); 734-763-3000) recommends accommodations through a Verified Individualized Services and Accommodations (VISA) form. Any information you provide is private and confidential and will be treated as such.

### Diversity and Inclusion

It is our intention that students from all backgrounds and perspectives will be well served by this
course, and that the diversity that students bring to this class will be viewed as an asset. We
welcome individuals of all ages, backgrounds, beliefs, ethnicities, genders, gender identities, gender
expressions, national origins, religious affiliations, sexual orientations, socioeconomic background,
family education level, ability - and other visible and nonvisible differences. All members of this
class are expected to contribute to a respectful, welcoming, and inclusive environment for every
other member of the class. Your suggestions are encouraged and appreciated.

### Campus Resources

As a student, you may experience a range of issues that can negatively impact your learning, such as
anxiety, depression, interpersonal or sexual violence, difficulty eating or sleeping, loss/grief, and/or
alcohol/drug problems. These mental health concerns or stressful events may lead to diminished
academic performance and affect your ability to participate in day-to-day activities.

In order to support you during such challenging times, the University of Michigan provides a number of
confidential resources to all enrolled students, many of which are listed [here](https://wellbeing.umich.edu/tools-resources/#resourcesforstudents). Some particularly useful resources include:

- [CoE CARE Center](https://docs.google.com/document/d/1KwA3_R93QSMhOJOmVMLydoT4D4Hu1fhM_QngiDprX6U/edit?usp=sharing)
- [Counseling and Psychological Services (CAPS)](https://caps.umich.edu/contact); 734-764-8312 (24/7 line)
- [Sexual Assault Prevention and Awareness Center (SAPAC)](https://sapac.umich.edu); 734-936-3333 (24/7 line)
- Psychiatric Emergency Services: 734-996-4747
- [Services for Students with Disabilities (SSD)](https://ssd.umich.edu); 734-763-3000; ssdoffice@umich.edu

### CSE Resources

<img src="../assets/site-images/CSE UAO Resources.png" alt="CSE UAO student support resources graphic" width="600">

---

## Acknowledgements

This course is being offered for the third time at the University of Michigan. With that said, many of the materials we will use are adopted from content created by countless other instructors for courses at other institutions.

- In particular, some materials are adopted from [EECS 398: Practical Data Science](https://practicaldsc.org), which itself was based on content from DSC 10, DSC 40A, and DSC 80 at the University of California, San Diego; and Data 6 and Data 100 at the University of California, Berkeley.
- Some homework problems have been adapted from various linear algebra courses and textbooks online and at other institutions. Some of these sources are listed at the bottom of the introduction to the [course notes](https://notes.eecs245.org/).
- Language in this syllabus has been adopted from other courses as well, including EECS 203, EECS 280, EECS 376, and EECS 485 here at the University of Michigan, and CSE 160 at the University of Washington.

---

## Disclaimer

While we try to do our best to plan ahead, unfortunately, sometimes circumstances do arise that necessitate a policy change. When this happens, the change will be announced, and this document will be updated with the new policy.

We appreciate any and all feedback, given that this course is new and evolving. If you'd like to provide us with anonymous feedback at any point, you can do so at [this form](https://forms.gle/3FQf9iJ21BrPoJhM9). Thank you.
