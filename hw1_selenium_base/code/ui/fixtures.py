from random import randint
import pytest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.header_page import HeaderPage
from ui.pages.profile_page import ProfilePage


@pytest.fixture
def r_number(down_limit=0, up_limit=10**9):
    return str(randint(down_limit, up_limit))


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def header_page(driver):
    return HeaderPage(driver=driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver=driver)
