from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject
from selenium.webdriver.support.select import Select

class AccountPage(PageObject):

    add_deposit = (By.CSS_SELECTOR, '[ng-click="deposit()"]')
    amount = (By.CSS_SELECTOR, '[type="number"]')
    deposit_button = (By.CSS_SELECTOR, '[type="submit"]')
    message_sucessfull_element = (By.CSS_SELECTOR, '[ng-show="message"]')
    message_sucessfull = 'Deposit Successful'
    withdrawl_button = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
    message_withdrawl_sucessfull = 'Transaction successful'
    infos_account = (By.CLASS_NAME, '[class ="ng-binding"]')
    message_error_element = (By.CSS_SELECTOR, '[ng-show="message"]')
    message_error = 'Transaction Failed. You can not withdraw amount more than the balance.'
    withdrawl_deposit = (By.CSS_SELECTOR, '[ng-click="withdrawl()"]')
    account_number = (By.CLASS_NAME, 'ng-binding')

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver=driver)

    # Clicar no botão Adicionar
    def add_balance(self):
        add_balance_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_deposit))
        add_balance_element.click()

    # Enviar valor no campo deposito
    def update_balance(self):
        update_balance_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(self.amount))
        update_balance_element.send_keys(200)

    # Confirmar novo saldo
    def confirm_balance(self):
        confirm_balance_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(self.deposit_button))
        confirm_balance_element.click()

    # Pegar o texto da mensagem de sucesso
    def has_message_sucessfull(self):
        message_element = self.driver.find_element(*self.message_sucessfull_element)
        is_message_displayed = message_element.is_displayed()
        has_message_text = message_element.text == self.message_sucessfull
        return is_message_displayed and has_message_text

    # Clicar no botão Withdrawl
    def withdrawl_balance(self):
        withdrawl_balance_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.withdrawl_button))
        withdrawl_balance_element.click()

    # Informar um valor para ser retirado da conta
    def update_withdrawl_balance(self):
        update_withdrawl_element = WebDriverWait(self.driver, 7).until(
            expected_conditions.visibility_of_element_located(self.amount))
        update_withdrawl_element.send_keys(50)

    # Confirmar retirada
    def confirm_withdrawl(self):
        confirm_withdrawl_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.deposit_button))
        confirm_withdrawl_element.click()

    # Pegar o texto da mensagem de retirada feita com sucesso
    def has_withdrawl_message_sucessfull(self):
        message_withdrawl_element = self.driver.find_element(*self.message_sucessfull_element)
        is_message_withdrawl_displayed = message_withdrawl_element.is_displayed()
        has_withdrawl_message_text = message_withdrawl_element.text == self.message_withdrawl_sucessfull
        return is_message_withdrawl_displayed and has_withdrawl_message_text

    #Retirar valor maior que o saldo
    def update_withdrawl_above_balance(self):
        withdrawl_upto_balance_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(self.amount))
        withdrawl_upto_balance_element.send_keys(10000)

    #Validar mensagem de retirada não autorizada
    def has_message_transaction_failed(self):
        message_fail = self.driver.find_element(*self.message_error_element)
        is_message_fail_displayed = message_fail.is_displayed()
        has_message__error_text = message_fail.text == self.message_error
        return is_message_fail_displayed and has_message__error_text

    # Selecionar  outra conta
    def select_second_account(self):
        second_account_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located((By.ID, 'accountSelect')))
        Select(second_account_element).select_by_visible_text('1002')

    def verify_change_account(self):
        select_element2 = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(self.account_number))


