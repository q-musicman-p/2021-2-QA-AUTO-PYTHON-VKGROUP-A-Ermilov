from contextlib import contextmanager

import allure

from ui.locators.segments_list_page_locators import SegmentsListPageLocators
from ui.pages.create_segment_page import CreateSegmentPage
from ui.pages.header_page import HeaderPage
from selenium.common.exceptions import TimeoutException


class SegmentsListPage(HeaderPage):
    locators = SegmentsListPageLocators()
    url = 'https://target.my.com/segments/segments_list'

    def click_on_create_new_segment_button(self):
        try:
            self.logger.debug('Not first try to create new segment')
            self.click(self.locators.CREATE_NEW_SEGMENT_BUTTON_LOCATOR)
        except TimeoutException:
            self.logger.debug('First try to create new segment')
            self.click(self.locators.CREATE_NEW_SEGMENT_LINK_LOCATOR)

        return CreateSegmentPage(self.driver)

    @allure.step('Create new segment {segment_name}')
    def create_new_segment(self, segment_name, timeout=None):
        create_segment_page = self.click_on_create_new_segment_button()
        return create_segment_page.create_new_segment(segment_name, timeout=timeout)

    @allure.step('Remove segment {segment_name}')
    def remove_segment(self, segment_name, timeout=None):
        self.click(
            locator=(
                self.locators.REMOVE_SEGMENT_LOCATOR_TEMPLATE[0],
                self.locators.REMOVE_SEGMENT_LOCATOR_TEMPLATE[1].format(segment_name)
            ),
            timeout=timeout
        )

        self.click(self.locators.CONFIRM_REMOVE_SEGMENT_BUTTON_LOCATOR, timeout=timeout)

    @allure.step('Get list of segments')
    def segments_list(self):
        return self.get_list_of(self.locators.ALL_SEGMENTS_LINK_LOCATOR, timeout=7)

    @allure.step('New segment {segment_name}')
    @contextmanager
    def new_segment(self, segment_name, timeout=None):
        seg_list_page = self.create_new_segment(segment_name, timeout=timeout)

        yield seg_list_page

        seg_list_page.remove_segment(segment_name, timeout=timeout)
        assert segment_name not in self.segments_list()
