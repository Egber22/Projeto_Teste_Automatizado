from pages.AddCustPage import AddCustPage
from pages.ManagerPage import ManagerPage

class Test_AddCustomerDuplicate:

    def test_addCustomerDuplicate (self, setup):

        login_page = setup
        login_page.click_bank_manager_login_button()

        login_manager_page = ManagerPage(driver=login_page.driver)
        login_manager_page.click_add_customer_button()

        addCust_duplicate_page = AddCustPage(driver=login_page.driver)
        addCust_duplicate_page.type_duplicate_name()
        addCust_duplicate_page.click_add_customer_button()

        assert addCust_duplicate_page.text_alert() == 'Cliente pode está duplicado', 'Exceção não foi identificada na tela'

        addCust_duplicate_page.click_alert()

