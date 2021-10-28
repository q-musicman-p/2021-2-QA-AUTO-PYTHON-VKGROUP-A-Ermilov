import pytest
from static_variables import EMAIL, PASSWORD
from ui.pages.login_page import LoginPage
from ui.pages.header_page import HeaderPage


class Base:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

        self.driver.get('https://target.my.com/')
        # assert 'myTarget' in self.driver.page_source

        self.login_page = LoginPage(driver)

    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.click(self.login_page.locators.ENTER_BUTTON_LOCATOR, timeout=15)
        self.login_page.fill_field(self.login_page.locators.EMAIL_FIELD_LOCATOR, EMAIL)
        self.login_page.fill_field(self.login_page.locators.PWD_FIELD_LOCATOR, PASSWORD)
        self.login_page.click(self.login_page.locators.SUBMIT_BUTTON_LOCATOR)

        return HeaderPage(self.driver)
