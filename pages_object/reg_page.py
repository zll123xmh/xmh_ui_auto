from playwright.sync_api import Page
from pages_object.base_page import BasePage

class RegPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        #self.register_button = page.get_by_role("link",name="注册")
        self.input_username = page.locator("//input[@name='username']")
        self.input_password = page.locator("//input[@name='password']")
        self.reg_input_username = page.locator("//input[@name='userpassword2']")
        self.phone_number = page.locator("//input[@name='mobile_phone']")
        self.email_address = page.locator("//input[@name='email']")
        self.reg_button = page.get_by_role("button",name="注册")

    def reg_page(self,username,password,phone_number,email_name):

        #self.register_button.wait_for(state="visible",timeout=10000)

        #self.click(self.register_button)

        self.input_username.wait_for(state="visible", timeout=10000)

        self.input_text(self.input_username,username)

        self.input_username.wait_for(state="visible", timeout=10000)

        self.input_text(self.input_password, password)

        self.reg_input_username.wait_for(state="visible", timeout=10000)

        self.input_text(self.reg_input_username,password)

        self.phone_number.wait_for(state="visible", timeout=10000)

        self.input_text(self.phone_number,phone_number)

        self.email_address.wait_for(state="visible", timeout=10000)

        self.input_text(self.email_address,email_name)

        self.reg_button.wait_for(state="visible", timeout=10000)

        self.click(self.reg_button)