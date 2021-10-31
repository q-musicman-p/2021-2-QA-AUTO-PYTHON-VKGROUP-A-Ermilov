from static_variables import BASE_TIMEOUT
from ui.pages.base_page import BasePage
from ui.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    locators = LoginPageLocators()
    url = 'https://target.my.com'

    def try_to_login(self, email, password, timeout=BASE_TIMEOUT):
        self.click(self.locators.ENTER_BUTTON_LOCATOR, timeout=timeout)
        self.fill_field(self.locators.EMAIL_FIELD_LOCATOR, email)
        self.fill_field(self.locators.PWD_FIELD_LOCATOR, password)
        self.click(self.locators.SUBMIT_BUTTON_LOCATOR)

        self.logger.debug('Loggining...')