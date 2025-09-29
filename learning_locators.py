print("More about locators")
# import playwright
# from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright
pl = sync_playwright().start()
# these steps seem to be memorized, can it be made into a function?
browser = pl.firefox.launch(headless=False, slow_mo= 5000)
page = browser.new_page()
my_url = "https://bootswatch.com/default"
target_page = page.goto(url=my_url)
#target_page = page.goto("https://playwright.dev/python")

