from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from project.supports.common_functions import *
from project.pages.base_page import Page


class BmiPage(Page):
    _metric_tab = (By.XPATH, "//a[.='Metric Units']")
    _age_txt = (By.NAME, 'cage')
    _male_rab = (By.ID, 'csex1')
    _female_rab = (By.ID, 'csex2')
    _height_txt = (By.ID, "cheightmeter")
    _weight_txt = (By.ID, 'ckg')
    _calculate_btn = (By.XPATH, "//input[@alt='Calculate']")
    _result_lbl = (By.CLASS_NAME, 'bigtext')

    def __init__(self, browser):
        self.driver = browser
        self.base_url = "https://www.calculator.net/bmi-calculator.html"

    def select_metric_tab(self):
        self.click(*self._metric_tab)

    def fill_form(self, age, gender, height, weight):
        self.fill(*self._age_txt, with_text=age)
        if gender == 'male':
            self.click(*self._male_rab)
        else:
            self.click(*self._female_rab)
        self.fill(*self._height_txt, with_text=height)
        self.fill(*self._weight_txt, with_text=weight)
        self.click(*self._calculate_btn)

    def get_result(self):
        return self.text(*self._result_lbl)
