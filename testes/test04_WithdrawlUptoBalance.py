from pages.AccountPage import AccountPage
from pages.CustomerPage import CustomerPage

class Test_WithDrawlUptoBalance:

    def test_withdrawl_deposit_availabel_balance(self, setup):
        login_page = setup

        login_page.click_customer_login_button()

        customer_page = CustomerPage(driver=login_page.driver)
        customer_page.select_first_customer()
        customer_page.click_login_button()

        account_page = AccountPage(driver=login_page.driver)

        account_page.withdrawl_balance()
        account_page.update_withdrawl_above_balance()
        account_page.confirm_withdrawl()

        assert account_page.has_message_transaction_failed(), 'Teste não realizado'