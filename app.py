# this is a sample for playwright automation
#!/usr/bin/env python3
print("Sample playwright automation")
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:  # instantiating the playwright clear this concept later
    """
    Starts Playwright when entering the block
    Assigns the Playwright instance to pl
    Automatically stops Playwright when exiting the block
    Ensures proper cleanup even if errors occur
    """
    # Launch a browser
    chromium_browser = playwright.chromium.launch(headless=False,
                                                  slow_mo=2000)  # trying to see what happens if true actions are done in the background

    # Create a new page
    page = chromium_browser.new_page()

    # Visit playwright url
    page.goto("https://playwright.dev/python")  # visits the python section
    # Locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")  # Locating and saving get by role
    # there can be more link types
    print("Docs:", page.url)
    docs_button.hover()
    docs_button.highlight()
    docs_button.click()

    # close the browser
    chromium_browser.close()
