from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class LoginPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    customer_login = (By.CSS_SELECTOR, '[ng-click="customer()"]')
    bank_manager_login = (By.CSS_SELECTOR, '[ng-click="manager()"]')

    def __init__(self):
        super(LoginPage, self).__init__()

    def open_login_page(self):
        self.driver.get(self.url)

    def click_customer_login_button(self):
        customer_login_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.customer_login))
        customer_login_element.click()

    def click_bank_manager_login_button(self):
        customer_login_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.bank_manager_login))
        customer_login_element.click()