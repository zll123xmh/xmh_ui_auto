import datetime

from playwright.sync_api import Page
from pages_object.baidu_login_page import BaiduPage
import pytest
from datetime import datetime
USERNAME = "18782626320"
PASSWORD = "190110zll"
class TestBaiduLogin:

    @pytest.mark.parametrize('username,password', [(USERNAME,PASSWORD)])
    def test_baidu_login(self,username,password,page:Page):
        baidu_page = BaiduPage(page)
        baidu_page.baidu_login_page(username,password)