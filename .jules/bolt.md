## 2025-05-20 - Tailwind CDN Production Usage
**Learning:** The project uses the Tailwind Play CDN (`<script src="https://cdn.tailwindcss.com"></script>`) which is intended for development. This blocks rendering and forces the browser to compile CSS on the client side every page load, preventing standard CSS optimizations like extraction, minification, and critical CSS inlining.
**Action:** Since a build step (architectural change) is out of scope, I will mitigate this by adding `preconnect` resource hints to establish early connections to the CDNs, but the core bottleneck remains.
