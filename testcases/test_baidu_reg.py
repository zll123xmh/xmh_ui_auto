import datetime

import allure,pytest
from playwright.sync_api import Page
from pages_object.baidu_reg_page import RegPage
from datetime import datetime
#USERNAME = datetime.now().strftime("zll123_456-%Y%m%d%H%M%S")
USERNAME = "zll123_456"
PHONE_NUMBER = "18691957634"
PASSWORD = "190110@zll"
VERIFY_CODE = "190110"
class TestReg:

    @pytest.mark.parametrize("username,phone_number,password,verify_code",[(USERNAME,PHONE_NUMBER,PASSWORD,VERIFY_CODE)])
    def test_reg(self,username,phone_number,password,verify_code,page:Page):

        register_page = RegPage(page)
        register_page.reg_page(username,phone_number,password,verify_code)