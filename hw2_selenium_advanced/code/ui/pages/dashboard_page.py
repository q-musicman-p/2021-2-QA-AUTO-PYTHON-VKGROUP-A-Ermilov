import allure

from selenium.common.exceptions import TimeoutException
from ui.locators.dashboard_page_locators import DashboardPageLocators
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.header_page import HeaderPage


class DashboardPage(HeaderPage):

    locators = DashboardPageLocators()
    url = 'https://target.my.com/dashboard'

    @allure.step('Create new campaign {campaign_name}')
    def create_new_campaign(self, main_url, campaign_name,  picture_path, timeout=None):
        try:
            self.logger.debug('Not first try to create camp')
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON_LOCATOR)
        except TimeoutException:
            self.logger.debug('First try to create camp')
            self.click(self.locators.CREATE_CAMPAIGN_LINK_LOCATOR)

        create_campaign_page = CreateCampaignPage(self.driver)
        return create_campaign_page.create_new_traffic_banner(
            main_url=main_url,
            campaign_name=campaign_name,
            banner_picture_path=picture_path,
            timeout=timeout
        )

    @allure.step('Get list of campaigns')
    def campaigns_list(self):
        return self.get_list_of(self.locators.ALL_CAMPAIGN_LINKS_LOCATOR, timeout=7)
