from selenium.webdriver.common.by import By


class HeaderPageLocators:
    RIGHT_BUTTON_LOCATOR = (
        By.XPATH,
        '//div[contains(@class, "right-module-rightButton")]'
    )
    LOGOUT_LINK_LOCATOR = (
        By.XPATH,
        '//a[contains(@href, "/logout")]'
    )
    CENTER_MODULE_BUTTON_LOCATOR_TEMPLATE = (
        By.XPATH,
        '//a[contains(@href, "{}")]'
    )
    PROFILE_BUTTON_LOCATOR = (
        By.XPATH,
        '//a[contains(@href, "/profile")]'
    )
    STATISTICS_BUTTON_LOCATOR = (
        By.XPATH,
        '//a[contains(@href, "/statistics")]'
    )
    DASHBOARD_BUTTON_LOCATOR = (
        By.XPATH,
        '//a[contains(@href, "/dashboard")]'
    )
