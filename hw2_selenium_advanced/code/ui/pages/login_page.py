import pytest

from ui.pages.base_page import BasePage
from ui.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    locators = LoginPageLocators()
    url = 'https://target.my.com/'
