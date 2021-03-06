from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from project.supports.common_functions import *
from project.pages.base_page import Page
from project.pages.page_object_partern import PageObjectPattern


class GoogleSearchPage(Page, PageObjectPattern):
    search_box_txt = (By.NAME, 'q')

    def __init__(self, browser):
        self.driver = browser
        self.base_url = "https://google.com"
        PageObjectPattern(self, browser)

    def search(self, query):
        self.fill(*self._search_box_txt, with_text=query)
