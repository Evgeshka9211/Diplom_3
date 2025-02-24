import allure

from pages.base_page import BasePage
from locators.recovery_locators import RecoveryLocators as RL
from data import Urls


class RecoveryPasswordPage(BasePage):

    @allure.step('Открытие страницы "Восстановление пароля"')
    def open_forgot_password_page(self):
        self.open_url(Urls.FORGOT_PASSWORD_URL)

    @allure.step('Получения заголовка')
    def check_title(self):
        return self.check_exist_element(RL.TITLE)

    @allure.step('Ввод данных в поле ввода "Email"')
    def input_email(self, email):
        self.set_text(RL.FILED_EMAIL, email)

    @allure.step('Проверка наличия поля ввода "Пароль"')
    def check_exist_field_password(self):
        return self.check_exist_element(RL.FIELD_PASSWORD)

    @allure.step('Ввод данных в поле "Пароль"')
    def input_password(self, password):
        self.set_text(RL.FIELD_PASSWORD, password)

    @allure.step('Получение статуса обводки поля ввода "Пароль"')
    def check_stroke_field_password(self):
        if self.find_element_visibility(RL.FIELD_ACTIVE_PASSWORD):
            return True

    @allure.step('Получение статуса поля ввода "Пароль"')
    def check_activ_fild_password(self):
        if self.find_element_visibility(RL.FIELD_ACTIVE_PASSWORD):
            return True

    @allure.step('Предусловие для кнопки "Показать/скрыть"')
    def precondition_for_button_show_hide(self, email):
        self.open_forgot_password_page()
        self.input_email(email)
        self.click_element_if_clickable(RL.BUTTON_RECOVERY)