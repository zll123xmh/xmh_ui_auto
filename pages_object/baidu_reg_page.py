from playwright.sync_api import Page
from pages_object.base_page import BasePage

class RegPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        #self.login_button = page.get_by_role("link",name="登录")
        #self.reg_button = page.get_by_role("link",name="立即注册")
        self.reg_input_username = page.get_by_role("textbox",name="用户名")
        self.reg_input_phone = page.get_by_role("textbox",name="手机号")
        self.input_password = page.get_by_role("textbox",name="密　码")
        #self.verify_code = page.get_by_role("button",name="获取验证码")
        self.reg_button = page.get_by_role("button",name="注册")

    def reg_page(self,username,phone_number,password):


        # self.login_button.wait_for(state="visible", timeout=10000)
        #
        # self.click(self.login_button)

        # self.reg_button.wait_for(state="visible", timeout=10000)
        #
        # self.click(self.reg_button)

        self.reg_input_username.wait_for(state="visible", timeout=10000)

        self.input_text(self.reg_input_username,username)

        self.reg_input_phone.wait_for(state="visible", timeout=10000)

        self.input_text(self.reg_input_phone,phone_number)

        self.input_password.wait_for(state="visible", timeout=1000)

        self.input_text(self.input_password,password)

        self.reg_button.wait_for(state="visible", timeout=10000)

        self.click(self.reg_button)