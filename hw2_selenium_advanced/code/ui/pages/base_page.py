import allure
import logging
import time

from ui.locators.base_page_locators import BasePageLocators
from selenium.common import exceptions
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
        self.logger = logging.getLogger('test')
        is_opened = self.is_opened()

        self.logger.debug(f"Init {self.__class__} with is_opened={is_opened}")

    def is_opened(self, timeout=BASE_TIMEOUT):
        """
        :return:
         True, if current url equals page's url and
         False, if page haven't url or page have different url in different cases
        """

        if self.url is None:
            return False

        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.strip('#/') == self.url:
                return True

        raise PageNotLoadedException(f'{self.url} did not open in {timeout}sec for {self.__class__.__name__}.\n'
                                     f'Current url: {self.driver.current_url}.')

    @allure.step
    def wait(self, timeout=None):
        if timeout is None:
            timeout = BASE_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step("Find {locator}")
    def find(self, locator, timeout=None):
        self.logger.debug(f'find {locator}')
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Click on {locator}")
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))

                self.logger.debug(f'click on {locator} (try={i})')
                elem.click()
                return
            except exceptions.StaleElementReferenceException:
                self.logger.debug(f'StaleElementReferenceException in click on {locator}')
                if i == CLICK_RETRY - 1:
                    raise
            except exceptions.ElementClickInterceptedException:
                self.logger.debug(f'ElementClickInterceptedException in click on {locator}')
                if i == CLICK_RETRY - 1:
                    raise

    @allure.step('Fill field {locator} into {text}')
    def fill_field(self, locator, text, timeout=None, clear=True):
        field = self.find(locator, timeout=timeout)

        if clear:
            self.logger.debug(f'clear field {locator}')
            field.clear()

        self.logger.debug(f'write in field {locator} with {text}')
        field.send_keys(text)

