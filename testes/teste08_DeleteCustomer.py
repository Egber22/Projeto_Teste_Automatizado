from pages.ListPage import ListPage
from pages.ManagerPage import ManagerPage


class Test_DeleteCustomer:
    def test_addCustomers(self, setup):
        login_page = setup
        login_page.click_bank_manager_login_button()

        login_manager_page = ManagerPage(driver=login_page.driver)
        login_manager_page.click_customers_button()

        delete_customer_page = ListPage(driver=login_page.driver)
        delete_customer_page.search_custumer()
        delete_customer_page.click_delete_button()
        assert delete_customer_page.is_delete_button_visible(),'Cliente não deletado'