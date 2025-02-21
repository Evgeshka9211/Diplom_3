import pytest

from selenium import webdriver
from data import Urls
from helper import StringHelper


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(options=options)
    browser.get(Urls.BASE_URL)
    yield browser
    browser.quit()

@pytest.fixture
def test_data():
    data = {
        'password': StringHelper.random_pass(),
        'email': StringHelper.random_email(),
        'name': StringHelper.random_name()
    }
    return data