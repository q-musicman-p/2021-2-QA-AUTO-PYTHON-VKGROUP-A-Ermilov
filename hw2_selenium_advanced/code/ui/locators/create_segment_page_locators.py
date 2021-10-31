from selenium.webdriver.common.by import By
from ui.locators.header_page_locators import HeaderPageLocators


class CreateSegmentPageLocators(HeaderPageLocators):
    IFRAME_SEGMENT_APPLICATIONS_AND_GAMES_CATEGORY_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'adding-segments-item') and " +
        "(text()='Приложения и игры в соцсетях' or text()='Apps and games in social networks')]"
    )
    IFRAME_CONDITION_CHECKBOX_LOCATOR = (
        By.XPATH,
        "//input[contains(@class, 'adding-segments')]"
    )
    IFRAME_SUBMIT_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'adding-segments')]//button[@data-class-name='Submit']"
    )
    SEGMENT_NAME_INPUT_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'input_create-segment')]//input"
    )
    SUBMIT_SEGMENT_BUTTON_LOCATOR = (
        By.XPATH,
        "//div[contains(@class,'create-segment')]//button[@data-class-name='Submit']"
    )
