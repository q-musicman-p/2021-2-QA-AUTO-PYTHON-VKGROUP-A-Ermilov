from selenium.webdriver.common.by import By


class ProfilePageLocators:
    FIO_FIELD_LOCATOR = (
        By.XPATH,
        '//div[@data-name="fio"]/div/input'
    )
    PHONE_FIELD_LOCATOR = (
        By.XPATH,
        '//div[@data-name="phone"]/div/input'
    )
    SAVE_BUTTON_LOCATOR = (
        By.XPATH,
        '//div[@class="button__text"]'
    )
