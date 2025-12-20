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
EECS 245, Winter 2026 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }

{% for staffer in site.staffersnobio %}
{{ staffer }}
{% endfor %}

{: .blue }
> **Welcome to EECS 245, Winter 2026!** This site is under construction; anything you see here is tentative and subject to change. If you're considering taking the course next term, look at:
> - [**eecs245.org/next**](./next), which has information on the **workload, course credit for various majors, and prerequisites**, along with the **letter grade distribution and course evaluations from Fall 2025**.
> - [**eecs245.org/fa25**](https://eecs245.org/fa25), the course website for Fall 2025, where you can find links to lecture recordings, notes, and lab worksheets from last semester.

{% for module in site.modules %}
{{ module }}
{% endfor %}