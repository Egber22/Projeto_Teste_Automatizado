from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class AddCustPage(PageObject):

    url_addcust = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'

    first_name= (By.CSS_SELECTOR, '[ng-click="addCust()"]')
    last_name = (By.CSS_SELECTOR, '[ng-model="lName"]')
    post_code = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    add_customer_button = (By.CSS_SELECTOR, '[type="submit"]')

    first_name_user = 'James'
    last_name_user = 'Potter'
    post_code_user = '0800'

    def __init__(self, driver):
        super(AddCustPage, self).__init__(driver=driver)

    def is_url_add_customer(self):
        return self.is_url(self.url_addcust)

    def type_text(self,first_name_user='teste'):
        type_text_element1 = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.first_name))
        type_text_element1.send_keys(self.first_name_user)

        type_text_element2 = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.last_name))
        type_text_element2.send_keys(self.last_name_user)

        type_text_element3 = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.post_code))
        type_text_element3.send_keys(self.post_code_user)

    def click_add_customer_button(self):
        add_customer_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_customer_button))
        add_customer_button_element.click()



