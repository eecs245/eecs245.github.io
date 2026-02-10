# Accessibility Issues (WCAG 2.1)

This document records the WCAG 2.1 issues identified in the site audit.

## 1) Missing alt text on meaningful images
- **WCAG SC:** 1.1.1 Non-text Content
- **Issue:** Images appear to convey content but have no `alt` text.
- **Affected files:**
  - `env-setup.md:273`
  - `syllabus.md:347`

## 2) Missing iframe titles
- **WCAG SC:** 4.1.2 Name, Role, Value
- **Issue:** Several embedded `iframe` elements do not have a `title` attribute.
- **Affected files:**
  - `calendar.md:30`
  - `env-setup.md:35`
  - `post-mt2-practice.md:69`
  - `post-mt2-practice.md:95`
  - `post-mt2-practice.md:168`
  - `post-mt2-practice.md:328`

## 3) Insufficient color contrast
- **WCAG SC:** 1.4.3 Contrast (Minimum)
- **Issue:** Multiple text/background combinations are below minimum contrast requirements for normal text.
- **Examples found:**
  - Module labels in `_sass/custom/module.scss:126` to `_sass/custom/module.scss:130` combined with white text (from generated `.label` styles) fail contrast in several cases:
    - `#FFFFFF` on `#F2C76E` ≈ `1.59:1`
    - `#FFFFFF` on `#15c791` ≈ `2.19:1`
    - `#FFFFFF` on `#779fcd` ≈ `2.75:1`
    - `#FFFFFF` on `#E94C4B` ≈ `3.75:1`
  - Zoom button in `calendar.md:20`:
    - `#FFFFFF` on `#e6804d` ≈ `2.78:1`
  - "New!" badges in:
    - `next.md:62`
    - `next.md:63`
    - `next.md:64`
    - `next.md:81`
    - `next.md:96`
    - Contrast example: `#FFFFFF` on `#17a2b8` ≈ `3.04:1`

## 4) Expand/collapse state not exposed to assistive tech
- **WCAG SC:** 4.1.2 Name, Role, Value
- **Issue:** Expandable code buttons toggle visual state but do not expose semantic state (`aria-expanded`) or controlled region (`aria-controls`).
- **Affected files:**
  - Button markup: `_layouts/module.html:40`
  - Toggle script: `_layouts/module.html:131`

## 5) Invalid/fragile semantic structure in staff templates
- **WCAG SC:** 1.3.1 Info and Relationships; 4.1.1 Parsing
- **Issue:** Staff templates include invalid or fragile HTML structure that can interfere with assistive parsing.
- **Examples:**
  - `div` inside heading:
    - `_layouts/staffer.html:14`
    - `_layouts/staffer-no-bio.html:14`
  - Nested paragraph structure:
    - `_layouts/staffer.html:17` and `_layouts/staffer.html:23`
    - `_layouts/staffer-no-bio.html:17` and `_layouts/staffer-no-bio.html:23`

## 6) Information conveyed primarily by color
- **WCAG SC:** 1.4.1 Use of Color
- **Issue:** Calendar legend describes event meaning primarily via color categories (red/blue/turquoise/orange), which may not be sufficient for all users.
- **Affected file:**
  - `calendar.md:12` to `calendar.md:17`
