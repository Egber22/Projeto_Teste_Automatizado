from pages.OpenAccountPage import OpenAccountPage
from pages.CustomerPage import CustomerPage

class Test_WithDrawlDeposit:

    def test_withdrawl_deposit(self, setup):
        login_page = setup
        login_page.click_customer_login_button()

        customer_page = CustomerPage(driver=login_page.driver)
        customer_page.select_first_customer()
        customer_page.click_login_button()

        account_page = OpenAccountPage(driver=login_page.driver)

        account_page.withdrawl_balance()
        account_page.update_withdrawl_balance()
        account_page.confirm_withdrawl()

        assert account_page.has_withdrawl_message_sucessfull(), 'Valor não retirado'