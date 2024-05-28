from pages.OpenAccountPage import AccountPage
from pages.CustomerPage import CustomerPage


class Test_AddDeposit:
    def test_add_deposit(self, setup):
        login_page = setup
        login_page.click_customer_login_button()

        customer_page = CustomerPage(driver=login_page.driver)
        customer_page.select_first_customer()
        customer_page.click_login_button()

        account_page = AccountPage(driver=login_page.driver)
        account_page.add_balance()
        account_page.update_balance()
        account_page.confirm_balance()

        assert account_page.has_message_sucessfull(), 'Saldo não atualizado'