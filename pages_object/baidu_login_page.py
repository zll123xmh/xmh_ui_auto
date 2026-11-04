from pages_object.base_page import BasePage
from playwright.sync_api import Page

class BaiduPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.baidu_login = page.locator("//a[@id='s-top-loginbtn']")
        self.baidu_input_name = page.locator("//input[@name='userName']")
        self.baidu_input_password = page.get_by_role("textbox",name="密码")
        self.read_box = page.get_by_role("checkbox",name="阅读并接受")
        self.baidu_login_button = page.get_by_role("button",name="登录")

    def baidu_login_page(self,username,password):

        self.baidu_login.wait_for(state="visible",timeout=10000)
        self.click(self.baidu_login)

        self.baidu_input_name.wait_for(state="visible", timeout=10000)
        self.input_text(self.baidu_input_name,username)

        self.baidu_input_password.wait_for(state="visible", timeout=10000)
        self.input_text(self.baidu_input_password,password)

        self.read_box.wait_for(state="visible", timeout=10000)
        self.click(self.read_box)

        self.baidu_login_button.wait_for(state="visible",timeout=10000)
        self.click(self.baidu_login_button)

