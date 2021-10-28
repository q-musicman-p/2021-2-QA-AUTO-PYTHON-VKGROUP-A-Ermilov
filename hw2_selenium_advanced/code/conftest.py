import pytest
import logging
from webdriver_manager.chrome import ChromeDriverManager

from ui.fixtures import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--url', default='http://www.python.org')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')

    return {'url': url}


def get_driver(download_dir=None):
    options = Options()
    if download_dir is not None:
        options.add_experimental_option("prefs", {"download.default_directory": download_dir})

    manager = ChromeDriverManager(version='latest', log_level=logging.NOTSET)
    browser = webdriver.Chrome(executable_path=manager.install(), options=options)

    browser.maximize_window()
    return browser

@pytest.fixture(scope='function')
def driver(config, temp_dir):
    browser = get_driver(download_dir=temp_dir)
    # url = config['url']
    # browser.get(url)

    yield browser

    browser.quit()


