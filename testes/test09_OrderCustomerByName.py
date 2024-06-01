from pages.ListPage import ListPage
from pages.ManagerPage import ManagerPage

class Test_OrderCustomerByName:

    def test_order_customer_by_name (self, setup):

        login_page = setup
        login_page.click_bank_manager_login_button()

        login_manager_page = ManagerPage(driver=login_page.driver)
        login_manager_page.click_customers_button()

        order_customer_by_name_page = ListPage(driver=login_page.driver)
        order_customer_by_name_page.verify_order_by_name()
        assert order_customer_by_name_page.first_elements_column() == sorted(order_customer_by_name_page.first_elements_column()), 'Não está em ordem alfabética crescente'