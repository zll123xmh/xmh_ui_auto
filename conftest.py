import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, Browser
import pytest,time

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,args=['--start-maximized'])
        yield browser
        browser.close()
Base_Url = "http://localhost"
@pytest.fixture(scope="function")
def page(browser:Browser):
    page = browser.new_page(no_viewport=True )
    page.goto(f"{Base_Url}/index.php?c = cart & a = succeed")
    yield page
    time.sleep(3)
    page.close()

