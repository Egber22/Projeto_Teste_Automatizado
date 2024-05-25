import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class CustomerPage(PageObject):
    url_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    user_list_customer = (By.ID, 'userSelect')
    login_button = (By.CSS_SELECTOR, '[type="submit"]')
    welcome_message = (By.CLASS_NAME, 'fontBig ng-binding')
    url_costumer_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'


    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)

    def is_url_customer(self):
        return self.is_url(self.url_customer)

    def select_first_customer(self):
        select_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located((By.ID, 'userSelect')))
        Select(select_element).select_by_visible_text('Hermoine Granger')

    def click_login_button(self):
        login_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.login_button))
        login_button_element.click()
        time.sleep(5)

    #def login_customer(self):
     #   welcome_message_element = self.driver.find_element(*self.welcome_message)

    def is_url_customer_account(self):
        return self.driver.current_url == self.url_costumer_account


