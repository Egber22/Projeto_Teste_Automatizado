from pages.CustomerPage import CustomerPage

class Test_SearchUser:
    def test_customer_login(self, setup):
        login_page = setup
        login_page.click_customer_login_button()

        customer_page = CustomerPage(driver=login_page.driver)
        customer_page.select_first_customer()
        customer_page.click_login_button()

        assert customer_page.is_url_customer_account(), 'URL não encontrada!'










