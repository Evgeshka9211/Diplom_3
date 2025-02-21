from pages.base_page import BasePage
import allure
from data import Urls


class LoginPage(BasePage):
    @allure.step('Открытие страницы "Вход"')
    def open_login_page(self):
        self.open_url(Urls.LOGIN_URL)
