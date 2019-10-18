from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from project.supports.common_functions import *
from project.pages.base_page import Page
from project.pages.page_object_partern import PageObjectPattern

class BmiPage(Page, PageObjectPattern):
    __metric_tab = (By.XPATH, "//a[.='Metric Units']")
    __age_txt = (By.NAME, 'cage')
    __male_rab = (By.ID, 'csex1')
    __female_rab = (By.ID, 'csex2')
    __height_txt = (By.ID, "cheightmeter")
    __weight_txt = (By.ID, 'ckg')
    __calculate_btn = (By.XPATH, "//input[@alt='Calculate']")
    __result_lbl = (By.CLASS_NAME, 'bigtext')

    def __init__(self, browser):
        self.driver = browser
        self.base_url = "https://www.calculator.net/bmi-calculator.html"
        PageObjectPattern.__init__(self, browser)

    def select_metric_tab(self):
        self.click(*self.__metric_tab)

    def fill_form(self, age, gender, height, weight):
        self.fill(*self.__age_txt, with_text=age)
        if gender == 'male':
            self.click(*self.__male_rab)
        else:
            self.click(*self.__female_rab)
        self.fill(*self.__height_txt, with_text=height)
        self.fill(*self.__weight_txt, with_text=weight)
        self.click(*self.__calculate_btn)

    def get_result(self):
        return self.text(*self.__result_lbl)
