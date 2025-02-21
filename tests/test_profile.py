import allure
from pages.profile_page import ProfilePage
from locators.profile_locators import ProfileLocators as PL

class TestProfile:

    @allure.title('Проверка открытия страницы "Личный кабинет"')
    def test_open_profile_page(self, driver, test_data):
        pp = ProfilePage(driver)
        pp.authorization(test_data)
        pp.click_element_if_clickable(PL.BUTTON_PROFILE_PAGE)
        assert pp.check_open_page()

    @allure.title('Проверка перехода на страницу "История заказов"')
    def test_open_history(self, driver, test_data):
        pp = ProfilePage(driver)
        pp.precondition_for_tests(test_data)
        assert pp.open_history_page()

    @allure.title('Проверка разлогина по нажатию "Выйти"')
    def test_exit(self, driver, test_data):
        pp = ProfilePage(driver)
        pp.precondition_for_tests(test_data)
        assert pp.exit()