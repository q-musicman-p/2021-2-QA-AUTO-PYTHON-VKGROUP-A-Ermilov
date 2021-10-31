import allure

from ui.locators.create_segment_page_locators import CreateSegmentPageLocators
from ui.pages.header_page import HeaderPage


class CreateSegmentPage(HeaderPage):
    locators = CreateSegmentPageLocators()
    url = 'https://target.my.com/segments/segments_list/new'

    @allure.step('Create new apps and games segment {segment_name}')
    def create_new_segment(self, segment_name, timeout=None):
        self.click(self.locators.IFRAME_SEGMENT_APPLICATIONS_AND_GAMES_CATEGORY_LOCATOR, timeout=timeout)
        self.click(self.locators.IFRAME_CONDITION_CHECKBOX_LOCATOR, timeout=timeout)
        self.click(self.locators.IFRAME_SUBMIT_BUTTON_LOCATOR, timeout=timeout)
        self.fill_field(self.locators.SEGMENT_NAME_INPUT_LOCATOR, text=segment_name, timeout=timeout)
        self.click(self.locators.SUBMIT_SEGMENT_BUTTON_LOCATOR, timeout=timeout)

        self.logger.debug(f'New segment {segment_name} is created')
        import ui.pages.segments_list_page as slp
        return slp.SegmentsListPage(self.driver)