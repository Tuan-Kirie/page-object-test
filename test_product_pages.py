import time

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(driver):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, url)
    page.open()
    page.product_can_be_add_to_card()
