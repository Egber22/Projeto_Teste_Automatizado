from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject

class CustomerPage(PageObject):
    url_transactions = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    user_list_customer = (By.ID, 'userSelect')
    login_button = (By.CSS_SELECTOR, '[type="submit"]')
    welcome_message = (By.CLASS_NAME, 'fontBig ng-binding')
    url_costumer_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    # Clicar no botão Adicionar
    def __init__(self, driver):
        super(TransactionsPage, self).__init__(driver=driver)

    def add_balance(self):
        select_element1 = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_deposit))
        select_element1.click()
