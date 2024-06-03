from pages.ManagerPage import ManagerPage
from pages.OpenAccountPage import OpenAccountPage

class Test_OpenAccount:
    def test_addCustomers(self, setup):

        login_page = setup
        login_page.click_bank_manager_login_button()

        login_manager_page = ManagerPage(driver=login_page.driver)
        login_manager_page.click_open_account_button()

        open_account_page = OpenAccountPage(driver=login_page.driver)
        open_account_page.select_first_customer()
        open_account_page.select_first_coin()
        open_account_page.click_process_button()
        assert open_account_page.is_alert_visible(), 'Cliente não foi adicionado.'
        open_account_page.click_alert()