from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class CustomerPage(PageObject):

    url_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    url_costumer_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    login_button = (By.CSS_SELECTOR, '[type="submit"]')
    logout_button = (By.CSS_SELECTOR, '[ng-show="logout"]')

    user_list_customer = (By.ID, 'userSelect')

    welcome_message = (By.CLASS_NAME, 'fontBig ng-binding')

    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)

    # Abre página de cliente
    def is_url_customer(self):
      return self.is_url(self.url_customer)

    # Seleciona o primeiro cliente
    def select_first_customer(self):
        first_customer_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, 'userSelect')))
        Select(first_customer_element).select_by_visible_text('Hermoine Granger')

    # Clica no botão "Login"
    def click_login_button(self):
        login_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.login_button))
        login_button_element.click()

    # Valida página atual
    def is_url_customer_account(self):
        url_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.logout_button ))
        if (url_element.is_displayed()):
            return self.driver.current_url == self.url_costumer_account