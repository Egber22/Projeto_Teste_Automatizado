from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ManagerPage(PageObject):

    url_manger = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    add_customer = (By.CSS_SELECTOR, '[ng-click="addCust()"]')

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)

    def is_url_manager(self):
        return self.is_url(self.url_manger)


