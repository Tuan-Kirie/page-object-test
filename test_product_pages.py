import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


@pytest.mark.skip
@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 pytest.param(
                                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                     marks=pytest.mark.xfail),
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(driver, url):
    # url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, url)
    page.open()
    page.product_can_be_add_to_card()


@pytest.mark.skip
@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver, url):
    page = ProductPage(driver, url)
    page.open()
    page.guest_cant_see_success_message_after_add_to_basket()


@pytest.mark.skip
@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(driver, url):
    page = ProductPage(driver, url)
    page.open()
    page.guest_cant_see_success_message_before_add_to_basket()


@pytest.mark.skip
@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(driver, url):
    page = ProductPage(driver, url)
    page.open()
    page.message_disappeared_after_adding_product_to_basket()


@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"])
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver, url):
    page = ProductPage(driver, url)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, page.driver.current_url)
    basket_page.check_item_presence()
