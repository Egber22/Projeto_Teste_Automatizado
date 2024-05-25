from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject

class LoginPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    customer_login = (By.CSS_SELECTOR, '[ng-click="customer()"]')

    def __init__(self):
        super(LoginPage, self).__init__()
    def open_login_page(self):
        self.driver.get(self.url)

    def click_customer_login_button(self):
        customer_login_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.customer_login))
        customer_login_element.click()