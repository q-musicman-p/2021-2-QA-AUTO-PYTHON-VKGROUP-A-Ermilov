from selenium.webdriver.common.by import By
from ui.locators.header_page_locators import HeaderPageLocators


class SegmentsListPageLocators(HeaderPageLocators):
    CREATE_NEW_SEGMENT_LINK_LOCATOR = (
        By.XPATH,
        "//a[contains(@href, '/segments/segments_list/new/')]"
    )
    CREATE_NEW_SEGMENT_BUTTON_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'button_submit') and @data-class-name='Submit']"
    )
    SEGMENT_LINK_LOCATOR_TEMPLATE = (
        By.XPATH,
        "//div[contains(@class, 'cells-module-name')]/a[@title='{}']"
    )
    REMOVE_SEGMENT_LOCATOR_TEMPLATE = (
        By.XPATH,
        SEGMENT_LINK_LOCATOR_TEMPLATE[1] +
        "/ancestor::div[contains(@class, 'main-module-Cell')]/following-sibling::div[4]/span"
    )
    CONFIRM_REMOVE_SEGMENT_BUTTON_LOCATOR = (
        By.XPATH,
        "//button[contains(@class, 'button button_confirm-remove')]"
    )
