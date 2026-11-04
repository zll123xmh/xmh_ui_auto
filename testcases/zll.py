from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://email.163.com")
    frame = page.frame_locator("//iframe[contains(@id, 'x-URS-iframe')]")
    frame.locator("//input[@name='email']").fill("zll123_456")
    frame.locator("//input[@name='password']").fill("190110-zll")
    frame.locator("//a[@id='dologin']").click()
    time.sleep(3)
    browser.close()