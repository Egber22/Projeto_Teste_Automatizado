import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject


class OpenAccountPage(PageObject):

    process_button = (By.CSS_SELECTOR, '[type = "submit"]')
    alert_button = 'Account created successfully with account Number :1021'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)

    def select_first_customer(self):
        select_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located((By.ID, 'userSelect')))
        Select(select_element).select_by_visible_text('Hermoine Granger')

    def select_first_coin(self):
        select_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located((By.ID, 'currency')))
        Select(select_element).select_by_visible_text('Dollar')

    def click_process_button(self):
        process_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.process_button))
        process_button_element.click()

    def click_alert(self):
        alert = WebDriverWait(self.driver, 4).until(expected_conditions.Alert)
        alert.accept()











