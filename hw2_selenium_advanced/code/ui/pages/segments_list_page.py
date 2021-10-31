from time import sleep

from ui.locators.segments_list_page_locators import SegmentsListPageLocators
from ui.pages.create_segment_page import CreateSegmentPage
from ui.pages.header_page import HeaderPage
from selenium.common.exceptions import TimeoutException


class SegmentsListPage(HeaderPage):
    locators = SegmentsListPageLocators()
    url = 'https://target.my.com/segments/segments_list'

    def click_on_create_new_segment_button(self):
        try:
            self.click(self.locators.CREATE_NEW_SEGMENT_BUTTON_LOCATOR)
        except TimeoutException:
            self.click(self.locators.CREATE_NEW_SEGMENT_LINK_LOCATOR)

        return CreateSegmentPage(self.driver)

    def create_new_segment(self, segment_name, timeout=None):
        create_segment_page = self.click_on_create_new_segment_button()
        create_segment_page.create_new_segment(segment_name, timeout=timeout)

    def remove_segment(self, segment_name):
        self.click(
            (
                self.locators.REMOVE_SEGMENT_LOCATOR_TEMPLATE[0],
                self.locators.REMOVE_SEGMENT_LOCATOR_TEMPLATE[1].format(segment_name)
            )
        )

        self.click(self.locators.CONFIRM_REMOVE_SEGMENT_BUTTON_LOCATOR)