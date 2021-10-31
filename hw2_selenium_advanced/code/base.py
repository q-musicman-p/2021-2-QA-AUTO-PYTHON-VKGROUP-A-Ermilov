import os

import allure
import pytest

from static_variables import EMAIL, PASSWORD
from ui.pages.dashboard_page import DashboardPage
from ui.pages.login_page import LoginPage


class Base:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger):
        self.driver = driver
        self.logger = logger

        self.driver.get('https://target.my.com/')
        self.login_page = LoginPage(driver)

        self.logger.debug('Initial setup completed')

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_tests_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_tests_count:
            screenshot = os.path.join(temp_dir, 'failure.png')
            driver.get_screenshot_as_file(screenshot)
            allure.attach.file(screenshot, 'failure.png', attachment_type=allure.attachment_type.PNG)

            browser_log = os.path.join(temp_dir, 'browser.log')
            with open(browser_log, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")

            with open(browser_log, 'r') as f:
                allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.try_to_login(email=EMAIL, password=PASSWORD, timeout=15)

        return DashboardPage(self.driver)
