from pages.AddCustPage import AddCustPage
from pages.ManagerPage import ManagerPage

class Test_AddCustomers:

    def test_addCustomer (self, setup):

        login_page = setup
        login_page.click_bank_manager_login_button()

        login_manager_page = ManagerPage(driver=login_page.driver)
        login_manager_page.click_add_customer_button()

        login_addCust_page = AddCustPage(driver=login_page.driver)
        login_addCust_page.type_text()
        login_addCust_page.click_add_customer_button()
        login_addCust_page.click_alert()
        assert login_addCust_page.is_customer_added() == '', 'Mensagem exibida não corresponde a mensagem esperada'
