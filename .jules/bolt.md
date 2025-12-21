# Bolt's Journal

## 2024-05-22 - Missing Resource Hints
**Learning:** This project relies heavily on third-party CDNs (Tailwind Play, Font Awesome, Google Fonts) but completely lacks `preconnect` resource hints. This means the browser delays the DNS lookup and TCP handshake for these critical resources until it parses the CSS or encounters the script tags, adding unnecessary latency to the critical rendering path.
**Action:** Always check for external resource origins and add `<link rel="preconnect">` tags for them in the `<head>` to speed up connection setup.
