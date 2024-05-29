import time

from pages.ListPage import ListPage
from pages.ManagerPage import ManagerPage
class Test_searchCustomer:
    def test_search_customer(self, setup):
        login_page = setup
        login_page.click_bank_manager_login_button()

        login_manager_page = ManagerPage(driver=login_page.driver)
        login_manager_page.click_customers_button()

        search_customer_page = ListPage(driver=login_page.driver)
        search_customer_page.search_first_name_customer()
        assert search_customer_page.is_name_searched(),'Cliente não encontrado'
