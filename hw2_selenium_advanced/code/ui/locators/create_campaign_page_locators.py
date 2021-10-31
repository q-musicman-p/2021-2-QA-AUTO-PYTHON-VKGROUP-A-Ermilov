from selenium.webdriver.common.by import By
from ui.locators.header_page_locators import HeaderPageLocators


class CreateCampaignPageLocators(HeaderPageLocators):
    TRAFFIC_LIST_ITEM_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, '_traffic')]"
    )
    MAIN_URL_INPUT_LOCATOR = (
        By.XPATH,
        "//div[@class='js-main-url-wrap']//input"
    )
    CAMPAIGN_NAME_INPUT_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'campaign-name')]//input"
    )
    BANNER_LOCATOR = (
        By.XPATH,
        "//div[contains(@id, 'patterns_banner')]"
    )
    UPLOAD_BANNER_PICTURE_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'bannerForm')]//div[contains(@class, 'upload-module-wrapper')]/input"
    )
    CREATE_CAMPAIGN_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'footer__button')]/button[@data-class-name='Submit']"
    )
