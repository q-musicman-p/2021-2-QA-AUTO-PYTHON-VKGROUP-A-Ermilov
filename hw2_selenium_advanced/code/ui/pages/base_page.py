import time

import pytest

from ui.locators.base_page_locators import BasePageLocators
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from static_variables import CLICK_RETRY, BASE_TIMEOUT


class PageNotLoadedException(Exception):
    pass


class BasePage(object):

    locators = BasePageLocators()
    url = None

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=BASE_TIMEOUT):
        """
        :return:
         True, if current url equals page's url and
         False, if page haven't url or page have different url in different cases
        """

        if self.url is None:
            return False  # we return False, if page have diff url or havenot it

        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True

        raise PageNotLoadedException(f'{self.url} did not open in {timeout}sec for {self.__class__.__name__}.\n'
                                     f'Current url: {self.driver.current_url}.')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = BASE_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
            except ElementClickInterceptedException:
                if i == CLICK_RETRY - 1:
                    raise

    def fill_field(self, locator, text, timeout=None):
        field = self.find(locator, timeout=timeout)
        field.clear()
        field.send_keys(text)
