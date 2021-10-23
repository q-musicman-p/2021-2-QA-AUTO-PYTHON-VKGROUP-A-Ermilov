import pytest
from static_variables import EMAIL, PASSWORD
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.header_page import HeaderPage
from ui.pages.profile_page import ProfilePage


class Base:

    @pytest.fixture(scope='function')
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.header_page: HeaderPage = request.getfixturevalue('header_page')
        self.profile_page: ProfilePage = request.getfixturevalue('profile_page')

    @pytest.fixture(scope='function', autouse=True)
    def login(self, setup):
        self.driver.get('https://target.my.com/')
        assert 'myTarget' in self.driver.page_source

        self.main_page.click(self.main_page.locators.ENTER_BUTTON_LOCATOR, timeout=15)
        self.main_page.fill_field(self.main_page.locators.EMAIL_FIELD_LOCATOR, EMAIL)
        self.main_page.fill_field(self.main_page.locators.PWD_FIELD_LOCATOR, PASSWORD)
        self.main_page.click(self.main_page.locators.SUBMIT_BUTTON_LOCATOR)
