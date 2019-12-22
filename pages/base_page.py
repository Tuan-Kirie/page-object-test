from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, selector, locator):
        try:
            self.driver.find_element(selector, locator)
        except NoSuchElementException:
            return False
        return True
