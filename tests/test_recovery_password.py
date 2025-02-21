import allure

from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPasswordPage
from locators.login_locators import LoginLocators
from locators.recovery_locators import RecoveryLocators as RL

class TestRecoveryPassword:

    @allure.title('Открытие страницы "Восстановление пароля"')
    def test_open_recovery_page(self, driver):
        lp = LoginPage(driver)
        lp.open_login_page()
        lp.click_element_if_clickable(LoginLocators.BUTTON_RECOVERY_PASSWORD)
        rp = RecoveryPasswordPage(driver)
        assert rp.check_title()

    @allure.title('Ввод почты и нажатие на кнопку "Восстановить"')
    def test_input_data_and_click_button(self, driver, test_data):
        rpp = RecoveryPasswordPage(driver)
        rpp.open_forgot_password_page()
        rpp.input_email(test_data)
        rpp.click_element_if_clickable(RL.BUTTON_RECOVERY)
        assert rpp.check_exist_field_password()

    @allure.step('Нажатие кнопки "Показать/скрыть"')
    def test_button_show_hide(self, driver, test_data):
        rpp = RecoveryPasswordPage(driver)
        rpp.precondition_for_button_show_hide(test_data)
        rpp.input_password(test_data)
        rpp.click_element_if_visibility(RL.BUTTON_SHOW_HIDE)
        assert (rpp.check_stroke_field_password() and rpp.check_activ_fild_password())
