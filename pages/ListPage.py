import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class ListPage(PageObject):
    url_list = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    search_field = (By.CSS_SELECTOR,'[ng-model="searchCustomer"]')
    account_number = '1001'
    account_number_customer = (By.CSS_SELECTOR, '["ng-binding ng-scope"]')
    delete_button = (By.CSS_SELECTOR,'[ng-click="deleteCust(cust)"]')
    def __init__(self, driver):
        super(ListPage, self).__init__(driver=driver)

    def is_url_list(self):
        return self.is_url(self.url_list)

    def search_custumer(self):
        search_custumer_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.search_field))
        search_custumer_element.send_keys(self.account_number)

    def click_delete_button(self):
        delete_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.delete_button))
        delete_button_element.click()

    def is_delete_button_visible(self):
        delete_button_visible = WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element(self.delete_button))
        return delete_button_visible