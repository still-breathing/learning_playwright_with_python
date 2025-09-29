#!/usr/bin/env python3
"""
Testing if the correct url is visited

"""

from playwright.sync_api import sync_playwright

def verify_url(page, pattern, description):
    current_url: object = page.url
    print(f"Current url: {current_url}")
    if current_url == pattern:
        print(f"Success: {description} page is loaded")
    else:
        print(f"Failure: {description} page is not loaded")
    print(f"function {page,pattern,description} is completed")
with sync_playwright() as pl:
    my_ff_browser = pl.firefox.launch(headless=False, slow_mo= 5000)
    my_url_1= "https://www.google.com/"
    my_url_2 = "https://playwright.dev/python"
    my_page = my_ff_browser.new_page() # why not my_ff_browser.goto(my_url)? because goto is a page object and not a browser object
    my_page.goto(my_url_1)
    verify_url(my_page, my_url_1, "Google")

    my_page.goto(my_url_2)
    verify_url(my_page, "https://playwight.dev/", "Playwright - fail test")
    print("Operation completed")
