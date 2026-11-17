import datetime

from playwright.sync_api import Page
from pages_object.baidu_login_page import BaiduPage
import pytest
from datetime import datetime
USERNAME_SUCCESS = "18792626320"
PASSWORD_SUCCESS = "190110@zll"
USERNAME_FAILURE = "18691957634"
PASSWORD_FAILURE = "190110@zll"


class TestBaiduLogin:

    @pytest.mark.parametrize('username,password', [(USERNAME_SUCCESS,PASSWORD_SUCCESS)])
    def test_baidu_success_login(self,username,password,page:Page):
        baidu_page = BaiduPage(page)
        baidu_page.baidu_login_page(username,password)

    @pytest.mark.parametrize('username,password', [(USERNAME_FAILURE,PASSWORD_FAILURE)])
    def test_baidu_failure_login(self,username:str,password:str,page:Page):
        baidu_page = BaiduPage(page)
        baidu_page.baidu_login_page(username,password)