import datetime

import allure,pytest
from playwright.sync_api import Page
from pages_object.reg_page import RegPage
from datetime import datetime
USERNAME = datetime.now().strftime("zll123_456-%Y%m%d%H%M%S")
PASSWORD = "190110zll"
PHONE_NUMBER = "18691957634"
EMAIL_ADDRESS = "zll123_456@163.com"
class TestReg:

    @pytest.mark.parametrize("username,password,phone_number,email_address",
                             [(USERNAME,PASSWORD,PHONE_NUMBER,EMAIL_ADDRESS),])
    def test_reg(self,username,password,phone_number,email_address,page:Page):

        register_page = RegPage(page)

        register_page.reg_page(username,password,phone_number,email_address)

