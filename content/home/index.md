---
# Files in this folder represent a Widget Page (homepage)
type: widget_page

# Homepage is headless, other widget pages are not.
headless: true

url: "/landing"
---

sections:
  - block: markdown
    id: section-1
    content:
      title: Section 1
      subtitle: A subtitle
      text: Add any **markdown** formatted content here - text, images, videos, galle
      <script src="https://cdn.jsdelivr.net/npm/p5@1.4.0/lib/p5.js"></script> <!-- load p5.js from CDN-->
      <script src = "particles.js"></script> <!-- this will pick our script  -->
