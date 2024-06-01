from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class OpenAccountPage(PageObject):

        process_button = (By.CSS_SELECTOR, '[type = "submit"]')

        def __init__(self, driver):
            super(OpenAccountPage, self).__init__(driver=driver)

        # Seleciona primeiro cliente
        def select_first_customer(self):
            select_element = WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, 'userSelect')))
            Select(select_element).select_by_visible_text('Hermoine Granger')

        # Seleciona primeira moeda
        def select_first_coin(self):
            select_element = WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, 'currency')))
            Select(select_element).select_by_visible_text('Dollar')

        # Clica em "Processar"
        def click_process_button(self):
            process_button_element = WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(self.process_button))
            process_button_element.click()

        # Verifica se alerta é exibido
        def is_alert_visible(self):
            alert = WebDriverWait(self.driver, 5).until(expected_conditions.Alert)
            return alert

        # Clica em "Ok" do alerta
        def click_alert(self):
            alert = WebDriverWait(self.driver, 5).until(expected_conditions.Alert)
            alert.accept()