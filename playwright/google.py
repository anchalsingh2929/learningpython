import time
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://google.com/")
    page.get_by_role("a", title="Search").click()

    time.sleep(5)

