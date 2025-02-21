import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators as MPL
from data import Urls

class TestMainPage:

    @allure.title('Переход по нажатию на кнопку «Конструктор»')
    def test_open_constructor(self, driver):
        mp = MainPage(driver)
        mp.open_reg_page()
        mp.click_element_if_clickable(MPL.BUTTON_CONSTRUCTOR)
        assert mp.get_url() == Urls.MAIN_PAGE_URL

    @allure.title('Переход по нажатию на кнопку "Лента заказов"')
    def test_open_orders(self, driver):
        mp = MainPage(driver)
        mp.open_reg_page()
        mp.click_element_if_clickable(MPL.BUTTON_ORDER_FEED)
        assert mp.get_url() == Urls.FEED_URL

    @allure.title('Открытие окна ингредиента')
    def test_open_window_ingredient(self, driver):
        mp = MainPage(driver)
        mp.open_main_page()
        mp.click_element_if_clickable(MPL.BUTTON_INGREDIENT_R2_D3)
        assert mp.check_clickable_order_button()

    @allure.title('Закрытие окна ингредиента')
    def test_close_window_ingredient(self, driver):
        mp = MainPage(driver)
        mp.precondition_close_window()
        mp.click_element_if_clickable(MPL.BUTTON_CLOSE)
        assert mp.check_clickable_order_button()

    @allure.title('Изменение счетчика ингредиента')
    def test_counter_add_ingredient(self, driver):
        mp = MainPage(driver)
        mp.open_main_page()
        pre_result = mp.get_count_value()
        mp.add_filling_to_order()
        post_result = mp.get_count_value()
        assert pre_result < post_result

    @allure.title('Создание заказа авторизованным пользователем')
    def test_placing_order(self, driver, test_data):
        pp = ProfilePage(driver)
        mp = MainPage(driver)
        pp.authorization(test_data)
        mp.add_filling_to_order()
        mp.click_element_if_clickable(MPL.BUTTON_ORDER)
        assert mp.check_placing_order() == 'идентификатор заказа'