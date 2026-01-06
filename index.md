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

{: .green }
> **Welcome to EECS 245, Winter 2026!** Make sure to read the [**Syllabus**](./syllabus) and complete the [**Welcome Survey**](https://docs.google.com/forms/d/e/1FAIpQLSelaC_Oanm3SQgFLg3IBzHIXXi9bB1DgPaaSUxizhaCwTtIPw/viewform?usp=publish-editor). See you in lecture on Wednesday at 12PM and in lab later this week!

{% for module in site.modules %}
{{ module }}
{% endfor %}