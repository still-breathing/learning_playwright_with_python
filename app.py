# this is a sample for playwright automation
print("Sample playwright automation")
from playwright.sync_api import sync_playwright
with sync_playwright() as playwright: # instantiating the playwright clear this concept later
    # Launch a browser
    chromium_browser = playwright.chromium.launch(headless=False, slow_mo=2000) #trying to see what happens if true actions are done in the background

    # Create a new page
    page = chromium_browser.new_page()

    # Visit playwright url
    page.goto("https://playwright.dev/python") # visits the python section
    # Locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs") # Locating and saving
    # there can be more link types
    docs_button.hover()
    docs_button.highlight()
    docs_button.click()

    # close the browser
    chromium_browser.close()



