from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_BUTTON_LOCATOR = (
        By.XPATH,
        '//div[contains(@class, "responseHead-module-button")]'
    )
    EMAIL_FIELD_LOCATOR = (By.NAME, 'email')
    PWD_FIELD_LOCATOR = (By.NAME, 'password')
    SUBMIT_BUTTON_LOCATOR = (
        By.XPATH,
        '//div[contains(@class, "authForm-module-button")]'
    )
    INVALID_LOGIN_OR_PWD_MESSAGE_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'formMsg')]"
    )
    UNCORRECT_EMAIL_MESSAGE_LOCATOR = (
        By.XPATH,
        '//div[contains(@class, "notify-module-error")]'
    )
