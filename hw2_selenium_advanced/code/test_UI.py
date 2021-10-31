import os.path
import pytest

from selenium.common.exceptions import TimeoutException
from base import Base
from utils import functions


class TestNegativeLogin(Base):

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_uncorrect_credentials(self):
        self.login_page.try_to_login(
            email=functions.random_str(digits=False) + '@mail.ru',
            password=functions.random_str(str_length=15),
            timeout=25
        )
        self.login_page.find(self.login_page.locators.INVALID_LOGIN_OR_PWD_MESSAGE_LOCATOR)

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_uncorrect_email(self):
        self.login_page.try_to_login(
            email=functions.random_str(digits=False),
            password=functions.random_str(str_length=15),
            timeout=25
        )
        self.login_page.find(self.login_page.locators.UNCORRECT_EMAIL_MESSAGE_LOCATOR)


class TestUI(Base):

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_create_campaign(self, login, root_dir):
        campaign_name = functions.random_str(str_length=15)

        dashboard_page = login.create_new_campaign(
            main_url=functions.random_str(str_length=8) + '.ru',
            campaign_name=campaign_name,
            picture_path=os.path.join(root_dir, 'data', 'banner_picture.png'),
            timeout=15
        )

        dashboard_page.find(
            (
                dashboard_page.locators.COMPANY_HREF_LOCATOR_TEMPLATE[0],
                dashboard_page.locators.COMPANY_HREF_LOCATOR_TEMPLATE[1].format(campaign_name)
            )
        )

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_create_segment(self, login):
        segments_list_page = login.click_on_tab('segments')

        segment_name = functions.random_str(str_length=10)
        segments_list_page.create_new_segment(
            segment_name=segment_name,
            timeout=15
        )

        segments_list_page.find(
            (
                segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[0],
                segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[1].format(segment_name)
            )
        )

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_delete_segment(self, login):
        segments_list_page = login.click_on_tab('segments')

        segment_name = functions.random_str(str_length=10)

        segments_list_page.create_new_segment(
            segment_name=segment_name,
            timeout=15
        )

        segments_list_page.remove_segment(segment_name)

        with pytest.raises(TimeoutException):
            self.driver.refresh()
            segments_list_page.find(
                locator=(
                    segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[0],
                    segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[1].format(segment_name)
                ),
                timeout=1
            )
