from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index.html file directly
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Take a screenshot of the head content by printing it to console or just screenshotting the body
        # Since resource hints are in head, they aren't visible in a screenshot.
        # But we can verify the page still loads correctly without errors.

        page.screenshot(path="verification/page_load.png")

        # Check if the links are in the DOM (head)
        # We can execute JS to get the head content
        head_html = page.evaluate("document.head.innerHTML")

        print("Checking for resource hints...")
        if 'rel="preconnect" href="https://fonts.googleapis.com"' in head_html:
            print("✅ fonts.googleapis.com preconnect found")
        else:
            print("❌ fonts.googleapis.com preconnect NOT found")

        if 'rel="preconnect" href="https://fonts.gstatic.com"' in head_html:
            print("✅ fonts.gstatic.com preconnect found")
        else:
            print("❌ fonts.gstatic.com preconnect NOT found")

        browser.close()

if __name__ == "__main__":
    verify_frontend()
