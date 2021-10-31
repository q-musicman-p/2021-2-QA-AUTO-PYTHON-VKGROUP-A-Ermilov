import allure

from ui.locators.create_campaign_page_locators import CreateCampaignPageLocators
from ui.pages.header_page import HeaderPage
from utils import decorators


class CreateCampaignPage(HeaderPage):

    locators = CreateCampaignPageLocators()
    url = 'https://target.my.com/campaign/new'

    @allure.step('Create new traffic banner to {main_url}')
    def create_new_traffic_banner(self, main_url, campaign_name,  banner_picture_path, timeout=None):
        self.click(self.locators.TRAFFIC_LIST_ITEM_LOCATOR, timeout=timeout)
        decorators.wait(
            self.fill_field, locator=self.locators.MAIN_URL_INPUT_LOCATOR, text=main_url, timeout=timeout
        )
        decorators.wait(
            self.fill_field, locator=self.locators.CAMPAIGN_NAME_INPUT_LOCATOR, text=campaign_name, timeout=timeout
        )
        self.click(self.locators.BANNER_LOCATOR, timeout=timeout)
        decorators.wait(
            self.fill_field,
            locator=self.locators.UPLOAD_BANNER_PICTURE_LOCATOR, text=banner_picture_path, timeout=timeout, clear=False
        )

        self.click(self.locators.CREATE_CAMPAIGN_BUTTON_LOCATOR, timeout=timeout)

        self.logger.debug(f'New traffic banner to {main_url} are created')
        import ui.pages.dashboard_page as dp
        return dp.DashboardPage(self.driver)


