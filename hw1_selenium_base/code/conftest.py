from selenium.webdriver import Chrome
from ui.fixtures import *


@pytest.fixture(scope='function')
def driver():
    browser = Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()
