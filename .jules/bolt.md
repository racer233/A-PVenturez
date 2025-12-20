## 2025-02-18 - [Resource Hints in Static Sites]
**Learning:** In a pure static site environment (no build system) using third-party CDNs (Tailwind Play, Google Fonts), performance optimizations are strictly limited to HTML-level techniques. `preconnect` and `dns-prefetch` become critical for reducing the waterfall latency, especially for chained resources like fonts.
**Action:** Always verify `preconnect` tags are present for external CDNs in static HTML projects.
