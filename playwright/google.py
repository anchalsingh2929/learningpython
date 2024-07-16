import time
from playwright.sync_api import Page, expect

def test_has_title(page):
    page.goto("https://youtube.com/")
    page.get_by_placeholder("Search", exact=True).fill("lyfofvipin_tech")
    time.sleep(3)
    page.get_by_role("button",name="Search",exact=True).click()
    page.get_by_role("button",name="Search",exact=True).click()
    time.sleep(6.7)

  