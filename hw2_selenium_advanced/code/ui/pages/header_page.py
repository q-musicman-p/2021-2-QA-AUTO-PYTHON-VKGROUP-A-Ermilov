from static_variables import CLICK_RETRY
from ui.pages.base_page import BasePage
from ui.locators.header_page_locators import HeaderPageLocators
from selenium.webdriver.support.wait import TimeoutException


class UnknowTabNameException(Exception):
    pass


class HeaderPage(BasePage):

    locators = HeaderPageLocators()
    url = None

    def click_on_logout_button(self):
        for i in range(CLICK_RETRY):
            try:
                self.click(self.locators.RIGHT_BUTTON_LOCATOR)
                self.click(self.locators.LOGOUT_LINK_LOCATOR)
                return
            except TimeoutException:
                if i == CLICK_RETRY - 1:
                    raise

    def click_on_tab(self, tab_name):
        if tab_name == 'profile':
            tab_locator = self.locators.PROFILE_BUTTON_LOCATOR
        elif tab_name == 'statistics':
            tab_locator = self.locators.STATISTICS_BUTTON_LOCATOR
        else:
            raise UnknowTabNameException(f'Unknow tab name {tab_name}!')

        self.click(tab_locator, 10)

