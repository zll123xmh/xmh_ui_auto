import datetime
import keyword

import allure,pytest
from playwright.sync_api import Page
from pages_object.add_cart_page import CartPage
from datetime import datetime

SHOPPING_NAME = "苹果手机"
SHOPPING_NAME2 = "电池"
class TestReg:

    @pytest.mark.parametrize("keyword",[(SHOPPING_NAME)])
    def test_add_success(self,keyword,page:Page):

        add_cart_page = CartPage(page)

        add_cart_page.add_cart_page(keyword)

    @pytest.mark.parametrize("keyword",[(SHOPPING_NAME2)])
    def test_add_fail(self,keyword,page:Page):

        add_cart_page = CartPage(page)

        add_cart_page.add_cart_page(keyword)