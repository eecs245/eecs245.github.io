---
layout: page
title: 👩‍🏫 Staff
description: A listing of the EECS 245 course staff.
nav_order: 6
---

# 👩‍🏫 Staff

{% assign course_staff = site.staffers | sort: "staff_order" %}
{% for staffer in course_staff %}
{{ staffer }}
{% endfor %}
