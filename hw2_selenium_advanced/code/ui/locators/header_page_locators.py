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
    PROFILE_BUTTON_LOCATOR = (
        By.XPATH,
        '//a[contains(@href, "/profile")]'
    )
    STATISTICS_BUTTON_LOCATOR = (
        By.XPATH,
        '//a[contains(@href, "/statistics")]'
    )
