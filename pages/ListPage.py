from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class ListPage(PageObject):

    search_field = (By.CSS_SELECTOR,'[ng-model="searchCustomer"]')

    account_number = '1001'
    account_number_customer = (By.CSS_SELECTOR, '["ng-binding ng-scope"]')

    first_name_customer = 'Albus'
    first_name_list = (By.CLASS_NAME,'ng-binding')
    first_name_header = (By.XPATH,"//thead/tr/td[1]/a")

    table = (By.XPATH, "//tbody/tr/td[1]")

    delete_button = (By.CSS_SELECTOR,'[ng-click="deleteCust(cust)"]')

    def __init__(self, driver):
        super(ListPage, self).__init__(driver=driver)

    # Pesquisa a conta do cliente
    def search_account_custumer(self):
        search_custumer_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.search_field))
        search_custumer_element.send_keys(self.account_number)

    # Pesquisa o "Primeiro nome" do cliente
    def search_first_name_customer(self):
        search_customer_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.search_field))
        search_customer_element.send_keys(self.first_name_customer)

    # Verifica se o nome é pesquisado
    def is_name_searched(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.first_name_list))
        element_text = element.text
        return element_text

    # Clica no botão "Delete"
    def click_delete_button(self):
        delete_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.delete_button))
        delete_button_element.click()

    # Verifica se o nome o botão "Delete" está visible
    def is_delete_button_visible(self):
        delete_button_visible = WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element(self.delete_button))
        return delete_button_visible

    # Verifica a ordenação por nome
    def verify_order_by_name(self):
         click_first_names_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.first_name_header))
         click_first_names_element.click()
         click_first_names_element.click()

    # Colocar a coluna de "Primeiros nomes" em uma lista
    def first_elements_column(self):
        first_names_elements = self.driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
        first_names = [elem.text for elem in first_names_elements]
        return first_names