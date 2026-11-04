import allure,pytest

from playwright.sync_api import Page

from pages_object.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)
        with allure.step("切换到iframe"):

            self.login_frame = self.page.frame_locator("//iframe[contains(@id,'x-URS-iframe')]")

        with allure.step("填写账号"):

            self.input_username = self.login_frame.locator("//input[@name='email']")

        with allure.step("填写密码"):

            self.input_password = self.login_frame.locator("//input[@name='password']")

        with allure.step("成功登录"):

            self.login_button = self.login_frame.locator("//a[@id='dologin']")

    def login_page(self,username,password):

        self.input_username.wait_for(state="visible",timeout=10000)

        self.input_text(self.input_username,username)

        self.input_password.wait_for(state="visible",timeout=10000)

        self.input_text(self.input_password,password)

        self.login_button.wait_for(state="visible",timeout=10000)

        self.click(self.login_button)