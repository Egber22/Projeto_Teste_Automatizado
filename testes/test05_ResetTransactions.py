from pages.CustomerPage import CustomerPage

class Test_ResetTransactions:
    def test_reset_transactions(self, setup):
        login_page = setup
        login_page.click_customer_login_button()
        customer_page = CustomerPage(driver=login_page.driver)
        customer_page.select_first_customer()
        customer_page.click_login_button()
        account_page.add_deposit()
        account_page.add_balance()
        account_page.update_balance()
        account_page.confirmme_balance()

account_page.click_on_transactions()
account_page.click_on_reset()
account_page.click_back()

assert account_page.check_balance_result(), 'Teste não realizado'