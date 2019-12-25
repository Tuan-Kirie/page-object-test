from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def check_item_presence(self):
        assert self.the_element_is_not_present(*BasketPageLocators.BASKET_PAGE_ITEM)

