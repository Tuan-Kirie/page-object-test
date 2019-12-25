import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_can_be_add_to_card(self):
        cost = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text
        name = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_NAME).text
        buy_button = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_ADD_TO_BASKET_BUTTON)
        buy_button.click()
        self.solve_quiz_and_get_code()
        cost_basket = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_BASKET_TOTAL_PRICE).text
        product_name_on_basket = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_BASKET_NAME_OF_PRODUCT).text
        assert cost == cost_basket, \
            "Cost's are differently"
        assert name == product_name_on_basket, \
            "Names are differently"

    def guest_cant_see_success_message_after_add_to_basket(self):
        buy_button = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_ADD_TO_BASKET_BUTTON)
        buy_button.click()
        assert self.the_element_is_not_present(*ProductPageLocators.PRODUCT_PAGE_SUCCEED_MESSAGE), \
            "Success message on page"

    def guest_cant_see_success_message_before_add_to_basket(self):
        assert self.the_element_is_not_present(*ProductPageLocators.PRODUCT_PAGE_SUCCEED_MESSAGE), \
            "Success message on page"

    def message_disappeared_after_adding_product_to_basket(self):
        buy_button = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_ADD_TO_BASKET_BUTTON)
        buy_button.click()
        time.sleep(1)
        assert self.the_element_is_disappeared(*ProductPageLocators.PRODUCT_PAGE_SUCCEED_MESSAGE),\
            "Message are no disappeared adter adding to busket"