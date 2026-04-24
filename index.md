---
layout: page
title: 🏡 Home
description: >-
  "Information about EECS 245: Mathematics for Machine Learning in Fall 2025 at the University of Michigan."
nav_order: 1
---

<!-- Embed MathJax for LaTeX rendering -->
<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

{: .blue }
Interested in taking this course in Spring 2026 or Fall 2026? Click [**here**](next) to learn more.

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
> The Final Exam is on <b>Monday, April 27th from 1:30-3:30PM in 1013 DOW</b>. See [**here**](https://edstem.org/us/courses/89676/discussion/7958167) for all relevant details.
>
> There will not be a mock final exam; instead, we've posted a [**Post-Midterm 2 Practice Problems**](../post-mt2-practice) worksheet, complete with solutions. Last semester's final exam is available [**here**](../resources#past-exams), and walkthrough videos are [**here**](https://www.youtube.com/playlist?list=PLEFTQpsm47qS-QgZ2hY-FJkqClfbGu7ds).

<a class="btn" style="background-color: #00274C; color: white;" data-current-week-link href="#{{ site.modules.first.title | slugify }}">Jump to the current week</a>

{% for module in site.modules %}
{{ module }}
{% endfor %}

<script>
(function() {
  const jumpLink = document.querySelector('[data-current-week-link]');
  if (!jumpLink) {
    return;
  }

  const modules = Array.from(document.querySelectorAll('.module'));
  if (!modules.length) {
    return;
  }

  const parseDate = (value) => {
    if (!value) {
      return null;
    }
    const parsed = new Date(value + 'T00:00:00');
    if (Number.isNaN(parsed.getTime())) {
      return null;
    }
    return parsed;
  };

  const moduleData = modules
    .map((moduleEl) => {
      const start = parseDate(moduleEl.dataset.weekStart);
      const end = parseDate(moduleEl.dataset.weekEnd);
      const header = moduleEl.querySelector('.module-header');
      if (!start || !end || !header || !header.id) {
        return null;
      }
      return { start, end, header };
    })
    .filter(Boolean);

  if (!moduleData.length) {
    return;
  }

  moduleData.sort((a, b) => a.start - b.start);

  const today = new Date();
  const todayMidnight = new Date(today.getFullYear(), today.getMonth(), today.getDate());
  let target = moduleData.find((module) => (
    todayMidnight >= module.start && todayMidnight <= module.end
  ));

  if (!target) {
    if (todayMidnight < moduleData[0].start) {
      target = moduleData[0];
    } else {
      for (let i = moduleData.length - 1; i >= 0; i -= 1) {
        if (todayMidnight > moduleData[i].end) {
          target = moduleData[i];
          break;
        }
      }
    }
  }

  if (target) {
    jumpLink.setAttribute('href', '#' + target.header.id);
  }
})();
</script>
