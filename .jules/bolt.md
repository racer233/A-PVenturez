# Bolt's Journal - Critical Learnings

## 2024-05-22 - [Resource Hints Strategy]
**Learning:** For this static site, `dns-prefetch` is used for library CDNs and `preconnect` for Google Fonts. `fonts.gstatic.com` requires `crossorigin` while `fonts.googleapis.com` does not.
**Action:** Apply this pattern consistently when adding external resources.
