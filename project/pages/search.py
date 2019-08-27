from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from project.supports.common_functions import *
from project.pages.base_page import Page

class GoogleSearchPage(Page):

    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, browser,url="https://google.com"):
        self.driver = browser
        self.URL = url

    def load(self):
        self.driver.get(self.URL)

    def search(self, query):
        self.find_element(*self.SEARCH_INPUT).send_keys(query)
