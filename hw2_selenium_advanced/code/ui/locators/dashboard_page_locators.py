from selenium.webdriver.common.by import By
from ui.locators.header_page_locators import HeaderPageLocators


class DashboardPageLocators(HeaderPageLocators):
    CREATE_CAMPAIGN_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'headControlsWrapper')]//div[contains(@class, 'createButton')]/div/div"
    )
    COMPANY_HREF_LOCATOR_TEMPLATE = (
        By.XPATH,
        "//div[@data-entity-type='campaign']/a[@title='{}']"
    )
