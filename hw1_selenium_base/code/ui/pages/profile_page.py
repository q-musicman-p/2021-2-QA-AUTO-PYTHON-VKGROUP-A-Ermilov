from ui.pages.base_page import BasePage
from ui.locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    locators = ProfilePageLocators()

    def fill_contact_information(self, fio, phone):
        self.fill_field(self.locators.FIO_FIELD_LOCATOR, fio)
        self.fill_field(self.locators.PHONE_FIELD_LOCATOR, phone)
        self.click(self.locators.SAVE_BUTTON_LOCATOR)
