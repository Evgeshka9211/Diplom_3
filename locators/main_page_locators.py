from selenium.webdriver.common.by import By

class MainPageLocators:

    """ Кнопка "Конструктор" """
    BUTTON_CONSTRUCTOR = (By.XPATH, '//*[text() = "Конструктор"]')

    """ Кнопка "Лента Заказов" """
    BUTTON_ORDER_FEED = (By.XPATH, '//p[contains(.,"Лента Заказов")]')

    """ Кнопка булки "R2-D3" """
    BUTTON_INGREDIENT_R2_D3 = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')

    """ Кнопка "Оформить заказ" """
    BUTTON_ORDER = (By.XPATH, '//*[text()="Оформить заказ"]')

    """ Текст "идентификатор заказа" """
    ID_ORDER_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')

    """ Id оформленного заказа """
    ID_ORDER = (By.XPATH, './/h2[contains(@class, "text text_type_digits-large")]')

    """ Кнопка "Закрыть" """
    BUTTON_CLOSE = (By.XPATH, '//button[contains(@class,"close")]')

    """ Заголовок окна ингредиента """
    TITLE_INGREDIENT_WINDOW = (By.XPATH, '//*[text() = "Детали ингредиента"]')

    """ Счетчик у булки "R2-D3" """
    INGREDIENT_COUNTER = (By.XPATH, './/p[contains(@class, "counter_counter")]')

    """ Корзина заказов """
    BASKET_ORDER = (By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]')