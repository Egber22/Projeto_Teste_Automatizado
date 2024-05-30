from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class TransactionsPage(PageObject):
    url_transactions = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    transactions_button = (By.CSS_SELECTOR, '[ng-click="transactions()"]')
    reset_button = (By.CSS_SELECTOR, '[ng-click="reset()"]')
    back_button = (By.CSS_SELECTOR, '[ng-click="back()"]')

    def __init__(self, driver):
        super(TransactionsPage, self).__init__(driver=driver)

    #Clicar em "Transactions"
    def click_on_transactions(self):
        transactions_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.transactions_button))
        transactions_element.click()

    #Clicar em "Reset"
    def click_on_reset(self):
        reset_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.reset_button))
        reset_element.click()

    #Clicar em "Voltar"
    def click_back(self):
        back_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.back_button))
        back_button_element.click()

