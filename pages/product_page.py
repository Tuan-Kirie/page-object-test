from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_can_be_add_to_card(self):
        cost = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text
        buy_button = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_ADD_TO_BASKET_BUTTON)
        buy_button.click()
        self.solve_quiz_and_get_code()
        cost_basket = self.driver.find_element(*ProductPageLocators.PRODUCT_PAGE_BASKET_TOTAL_PRICE).text
        assert cost == cost_basket, "Cost's are differently"
