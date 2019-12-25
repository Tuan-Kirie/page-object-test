from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import MainPageLocators

class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        # self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, selector, locator):
        try:
            self.driver.find_element(selector, locator)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def the_element_is_not_present(self, selector, locator, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((selector, locator)))
        except TimeoutException:
            return True
        return False

    def the_element_is_disappeared(self, selector, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((selector, locator)))
        except TimeoutException:
            return False
        return True

    def go_to_basket_page(self):
        basket_button_link = self.driver.find_element(*MainPageLocators.GO_TO_BASKET_BUTTON)
        basket_button_link.click()
