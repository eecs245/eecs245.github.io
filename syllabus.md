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

See the [👩‍🏫 Staff](../staff) page for contact information, and [eecs245.org/next](https://eecs245.org/next) for course evaluations from Fall 2025.

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
<li>Have not already taken a linear algebra course (if you've already taken Math 214, 217, 417, or 419, this course is not for you).</li>
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

- **Ed:** We’ll be using Ed as our course message and discussion board. More
  details are in the [Communication](#communication) section below. If you
  didn’t already get an invitation to our Ed course, [sign up
  here](https://edstem.org/us/join/CCnkTE).

- **Gradescope:** You’ll submit all assignments to
  [Gradescope](https://www.gradescope.com/courses/1202817/), and this is where all of
  your grades will live as well. All homeworks will involve creating a PDF with your answers and submitting that to Gradescope. Some homeworks will also involve submitting code to an autograder on Gradescope; we will not be using the EECS department-specific autograder. You should have received an email invitation for
  Gradescope, but if not please let us know as soon as possible (preferably via
  Ed).

{: .red }
Note that we will **not** be using Canvas for anything this semester (so please don't try and send us messages on Canvas!).

### Programming Environment

Some labs and homeworks will involve writing Python code in Jupyter Notebooks. **As soon as you can**, follow the steps in the [Environment Setup](../env-setup) page to set up your programming environment locally on your computer. Alternatively, we've created a Jupyter Notebook server that will allow you to access and write code directly from your browser, but it can be unreliable, so you should only use it as a last resort.

### Forms

Please fill out the required [Welcome Survey](https://docs.google.com/forms/d/e/1FAIpQLSelaC_Oanm3SQgFLg3IBzHIXXi9bB1DgPaaSUxizhaCwTtIPw/viewform?usp=publish-editor) to tell us a bit more about your background and whether you need alternate exams **no later than Friday, January 16th**.

---

## Communication

This semester, we’ll be using Ed as our course message board. You will be added
to Ed automatically; use the invite link in the section above if you weren't
added.

If you have a question about anything to do with the course — if you’re stuck
on a problem, didn’t understand something from lecture, want clarification on
course logistics, or just have a general question about machine learning — you can
make a post on Ed. We only ask that if your question includes some or all of an
answer (even if you’re not sure it’s right), please make your post private so
that others cannot see it. You can also post anonymously to other students if
you prefer.

Course staff will regularly check Ed and try to answer any questions that you
have. You’re also encouraged to answer questions asked by other students.
Explaining something is a great way to solidify your understanding of it!

**Please don’t email individual staff members, just make a private or public Ed
post instead.**

---

## Course Components

### Lectures

Lectures will be held in-person on Mondays and Wednesdays from 12-1:30PM in 1013 DOW. Attendance is not required, **though you are encouraged to attend in-person if you are able to**, no matter which section you're enrolled in (i.e. students in LEC 001 and LEC 002 can both attend lecture). Lectures will be recorded. We will do our best to make lectures are interactive and well-worth your time.

Recordings will be made publicly available so that students who are not enrolled – including students not at Michigan – can benefit from the recordings. As part of your participation in this course, you may be recorded (e.g. if you answer a question). If you do not wish to be recorded, please email the instructor to discuss alternate arrangements.

Course notes have been written specifically for EECS 245, and will be your main resource in this class. These can be found at [notes.eecs245.org](https://notes.eecs245.org). We are constantly refining the notes, and will link them directly underneath the relevant lecture once they are ready.

{: .yellow }
**These notes aren't optional readings, they're mandatory.** It is nearly impossible to succeed in this course without reading them regularly. See the [Advice](https://notes.eecs245.org/advice) section of the notes for testimonies from previous students.

If you find any typos or ways to improve the notes, please fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSfrAu2o3eBa9ZvjerOFxqDHV63GlR9NoYdA4TOgK8BBoSguCg/viewform?usp=dialog).

Live lectures will closely follow the notes. Instead of presenting using slides in lecture, we will start with a blank document on a tablet, and write out the lecture content in real time, allowing us to move at a pace that is appropriate for the class and to focus on the high-level ideas (details can be found in the notes). Anything we write in live lectures will be posted as a PDF on the course website after lecture.

### Labs

There are **three** lab sections throughout the week. **You can attend any lab section on any given week, regardless of which section you're enrolled in.**
- Thursdays, 12:30-2:30PM in 2918 COOL
- Thursdays, 3:30-5:30PM in 1017 DOW
- Fridays, 11:30AM-1:30PM in 1014 DOW

{: .yellow }
> Due to staffing shortages, **we will not be staffing the Thursday 4:30-6:30PM lab section**. If you are enrolled in this section, you should attend one of the other three sections above. 
> 
> If the only time you are free is Thursday 4:30-6:30PM, you should attend the second half of the Thursday 3:30-5:30PM section and then the office hours that follow afterwards held by the same TA.

Labs are meant to provide hands-on practice with the recent lecture material and preparation for the upcoming homeworks and exams. 

Each lab session will have an accompanying **physical worksheet** that is distributed in-person at the start of lab and meant to be completed during the live lab session. Each worksheet is broken into several activities; some activities will involve writing math on the paper worksheet, and others will involve writing code in a Jupyter Notebook and either showing your TA a working solution or submitting it to the autograder. 

To earn credit for a lab, you must make an effort to attempt all "required" activities and **show the lab TA an almost completed worksheet** by the end of the lab session. **This means that there is no option to receive credit for labs remotely.** Worksheets will usually include additional practice problems for you to work through after lab.

There will be 13 labs in total. Each week you attend and submit the lab will earn you 1 "lab point", up to a maximum of 10 lab points. Your lab score will be the number of lab points you earn out of 10. This means **you can miss up to 3 labs for any reason** (late add, extenuating circumstances, etc.) and still earn a full lab score. This flexibility is provided in lieu of allowing for remote submissions, since we really believe in the power of working on problems in-person and on-paper with other students. Details can be found in the [Grades](#grades) section below.

Lab worksheets and solutions will be posted on the course website on Friday afternoons, after all lab sessions have concluded.

### Homeworks

This class will have 11 **weekly** homework assignments, which are to be completed **individually**. Homeworks will usually be released on Friday afternoons and be due the following **Friday at 11:59PM**, though this may change in any given week. See the [course homepage](../) for the most up-to-date deadline schedule.

**Collaboration Policy**

The majority of homework problems will involve writing solutions to math problems, but some will involve writing code in a Jupyter Notebook. The point of a homework problem is not really to "find the answer" – we know the answers, and ChatGPT can easily provide answers to any homework problem we could ask you. Rather, the point of a homework problem is to help you **deeply understand the material**, **apply it to new problems**, and build **problem-solving skills** along the way that will pay dividends in future courses and in your life as a graduate of the University of Michigan.

Think of it like this: driving 10 miles is a lot easier than running 10 miles, and in many cases, driving makes total sense. But, if you're trying to exercise, driving 10 miles won't really help you achieve your goals. If you buy that analogy, just think of driving as "copying the answers from someone else" and running as "thinking through problems yourself" – both may earn you the same score on homeworks, but only the latter will help you in the long run.

**With that in mind, you can – and are actually encouraged to! – talk to other students in the class about the problems and discuss solution strategies. Talking and debating about challenging ideas is a great way to solidify your own understanding of the material.** That said, you should not share any written communication. You can tell someone how to approach a homework problem if they're stuck, but you cannot show them how to do it. One way to tell if you are respecting this boundary is to ask yourself whether your collaboration could take place over the phone. Additionally, the content of your verbal communication should involve the problem-solving strategy and approach, and you should not directly compare answers with classmates.

Similarly, you can ask generative AI tools like ChatGPT for help with concepts, because these tools _can_ be genuinely useful. Just be cautious that they can also lead you astray. If you find a particularly useful explanation online, either on a website or from a generative AI tool, please let us know! **You cannot ask generative AI tools to solve homework problems for you or to verify your answers.** Doing so is only cheating yourself. **Remember you will not be able to use these tools during the exams, which are worth 70% of your overall grade.**

If we suspect that your homework answers are not the result of your own work, we reserve the right to interview you in-person and ask you to answer and explain similar questions, and submit a case to the [Honor Council](https://ecas.engin.umich.edu/honor-council/).

You may post homework-related questions on Ed, though your questions and answers should be about approaches, not answers to specific problems. If your question includes some or all of an answer (even if you’re not sure it’s right), you must make your post private so that others cannot see it. We are not able to tell you whether your answer is correct.

**Late Policy, Slip Days, and Drops**

All homeworks must be submitted by 11:59PM Ann Arbor time on the due date to
be considered on time. If you make a submission after the
deadline, your assignment will be counted as late.

You have **8 "slip days"** to use throughout the semester. A slip day extends
the deadline of a homework by 24 hours. **You may use up to 2 slip days on any one homework assignment**. (Since lab worksheets must be submitted in-person, they cannot be submitted late, and can't use up slip days.)

Slip days are designed to be a transparent and predictable source of leniency
in deadlines. You can use a slip day if you are too busy to complete a homework on its original due date (or if you forgot about it). But slip days are also meant for things like the internet going down at 11:58PM just as you
go to submit your homework. Slip days are meant to be used in exceptional
circumstances, so you probably should not need to use all 8, but if you have
something going on in your life that is impeding your ability to do your
classwork on time, please reach out to us as soon as possible so we can work
something out. The earlier you let us know that something's going on,
the more we can do to help, so please reach out.

Slip days are applied automatically at the end of the semester, and you don’t
need to ask in order to use one. It’s your responsibility to keep track of
how many you have left. If you’ve run out of slip days and submit an assignment
late, that homework may still be graded, but you will receive a 0 on it when
we calculate grades at the end of the semester.

In addition, your lowest 2 homework scores will be dropped from your final grade. This means that you can miss up to 2 homeworks for any reason and still earn a full homework score. You do not use up any slip days on homeworks you don't submit, e.g. if you choose not to submit Homework 2, it costs you 0 slip days.

**Regrade Requests**

Most homework problems will be graded manually by our excellent graders, strictly adhering to a rubric. If you believe that the grader has made a mistake in applying the rubric shown to you on Gradescope, you may submit a regrade request directly on Gradescope within one week of the grades being released. If you do not submit a regrade request within one week, your original grade will be final. Part of your grade is clarity, so if your answer was mostly right but unclear you may still not be eligible for full credit.

Some homework problems will be graded automatically by the autograder. If you believe that the autograder has made a mistake in grading your homework, send the instructor an email, again, within one week of the grades being released. Note that it's rare that something is wrong with the autograder, and if that's the case, we'll typically fix the necessary test cases and re-run the autograder for the entire class.

Homeworks should be written or typed up and turned in by each student individually. If you want to type up your answers, we will provide a LaTeX template through Overleaf; click the 🍃 emoji next to each homework on the homepage to access the template. Homework 1 will include instructions on how to use the template. This template will be optional, except for one homework assignment, for which it will be mandatory.

### Office Hours

To get help on assignments and concepts, course staff will be hosting several office hours per week. The vast majority of office hours will be held in-person on North Campus, though we will hold remote office hours, depending on staff availability. See the [Calendar](../calendar) tab of the course website for the most up-to-date schedule and directions. If you aren't able to consistently attend at least one office hours slot a week, please email the instructor – we will try our best to move things around to get you the support you need.

In a theoretical class such as this one, it's important to make good use of office hours. Homework assignments will be challenging, so you should plan to attend office hours at least once a week. Even if you don’t have specific questions, you will likely get a lot out of conversing about the material and hearing others' questions. And even if you've mastered the material, still come and say hi – take advantage of the fact that this is a relatively small class.

---

## Exams

This class has two Midterm Exams and one Final Exam, all of which will be administered in-person and on paper.

| Exam | Date and Time | Content |
| --- | --- | --- |
| Midterm 1 | Monday, February 16th, 7-9PM | Lectures 1-10, Chapters 1-4 only |
| Midterm 2 | Monday, March 30th, 7-9PM | Lectures 11-19, Chapters 5-8 only |
| Final Exam | Monday, April 27th, 1:30-3:30PM | ~30% Lectures 1-10<br>~30% Lectures 11-19<br>~40% Lectures 20-25 |

The specific lecture numbers above are subject to change slightly. Midterm 2 is not cumulative. The Final Exam will be cumulative, and broken into three parts:

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

1. **Part 1** of the Final Exam will be based on Midterm 1 content. If you score higher on Part 1 than you did on Midterm 1, we will replace your Midterm 1 score with $$\frac{\text{Part 1 score} + \text{Midterm 1 score}}{2}$$.
2. **Part 2** of the Final Exam will be based on Midterm 2 content. If you score higher on Part 2 than you did on Midterm 2, we will replace your Midterm 2 score with $$\frac{\text{Part 2 score} + \text{Midterm 2 score}}{2}$$.
3. **Part 3** of the Final Exam will be based on the content introduced after Midterm 2.

This "redemption policy" for Parts 1 and 2 is designed to help you boost your Midterm 1 and Midterm 2 scores if you didn't do as well as you'd hoped. This policy can only help your grade; it can't hurt. To be clear, all three parts of the Final Exam are required and part of your Final Exam score.

If you have conflicts with any of the exams, please let us know on the [Welcome Survey](https://docs.google.com/forms/d/e/1FAIpQLSelaC_Oanm3SQgFLg3IBzHIXXi9bB1DgPaaSUxizhaCwTtIPw/viewform?usp=publish-editor). We may provide alternate exam times for students with a valid, documented conflict with a required activity in another course or official university-affiliated activity, or to help students avoid negative academic consequences when their religious obligations conflict with academic requirements.

Exams are to be completed individually, with absolutely no collaboration allowed. Any suspected violations will be reported to the [Honor Council](https://ecas.engin.umich.edu/honor-council/).

---

## Grades

### Weights

| Component                               | Weight              | Notes                           |
| --------------------------------------- | ------------------- | ------------------------------- |
| Midterm 1                                    | 20% | see [Exams](#exams) section above |
| Midterm 2                                    | 20% | see [Exams](#exams) section above  |
| Final Exam                                   | 30%                 |  |
| Homeworks | 20% | • 11 total; 2 lowest scores dropped <br> • 8 slip days available to use with a max of 2 per homework  |
| Labs | 10% | 13 total; 3 lowest scores dropped  |


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

You can see last semester's letter grade distribution [here](https://eecs245.org/next/#workload-and-final-grade-distribution); we will aim to achieve a similar distribution this semester, but minor variations are expected.

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

This course is being offered for the second time at the University of Michigan. With that said, many of the materials we will use are adopted from content created by countless other instructors for courses at other institutions.

- In particular, some materials are adopted from [EECS 398: Practical Data Science](https://practicaldsc.org), which itself was based on content from DSC 10, DSC 40A, and DSC 80 at the University of California, San Diego; and Data 6 and Data 100 at the University of California, Berkeley.
- Some homework problems have been adapted from various linear algebra courses and textbooks online and at other institutions. Some of these sources are listed at the bottom of the introduction to the [course notes](https://notes.eecs245.org/).
- Language in this syllabus has been adopted from other courses as well, including EECS 203, EECS 280, EECS 376, and EECS 485 here at the University of Michigan, and CSE 160 at the University of Washington.

---

## Disclaimer

While we try to do our best to plan ahead, unfortunately, sometimes circumstances do arise that necessitate a policy change. When this happens, the change will be announced, and this document will be updated with the new policy.

We appreciate any and all feedback, given that this course is new and evolving. If you'd like to provide us with anonymous feedback at any point, you can do so at [this form](https://forms.gle/3FQf9iJ21BrPoJhM9). Thank you.
