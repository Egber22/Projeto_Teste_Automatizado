import pytest
from pages.LoginPage import LoginPage

@pytest.fixture()
def setup():
    # Pre condicao: abrir o browser e acessar a página.
    login_page = LoginPage()
    login_page.open_login_page()

    yield login_page
    # Pos condicao
    login_page.close()