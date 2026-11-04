from playwright.sync_api import Page,Locator
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def input_text(self,locator: Locator,text: str):
        locator.wait_for(state="visible",timeout=10000)
        locator.fill(text)


    def click(self,locator: Locator):
        locator.wait_for(state="visible",timeout=10000)
        locator.click()