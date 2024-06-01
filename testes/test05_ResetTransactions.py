from pages.CustomerPage import CustomerPage
from pages.TransactionsPage import TransactionsPage

class Test_ResetTransactions:
    def test_reset_transactions(self, setup):
        login_page = setup
        login_page.click_customer_login_button()
        customer_page = CustomerPage(driver=login_page.driver)
        customer_page.select_first_customer()
        customer_page.click_login_button()

        transactions_page = TransactionsPage(driver=login_page.driver)

        transactions_page.click_on_transactions()
        transactions_page.click_on_reset()
        transactions_page.click_back()
        assert customer_page.is_url_customer_account(), 'URL não encontrada!'