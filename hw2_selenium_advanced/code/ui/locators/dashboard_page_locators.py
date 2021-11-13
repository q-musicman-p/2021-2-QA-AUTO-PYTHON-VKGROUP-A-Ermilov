from selenium.webdriver.common.by import By
from ui.locators.header_page_locators import HeaderPageLocators


class DashboardPageLocators(HeaderPageLocators):
    CREATE_CAMPAIGN_LINK_LOCATOR = (
        By.XPATH,
        "//a[contains(@href, '/campaign/new')]"
    )
    CREATE_CAMPAIGN_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'headControlsWrapper')]//div[contains(@class, 'createButton')]/div/div"
    )
    ALL_CAMPAIGN_LINKS_LOCATOR = (
        By.XPATH,
        "//div[@data-entity-type='campaign']/a"
    )
    CAMPAIGN_LINK_LOCATOR_TEMPLATE = (
        By.XPATH,
        ALL_CAMPAIGN_LINKS_LOCATOR[1] + "[@title='{}']"
    )
