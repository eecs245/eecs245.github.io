---
title: "Agents"
nav_exclude: true
---

# Website Agent Notes

- Treat a lab or homework as released when its schedule event has the released assignment link, usually `problems:`, or when the user explicitly says it has been released.
- Lab and homework titles should be plain text whether released or unreleased. Do not use `<b>`, `<strong>`, or Markdown bold in lab/homework `title:` fields.
- Homework events use `type: hw`; do not change them to `type: homework`.
- Before publishing lab/homework solutions, verify the private source against the already-released student-facing artifact. Do not infer the source only from the directory name (`private/labs/labNN`, `private/homeworks/hwNN`); compare the source assignment title/date and non-solutions PDF against the current `website/resources/.../<assignment>.pdf`, and search adjacent sources if they do not match.
- After publishing solutions, verify the assignment page title, homepage/module `title:`, non-solutions PDF title/date, and solutions PDF title/date all refer to the same assignment before reporting completion.
