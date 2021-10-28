from time import sleep

import pytest
from base import Base


class TestUI(Base):

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'tab_name, url',
        [
            pytest.param('profile', 'https://target.my.com/profile'),
            pytest.param('statistics', 'https://target.my.com/statistics')
        ]
    )
    def test_tabs_navigation(self, tab_name, url, login):
        header_page = login
        header_page.click_on_tab(tab_name)
        assert self.driver.current_url.startswith(url)


    def test_123(self):
        print("no login test")
        sleep(5)
        assert 1 + 2 == 3