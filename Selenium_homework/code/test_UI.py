import pytest
from base import Base


class TestUI(Base):
    @pytest.mark.UI
    def test_login(self):
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    @pytest.mark.UI
    def test_logout(self):
        self.header_page.click_on_logout_button()
        assert self.driver.current_url == 'https://target.my.com/'

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'tab_name, url',
        [
            pytest.param('profile', 'https://target.my.com/profile'),
            pytest.param('statistics', 'https://target.my.com/statistics')
        ]
    )
    def test_tabs_navigation(self, tab_name, url):
        self.header_page.click_on_tab(tab_name)
        assert self.driver.current_url.startswith(url)

    @pytest.mark.UI
    def test_change_profile_information(self, r_number):
        self.header_page.click_on_tab('profile')

        self.profile_page.fill_contact_information(fio='test' + r_number, phone=r_number)

        self.driver.refresh()

        fio = self.profile_page.find(self.profile_page.locators.FIO_FIELD_LOCATOR)
        phone = self.profile_page.find(self.profile_page.locators.PHONE_FIELD_LOCATOR)

        assert fio.get_attribute('value') == 'test' + r_number and phone.get_attribute('value') == r_number
