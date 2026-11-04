from playwright.sync_api import Page
from pages_object.base_page import BasePage

class CartPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        self.input_keyword = page.locator("//input[@name='keyword']")
        self.search_name_button = page.get_by_role("button",name="搜    索")
        self.phone_link = page.get_by_role("link",name="苹果 (Apple) iPhone 6 (A1586) 16GB 金色 移动联通电信4G手机")
        self.add_cart_button = page.locator("#joinCarButton")
        # print(page.locator("#joinCarButton").count())
        self.order_button = page.locator("//span[@class='shopCar_T_span3']")
        self.buy_button = page.get_by_role("link",name="结算")

    def add_cart_page(self,keyword:str):

        self.input_keyword.wait_for(state="visible", timeout=10000)

        self.input_text(self.input_keyword,keyword)

        self.search_name_button.wait_for(state="visible", timeout=10000)

        self.click(self.search_name_button)

        self.phone_link.wait_for(state="visible", timeout=10000)

        self.click(self.phone_link)

        self.add_cart_button.wait_for(state="visible", timeout=10000)

        self.click(self.add_cart_button)

        self.order_button.wait_for(state="visible", timeout=10000)

        self.click(self.order_button)

        self.buy_button.wait_for(state="visible", timeout=10000)

        self.click(self.buy_button)