from playwright.sync_api import Page
from pages_object.login_page import LoginPage

import pytest,allure

USERS_NAME = "zll123_456"
PASSWORD = "190110-zll"
class TestLogin:

    @allure.feature("首页")
    @allure.story("登录")
    @allure.title("163邮箱用户登录")
    @pytest.mark.parametrize('username,password', [(USERS_NAME,PASSWORD)])
    def test_login_001_case(self,username,password,page: Page):
        login_page = LoginPage(page)
        login_page.login_page(username,password)