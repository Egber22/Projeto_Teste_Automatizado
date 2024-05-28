import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class AccountPage(PageObject):

    add_deposit = (By.CSS_SELECTOR, '[ng-click="deposit()"]')
    #add_deposit = (By.CLASS_NAME, 'btn btn-lg tab btn-primary')
    amount = (By.CSS_SELECTOR, '[type="number"]')
    deposit_button = (By.CSS_SELECTOR, '[type="submit"]')
    message_sucessfull_element = (By.CSS_SELECTOR, '[ng-show="message"]')
    message_sucessfull = 'Deposit Successful'

    # Clicar no botão Adicionar
    def __init__(self, driver):
        super(AccountPage, self).__init__(driver=driver)

    def add_balance(self):
        select_element1 = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_deposit))
        #Select(select_element).element_to_be_clickable(self.add_deposit)
        select_element1.click()

    # Enviar valor no campo deposito
    def update_balance(self):
        select_element2 = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(self.amount))
        #Select(select_element).element_to_be_clickable(self.add_deposit)
        select_element2.send_keys(200)

    # Confirmar novo saldo
    def confirm_balance(self):
        select_element3 = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(self.deposit_button))
        #Select(select_element).element_to_be_clickable(self.deposit_button)
        select_element3.click()

    # Pegar o texto da mensagem de sucesso
    def has_message_sucessfull(self):
        #select_element4 = WebDriverWait(self.driver, 4).until(
          #  expected_conditions.visibility_of_element_located(self.message_sucessfull_element))
        time.sleep(3)
        message_element = self.driver.find_element(*self.message_sucessfull_element)
        is_message_displayed = message_element.is_displayed()
        has_message_text = message_element.text == self.message_sucessfull
        return is_message_displayed and has_message_text


