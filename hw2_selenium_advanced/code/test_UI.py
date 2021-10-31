import os.path

import pytest

from time import sleep

from selenium.webdriver.common.by import By

from base import Base
from utils import functions


class TestNegativeLogin(Base):

    @pytest.mark.skip
    @pytest.mark.UI
    def test_uncorrect_credentials(self):
        # self.login_page.try_to_login(email='vasya_pupkin@mail.ru', password='1234567890')
        # assert "Error" in self.driver.page_source  # BAD!!!
        pass

    @pytest.mark.skip
    @pytest.mark.UI
    def test_some_neg_login(self):  # ???
        pass


class TestUI(Base):

    @pytest.mark.UI
    def test_create_campaign(self, login, root_dir):
        create_campaign_page = login.create_new_campaign()

        campaign_name = functions.random_str(str_length=15)

        dashboard_page = create_campaign_page.create_new_traffic_banner(
            main_url=functions.random_str(str_length=8) + '.ru',
            campaign_name=campaign_name,
            banner_picture_path=os.path.join(root_dir, 'data', 'banner_picture.png'),
            timeout=10
        )

        dashboard_page.find(
            (
                dashboard_page.locators.COMPANY_HREF_LOCATOR_TEMPLATE[0],
                dashboard_page.locators.COMPANY_HREF_LOCATOR_TEMPLATE[1].format(campaign_name)
            )
        )

    @pytest.mark.UI
    def test_create_segment(self, login):
        segments_list_page = login.click_on_tab('segments')

        segment_name = functions.random_str(str_length=10)
        segments_list_page.create_new_segment(
            segment_name=segment_name,
            timeout=5
        )

        segments_list_page.find(
            (
                segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[0],
                segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[1].format(segment_name)
            )
        )

    @pytest.mark.UI
    def test_delete_segment(self, login):
        segments_list_page = login.click_on_tab('segments')

        segment_name = functions.random_str(str_length=10)

        segments_list_page.create_new_segment(
            segment_name=segment_name,
            timeout=5
        )

        segments_list_page.remove_segment(segment_name)

        from selenium.common.exceptions import TimeoutException
        with pytest.raises(TimeoutException):
            self.driver.refresh()
            segments_list_page.find(
                locator=(
                    segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[0],
                    segments_list_page.locators.SEGMENT_LINK_LOCATOR_TEMPLATE[1].format(segment_name)
                ),
                timeout=1
            )
