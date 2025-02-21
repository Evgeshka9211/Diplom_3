import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators as MPL
from locators.profile_locators import ProfileLocators as PL
from locators.order_feed_locators import OrderPageLocators as OPL


class TestOrderFeed:

    @allure.title('Проверка открытия окна с информацией заказе')
    def test_open_order_window(self, driver):
        ofp = OrderFeedPage(driver)
        ofp.open_page()
        ofp.click_element_if_clickable(OPL.ORDER_OBJECT)
        assert ofp.check_order_window()

    @allure.title('Сравнение идентификатора заказа в ленте и в истории')
    def test_find_order_in_list(self, driver, test_data):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)
        pp.authorization(test_data)
        mp.add_filling_to_order()
        mp.click_element_if_clickable(MPL.BUTTON_ORDER)
        order_id = mp.get_order_id()
        mp.click_element_if_clickable(MPL.BUTTON_CLOSE)
        pp.click_element_if_clickable(PL.BUTTON_PROFILE_PAGE)
        pp.open_history_page()
        order_id_history = pp.found_order_at_history(order_id)
        mp.click_element_if_clickable(MPL.BUTTON_ORDER_FEED)
        order_id_order_feed = ofp.found_order_at_feed(order_id)
        assert order_id_order_feed and order_id_history

    @allure.title('Проверка изменения счетчика заказов')
    def test_today_orders_counter(self, driver, test_data):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)
        pp.authorization(test_data)
        mp.click_element_if_clickable(MPL.BUTTON_ORDER_FEED)
        pre_count = ofp.get_total_count_today()
        mp.click_element_if_clickable(MPL.BUTTON_CONSTRUCTOR)
        mp.add_filling_to_order()
        mp.click_element_if_clickable(MPL.BUTTON_ORDER)
        mp.click_element_if_clickable(MPL.BUTTON_CLOSE)
        mp.click_element_if_clickable(MPL.BUTTON_ORDER_FEED)
        post_count = ofp.get_total_count_today()
        assert post_count > pre_count

    @allure.title('Проверка появления нового заказа в ленте')
    def test_new_order_at_order_feed(self, driver, test_data):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)
        pp.authorization(test_data)
        mp.add_filling_to_order()
        mp.click_element_if_clickable(MPL.BUTTON_ORDER)
        order_id = mp.get_order_id()
        mp.click_element_if_clickable(MPL.BUTTON_CLOSE)
        mp.click_element_if_clickable(MPL.BUTTON_ORDER_FEED)
        assert ofp.found_order_at_feed(order_id)