from selenium import webdriver
from selenium.webdriver.common.by import By


class Page(object):
    """
    Base class that all page models can inherit from
    """

    def __init__(self, selenium_driver, base_url='http://google.com'):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def find(self, *loc):
        return self.driver.find_element(*loc)

    def all(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self, path):
        url = self.base_url + path
        self.driver.get(url)

    def click(self, *locator):
        try:
            element = self.find(*locator)
            if element is not None:
                element.click()
        except Exception as e:
            print(str(e))
            raise ("Error when clicking the element with path,'%s' in the conf/locators.conf file" % locator)

    def fill(self, *locator, with_text, clear=True):
        try:
            element = self.find(*locator)
            if element is not None:
                if clear is True:
                    element.clear()
                element.send_keys(with_text)

        except Exception as e:
            print(str(e))
            raise("Error when fill the element with path,'%s' in the conf/locators.conf file" % locator)

    def is_element_visible(self, *locator):
        if self.find(*locator) is not None:
            return True
        else:
            return False

    def text(self, *locator):
        if self.is_element_visible(*locator) is True:
            return self.find(*locator).text
