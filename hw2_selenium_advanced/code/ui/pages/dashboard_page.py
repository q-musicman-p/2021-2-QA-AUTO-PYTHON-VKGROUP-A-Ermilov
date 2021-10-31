from ui.locators.dashboard_page_locators import DashboardPageLocators
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.header_page import HeaderPage


class DashboardPage(HeaderPage):

    locators = DashboardPageLocators()
    url = 'https://target.my.com/dashboard'

    def create_new_campaign(self):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON_LOCATOR)

        return CreateCampaignPage(self.driver)
