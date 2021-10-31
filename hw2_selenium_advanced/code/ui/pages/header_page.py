from static_variables import CLICK_RETRY
from ui.pages.base_page import BasePage
from ui.locators.header_page_locators import HeaderPageLocators
from selenium.webdriver.support.wait import TimeoutException


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

    def click_on_tab(self, tab_name, timeout=10):
        self.click(
            locator=(
                self.locators.CENTER_MODULE_BUTTON_LOCATOR_TEMPLATE[0],
                self.locators.CENTER_MODULE_BUTTON_LOCATOR_TEMPLATE[1].format(tab_name)
            ),
            timeout=timeout
        )
        # if tab_name == 'profile':
        #     self.click(self.locators.PROFILE_BUTTON_LOCATOR, timeout)
        # elif tab_name == 'statistics':
        #     self.click(self.locators.STATISTICS_BUTTON_LOCATOR, timeout)
        # elif tab_name == 'dashboard':
        #     self.click(self.locators.DASHBOARD_BUTTON_LOCATOR, timeout)
        # elif tab_name == 'segments':

        if tab_name == 'dashboard':
            import ui.pages.dashboard_page as dp
            return dp.DashboardPage(self.driver)
        elif tab_name == 'segments':
            import ui.pages.segments_list_page as slp
            return slp.SegmentsListPage(self.driver)
