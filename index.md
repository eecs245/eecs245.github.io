---
layout: page
title: 🏡 Home
description: >-
  Information about EECS 245: Mathematics for Machine Learning in Fall 2026 at the University of Michigan.
nav_order: 1
---

<!-- Embed MathJax for LaTeX rendering -->
<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

# Mathematics for Machine Learning 🧠
{: .no_toc }
{: .mb-2 }
EECS 245, Fall 2026 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }
**Lectures**: Tuesdays and Thursdays, 10:30AM-12PM, 1010 DOW • **Labs**: Various [times](calendar) on Wednesday

{: .green }
> **Midterm 1 is on Tuesday, October 6th from 7-9PM in 1013 DOW. See all relevant logistics [here](https://edstem.org/us/courses/101561/discussion/8322342).**

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
      /* Include the full Monday-Sunday week, even when classes start Tuesday. */
      start.setDate(start.getDate() - (start.getDay() + 6) % 7);
      end.setDate(end.getDate() + (7 - end.getDay()) % 7);
      return { start, end, header, moduleEl };
    })
    .filter(Boolean);

  if (!moduleData.length) {
    return;
  }

  moduleData.sort((a, b) => a.start - b.start);

  const today = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'America/Detroit', year: 'numeric', month: '2-digit', day: '2-digit'
  }).format(new Date());
  const todayMidnight = parseDate(today);
  let target = moduleData.find((module) => (
    todayMidnight >= module.start && todayMidnight <= module.end
  ));

  if (target) {
    target.moduleEl.classList.add('module-current');
    target.moduleEl.setAttribute('aria-current', 'true');
  }

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
