import os.path
import pytest

from base import Base
from utils import functions


class TestNegativeLogin(Base):

    @pytest.mark.UI
    def test_uncorrect_credentials(self):
        self.login_page.try_to_login(
            email=functions.random_str(digits=False, email=True),
            password=functions.random_str(str_length=15),
            timeout=25
        )
        self.login_page.is_visible(self.login_page.locators.INVALID_LOGIN_OR_PWD_MESSAGE_LOCATOR)

    @pytest.mark.UI
    def test_uncorrect_email(self):
        self.login_page.try_to_login(
            email=functions.random_str(digits=False),
            password=functions.random_str(str_length=15),
            timeout=25
        )
        self.login_page.is_visible(self.login_page.locators.UNCORRECT_EMAIL_MESSAGE_LOCATOR)


class TestUI(Base):

    authorize = True

    @pytest.mark.UI
    def test_create_campaign(self, root_dir):
        campaign_name = functions.random_str(str_length=15)

        new_dashboard_page = self.dashboard_page.create_new_campaign(
            main_url=functions.random_str(str_length=8, url=True),
            campaign_name=campaign_name,
            picture_path=os.path.join(root_dir, 'data', 'banner_picture.png'),
            timeout=15
        )

        assert campaign_name in new_dashboard_page.campaigns_list()

    @pytest.mark.UI
    def test_create_segment(self):
        segments_list_page = self.dashboard_page.click_on_tab('segments')
        segment_name = functions.random_str(str_length=10)

        with segments_list_page.new_segment(segment_name=segment_name, timeout=15) as seg_list_page:
            assert segment_name in seg_list_page.segments_list()

    @pytest.mark.UI
    def test_delete_segment(self):
        segments_list_page = self.dashboard_page.click_on_tab('segments')
        segment_name = functions.random_str(str_length=10)

        with segments_list_page.new_segment(segment_name=segment_name, timeout=15):
            pass
